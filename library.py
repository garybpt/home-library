import json
import os

# Function to save the student dictionary to a JSON file
def save_json(home_library):
    with open(LIBRARY_RECORD, "w") as file:
        json.dump(home_library, file, indent=4)

# Function to load the student dictionary from a JSON file
def open_json():
    if os.path.exists(LIBRARY_RECORD):
        with open(LIBRARY_RECORD, "r") as file:
            try:
                return json.load(file)
            except json.decoder.JSONDecodeError:
                return {}
    else:
        return {}

# Define a filename for the student record JSON file
LIBRARY_RECORD = "/Users/garybutterfield/GitHub/home-library/home_library.json"

# Load the existing student dictionary or create an empty one
home_library = open_json()

while True:
    print("\nWelcome to your home library.\n")
    print("1. Add a Book\n2. Search for a Book\n3. List All Books\n4. Update a Library Record\n5. Delete Book\n6. Exit\n")

    choice = input("Please select an option: ")

    if choice == "1": # Add a student record
        print("\nYou chose to add a new book\n")

        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        subject = input("Enter Student Subject: ")

        student = {
            "ID": student_id,
            "NAME": name,
            "AGE": age,
            "SUBJECT": subject
        }

        home_library[student_id] = student
        save_json(home_library)

        print("Student record added successfully.")

    elif choice == "2": # Search for a student record
        print("\nYou chose to search for a book\n")

        student_id = input("Enter Student ID to search: ")

        if student_id in home_library:
            student = home_library[student_id]
            print("ID:", student["ID"])
            print("Name:", student["NAME"])
            print("Age:", student["AGE"])
            print("Subject:", student["SUBJECT"])
        else:
            print("Student record not found.")

    elif choice == "3": # List all records
        print("\nYou chose to list all library books\n")

        for student_id, student in home_library.items():
            print(f"ID: {student_id}, Name: {student['NAME']}, Age: {student['AGE']}, Subject: {student['SUBJECT']}")

    elif choice == "4": # Update student record
        print("\nYou chose to update a library record\n")

        student_id = input("Enter Student ID to update: ")

        if student_id in home_library:
            student = home_library[student_id]

            print("What would you like to update?")
            print("1. Name\n2. Age\n3. Subject")
            update_choice = input("Enter your choice: ")

            if update_choice == "1":
                new_name = input("Enter the new name: ")
                student["NAME"] = new_name
            elif update_choice == "2":
                new_age = input("Enter the new age: ")
                student["AGE"] = new_age
            elif update_choice == "3":
                new_subject = input("Enter the new subject: ")
                student["SUBJECT"] = new_subject
            else:
                print("Invalid choice.")

            home_library[student_id] = student
            save_json(home_library)
            print("Student record updated successfully.")
        else:
            print("Student ID not found. Cannot update the record.")

    elif choice == "5": # Delete student record
        print("\nYou chose to delete a library record\n")

        student_id_to_delete = input("Enter Student ID to delete: ")

        if student_id_to_delete in home_library:
            del home_library[student_id_to_delete]
            save_json(home_library)
            print(f"Student record with ID {student_id_to_delete} has been deleted.")
        else:
            print("Student ID not found. Cannot delete the record.")

    elif choice == "6": # Exit
        print("\nExiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")