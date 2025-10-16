from datetime import datetime
import task

def add(tasks, description):
    current_time = str(datetime.now())
    new_task = task.Task(description, "todo", current_time, current_time)
    tasks.append(new_task)
    print(f"Task added successfully (ID: {new_task.id})")
    return tasks
