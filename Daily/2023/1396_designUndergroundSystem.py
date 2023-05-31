from typing import *
from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.check_in = defaultdict(lambda: defaultdict(int))
        self.rcd = defaultdict(list)

    def checkIn(self, id: int, start_station: str, start_t: int) -> None:
        self.check_in[id] = (start_station, start_t)

    def checkOut(self, id: int, end_station: str, end_t: int) -> None:
        start_station, start_t = self.check_in[id]
        self.rcd[(start_station, end_station)].append(end_t - start_t)

    def getAverageTime(self, start_station: str, end_station: str) -> float:
        return sum(self.rcd[(start_station, end_station)]) / len(self.rcd[start_station, end_station])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
