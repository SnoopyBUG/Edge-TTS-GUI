import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import subprocess

voice = "zh-CN-YunyangNeural"
mp3_dir = "D:\\LZT\\Study\\Code\\edge-tts\\temp.mp3"
srt_dir = "D:\\LZT\\Study\\Code\\edge-tts\\temp.srt"

def run_command():
    user_input = entry.get()
    if user_input:
        commands = [
            'edge-tts --voice %s --text %s --write-media %s --write-subtitles %s' % (voice, user_input, mp3_dir,srt_dir),
            'wmplayer.exe %s' % mp3_dir
        ]
        try:
            for command in commands:
                subprocess.run(command, cwd='C:\\Program Files\\Windows Media Player', check=True, shell=True)
            tk.messagebox.showinfo("Success", "Commands executed successfully!")
        except subprocess.CalledProcessError as e:
            tk.messagebox.showerror("Error", f"Command failed: {e}")
    else:
        tk.messagebox.showwarning("Input Error", "Please enter some text.")

# 创建主窗口
root = tk.Tk()
root.title("Edge-TTS GUI")
root.geometry("400x300")

# 创建样式
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))

# 创建标签和文本输入框
label = ttk.Label(root, text="Enter text:")
label.pack(pady=10)

entry = ttk.Entry(root, width=50)
entry.pack(pady=10)

# 创建执行按钮
button = ttk.Button(root, text="Run Command", command=run_command)
button.pack(pady=20)

# 运行主循环
root.mainloop()