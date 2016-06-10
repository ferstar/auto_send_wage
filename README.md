# 缘由
认识一个人事妹子每次发工资时要给每个员工依次用微信发送对应的工资条, 本着程序猿济世救民的国际主义精神, 撸了这么个小脚本

## 运行环境

1. Windows
2. Python 2.7.xx

## 使用方法

1. 安装 Python 2.7.11

    我默认安装到了`C:\Python27`
    如果路径不同, 需要修改这两处对应路径
    https://github.com/ferstar/auto_send_wage/blob/master/run.bat#L31
    https://github.com/ferstar/auto_send_wage/blob/master/run.bat#L32
2. 将要发送的工资条截图文件重命名为对应姓名, 放入`images`文件夹
    
    例如: 张三丰 -对应图片-> 张三丰.png 
3. 图片安放好后, 双击运行`run.bat`按照提示操作即可

## 注意

1. 感谢这个轮子 https://github.com/littlecodersh/ItChat
2. 程序路径不要包含中文
3. 消息发送对象必须有中文备注
