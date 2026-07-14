a = float(input("Input Rods: "))
print(f"your input rods {a} rods.")
answer_meters = 5.0292*a
answer_furlong  = 40*a
answer_mile = 1609.34*answer_meters
answer_foot = 0.3048* answer_meters
answer_average_walking_speed_per_hour =  60*3.1* answer_mile
print("conversions")
print(f"Meters: {answer_meters}")
print(f"Foot: {answer_foot}")
print(f"Miles: {answer_mile}")
print(f"furlongs: {answer_furlong}")
print(f"Mintues to walk {a} rods: {answer_meters}")

