from datetime import datetime

def mark_done(tasks, id):
    current_time = str(datetime.now())
    index = next((i for i, x in enumerate(tasks) if callback(x, id)), None)
    if index == None:
        print(f"Could not find task with ID {id}")
        return tasks
    tasks[index].status = "done"
    tasks[index].updatedAt = current_time
    print(f"Marked task with ID: {id} as done")
    return tasks

def callback(x, target_id):
    return x.id == target_id
