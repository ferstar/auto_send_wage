@echo off
cls
title 工资条自动发送程序
color 0A
echo.
echo ==============================
echo 请选择要进行的操作，然后按回车
echo ==============================
echo.
echo 1.准备好了,发消息吧
echo.
echo Q.我就看看,暂时不发
echo.
echo.
:cho
set choice=
set /p choice= 请选择:
IF NOT "%choice%"=="" SET choice=%choice:~0,1%
if /i "%choice%"=="1" goto run
if /i "%choice%"=="Q" goto endd
echo 选择无效，请重新输入
echo.
goto cho
:run
echo.
echo 请确保将图片放入 images 文件夹内
echo.
echo 图片名为微信备注名
echo.
pause
C:\Python27\Scripts\pip.exe install -r requirements.txt
C:\Python27\python.exe pay.py
echo.
echo 任务执行完毕
echo.
echo 失败图片在 images 目录
echo.
echo 按任意键退出 & pause > nul
:endd
exit