import mysql.connector
from PySide6.QtWidgets import QApplication, QWidget 
from PySide6.QtCore import QFile
import sys

app = QApplication(sys.argv)

tela_main = QFile('main.iu')
tela_main.open(QFile.ReadOnly)

loader = QUiLoader()

window = loader.load(tela_main)
window.show()

def clicar():
    valueInput = window.textEdit.value()
    print(valueInput)
    return

window.Cancelar.clicked.connect();

app.exec()



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