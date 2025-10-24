# Calculate meeting time for two objects moving toward each other
distance = float(input())  # initial distance between objects
speed1 = float(input())  # speed of first object
speed2 = float(input())  # speed of second object

meeting_time = distance / (speed1 + speed2)
print(meeting_time)
