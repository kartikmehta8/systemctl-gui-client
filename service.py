import tkinter as tk
import subprocess

def start_service():
    service = selected_service.get()
    command = f"sudo systemctl start {service}"
    execute_command(command)

def stop_service():
    service = selected_service.get()
    command = f"sudo systemctl stop {service}"
    execute_command(command)

def restart_service():
    service = selected_service.get()
    command = f"sudo systemctl restart {service}"
    execute_command(command)

def execute_command(command):
    password = password_entry.get()
    full_command = f"echo {password} | {command} 2>&1"
    process = subprocess.Popen(full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode == 0:
        output_text.config(text=f"\nSUCCESS\n\n{output.decode()}")
    else:
        output_text.config(text=f"\nFAILURE\n\n{error.decode()}")

window = tk.Tk()
window.title("Service Control Panel")

# Terminal-like styling
bg_color = "#262626"
fg_color = "#FFFFFF"
entry_bg_color = "#000000"
entry_fg_color = "#FFFFFF"

window.configure(bg=bg_color)

password_label = tk.Label(window, text="Password:", bg=bg_color, fg=fg_color)
password_label.grid(row=0, column=0, sticky="w")
password_entry = tk.Entry(window, show="*", bg=entry_bg_color, fg=entry_fg_color)
password_entry.grid(row=0, column=1, sticky="w")

service_label = tk.Label(window, text="Service:", bg=bg_color, fg=fg_color)
service_label.grid(row=1, column=0, sticky="w")
services = ["ssh", "network", "apache2", "mysql", "nginx", "cron"]
selected_service = tk.StringVar()
selected_service.set(services[0])
service_dropdown = tk.OptionMenu(window, selected_service, *services)
service_dropdown.config(bg=entry_bg_color, fg=entry_fg_color)
service_dropdown.grid(row=1, column=1, sticky="w")

start_button = tk.Button(window, text="START", command=start_service, bg=bg_color, fg=fg_color)
start_button.grid(row=2, column=0, pady=10)
stop_button = tk.Button(window, text="STOP", command=stop_service, bg=bg_color, fg=fg_color)
stop_button.grid(row=2, column=1, pady=10)
restart_button = tk.Button(window, text="RESTART", command=restart_service, bg=bg_color, fg=fg_color)
restart_button.grid(row=2, column=2, pady=10)

output_label = tk.Label(window, text="Output:", bg=bg_color, fg=fg_color)
output_label.grid(row=3, column=0, sticky="w")
output_text = tk.Label(window, text="", bg=entry_bg_color, fg=entry_fg_color, justify="left", anchor="nw")
output_text.grid(row=3, column=1, columnspan=2, sticky="w")

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)

window.mainloop()

