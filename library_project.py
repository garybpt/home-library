import json, os

# Function to save the home library to a JSON file in alphabetical order
def save_json(home_library):
    sorted_home_library = dict(sorted(home_library.items()))
    with open(LIBRARY_RECORD, "w") as file: # The global variable is being converted to a local variable as 'file'
        json.dump(sorted_home_library, file, indent=4, sort_keys=True) # The library book is being saved in sorted (alphabetical) order


# Function to load the home library from a JSON file
def open_json():
    if os.path.exists(LIBRARY_RECORD): # Using os, the dictionary location is being searched for
        with open(LIBRARY_RECORD, "r") as file: # If the dictionary exists, the global variable is being converted to a local variable as 'file'
            try:
                return json.load(file) # The json file is being opened
            except json.decoder.JSONDecodeError: # An exception is handled if JSONDecodeError error occurs
                return {}
    else:
        return {}
    

# Function to add a new book to the library
def add_library_book():
    print("\nYou chose to add a new library book\n")

    book_title = input("Enter the book title: ")
    author = input("Enter the author: ")
    genre = input("Enter the genre (fiction, non-fiction, cooking): ")

    has_read = input("Have you read this book? (yes/no): ").lower() # Converts the answer to lower case to reduce the risk of errors

    if has_read == "yes":
        last_read = input("\nYear last read: ")
        rating = input("\nEnter your rating out of 5*: ")
        review = input("Enter your review: ")
    else: # Auto-fill with holding entry if not applicable
        last_read = "N/A"
        rating = "N/A"
        review = "N/A"

    book = { # This is the dictionary template with key values that the script will follow
        "TITLE": book_title,
        "AUTHOR": author,
        "GENRE": genre,
        "LAST_READ": last_read,
        "RATING": rating,
        "REVIEW": review
    }

    home_library[book_title] = book
    save_json(home_library) # Once the info is in place, the script calls the save function to update the library

    print("\nLibrary book added successfully.")


# Function to search the library for a specific book
def search_library_book():
    print("\nYou chose to search for a library book\n")

    search_term = input("Enter book title, author, year read, or genre (fiction, non-fiction, or cooking) to search the library: ")

    found_books = [] # Any books found will be added to a temporary dictionary to be returned

    for book_title, book in home_library.items():
        if (
            search_term.lower() in book_title.lower() # All search terms are converted to lower case to reduce the risk of errors
            or search_term.lower() in book["LAST_READ"].lower() # All books that contain the search term will be added to the temporary dictionary
            or search_term.lower() in book["AUTHOR"].lower()
            or search_term.lower() in book["GENRE"].lower()
        ):
            found_books.append(book) # Here, the found book(s) will be added to the temporary dictionary

    if found_books:
        print("\nMatching library book found:")
        for book in found_books:
            print("\nTitle:", book["TITLE"]) # This is the order that the found book(s) will be returned, which mirrors the input template
            print("Author:", book["AUTHOR"])
            print("Genre:", book["GENRE"])
            print("Last Read:", book["LAST_READ"])
            print("Rating:", book["RATING"])
            print("Review:", book["REVIEW"])
            print() # Add an empty line between each book
    else:
        print("No matching library book found.")


# Function to list all books in the library
def list_library_books():
    print("\nYou chose to list all library books\n")

    for book_title, book in home_library.items(): # This will list all library books using the below template
        print(f"Book title: {book_title}")
        print(f"Author: {book['AUTHOR']}")
        print(f"Genre: {book['GENRE']}")
        print("Last Read:", book["LAST_READ"])
        print(f"Rating: {book['RATING']}")
        print(f"Review: {book['REVIEW']}")
        print() # Add an empty line between each book


# Function to update an existing library book
def update_library_book():
    print("\nYou chose to update a library book\n")

    book_title = input("Enter the book title to update: ")

    if book_title in home_library:
        book = home_library[book_title] 
        # This function needs a little more work, but at the moment the user can update any one bit of information at a time before returning to the main menu
        # Ideally, this would have it's own while loop, and only return to main menu when instructed to do so

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
        save_json(home_library) # The save function is called and library dictionary updated
        print("Library book updated successfully.")
    else:
        print("Library book not found. Cannot update the book.")


# Function to delete a book from the library
def delete_library_book():
    print("\nYou chose to delete a library book\n")

    library_record_to_delete = input("Enter the book title to delete: ")

    if library_record_to_delete in home_library:
        del home_library[library_record_to_delete] # If the library book is found it is deleted from the library dictionary
        save_json(home_library) # The save function is called and library dictionary updated
        print(f"Library book with the {library_record_to_delete} book title has been deleted.")
    else:
        print("Library book not found. Cannot delete the book.")


# Define a filename for the home library JSON file
LIBRARY_RECORD = "/Users/garybutterfield/GitHub/home-library/home_library.json" # This is a global variable and location of the library dictionary json file

# Load the existing home library or create an empty one
home_library = open_json()


# The start of the library loop
while True: # I have removed the exit function in prep for Discord so this loop will always be true unless and error occurs
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