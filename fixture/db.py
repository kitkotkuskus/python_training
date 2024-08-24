import pymysql.cursors
from python_training.model.group import Group
from python_training.model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, fax, email, email2, email3, homepage, byear, ayear from addressbook")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, fax, email, email2, email3, homepage, byear, ayear) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename,
                                    lastname=lastname, nickname=nickname, company=company,
                                    title=title, address=address, home=home, mobile=mobile,
                                    work=work, fax=fax, email=email, email2=email2, email3=email3,
                                    homepage=homepage, byear=byear, ayear=ayear))
        finally:
            cursor.close()
        return list

    # where
    # deprecated = '0000-00-00 00:00:00

    def get_all_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, lastname, firstname, address, email, email2, email3, home, mobile, work from addressbook")
            for row in cursor:
                (id, lastname, firstname, address, email, email2, email3, home, mobile, work) = row
                list.append(Contact(id=str(id), lastname=lastname, firstname=firstname,
                                    address=address, email=email, email2=email2, email3=email3,
                                    home=home, mobile=mobile, work=work))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()