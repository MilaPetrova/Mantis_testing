__author__ = 'Liudmila'
from model.project import MyProject

def test_create_project(app):
    old_projects = app.project.get_project_list()
    project = MyProject(name="name21", status="stable", view_status="private", description="description1")
    app.project.create_project(project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert old_projects.sort(key=lambda x: x.name) == new_projects.sort(key=lambda x: x.name)