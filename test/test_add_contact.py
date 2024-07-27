# -*- coding: utf-8 -*-
from python_training.model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="IvAnOv",
                               file_place="C:\\field_image_muholovka.jpg", title="employee", company="bank",
                               address="Russia, Moscow, Green street 5", home="564585", mobile="89746521278",
                               work="-", fax="-", email="test@test.ru", email2="-", email3="-", homepage="www.ivanov.ru",
                               byear="1990", ayear="2000"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", file_place=None, title="", company="", address="",
                               home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", byear="", ayear=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


