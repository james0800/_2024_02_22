import random
def f(num:int):
    
    with open("names.txt") as file:
        con=file.read()
        arr:list[str]=con.split('\n')
        name=random.choices(arr,k=num)
        file.close()
        return name
names:list[str]=f(5)
st:list=[]
for i in names:
    stu:dict={}
    stu["name"]=i
    stu["height"]=random.randint(150,220)
    
    
    stu["weight"]=random.randint(40,90)
    
    st.append(stu)
print(st)