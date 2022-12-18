def make_album(name: str, album: str, song_num: str = '') -> dict[str, str, str]:
    """
    ...
    :param name:...
    :param album:...
    :param song_num:...
    :return:....
    """

    output = {}
    if song_num:
        output['name'] = name
        output['album'] = album
        output['song_num'] = song_num
    else:
        output['name'] = name
        output['album'] = album
    return output


print(make_album('Jay', 'fan te xi', '10'))
print(make_album('Jay', 'also fan te xi'))