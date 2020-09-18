import Aux_Funcs
import Galaxy_Types

class GalaxyGen:

    def __init__(self, seed: int, name: str):
        self.seed = int
        self.name = str

    def galaxyGenerator(self) -> Galaxy_Types.Galaxy:
        """
        Where all the data comes together to formulate and generate the larger axy
        """
        pass



    def starGenerate(self) -> Galaxy_Types.Star:
        """
        Function to generate either a specific class or generic rtandom star
        """
        pass
    
    
    
    def planetGenerator(self) -> Galaxy_Types.Planet:
        """
        Function to generate either a specific type or generic rtandom planet
        """
        pass
    
    
    
    def moonGenerator(self) -> Galaxy_Types.Moon:
        """
        Copy of planetGenerator with extra logic to determin moons
        """
        pass
    
    
    
    def asteroidGenerator(self) -> Galaxy_Types.Asteroid:
        """
        Function to generate a generic rtandom asteroid
        """
        pass
    
    
    
    def planemoGenerator(self) -> Galaxy_Types.Planet:
        """
        Function to generate rouge planets without a solar system in insterstellar space
        """
        pass

if __name__ == "__main__":

    print(f"This is a lib file. Not to be run on it's own.")