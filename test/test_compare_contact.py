import re
from model.contact import Contact


def test_compare_fields_on_home_page(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(contact_from_home_page) == len(contact_from_db)
    for i in range(len(contact_from_home_page)):
        assert contact_from_home_page[i].all_emails == merge_emails_like_on_home_page(contact_from_db[i])
        assert contact_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db[i])
        assert contact_from_home_page[i].address == contact_from_db[i].address
        assert contact_from_home_page[i].lastname == contact_from_db[i].lastname
        assert contact_from_home_page[i].firstname == contact_from_db[i].firstname

# def test_compare_fields_on_home_page(app, db):
#     contact_from_home_page = app.contact.get_contact_list()
#     contact_from_db = db.get_contact_list()
#     home_page_emails = [contact.all_emails for contact in contact_from_home_page]
#     db_emails = [merge_emails_like_on_home_page(contact) for contact in contact_from_db]
#     home_page_phones = [contact.all_phones_from_home_page for contact in contact_from_home_page]
#     db_phones = [merge_phones_like_on_home_page(contact) for contact in contact_from_db]
#     home_page_address = [contact.address for contact in contact_from_home_page]
#     db_address = [contact.address for contact in contact_from_db]
#     home_page_lastname = [contact.lastname for contact in contact_from_home_page]
#     db_lastname = [contact.lastname for contact in contact_from_db]
#     home_page_firstname = [contact.firstname for contact in contact_from_home_page]
#     db_firstname = [contact.firstname for contact in contact_from_db]
#     assert sorted(home_page_emails) == sorted(db_emails)
#     assert sorted(home_page_phones) == sorted(db_phones)
#     assert sorted(home_page_address) == sorted(db_address)
#     assert sorted(home_page_lastname) == sorted(db_lastname)
#     assert sorted(home_page_firstname) == sorted(db_firstname)


# def test_compare_fields_on_home_page(app):
#     contact_from_home_page = app.contact.get_contact_list()[0]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_home_page.all_emails == merge_emails_like_on_home_page(contact_from_edit_page)
#     assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
#     assert contact_from_home_page.address == contact_from_edit_page.address
#     assert contact_from_home_page.lastname == contact_from_edit_page.lastname
#     assert contact_from_home_page.firstname == contact_from_edit_page.firstname

# def test_compare_fields_on_contact_view_page(app):
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.all_emails == merge_emails_like_on_home_page(contact_from_edit_page)
#     assert contact_from_view_page.home == contact_from_edit_page.home
#     assert contact_from_view_page.mobile == contact_from_edit_page.mobile
#     assert contact_from_view_page.work == contact_from_edit_page.work
#     assert contact_from_view_page.address == contact_from_edit_page.address
#     assert contact_from_view_page.firstname == contact_from_edit_page.firstname
#     assert contact_from_view_page.lastname == contact_from_edit_page.lastname


def clear(s):
    return re.sub("[- ()]", "", s)


def merge_emails_like_on_home_page(contact):
    return list(filter(lambda x: x != "",
                     map(lambda x: re.sub("\n", "", x),
                         filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None,
                                [contact.home, contact.mobile, contact.work]))))