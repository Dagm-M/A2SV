class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = ["/"]

        for p in path:
            if  p == "..":
                if len(stack) > 2:
                    stack.pop()
                    stack.pop()
            
                elif len(stack) == 2:
                    stack.pop()
            elif not(p == "." or p == ""):
                stack.append(p)
                stack.append("/")

        if len(stack) > 1:
            stack.pop()

        return "".join(stack)
