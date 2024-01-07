import sys
import os

source_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.insert(0, source_path)

import pytest

from Source.group import Group
from Source.task import Task

class TestModifyTasks:
    def test_add_task(self):
        new_task = Task("Write code that works")
        new_group = Group("Reach goals")
        
        new_task.set_group(new_group)
        assert new_group.get_tasks() == [new_task]
        assert new_task.get_group() == new_group
    
    def test_move_task(self):
        new_task = Task("Don't take 2 hours just to get pytest running")
        
        possible_group = Group("Possible tasks")
        impossible_group = Group("Impossible tasks")
        
        new_task.set_group(possible_group)
        
        # Hours later
        
        new_task.set_group(impossible_group)
        
        assert new_task.get_group() == impossible_group
        assert possible_group.get_tasks() == []
        assert impossible_group.get_tasks() == [new_task]
        
    def test_remove_task(self):
        deletable_task = Task("Have a life")
        group = Group("Group")
        
        deletable_task.set_group(group)
        
        deletable_task.delete()
        
        assert group.get_tasks() == []
        
    def test_edit_task_name(self):
        task = Task("Hello world")
        
        new_name = "Goodbye world"       
        task.set_name(new_name)
        
        assert task.get_name() == new_name
        
class TestModifyGroups:
    def test_edit_group_name(self):
        group = Group("Bad name")
        new_name = "Good name"     
        group.set_name(new_name)
        
        assert group.get_name() == new_name