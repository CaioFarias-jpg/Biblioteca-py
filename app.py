import mysql.connector

#criação da conexão com bd
conector = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "biblioteca_py",
)

#instancia de execução de comandos sql
cursor = conector.cursor()

cursor.execute("INSERT INTO livros(isbn, autor, titulo, data_lancamento, genero, editora) VALUES(12345678910, 'Machado de Assis', 'Dom Casmurro', '1899-02-25', 'Romance', 'Livraria Garnier')")

conector.commit()