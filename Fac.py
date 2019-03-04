#coding:utf-8
class Payment(object):
    def __init__(self):
        pass
    def give_money(self):
        pass
    def give_ok(self):
        pass

class IFactory(Payment):
    def Createpayment(self):
        pass

class alipay(Payment):
    def __init__(self):
        print('支付宝ing')
    def give_money(self):
        print('支付宝支付中')
        print('...')
    def give_ok(self):
        print('支付宝支付成功')


class wxpay(Payment):
    def __init__(self):
        print('微信ing')
    def give_money(self):
        print('微信支付中')
        print('...')
    def give_ok(self):
        print('微信支付成功')
#创建支付宝支付工厂
class alipayFactory(IFactory):
    def Createpayment(self):
        return alipay()
#创建微信支付支付工厂
class wxpayFactory(IFactory):
    def Createpayment(self):
        return wxpay()

if __name__ == "__main__":
    ali= alipayFactory()#创建支付宝支付
    wx = wxpayFactory()#创建微信支付
    #bank=bankFactory

#此时，如果还想创建银行支付，则只需要创建一个银行支付子类与银行支付工厂类的方法
class bankpay(Payment):#创建银行支付子类
    def __init__(self):
        print('银行ing')

    def give_money(self):
        print('银行支付中')
        print('...')

    def give_ok(self):
        print('银行支付成功')

class bankpayFactory(IFactory):#创建银行支付工厂类
    def Createpayment(self):
        return bankpay()


