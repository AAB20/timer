import tkinter as tk
from datetime import datetime, timedelta

def update_timer():
    """ Update the timer display """
    now = datetime.now()
    time_left = end_time - now
    
    if time_left > timedelta(0):
        days, seconds = time_left.days, time_left.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        timer_label.config(text=f"{days} days, {hours:02}:{minutes:02}:{seconds:02}")
        root.after(1000, update_timer)
    else:
        timer_label.config(text="Time's up!")
        root.after(1000, update_timer)

# Set the end time (June 8, 2025)
end_time = datetime(2025, 6, 8)

# Create the main window
root = tk.Tk()
root.title("Countdown Timer")

# Create and place the timer label with black text color
timer_label = tk.Label(root, font=('Helvetica', 48), fg='black')
timer_label.pack(pady=20)

# Start the timer update loop
update_timer()

# Run the Tkinter event loop
root.mainloop()
