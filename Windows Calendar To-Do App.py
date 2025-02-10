from datetime import datetime, timedelta
import os

ICS_FILE = "todo_calendar.ics"

def generate_ics_event(task, start_time, end_time):
    """Genereer een ICS-gebeurtenis voor de taak."""
    event = f"""BEGIN:VEVENT
SUMMARY:{task}
DTSTART:{start_time.strftime('%Y%m%dT%H%M%S')}
DTEND:{end_time.strftime('%Y%m%dT%H%M%S')}
END:VEVENT
"""
    return event

def parse_datetime(date_str, time_str):
    """Parse de ingevoerde datum en tijd in een datetime object."""
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')  # Formaat: 2025-02-10
        time_obj = datetime.strptime(time_str, '%H:%M')  # Formaat: 14:30
        return date_obj.replace(hour=time_obj.hour, minute=time_obj.minute, second=0)
    except ValueError:
        print("⚠ Ongeldig datum of tijd formaat! Gebruik het formaat: YYYY-MM-DD en HH:MM")
        return None

def save_to_calendar(task, start_time):
    """Voegt een taak toe aan het ICS-bestand."""
    end_time = start_time + timedelta(hours=1)  # Standaardduur: 1 uur
    ics_event = generate_ics_event(task, start_time, end_time)

    if not os.path.exists(ICS_FILE):
        with open(ICS_FILE, "w") as file:
            file.write("BEGIN:VCALENDAR\nVERSION:2.0\n")

    with open(ICS_FILE, "a") as file:
        file.write(ics_event)

    print(f"✅ Taak toegevoegd aan {ICS_FILE}! Import dit bestand in je Windows Agenda.")

def main():
    while True:
        print("\n🎯 Windows Calendar To-Do App")
        print("1️⃣ Bekijk kalenderbestand")
        print("2️⃣ Taak toevoegen")
        print("3️⃣ Afsluiten")
        choice = input("👉 Kies een optie: ")

        if choice == "1":
            if os.path.exists(ICS_FILE):
                print(f"📅 Open {ICS_FILE} om je taken te bekijken.")
            else:
                print("📭 Geen kalenderbestand gevonden.")
        elif choice == "2":
            task = input("📝 Voer een nieuwe taak in: ")
            date_str = input("📅 Voer de datum in (YYYY-MM-DD): ")
            time_str = input("⏰ Voer de tijd in (HH:MM): ")

            start_time = parse_datetime(date_str, time_str)
            if start_time:
                save_to_calendar(task, start_time)
        elif choice == "3":
            with open(ICS_FILE, "a") as file:
                file.write("END:VCALENDAR\n")  # Sluit het bestand correct af
            print("👋 Tot ziens!")
            break
        else:
            print("⚠ Ongeldige keuze, probeer opnieuw!")

if __name__ == "__main__":
    main()


