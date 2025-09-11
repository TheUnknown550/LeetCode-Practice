#include<iostream>
#include<vector>

using namespace std;

string longestCommonPrefix(vector<string>& strs) {

    if(strs.size() == 1){ // check if the vector have a single word
        return strs.at(0);
    }

    string output = "";
    for(int i = 0; i < strs.at(0).length(); i++){ // loop through each character of a text
        bool state = false; // check if prefix is true
        for(int j = 1; j < strs.size(); j++){ // loop through all texts in the vector
            // cout << strs.at(0).at(i) << " " << strs.at(j).at(i) << endl;
            if(i >= strs[j].length() || strs[0][i] != strs[j][i]){ // check if the value isn't the same
                return output;
            }else{
                // cout << "Converting Prefix State: " <<endl;
                state = true; // found the prefix
            }
        }
        if (state){
            // cout << "Pushing back: " << strs.at(0).at(i) <<endl;
            output.push_back(strs.at(0).at(i)); // if no intertupt then will return the prefix
        }
    }
    return output;
}

int main(){
    vector<string> strs = {"a"};

    cout << longestCommonPrefix(strs)<< endl;

    return 0;
}