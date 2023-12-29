import json
import os

# Function to save the home library to a JSON file
def save_json(home_library):
    with open(LIBRARY_RECORD, "w") as file:
        json.dump(home_library, file, indent=4)

# Function to load the home library from a JSON file
def open_json():
    if os.path.exists(LIBRARY_RECORD):
        with open(LIBRARY_RECORD, "r") as file:
            try:
                return json.load(file)
            except json.decoder.JSONDecodeError:
                return {}
    else:
        return {}

# Define a filename for the home library JSON file
LIBRARY_RECORD = "/Users/garybutterfield/GitHub/home-library/home_library.json"

# Load the existing home library or create an empty one
home_library = open_json()

while True:
    print("\nWelcome to your home library.\n")
    print("1. Add a library record\n2. Search for a library record\n3. List all library records\n4. Update a library record\n5. Delete library record\n6. Exit\n")

    choice = input("Please select an option: ")

    if choice == "1": # Add a library record
        print("\nYou chose to add a new book\n")

        book_title = input("Enter the book titleD: ")
        author = input("Enter the author: ")
        rating = input("Enter your rating out of 5*: ")
        review = input("Enter your review: ")

        book = {
            "TITLE": book_title,
            "AUTHOR": author,
            "RATING": rating,
            "REVIEW": review
        }

        home_library[book_title] = book
        save_json(home_library)

        print("Student record added successfully.")

    elif choice == "2": # Search for a library record
        print("\nYou chose to search for a library record\n")

        book_title = input("Enter Student ID to search: ")

        if book_title in home_library:
            student = home_library[book_title]
            print("Title:", book_title["TITLE"])
            print("Author:", author["AUTHOR"])
            print("Rating:", rating["RATING"])
            print("Review:", review["REVIEW"])
        else:
            print("Library record not found.")

    elif choice == "3": # List all library records
        print("\nYou chose to list all library books\n")

        for book_title, book in home_library.items():
            print(f"Title: {book_title}, Author: {author['AUTHOR']}, Rating: {rating['RATING']}, Review: {review['REVIEW']}")

    elif choice == "4": # Update library record
        print("\nYou chose to update a library record\n")

        book_title = input("Enter Student ID to update: ")

        if book_title in home_library:
            student = home_library[book_title]

            print("What would you like to update?")
            print("1. Book Title\n2. Author\n3. Rating\n4. Review")
            update_choice = input("Enter your choice: ")

            if update_choice == "1":
                new_author_title = input("Enter your new book title: ")
                student["TITLE"] = new_author_title
            elif update_choice == "2":
                new_age = input("Enter the new author: ")
                student["AUTHOR"] = new_age
            elif update_choice == "3":
                new_rating = input("Enter your new rating out of 5*: ")
                student["RATING"] = new_rating
            elif update_choice == "4":
                new_review = input("Enter your new review: ")
                student["REVIEW"] = new_review
            else:
                print("Invalid choice.")

            home_library[book_title] = book
            save_json(home_library)
            print("Library record updated successfully.")
        else:
            print("Student ID not found. Cannot update the record.")

    elif choice == "5": # Delete library record
        print("\nYou chose to delete a library record\n")

        library_record_to_delete = input("Enter the book title to delete: ")

        if library_record_to_delete in home_library:
            del home_library[library_record_to_delete]
            save_json(home_library)
            print(f"Library record with the {library_record_to_delete} book title has been deleted.")
        else:
            print("Library record not found. Cannot delete the record.")

    elif choice == "6": # Exit
        print("\nExiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")