import random
def f(num:int)->list[str]:
    with open("names.txt") as file:
        name:str=file.open()
        namelist:list[str]=name.split(sep="\n")
        r:list[str]=random.choice(name,num=num)
        return r
        file.closed
