from task9_12_2 import User


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'cam ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privilege = Privileges()
