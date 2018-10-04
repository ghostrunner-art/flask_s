# 通过字符串找模块中的类的类属性的值
''''''
'''
# 多用户配置文件
import importlib
set = 'set.sset.setting.Foo' #类路径
*q,s  = set.rsplit('.') #切割获取目录及类名
q = '.'.join(q)    #用.拼接*q成为一个字符串
x=importlib.import_module(q)  #通过importlib.import_module方法寻找目录
cls=getattr(x,s)  #通过getattr在目录中找到类
dir_cls=dir(cls)  #查看所有的类属性及方法
for key in dir_cls: #遍历循环属性及方法
    if key.isupper():  #如果是大写就取到
        s = getattr(cls,key)  #通过getattr在类中获得大写的属性的值
        print(key,s) #打印
'''

