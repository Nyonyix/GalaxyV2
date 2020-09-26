import Aux_Funcs
import Galaxy_Types
import json
import random
import os

class GalaxyGen:

    def __init__(self,star_count:int, min_planets: int, max_planets, seed: int, name: str, def_file: str):
        self.seed = seed
        self.name = name
        self.star_count = star_count
        self.min_planets = min_planets
        self.max_planets = max_planets
        self.generated_stars = {}
        self.def_file = self.loadFile(def_file)

    def loadFile(self, filename: str) -> dict:
        with open(filename, 'r') as f:
            return json.load(f)

    def galaxyGenerator(self) -> Galaxy_Types.Galaxy:
        """
        Where all the data comes together to formulate and generate the larger axy
        """
        pass

    def starGenerate(self) -> Galaxy_Types.Star:
        """
        Function to generate either a specific class or generic rtandom star
        """
        star_def = self.def_file["star_types"]
        star_id = 0

        while len(self.generated_stars) < self.star_count:
            for var, val in star_def.items():
                star_id_str = str(star_id)
                if len(self.generated_stars) != self.star_count:
                    if random.randint(0, 100) <= val["weight"]:
                        self.generated_stars[star_id_str] = {}
                        self.generated_stars[star_id_str]["star_type"] = ""
                        self.generated_stars[star_id_str]["star_type_str"] = ""
                        self.generated_stars[star_id_str]["star_type"] = str(var)
                        self.generated_stars[star_id_str]["star_type_str"] = val["name_str"]
                        star_id += 1
                        continue

    def genStarPhysical(self) -> dict:
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

    GalaxyGenOBJ = GalaxyGen(int(os.sys.argv[1]), 0, 0, 1226, "Hi", "../res/definitions.json")
    GalaxyGenOBJ.starGenerate()

    count = {}
    for val in GalaxyGenOBJ.generated_stars.values():
        try:
            count[val["star_type"]] += 1
        except KeyError:
            count[val["star_type"]] = 0
            count[val["star_type"]] += 1
    
    for var, val in count.items():
        print(f"{var}: {val}")
    print(f"Total: {len(GalaxyGenOBJ.generated_stars)}")