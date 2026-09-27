

import csv
import os
from datetime import datetime


def get_time_based_greeting():
    """Return 'Good morning', 'Good afternoon' or 'Good evening' based on the current time."""
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning"
    elif hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"


def build_welcome_message(name, organization, workshop_name):
    """Build a personalized welcome message for one participant."""
    greeting = get_time_based_greeting()
    org_part = f" from {organization}" if organization else ""
    return (
        f"{greeting}, {name}{org_part}! "
        f"Welcome to '{workshop_name}'. We're glad to have you with us today."
    )


def collect_participants_interactively():
    """Prompt the user to enter participants one at a time until they type 'done'."""
    participants = []
    print("\nEnter participant details (type 'done' as the name to finish).\n")
    while True:
        name = input("Participant name: ").strip()
        if name.lower() == "done":
            break
        if not name:
            print("Name cannot be empty. Try again.")
            continue
        organization = input("Organization (optional, press Enter to skip): ").strip()
        participants.append({"name": name, "organization": organization})
    return participants


def load_participants_from_csv(filepath):
    """Load participants from a CSV file with 'name' and optional 'organization' columns."""
    participants = []
    with open(filepath, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get("name", "").strip()
            organization = row.get("organization", "").strip()
            if name:
                participants.append({"name": name, "organization": organization})
    return participants


def greet_participants(participants, workshop_name):
    """Print a personalized greeting for each participant and a summary."""
    if not participants:
        print("\nNo participants to greet.")
        return

    print(f"\n{'=' * 60}")
    print(f"  {workshop_name} — Participant Greetings")
    print(f"  {datetime.now().strftime('%A, %d %B %Y at %H:%M')}")
    print(f"{'=' * 60}\n")

    for person in participants:
        message = build_welcome_message(
            person["name"], person.get("organization", ""), workshop_name
        )
        print(f"- {message}")

    print(f"\n{'-' * 60}")
    print(f"Total participants greeted: {len(participants)}")
    print(f"{'-' * 60}\n")


def main():
    print("=== Workshop Participant Greeting Application ===")
    workshop_name = input("Enter the workshop name: ").strip() or "the workshop"

    print("\nHow would you like to add participants?")
    print("  1. Enter names manually")
    print("  2. Load from a CSV file (columns: name, organization)")
    choice = input("Choose 1 or 2: ").strip()

    if choice == "2":
        filepath = input("Enter the CSV file path: ").strip()
        if not os.path.isfile(filepath):
            print(f"File not found: {filepath}")
            return
        participants = load_participants_from_csv(filepath)
    else:
        participants = collect_participants_interactively()

    greet_participants(participants, workshop_name)


if __name__ == "__main__":
    main()