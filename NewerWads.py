from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# address domain/path
# GET
# POST
# UPDATE
# DELETE

class ToDo(BaseModel):
    task : str
    description : str
    status : str

class UpdatetoDo(BaseModel):
    task : Optional[str]= None
    description : Optional[str]= None
    status : Optional[str]= None

toDos = {
    1: ToDo(task = "Homework", description = "urgent", status = "complete"),
    2: ToDo(task = "Excercise", description = "not urgent", status = "incomplete"),
    3: ToDo(task = "Laundry", description = "not urgent", status = "incomplete")
}

@app.get("/")
def index():
    return { "Yo waddup" : "Todo list creator API this is"}

#path paramater
# domain/get-toDo/1

@app.get("/get-toDo/{id}")
def get_toDo(id : int = Path(status = "Search the ID of the toDo you want to search")):
    return toDos[id]

#query parameter
#domain / get-toDo?search="task"
@app.get("/get-toDo-by-task/{toDo_id}")
def get_toDo(*, toDo_id: int, task: Optional[str] = None, status: str): 
    for toDo_id in toDos:
        if toDos[toDo_id]["task"] == task:
            return toDos[toDo_id]
    return {"Error":"toDover :("}

#POST method
@app.post("/create-toDo/{toDo_id}")
def add_toDo(toDo_id: int, toDo : ToDo):
    if toDo_id in toDos:
        return {"error" : "toDo exist already"}
    toDos[toDo_id] = toDo
    return toDos[toDo_id]

#PUT method
@app.put("/update-toDo/{toDo_id}")
def update_toDo(toDo_id: int, toDo: UpdatetoDo):
    if toDo_id not in toDos:
        return {"error" : "toDover (Todo hasn’t been added)"}

    if toDo.task != None:
        toDos[toDo_id].task = toDo.task
    if toDo.description != None:
        toDos[toDo_id].description = toDo.description
    if toDo.status != None:
        toDos[toDo_id].status = toDo.status
        
    return toDos[toDo_id]

#DELETE method
@app.delete("/delete-toDo/{toDo_id}")
def delete_toDo(toDo_id:int):
    if toDo_id not in toDos:
        return {"error" : "Delete failed"}
    del toDos[toDo_id]
    return {"data" : "Deletable and deleted"}
