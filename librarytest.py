import unittest

from bookbot.library import Library, Book


class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Set up a new Library instance before each test."""
        self.library = Library("Test Library")
        self.books = [
            Book("The Trial", "Franz Kafka"),
            Book("The Catcher in the Rye", "J.D. Salinger"),
            Book("To Kill a Mockingbird", "Harper Lee"),
            Book("1984", "George Orwell"),
            Book("The Great Gatsby", "F. Scott Fitzgerald"),
        ]

        # Add books to library
        for book in self.books:
            self.library.add_book(book)

    def test_add_book(self):
        """Test adding a book to the library."""
        new_book = Book("Moby Dick", "Herman Melville")
        self.library.add_book(new_book)
        self.assertIn(new_book, self.library.books, "Failed to add book to library")

    def test_remove_book(self):
        """Test removing a book from the library."""
        book_to_remove = self.books[0]  # The Trial by Franz Kafka
        self.library.remove_book(book_to_remove)
        self.assertNotIn(book_to_remove, self.library.books, "Book was not removed")

    def test_remove_nonexistent_book(self):
        """Test removing a book that does not exist in the library."""
        book_to_remove = Book("Nonexistent Book", "Unknown Author")
        self.library.remove_book(book_to_remove)
        self.assertEqual(len(self.library.books), len(self.books), "Removing a nonexistent book should not change the library")

    def test_search_books_by_title(self):
        """Test searching for books by title."""
        search_results = self.library.search_books("Great")
        expected_titles = ["The Great Gatsby"]
        actual_titles = [book.title for book in search_results]
        self.assertEqual(actual_titles, expected_titles, "Title search returned incorrect results")

    def test_search_books_by_author(self):
        """Test searching for books by author."""
        search_results = self.library.search_books("Orwell")
        expected_titles = ["1984"]
        actual_titles = [book.title for book in search_results]
        self.assertEqual(actual_titles, expected_titles, "Author search returned incorrect results")

    def test_search_case_insensitive(self):
        """Test case insensitivity in search."""
        search_results = self.library.search_books("salinger")
        expected_titles = ["The Catcher in the Rye"]
        actual_titles = [book.title for book in search_results]
        self.assertEqual(actual_titles, expected_titles, "Search should be case insensitive")


if __name__ == "__main__":
    unittest.main()