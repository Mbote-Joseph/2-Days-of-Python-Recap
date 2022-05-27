books = set()

def add(books):
    file = open('books.csv', 'a')
    file.write(input('Enter a book: '))
    file.write(input('Enter the author: '))
    file.write(input('Enter the year: '))
    file.write(input('\n'))
    file.close()
    return True

add(books)
