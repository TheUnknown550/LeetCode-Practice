#include<iostream>

using namespace std;

int romanToInt(string s){
    // loop through all digits of roman numerals O(n)
    int num = 0;
    for(int i = 0; i < s.length(); i++){
        if(s.at(i) == 'I'){
            if(i+1 < s.length() && s.at(i+1) == 'V'){ // check if value is IV = 4
                cout << "IV = " << 4 <<endl;
                num += 4;
                i++;
            }else if(i+1 < s.length() && s.at(i+1) == 'X'){ // check if value is IX = 9
                cout << "IX = " << 9 <<endl;
                num += 9;
                i++;
            }else{ // value is add 1
                cout << "I = " << 1 <<endl;
                num += 1;
            }
        }
        else if(s.at(i) == 'V'){ // add 5 to the number
            cout << "V = " << 5 <<endl;
            num += 5;
        }
        else if(s.at(i) == 'X'){ // add 10 to the number
            if(i+1 < s.length() && s.at(i+1) == 'L'){ // check if it's XL = 40
                cout << "XL = " << 40 <<endl;
                num += 40;
                i++;
            }
            else if(i+1 < s.length() && s.at(i+1) == 'C'){// check if it's XC = 90
                cout << "XC = " << 90 <<endl;
                num += 90;
                i++;
            }else{ // value is 10
                cout << "X = " << 10 <<endl;
                num += 10;
            }
        }else if(s.at(i) == 'L'){ // L = 50
            cout << "L = " << 50 <<endl;
            num += 50;
        }else if(s.at(i) == 'C'){
            if(i+1 < s.length() && s.at(i+1) == 'D'){ // Check if it's CD = 400
                cout << "CD = " << 400 <<endl;
                num += 400;
                i++;
            }else if(i+1 < s.length() && s.at(i+1) == 'M'){ // Check if it's CM = 900
                cout << "CM = " << 900 <<endl;
                num += 900;
                i++;
            }else{
                num += 100;
            }
        }else if(s.at(i) == 'D'){ // if D the give + 500
            cout << "D = " << 500 <<endl;
            num += 500;
        }else if(s.at(i) == 'M'){ // if M then + 1000
            cout << "M = " << 1000 <<endl;
            num += 1000;
        }
    }
    return num;
}

int main(){
    string s = "MCMXCIV";

    cout << romanToInt(s)<< endl;

    return 0;
}