from typing import Optional
from fastapi import FastAPI

app=FastAPI()

item=[]

@app.get("/")
def index():
    return {"data":"Hello"}

@app.post("/item")
def create_item(ID:int,Name:str,Weight:float,Description:Optional[str]=None):
    item.append({
        "ID":ID,
        "Name":Name,
        "Weight":Weight,
        "Description":Description
    })

    return{"data":item}


@app.get("/item")
def show_items():
    return {"data":item}

@app.put("/item/{id}")
def update_item(id:int,Name:str,Weight:float,Description:Optional[str]=None):
    for q in item:
        if q["ID"]==id:
            q["Name"]=Name
            q["Weight"]=Weight
            q["Description"]=Description
    return {"data":item}