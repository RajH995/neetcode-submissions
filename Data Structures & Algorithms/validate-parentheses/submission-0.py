class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []

        for x in s:
            if x == ")":
                if my_stack and my_stack.pop() == "(":
                    continue
                else:
                    return False
            elif x == "}":
                if my_stack and my_stack.pop() == "{":
                    continue
                else:
                    return False
            elif x == "]":
                if my_stack and my_stack.pop() == "[":
                    continue
                else:
                    return False
            else:
                my_stack.append(x)

        return len(my_stack) == 0
        