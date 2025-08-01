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