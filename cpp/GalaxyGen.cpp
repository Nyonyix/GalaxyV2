#include "inc/GalaxyGen.hpp"
#include <fstream>
#include <sstream>

using nlohmann::json;

GalaxyGenerator::GalaxyGenerator(std::string name, int seed, int star_count, int min_planets, int max_planets)
{
}

GalaxyGenerator::~GalaxyGenerator()
{
}

json GalaxyGenerator::loadDef(std::string filename)
{
    std::ifstream f("Hello");
    std::stringstream ss;
    ss << f.rdbuf();
    std::string j_string = ss.str();
    json j = json::parse(j_string);
    return j;
}

json GalaxyGenerator::genStar()
{
    json out_json;
    std::cout << "Hello from genStar()" << std::endl;
    out_json = GalaxyGenerator::loadDef("definitions.json");
    return out_json;
}
