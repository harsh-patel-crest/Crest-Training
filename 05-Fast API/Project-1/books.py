from fastapi import Body, FastAPI

app=FastAPI()

Books=[
    {
        'title': 'Title 1', 'author': 'Author 1', 'category': 'Science'
    },
    {
        'title': 'Title 2', 'author': 'Author 2', 'category': 'Science'
    },
    {
        'title': 'Title 3', 'author': 'Author 3', 'category': 'Maths'
    },
    {
        'title': 'Title 4', 'author': 'Author 1', 'category': 'History'
    },
    {
        'title': 'Title 5', 'author': 'Author 2', 'category': 'Maths'
    }
]

@app.get('/books')
async def read_all_books():
    return Books

@app.get('/books/{book_title}')
async def read_all_books(book_title:str):
    for book in Books:
        if book.get('title').casefold()==book_title.casefold():
            return book

@app.get('/books/')
async def read_category_by_query(category:str):
    books_to_return=[]
    for book in Books:
        if book.get('category').casefold()==category.casefold():
            books_to_return.append(book)
    return books_to_return

# @app.get('/books/byAuthor/{book_author}/')
# async def get_all_books_by_author(book_author:str):
#     books_to_return=[]
#     for book in Books:
#         if book.get('author').casefold()==book_author.casefold():
#             books_to_return.append(book)
#     return books_to_return

@app.get('/books/byAuthor/')
async def get_all_books_by_author(book_author:str):
    books_to_return=[]
    for book in Books:
        if book.get('author').casefold()==book_author.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get('/books/{book_author}/')
async def read_author_category_by_query(category:str, book_author:str):
    books_to_return=[]
    for book in Books:
        if book.get('author').casefold()==book_author.casefold() and book.get('category').casefold()==category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post('/books/create_book')
async def create_book(new_book=Body()):
    Books.append(new_book)

@app.put('/books/update_book')
async def update_book(updated_book=Body()):
    for i in range(len(Books)):
        if Books[i].get('title').casefold()==updated_book.get('title').casefold():
            Books[i]=updated_book

@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title:str):
    for i in range(len(Books)):
        if Books[i].get('title').casefold()==book_title.casefold():
            Books.pop(i)
            break
