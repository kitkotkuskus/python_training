import random
from python_training.model.contact import Contact
from python_training.model.group import Group


def test_del_contact_from_group(app, db, json_contacts, orm):
    contact = json_contacts
    # Проверяем, что есть хотя бы одна группа
    if app.group.count() == 0:
        app.group.create(Group(name="test1"))
    # Проверяем, что есть хотя бы один контакт
    if len(app.contact.get_contact_list()) == 0:
        app.contact.create(contact)
    all_groups = db.get_group_list()
    random_group = random.choice(all_groups)
    # Получаем все контакты в выбранной группе
    contact_in_group = orm.get_contacts_in_group(random_group)
    # Проверяем наличие контакта в группе
    if len(contact_in_group) == 0:
        all_contacts = db.get_contact_list()
        random_contact = random.choice(all_contacts)
        app.contact.add_to_group(random_contact.id, random_group.id)
        contact_in_group = orm.get_contacts_in_group(random_group)
    # Ищем рандомный контакт в группе и удаляем его
    random_contact = random.choice(contact_in_group)
    app.contact.del_from_group(random_contact.id, random_group.id)