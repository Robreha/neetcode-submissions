class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}

        for i in s:
            if i in closeToOpen: #Closed Bracket
                if stack and stack[-1] == closeToOpen[i]:
                    stack.pop()
                else:
                    return False
            else: #Open Bracket
                stack.append(i)

        return stack == []