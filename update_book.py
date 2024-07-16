import restore_all_book_list
def update_book(book_list):
    found_search_result = False
    search_query=input("Enter your text to search for update: ")
    for index, book in enumerate(book_list):
        if search_query.lower() in book["title"].lower():
            found_search_result = True
            print(
                f'{index+1}.{book["title"]} - {book["authors"]} - {book["publisher"]} - {book["isbn"]} - {book["publishYear"]} - {book["language"]} - {book["price"]} - {book["quantity"]}'
            )
        elif search_query.lower() in book["authors"].lower():
            found_search_result = True
            print(
                f'{index+1}.{book["title"]} - {book["authors"]} - {book["publisher"]} - {book["isbn"]} - {book["publishYear"]} - {book["language"]} - {book["price"]} - {book["quantity"]}'
            )
        elif search_query.lower() in book["isbn"].lower():
            found_search_result = True
            print(
                f'{index+1}.{book["title"]} - {book["authors"]} - {book["publisher"]} - {book["isbn"]} - {book["publishYear"]} - {book["language"]} - {book["price"]} - {book["quantity"]}'
            )

    if not found_search_result:
        print("No item found. Please insert 4 to search again or see the book list by type 2 or 0 for leave")

    if found_search_result:
        selected_index= input("Enter the index number to update: ")
        selected_index=int(selected_index)
        
        #new value input
        print("Please leave empty if you don't want to change any field.")
        new_title=input("Enter updte title: ")
        new_authors=input("Enter updte authors use coma for multiple authors: ")
        new_publisher= input("Enter updte book publisher name: ")
        new_isbn=input("Enter updte 13 digit ISBN number: ")
        new_publishYear=input("Enter updte book Publishing Year: ")
        new_language=input("Enter updte book language: ")
        new_price=input("Book update Price: ")
        new_quantity=input("Update the Quantity of books: ")

        user_input={
            "title": new_title,
            "authors": new_authors,
            "publisher": new_publisher,
            "isbn": new_isbn,
            "publishYear": new_publishYear,
            "language": new_language,
            "price": new_price,
            "quantity": new_quantity,
        }

        #function to update the item
        original_book=book_list[selected_index - 1]
        # Function to update dictionary conditionally
        def update_book(original_book, update_book):
            for key, value in update_book.items():
                if key in original_book and value != '':
                    original_book[key] = value
            return original_book

        # Update the dictionary
        updated_book = update_book(original_book, user_input)

        # Print the updated dictionary to verify
        #print(updated_book)
        
        print(book_list)
        print("Book updated succesfully.")

        with open("books.csv","w") as file_pointer:
            for book in book_list:
                line = f"{book['title']},{book['authors']},{book['publisher']},{book['isbn']},{book['publishYear']},{book['language']},{book['price']},{book['quantity']}\n"
                file_pointer.write(line)
        
        restore_all_book_list.restore_all_book_list(book_list)
    return book_list