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

    def describe_restaurant(self):
        """
        输出餐馆的名字和类型
        :return:None
        """
        print('name:' + self.restaurant_name + ' cuisine_type:' + self.cuisine_type)

    def open_restaurant(self):
        """
        输出营业状态
        :return:
        """
        print(self.restaurant_name + ' is opening')


restaurant1 = Restaurant('G3', 'chuan cai')
restaurant2 = Restaurant('ting sha', 'yue cai')
print(restaurant1.restaurant_name, restaurant1.cuisine_type)
print(restaurant2.restaurant_name, restaurant2.cuisine_type)
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant1.open_restaurant()
restaurant2.open_restaurant()
