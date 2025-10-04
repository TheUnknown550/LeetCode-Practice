using System;
using System.Collections.Generic;

namespace LeetCodePractice
{
    // Solution class with your LeetCode method
    class Solution
    {
        public bool IsValid(string s)
        {
            Stack<char> stack = new Stack<char>(); // use stacks
            
            foreach (char c in s)
            {
                if (c == '(') stack.Push(')'); // if open bracket happend close brackets should come after
                else if (c == '{') stack.Push('}');
                else if (c == '[') stack.Push(']');
                else
                {
                    if (stack.Count == 0 || stack.Pop() != c) // if when pop from stack isn't correct is false
                        return false;
                }
            }
            return stack.Count == 0;
        }
    }

    // Main program to run test cases
    class Program
    {
        static void Main(string[] args)
        {
            Solution solution = new Solution();

            // Test cases
            string[] tests = { "()", "()[]{}", "(]", "([)]", "{[]}" };

            foreach (var test in tests)
            {
                bool result = solution.IsValid(test);
                Console.WriteLine($"Input: {test} -> Output: {result}");
            }
        }
    }
}
