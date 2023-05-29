
##启动该服务有两种方式
方式一：
通过运行Python脚本启动服务，run.py 代码如下：

from waitress import serve
import main
serve(main.app, host='127.0.0.1',port=5000)
1
2
3
直接运行 run.py 即可

python run.py
1
验证我们可通过postman发送请求，得到如下结果：

##启动该服务有两种方式
方式一：
通过运行Python脚本启动服务，run.py 代码如下：

from waitress import serve
import main
serve(main.app, host='127.0.0.1',port=5000)
1
2
3
直接运行 run.py 即可

python run.py
1
验证我们可通过postman发送请求，得到如下结果：
————————————————
版权声明：本文为CSDN博主「小白白程序员」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_39691492/article/details/122088475
