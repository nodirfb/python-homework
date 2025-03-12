import json

# 3. Task: JSON Modification
#    1. Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.

def reading_books_json():
    with open('books.json') as f:
        books = json.load(f)
    return books

def writing_books_to_json(obj):
    with open('books.json', 'w')as f:
        json.dump(obj,f,indent=2)

def book_list():
    books = reading_books_json()
    print('   📚Book list: ')
    for index, book in enumerate(books):
        print(f'Book id: {index}')
        print('title:', book['title'],)
        print('author:', book['author'])
        print('year:', book['year'])
        print('genre:', book['genre'], end='\n\n')


def add_new_book(title,author,year,genre):
    try:
        books = reading_books_json()
        new_book = {
            'title':f'{title}',
            'author':f'{author}',
            'year':f'{year}',
            'genre':f'{genre}'
        }
        books.append(new_book)

        writing_books_to_json(books)
        print('\n✅Book sucessfully Added!')
        
    except FileNotFoundError:
        books = []
        new_book = {
            'title':f'{title}',
            'author':f'{author}',
            'year':f'{year}',
            'genre':f'{genre}'
        }
        books.append(new_book)

        writing_books_to_json(books)
        print('\n✅Book sucessfully Added!')

def update_existing_book():
    try:
        books = reading_books_json()
        book_list()
        
        id = int(input('Please choose the book id that you want to update: '))

        title = input('title: ').strip()
        aurthor = input('author: ').strip()
        year = input('year: ').strip()
        genre = input('genre: ').strip()

        books[id]['title'] = title
        books[id]['author'] = aurthor
        books[id]['year'] = year
        books[id]['genre'] = genre

        writing_books_to_json(books)
        
        print('\n✅Book sucessfully updated!')
        
    except FileNotFoundError:
        print('You did not add any books yet')

def delete_books():
    try:
        books = reading_books_json()
        book_list()

        id = int(input('Please choose the book id that you want to delete: '))

        del books[id]

        writing_books_to_json(books)
        print('\n✅Book sucessfully deleted!')
    except FileNotFoundError:
        print('You did not add any books yet')


stop = True
while stop:
    print('\n1. Add new book')
    print('2. Update existing book')
    print('3. Delete existing book')
    print('0. Exit')

    command = int(input('Choose the command: '))

    if command == 1:
        title = input('title: ').strip()
        author = input('author: ').strip()
        year = input('year: ').strip()
        genre = input('genre: ').strip()
        add_new_book(title,author,year,genre)
    elif command == 2:
        update_existing_book()
    elif command == 3:
        delete_books()
    elif command == 0:
        stop = False
    
        