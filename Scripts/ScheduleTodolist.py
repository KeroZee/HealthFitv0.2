class Quotes:
    def __init__(self, contents):
        self.contents = contents

    def get_contents(self):
        return self.contents

    def set_contents(self, contents):
        self.contents = contents


    def __str__(self):
        s = f'{self.get_contents()}'
        return s

class Author(Quotes):
    def __init__(self, contents, author):
        super().__init__(contents)
        self.author = author

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def __str__(self):
        s = super().__str__()
        s = f'{self.get_author()}'
        return s




