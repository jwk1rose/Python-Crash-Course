areas = ['da li', 'heaven', 'west_lake(with baobao)', 'west lake University', 'anywhere with beautiful scenery']
print("初始\n" + str(areas))
areas.sort()
print("正序\n" + str(areas))
areas.sort(reverse=True)
# sort 改变形参数据
print("逆序\n" + str(areas))
print("正序\n" + str(sorted(areas)))
# sorted 不改变形参数据
print("逆序\n" + str(sorted(areas, reverse=True)))
