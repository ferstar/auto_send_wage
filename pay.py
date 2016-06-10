# encoding: utf-8

"""
@author: ferstar
@software: PyCharm Community Edition
@file: pay.py
@time: 2016/6/9 17:00
"""
import logging
import shutil
import sys

import itchat
import os


def log():
    # 创建一个logger实例
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # 创建一个handler,用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # 定义handler的输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)

    # 给logger添加handler
    logger.addHandler(ch)
    return logger


def get_parent_path():
    path = os.path.dirname(sys.argv[0])
    return os.path.abspath(path)


def get_user_img(d):
    new_dict = {}
    for parent, dirnames, filenames in os.walk(d):
        for filename in filenames:
            item = filename.split(".")
            peer_path = parent + "\\" + item[0].decode("gbk") + "." + item[1]
            new_dict[item[0].decode("gbk")] = peer_path
    return new_dict


def get_user_name(remark_name, contract_list):
    """根据备注取得用户名/全拼"""
    user_name = ""
    quan_pin = ""
    for i in contract_list:
        if i["RemarkName"] == remark_name:
            user_name = i["UserName"]
            quan_pin = i["RemarkPYQuanPin"]
            break
    return user_name, quan_pin


def main():
    parent_dir = get_parent_path()
    image_dir = parent_dir + "\\" + "images"
    image_dict = get_user_img(image_dir)
    fail_lst = []
    itchat.auto_login()
    contract = itchat.get_contract()
    for user, image in image_dict.items():
        user_name, quan_pin = get_user_name(user, contract)
        if not user_name or not quan_pin:  # 好友列表不存在
            fail_lst.append(user)
            log.debug(u"%s 的工资条发送失败!" % user)
            continue
        temp_path = parent_dir + "\\" + quan_pin + "." + image.split(".")[1]
        # 中文图片移到上级目录, 改名为拼音
        shutil.move(image, temp_path)
        if itchat.send_image(temp_path, user_name):
            log.debug(u"%s 的工资条发送成功!" % user)
            os.remove(temp_path)  # 删除临时文件
        else:
            fail_lst.append(user)
            log.debug(u"%s 的工资条发送失败!" % user)
    log.debug(u"成功发送 %s 条工资信息" % (len(image_dict) - len(fail_lst)))
    if fail_lst:
        log.debug(u"%s 条发送失败, 名单如下" % len(fail_lst))
        for i in fail_lst:
            log.debug(i)
        os.startfile(image_dir)


if __name__ == '__main__':
    log = log()
    main()
