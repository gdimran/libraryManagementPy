import datetime
import restore_all_book_list
import restore_all_lend_book_list


def return_lend_book(book_lend_list, book_list):
    found_search_result = False
    search_query = input("Search for Book That you want to return: ")
    for index, book_lend in enumerate(book_lend_list):
        if search_query.lower() in book_lend["title"].lower():
            found_search_result = True
            print(
                f'{index+1}.{book_lend["title"]} - {book_lend["lendby"]} - {book_lend["phone"]} - {book_lend["quantity"]} - {book_lend["lendDate"]} - {book_lend["returnDate"]}'
            )
        elif search_query.lower() in book_lend["lendby"].lower():
            found_search_result = True
            print(
                f'{index+1}.{book_lend["title"]} - {book_lend["lendby"]} - {book_lend["phone"]} - {book_lend["quantity"]} - {book_lend["lendDate"]} - {book_lend["returnDate"]}'
            )
        elif search_query.lower() in book_lend["phone"].lower():
            found_search_result = True
            print(
                f'{index+1}.{book_lend["title"]} - {book_lend["lendby"]} - {book_lend["phone"]} - {book_lend["quantity"]} - {book_lend["lendDate"]} - {book_lend["returnDate"]}'
            )

    if not found_search_result:
        print("No item found If you want to search agin please type 7 to search again or type 8 to see the list or type 0 to leave.")

    if found_search_result:
        selected_index = input(
            "Enter the index number of Which book You want to return: "
        )
        selected_index = int(selected_index)
        book_name = book_lend_list[selected_index - 1]["title"]
        today = datetime.date.today()
        return_date = today.strftime("%d/%m/%Y")
        quantity = book_lend_list[selected_index - 1]["quantity"]
        book_lend_list[selected_index - 1]["quantity"] = 0
        book_lend_list[selected_index - 1]["returnDate"] = return_date

        print("Lend Book Returned successfully!")
        with open("book-lend-lists.csv", "w") as file_pointer:
            for book_lend in book_lend_list:
                line = f"{book_lend['title']},{book_lend['lendby']},{book_lend['phone']},{book_lend['quantity']},{book_lend['lendDate']},{book_lend['returnDate']}\n"
                file_pointer.write(line)

        # finding the item index in book list
        index = next((index for index, d in enumerate(book_list) if d["title"] == book_name), None)
        
        # Update the book quantity when book return
        if index is not None:
            existing_quantity = book_list[index]["quantity"]
            new_quantity = int(existing_quantity) + int(quantity)
            book_list[index]["quantity"] = new_quantity

        with open("books.csv", "w") as file_pointer:
            for book in book_list:
                line = f"{book['title']},{book['authors']},{book['publisher']},{book['isbn']},{book['publishYear']},{book['language']},{book['price']},{book['quantity']}\n"
                file_pointer.write(line)

        restore_all_book_list.restore_all_book_list(book_list)
        restore_all_lend_book_list.restore_all_lned_book_list(book_lend_list)


