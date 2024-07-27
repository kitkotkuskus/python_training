class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None,
                 nickname=None, file_place=None, title=None, company=None,
                 address=None,home=None, mobile=None, work=None, fax=None,
                 email=None, email2=None, email3=None, homepage=None, byear=None, ayear=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.file_place = file_place
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.byear = byear
        self.ayear = ayear
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return self.id == other.id and self.lastname == other.lastname