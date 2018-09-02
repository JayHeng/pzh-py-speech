# -*- coding: utf-8 -*
import wx
import sys, os
reload(sys)
sys.setdefaultencoding('utf-8')
import subprocess
sys.path.append(os.path.abspath("../gui"))
import jayspyspeech_win
import numpy
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.tri as Tri

import wave
import pyaudio
import speech_recognition
import pyttsx3

MAX_AUDIO_CHANNEL = 8
#unit: inch
PLOT_PANEL_WIDTH = 720
PLOT_PANEL_HEIGHT = 360
#unit: percent
PLOT_AXES_WIDTH_TITLE = 0.05
PLOT_AXES_HEIGHT_LABEL = 0.075
AUDIO_CHUNK_SIZE = 1024

AUDIO_PLAY_STATE_START = 0
AUDIO_PLAY_STATE_PLAY = 1
AUDIO_PLAY_STATE_PAUSE = 2
AUDIO_PLAY_STATE_RESUME = 3
AUDIO_PLAY_STATE_END = 4

class wavCursor(object):
    def __init__(self, ax, x, y):
        self.ax = ax
        self.vline = ax.axvline(color='r', alpha=1)
        self.hline = ax.axhline(color='r', alpha=1)
        self.marker, = ax.plot([0],[0], marker="o", color="crimson", zorder=3)
        self.x = x
        self.y = y
        self.xlim = self.x[len(self.x)-1]
        self.text = ax.text(0.7, 0.9, '', bbox=dict(facecolor='red', alpha=0.5))

    def moveMouse(self, event):
        if not event.inaxes:
            return
        x, y = event.xdata, event.ydata
        if x > self.xlim:
            x = self.xlim
        index = numpy.searchsorted(self.x, [x])[0]
        x = self.x[index]
        y = self.y[index]
        self.vline.set_xdata(x)
        self.hline.set_ydata(y)
        self.marker.set_data([x],[y])
        self.text.set_text('x=%1.2f, y=%1.2f' % (x, y))
        self.text.set_position((x,y))
        self.ax.figure.canvas.draw_idle()

class wavCanvasPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        dpi = 60
        width = PLOT_PANEL_WIDTH / dpi
        height = PLOT_PANEL_HEIGHT / dpi
        self.wavFigure = Figure(figsize=[width,height], dpi=dpi, facecolor='#404040')
        self.wavCanvas = FigureCanvas(self, -1, self.wavFigure)
        self.wavSizer = wx.BoxSizer(wx.VERTICAL)
        self.wavSizer.Add(self.wavCanvas, 1, wx.EXPAND|wx.ALL)
        self.SetSizerAndFit(self.wavSizer)
        self.wavAxes = [None] * MAX_AUDIO_CHANNEL
        self.wavCursor = [None] * MAX_AUDIO_CHANNEL

    def fromstring(self, wavData, alignedByte):
        if alignedByte <= 8:
            src = numpy.ndarray(len(wavData), numpy.dtype('>i1'), wavData)
            dest = numpy.zeros(len(wavData) / alignedByte, numpy.dtype('>i8'))
            for i in range(alignedByte):
                dest.view(dtype='>i1')[alignedByte-1-i::8] = src.view(dtype='>i1')[i::alignedByte]
            [hex(x) for x in dest]
            return True, dest
        else:
            return False, wavData

    def readWave(self, wavPath, wavInfo):
        if os.path.isfile(wavPath):
            # Open the wav file to get wave data and parameters
            wavFile =  wave.open(wavPath, "rb")
            wavParams = wavFile.getparams()
            wavChannels = wavParams[0]
            wavSampwidth = wavParams[1]
            wavFramerate = wavParams[2]
            wavFrames = wavParams[3]
            wavInfo.SetStatusText('Opened Audio Info = ' +
                                  'Channels:' + str(wavChannels) +
                                  ', SampWidth:' + str(wavSampwidth) + 'Byte' +
                                  ', SampRate:' + str(wavFramerate) + 'kHz' +
                                  ', FormatTag:' + wavParams[4])
            wavData = wavFile.readframes(wavFrames)
            wavFile.close()
            # Transpose the wav data if wave has multiple channels
            if wavSampwidth == 1:
                dtype = numpy.int8
            elif wavSampwidth == 2:
                dtype = numpy.int16
            elif wavSampwidth == 3:
                dtype = None
            elif wavSampwidth == 4:
                dtype = numpy.float32
            else:
                return 0, 0, 0
            if dtype != None:
                retData = numpy.fromstring(wavData, dtype = dtype)
            else:
                # Implement int24 manually
                status, retData = self.fromstring(wavData, 3)
                if not status:
                    return 0, 0, 0
            if wavChannels != 1:
                retData.shape = -1, wavChannels
                retData = retData.T
            # Calculate and arange wave time
            retTime = numpy.arange(0, wavFrames) * (1.0 / wavFramerate)
            retChannels = wavChannels
            return retChannels, retData, retTime
        else:
            return 0, 0, 0

    def showWave(self, wavPath, wavInfo):
        self.wavFigure.clear()
        waveChannels, waveData, waveTime = self.readWave(wavPath, wavInfo)
        if waveChannels != 0:
            # Note: only show max supported channel if actual channel > max supported channel
            if waveChannels > MAX_AUDIO_CHANNEL:
                waveChannels = MAX_AUDIO_CHANNEL
            # Polt the waveform of each channel in sequence
            for i in range(waveChannels):
                left = PLOT_AXES_HEIGHT_LABEL
                bottom = (1.0 / waveChannels) * (waveChannels - 1 - i) + PLOT_AXES_HEIGHT_LABEL
                height = 1.0 / waveChannels - (PLOT_AXES_WIDTH_TITLE + PLOT_AXES_HEIGHT_LABEL)
                width = 1 - left - 0.05
                self.wavAxes[i] = self.wavFigure.add_axes([left, bottom, width, height], facecolor='k')
                self.wavAxes[i].set_prop_cycle(color='#00F279', lw=[1])
                self.wavAxes[i].set_xlabel('time (s)', color='w')
                self.wavAxes[i].set_ylabel('value', color='w')
                if waveChannels == 1:
                    data = waveData
                else:
                    data = waveData[i]
                self.wavAxes[i].plot(waveTime, data)
                self.wavAxes[i].grid()
                self.wavAxes[i].tick_params(labelcolor='w')
                self.wavAxes[i].set_title('Audio Channel ' + str(i), color='w')
                self.wavCursor[i] = wavCursor(self.wavAxes[i], waveTime, data)
                self.wavCanvas.mpl_connect('motion_notify_event', self.wavCursor[i].moveMouse)
        # Note!!!: draw() must be called if figure has been cleared once
        self.wavCanvas.draw()

    def showWelcome (self):
        self.wavFigure.clear()
        # Get Code from below link
        # https://matplotlib.org/gallery/images_contours_and_fields/tripcolor_demo.html#sphx-glr-gallery-images-contours-and-fields-tripcolor-demo-py
        n_angles = 36
        n_radii = 8
        min_radius = 0.25
        radii = numpy.linspace(min_radius, 0.95, n_radii)
        angles = numpy.linspace(0, 2 * numpy.pi, n_angles, endpoint=False)
        angles = numpy.repeat(angles[..., numpy.newaxis], n_radii, axis=1)
        angles[:, 1::2] += numpy.pi / n_angles
        x = (radii * numpy.cos(angles)).flatten()
        y = (radii * numpy.sin(angles)).flatten()
        z = (numpy.cos(radii) * numpy.cos(3 * angles)).flatten()
        triang = Tri.Triangulation(x, y)
        triang.set_mask(numpy.hypot(x[triang.triangles].mean(axis=1),
                                    y[triang.triangles].mean(axis=1))
                        < min_radius)
        welcomeAxes = self.wavFigure.add_axes([0.13,0.2,0.7,0.7], facecolor='#404040')
        #welcomeAxes.set_aspect('equal')
        welcomeAxes.tripcolor(triang, z, shading='flat')
        # Set some properties
        welcomeAxes.set_title('Welcome to use JaysPySPEECH', color='w')
        welcomeAxes.set_xticks([])
        welcomeAxes.set_yticks([])
        welcomeAxes.spines['top'].set_visible(False)
        welcomeAxes.spines['right'].set_visible(False)
        welcomeAxes.spines['bottom'].set_visible(False)
        welcomeAxes.spines['left'].set_visible(False)
        self.wavCanvas.draw()

