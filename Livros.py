from database import Database

class Livros():
    db = Database('livros')

    @classmethod
    def create(cls, data : dict):
        cls.db.insert(data).exec()
        cls.db._conn.commit()

    @classmethod
    def find_one(cls, rules:dict=None):
        return cls.db.select().where(rules).exec().fetchnone()

    @classmethod
    def find_all(cls, rules:dict=None):
        return cls.db.select().where(rules).exec().fetchall()

    @classmethod
    def update(cls, data=None,*, id):
        return cls.db.update(fields=data, id=id)

    @classmethod
    def delete(cls, id:int):
        return cls.db.delete(id)