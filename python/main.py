def create_task():
    description = input("Enter description: ")
    assignee = int(input("Enter assignee: "))

    return {"description": description, "assignee": assignee}


def create_space(name):
    list_of_tasks = []
    for _ in range(3):
        task = create_task()
        list_of_tasks.append(task)

    space = {
        "name": name,
        "tasks": list_of_tasks
    }

    return space


space = create_space("Dev")
print(space)
