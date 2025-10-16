# task.py
from functions.add import add
from functions.delete import delete
from functions.list_tasks import list_tasks
from functions.mark_done import mark_done
from functions.mark_in_progress import mark_in_progress
from functions.update import update

commands = [
    {
        "base_name": "add",
        "additional_arguments": ["task_name"],
        "minimum_required_arguments": 2,
        "maximum_arguments": 2,
        "function_call_name": add
    }, 
    {
        "base_name": "update",
        "additional_arguments": ["task_id", "new_description"],
        "minimum_required_arguments": 3,
        "maximum_arguments": 3,
        "function_call_name": update
    }, 
    {
        "base_name": "delete",
        "additional_arguments": ["task_id"],
        "minimum_required_arguments": 2,
        "maximum_arguments": 2,
        "function_call_name": delete
    }, 
    {
        "base_name": "mark-in-progress",
        "additional_arguments": ["task_id"],
        "minimum_required_arguments": 2,
        "maximum_arguments": 2,
        "function_call_name": mark_in_progress
    }, 
    {
        "base_name": "mark-done",
        "additional_arguments": ["task_id"],
        "minimum_required_arguments": 2,
        "maximum_arguments": 2,
        "function_call_name": mark_done
    }, 
    {
        "base_name": "list",
        "additional_arguments": ["filter"],
        "minimum_required_arguments": 1,
        "maximum_arguments": 2,
        "function_call_name": list_tasks
    }, 
]
