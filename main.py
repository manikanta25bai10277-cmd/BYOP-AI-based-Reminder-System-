import time

print("=== Eye Care Reminder System ===")

# Input
usage = int(input("How many hours do you use screen daily? "))

dryness = input("Do you feel dryness in eyes? (yes/no): ").lower()
redness = input("Do you have redness in eyes? (yes/no): ").lower()
itching = input("Do you feel itching? (yes/no): ").lower()

# Condition Detection (AI Logic)
if dryness == "yes" and redness == "yes":
    problem = "Dry Eye Syndrome"
elif itching == "yes":
    problem = "Eye Allergy"
else:
    problem = "Normal Eye Strain"

print("\nDetected Condition:", problem)

# Suggestions
print("\nSuggested Care:")

if problem == "Dry Eye Syndrome":
    print("- Blink frequently 👀")
    print("- Use lubricating eye drops 💧")
    print("- Follow 20-20-20 rule")

elif problem == "Eye Allergy":
    print("- Avoid dust and allergens")
    print("- Wash eyes with clean water")
    print("- Consult doctor if severe")

else:
    print("- Take regular breaks")
    print("- Reduce screen brightness")
    print("- Maintain proper distance")

# Interval Logic
if usage > 6:
    interval = 5
    print("\nHigh usage → Frequent reminders")
else:
    interval = 10
    print("\nNormal usage → Moderate reminders")

# Reminder Function (now inside same file)
def start_reminder(interval):
    for i in range(5):
        print("\n🔔 Eye Care Reminder:")
        print("Blink your eyes 👀")
        print("Look away from screen 🖥️")
        print("Use eye drops 💧")
        time.sleep(interval)

# Start Reminder
start_reminder(interval)