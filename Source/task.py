class Task:
    def __init__(self, name, group=None):
        self.name = name
        self.group = group
        
    def delete(self):
        if self.group:
            self.group.remove_task(self)
        self.group = None
        
    """Getters and setters"""
    
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name
    
    def get_group(self):
        return self.group
    
    def set_group(self, new_group):
        old_group = self.group
        if old_group:
            old_group.remove_task(self)
        self.group = new_group
        new_group.add_task(self)