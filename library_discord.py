import discord
from discord.ext import commands
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the bot token from the environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")

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
LIBRARY_RECORD = "home_library.json"

# Load the existing home library or create an empty one
home_library = open_json()

# Define intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.reactions = True

# Create the bot with intents
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def add_record(ctx):
    print("\nYou chose to add a new library record\n")

    book_title = input("Enter the book title: ")
    author = input("Enter the author: ")
    genre = input("Enter the genre (fiction, non-fiction, cooking): ")

    has_read = input("Have you read this book? (yes/no): ").lower()

    if has_read == "yes":
        rating = input("\nEnter your rating out of 5*: ")
        review = input("Enter your review: ")
    else: # Auto-fill with holding entry for not read
        rating = "Not Read"
        review = "Not Read"

    book = {
        "TITLE": book_title,
        "AUTHOR": author,
        "GENRE": genre,
        "RATING": rating,
        "REVIEW": review
    }

    home_library[book_title] = book
    save_json(home_library)

    await ctx.send("\nLibrary record added successfully.")

@bot.command()
async def search_record(ctx, search_term):
    print("\nYou chose to search for a library record\n")

    found_books = []

    for book_title, book in home_library.items():
        if (
            search_term.lower() in book_title.lower()
            or search_term.lower() in book["AUTHOR"].lower()
            or search_term.lower() in book["GENRE"].lower()
        ):
            found_books.append(book)

    if found_books:
        response = "\nMatching library records found:"
        for book in found_books:
            response += f"\n\nTitle: {book['TITLE']}\nAuthor: {book['AUTHOR']}\nGenre: {book['GENRE']}\nRating: {book['RATING']}\nReview: {book['REVIEW']}\n"
    else:
        response = "No matching library records found."

    await ctx.send(response)

@bot.command()
async def list_records(ctx):
    print("\nYou chose to list all library books\n")

    response = ""
    for book_title, book in home_library.items():
        response += f"Book title: {book_title}\nAuthor: {book['AUTHOR']}\nGenre: {book['GENRE']}\nRating: {book['RATING']}\nReview: {book['REVIEW']}\n\n"

    await ctx.send(response)

@bot.command()
async def update_record(ctx, book_title, update_choice, new_value):
    print("\nYou chose to update a library record\n")

    if book_title in home_library:
        book = home_library[book_title]

        if update_choice == "1":
            book["TITLE"] = new_value
        elif update_choice == "2":
            book["AUTHOR"] = new_value
        elif update_choice == "3":
            book["GENRE"] = new_value
        elif update_choice == "4":
            book["RATING"] = new_value
        elif update_choice == "5":
            book["REVIEW"] = new_value
        else:
            await ctx.send("Invalid choice.")

        home_library[book_title] = book
        save_json(home_library)
        await ctx.send("Library record updated successfully.")
    else:
        await ctx.send("Library record not found. Cannot update the record.")

@bot.command()
async def delete_record(ctx, library_record_to_delete):
    print("\nYou chose to delete a library record\n")

    if library_record_to_delete in home_library:
        del home_library[library_record_to_delete]
        save_json(home_library)
        await ctx.send(f"Library record with the {library_record_to_delete} book title has been deleted.")
    else:
        await ctx.send("Library record not found. Cannot delete the record.")

@bot.command()
async def exit_library(ctx):
    await ctx.send("\nLeaving the library.")
    await bot.close()

bot.run(BOT_TOKEN)
