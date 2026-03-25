from reminder import start_reminder
from logger import log_data

print("=== Eye Care Reminder System ===")

usage = int(input("How many hours do you use screen daily? "))

if usage > 6:
    interval = 10
    print("High usage detected → Frequent reminders")
else:
    interval = 20
    print("Normal usage → Moderate reminders")

log_data("User usage: " + str(usage))
log_data("Interval: " + str(interval))

start_reminder(interval)
