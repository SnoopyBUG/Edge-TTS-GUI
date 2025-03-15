import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import subprocess

voice = "zh-CN-YunyangNeural"                                # Choose voice: [$ edge-tts --list-voices]
mp3_path = "D:\\temp.mp3"                                    # path of audio (mp3)
srt_path = "D:\\temp.srt"                                    # path of SubRip Text
wmplayer_path = "C:\\Program Files\\Windows Media Player"    # path of [Windows Media Player]

def run_command():
    user_input = entry.get()
    file_path = file_entry.get()
    if user_input or (file_var.get() and file_path):
        if file_var.get():
            commands = [
                'edge-tts --voice %s --file %s --write-media %s --write-subtitles %s' % (voice, file_path, mp3_path, srt_path),
                'wmplayer.exe %s' % mp3_path
            ]
        else:
            commands = [
                'edge-tts --voice %s --text %s --write-media %s --write-subtitles %s' % (voice, user_input, mp3_path, srt_path),
                'wmplayer.exe %s' % mp3_path
            ]
        try:
            for command in commands:
                subprocess.run(command, cwd=wmplayer_path, check=True, shell=True)
            tk.messagebox.showinfo("Success", "Commands executed successfully!")
        except subprocess.CalledProcessError as e:
            tk.messagebox.showerror("Error", f"Command failed: {e}")
    else:
        tk.messagebox.showwarning("Input Error", "Please enter some text, or use file as input.")

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
button = ttk.Button(root, text="RUN", command=run_command)
button.pack(pady=20)

# 运行主循环
root.mainloop()
