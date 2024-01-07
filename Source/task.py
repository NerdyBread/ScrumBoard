class Task:
    def __init__(self, name, group=None):
        self.name = name
        self.group = group
        
    """Getters and setters"""
    
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name
    
    def get_group(self):
        return self.group
    
    def set_group(self, new_group):
        # This will be added to once the group class is created
        self.group = new_group