import tkinter as tk
from tkinter import font
from time import strftime
from datetime import datetime

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.root.geometry("600x300")
        self.root.configure(bg='black')
        self.root.resizable(False, False)
        
        # Create a main frame
        self.main_frame = tk.Frame(root, bg='black')
        self.main_frame.pack(expand=True, fill='both')
        
        # Time label
        self.time_label = tk.Label(
            self.main_frame, 
            font=('Helvetica', 60, 'bold'),
            bg='black',
            fg='cyan'
        )
        self.time_label.pack(pady=20)
        
        # Date label
        self.date_label = tk.Label(
            self.main_frame,
            font=('Helvetica', 24),
            bg='black',
            fg='white'
        )
        self.date_label.pack()
        
        # Day label
        self.day_label = tk.Label(
            self.main_frame,
            font=('Helvetica', 30, 'bold'),
            bg='black',
            fg='yellow'
        )
        self.day_label.pack(pady=10)
        
        # AM/PM indicator
        self.ampm_label = tk.Label(
            self.main_frame,
            font=('Helvetica', 20),
            bg='black',
            fg='orange'
        )
        self.ampm_label.place(x=500, y=70)
        
        # Update clock immediately
        self.update_clock()
        
        # Add a quit button
        quit_button = tk.Button(
            self.main_frame,
            text="Quit",
            font=('Helvetica', 12),
            command=root.destroy,
            bg='red',
            fg='white'
        )
        quit_button.pack(side='bottom', pady=10)
    
    def update_clock(self):
        # Get current time
        time_string = strftime('%H:%M:%S')
        self.time_label.config(text=time_string)
        
        # Get current date
        date_string = datetime.now().strftime("%B %d, %Y")
        self.date_label.config(text=date_string)
        
        # Get current day
        day_string = datetime.now().strftime("%A")
        self.day_label.config(text=day_string)
        
        # Get AM/PM
        ampm_string = datetime.now().strftime("%p")
        self.ampm_label.config(text=ampm_string)
        
        # Update every 200 milliseconds
        self.time_label.after(200, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()