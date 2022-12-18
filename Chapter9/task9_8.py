class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'cam ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class User:
    def __init__(self, first_name, last_name, **user_info):
        """
        构造函数
        :param first_name:
        :param last_name:
        :param user_info: 可选的其他输入
        """
        self.info = {'first_name': first_name, 'last_name': last_name, 'login_attempts': 0}
        for key, value in user_info.items():
            self.info[key] = value

    def describe_user(self):
        for key, value in self.info.items():
            print(str(key) + ':' + str(value))

    def greet_user(self):
        print('Hello,' + self.info['first_name'])

    def increase_login_attempts(self):
        self.info['login_attempts'] += 1

    def reset_login_attempts(self):
        self.info['login_attempts'] = 0


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privilege = Privileges()


user = Admin('zhang', 'wang')
user.privilege.show_privileges()