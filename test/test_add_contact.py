# -*- coding: utf-8 -*-
from python_training.model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="IvAnOv",
                               file_place="C:\\field_image_muholovka.jpg", title="employee", company="bank",
                               address="Russia, Moscow, Green street 5", home="564585", mobile="89746521278",
                               work="-", fax="-", email="test@test.ru", email2="-", email3="-", homepage="www.ivanov.ru",
                               byear="1990", ayear="2000"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", file_place=None, title="", company="", address="",
                               home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", byear="", ayear=""))
