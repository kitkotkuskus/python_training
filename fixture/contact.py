from python_training.model.contact import Contact
import re


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
        self.contact_cache = None

    def update(self, contact):
        self.update_by_index(0)

    def update_by_index(self, index, contact):
        wd = self.app.wd
        self.open_home_page()
        # open card some contact
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        # upd contact form
        self.fill_contact_form(contact)
        # submit contact update
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # select contact
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def open_home_page(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("Send e-Mail")) > 0):
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

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("[name='entry']"):
                cells = element.find_elements_by_tag_name('td')
                id = element.find_element_by_css_selector("td.center").find_element_by_name("selected[]").get_attribute("value")
                lastname = element.find_element_by_css_selector("td:nth-child(2)").text
                firstname = element.find_element_by_css_selector("td:nth-child(3)").text
                all_phones = cells[5].text
                all_emails = cells[4].text
                address = cells[3].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails, address=address))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        home = wd.find_element_by_name('home').get_attribute('value')
        work = wd.find_element_by_name('work').get_attribute('value')
        mobile = wd.find_element_by_name('mobile').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        address = wd.find_element_by_name('address').text
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       home=home, work=work, mobile=mobile, email=email,
                       email2=email2, email3=email3, address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id('content').text
        home = re.search("H: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        email = wd.find_element_by_css_selector("a:nth-child(15)").text
        email2 = wd.find_element_by_css_selector("a:nth-child(17)").text
        email3 = wd.find_element_by_css_selector("a:nth-child(19)").text
        all_names = wd.find_element_by_css_selector("b:nth-child(1)").text.split()
        all_info = wd.find_element_by_id('content').text.splitlines()
        return Contact(home=home, work=work, mobile=mobile, email=email, email2=email2,
                       email3=email3, firstname=all_names[0], lastname=all_names[2], address=all_info[5])

