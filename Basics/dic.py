books={
    'The Hobbit': {
        'author': 'J.R.R. Tolkien',
        'year': 1937
    },
    'The Lord of the Rings': {
        'author': 'J.R.R. Tolkien',
        'year': 1954
    },
    'The Catcher in the Rye': {
        'author': 'J.D. Salinger',
        'year': 1951
    },
}

for book in books:
    print(book)
    print(books[book]['author'])
    print(books[book]['year'])