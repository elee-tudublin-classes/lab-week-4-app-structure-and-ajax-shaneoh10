from fastapi import APIRouter, Form
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.services.todo_service import add_todo, get_all_todos

router = APIRouter(prefix="/todo", tags=["todo"])


templates = Jinja2Templates(directory="app/view_templates")


@router.get("/", response_class=HTMLResponse)
async def todos(request: Request):
    """Handle http get requests for the site root / and return the todos.html page"""

    return templates.TemplateResponse(
        "todos.html", {"request": request, "todoList": get_all_todos()}
    )


@router.post("/add")
def add_item(request: Request, item: str = Form(...)):
    """Add a new todo item to the list"""
    new_todo: str = add_todo(item)

    return templates.TemplateResponse(
        "partials/todo/todo_li.html", {"request": request, "todo": new_todo}
    )
