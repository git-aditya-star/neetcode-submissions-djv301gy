class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False
        if s[0] in (")", "}", "]"):
            return False

        for bracket in s:
            if bracket in ("(", "{", "["):
                stack.append(bracket)
            else:
                if (len(stack) == 0):
                    return False
                last_ele = stack[-1]
                match last_ele:
                    case "(":
                        if bracket == ")":
                            stack.pop()
                        else:
                            return False
                    case "{":
                        if bracket == "}":
                            stack.pop()
                        else:
                            return False
                    case "[":
                        if bracket == "]":
                            stack.pop()
                        else:
                            return False
        if len(stack) > 0:
            return False
        return True
