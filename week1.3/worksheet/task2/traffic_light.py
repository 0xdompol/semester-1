"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Dominic Polniaszek
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input("Input the maximum run time: "))  # read an integer number of steps (>0)

state = "red"

print(f"Time {systime:03} State {state}")

# Simulate the traffic light system up to time=maxtime in 1-second steps
traffic_counter = 0
systime += 1

while systime != (maxtime+1):
    if traffic_counter < 3:
        state = "red"
    elif traffic_counter > 2 and traffic_counter < 6:
        state = "red_amber"
    elif traffic_counter > 5 and traffic_counter < 11:
        state = "green"
    elif traffic_counter > 10 and traffic_counter < 13:
        state = "amber"
    else:
        traffic_counter = -2
    print(f"Time {systime:03} State {state}")
    systime += 1
    traffic_counter += 1

# At the end of each step you should output the time and state using the statement on line 14