import tkinter as tk
import subprocess

# Function to launch another Python file
def launch_file(file_name):
    subprocess.Popen(['python', file_name])

# Create the main window
root = tk.Tk()
root.title("Python Launcher")
root.geometry("300x200")

# Create buttons to launch other Python files
btn1 = tk.Button(root, text="create_table.py", command=lambda: launch_file('create_table.py'))
btn2 = tk.Button(root, text="Launch file2.py", command=lambda: launch_file('file2.py'))
btn3 = tk.Button(root, text="Launch file3.py", command=lambda: launch_file('file3.py'))
btn4 = tk.Button(root, text="Launch file4.py", command=lambda: launch_file('file4.py'))
btn5 = tk.Button(root, text="Launch file5.py", command=lambda: launch_file('file5.py'))

# Arrange buttons on the window
btn1.pack(pady=10)
btn2.pack(pady=10)
btn3.pack(pady=10)
btn4.pack(pady=10)
btn5.pack(pady=10)

# Start the main loop
root.mainloop()