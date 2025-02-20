from collections import deque


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return self.title + " " + self.author

class Library:
    def __init__(self, name):
        self.name = name
        self.books = deque()

    def __str__(self):
        return f"{self.name} :: {self.books}"

    def add_book(self, book):
        self.books.append(book)


    def remove_book(self, book):
        found_index = None
        for index in range(len(self.books)):
            current_book = self.books[index]
            if book.title == current_book.title and book.author == current_book.author:
                found_index = index
                break

        if found_index is not None:
            del self.books[found_index]

    def search_books(self, search_string):
        value = search_string.lower()
        return [
            x
            for x in self.books if value in x.author.lower() or value in x.title.lower()
        ]
