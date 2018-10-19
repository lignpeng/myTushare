
#coding=utf-8

import json
import os

# arr = [['1','2','3'],['4','5','6']]
# dic = {'aa':arr}
# str = json.dumps(dic)#输出str类型
# print(str)

# data_Path=os.path.abspath(os.path.join(os.path.dirname(__file__), "data.js"))

# if not os.path.exists(data_Path):
    # os.system(r'touch {}'.format(data_Path))
#需要注意的是，当你再次使用“w”方式在文件中写数据，所有原来的内容都会被删除。如果想保留原来的内容，可以使用“a”方式在文件中结尾附加数据：
# fileHandle = open(data_Path,'w')
# dd = '''\n\nwindow.getMockData = function (fullCode, type) {
#   fullCode = fullCode || 'SZ300545'
#   if (mockData[fullCode] && mockData[fullCode][type]) {
#     return mockData[fullCode][type]
#   }
#   return []
# }
# '''
# fileHandle.write ( 'var mockData ='+str+ dd)
# fileHandle.close()

def saveDataToJs(stocknumber,type,data):
    dic = {type:data}
    fileName = 'index/kshape/data/' + stocknumber + '-' + type + '.js'
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), fileName))
    print(file_path)
    if not os.path.exists(file_path):
        os.system(r'touch {}'.format(file_path))
    fileHandle = open(file_path,'w')
    dd = '''\n\nwindow.getMockData = function (fullCode, type) {
    if (mockData[type]) {
        return mockData[type]
    }
    return []
}
    '''
    str = json.dumps(dic)
    fileHandle.write ( 'var mockData ='+str+ dd)
    fileHandle.close()


# arr = [['1','2','3'],['4','5','6']]
# saveDataToJs('123010','D',arr)
