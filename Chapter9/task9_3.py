class User:
    def __init__(self, first_name, last_name, **user_info):
        """
        构造函数
        :param first_name:
        :param last_name:
        :param user_info: 可选的其他输入
        """
        self.info = {'first_name': first_name, 'last_name': last_name}
        for key, value in user_info.items():
            self.info[key] = value

    def describe_user(self):
        for key, value in self.info.items():
            print(str(key) + ':' + str(value))

    def greet_user(self):
        print('Hello,' + self.info['first_name'])


user1 = User('bao', 'bao', age=21, describe='beautiful', gender='girl')
user2 = User('kang', 'kang', age=20, describe='handsome', gender='boy', weight=150)
user1.describe_user()
user2.describe_user()
user1.greet_user()
user2.greet_user()
