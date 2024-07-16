def search_books(book_list):
    found_search_result = False
    search_term = input("Enter what you want to search: ")

    for book in book_list:

        search_term_lower = search_term.lower()
        title_lowercase = book["title"].lower()
        authors_lowercase = book["authors"].lower()
        isbn_lowercase = book["isbn"].lower()

        if search_term_lower in title_lowercase:
            found_search_result = True
            print("Found:\n")
            print(
                f'Title: {book["title"]} - Author(s): {book["authors"]} - Publisher: {book["publisher"]} - ISBN: {book["isbn"]} - Publishing Year:{book["publishYear"]} - Language:{book["language"]} - Price:{book["price"]} - Quantity: {book["quantity"]}'
            )
        elif search_term_lower in authors_lowercase:
            found_search_result = True
            print("Found:\n")
            print(
                f'Title: {book["title"]} - Author(s): {book["authors"]} - Publisher: {book["publisher"]} - ISBN: {book["isbn"]} - Publishing Year:{book["publishYear"]} - Language:{book["language"]} - Price:{book["price"]} - Quantity: {book["quantity"]}'
            )
        elif search_term_lower in isbn_lowercase:
            found_search_result = True
            print("Found:\n")
            print(
                f'Title: {book["title"]} - Author(s): {book["authors"]} - Publisher: {book["publisher"]} - ISBN: {book["isbn"]} - Publishing Year:{book["publishYear"]} - Language:{book["language"]} - Price:{book["price"]} - Quantity: {book["quantity"]}'
            )
    if not found_search_result:
        print("No item found If you want to search agin please type 3 to search again or type 0 to leave.")
    return
