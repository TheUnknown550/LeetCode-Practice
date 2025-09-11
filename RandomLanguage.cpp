#include <iostream>
#include <vector>
#include <cstdlib>   // for rand() and srand()
#include <ctime>     // for time()

using namespace std;

int main() {
    // Seed random number generator
    srand(static_cast<unsigned int>(time(nullptr)));

    // List of programming languages (modifiable)
    vector<string> languages = {
        "C++", "Python", "Java", "C#"
    };

    // Randomly select a language
    int randomIndex = rand() % languages.size();
    string randomLanguage = languages[randomIndex];

    // Output
    cout << "Random programming language: " << randomLanguage << endl;

    return 0;
}
