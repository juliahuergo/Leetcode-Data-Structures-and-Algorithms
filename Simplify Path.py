class Solution(object):
    def simplifyPath(self, path):
        dirs = path.split("/")
        stack = []
        
        for d in dirs:
            if d:
                if d == "..":
                    if stack:
                        stack.pop()
                elif d != ".":
                    stack.append(d)
                #d can be "." (current directory), ".." (previous dir.), or an actual name of a directory
        
        return "/" + "/".join(stack)
