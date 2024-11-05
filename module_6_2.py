class Vehicle:

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self,__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    __COLOR_VARIANTS={'black', 'white', 'silver'}

    def get_model(self):
        


class Sedan(Vehicle):
    _PASSENGERS_LIMIT = 5