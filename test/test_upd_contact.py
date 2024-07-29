from python_training.model.contact import Contact
from random import randrange


def test_upd_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", file_place=None, title="", company="", address="",
                               home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", byear="", ayear=""))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Petr", middlename="Petrovich", lastname="Petrov", nickname="PeTrOv",
                               file_place="C:\\20639.jpg", title="admin", company="sport",
                               address="Russia, Moscow, Red street 4", home="444444", mobile="89667891255",
                               work="124544", fax="124544", email="test44@test.ru", email2="test44@test.ru", email3="test44@test.ru", homepage="www.petrov.ru",
                               byear="1994", ayear="2004")
    contact.id = old_contacts[index].id
    app.contact.update_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

