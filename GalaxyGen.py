import random
import datetime
import aux_funcs

class CelestialObject(object):
    def __init__(self, id: int, colour: float, temp: float, mass: float, radius: float):
        self.id = int
        self.colour = float
        self.temp = float
        self.mass = float
        self.radius = float

class Star(CelestialObject):
    pass

class Planet(CelestialObject):
    pass

class Moon(Planet):
    pass

class Asteroid(CelestialObject):
    pass

class SpaceObject(CelestialObject):
    pass

class GalaxyGen:

    def __init__(self, seed: int, name: str):
        self.seed = int
        self.name = str

    def galaxyGenerator(self) -> None:
        """
        Where all the data comes together to formulate and generate the larger axy
        """
        pass



    def starGenerate(self) -> Star:
        """
        Function to generate either a specific class or generic rtandom star
        """
        pass
    
    
    
    def planetGenerator(self) -> Planet:
        """
        Function to generate either a specific type or generic rtandom planet
        """
        pass
    
    
    
    def moonGenerator(self) -> Moon:
        """
        Copy of planetGenerator with extra logic to determin moons
        """
        pass
    
    
    
    def asteroidGenerator(self) -> Asteroid:
        """
        Function to generate a generic rtandom asteroid
        """
        pass
    
    
    
    def planemoGenerator(self) -> Planet:
        """
        Function to generate rouge planets without a solar system in insterstellar space
        """
        pass

if __name__ == "__main__":

    print(f"This is a lib file. Not to be run on it's own.")