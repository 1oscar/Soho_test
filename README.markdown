---
tags: python,soho
---

## 使用说明：
1. **直接使用 `main.py -d 60 -u http://m.sohu.com -o /tmp/backup`命令之前的需要：**

>mac terminal下


 ** `pwd`   #获取当前路径，我的路径为`/Users/duankaifei/github/Soho_test`**
  **`ln -s /Users/duankaifei/github/Soho_test/main.py /usr/bin/main.py` #建立当前main.py到／usr/bin／main.py的软连接，这样就可以直接使用上述命令了**
 
2. **克隆**到本地，运行`main.py -d 60 -u http://m.sohu.com -o /tmp/backup`即可
3. 运行代码，如果要停止运行，请直接中断`ctrl+c`即可

## 过程与思路
1. 首先运行main.py和平时的python main.py不一样，这不要紧，这个我是放在了最后来考虑的，因为我知道这个可以通过sys.argv来获取每一个参数然后传给后面抓取等需要的参数 
2. 首先肯定要抓取页面，先确定用urllib2库
3. 存放的架构js, css, images等都是基于抓取下来的页面才考虑的，暂时放着
4. 每60秒备份一次，这个就是循环备份,`ctrl+c`来中断，最后考虑这个即可
5. 存放形式按时间间隔这个使用time库即可实现
6. 时间分隔存储代码，这个肯定首先要建立目录，才可保存网页的时候保存在这个目录下
7. 存储images，css，js等代码分别用不同的函数来执行
 - 存储图片的时候，需要考虑到jpg和png两种
 - 最终在本地存储的图片个数你会发现和代码里打印出的正则匹配出的图片个数不一样，这是因为有些图片名字是一样的，其实就是一样的图片，所以这里本地存储的会变少
 - 当然如果后期图画很多的话，可以这样优化：**正则出的图片列表去重操作即可**代码如下(共存在三种方法，这里仅列出一种，想知道的话，录了我就告诉你)：
 ```python
     image_dict = {}
     image_dict = image_list.fromkeys()
     image_list = image_dict.keys()
 ```

8. 获取页面images，css，js等的链接时候，可以通过正则来获取，**这里正则获取的时候�粗心写错了符号，耽误了点时间**
9. 回到第一条
 - 尝试1：在代码第一行导入path，这样便可通过python main.py来运行，但是不符合要求
 - 尝试2: `chmod +x main.py`在当前目录下执行上述命令，使得root，组用户，组外用户都可以执行此代码，通过这种形式执行：`./main.py`， 但是这也是不符合要求的
 - 尝试3: 把main.py代码拷贝到/usr/bin/下，这样可以直接执行`main.py`,但是这样很不友好，不方便管理维护代码等
 - 尝试4: 直接把pyhton运行的目录添加到当前代码的目录下，可以通过两种形式：终端下：`export PYTHONPATH=PYTHONPATH: DIR`,DIR即是python系统路径到到现在代码路径中间的路径等，但是这样还是不满足要求
 - 尝试5. 便是使用说明说的形式，建立软连接等,还是比较简单的
10. 代码结束直接运行`ctrl+c`即可
11. 代码没有添加判断语句,`try...expept`,因为代码默认比较小巧，很容易判断出现问题在哪里，后期要是优化，可以添加上,下面给出两种示例

```python
import traceback

try:
    代码语句
#这里推荐使用exception, e:可以捕获所有的异常等，e即是异常的代码
excep exception, e:  
    traceback.print_exc()  
    #这是可选的，traceback可以准确的输出代码的哪一行哪里出错以及原因等
    print str(e)  #这个也是打印出代码出错原因，但是没有traceback.print_exc（）详细，更加方便等
    代码语句
```

>您可能想了解的问题：

1. 为什么有些注释没有删除？
 代码写的多了容易忘记当初为什么写，这样一方面可以让自己快速回忆代码，另一方面也是为了别人测试与了解我代码更加的方便，直接把注释去掉即可。
