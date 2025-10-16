import json

def save_json(tasks, path="tasks.json"):
    json_text = "["
    for i in range(len(tasks)):
        current_task = {
            "id": tasks[i].id,
            "description": tasks[i].description,
            "status": tasks[i].status,
            "createdAt": tasks[i].createdAt,
            "updatedAt": tasks[i].updatedAt
        }
        if i == (len(tasks) - 1):
             json_text += f"{json.dumps(current_task)}\n"
        else:
             json_text += f"{json.dumps(current_task)},\n"
    json_text += "]"
    return json_text

def load_json(path):
    pass