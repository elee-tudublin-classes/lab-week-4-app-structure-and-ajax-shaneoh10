from app.data_access.todo_dba import add_to_todo_list, get_todo_list


def get_all_todos():
    return get_todo_list()


def add_todo(item: str):
    new_todo = add_to_todo_list(item)

    return new_todo
