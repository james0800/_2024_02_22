from pydantic import BaseModel,RootModel

class data(BaseModel):
    name:str
    height:int
    weight:int
    bmi:float=0
    bmi_:str=""
    
    def f(self):
        self.bmi=self.weight/(self.height/100)**2
        if self.bmi<18.5:
            self.bmi_="體重過輕"
        elif self.bmi<24:
            self.bmi_="正常範圍"
        elif self.bmi<27 :
            self.bmi_="過重"
        elif self.bmi<30 :
            self.bmi_="輕度肥胖"
        elif self.bmi<35 :
            self.bmi_="中度肥胖"
        else :
            self.bmi_="重度肥胖"
        

class AllData(RootModel):
    root:list[data]
    def __iter__(self):
        return iter(self.root)
    def __getitem__(self,indext):
        return self.root[indext]

