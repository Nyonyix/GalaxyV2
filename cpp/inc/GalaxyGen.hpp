#ifndef GALAXYGEN_H
#define GALAXYGEN_H

#include <iostream>
#include "json.hpp"

using nlohmann::json;

class GalaxyGenerator
{
private:
    
    std::string name;
    int seed;
    int star_count;
    int min_planets;
    int max_planets;

public:
    GalaxyGenerator(std::string name, int seed, int star_count, int min_planets, int max_planets);
    ~GalaxyGenerator();

    static json loadDef(std::string filename);
    static json genStar();

};

#endif