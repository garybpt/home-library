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
    

def add_library_book():
    print("\nYou chose to add a new library book\n")

    book_title = input("Enter the book title: ")
    author = input("Enter the author: ")
    genre = input("Enter the genre (fiction, non-fiction, cooking): ")

    has_read = input("Have you read this book? (yes/no): ").lower()

    if has_read == "yes":
        last_read = input("\nYear last read: ")
        rating = input("\nEnter your rating out of 5*: ")
        review = input("Enter your review: ")
    else: # Auto-fill with holding entry if not applicable
        last_read = "N/A"
        rating = "N/A"
        review = "N/A"

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

    print("\nLibrary book added successfully.")


def search_library_book():
    print("\nYou chose to search for a library book\n")

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
        print("\nMatching library book found:")
        for book in found_books:
            print("\nTitle:", book["TITLE"])
            print("Author:", book["AUTHOR"])
            print("Genre:", book["GENRE"])
            print("Last Read:", book["LAST_READ"])
            print("Rating:", book["RATING"])
            print("Review:", book["REVIEW"])
            print() # Add an empty line between each book
    else:
        print("No matching library book found.")


def list_library_books():
    print("\nYou chose to list all library books\n")

    for book_title, book in home_library.items():
        print(f"Book title: {book_title}")
        print(f"Author: {book['AUTHOR']}")
        print(f"Genre: {book['GENRE']}")
        print("Last Read:", book["LAST_READ"])
        print(f"Rating: {book['RATING']}")
        print(f"Review: {book['REVIEW']}")
        print() # Add an empty line between each book

def update_library_book():
    print("\nYou chose to update a library book\n")

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
        print("Library book updated successfully.")
    else:
        print("Library book not found. Cannot update the book.")

def delete_library_book():
    print("\nYou chose to delete a library book\n")

    library_record_to_delete = input("Enter the book title to delete: ")

    if library_record_to_delete in home_library:
        del home_library[library_record_to_delete]
        save_json(home_library)
        print(f"Library book with the {library_record_to_delete} book title has been deleted.")
    else:
        print("Library book not found. Cannot delete the book.")

# Define a filename for the home library JSON file
LIBRARY_RECORD = "/Users/garybutterfield/GitHub/home-library/home_library.json"

# Load the existing home library or create an empty one
home_library = open_json()

while True:
    print("\nWelcome to your home library.\n")
    print("1. Add a library book\n2. Search for a library book\n3. List all library book\n4. Update a library book\n5. Delete a library book\n")

    choice = input("Please select an option: ")

    if choice == "1": # Add a library book
        add_library_book()
        

    elif choice == "2":  # Search for a library book
        search_library_book()

    elif choice == "3": # List all library book
        list_library_books()

    elif choice == "4": # Update library book
        update_library_book()

    elif choice == "5": # Delete library book
        delete_library_book()

    else:
        print("Invalid choice. Please select a valid option.")