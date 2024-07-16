def view_all_lend_book_list(book_lend_list):
    book_lend_list.clear()
    with open("book-lend-lists.csv", "r") as file_pointer:
            for line in file_pointer.readlines():
                line_splitted=line.strip().split(",")
                lend_book={
                        "title": line_splitted[0],
                        "person": line_splitted[1],
                        "phone": line_splitted[2],
                        "quantity": line_splitted[3],
                        "lendDate": line_splitted[4],
                        "returnDate": line_splitted[5],
                    }
                book_lend_list.append(lend_book)

    for lend_book in book_lend_list:
        print(f'Title: {lend_book["title"]} - Lend By: {lend_book["person"]} - Phone: {lend_book["phone"]} - Quantity: {lend_book["quantity"]} - Lend Date:{lend_book["lendDate"]} - Return Date:{lend_book["returnDate"]}')
    return book_lend_list 