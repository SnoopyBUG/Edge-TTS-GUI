import edge_tts
import asyncio
import chardet
import pygame

import tkinter as tk
from tkinter import ttk
import subprocess

voice = "zh-CN-YunyangNeural"     # Choose voice: [$ edge-tts --list-voices]
mp3_path = "D:\\temp.mp3"         # path of audio (mp3)
srt_path = "D:\\temp.srt"         # path of SubRip Text


async def TTS(text, voice):
    tts = edge_tts.Communicate(text=text, voice=voice)
    await tts.save(mp3_path, srt_path)

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()
    pygame.quit()

def run():
    user_input = entry.get()
    file_path = file_entry.get()
    if user_input or (file_var.get() and file_path):
        try:
            output_text.set("<<<<<<<<<<  Generating...  >>>>>>>>>>\n\n")
            root.update_idletasks()
            if file_var.get():
                text = open(file_path, "r", encoding = chardet.detect(open(file_path, 'rb').read())["encoding"]).read()
                asyncio.run(TTS(text=text, voice=voice))
            else:
                asyncio.run(TTS(text=user_input, voice=voice))

            play_sound()
            output_text.set("Generated successfully!\n%s\n%s"%(mp3_path,srt_path))
        except Exception as e:
            output_text.set(f"Failed: {e}")
    else:
        output_text.set("Please enter some text, or use file as input.")

# 创建主窗口
root = tk.Tk()
root.title("Edge-TTS")
root.geometry("400x400")

# 创建样式
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))

# 创建标签和文本输入框
label = ttk.Label(root, text="Enter SHORT text to convert to speech")
label.pack(pady=10)

entry = ttk.Entry(root, width=50)
entry.pack(pady=10)

# 创建文件路径输入框
file_label = ttk.Label(root, text="Enter absolute path of LONG text file")
file_label.pack(pady=10)

file_entry = ttk.Entry(root, width=50)
file_entry.pack(pady=10)

# 创建复选框
file_var = tk.BooleanVar()
file_check = ttk.Checkbutton(root, text="Use file as input", variable=file_var)
file_check.pack(pady=10)

# 创建执行按钮
button = ttk.Button(root, text="RUN", command=run)
button.pack(pady=20)

# 创建输出文本框
output_text = tk.StringVar()
output_label = ttk.Label(root, textvariable=output_text, wraplength=380)
output_label.pack(pady=10)

# 运行主循环
root.mainloop()
