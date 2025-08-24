#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name, teacher=None):
        super().__init__(first_name, last_name)
        self.knowledge = []
        self.teacher = teacher
    
    def learn(self, new_knowledge):
        """Accept a new piece of knowledge and add it to the knowledge list"""
        self.knowledge.append(new_knowledge)
        