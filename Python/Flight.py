# Flight
# There is a class named Flight, which has the upTime and downTime as the properties. The class should also have a method named calculateFlight, which will return the calculated flying time. You need to complete this method.

# Here, upTime denotes the time at which a given bird starts flying, and downTime is the time at which the bird lands somewhere.

# You don't need to worry about input/output and object of the class. The given template will take care of it. Also, it is given the bird will fly in the morning, and will land before night of the same day.

# The input will contain the upTime and downTime, in 24 hr notation as hh:mm (h is hour, and m is min). You need to calculate the flying time of the given bird (in minutes), as output.

# Input
# First line contains upTime in the given notation. Second line contains downTime in the given notation.

# Output
# One Integer denoting the flying time in minutes.

# Example
# Input1:

# 10:55
# 22:55
# Output1:

# 720
# Explanation:

# Flying time will be 12 hrs = 720 min.

class Flight:
 def __init__(self,upTime,downTime):
     self.uptime=upTime
     self.downtime=downTime
 def flight_time(self):
  time=self.downtime-self.uptime
  return time

n=[int(x) for x in input().split(':')]
m=[int(x) for x in input().split(':')]
up=(n[0]*60)+n[1]
down=(m[0]*60+m[1])
f1=Flight(up,down)
print(f1.flight_time())

    