# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application_contact import ApplicationContact


@pytest.fixture
def app_contact(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app_contact):
    app_contact.login(username="admin", password="secret")
    app_contact.create_contact(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="IvAnOv",
                                          file_place="C:\\field_image_muholovka.jpg", title="employee", company="bank",
                                          address="Russia, Moscow, Green street 5",home="564585", mobile="89746521278",
                                          work="-", fax="-", email="test@test.ru", email2="-", email3="-", homepage="www.ivanov.ru",
                                          byear="1990", ayear="2000" ))
    app_contact.logout()


def test_add_empty_contact(app_contact):
    app_contact.login(username="admin", password="secret")
    app_contact.create_contact(Contact(firstname="", middlename="", lastname="", nickname="", file_place="", title="", company="", address="",
                                          home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", byear="", ayear=""))
    app_contact.logout()
