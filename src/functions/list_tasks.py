def list_tasks(tasks, filter="none"):
    filtered_tasks = [item for item in tasks if item.status == filter]
    if filter == "none":
        filtered_tasks = tasks
        
    for task in filtered_tasks:
        print(f"{task.description}: {task.status}")
    return tasks