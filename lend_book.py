import datetime
import restore_all_book_list


def lend_book(book_lend_list, book_list):
    found_search_result = False
    search_query = input("Search for Book That you want to Lend: ")
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
        print("No item found. If you want to search agin please type 6 to search again or type 0 to leave.")

    if found_search_result:
        selected_index = input("Enter the index number of Which book You want to lend: ")
        selected_index = int(selected_index)
        existing_quantity = book_list[selected_index - 1]["quantity"]
        #if book quantity is less than two then customer can't lend the book
        if int(existing_quantity) <2:
            print("Sorry! not enough books available to lend")
        else:    
            book_name = book_list[selected_index - 1]["title"]
            lend_by_person = input("Enter Your name: ")
            lend_by_person_phone = input("Enter Your phone number: ")
            quantity = input("Enter quantity: ")
            
            #if same person using same name and phone can't lend same book if he already have that book in lend list.
            # finding the item index in book list
            finding_person_key='lendby'
            finding_phone_key='phone'
            finding_book_key='title'
            def get_if_areadyhas_same_book_lend(finding_book_key,book_name,finding_person_key,lend_by_person,finding_phone_key,lend_by_person_phone,book_lend_list ):
                for book in book_lend_list:
                    if finding_book_key in book and finding_person_key in book and finding_phone_key in book:
                        if book[finding_book_key]==book_name and book[finding_person_key]==lend_by_person and book[finding_phone_key]==lend_by_person_phone:
                            if 'quantity' in book:
                                return book['quantity']
                            else:
                                return None
                return None
            hasbookAlread=get_if_areadyhas_same_book_lend(finding_book_key,book_name,finding_person_key,lend_by_person,finding_phone_key,lend_by_person_phone,book_lend_list)
            if hasbookAlread is not None:
                if int(hasbookAlread)!=0:
                     print(f"You aleady have this book:'{hasbookAlread}' pcs. Please return them first")
                else:
                    today = datetime.date.today()
                    current_date = today.strftime("%d/%m/%Y")
                    book_lend = {
                        "title": book_name,
                        "lendby": lend_by_person,
                        "phone": lend_by_person_phone,
                        "quantity": quantity,
                        "lendDate": current_date,
                        "returnDate": "0",
                    }
                    book_lend_list.clear()
                    book_lend_list.append(book_lend)

                    print("Lend Book Added successfully!")
                    print(book_lend_list)
                    with open("book-lend-lists.csv", "a") as file_pointer:
                        for book_lend in book_lend_list:
                            line = f"{book_lend['title']},{book_lend['lendby']},{book_lend['phone']},{book_lend['quantity']},{book_lend['lendDate']},{book_lend['returnDate']}\n"
                            file_pointer.write(line)

                    # updating csv file of book list after lend book
                    new_quantity = int(existing_quantity) - int(quantity)
                    book_list[selected_index - 1]["quantity"] = new_quantity

                    with open("books.csv", "w") as file_pointer:
                        for book in book_list:
                            line = f"{book['title']},{book['authors']},{book['publisher']},{book['isbn']},{book['publishYear']},{book['language']},{book['price']},{book['quantity']}\n"
                            file_pointer.write(line)

                    restore_all_book_list.restore_all_book_list(book_list)

    return book_lend_list
