# use numpy array to record trolley's trace,
# learn from existing trace/track
#
dictionary=dict( [["a",1],["b",2],["c",3]] )
print(dictionary)   #{'b': 2, 'a': 1, 'c': 3}
print( type(dictionary ))  #<class 'dict'>


a_dict = {'name':'DYX', 'sex':'male', 'age':24}
print(a_dict.get('ranking'))   #None  指定的键ranking不存在返回None
print(a_dict.get('ranking','No entry'))  #No entry  指定的键不存在，返回指定的内容No entry

a_dict = {'name': 'DYX', 'sex': 'male', 'age': 24}
print(a_dict.keys())  # 输出字典的键 dict_keys(['name', 'age', 'sex'])
print(type(a_dict.keys()))  # 查看一下类型 <class 'dict_keys'>
print(list(a_dict.keys()))  # ['age', 'name', 'sex']

# 可以用循环的方式输出
for key in a_dict.keys():
    print(key, end=" ")  # name sex age

a_dict = {'name': 'DYX', 'sex': 'male', 'age': 24}
print(a_dict.items())  # dict_items([('age', 24), ('name', 'DYX'), ('sex', 'male')])
print(type(a_dict.items()))  # <class 'dict_items'>

# 通常用遍历来做
for item in a_dict.items():
    print(item, end=" ")  # ('sex', 'male') ('name', 'DYX') ('age', 24)
# 查看一下item的类型
print("\n", type(item))  # <class 'tuple'> 元组类型

a_dict = {'name':'DYX', 'sex':'male', 'age':24}
for key,values in a_dict.items():
    print(key,values) #单纯遍历输出两个值，所以不是元组形式
#age 24
#sex male
#name DYX

#update
#dict_items([('sex', 'male'), ('age', 24), ('name', 'DYX'), ('ranking', [98, 97])])
a_dict.update( {'a':'a','b':'b'} )
print(a_dict)  #查看添加后的字典

# delete
#print(a_dict)  #{'age': 24, 'sex': 'male'}
#del a_dict
#print(a_dict)  #NameError: name 'a_dict' is not defined  报错

#clear()方法来删除字典中所有元素。
a_dict = {'name':'DYX', 'sex':'male', 'age':24}
a_dict.clear()
print(a_dict)  #{}
#注意和del 的不同，del是删除整个字典，clear()方法是删除字典里面的元素。

#pop()方法删除并返回指定“键”的元素。
a_dict = {'name':'DYX', 'sex':'male', 'age':24}
temp = a_dict.pop("name")

a_dict = {'name':'DYX', 'sex':'male', 'age':24}
print("name" in a_dict) #True
print("ranking" in a_dict) #False

#Python2中，字典对象has_key()方法测试字典是否包含指定的键。python3不再支持这个方法，需要使用in。
#a_dict = {'name':'DYX', 'sex':'male', 'age':24}
#print (a_dict.has_key("name"))  #True
#print(a_dict.has_key("ranking"))  #False

import collections
x=collections.OrderedDict()  #创建一个有序字典
x['a']=3   #有就修改元素的“值”，无就在字典中更新这个“键-值对”
x['b']=5
x['c']=8
print(x)    #OrderedDict( [ ('a', 3), ('b', 5), ('c', 8) ] )
print( dict(x) )   #又变为无序字典{'b': 5, 'a': 3, 'c': 8}

#浅复制
a_dict = {'name':'DYX', 'sex':'male', 'age':24}
b_dict = a_dict.copy()
print(b_dict)  #{'age': 24, 'name': 'DYX', 'sex': 'male'}
b_dict["name"] = "DDD"
print(b_dict)  #{'sex': 'male', 'name': 'DDD', 'age': 24}
print(a_dict)  #{'sex': 'male', 'name': 'DYX', 'age': 24}
#修改b_dict不影响a_dict

#
a_dict = {'name':'DYX', 'sex':'male', 'age':24}
c_dict = a_dict
c_dict["name"] = "DDD"
print(c_dict)  #{'sex': 'male', 'name': 'DDD', 'age': 24}
print(a_dict) #{'sex': 'male', 'name': 'DDD', 'age': 24}
#修改c_dict等同修改a_dict

#排序 根据键
test_dict = {"DDD":15, "CMJ":43, "HLZ":66, "HXH":39}
res = sorted(test_dict.items())
print(res)  #[('CMJ', 43), ('DDD', 15), ('HLZ', 66), ('HXH', 39)]
#等同于
res = sorted(test_dict.items(),key=lambda d:d[0])
print(res) #[('CMJ', 43), ('DDD', 15), ('HLZ', 66), ('HXH', 39)]

#值
res = sorted(test_dict.items(),key=lambda d:d[1])
print(res)  #[('DDD', 15), ('HXH', 39), ('CMJ', 43), ('HLZ', 66)]

res = sorted(test_dict.items(),key=lambda d:d[1], reverse = True)
print(res)  #[('HLZ', 66), ('CMJ', 43), ('HXH', 39), ('DDD', 15)]

#“键Key”进行排序
test_dict = {"DDD":15, "CMJ":43, "HLZ":66, "HXH":39}
#依据五选排名（不懂的忽略我这句注释）
sorted_key = sorted(test_dict)
print(sorted_key )  #['CMJ', 'DDD', 'HLZ', 'HXH']
#print(type(sorted_key))  #<class 'list'>
for k in sorted_key:
    print(k, test_dict[k],end = " ")  #CMJ 43 DDD 15 HLZ 66 HXH 39

#“值Value”进行排序
test_dict = {"DDD":15, "CMJ":43, "HLZ":66, "HXH":39}
sorted_value = sorted(test_dict, key=test_dict.__getitem__)
print(sorted_value)  #['DDD', 'HXH', 'CMJ', 'HLZ']
for k in sorted_value:
    print(k, test_dict[k],end = " ")  #DDD 15 HXH 39 CMJ 43 HLZ 66

