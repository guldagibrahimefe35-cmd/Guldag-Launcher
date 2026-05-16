import tkinter as tk
from tkinter import messagebox
import minecraft_launcher_lib
import subprocess
import os
import threading

MC_DIR = os.path.join(os.getcwd(), "minecraft")
VERSION = "1.21.11"

def launch_game():
    username = entry.get()
    if not username:
        messagebox.showerror("Hata", "Nick girmeden olmaz gardaş")
        return

    def task():
        try:
            minecraft_launcher_lib.install.install_minecraft_version(
                VERSION, MC_DIR
            )

            options = {
                "username": username,
                "uuid": "00000000-0000-0000-0000-000000000000",
                "token": "",
            }

            command = minecraft_launcher_lib.command.get_minecraft_command(
                VERSION, MC_DIR, options
            )

            subprocess.Popen(command)

        except Exception as e:
            messagebox.showerror("Çöktü", str(e))

    threading.Thread(target=task).start()

root = tk.Tk()
root.title("Dayı Launcher")
root.geometry("300x150")
root.resizable(False, False)

tk.Label(root, text="Nick Gir").pack(pady=10)
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Başlat", command=launch_game).pack(pady=15)

root.mainloop()
