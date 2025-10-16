# main.py
# entrypoint for the CLI
import sys, config, task
import saving
arguments = sys.argv[1:]
task_data = [task.Task("blah", "duh", "bla", "whocares", id="1"), task.Task("blah", "duh", "bla", "whocares", id="1")] # connected to json storage
saving.save_json(task_data)


# get the available commands from config.py
commands = config.commands
def print_exit(message, exit_code=1):
    print(message)
    sys.exit(exit_code)

def call_function(function_name, command_data, arguments):
    global task_data
    arguments.insert(0, task_data)
    print(f"calling {function_name}, {arguments}")
    task_data = command_data["function_call_name"](*arguments) # wow thanks unpacking operator


if arguments == []:
    print_exit("Welcome to the taskmanager CLI. Check README.md for usage instructions or run with --help", exit_code=0)
    sys.exit(0)

base_command = arguments[0]
for command in commands:
    if base_command == command["base_name"]:
        if len(arguments) < command["minimum_required_arguments"]:
            print_exit("Not enough arguments given!")
        elif len(arguments) > command["maximum_arguments"]:
            print_exit("Too many arguments given!")
        
        call_function(base_command, command, arguments[1:])
