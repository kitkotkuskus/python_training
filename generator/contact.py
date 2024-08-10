from python_training.model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
            Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                    lastname=random_string("lastname", 10), nickname=random_string("lastname", 10),
                    file_place="C:\\field_image_muholovka.jpg", title=random_string("title", 10), company=random_string("company", 10),
                    address=random_string("lastname", 10), home=random_number(11), mobile=random_number(11),
                    work=random_number(11), fax=random_number(6), email=random_mail("mail"), email2=random_mail("mail"),
                    email3=random_mail("mail"), homepage=random_page("www."),
                    byear=random_number(4), ayear=random_number(4))
            for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

