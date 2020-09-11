class Book():
    
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
        
    def __str__(self):
        return f'{self.title} by {self.author}'
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book object has been deleted")
        
book_obj = Book("A Brief History of Time","Stephen Hawkins",343)

print(book_obj,f"length of {len(book_obj)} pages")

del book_obj


