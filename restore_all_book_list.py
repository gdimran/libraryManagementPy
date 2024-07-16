def restore_all_book_list(book_list):
    book_list.clear()
    with open("books.csv", "r") as file_pointer:
        for line in file_pointer.readlines():
            line_splitted = line.strip().split(",")
            book = {
                "title": line_splitted[0],
                "authors": line_splitted[1],
                "publisher": line_splitted[2],
                "isbn": line_splitted[3],
                "publishYear": line_splitted[4],
                "language": line_splitted[5],
                "price": line_splitted[6],
                "quantity": line_splitted[7],
            }
            book_list.append(book)

    return book_list
