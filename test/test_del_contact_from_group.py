import random
from model.contact import Contact
from model.group import Group


def test_del_contact_from_group(app, db, orm):
    if app.group.count() == 0:
        app.group.create(Group(name="test1"))
    if len(app.contact.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", file_place=None, title="", company="",
                    address="", home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="",
                    byear="", ayear=""))
    all_groups = db.get_group_list()
    random_group = random.choice(all_groups)
    if len(orm.get_contacts_in_group(random_group)) == 0:
        all_contacts = db.get_contact_list()
        random_contact = random.choice(all_contacts)
        app.contact.add_to_group(random_contact.id, random_group.id)
    contact_in_group = orm.get_contacts_in_group(random_group)
    random_contact = random.choice(contact_in_group)
    app.contact.del_from_group(random_contact.id, random_group.id)
    contact_in_group.remove(random_contact)
    new_contact_in_group = orm.get_contacts_in_group(random_group)
    assert sorted(contact_in_group, key=Contact.id_or_max) == sorted(new_contact_in_group, key=Contact.id_or_max)