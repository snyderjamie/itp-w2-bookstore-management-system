# we are builging a collection, not extracting a collection from string
def create_bookstore(name):
    # setter and getter function
    # store = name
    store = {
        'name': name,
        'authors': [],
        'books': []
    }
    return store


def get_bookstore_name(bookstore):
    # this is the getter portion of the fuction
    return bookstore['name']


def add_author(bookstore, name, nationality):
    # from the assert statement we found out that we need 
    # to the creat a dictionary
    # store is the first value, 
    author = {
        'name': name, 
        'nationality': nationality,
    }
    bookstore['authors'].append(author)

    return author


def get_author_by_name(bookstore, name):
    # for author in bookstore['authors']:
    #    if name == author['name']:
    #       return author
    author_list = bookstore['authors']
    
    for author in author_list:
        if name == author['name']:
            return author

def add_book(bookstore, title, isbn, author):
    book = {
        'title' = title, 
        'isbn' = isbn,
        'author' = author
    }
    bookstore['book'].append(book)
    return book


def get_book_by_title(bookstore, title):
    book_list = bookstore['book']
    for title in book['title']:
        if title == book['title']:
            return book


def get_books_by_author(bookstore, author):
    books = []
    book_list = bookstore['books']
    for book in book_list:
        if author == book['author']:
            books.append(book)
    return books
    
