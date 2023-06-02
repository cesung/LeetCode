public class Solution {
    public bool IsValid(string s) {
        var rcd = new Dictionary<char, char> {
            [')'] = '(',
            ['}'] = '{',
            [']'] = '[',
        };

        var stack = new Stack<char>();

        foreach (char ch in s) {
            if (
                ch == '(' || 
                ch == '[' ||
                ch == '{'
            ) {
                stack.Push(ch);
            }
            else {
                if (stack.Count == 0) {
                    return false;
                }

                if (stack.Peek() != rcd[ch]) {
                    return false;
                } else {
                    stack.Pop();
                }
            }
        }

        return stack.Count == 0;
    }
}