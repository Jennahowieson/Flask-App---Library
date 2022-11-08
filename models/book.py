class Book:
    def __init__(self,title,author,genre,checkedin):
        self.title = title
        self.author = author
        self.genre = genre
        self.checkedin = checkedin

    def unspace_title(self,title):
        return self.title.replace(" ","")
