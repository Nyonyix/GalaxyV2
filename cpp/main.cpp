#include "inc/GalaxyGen.hpp"
#include <iostream>

using nlohmann::json;

int main(int argc, char const *argv[])
{
    json test = GalaxyGenerator::genStar();
    std::string j_str = test.dump();
    std::cout << "test" << std::endl;

    int galaxy = 0;
    return 0;
}
