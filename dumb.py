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

# import collections

# dic = collections.OrderedDict()
# dic["keaton"] = [4,1]
# dic["aylor"] = [3,2]
# dic["billy"] = [1,3]
# dic["sally"] = [6,0]

# print(min(dic, key =dic.get))
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



import heapq as H

keaton = [5,3,6,5,1,9,56,1,34]
aylor = {(1,2):9,(1,3): 8, (1,4):1, (1,5): 6}
# test = [(1,(1,2,3)),(5(1,3,3)), (0,(3,1,2))]
test = [((1,2),((1,2,3),(4,5,7))),((0,2),((1,2,3),(4,5,8))),((0,1),((1,2,3),(4,5,9)))]
# print(test)
# curr = ((1,2,3),(4,5,8))

H.heapify(test)
if ((0,2),((1,2,3),(4,5,8))) in test:
    print("really?")# H.heappush(keaton, 0)
print(test[1])
# if 0 in keaton:
    # print("noway")
# print(keaton[3])
# H.heappush(keaton, 0)
# small = H.heappop(keaton)
# small1 = H.heappop(keaton)

# print(small)
# print(small1)
hold = H.heappop(test)
print(hold)
print(test)
if test:
    print("yeah")
other = []
H.heapify(other)
H.heappush(other, 3)
if other:
    print("dont")