from task import Task
from group import Group

if __name__ == "__main__":
    # Default starting setup
    ice_box = Group("Ice Box")
    in_progress = Group("In Progress")
    done = Group("Done")
    
    default_task = Task("Welcome to ScrumBoard!")
    default_task.set_group(ice_box)