#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

def fun_Filter_Data(log):
    filter_ls = []
    with open("data/{0}".format(log)) as f:
        for line in f:
            try:
                val = line.replace("\n", "").split("msec = ")[1]
                if float(val) > 25:
                    filter_ls.append(line)
            except Exception as e:
                pass

    with open("result/{0}".format(log.split("_")[1]),"a") as f:
        for line in filter_ls:
            f.write(line)

def del_file(path):
    file_ls = os.listdir(path)
    for file in file_ls:
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            del_file(file_path)
        else:
            os.remove(file_path)

if __name__ == "__main__":
    pwd = os.getcwd()
    file_list = os.listdir(pwd+"/data/")
    del_file(pwd+"/result/")
    for file in file_list:
        fun_Filter_Data(file)
