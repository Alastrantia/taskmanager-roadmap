def mark_in_progress(tasks, id):
    index = next((i for i, x in enumerate(tasks) if callback(x, id)), None)
    if index == None:
        print(f"Could not find task with ID {id}")
        return tasks
    tasks[index].status = "in-progress"
    return tasks

def callback(x, target_id):
    return x.id == target_id
