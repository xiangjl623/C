#include <iostream>
#include <map>
#include <string>

int main() {
    std::map<std::string, int> scores;
    scores["Alice"] = 95;
    scores["Bob"] = 87;
    scores["Charlie"] = 92;

    for (const auto& pair : scores)
        std::cout << pair.first << ": " << pair.second << std::endl;

    return 0;
}
