class BookClass:
    book_list = []

    def __init__(self, title, author, isbn, num_of_copies):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.num_of_copies=num_of_copies

    def display(self):
        print(f"Book Title={self.title}.\nAuthor={self.author}.\nisbn={self.isbn}.\nNumber of copies={self.num_of_copies}.")
