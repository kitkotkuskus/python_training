# -*- coding: utf-8 -*-
import pytest
from python_training.model.contact import Contact
from python_training.fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="IvAnOv",
                                          file_place="C:\\field_image_muholovka.jpg", title="employee", company="bank",
                                          address="Russia, Moscow, Green street 5",home="564585", mobile="89746521278",
                                          work="-", fax="-", email="test@test.ru", email2="-", email3="-", homepage="www.ivanov.ru",
                                          byear="1990", ayear="2000"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", middlename="", lastname="", nickname="", file_place="", title="", company="", address="",
                                          home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", byear="", ayear=""))
    app.session.logout()
