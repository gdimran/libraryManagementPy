def create_book(book_list):
    book_list.clear()
    title = input("Enter book title: ")
    authors=input("Enter authors use coma for multiple authors: ")
    publisher= input("Enter book publisher name: ")
    isbn=input("Enter 13 digit ISBN number: ")
    publishYear=input("Enter book Publishing Year: ")
    language=input("Enter book language: ")
    price=float(input("Book Price: "))
    quantity=int(input("Number of books: "))

    #authors= authors.split(',')
    
    book={
        "title": title,
        "authors": authors,
        "publisher": publisher,
        "isbn": isbn,
        "publishYear": publishYear,
        "language": language,
        "price": price,
        "quantity": quantity,
    }
    
    book_list.append(book)

    print("Book Added successfully!")
    with open("books.csv", "a") as file_pointer:
        for book in book_list:
            line = f"{book['title']},{book['authors']},{book['publisher']},{book['isbn']},{book['publishYear']},{book['language']},{book['price']},{book['quantity']}\n"
            file_pointer.write(line)
    return book_list