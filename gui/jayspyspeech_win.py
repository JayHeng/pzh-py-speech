# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jul 11 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class speech_win
###########################################################################

class speech_win ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"JaysPySPEECH", pos = wx.DefaultPosition, size = wx.Size( 942,694 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 64, 64, 64 ) )

		self.menubar = wx.MenuBar( 0 )
		self.m_menu_help = wx.Menu()
		self.m_menuItem_homePage = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"Home Page", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.Append( self.m_menuItem_homePage )

		self.m_menuItem_about = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"About Author", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.Append( self.m_menuItem_about )

		self.menubar.Append( self.m_menu_help, u"Help" )

		self.SetMenuBar( self.menubar )

		win_sizer = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		edit_win = wx.BoxSizer( wx.VERTICAL )

		dir_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_selectAudioFile = wx.StaticText( self, wx.ID_ANY, u"Select Audio File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_selectAudioFile.Wrap( -1 )

		self.m_staticText_selectAudioFile.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		dir_win.Add( self.m_staticText_selectAudioFile, 0, wx.ALL, 5 )

		self.m_genericDirCtrl_audioDir = wx.GenericDirCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 180,250 ), wx.DIRCTRL_SHOW_FILTERS|wx.HSCROLL, wx.EmptyString, 0 )

		self.m_genericDirCtrl_audioDir.ShowHidden( False )
		self.m_genericDirCtrl_audioDir.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_genericDirCtrl_audioDir.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		dir_win.Add( self.m_genericDirCtrl_audioDir, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText_null0 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_staticText_null0.Wrap( -1 )

		dir_win.Add( self.m_staticText_null0, 0, wx.ALL, 5 )

		self.m_button_play = wx.Button( self, wx.ID_ANY, u"Play Start", wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
		dir_win.Add( self.m_button_play, 0, wx.ALL, 5 )


		edit_win.Add( dir_win, 1, wx.EXPAND, 5 )

		rec_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_null1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_null1.Wrap( -1 )

		rec_win.Add( self.m_staticText_null1, 0, wx.ALL, 5 )

		self.m_staticText_recordAudioFile = wx.StaticText( self, wx.ID_ANY, u"Record Audio File:", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.m_staticText_recordAudioFile.Wrap( -1 )

		self.m_staticText_recordAudioFile.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		rec_win.Add( self.m_staticText_recordAudioFile, 0, wx.ALL, 5 )

		self.m_staticText_channels = wx.StaticText( self, wx.ID_ANY, u"Channels:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText_channels.Wrap( -1 )

		self.m_staticText_channels.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		rec_win.Add( self.m_staticText_channels, 0, wx.ALL, 5 )

		m_choice_channelsChoices = [ u"Mono", u"Stereo" ]
		self.m_choice_channels = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_channelsChoices, 0 )
		self.m_choice_channels.SetSelection( 1 )
		rec_win.Add( self.m_choice_channels, 0, wx.ALL, 5 )

		self.m_staticText_sampRate = wx.StaticText( self, wx.ID_ANY, u"Samp Rate:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText_sampRate.Wrap( -1 )

		self.m_staticText_sampRate.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		rec_win.Add( self.m_staticText_sampRate, 0, wx.ALL, 5 )

		m_choice_sampRateChoices = [ u"44100", u"22050", u"16000", u"11025" ]
		self.m_choice_sampRate = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_sampRateChoices, 0 )
		self.m_choice_sampRate.SetSelection( 0 )
		rec_win.Add( self.m_choice_sampRate, 0, wx.ALL, 5 )

		self.m_staticText_hz = wx.StaticText( self, wx.ID_ANY, u"Hz", wx.DefaultPosition, wx.Size( 20,-1 ), 0 )
		self.m_staticText_hz.Wrap( -1 )

		self.m_staticText_hz.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		rec_win.Add( self.m_staticText_hz, 0, wx.ALL, 5 )

		self.m_staticText_bitDepth = wx.StaticText( self, wx.ID_ANY, u"Bit Depth:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText_bitDepth.Wrap( -1 )

		self.m_staticText_bitDepth.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		rec_win.Add( self.m_staticText_bitDepth, 0, wx.ALL, 5 )

		m_choice_bitDepthChoices = [ u"8", u"16", u"24", u"32" ]
		self.m_choice_bitDepth = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_bitDepthChoices, 0 )
		self.m_choice_bitDepth.SetSelection( 1 )
		rec_win.Add( self.m_choice_bitDepth, 0, wx.ALL, 5 )

		self.m_staticText_bits = wx.StaticText( self, wx.ID_ANY, u"bits", wx.DefaultPosition, wx.Size( 20,-1 ), 0 )
		self.m_staticText_bits.Wrap( -1 )

		self.m_staticText_bits.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		rec_win.Add( self.m_staticText_bits, 0, wx.ALL, 5 )

		self.m_staticText_recFileName = wx.StaticText( self, wx.ID_ANY, u"File:", wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_staticText_recFileName.Wrap( -1 )

		self.m_staticText_recFileName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		rec_win.Add( self.m_staticText_recFileName, 0, wx.ALL, 5 )

		self.m_textCtrl_recFileName = wx.TextCtrl( self, wx.ID_ANY, u"rec_untitled1.wav", wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
		rec_win.Add( self.m_textCtrl_recFileName, 0, wx.ALL, 5 )

		self.m_staticText_null2 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_staticText_null2.Wrap( -1 )

		rec_win.Add( self.m_staticText_null2, 0, wx.ALL, 5 )

		self.m_button_record = wx.Button( self, wx.ID_ANY, u"Record Start", wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
		rec_win.Add( self.m_button_record, 0, wx.ALL, 5 )


		edit_win.Add( rec_win, 1, wx.EXPAND, 5 )


		win_sizer.Add( edit_win, 1, wx.EXPAND, 5 )

		show_win = wx.BoxSizer( wx.VERTICAL )

		plot_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_showAudioFile = wx.StaticText( self, wx.ID_ANY, u"Show Audio File:", wx.DefaultPosition, wx.Size( 215,-1 ), 0 )
		self.m_staticText_showAudioFile.Wrap( -1 )

		self.m_staticText_showAudioFile.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		plot_win.Add( self.m_staticText_showAudioFile, 0, wx.ALL, 5 )

		self.m_staticText_domain = wx.StaticText( self, wx.ID_ANY, u"Domain:", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.m_staticText_domain.Wrap( -1 )

		self.m_staticText_domain.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		plot_win.Add( self.m_staticText_domain, 0, wx.ALL, 5 )

		m_choice_domainChoices = [ u"Time", u"Frequency" ]
		self.m_choice_domain = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_domainChoices, 0 )
		self.m_choice_domain.SetSelection( 0 )
		plot_win.Add( self.m_choice_domain, 0, wx.ALL, 5 )

		self.m_panel_plot = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 720,360 ), wx.TAB_TRAVERSAL )
		self.m_panel_plot.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		self.m_panel_plot.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_panel_plot.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		plot_win.Add( self.m_panel_plot, 1, wx.EXPAND |wx.ALL, 5 )


		show_win.Add( plot_win, 1, wx.EXPAND, 5 )

		ctrl_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_conv = wx.StaticText( self, wx.ID_ANY, u"Audio/Text  Conversation Configuration and Display:", wx.DefaultPosition, wx.Size( 285,-1 ), 0 )
		self.m_staticText_conv.Wrap( -1 )

		self.m_staticText_conv.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		ctrl_win.Add( self.m_staticText_conv, 0, wx.ALL, 5 )

		self.m_button_asrttsTextClear = wx.Button( self, wx.ID_ANY, u"Clear Text", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		ctrl_win.Add( self.m_button_asrttsTextClear, 0, wx.ALL, 5 )

		self.m_staticText_null3 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText_null3.Wrap( -1 )

		ctrl_win.Add( self.m_staticText_null3, 0, wx.ALL, 5 )

		self.m_staticText_lang = wx.StaticText( self, wx.ID_ANY, u"Language:", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.m_staticText_lang.Wrap( -1 )

		self.m_staticText_lang.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		ctrl_win.Add( self.m_staticText_lang, 0, wx.ALL, 5 )

		m_choice_langChoices = [ u"US English", u"Mandarin Chinese" ]
		self.m_choice_lang = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_langChoices, 0 )
		self.m_choice_lang.SetSelection( 0 )
		ctrl_win.Add( self.m_choice_lang, 0, wx.ALL, 5 )

		self.m_staticText_asrEngine = wx.StaticText( self, wx.ID_ANY, u"ASR Engine:", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText_asrEngine.Wrap( -1 )

		self.m_staticText_asrEngine.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		ctrl_win.Add( self.m_staticText_asrEngine, 0, wx.ALL, 5 )

		m_choice_asrEngineChoices = [ u"CMU Sphinx", u"Google Speech Recognition", u"Google Cloud Speech API", u"Wit.ai", u"Microsoft Bing Voice Recognition", u"Houndify API", u"IBM Speech to Text", u"Snowboy Hotword Detection" ]
		self.m_choice_asrEngine = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 155,-1 ), m_choice_asrEngineChoices, 0 )
		self.m_choice_asrEngine.SetSelection( 0 )
		ctrl_win.Add( self.m_choice_asrEngine, 0, wx.ALL, 5 )

		self.m_staticText_asrId = wx.StaticText( self, wx.ID_ANY, u"Id:", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.m_staticText_asrId.Wrap( -1 )

		self.m_staticText_asrId.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		ctrl_win.Add( self.m_staticText_asrId, 0, wx.ALL, 5 )

		self.m_textCtrl_asrId = wx.TextCtrl( self, wx.ID_ANY, u"N/A", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		ctrl_win.Add( self.m_textCtrl_asrId, 0, wx.ALL, 5 )

		self.m_staticText_asrKey = wx.StaticText( self, wx.ID_ANY, u"Key:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_asrKey.Wrap( -1 )

		self.m_staticText_asrKey.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		ctrl_win.Add( self.m_staticText_asrKey, 0, wx.ALL, 5 )

		self.m_textCtrl_asrKey = wx.TextCtrl( self, wx.ID_ANY, u"N/A", wx.DefaultPosition, wx.Size( 232,-1 ), 0 )
		ctrl_win.Add( self.m_textCtrl_asrKey, 0, wx.ALL, 5 )

		self.m_staticText_ttsEngine = wx.StaticText( self, wx.ID_ANY, u"TTS Engine:", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText_ttsEngine.Wrap( -1 )

		self.m_staticText_ttsEngine.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		ctrl_win.Add( self.m_staticText_ttsEngine, 0, wx.ALL, 5 )

		m_choice_ttsEngineChoices = [ u"pyttsx3 - SAPI5", u"gTTS" ]
		self.m_choice_ttsEngine = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 155,-1 ), m_choice_ttsEngineChoices, 0 )
		self.m_choice_ttsEngine.SetSelection( 0 )
		ctrl_win.Add( self.m_choice_ttsEngine, 0, wx.ALL, 5 )

		self.m_staticText_voice = wx.StaticText( self, wx.ID_ANY, u"Voice:", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.m_staticText_voice.Wrap( -1 )

		self.m_staticText_voice.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		ctrl_win.Add( self.m_staticText_voice, 0, wx.ALL, 5 )

		m_choice_voiceChoices = []
		self.m_choice_voice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 310,-1 ), m_choice_voiceChoices, 0 )
		self.m_choice_voice.SetSelection( 0 )
		ctrl_win.Add( self.m_choice_voice, 0, wx.ALL, 5 )

		self.m_staticText_null4 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText_null4.Wrap( -1 )

		ctrl_win.Add( self.m_staticText_null4, 0, wx.ALL, 5 )

		self.m_staticText_ttwEngine = wx.StaticText( self, wx.ID_ANY, u"TTW Engine: ", wx.DefaultPosition, wx.Size( 70,-1 ), 0 )
		self.m_staticText_ttwEngine.Wrap( -1 )

		self.m_staticText_ttwEngine.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		ctrl_win.Add( self.m_staticText_ttwEngine, 0, wx.ALL, 5 )

		m_choice_ttwEngineChoices = [ u"eSpeak TTS", u"Festival SSS" ]
		self.m_choice_ttwEngine = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 155,-1 ), m_choice_ttwEngineChoices, 0 )
		self.m_choice_ttwEngine.SetSelection( 0 )
		ctrl_win.Add( self.m_choice_ttwEngine, 0, wx.ALL, 5 )

		self.m_staticText_gender = wx.StaticText( self, wx.ID_ANY, u"Gender:", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		self.m_staticText_gender.Wrap( -1 )

		self.m_staticText_gender.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		ctrl_win.Add( self.m_staticText_gender, 0, wx.ALL, 5 )

		m_choice_genderChoices = [ u"Male", u"Female" ]
		self.m_choice_gender = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 70,-1 ), m_choice_genderChoices, 0 )
		self.m_choice_gender.SetSelection( 0 )
		ctrl_win.Add( self.m_choice_gender, 0, wx.ALL, 5 )


		show_win.Add( ctrl_win, 1, wx.EXPAND, 5 )

		conv_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		text_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_textCtrl_asrttsText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 480,120 ), wx.TE_MULTILINE )
		text_win.Add( self.m_textCtrl_asrttsText, 0, wx.ALL, 5 )


		conv_win.Add( text_win, 1, wx.EXPAND, 5 )

		asrtts_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_button_asr = wx.Button( self, wx.ID_ANY, u"ASR", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		asrtts_win.Add( self.m_button_asr, 0, wx.ALL, 5 )

		self.m_textCtrl_asrFileName = wx.TextCtrl( self, wx.ID_ANY, u"asr_untitled1.txt", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		asrtts_win.Add( self.m_textCtrl_asrFileName, 0, wx.ALL, 5 )

		self.m_button_tts = wx.Button( self, wx.ID_ANY, u"TTS", wx.DefaultPosition, wx.Size( 40,-1 ), 0 )
		asrtts_win.Add( self.m_button_tts, 0, wx.ALL, 5 )

		self.m_textCtrl_ttsFileName = wx.TextCtrl( self, wx.ID_ANY, u"tts_untitled1.wav", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		asrtts_win.Add( self.m_textCtrl_ttsFileName, 0, wx.ALL, 5 )


		conv_win.Add( asrtts_win, 1, wx.EXPAND, 5 )


		show_win.Add( conv_win, 1, wx.EXPAND, 5 )


		win_sizer.Add( show_win, 1, wx.EXPAND, 5 )


		self.SetSizer( win_sizer )
		self.Layout()
		self.statusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.showHomepageInfo, id = self.m_menuItem_homePage.GetId() )
		self.Bind( wx.EVT_MENU, self.showAboutInfo, id = self.m_menuItem_about.GetId() )
		self.m_genericDirCtrl_audioDir.Bind( wx.EVT_TREE_SEL_CHANGED, self.viewAudio )
		self.m_button_play.Bind( wx.EVT_BUTTON, self.playAudio )
		self.m_button_record.Bind( wx.EVT_BUTTON, self.recordAudio )
		self.m_button_asrttsTextClear.Bind( wx.EVT_BUTTON, self.clearAsrTtsText )
		self.m_choice_voice.Bind( wx.EVT_ENTER_WINDOW, self.refreshVoice )
		self.m_button_asr.Bind( wx.EVT_BUTTON, self.audioSpeechRecognition )
		self.m_button_tts.Bind( wx.EVT_BUTTON, self.textToSpeech )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def showHomepageInfo( self, event ):
		event.Skip()

	def showAboutInfo( self, event ):
		event.Skip()

	def viewAudio( self, event ):
		event.Skip()

	def playAudio( self, event ):
		event.Skip()

	def recordAudio( self, event ):
		event.Skip()

	def clearAsrTtsText( self, event ):
		event.Skip()

	def refreshVoice( self, event ):
		event.Skip()

	def audioSpeechRecognition( self, event ):
		event.Skip()

	def textToSpeech( self, event ):
		event.Skip()


