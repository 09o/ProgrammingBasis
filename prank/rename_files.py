'''
这是一个程序，可以读取一系列文件，并按照一定规则重命名每个文件。
'''

import os

def rename_files():
    # (1) get file names from a folder
    file_list = os.listdir(r"C:\Users\igswa\Udacity\python\prank")
    '''
     对于Windows系统中的路径，前面需要加上字母"r"(r=raw pack[原包装])。
     其功能是告诉python程序接受这个字符串本身，不要用其他方式解读它。
    '''
    # print(file_list)
    
    # save_path = os.getcwd()
    # print("Current Working Directory is:", save_path)
    # CWD means Current Working Directory(当前工作目录)
    
    # 当源代码不与文件在同一路径当中时，此时工作目录会处于源代码目录
    # 为了修改后续文件，需要将当前工作目录改为文件所在路径当中去

    # os.chdir(r"C:\Users\igswa\Udacity\python\prank")
    # os.chdir(path) 可以改变工作目录


    # (2) for each file, rename filename
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(str.maketrans('','','0123456789')))
        os.rename(file_name, file_name.translate(str.maketrans('','','0123456789')))
"""
        str.translate(s, table[, deletechars])
        遵循这样的使用技巧：
        import string
        string.translate(file_name,None,'0123456789')
        其用法等同于（将file_name放在前面，替换string模块）：
        file_name.translate(None, '0123456789')
"""

rename_files()