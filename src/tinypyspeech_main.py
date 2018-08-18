import wx
import sys, os
sys.path.append(os.path.abspath("../gui"))
import tinypyspeech_win
import numpy
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

import wave
import pyaudio

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

    def readWave(self, wavPath, wavInfo):
        if os.path.isfile(wavPath):
            # Open the wav file to get wave data and parameters
            wavFile =  wave.open(wavPath, "rb")
            wavParams = wavFile.getparams()
            wavChannels = wavParams[0]
            wavFramerate = wavParams[2]
            wavFrames = wavParams[3]
            wavInfo.Clear()
            wavInfo.write('Channels:' + str(wavChannels))
            wavInfo.write(', SampWidth:' + str(wavParams[1]) + 'Byte')
            wavInfo.write(', SampRate:' + str(wavParams[2]) + 'kHz')
            wavInfo.write(', FormatTag:' + wavParams[4])
            wavData = wavFile.readframes(wavFrames)
            wavFile.close()
            # Transpose the wav data if wave has multiple channels
            retData = numpy.fromstring(wavData, dtype = numpy.short)
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

class mainWin(tinypyspeech_win.speech_win):

    def __init__(self, parent):
        tinypyspeech_win.speech_win.__init__(self, parent)
        self.wavPanel = wavCanvasPanel(self.m_panel_plot)
        self.m_genericDirCtrl_audioDir.SetFilter("Audio files (*.wav)|*.wav")
        self.isRecording = False
        # Start -> Play -> Pause -> Resume -> End
        self.playState = AUDIO_PLAY_STATE_START

    def viewAudio( self, event ):
        self.wavPath =  self.m_genericDirCtrl_audioDir.GetFilePath()
        self.wavPanel.showWave(self.wavPath, self.m_textCtrl_audioInfo)
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
            fileName = self.m_textCtrl_fileName.GetLineText(0)
            if fileName == '':
                fileName = 'Untitled 1'
            self.wavPath = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'audio', 'record', fileName+'.wav')
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

if __name__ == '__main__':
    app = wx.App()

    main_win = mainWin(None)
    main_win.SetTitle(u"tinyPySPEECH v0.5.0")
    main_win.Show()

    app.MainLoop()
