import json, os

class LibraryManager:

    def __init__(self, filename):
        self.filename = filename
        self.library = self.load_library()

    def load_library(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                try:
                    return json.load(file)
                except json.decoder.JSONDecodeError:
                    return {}
        return {}
    
    def save_library(self):
        with open(self.filename, "w") as file:
            json.dump(dict(sorted(self.library.items)))

    def add_record(self):
        print('\nYou chose to add a new library book.\n')
        title = input('Enter the book title: ')
        author = input('Enter the author: ')
        genre = input('Enter the genre(fiction, non-fiction, cooking): ')

        has_read = input('Have you read this book? (yes/no): ').lower()

        if has_read== 'yes':
            last_record = input('Year last read: ')
            rating = input('Enter your rating out of 5*: ')
            review = input(' Enter your review: ')
        else:
            last_read = rating = review = 'N/A'

        self.library[title] = {
            'TITLE': title,
            'AUTHOR': author,
            'GENRE': genre,
            'LAST_READ': last_read,
            'RATING': rating,
            'REVIEW': review
        }
        self.save_library()
        print('Library book added successfully.')

    def search_records(self):
        print('\nYou chose to search for a library book\n')
        query = input('Enter the book title, author, year read, or genre to search: ').lower()
        found = [
            book for book in self.library.values()
            if any(query in str(value).lower() for key, value in book.items() if key in ['TITLE', 'AUTHOR', 'GENRE', 'LAST_READ'])
        ]
        if found:
            print('/nMatching library books found: ')
            for book in found:
                self.print_record(book)
        else:
            print('No matching library books found.')

    def list_records(self):
        print('\nYou chose to list all library books\m')
        for book in self.library.values():
            self.print_record(book)

    def update_record(self):
        print('\nYou chose to update a library book\n')
        title = input('Enter the book title to update: ')

        if title not in self.library:
            print('Library book not found.')
            return
        
        book = self.library[title]
        print('1. Book Title\n2. Author\n3. Genre\n4. Last Read\n5. Rating\n6. Review')
        field_map = {
            '1': 'TITLE',
            '2': 'AUTHOR',
            '3': 'GENRE',
            '4': 'LAST_READ',
            '5': 'RATING',
            '6': 'REVIEW'
        }
        choice = input('Enter your choice: ')
        field = field_map.get(choice)

        if not field:
            print('Invalid choice.')
            return
        new_value = input(f"Enter new value for {field.replace('_', ' ').title()}: ")
        book[field] = new_value
        if field == 'TITLE':
            self.library[new_value] = self.library.pop(title)
            self.save_library()
            print('Library book updated successfully.')

    def delete_record(self):
        print('\nYou chose to delete a library book\n')
        title = input('Enter the book title to delete: ')

        if title in self.library:
            del self.library[title]
            self.save_library()
            print(f'Library book, {title}, has been deleted.')
        else:
            print('Library book not found.')
        
    def print_record(self, book):
        print(f"\nTitle: {book['TITLE']}")
        print(f"Author: {book['AUTHOR']}")
        print(f"Genre: {book['GENRE']}")
        print(f"Last Read: {book['LAST_READ']}")
        print(f"Rating: {book['RATING']}")
        print(f"Review: {book['REVIEW']}\n")

    def run(self):
        while True:
            print('\nWelcome to your home library. \n')
            print('1. Add a library book\n2. Search for a library book\n3. List all library books\n4. Update a library book\n5. Delete a library book\n')

            choice = input('Please select an option: ')

            if choice == '1':
                self.add_record
            elif choice == '2':
                self.search_records
            elif choice == '3':
                self.list_records
            elif choice == '4':
                self.update_record
            elif choice == '5':
                self.delete_record
            else:
                print('Please select a valid option')
        
if __name__ == '__main__':
    LIBRARY_RECORD = "/Users/garybutterfield/GitHub/home-library/home_library.json"
    manager = LibraryManager(LIBRARY_RECORD)
    manager.run()