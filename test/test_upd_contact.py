from python_training.model.contact import Contact


def test_upd_contact(app):
    app.contact.update(Contact(firstname="Petr", middlename="Petrovich", lastname="Petrov", nickname="PeTrOv",
                               file_place="C:\\20639.jpg", title="admin", company="sport",
                               address="Russia, Moscow, Red street 4", home="444444", mobile="89667891255",
                               work="124544", fax="124544", email="test44@test.ru", email2="test44@test.ru", email3="test44@test.ru", homepage="www.petrov.ru",
                               byear="1994", ayear="2004"))


