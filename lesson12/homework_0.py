import requests
from requests import Response
from pydantic import root_model,BaseModel
from pprint import pprint
from pydantic import BaseModel, RootModel, Field,field_validator
from pprint import pprint
import pandas as pd

url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
class Data(BaseModel):
    #擷取資料
    where:str=Field(alias="sna")
    nmae:str=Field(alias="sarea")
    total:int=Field(alias="tot")
    boIn:int=Field(alias="sbi")
    boOut:int=Field(alias="bemp")
    data:str=Field(alias="mday")
    field_validator("total","boIn","boOut",mode='before')
    #避免特定資列為空字串
    @classmethod
    def empty_to_zero(cls,value):
        if value=='':
            return '0'
        else:
            return value  


class AllData(RootModel):
    root:list[Data]
    def __iter__(self) :
        return iter(self.root)
    def __getitem__(self,ind):
        return self.root[ind]
    
    
def get_request(link:str)->Response|None:
    try:
        re:Response=requests.get(link)
        re.raise_for_status()
        if re.status_code==200:
            print("Asset")
            return re
        else:
            print("Fail")
    except:
        print("Fail")
        return None

def main()->int:
    req:requests=get_request(url)
    if req==None:
        return -1
    ind=req.text
    data:Data=AllData.model_validate_json(ind)
    pd.DataFrame(data)
    return 0
print(main())



