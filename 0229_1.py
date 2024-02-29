import statistics
print(statistics.variance([0,5,14,8]))
print(statistics.variance([4,5,7,8]))
soccer = eval(input("scccer="))

if soccer >=60:
    print("acc")
else :
    print("false")
print("end")

add=input("y/n")

if add=="y":
    soccer=soccer*1.5
print(f"soccer={round(soccer)}")