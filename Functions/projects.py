project_list = ["Project 1", "Project 2", "Project 3", "Project 4", "Project 5"]

def add_project():
    project_list.append(input("Enter a project: "))
    return project_list

def view_project():
    print(project_list)
    return project_list

def add_project_at(index, project):
    project_list.insert(index, project)
    return project_list

def remove_project(index):
    project_list.pop(index)
    return project_list

add_project_at(index=int(input("Enter the index: ")), project=input("Enter the project: "))

view_project()