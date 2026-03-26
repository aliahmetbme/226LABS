def taskManager():
    task_dict = {}
    execution_order = []
    completed_tasks = set()

    try:
        num_tasks = int(input("Enter number of tasks: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    for _ in range(num_tasks):
        task_name = input("Enter task name: ")
        num_deps = int(input(f"How many dependencies for {task_name}? "))

        dependencies = []

        for j in range(num_deps):
            dep = input(f"Enter dependency {j+1}: ")
            dependencies.append(dep)
        
        task_dict[task_name] = dependencies

    print("\nTASK STRUCTURE:")
    for task, deps in task_dict.items():
        print(f"{task} -> {deps}")    

    print("\nINITIAL TASKS (no dependencies):")
    initial_task_found = False
    for task, deps in task_dict.items():
        if not deps:
            print(task)
            initial_task_found = True
    
    if not initial_task_found:
        print("None")   
    
    while len(completed_tasks) < len(task_dict):
        progress_made = False

        for task, deps in task_dict.items():
            if task not in completed_tasks and all(dep in completed_tasks for dep in deps):
                completed_tasks.add(task)
                execution_order.append(task)
                progress_made = True
        
        if not progress_made:
            break

    print("\nEXECUTION ORDER:")
    if not execution_order:
        print("No task can be started.")
    else:
        for i, task in enumerate(execution_order):
            print(f"Step {i+1}: {task}")

    if len(completed_tasks) < num_tasks:
        print("ERROR: Circular dependency detected!")
        print("These tasks could not be completed:")
        for task in task_dict:
            if task not in completed_tasks:
                print(task)
    else:
        print("ALL TASKS COMPLETED SUCCESSFULLY")

taskManager()
