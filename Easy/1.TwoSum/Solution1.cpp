#include<iostream>
#include<vector>

using namespace std;

int main(){
    // markers
    vector<int> numbers = {2, 7, 11, 15};
    int target = 9;

    // loop through both arrays O(n)
    for(int i = 0; i < numbers.size(); i++){
        for(int j = i + 1; j < numbers.size(); j++){
            if(numbers[i] + numbers[j] == target){ // if sum is = targert we found the solution
                cout << "Indices: " << i << ", " << j << endl;
                return 0;
            }
        }
    }
    cout << "No two sum solution found." << endl;
    return 0;
}