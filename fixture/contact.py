

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # open add contact
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_name("submit").click()

    def update(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # open card first contact
        wd.find_element_by_xpath("//div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()
        # upd contact form
        self.fill_contact_form(contact)
        # submit contact update
        wd.find_element_by_name("update").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        wd.find_element_by_id("1").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_file_form(self, file):
        wd = self.app.wd
        if file is not None:
            wd.find_element_by_xpath("//div[@id='content']/form/input[@type='file']").send_keys(file)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.firstname)
        wd.find_element_by_name("photo").clear()
        self.fill_file_form(contact.file_place)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_xpath("//option[@value='20']").click()
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_xpath("//option[@value='January']").click()
        self.change_field_value("byear", contact.byear)
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[23]").click()
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[12]").click()
        self.change_field_value("ayear", contact.ayear)
