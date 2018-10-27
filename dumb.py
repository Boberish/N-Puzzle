# k = "keaton"

# k = list(k)

# # del k[3:]
# # print(k)

# k = ((1,1),(2,1))
# e = ((2,1),(1,1))

# # if k == e:
# #     print("kekjek")

# # # a = []
# # a = list(list(x) for x in k)
# # print(a)
# # k = {}
# k = {'k':1,'e':2,'a':3}

# # k['e'] = 4
# # print(k)

import collections

dic = collections.OrderedDict()
dic["keaton"] = [4,1]
dic["aylor"] = [3,2]
dic["billy"] = [1,3]
dic["sally"] = [6,0]

print(min(dic, key =dic.get))
# # print(dic)
# dic = collections.OrderedDict(sorted(dic.items(), key=lambda x: x[1]))

# print(list(dic.keys()))

# keaton = [1,2,3,4,5]
# new = [num  for num in keaton]
# print(new)

# se = set(dic)
# if 'aylor' in se:
#     print("YOYO")
# print(se)