class Group_contact_name:
    def __init__(self, firstname, middlename, lastname, nickname):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname

class Group_contact_file:
    def __init__(self, file_place):
        self.file_place = file_place

class Group_contact_job:
    def __init__(self, title, company, address):
        self.title = title
        self.company = company
        self.address = address

class Group_contact_phone:
    def __init__(self, home, mobile, work, fax):
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax

class Group_contact_email:
    def __init__(self, email, email2, email3):
        self.email = email
        self.email2 = email2
        self.email3 = email3

class Group_contact_homepage:
    def __init__(self, homepage):
        self.homepage = homepage

class Group_contact_date:
    def __init__(self, byear, ayear):
        self.byear = byear
        self.ayear = ayear