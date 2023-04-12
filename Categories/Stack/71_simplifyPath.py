from typing import *

class Solution:
    def simplifyPath(self, path: str) -> str:        
        stack = []
        for directory in path.split('/'):
            if (
                not directory or
                directory == '.'
            ):
                continue

            if directory == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(directory)

        
        return "/" + "/".join(stack)