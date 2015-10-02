__author__ = 'Liudmila'

from model.project import MyProject
import random

def test_delete_project(app):
    old_projects = app.project.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project(project.name)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert old_projects.sort(key=lambda x: x.name) == new_projects.sort(key=lambda x: x.name)