print("=== Eye Care Reminder System ===")

usage = int(input("How many hours do you use screen daily? "))
dryness = input("Do you feel dryness in eyes? (yes/no): ").lower()
redness = input("Do you have redness in eyes? (yes/no): ").lower()
itching = input("Do you feel itching? (yes/no): ").lower()

# AI-like decision
if dryness == "yes" and redness == "yes":
    problem = "Dry Eye Syndrome"
elif itching == "yes":
    problem = "Eye Allergy"
else:
    problem = "Normal Eye Strain"

print("\nDetected Condition:", problem)

if usage > 6:
    interval = 10
    print("High usage → Frequent reminders")
else:
    interval = 20
    print("Normal usage → Moderate reminders")

    print("\nSuggested Care:")

if problem == "Dry Eye Syndrome":
    print("- Blink frequently")
    print("- Use lubricating eye drops (artificial tears)")
    print("- Follow 20-20-20 rule")

elif problem == "Eye Allergy":
    print("- Avoid dust and allergens")
    print("- Wash eyes with clean water")
    print("- Consult doctor if severe")

else:
    print("- Take regular breaks")
    print("- Reduce screen brightness")
    print("- Maintain proper distance from screen")
    
from reminder import start_reminder
start_reminder(interval)