from time import time
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from fastapi import BackgroundTasks, FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    servers=[{"url": "https://fastapilangchain-1-w0858112.deta.app"}]
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_requests(request, call_next):
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time
    print(f"Request: {request.url} processed in: {process_time} sec")
    return response


class Todo(BaseModel):
    id: Optional[int] = None
    task: str
    is_completed: bool = False


async def send_email_notification(todo: Todo):
    print(f"Email notification for Todo {todo.id} sent!")


todos: List[Todo] = [
    Todo(id=1, task="Einkaufen", is_completed=False),
    Todo(id=2, task="Wäsche waschen", is_completed=False),
    Todo(id=3, task="Programmieren", is_completed=False),
]


@app.post("/todos")
async def create_todo(todo: Todo, background_tasks: BackgroundTasks):
    todo.id = len(todos) + 1
    todos.append(todo)
    background_tasks.add_task(send_email_notification, todo)
    return todo


# @app.post("/todos")
# async def create_todo(todo: Todo):
#     todo.id = len(todos) + 1
#     todos.append(todo)
#     return todo

# @app.get("/todos", response_model=List[Todo])
# async def read_todos():
#     return todos


@app.get("/todos", response_model=List[Todo])
async def read_todos(completed: Optional[bool] = None):
    if completed is None:
        return todos
    else:
        return [todo for todo in todos if todo.is_completed == completed]


@app.get("/todos/{id}")
async def read_todo(id: int):
    for todo in todos:
        if todo.id == id:
            return todo
    raise HTTPException(status_code=404, detail="Item not found")


@app.put("/todos/{id}")
async def update_todo(id: int, new_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == id:
            todos[index] = new_todo
            todos[index].id = id
            return
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/todos/{id}")
async def delete_todo(id: int):
    for index, todo in enumerate(todos):
        if todo.id == id:
            del todos[index]
            return
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/api-docs")
async def get_openapi_yaml():
    return FileResponse('openapi.yaml', media_type='application/x-yaml')