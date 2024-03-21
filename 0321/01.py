from  lib.MC import data,AllData
names = [
    {'name':'徐xx','height':178,'weight':78},
    {'name':'王xx','height':168,'weight':75},
    {'name':'張xx','height':183,'weight':78},
]
guy:AllData=AllData.model_validate(names)
for i in guy:
    i.f()
    print(f"{i.name} {i.bmi:.2f} {i.bmi_}")