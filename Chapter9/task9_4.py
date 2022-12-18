class Restaurant:
    """
    餐馆类
    """

    def __init__(self, restaurant_name: str, cuisine_type: str):
        """
        构造函数
        :param restaurant_name:餐馆名字
        :param cuisine_type:类型
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """
        输出餐馆的名字和类型
        :return:None
        """
        print(
            'name:' + self.restaurant_name + ' cuisine_type:' + self.cuisine_type + 'number_served:' + str(
                self.number_served))

    def open_restaurant(self):
        """
        输出营业状态
        :return:
        """
        print(self.restaurant_name + ' is opening')

    def set_number_served(self, number):
        """
        设置就餐人数
        :return:
        """
        self.number_served = number

    def increment_number_served(self, number):
        """

        :return:
        """
        self.number_served += number


restaurant = Restaurant('G3', 'chuancai')
restaurant.set_number_served(1000)
restaurant.describe_restaurant()
restaurant.increment_number_served(100)
restaurant.describe_restaurant()
