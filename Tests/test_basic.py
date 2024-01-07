import sys
import os

source_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
print(source_path)
sys.path.insert(0, source_path)
print(sys.path[0])

import pytest

from Source.group import Group
from Source.task import Task

class TestMoveTasks:
    def test_add_task(self):
        new_task = Task("Write code that works")
        new_group = Group("Reach goals")
        
        new_task.set_group(new_group)
        assert new_group.get_tasks() == [new_task]
        assert new_task.get_group() == new_group
    
    def test_remove_task(self):
        new_task = Task("Don't take 2 hours just to get pytest running")
        
        possible_group = Group("Possible tasks")
        impossible_group = Group("Impossible tasks")
        
        new_task.set_group(possible_group)
        
        # Hours later
        
        new_task.set_group(impossible_group)
        
        assert new_task.get_group() == impossible_group
        assert possible_group.get_tasks() == []
        assert impossible_group.get_tasks() == [new_task]