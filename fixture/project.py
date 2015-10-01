__author__ = 'Liudmila'
from model.project import MyProject
from selenium.webdriver.support.select import Select

class MyProjectHelper:

    def __init__(self, app):
        self.app = app


    def create_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_css_selector("td.form-title > form > input.button-small").click()
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input.button").click()
        self.project_cache = None

    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        status_value = Select(wd.find_element_by_name("status"))
        status_value.select_by_visible_text(project.status)
        view_status_value = Select(wd.find_element_by_name("view_state"))
        view_status_value.select_by_visible_text(project.view_status)
        self.change_field_value("description", project.description)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def open_project_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/proj_page")and len(wd.find_element_by_css_selector("td.form-title > form > input.button-small")) > 0):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    project_cache = None
    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            project_cache = []
            for element in wd.find_elements_by_xpath("//div[1]/table/tbody/tr"):
                cells = element.find_elements_by_tag_name("td")
                text = cells[0].text
                project_cache.append(MyProject(name=text))
            return  project_cache



