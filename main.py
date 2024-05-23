import json
import os
from datetime import datetime, timedelta

class HabitTracker:
    def __init__(self, data_file="habits.json"):
        self.data_file = data_file
        self.habits = self.load_habits()

    def load_habits(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                return json.load(file)
        else:
            return []

    def save_habits(self):
        with open(self.data_file, "w") as file:
            json.dump(self.habits, file, indent=4)

    def add_habit(self, habit_name, target):
        self.habits.append({
            "name": habit_name,
            "target": target,
            "progress": []
        })
        self.save_habits()

    def remove_habit(self, habit_index):
        del self.habits[habit_index]
        self.save_habits()

    def log_progress(self, habit_index, completed=True):
        today = datetime.now().strftime("%Y-%m-%d")
        self.habits[habit_index]["progress"].append({
            "date": today,
            "completed": completed
        })
        self.save_habits()

    def view_habits(self):
        for index, habit in enumerate(self.habits):
            print(f"{index + 1}. {habit['name']}: Target - {habit['target']}")

    def view_progress(self, habit_index):
        habit = self.habits[habit_index]
        progress = habit["progress"]
        print(f"Habit: {habit['name']}")
        for entry in progress:
            print(f"Date: {entry['date']}, Completed: {entry['completed']}")
        print("")

def main():
    tracker = HabitTracker()

    while True:
        print("Command-Line Habit Tracker")
        print("1. Add Habit")
        print("2. Remove Habit")
        print("3. Log Progress")
        print("4. View Habits")
        print("5. View Progress")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            habit_name = input("Enter habit name: ")
            target = input("Enter habit target (e.g., daily, weekly, monthly): ")
            tracker.add_habit(habit_name, target)
            print("Habit added successfully.\n")

        elif choice == "2":
            tracker.view_habits()
            habit_index = int(input("Enter the index of the habit to remove: ")) - 1
            tracker.remove_habit(habit_index)
            print("Habit removed successfully.\n")

        elif choice == "3":
            tracker.view_habits()
            habit_index = int(input("Enter the index of the habit to log progress for: ")) - 1
            status = input("Has the habit been completed today? (y/n): ").lower()
            if status == "y":
                tracker.log_progress(habit_index, completed=True)
            elif status == "n":
                tracker.log_progress(habit_index, completed=False)
            print("Progress logged successfully.\n")

        elif choice == "4":
            tracker.view_habits()

        elif choice == "5":
            tracker.view_habits()
            habit_index = int(input("Enter the index of the habit to view progress for: ")) - 1
            tracker.view_progress(habit_index)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")

if __name__ == "__main__":
    main()
