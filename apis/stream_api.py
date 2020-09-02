"""
    1. 登录到Tushare
    2. 开始监听数据推送
        ……数据推送有不同的API函数
    3. 保存到

"""

import tushare as ts

class RealTimeQuote:
    def __init__(self):
        self.token = '7e93ee7b3ee24dcb47197b655836658b754895d282b033de63a9535e'
        self.ts = ts
        self.ts.set_token(self.token)
