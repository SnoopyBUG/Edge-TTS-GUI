# Edge-TTS-GUI

**input text → generate audio → play the audio**

GUI for Edge-TSS, **playing the audio** generated immediately with wmplayer on Windows. 

Based on Edge-TSS (https://github.com/rany2/edge-tts).

懒得开口说话，目前作为本人（i人）的嘴替。

Too lazy to speak, currently acting as the mouthpiece for me (an introvert).

## 0 Notice
```
Make sure Windows Media Player is available.
```

## 1 Install edge-tts
```
$ pip install edge-tts
```

## 2 Change voice & path
```
voice = "zh-CN-YunyangNeural"                                 # Choose voice
mp3_path = "D:\\temp.mp3"                                     # path of audio (mp3)
srt_path = "D:\\temp.srt"                                     # path of SubRip Text
wmplayer_path = "C:\\Program Files\\Windows Media Player"     # path of [Windows Media Player]
```

## 3 run GUI
```
$ python Edge-TTS-GUI.py
```
