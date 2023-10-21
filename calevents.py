import calendar
import tkinter as tk
from tkinter import messagebox

# Function to add event to the events dictionary
def add_event():
    event_date = int(date_entry.get())
    event_description = description_entry.get()
    if event_date in events:
        events[event_date].append(event_description)
    else:
        events[event_date] = [event_description]
    update_events_text()

# Function to update events_text with events dictionary
def update_events_text():
    events_text.set("Events:\n")
    for date, descriptions in events.items():
        for description in descriptions:
            events_text.set(events_text.get() + f"{date}: {description}\n")

# Function to show calendar and events
def show_calendar():
    try:
        yy = int(year_entry.get())
        mm = int(month_entry.get())
        cal_text.set(calendar.month(yy, mm))
        update_events_text()
    except ValueError:
        messagebox.showerror("Error", "Invalid input for year or month!")

# Function to handle calendar date clicks
def on_date_click(event):
    clicked_date = int(event.widget.cget("text"))
    month_entry.delete(0, tk.END)
    month_entry.insert(0, str(clicked_date))

# Create a tkinter window
root = tk.Tk()
root.title("Calendar with Multiple Events")

# Year input
year_label = tk.Label(root, text="Enter year:")
year_label.pack()
year_entry = tk.Entry(root)
year_entry.pack()

# Month input
month_label = tk.Label(root, text="Enter month:")
month_label.pack()
month_entry = tk.Entry(root)
month_entry.pack()

# Event date input
date_label = tk.Label(root, text="Enter event date:")
date_label.pack()
date_entry = tk.Entry(root)
date_entry.pack()

# Event description input
description_label = tk.Label(root, text="Enter event description:")
description_label.pack()
description_entry = tk.Entry(root)
description_entry.pack()

# Button to add event
add_button = tk.Button(root, text="Add Event", command=add_event)
add_button.pack()

# Button to show calendar and events
show_button = tk.Button(root, text="Show Calendar", command=show_calendar)
show_button.pack()

# Calendar display
cal_text = tk.StringVar()
cal_label = tk.Label(root, textvariable=cal_text)
cal_label.pack()

# Events display
events_text = tk.StringVar()
events_label = tk.Label(root, textvariable=events_text)
events_label.pack()

# Dictionary to store events with dates as keys and descriptions as values
events = {}

# Bind click event to dates in the calendar
cal_label.bind("<Button-1>", on_date_click)

# Run the tkinter main loop
root.mainloop()
