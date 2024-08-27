from python_training.model.contact import Contact
from python_training.model.group import Group
import random


def test_add_contact_to_group(app, db, orm):
    if app.group.count() == 0:
        app.group.create(Group(name="test1"))
    if len(app.contact.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", file_place=None, title="", company="",
                    address="", home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="",
                    byear="", ayear=""))
    all_groups = app.group.get_group_list()
    random_group = random.choice(all_groups)
    if len(orm.get_contacts_not_in_group(random_group)) == 0:
        app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", file_place=None, title="", company="",
                    address="", home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="",
                    byear="", ayear=""))
    old_contacts_not_in_group = orm.get_contacts_not_in_group(random_group)
    random_contact = random.choice(old_contacts_not_in_group)
    app.contact.add_to_group(random_contact.id, random_group.id)
    old_contacts_not_in_group.remove(random_contact)
    new_contacts_not_in_group = orm.get_contacts_not_in_group(random_group)
    assert sorted(old_contacts_not_in_group, key=Contact.id_or_max) == sorted(new_contacts_not_in_group, key=Contact.id_or_max)

