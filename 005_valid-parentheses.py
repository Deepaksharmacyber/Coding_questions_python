"""
LeetCode Problem: 20. Valid Parentheses
Link: https://leetcode.com/problems/valid-parentheses/

Description:
Given a string containing only the characters '(', ')', '{', '}', '[' and ']',
determine whether the string is valid.

A valid string must satisfy:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every closing bracket must have a corresponding open bracket.

Examples:
- "()"       -> True
- "()[]{}"   -> True
- "(]"       -> False
- "([])"     -> True
- "([)]"     -> False

Constraints:
- 1 <= s.length <= 10^4
- s consists only of characters: '()[]{}'

Approach:
- Use a stack.
- When encountering an opening bracket, push the expected closing bracket.
- When encountering a closing bracket, verify it matches the top of stack.
- If mismatch or stack is empty → invalid.
- At the end, stack must be empty for the string to be valid.

Time Complexity: O(n)
    - We iterate through each character exactly once.
    - Stack operations (push/pop) are O(1).
    - Therefore, overall complexity is linear in the length of string.

Space Complexity: O(n)
    - In the worst case (e.g., "(((([[[{{{"), all characters are opening brackets
      and get stored in the stack → O(n) extra space.
    - Best case (all closing brackets immediately match), stack stays small.

"""

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for ch in s:
            # Opening bracket: push expected closing bracket
            if ch in pairs:
                stack.append(pairs[ch])
            else:
                # Closing bracket: check for mismatch or empty stack
                if not stack or stack[-1] != ch:
                    return False
                stack.pop()

        # Valid only if no unmatched brackets remain
        return len(stack) == 0
