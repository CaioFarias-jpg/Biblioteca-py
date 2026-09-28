from database import Database

class Livro(Database):
    def __init__(self,):
        self.db = Database('livros')

    def create(self,):
        self.db.insert({'isbn' : 12345678912345, 
                       'titulo' : 'Star Wars', 
                       'autor' : 'George Lucas', 
                       'data_lancamento' : '1899-02-25', 
                       'genero' : 'Ficção', 
                       'editora' : 'Lucas Film'
                       })exec()
                        self.db._conn.commit()