import re
import pyautogui
from time import sleep

# 修改地址
class http:
    def __init__(self):
        self.ct4 = ['newsId=873151453']
        self.ct5 = ['newsId=674133349']
        self.ct6 = ['newsId=553208387']
        self.xt4 = ['newsId=880141277']
        self.xt5 = ['newsId=737665584']
        self.xt6 = ['newsId=728445290']
        self.newhttplist = []
        self.http_1 = 'https://ics.autohome.com.cn/price/promotion/edit?temp=1&newsId=873151453'
    def res(self,i,s):
        http1 = re.sub('newsId=(\w*)',i,s)
        self.newhttplist.append(http1)
    def newhttp(self,s):
        for i in s:
            self.res(i,self.http_1)

# 点击操作
class click:
    def __init__(self):
        # 间隔时间(根据网络情况调整)
        self.Intervals = 5
        # 发布次数(初始值)
        self.set = 0
        # 地址栏位置
        self.Bar = (963,46)
        # 发布位置
        self.Confirm = (488,960)
        # 确定位置
        self.Confirm2 = (1100,575)
    def click(self,i):
        while self.set <= i:
            # 点击地址栏
            pyautogui.click(self.Bar)
            sleep(1)
            # 输入地址
            pyautogui.write(qczj_http.newhttplist[self.set])
            print(qczj_http.newhttplist[self.set])
            sleep(0.5)
            # 回车
            pyautogui.press('enter')
            sleep(self.Intervals)
            # 点击页面
            pyautogui.click(1355,295)
            sleep(1)
            # 模拟滚轮
            pyautogui.press('pgdn',presses=5)
            sleep(1)
            # 点击发布
            pyautogui.click(self.Confirm)
            sleep(1)
            pyautogui.click(self.Confirm2)
            sleep(1)
            self.set += 1

# 实例化
qczj_http = http()
qczj_click = click()

# 主函数
def run():
    choose = pyautogui.confirm(text='汽车之家自动发文程序即将运行,请确认后台是否登录,地址栏输入法是否为英文.如需使用推荐名额请等程序运行结束后手动修改.', title='汽车之家自动发文', buttons=['OK', 'Cancel'])
    if choose == 'OK':
        qczj_http.newhttp(qczj_http.ct4)
        qczj_http.newhttp(qczj_http.ct5)
        qczj_http.newhttp(qczj_http.ct6)
        qczj_http.newhttp(qczj_http.xt4)
        qczj_http.newhttp(qczj_http.xt5)
        qczj_http.newhttp(qczj_http.xt6)
        qczj_click.click(5)
        # print(qczj_http.newhttplist)
run()
