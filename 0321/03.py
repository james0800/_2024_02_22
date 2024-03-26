from pprint import pprint
import random
from lib import MC2
import pyinputplus as pyip

num:int=pyip.inputInt()
names:list[str]=MC2.f(num)
st:list=[]
for i in names:
    stu:dict={}
    stu["name"]=i
    stu["height"]=random.randint(150,220)
    
    
    stu["weight"]=random.randint(40,90)
    
    st.append(stu)
print(st)