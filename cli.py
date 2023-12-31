# from functions import get_todos, write_todos,... (but the line2 one is better)
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        # todos = [item.strip('\n') for item in todos]       list comprehension example

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            index = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a todo: ")
            todos[index] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            message = f"Todo '{todo_to_remove}' was removed from the list successfully."
            print(message)

            functions.write_todos(todos)

        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")

print('Bye!')
