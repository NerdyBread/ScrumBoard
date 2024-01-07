class Group:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        
    def add_task(self, new_task):
        self.tasks.append(new_task)
        
    def remove_task(self, task):
        self.tasks.remove(task)
        
    """Getters and setters"""
    def get_tasks(self):
        return self.tasks