# JaysPySPEECH
A tiny audio speech assistant based on PyAudio+Matplotlib+SpeechRecognition(PocketSphinx)+pyttsx3(eSpeak) 

<img src="http://odox9r8vg.bkt.clouddn.com/image/cnblogs/JaysPySPEECH_overview1.PNG" style="zoom:100%" />

### How to build :
********************
First of all, you should install all packages listed in [《JaysPySPEECH环境搭建》](https://www.cnblogs.com/henjay724/p/9542690.html), then follow below steps:
```text
  1. cd to "\JaysPySPEECH\bin\"
  2. Update pathex in JaysPySPEECH.spec to current path in your PC
  3. Run "pyinstaller JaysPySPEECH.spec"
  4. You will see "\JaysPySPEECH\bin\dist\JaysPySPEECH.exe" is generated
  5. Move JaysPySPEECH.exe to dictionary "\JaysPySPEECH\bin\" (this step is a MUST!!!)
  6. Open "\JaysPySPEECH\bin\JaysPySPEECH.exe" to use it
```

> Note1: It is only verified in environment: Windows 10, x64bit
> Note2: TTW(Text-to-Wav) feature cannot be used as PyInstaller cannot pack pyttsx3+eSpeak up

### Features in v1.0.0 :
********************
* View the waveform of selected .wav file
* Record sound from microphone to .wav file (\conv\rec)
* Play selected .wav file
* ASR: Recognize selected .wav file to text (\conv\asr)
* TTS: Translate input text to speech
* TTW: Translate input text to .wav file (\conv\tts)
* Both English and Chinese are supported in ASR,TTS,TTW
* Design detail: [《JaysPySPEECH诞生记(全七篇)》](https://www.cnblogs.com/henjay724/p/9541867.html)

Known issues:
* The audio data are all 0x00s if BitDepth is set as 8bits when recording sound (it seems to be PyAudio issue)
* Sometimes Application will hang up if language is set as Chinese when using TTS (it may be MSSpeech_TTS_xxx language package installation issue)

### License :
********************
This package is licensed under the BSD three-clause license. See the LICENSE.txt file for details.

Copyright © 2017-2018 Jay Heng.