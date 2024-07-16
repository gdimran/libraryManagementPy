import restore_all_book_list
def remove_book(book_list):
    found_search_result = False
    search_query=input("Enter your text to search for remove: ")
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
        print("No item found")

    if found_search_result:
        selected_index= input("Enter the index number to remove: ")
        selected_index=int(selected_index)
        book_list.pop(selected_index-1)
        print("Book removed succesfully.")

        with open("books.csv","w") as file_pointer:
            for book in book_list:
                line = f"{book['title']},{book['authors']},{book['publisher']},{book['isbn']},{book['publishYear']},{book['language']},{book['price']},{book['quantity']}\n"
                file_pointer.write(line)
        
        restore_all_book_list.restore_all_book_list(book_list)

    return book_list
    
