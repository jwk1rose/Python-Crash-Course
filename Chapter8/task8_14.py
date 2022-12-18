def car_info(maker, size, **info):
    """
    ...too simple ...
    :param maker:
    :param size:
    :param info:
    :return:
    """
    car = {'maker': maker, 'size': size}
    for key, value in info.items():
        car[key] = value
    return car


print(car_info('bentian', 'SUV', color='green', prize=100000, tow_package=True))
