class Galaxy(object):
    pass

class CelestialObject(dict):

    def __init__(self, type_str: str, id: int, colour: float, temp: float, 
    mass: float, radius: float):
        self.type_str = type_str
        self.id = id
        self.colour = colour
        self.temp = temp
        self.mass = mass
        self.radius = radius
        self.resources = dict
        self.atmosphere = dict
        self.oceans = list
        self.life = list
        self.civilization = list

    def toDict(self):
        return_dict = {}
        for var, val in vars(self).items():
            return_dict[str(var)] = {}
            if type(val) == int:
                return_dict[str(var)] = int(val)
            elif type(val) == float:
                return_dict[str(var)] = float(val)
            else:
                return_dict[str(var)] = str(val)
        return dict(return_dict)  

class Star(CelestialObject):

    def __init__(self, spec_class: str, sys_radius: float, is_parent: bool, 
    is_child: bool, type_str: str, id: int, colour: float, temp: float, 
    mass: float, radius: float):
        super().__init__(type_str, id, colour, temp, mass, radius)
        self.spec_class = spec_class
        self.sys_radius = sys_radius
        self.is_parent = is_parent
        self.is_child = is_child

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