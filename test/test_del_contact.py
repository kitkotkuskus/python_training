from python_training.model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="", middlename="", lastname="",
                                   nickname="", file_place=None, title="", company="",
                                   address="",home="", mobile="", work="", fax="", email="",
                                   email2="", email3="", homepage="", byear="", ayear=""))
    app.contact.delete_first_contact()