from library_books import library_books
from datetime import datetime, timedelta

class Library:
    """
    A minimal library class.
    It uses a dictionary to store books and their status.
    Key: book title (str)
    Value: status (str, "Available" or "Checked Out")
    """
    def __init__(self):
        # We'll start with a few books already in our dictionary
        self.books = {
            "The Hobbit": "Available",
            "1984": "Available",
            "Dune": "Available"
        }

    def show_available(self):
        """Prints all books that are "Available"."""
        print("\n--- Available Books ---")
        found = False
        for title, status in self.books.items():
            if status == "Available":
                print(f"- {title}")
                found = True
        if not found:
            print("No books are currently available.")
        print("-----------------------")

    def check_out(self, title):
        """Checks out a book if it is available."""
        if title not in self.books:
            print(f"Sorry, we don't have the book '{title}'.")
        elif self.books[title] == "Available":
            self.books[title] = "Checked Out"
            print(f"You checked out '{title}'.")
        else:
            print(f"Sorry, '{title}' is already checked out.")

    def return_book(self, title):
        """Returns a book if it is checked out."""
        if title not in self.books:
            print(f"Sorry, we don't have the book '{title}'.")
        elif self.books[title] == "Checked Out":
            self.books[title] = "Available"
            print(f"You returned '{title}'.")
        else:
            print(f"'{title}' is already on the shelf.")

# --- Main Program ---
# This part is outside the class and runs the menu
def main():
    # Create our one Library object
    lib = Library()
    print("Welcome to the Tiny Library!")

    # A simple, endless loop for the menu
    while True:
        # A single-line menu
        print("\n(1) Show available (2) Check out (3) Return (4) Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            lib.show_available()
            
        elif choice == '2':
            book_title = input("Enter book title to check out: ")
            lib.check_out(book_title)
            
        elif choice == '3':
            book_title = input("Enter book title to return: ")
            lib.return_book(book_title)
            
        elif choice == '4':
            print("Goodbye!")
            break  # This exits the 'while True' loop
            
        else:
            print("Invalid choice. Please pick 1, 2, 3, or 4.")

# This line runs the 'main' function when you start the script
if __name__ == "__main__":
    main()


if __name__ == "__main__":
    # You can use this space to test your functions
    pass
