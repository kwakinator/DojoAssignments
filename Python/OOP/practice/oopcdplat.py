# class User(object):
#     pass
#
# michael = User()
# anna = User()
# print User()
# print User()

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = True
    def login(self):
        self.logged = True
        print self.name + " is logged in."
        return self
    def logout(self):
        self.logged = False
        print self.name + " is not logged in"
        return self
    def show(self):
        print "My name is {}. You can email me at {}".format(self.name, self.email)
        return self

new_user = User("Anna", "anna@anna.com")
print new_user.email

print new_user.login().show().logout()
