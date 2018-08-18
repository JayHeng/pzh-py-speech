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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 940,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 64, 64, 64 ) )

		win_sizer = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		edit_win = wx.BoxSizer( wx.VERTICAL )

		dir_win = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText_selectAudioFile = wx.StaticText( self, wx.ID_ANY, u"Select Audio File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_selectAudioFile.Wrap( -1 )

		self.m_staticText_selectAudioFile.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		dir_win.Add( self.m_staticText_selectAudioFile, 0, wx.ALL, 5 )

		self.m_genericDirCtrl_audioDir = wx.GenericDirCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 180,100 ), wx.DIRCTRL_SHOW_FILTERS|wx.HSCROLL, wx.EmptyString, 0 )

		self.m_genericDirCtrl_audioDir.ShowHidden( False )
		self.m_genericDirCtrl_audioDir.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_genericDirCtrl_audioDir.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		dir_win.Add( self.m_genericDirCtrl_audioDir, 1, wx.EXPAND |wx.ALL, 5 )


		edit_win.Add( dir_win, 1, wx.EXPAND, 5 )

		rec_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_recordAudioFile = wx.StaticText( self, wx.ID_ANY, u"Record Audio File:", wx.DefaultPosition, wx.Size( 180,-1 ), 0 )
		self.m_staticText_recordAudioFile.Wrap( -1 )

		self.m_staticText_recordAudioFile.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		rec_win.Add( self.m_staticText_recordAudioFile, 0, wx.ALL, 5 )

		self.m_staticText_fileName = wx.StaticText( self, wx.ID_ANY, u"File Name:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText_fileName.Wrap( -1 )

		self.m_staticText_fileName.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		rec_win.Add( self.m_staticText_fileName, 0, wx.ALL, 5 )

		self.m_textCtrl_fileName = wx.TextCtrl( self, wx.ID_ANY, u"Untitled 1", wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
		rec_win.Add( self.m_textCtrl_fileName, 0, wx.ALL, 5 )

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

		self.m_staticText_channels = wx.StaticText( self, wx.ID_ANY, u"Channels:", wx.DefaultPosition, wx.Size( 60,-1 ), 0 )
		self.m_staticText_channels.Wrap( -1 )

		self.m_staticText_channels.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		rec_win.Add( self.m_staticText_channels, 0, wx.ALL, 5 )

		m_choice_channelsChoices = [ u"Mono", u"Stereo" ]
		self.m_choice_channels = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 80,-1 ), m_choice_channelsChoices, 0 )
		self.m_choice_channels.SetSelection( 1 )
		rec_win.Add( self.m_choice_channels, 0, wx.ALL, 5 )

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

		self.m_staticText_null0 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_staticText_null0.Wrap( -1 )

		rec_win.Add( self.m_staticText_null0, 0, wx.ALL, 5 )

		self.m_button_record = wx.Button( self, wx.ID_ANY, u"Record Start", wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
		rec_win.Add( self.m_button_record, 0, wx.ALL, 5 )


		edit_win.Add( rec_win, 1, wx.EXPAND, 5 )


		win_sizer.Add( edit_win, 1, wx.EXPAND, 5 )

		show_win = wx.BoxSizer( wx.VERTICAL )

		plot_win = wx.BoxSizer( wx.VERTICAL )

		self.m_panel_plot = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 720,360 ), wx.TAB_TRAVERSAL )
		self.m_panel_plot.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		self.m_panel_plot.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_panel_plot.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		plot_win.Add( self.m_panel_plot, 1, wx.EXPAND |wx.ALL, 5 )


		show_win.Add( plot_win, 1, wx.EXPAND, 5 )

		hmi_win = wx.BoxSizer( wx.VERTICAL )

		ctrl_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_staticText_null1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 30,-1 ), 0 )
		self.m_staticText_null1.Wrap( -1 )

		ctrl_win.Add( self.m_staticText_null1, 0, wx.ALL, 5 )

		self.m_button_play = wx.Button( self, wx.ID_ANY, u"Play Start", wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
		ctrl_win.Add( self.m_button_play, 0, wx.ALL, 5 )

		self.m_staticText_audioInfo = wx.StaticText( self, wx.ID_ANY, u"Opened Audio Info:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_audioInfo.Wrap( -1 )

		self.m_staticText_audioInfo.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_APPWORKSPACE ) )

		ctrl_win.Add( self.m_staticText_audioInfo, 0, wx.ALL, 5 )

		self.m_textCtrl_audioInfo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
		ctrl_win.Add( self.m_textCtrl_audioInfo, 0, wx.ALL, 5 )


		hmi_win.Add( ctrl_win, 1, wx.EXPAND, 5 )

		text_win = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 720,150 ), 0|wx.HSCROLL|wx.VSCROLL )
		text_win.Add( self.m_textCtrl2, 0, wx.ALL, 5 )


		hmi_win.Add( text_win, 1, wx.EXPAND, 5 )


		show_win.Add( hmi_win, 1, wx.EXPAND, 5 )


		win_sizer.Add( show_win, 1, wx.EXPAND, 5 )


		self.SetSizer( win_sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_genericDirCtrl_audioDir.Bind( wx.EVT_TREE_SEL_CHANGED, self.viewAudio )
		self.m_button_record.Bind( wx.EVT_BUTTON, self.recordAudio )
		self.m_button_play.Bind( wx.EVT_BUTTON, self.playAudio )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def viewAudio( self, event ):
		event.Skip()

	def recordAudio( self, event ):
		event.Skip()

	def playAudio( self, event ):
		event.Skip()


