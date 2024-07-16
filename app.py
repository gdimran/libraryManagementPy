import create_book
import view_all_book_list
import search_books
import restore_all_book_list
import remove_book
import update_book
import lend_book
import restore_all_lend_book_list
import view_all_lend_book_list
import return_lend_book

book_list = []
book_lend_list = []



def restore_book_lists_exists(file_path):
    try:
        restore_all_book_list.restore_all_book_list(book_list)
    except FileNotFoundError:
        print(f"The Books database is empty Please insert data.")
def view_book_lists_exists(file_path):
    try:
        view_all_book_list.view_all_book_list(book_list)
    except FileNotFoundError:
        print(f"The Books database is empty Please insert data.")

def restore_lend_book_lists_if_exists(file_path):
    try:
        restore_all_lend_book_list.restore_all_lned_book_list(book_lend_list)
    except FileNotFoundError:
        print(f"The lend database is empty Please insert data.")
def view_lend_book_lists_if_exists(file_path):
    try:
        view_all_lend_book_list.view_all_lend_book_list(book_lend_list)
    except FileNotFoundError:
        print(f"The lend database is empty Please insert data.")




# Example usage:
books = './books.csv'
lend_books = './book-lend-lists.csv'



print("Welcome to Library management system!")

menu_text = """
Your Options:
1. Add New Book
2. View All Books
3. Search Books
4. Remove Books
5. Update Books
6. Lend Books
7. Return Books
8. Lend Books List
0. Exit
"""

while True:

    restore_book_lists_exists(books)
    restore_lend_book_lists_if_exists(lend_books)
    print(menu_text)
    choice = input("Enter your choice: ")

    if choice == "1":
        book_list = create_book.create_book(book_list)
    elif choice == "2":
        view_book_lists_exists(books)
    elif choice == "3":
        search_books.search_books(book_list)
    elif choice == "4":
        remove_book.remove_book(book_list)
    elif choice == "5":
        update_book.update_book(book_list)
    elif choice == "6":
        lend_book.lend_book(book_lend_list,book_list)
    elif choice == "7":
        return_lend_book.return_lend_book(book_lend_list,book_list)
    elif choice == "8":
        view_lend_book_lists_if_exists(lend_books)
    elif choice == "0":
        print("Thanks for using the application.")
        break
    else:
        print("Wrong Choice!")
