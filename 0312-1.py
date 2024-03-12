import random
import pyinputplus as pyip
def game():
    min=1
    max=100
    i=-10
    times=0
    anser=random.randint(min,max)
    print(anser)
    while True:
        i=pyip.inputInt(f"input{min}~{max} ",min=min,max=max)
        times+=1
        if i==anser :
            print("right")
            break
        elif i>anser:
            print("bigger")
            max=i
        elif i<anser:
            print("smaller")
            min=i
    print(times)
def main():
    while True:
        game()
        if input("contuin?")=="N":
            break

    return 0

main()