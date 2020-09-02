"""
    1. 把我们需要的数据请求函数都写成api
"""

import tushare as ts
import pandas as pd

class BatchApi(object):

    def __init__(self):
        """
            初始化Tushare
        """
        self.ts = ts
        self.ts.set_token('7e93ee7b3ee24dcb47197b655836658b754895d282b033de63a9535e')
        pass


if __name__ == '__main__':
    ts.set_token('7e93ee7b3ee24dcb47197b655836658b754895d282b033de63a9535e')
    pro = ts.pro_api()
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    data2 = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    print(data.head)
    print(data2.head)