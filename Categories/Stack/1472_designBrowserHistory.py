from typing import *

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.ptr = 0

    def visit(self, url: str) -> None:
        cur = len(self.history) - 1

        while cur != self.ptr:
            self.history.pop()
            cur -= 1

        self.ptr += 1
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.ptr = max(
            0,
            self.ptr - steps
        )

        return self.history[self.ptr]
        
    def forward(self, steps: int) -> str:
        self.ptr = min(
            len(self.history) - 1,
            self.ptr + steps
        )

        return self.history[self.ptr]
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)