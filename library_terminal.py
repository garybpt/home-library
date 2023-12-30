import json
import os

# Function to save the home library to a JSON file in alphabetical order
def save_json(home_library):
    sorted_home_library = dict(sorted(home_library.items()))
    with open(LIBRARY_RECORD, "w") as file:
        json.dump(sorted_home_library, file, indent=4, sort_keys=True)

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
    print("1. Add a library record\n2. Search for a library record\n3. List all library records\n4. Update a library record\n5. Delete a library record\n6. Exit\n")

    choice = input("Please select an option: ")

    if choice == "1": # Add a library record
        print("\nYou chose to add a new library record\n")

        book_title = input("Enter the book title: ")
        author = input("Enter the author: ")
        genre = input("Enter the genre (fiction, non-fiction, cooking): ")

        has_read = input("Have you read this book? (yes/no): ").lower()

        if has_read == "yes":
            last_read = input("\nYear last read: ")
            rating = input("\nEnter your rating out of 5*: ")
            review = input("Enter your review: ")
        else: # Auto-fill with holding entry for not read
            last_read = "Not Read"
            rating = "Not Read"
            review = "Not Read"

        book = {
            "TITLE": book_title,
            "AUTHOR": author,
            "GENRE": genre,
            "LAST_READ": last_read,
            "RATING": rating,
            "REVIEW": review
        }

        home_library[book_title] = book
        save_json(home_library)

        print("\nLibrary record added successfully.")

    elif choice == "2":  # Search for a library record
        print("\nYou chose to search for a library record\n")

        search_term = input("Enter book title, author, year read, or genre (fiction, non-fiction, or cooking) to search the library: ")

        found_books = []

        for book_title, book in home_library.items():
            if (
                search_term.lower() in book_title.lower()
                or search_term.lower() in book["LAST_READ"].lower()
                or search_term.lower() in book["AUTHOR"].lower()
                or search_term.lower() in book["GENRE"].lower()
            ):
                found_books.append(book)

        if found_books:
            print("\nMatching library records found:")
            for book in found_books:
                print("\nTitle:", book["TITLE"])
                print("Author:", book["AUTHOR"])
                print("Genre:", book["GENRE"])
                print("Last Read:", book["LAST_READ"])
                print("Rating:", book["RATING"])
                print("Review:", book["REVIEW"])
                print() # Add an empty line between each book
        else:
            print("No matching library records found.")

    elif choice == "3": # List all library records
        print("\nYou chose to list all library books\n")

        for book_title, book in home_library.items():
            print(f"Book title: {book_title}")
            print(f"Author: {book['AUTHOR']}")
            print(f"Genre: {book['GENRE']}")
            print("Last Read:", book["LAST_READ"])
            print(f"Rating: {book['RATING']}")
            print(f"Review: {book['REVIEW']}")
            print() # Add an empty line between each book

    elif choice == "4": # Update library record
        print("\nYou chose to update a library record\n")

        book_title = input("Enter the book title to update: ")

        if book_title in home_library:
            book = home_library[book_title]

            print("What would you like to update?")
            print("1. Book Title\n2. Author\n3. Genre\n4. Last Read\n5. Rating\n6. Review")
            update_choice = input("Enter your choice: ")

            if update_choice == "1":
                new_author_title = input("Enter your new book title: ")
                book["TITLE"] = new_author_title
            elif update_choice == "2":
                new_age = input("Enter the new author: ")
                book["AUTHOR"] = new_age
            elif update_choice == "3":
                new_genre = input("Enter the new genre: ")
                book["GENRE"] = new_genre
            elif update_choice == "4":
                new_year = input("Year read: ")
                book["LAST_READ"] = new_year
            elif update_choice == "5":
                new_rating = input("Enter your new rating out of 5*: ")
                book["RATING"] = new_rating
            elif update_choice == "6":
                new_review = input("Enter your new review: ")
                book["REVIEW"] = new_review
            else:
                print("Invalid choice.")

            home_library[book_title] = book
            save_json(home_library)
            print("Library record updated successfully.")
        else:
            print("Library record not found. Cannot update the record.")

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
        print("\nLeaving the library.")
        break

    else:
        print("Invalid choice. Please select a valid option.")