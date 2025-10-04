#include<iostream>
#include<vector>
#include<cmath>

using namespace std;

bool Palinedrome(int x){
    if(x < 0){return false;} // if negative values is not palinedrome
    if(x < 10){return true;} // if have 1 digit automatic palinedrome

    // find numbers of digits of x
    int xDigits = log10(x);
    // cout << xDigits;
    
    for(int i = 0; i <= xDigits; i++){ // loop through all digits of x
        int x1 = ((int)floor(x / pow(10, i))) % 10;
        int x2 = ((int)floor(x / pow(10, (xDigits)-i))) % 10; 
        // cout << x1 << " " << x2 <<endl;
        if(x1 != x2){
            return false;
        }
    }

    return true;
}

int main(){
    int x = 1;

    cout << Palinedrome(x)<< endl;

    return 0;
}