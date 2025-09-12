# Add the value if the value comes after 
# XXVI Large values will come first. 
# XXIV If detect a smaller value before a larger then it will subtact

def romanToInt(s: str) -> int:
    # create a dictionary
    romanValueDict = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    value = 0
    prevValue = 0
    total = 0
    
    # loop through all values
    for r in reversed(s):
        value = romanValueDict[r]
        if(value < prevValue):
            total -= value
        else:
            total += value
        prevValue = value
    return total

def main():
    print(romanToInt("XXIV"))
    # print("Hello World")
    
    
if __name__ == "__main__": # not being runned when being import
    main()