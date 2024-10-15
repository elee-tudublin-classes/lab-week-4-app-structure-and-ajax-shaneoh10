from pydantic import BaseModel


class ToDo(BaseModel):
    id: int
    details: str
    completed: bool = False
    user_id: int = 0
