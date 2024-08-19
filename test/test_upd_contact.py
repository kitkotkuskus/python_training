from python_training.model.contact import Contact
import random


def test_upd_contact(app, json_contacts, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", file_place=None, title="", company="", address="",
                               home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="", byear="", ayear=""))
    old_contacts = db.get_contact_list()
    random_contacts = random.choice(old_contacts)
    contact = json_contacts
    contact.id = random_contacts.id
    app.contact.update_by_id(random_contacts.id, contact)
    new_contacts = db.get_contact_list()
    index = old_contacts.index(random_contacts)
    old_contacts[index] = contact
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

