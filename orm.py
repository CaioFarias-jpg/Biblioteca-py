class ORM:
    def __init__(self, data:dict):
        self.__dict__.update(data)

        for key, value in data.items():
            setattr(self, f'get_(key)', lambda : self.__getattribute__(key))
            setattr(self, f'set_(key)', lambda  new: self.__setattr__(key, new))