def build_profile(first: str, last: str, **user_info: str) -> dict:
    """
    to easy to describe
    :param first:
    :param last:
    :param user_info:
    :return:
    """
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


print(build_profile('Ji', 'Wenakng', weight='75kg', height='1.85cm'))
