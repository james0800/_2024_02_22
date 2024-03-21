import random
def f(num:int):
    with open("names.txt",encoding="utf8") as file:
        con=file.read()
        arr:list[str]=con.split('\n')
        name=random.choices(arr,k=num)
        return name
        file.close()
