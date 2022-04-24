class UndergroundSystem:
    def __init__(self):
        self.checked_in = {}
        self.station_times = defaultdict(int)
        self.station_freqs = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checked_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        name2, t2 = self.checked_in.pop(id)
        self.station_times[(name2, stationName)] += t - t2
        self.station_freqs[(name2, stationName)] += 1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.station_times[(startStation, endStation)] / self.station_freqs[(startStation, endStation)]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)