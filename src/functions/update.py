from datetime import datetime

def update(tasks, id, description):
    current_time = str(datetime.now())
    index = next((i for i, x in enumerate(tasks) if callback(x, id)), None)
    if index == None:
        print(f"Could not find task with ID {id}")
        return tasks
    tasks[index].description = description
    tasks[index].updatedAt = current_time
    print(f"Task with ID: {tasks[index].id} updated successfully")
    return tasks

def callback(x, target_id):
    return x.id == target_id
