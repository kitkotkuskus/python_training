from python_training.model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="", middlename="", lastname="",
                                   nickname="", file_place=None, title="", company="",
                                   address="",home="", mobile="", work="", fax="", email="",
                                   email2="", email3="", homepage="", byear="", ayear=""))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
