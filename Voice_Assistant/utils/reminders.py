import json
import os
import time
import threading
from datetime import datetime

REMINDER_FILE = "data/reminders.json"

def load_reminders():
    """Load reminders from JSON file"""
    if os.path.exists(REMINDER_FILE):
        with open(REMINDER_FILE, "r") as f:
            return json.load(f)
    return []

def save_reminders(reminders):
    """Save reminders to JSON file"""
    # Ensure data folder exists
    os.makedirs("data", exist_ok=True)
    with open(REMINDER_FILE, "w") as f:
        json.dump(reminders, f)

def set_reminder(text):
    """Parse 'remind me to ... at 3:30 PM' and save reminder"""
    try:
        parts = text.split(" at ")
        if len(parts) != 2:
            return "Please say: remind me to [task] at [time]"
        
        task = parts[0].replace("remind me to", "").strip()
        time_str = parts[1].strip()
        
        # Parse time like "3:30 PM" or "15:30"
        try:
            reminder_time = datetime.strptime(time_str, "%I:%M %p")
        except:
            reminder_time = datetime.strptime(time_str, "%H:%M")
        
        now = datetime.now()
        reminder_datetime = now.replace(hour=reminder_time.hour, minute=reminder_time.minute, second=0, microsecond=0)
        
        if reminder_datetime < now:
            reminder_datetime = reminder_datetime.replace(day=now.day + 1)
        
        reminders = load_reminders()
        reminders.append({
            "task": task,
            "time": reminder_datetime.isoformat()
        })
        save_reminders(reminders)
        return f"Reminder set for {task} at {reminder_datetime.strftime('%I:%M %p')}"
    except Exception as e:
        return f"Could not set reminder. Please say like: remind me to call mom at 3:30 PM"

def check_reminders(speak_func):
    """Background thread to check and speak reminders"""
    def reminder_loop():
        while True:
            reminders = load_reminders()
            now = datetime.now()
            new_reminders = []
            for r in reminders:
                reminder_time = datetime.fromisoformat(r["time"])
                if reminder_time <= now:
                    speak_func(f"Reminder: {r['task']}")
                else:
                    new_reminders.append(r)
            save_reminders(new_reminders)
            time.sleep(30)  # Check every 30 seconds
    
    thread = threading.Thread(target=reminder_loop, daemon=True)
    thread.start()