class Galaxy(object):
    pass

class CelestialObject(object):

    resources = dict
    atmosphere = dict
    oceans = dict
    life = list
    civilization = str

    def __init__(self, type_str: str, id: int, colour: float, temp: float, 
    mass: float, radius: float):
        self.type_str = str
        self.id = int
        self.colour = float
        self.temp = float
        self.mass = float
        self.radius = float

class Star(CelestialObject):

    def __init__(self, spec_class: str, sys_radius: float, is_parent: bool, 
    is_child: bool, type_str: str, id: int, colour: float, temp: float, 
    mass: float, radius: float):
        super.__init__(self, type_str, id, colour, temp, mass, radius)
        self.spec_class = str
        self.sys_radius = float
        self.is_parent = bool
        self.is_child = bool

class Planet(CelestialObject):

    def __init__(self, type_str: str, 
    id: int, colour: float, temp: float, mass: float, radius: float):
        super().__init__(type_str, id, colour, temp, mass, radius)


class Moon(Planet):

    def __init__(self, type_str: str, id: int, 
    colour: float, temp: float, mass: float, radius: float):
        super().__init__(type_str, id, colour, temp, mass, radius)

class Asteroid(CelestialObject):

    def __init__(self, type_str: str, id: int, colour: float, temp: float, 
    mass: float, radius: float):
        super().__init__(type_str, id, colour, temp, mass, radius)

class GenericObject(CelestialObject):

    def __init__(self, type_str: str, id: int, colour: float, temp: float, 
    mass: float, radius: float):
        super().__init__(type_str, id, colour, temp, mass, radius)