class mainWin(jayspyspeech_win.speech_win):

    def __init__(self, parent):
        jayspyspeech_win.speech_win.__init__(self, parent)
        icon = wx.Icon()
        icon.CopyFromBitmap(wx.Bitmap( u"../img/jayspyspeech.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(icon)
        self.wavPanel = wavCanvasPanel(self.m_panel_plot)
        self.m_genericDirCtrl_audioDir.SetFilter("Audio files (*.wav)|*.wav")
        self.isRecording = False
        # Start -> Play -> Pause -> Resume -> End
        self.playState = AUDIO_PLAY_STATE_START
        self.statusBar.SetFieldsCount(1)
        self.wavPanel.showWelcome()
        self.ttsObj = None

    def viewAudio( self, event ):
        self.wavPath =  self.m_genericDirCtrl_audioDir.GetFilePath()
        self.wavPanel.showWave(self.wavPath, self.statusBar)
        if self.playState != AUDIO_PLAY_STATE_START:
            self.playState = AUDIO_PLAY_STATE_END
            self.m_button_play.SetLabel('Play Start')

    def recordAudioCallback(self, in_data, frame_count, time_info, status):
        if not self.isRecording:
            status = pyaudio.paComplete
        else:
            self.wavFrames.append(in_data)
            status = pyaudio.paContinue
        return (in_data, status)

    def recordAudio( self, event ):
        if not self.isRecording:
            self.isRecording = True
            self.m_button_record.SetLabel('Record Stop')
            # Get the wave parameter from user settings
            fileName = self.m_textCtrl_recFileName.GetLineText(0)
            if fileName == '':
                fileName = 'rec_untitled1.wav'
            self.wavPath = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'conv', 'rec', fileName)
            self.wavSampRate = int(self.m_choice_sampRate.GetString(self.m_choice_sampRate.GetSelection()))
            channels = self.m_choice_channels.GetString(self.m_choice_channels.GetSelection())
            if channels == 'Mono':
                self.wavChannels = 1
            else: #if channels == 'Stereo':
                self.wavChannels = 2
            bitDepth = int(self.m_choice_bitDepth.GetString(self.m_choice_bitDepth.GetSelection()))
            if bitDepth == 8:
                self.wavBitFormat = pyaudio.paInt8
            elif bitDepth == 24:
                self.wavBitFormat = pyaudio.paInt24
            elif bitDepth == 32:
                self.wavBitFormat = pyaudio.paFloat32
            else:
                self.wavBitFormat = pyaudio.paInt16
            # Record audio according to wave parameters
            self.wavFrames = []
            self.wavPyaudio = pyaudio.PyAudio()
            self.wavStream = self.wavPyaudio.open(format=self.wavBitFormat,
                                                  channels=self.wavChannels,
                                                  rate=self.wavSampRate,
                                                  input=True,
                                                  frames_per_buffer=AUDIO_CHUNK_SIZE,
                                                  stream_callback=self.recordAudioCallback)
            self.wavStream.start_stream()
        else:
            self.isRecording = False
            self.m_button_record.SetLabel('Record Start')
            self.wavStream.stop_stream()
            self.wavStream.close()
            self.wavPyaudio.terminate()
            # Save the wave data into file
            wavFile = wave.open(self.wavPath, 'wb')
            wavFile.setnchannels(self.wavChannels)
            wavFile.setsampwidth(self.wavPyaudio.get_sample_size(self.wavBitFormat))
            wavFile.setframerate(self.wavSampRate)
            wavFile.writeframes(b''.join(self.wavFrames))
            wavFile.close()

    def playAudioCallback(self, in_data, frame_count, time_info, status):
        if self.playState == AUDIO_PLAY_STATE_PLAY or self.playState == AUDIO_PLAY_STATE_RESUME:
            data = self.wavFile.readframes(frame_count)
            if self.wavFile.getnframes() == self.wavFile.tell():
                status = pyaudio.paComplete
                self.playState = AUDIO_PLAY_STATE_END
                self.m_button_play.SetLabel('Play Start')
            else:
                status = pyaudio.paContinue
            return (data, status)
        else:
            # Note!!!:
            data = numpy.zeros(frame_count*self.wavFile.getnchannels()).tostring()
            return (data, pyaudio.paContinue)

    def playAudio( self, event ):
        if os.path.isfile(self.wavPath):
            if self.playState == AUDIO_PLAY_STATE_END:
                self.playState = AUDIO_PLAY_STATE_START
                self.wavStream.stop_stream()
                self.wavStream.close()
                self.wavPyaudio.terminate()
                self.wavFile.close()
            if self.playState == AUDIO_PLAY_STATE_START:
                self.playState = AUDIO_PLAY_STATE_PLAY
                self.m_button_play.SetLabel('Play Pause')
                self.wavFile =  wave.open(self.wavPath, "rb")
                self.wavPyaudio = pyaudio.PyAudio()
                self.wavStream = self.wavPyaudio.open(format=self.wavPyaudio.get_format_from_width(self.wavFile.getsampwidth()),
                                                      channels=self.wavFile.getnchannels(),
                                                      rate=self.wavFile.getframerate(),
                                                      output=True,
                                                      stream_callback=self.playAudioCallback)
                self.wavStream.start_stream()
            elif self.playState == AUDIO_PLAY_STATE_PLAY or self.playState == AUDIO_PLAY_STATE_RESUME:
                self.playState = AUDIO_PLAY_STATE_PAUSE
                self.m_button_play.SetLabel('Play Resume')
            elif self.playState == AUDIO_PLAY_STATE_PAUSE:
                self.playState = AUDIO_PLAY_STATE_RESUME
                self.m_button_play.SetLabel('Play Pause')
            else:
                pass

    def getLanguageSelection(self):
        languageType = self.m_choice_lang.GetString(self.m_choice_lang.GetSelection())
        if languageType == 'Mandarin Chinese':
            languageType = 'zh-CN'
            languageName = 'Chinese'
        else: # languageType == 'US English':
            languageType = 'en-US'
            languageName = 'English'
        return languageType, languageName

    def audioSpeechRecognition( self, event ):
        if os.path.isfile(self.wavPath):
            asrObj = speech_recognition.Recognizer()
            with speech_recognition.AudioFile(self.wavPath) as source:
                # Read the entire audio file
                speechAudio = asrObj.record(source)
            self.m_textCtrl_asrttsText.Clear()
            # Get language type
            languageType, languageName = self.getLanguageSelection()
            engineType = self.m_choice_asrEngine.GetString(self.m_choice_asrEngine.GetSelection())
            if engineType == 'CMU Sphinx':
                # Recognize speech using Sphinx
                try:
                    speechText = asrObj.recognize_sphinx(speechAudio, language=languageType)
                    self.m_textCtrl_asrttsText.write(speechText)
                    self.statusBar.SetStatusText("ASR Conversation Info: Successfully")
                    fileName = self.m_textCtrl_asrFileName.GetLineText(0)
                    if fileName == '':
                        fileName = 'asr_untitled1.txt'
                    asrFilePath = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'conv', 'asr', fileName)
                    asrFileObj = open(asrFilePath, 'wb')
                    asrFileObj.write(speechText)
                    asrFileObj.close()
                except speech_recognition.UnknownValueError:
                    self.statusBar.SetStatusText("ASR Conversation Info: Sphinx could not understand audio")
                except speech_recognition.RequestError as e:
                    self.statusBar.SetStatusText("ASR Conversation Info: Sphinx error; {0}".format(e))
            else:
                self.statusBar.SetStatusText("ASR Conversation Info: Unavailable ASR Engine")

    def refreshVoice( self, event ):
        languageType, languageName = self.getLanguageSelection()
        engineType = self.m_choice_ttsEngine.GetString(self.m_choice_ttsEngine.GetSelection())
        if engineType == 'pyttsx3 - SAPI5':
            if self.ttsObj == None:
                 self.ttsObj = pyttsx3.init()
            voices = self.ttsObj.getProperty('voices')
            voiceItems = [None] * len(voices)
            itemIndex = 0
            for voice in voices:
                voiceId = voice.id.lower()
                voiceName = voice.name.lower()
                if (voiceId.find(languageType.lower()) != -1) or (voiceName.find(languageName.lower()) != -1):
                    voiceItems[itemIndex] = voice.name
                    itemIndex += 1
            voiceItems = voiceItems[0:itemIndex]
            self.m_choice_voice.Clear()
            self.m_choice_voice.SetItems(voiceItems)
        else:
            voiceItem = ['N/A']
            self.m_choice_voice.Clear()
            self.m_choice_voice.SetItems(voiceItem)

    def textToWav(self, text, language):
        fileName = self.m_textCtrl_ttsFileName.GetLineText(0)
        if fileName == '':
            fileName = 'tts_untitled1.wav'
        ttsFilePath = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'conv', 'tts', fileName)
        ttwEngineType = self.m_choice_ttwEngine.GetString(self.m_choice_ttwEngine.GetSelection())
        if ttwEngineType == 'eSpeak TTS':
            ttsTextFile = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'ttsTextTemp.txt')
            ttsTextFileObj = open(ttsTextFile, 'wb')
            ttsTextFileObj.write(text)
            ttsTextFileObj.close()
            try:
                #espeak_path = "C:/tools_mcu/eSpeak/command_line/espeak.exe"
                #subprocess.call([espeak_path, "-v"+languageType[0:2], text])
                gender = self.m_choice_gender.GetString(self.m_choice_gender.GetSelection())
                gender = gender.lower()[0] + '3'
                subprocess.call(["espeak", "-v"+language[0:2]+'+'+gender, "-f"+ttsTextFile, "-w"+ttsFilePath])
            except:
                self.statusBar.SetStatusText("TTW Conversation Info: eSpeak is not installed or its path is not added into system environment")
            os.remove(ttsTextFile)
        else:
            self.statusBar.SetStatusText("TTW Conversation Info: Unavailable TTW Engine")

    def textToSpeech( self, event ):
        languageType, languageName = self.getLanguageSelection()
        # Get text from m_textCtrl_asrttsText
        lines = self.m_textCtrl_asrttsText.GetNumberOfLines()
        if lines != 0:
            data = ''
            for i in range(0, lines):
                data += self.m_textCtrl_asrttsText.GetLineText(i)
        else:
            return
        ttsEngineType = self.m_choice_ttsEngine.GetString(self.m_choice_ttsEngine.GetSelection())
        if ttsEngineType == 'pyttsx3 - SAPI5':
            if self.ttsObj == None:
                 self.ttsObj = pyttsx3.init()
            hasVoice = False
            voices = self.ttsObj.getProperty('voices')
            voiceSel = self.m_choice_voice.GetString(self.m_choice_voice.GetSelection())
            for voice in voices:
                #print ('id = {} \nname = {} \nlanguages = {} \n'.format(voice.id, voice.name, voice.languages))
                voiceId = voice.id.lower()
                voiceName = voice.name.lower()
                if (voiceId.find(languageType.lower()) != -1) or (voiceName.find(languageName.lower()) != -1):
                    if (voiceSel == '') or (voiceSel == voice.name):
                        hasVoice = True
                        break
            if hasVoice:
                self.ttsObj.setProperty('voice', voice.id)
                self.ttsObj.say(data)
                self.statusBar.SetStatusText("TTS Conversation Info: Run and Wait")
                self.ttsObj.runAndWait()
                self.statusBar.SetStatusText("TTS Conversation Info: Successfully")
            else:
                self.statusBar.SetStatusText("TTS Conversation Info: Language is not supported by current PC")
            self.textToWav(data, languageType)
        else:
            self.statusBar.SetStatusText("TTS Conversation Info: Unavailable TTS Engine")

    def clearAsrTtsText( self, event ):
        self.m_textCtrl_asrttsText.Clear()

    def showHomepageInfo( self, event ):
        messageText = (('Code: \n    https://github.com/JayHeng/JaysPySPEECH.git \n') +
                       ('Doc: \n    https://www.cnblogs.com/henjay724/p/9541867.html \n'))
        wx.MessageBox(messageText, "Homepage", wx.OK | wx.ICON_INFORMATION)

    def showAboutInfo( self, event ):
        messageText = (('Author: Jay Heng \n') +
                       ('Email: hengjie1989@foxmail.com \n'))
        wx.MessageBox(messageText, "About", wx.OK | wx.ICON_INFORMATION)

if __name__ == '__main__':
    app = wx.App()

    main_win = mainWin(None)
    main_win.SetTitle(u"JaysPySPEECH v1.0.0")
    main_win.Show()

    app.MainLoop()
