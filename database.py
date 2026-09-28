import mysql.connector


class Database:
    def __init__(self, table: str):
        self.__host__ = "localhost"
        self.__user__ = "root"
        self.__password__ = ""
        self.__database__ = "biblioteca_py"

        self.table = table
        self.query = ""

        self.__initialize__()

    def __initialize__(self):
        self.conn = self.__connection__()
        self.cursor = self.__create_cursor__()

    def __connection__(self):
        return mysql.connector.connect(
            host=self.__host__,
            user=self.__user__,
            password=self.__password__,
            database=self.__database__,
        )

    def __create_cursor__(self):
        return self.conn.cursor()

    def exec(self):
        self._cursor.execute(self.query)
        self._conn.commit()

    def select(self, fields=["*"]):
        self.query = f"SELECT {self.define_fields(fields)} FROM {self.table};"

    def define_fields(self, fields):
        items = ""

        for field in fields:
            items += (
                f"{field}," if not (field == fields[-1]) else
                f"{field}"
            )

        return items

    def where(self, rules = ()):
        self.query += "WHERE "

        for key, value in rules.items():
            self.query+= f"{key} LIKE '%{value}%' "

        return self

    def insert(self, fields : dict ={}):
        values = ''
        formatted_values = []

        for value in fields.values():
            if insistance(value, str):
                value = f"'{value}'"
            formatted_values



# db = Database('livros')
# livros = db.select(["titulo", "autor"]).where({'id' : 1}).exec()
