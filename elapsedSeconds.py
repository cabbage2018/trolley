from dateutil.parser import parse

# 输入时间格式
a = parse('2019-10-30 23:43:10.123')
b = parse("2019-10-28/09:08:13.56212")

(a-b).days      # 获取天数的时间差
(a-b).seconds       # 获取时间差中的秒数，也就是23:43:10到09:08:13，不包括前面的天数和秒后面的小数
(a-b).total_seconds()       # 包括天数，小时，微秒等在内的所有秒数差
(a-b).microseconds      # 秒小数点后面的差值
