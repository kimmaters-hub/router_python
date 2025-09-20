import heapq
import bisect
from collections import defaultdict

class Router(object):
    def __init__(self, memoryLimit):
        self.packetHeap = []
        self.memoryLimit = memoryLimit
        self.seq = 0
        self.seenPackets = set()
        self.destHistory = defaultdict(list)

    def addPacket(self, source, destination, timestamp):
        key = (source, destination, timestamp)
        if key in self.seenPackets:
            return False

        if len(self.packetHeap) >= self.memoryLimit:
            old_timestamp, _, old_source, old_destination = heapq.heappop(self.packetHeap)
            self.seenPackets.remove((old_source, old_destination, old_timestamp))
            # Remove old_timestamp from destHistory[old_destination]
            idx = bisect.bisect_left(self.destHistory[old_destination], old_timestamp)
            if idx < len(self.destHistory[old_destination]) and self.destHistory[old_destination][idx] == old_timestamp:
                self.destHistory[old_destination].pop(idx)

        packet = (timestamp, self.seq, source, destination)
        self.seq += 1
        heapq.heappush(self.packetHeap, packet)
        self.destHistory[destination].append(timestamp)
        self.seenPackets.add(key)
        return True

    def forwardPacket(self):
        if not self.packetHeap:
            return []

        timestamp, _, source, destination = heapq.heappop(self.packetHeap)
        self.seenPackets.remove((source, destination, timestamp))
        # Remove timestamp from destHistory[destination]
        idx = bisect.bisect_left(self.destHistory[destination], timestamp)
        if idx < len(self.destHistory[destination]) and self.destHistory[destination][idx] == timestamp:
            self.destHistory[destination].pop(idx)

        return [source, destination, timestamp]

    def getCount(self, destination, startTime, endTime):
        timestamps = self.destHistory[destination]
        left = bisect.bisect_left(timestamps, startTime)
        right = bisect.bisect_right(timestamps, endTime)
        return right - left
