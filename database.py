import mysql.connector

class Database:
    def __init__(self, table : str):
        self.__host__ = "localhost"
        self.__user__ = "root"
        self.__password__ = ""
        self.__database__ = "biblioteca_py"

        self.table = table
        self.query = ""

        self.__initialize__()
        

    def __initialize__(self):
        self._conn = self.__connection__()
        self._cursor = self.__create_cursor__()

    def __connection__(self):
        return mysql.connector.connect(
            host = self.__host__,
            user = self.__user__,
            password = self.__password__,
            database = self.__database__,
        )
    
    def __create_cursor__(self):
        return self._conn.cursor(dictionary=True)

    def exec(self):
        self.query +=";"
        self._cursor.execute(self.query)
        return self._cursor

    def select(self, fields=["*"]):
        self.query = f"SELECT {self.define_fields(fields)} FROM {self.table} "

        return self

    def define_fields(self, fields):
        campos = ""

        for field in fields:
            campos += f"{field}" if field == fields[-1] else f"{field},"

        return campos

    def where(self, rules: dict = None):
        if not rules:
            return self

        self.query += "WHERE "

        conditions = []

        for key, value in rules.items():
            conditions.append(f"{key} = {f"'{value}'" if isinstance(value, str) else f"{value}"}")

        self.query += " AND ".join(conditions)

        return self

    def insert(self, fields:dict=None):
        if fields is None or len(fields.items()) <= 0:
            return self
        values = []

        for value in fields.values():
            if isinstance(value, str):
                value = f"'{value}'"
            
            values.append(str(value))

        self.query = f"INSERT INTO {self.table}({', '.join(fields)}) VALUES({",".join(values)})"
        return self
    
    def update(self,*, fields:dict=None, id):
        values = []

        for value in fields.values():
            if isinstance(value, str):
                value = f"'{value}'"
            
            values.append(str(value))

        self.query = f"UPDATE {self.table}({', '.join(fields)}) VALUES({",".join(values)})"
        return self.where({'id': id})
    
    def delete(self, id):
        self.query = f"DELETE FROM {self.table} "

        return self.where({'id': id})