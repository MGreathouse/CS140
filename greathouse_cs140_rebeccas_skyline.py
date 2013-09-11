skyline = input("Skyline width?")
maximum = input("max width?")
smallest = input("smallest width?")

skyline = int(skyline)
maximum = int(maximum)
smallest = int(smallest)
import random
value = random.randint(smallest,maximum)

while skyline > maximum:
    if value <= (skyline - smallest):
        print(value)
    if value >= (skyline - smallest):
    	value = random.randint(smallest, maximum)