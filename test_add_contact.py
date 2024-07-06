# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group_contact import *

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_contact_name(wd, Group_contact_name(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="IvAnOv"))
        self.add_contact_file(wd, Group_contact_file(file_place="C:\\field_image_muholovka.jpg"))
        self.add_contact_job_info(wd, Group_contact_job(title="employee", company="bank", address="Russia, Moscow, Green street 5"))
        self.add_contact_telephone_info(wd, Group_contact_phone(home="564585", mobile="89746521278", work="-", fax="-"))
        self.add_contact_mail_info(wd, Group_contact_email(email="test@test.ru", email2="-", email3="-"))
        self.add_contact_homepage_info(wd, Group_contact_homepage(homepage="www.ivanov.ru"))
        self.add_contact_date_form(wd, Group_contact_date(byear="1990", ayear="2000"))
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.add_contact_name(wd, Group_contact_name(firstname="", middlename="", lastname="", nickname=""))
        self.add_contact_job_info(wd, Group_contact_job(title="", company="", address=""))
        self.add_contact_telephone_info(wd, Group_contact_phone(home="", mobile="", work="", fax=""))
        self.add_contact_mail_info(wd, Group_contact_email(email="", email2="", email3=""))
        self.add_contact_homepage_info(wd, Group_contact_homepage(homepage=""))
        self.add_contact_date_form(wd, Group_contact_date(byear="", ayear=""))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def add_contact_name(self, wd, group_contact):
        # open add contact
        wd.find_element_by_link_text("add new").click()
        # fill contact name form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(group_contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(group_contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(group_contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(group_contact.nickname)

    def add_contact_file(self, wd, group_contact):
        # choose contact photo
        wd.find_element_by_xpath("//div[@id='content']/form/input[@type='file']").send_keys(
            group_contact.file_place)

    def add_contact_job_info(self, wd, group_contact):
        # fill contact job info form
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(group_contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(group_contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(group_contact.address)

    def add_contact_telephone_info(self, wd, group_contact):
        # fill contact telephone form
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(group_contact.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(group_contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(group_contact.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(group_contact.fax)

    def add_contact_mail_info(self, wd, group_contact):
        # fill contact mail form
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(group_contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(group_contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(group_contact.email3)

    def add_contact_homepage_info(self, wd, group_contact):
        # fill contact homepage form
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(group_contact.homepage)

    def add_contact_date_form(self, wd, group_contact):
        # fill contact name form and submit
        wd.find_element_by_name("bday").click()
        wd.find_element_by_xpath("//option[@value='21']").click()
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_xpath("//option[@value='July']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(group_contact.byear)
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[23]").click()
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[12]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(group_contact.ayear)
        # submit contact creation
        wd.find_element_by_name("submit").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
