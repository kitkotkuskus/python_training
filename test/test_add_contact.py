# -*- coding: utf-8 -*-
from python_training.model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_number(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_mail(prefix):
    return prefix + '@' + random_string('', 4) + '.' + random_string('', 3)

def random_page(prefix):
    return prefix + random_string('', 6) + '.' + random_string('', 3)

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", file_place=None, title="", company="",
                    address="", home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="",
                    byear="", ayear="")]+[
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10), nickname=random_string("lastname", 10),
                    file_place="C:\\field_image_muholovka.jpg", title=random_string("title", 10), company=random_string("company", 10),
                    address=random_string("lastname", 10), home=random_number(11), mobile=random_number(11),
                    work=random_number(11), fax=random_number(6), email=random_mail("mail"), email2=random_mail("mail"), email3=random_mail("mail"), homepage=random_page("www."),
                    byear=random_number(4), ayear=random_number(4))
for i in range(2)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

