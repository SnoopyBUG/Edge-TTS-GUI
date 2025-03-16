# Edge-TTS-GUI

**input text → generate audio → play the audio**

GUI for Edge-TSS, **playing the audio** generated immediately. 

Based on Edge-TSS (https://github.com/rany2/edge-tts).

懒得开口说话，目前作为本人（i人）的嘴替。

Too lazy to speak, currently acting as the mouthpiece for me (an introvert).

## 1 Install
```
$ pip install edge-tts
$ pip install asyncio
$ pip install chardet
$ pip install pygame
```

## 2 Change voice & path
```
voice = "zh-CN-YunyangNeural"                                 # Choose voice: [$ edge-tts --list-voices]
mp3_path = "D:\\temp.mp3"                                     # path of audio (mp3)
srt_path = "D:\\temp.srt"                                     # path of SubRip Text
```

## 3 Run GUI
```
$ python Edge-TTS-GUI.py
```
You can input short text converting to speech directly, or convert a text file to a speech.

Demo: https://www.bilibili.com/video/BV125QUYEEen

![image](https://github.com/user-attachments/assets/8f7a014f-be33-498f-af88-109cf4134718)
