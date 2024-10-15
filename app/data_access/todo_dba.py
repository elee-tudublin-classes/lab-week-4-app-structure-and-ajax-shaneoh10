from app.models.todo import ToDo

todos_list = []

t1 = ToDo(
    id=1, details="Add my 2 questions to PeerWise, then answer 10 leaving feedback."
)
t2 = ToDo(id=2, details="Watch week 4 lab video.")
t3 = ToDo(id=3, details="Complete week 4 lab and push to GitHub Classroom.")
t4 = ToDo(id=4, details="Learn the parts of Python I have forgotten.")

todos_list.append(t1)
todos_list.append(t2)
todos_list.append(t3)
todos_list.append(t4)


def get_todo_list():
    """Return the list of todo items"""
    return todos_list


def add_to_todo_list(details: str):
    """Add a new todo item to the list"""
    # generate id based on list length and set details = the param value
    new_todo = ToDo(id=len(todos_list) + 1, details=details)

    todos_list.append(new_todo)

    return new_todo
