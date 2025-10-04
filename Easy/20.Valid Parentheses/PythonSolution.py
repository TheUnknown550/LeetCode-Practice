# to use stacks by 

def isValid(s: str) -> bool:
    stack = []
    for brackets in s:
        if(brackets == "("):
            stack.append(")")
        elif(brackets == "["):
            stack.append("]")
        elif(brackets == "{"):
            stack.append("}")
        else:
            if not stack or stack.pop() != brackets:
                return False
    return not stack
            

def main():
    s = "([])"
    print(isValid(s))

if __name__ == "__main__":
    main()