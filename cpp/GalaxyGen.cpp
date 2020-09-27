#include "inc/GalaxyGen.hpp"
#include <fstream>
#include <sstream>
#include <random>
#include <vector>

using nlohmann::json;

GalaxyGenerator::GalaxyGenerator(std::string name, int seed, int star_count, int min_planets, int max_planets)
{
}

GalaxyGenerator::~GalaxyGenerator()
{
}

int GalaxyGenerator::randomGen(int min, int max)
{
    std::default_random_engine gen;
    std::uniform_int_distribution<int> dist(min, max);
    return dist(gen);
}

double GalaxyGenerator::randomGen(double min, double max)
{
    std::default_random_engine gen;
    std::uniform_real_distribution<double> dist(min, max);
    return dist(gen);
}

json GalaxyGenerator::loadDef(std::string filename)
{
    std::ifstream f(filename);
    json j;
    f >> j;
    return j;
}

void GalaxyGenerator::genStar()
{
    json star_def = GalaxyGenerator::loadDef("res/definitions.json")["star_types"];

    int i = 0;
    std::vector<std::string> star_str_vect;
    for (const auto& item : star_def.items())
    {

        star_str_vect.push_back(item.value()["name_str"]);

    }

    for (const auto& item : star_str_vect)
    {
        std::cout << item << std::endl;
    }
    
}
