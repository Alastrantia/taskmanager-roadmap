# main.py
# entrypoint for the CLI
import sys, config
import saving

arguments = sys.argv[1:]
task_data = saving.load_json()

# get the available commands from config.py
commands = config.commands
def print_exit(message, exit_code=1):
    print(message)
    sys.exit(exit_code)

def call_function(command_data, arguments):
    global task_data
    arguments.insert(0, task_data)
    task_data = command_data["function_call_name"](*arguments) # wow thanks unpacking operator
    saving.save_json(task_data)
    sys.exit(0)


if arguments == []:
    print_exit("Welcome to the taskmanager CLI. Check README.md for usage instructions", exit_code=0)
    sys.exit(0)

base_command = arguments[0]
for command in commands:
    if base_command == command["base_name"]:
        if len(arguments) < command["minimum_required_arguments"]:
            print_exit("Not enough arguments given!")
        elif len(arguments) > command["maximum_arguments"]:
            print_exit("Too many arguments given!")
        
        call_function(command, arguments[1:])

print_exit("Command not found, check README.md for usage instructions")