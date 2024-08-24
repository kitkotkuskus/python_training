from python_training.model.contact import Contact
from python_training.model.group import Group
import random


def test_add_contact_to_group(app, db, json_contacts):
    contact = json_contacts
    # Проверяем, что есть хотя бы одна группа
    if app.group.count() == 0:
        app.group.create(Group(name="test1"))
    # Проверяем, что есть хотя бы один контакт
    if len(app.contact.get_contact_list()) == 0:
        app.contact.create(contact)

    all_groups = app.group.get_group_list()
    all_contacts = app.contact.get_contact_list()
    random_contact = random.choice(all_contacts)
    random_group = random.choice(all_groups)
    app.contact.add_to_group(random_contact.id, random_group.id)
