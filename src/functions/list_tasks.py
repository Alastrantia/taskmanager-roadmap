def list_tasks(tasks, filter="none"):
    if filter == "none":
        return tasks
    if filter == "done":
        done_tasks = [item for item in tasks if item.status == 'done']
        return done_tasks
    if filter == "todo":
        todo_tasks = [item for item in tasks if item.status == 'todo']
        return todo_tasks
    if filter == "in-progress":
        progress_tasks = [item for item in tasks if item.status == 'in-progress']
        return progress_tasks
    else:
        return "Invalid filter"
