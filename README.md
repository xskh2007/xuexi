

众所周知，在安装了Python的机器，通过命令行中的python xx.py，可以运行这个python文件，而如果你想在一些没有安装Python的机器，运行你的python文件，你可以利用py2exe这个组件将其打包成exe。

py2exe组件的安装极其简单，打开其托管在sourceforge的页面https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/

无论是64位系统好，32位系统好，基本上，下载关于python2.7的py2exe就对了，因为现在官网上最后一版python2.x就是python2.7.1，当然，如果有特殊情况除外。


这个py2exe-0.6.9.win32-py2.7.exe文件，可以直接无脑下一步安装到低。

之后，在需要转换成exe的python文件夹下，创建一个setup.py，里面写如下的python代码：

[python] view plain copy
print?在CODE上查看代码片派生到我的代码片

    from distutils.core import setup  
    import py2exe  
    setup(console=["将要转换的文件名称.py"])  

然后用命令行运行从终端（cmd）进入这个目录，输入以下命令：

[plain] view plain copy
print?在CODE上查看代码片派生到我的代码片

    python setup.py py2exe  

命令行弹完一大堆东西之后，这样便完成了从.py文件到 .exe文件的转换，生成的软件在dist文件夹内，直接将这个dist文件夹扔到没有安装python即可。在没有安装python的电脑，直接运行dist文件夹中的exe文件夹，则可以执行其中的python程序，同时，在一定程序下，起到封装python代码的功能。

