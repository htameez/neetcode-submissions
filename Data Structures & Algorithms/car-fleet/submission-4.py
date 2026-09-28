class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        
        track = []
        for i in range(len(position)):
            track.append((position[i], speed[i]))
        
        track.sort(reverse=True)

        times = []
        times.append((target - track[0][0]) / track[0][1]) # car at front's time
        print(times[-1])

        for i in range(1, len(track)):
            currTime = (target - track[i][0]) / track[i][1]
            if currTime > times[-1]:
                times.append(currTime) # form new fleet
                print(times[-1])
        
        return len(times)




        