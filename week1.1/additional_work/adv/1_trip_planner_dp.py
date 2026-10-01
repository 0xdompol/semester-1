destination_name = input("What is your destination")
cond = False
while cond == False:
    distance_miles_input = int(input("How many miles will you travel"))
    if distance_miles_input < 1:
        continue
    time_hours_input = int(input("How much time will you take in hours"))
    if time_hours_input < 1:
        continue
    break

Avg_speed = distance_miles_input / time_hours_input
print("You will reach ",destination_name," at the average speed of ",Avg_speed,"m/ph.")
"""Advanced Task 1: Trip Planner
- Ask for a destination name, total distance in miles, and planned travel time in hours.
- Convert the numeric inputs so you can calculate an approximate average speed for the journey.
- Display a human-readable summary that includes the destination and the speed formatted to two decimal places.
- Extension: warn if either numeric value is zero or negative.
"""
