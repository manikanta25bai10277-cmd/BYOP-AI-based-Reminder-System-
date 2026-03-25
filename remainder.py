import time

def start_reminder(interval):
    while True:
        print("\n🔔 Eye Care Reminder:")
        print("1. Blink your eyes 👀")
        print("2. Look away from screen 🖥️")
        print("3. Use eye drops 💧")
        
        time.sleep(interval)