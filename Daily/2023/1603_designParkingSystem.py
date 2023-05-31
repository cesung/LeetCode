from typing import *
from collections import defaultdict


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.rcd = defaultdict(int, {
            1: big,
            2: medium,
            3: small,
        })

    def addCar(self, carType: int) -> bool:
        self.rcd[carType] -= 1

        return True if (
            self.rcd[carType] >= 0
        ) else False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
