# trolley
Train a trolley to trace certain pattern of lane.
size is of 4m*3.5m.

python倒叙遍历一个list
C语言中从后往前遍历数组是很方便的，如：

for(int i = 5; i >= 0; i--){
    printf("%d\n", i);
}
但是在python中默认是从前往后遍历列表的，有时候需要从后往前遍历。根据 range 函数的用法：

range(start, end[, step])

python中从后往前遍历列表的方法为：

lists = [0, 1, 2, 3, 4, 5]
# 输出 5, 4, 3, 2, 1, 0
for i in range(5, -1, -1):
    print(lists[i])
 
# 输出5, 4, 3
for i in range(5, 2, -1):
    print(lists[i])
从最后遍历到最前面，就是

for i in range(len(lists)-1, -1, -1):
