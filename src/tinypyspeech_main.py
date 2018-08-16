import wx
import sys, os
sys.path.append(os.path.abspath("../gui"))
import tinypyspeech_win
import numpy
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure

import wave

MAX_AUDIO_CHANNEL = 8
#unit: inch
PLOT_PANEL_WIDTH = 720
PLOT_PANEL_HEIGHT = 360
#unit: percent
PLOT_AXES_WIDTH_TITLE = 0.05
PLOT_AXES_HEIGHT_LABEL = 0.075

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

    def readWave(self, wavPath):
        if os.path.isfile(wavPath):
            # Open the wav file to get wave data and parameters
            wavFile =  wave.open(wavPath, "rb")
            wavParams = wavFile.getparams()
            wavChannels = wavParams[0]
            wavFramerate = wavParams[2]
            wavFrames = wavParams[3]
            wavData = wavFile.readframes(wavFrames)
            wavFile.close()
            # Transpose the wav data if wave has multiple channels
            retData = numpy.fromstring(wavData, dtype = numpy.short)
            retData.shape = -1, 2
            retData = retData.T
            # Calculate and arange wave time
            retTime = numpy.arange(0, wavFrames) * (1.0 / wavFramerate)
            retChannels = wavChannels
            return retChannels, retData, retTime
        else:
            return 0, 0, 0

    def showWave(self, wavPath):
        self.wavFigure.clear()
        waveChannels, waveData, waveTime = self.readWave(wavPath)
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
                wavAxes = self.wavFigure.add_axes([left, bottom, width, height], facecolor='k')
                wavAxes.set_prop_cycle(color='#00F279', lw=[1])
                wavAxes.set_xlabel('time (s)', color='w')
                wavAxes.set_ylabel('value', color='w')
                wavAxes.plot(waveTime, waveData[i])
                wavAxes.tick_params(labelcolor='w')
                wavAxes.set_title('Audio Channel ' + str(i), color='w')
            # Note!!!: draw() must be called if figure has been cleared once
            self.wavCanvas.draw()

class mainWin(tinypyspeech_win.speech_win):

    def __init__(self, parent):
        tinypyspeech_win.speech_win.__init__(self, parent)
        self.wavPanel = wavCanvasPanel(self.m_panel_plot)
        self.m_genericDirCtrl_audioDir.SetFilter("Audio files (*.wav)|*.wav")

    def viewAudio( self, event ):
        self.wavPath =  self.m_genericDirCtrl_audioDir.GetFilePath()
        self.wavPanel.showWave(self.wavPath)

if __name__ == '__main__':
    app = wx.App()

    main_win = mainWin(None)
    main_win.SetTitle(u"tinyPySPEECH v0.1.1")
    main_win.Show()

    app.MainLoop()
