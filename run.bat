@echo off
cls
title �������Զ����ͳ���
color 0A
echo.
echo ==============================
echo ��ѡ��Ҫ���еĲ�����Ȼ�󰴻س�
echo ==============================
echo.
echo 1.׼������,����Ϣ��
echo.
echo Q.�ҾͿ���,��ʱ����
echo.
echo.
:cho
set choice=
set /p choice= ��ѡ��:
IF NOT "%choice%"=="" SET choice=%choice:~0,1%
if /i "%choice%"=="1" goto run
if /i "%choice%"=="Q" goto endd
echo ѡ����Ч������������
echo.
goto cho
:run
echo.
echo ��ȷ����ͼƬ���� images �ļ�����
echo.
echo ͼƬ��Ϊ΢�ű�ע��
echo.
pause
C:\Python27\Scripts\pip.exe install -r requirements.txt
C:\Python27\python.exe pay.py
echo.
echo ����ִ�����
echo.
echo ʧ��ͼƬ�� images Ŀ¼
echo.
echo ��������˳� & pause > nul
:endd
exit