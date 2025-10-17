import json
import task

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
             json_text += f"{json.dumps(current_task)}"
        else:
             json_text += f"{json.dumps(current_task)},\n"
    json_text += "]"
    with open(path, "w") as f:
        f.write(json_text)
    return json_text

def load_json(path="tasks.json"):
    new_data = []
    with open(path, "r") as f:
       contents = f.read()
       if contents == "":
           return []
       json_data = json.loads(contents)
    for item in json_data:
       new_data.append(task.Task(item["description"], item["status"], item["createdAt"], item["updatedAt"], id=item["id"]))
    return new_data