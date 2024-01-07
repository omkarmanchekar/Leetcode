class Solution:
    def __init__(self):
        self.result = []

    def willCollide(self):
        if len(self.result) < 2:
            return False

        last_asteroid = self.result[-1]
        second_last_asteroid = self.result[-2]
        return (last_asteroid < 0 < second_last_asteroid) 

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Check if length of asteroids is greater than 2, if not return the asteroids list as it is 
        Create result array which will act as a stack
        Add the first asteroid in result 
        iterate over the asteroids list from index 1 
        check if the iterator astroid will collide with the last asteroid in result 
            if they will collide check will will survive 
            else continue with the iterator 
        """


        for ash in asteroids:

            self.result.append(ash)
                
            while len(self.result) and self.willCollide():
                last = self.result[-1]
                second_last = self.result[-2]
                self.result = self.result[:-2]
                if abs(last) > abs(second_last):
                    self.result.append(last)
                elif abs(last) < abs(second_last):
                    self.result.append(second_last)

        return self.result          




