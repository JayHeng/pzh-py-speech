# 痞子衡语音处理助手
A tiny audio speech (.wav) utility tool (GUI) based on Python2.7+wxPython4.0+PyAudio+Matplotlib+SpeechRecognition(PocketSphinx)+pyttsx3(eSpeak) | 一款支持多引擎的wav格式语音处理小工具（音频录播与波形显示，语音识别，文语合成） 

[![GitHub release](https://img.shields.io/github/release/JayHeng/pzh-py-speech.svg)](https://github.com/JayHeng/pzh-py-speech/releases/latest) [![GitHub commits](https://img.shields.io/github/commits-since/JayHeng/pzh-py-speech/v1.0.0.svg)](https://github.com/JayHeng/pzh-py-speech/compare/v1.0.0...master) [![GitHub license](https://img.shields.io/github/license/JayHeng/pzh-py-speech.svg)](https://github.com/JayHeng/pzh-py-speech/blob/master/LICENSE.txt)

[English](./README-en.md) | 中文

<img src="http://henjay724.com/image/cnblogs/JaysPySPEECH_overview_github.PNG" style="zoom:100%" />

### 1. 二次开发与重编 :
********************
　　参考这篇文章 [《痞子衡语音处理助手-开发环境搭建》](https://www.cnblogs.com/henjay724/p/9542690.html) 安装所有非Python相关的开发工具, 然后按照如下步骤继续安装Python环境:  
```text
  1. 安装Python2.7.15 x86 version  
  2. 确认系统路径包含"\Python27\" 和 "\Python27\Scripts\"  
  3. 双击"\pzh-py-speech\env\do_setup_by_pip.bat"脚本安装所有依赖的第三方Python库  
  4. 双击"\pzh-py-speech\env\do_pack_by_pyinstaller.bat"脚本重新生成pzh-speech.exe  
  5. 双击"\pzh-py-speech\bin\pzh-speech.exe"运行  
```

### 2. 软件功能 :
********************
* 支持查看所选的.wav文件波形图  
* 支持从麦克风录制声音进.wav文件 (\conv\rec)  
* 支持播放所选的.wav文件  
* ASR: 支持识别.wav文件里的内容并保存到文本文件 (\conv\asr)  
* TTS: 支持将输入的文本内容转换成语音播放  
* TTW: 支持将输入的文本内容转换成.wav文件 (\conv\tts)  
* 支持两种语言（中英）的上述ASR,TTS,TTW处理  
* 软件设计细节详见: [《痞子衡语音处理助手诞生记(全七篇)》](https://www.cnblogs.com/henjay724/p/9541867.html)

已知问题:  
* 在录制声音时，如果BitDepth设为8bits，录制的音频数据全是0x00 (应该是PyAudio库的问题)  
* 在处理TTS时，如果语言设置为中文，有时候软件会停止执行 (可能是MSSpeech_TTS_xxx language包的安装问题)  

### 3. License :
********************
　　软件采用BSD three-clause license， 更多许可证细节详见LICENSE.txt。

Copyright © 2017-2018 Jay Heng.