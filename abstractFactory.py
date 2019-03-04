# coding:utf-8
#创建支付基类与子类（支付宝与微信支付）
class Payment(object):
    def __init__(self):
        pass
    def give_money(self):
        pass
    def give_ok(self):
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

#创建商店基类与子类（衣服商店与零食商店）
class store(object):
    def __init__(self):
        pass
    def get_money(self):
        pass

class clothesstore(store):
    def __init__(self):
        print "正在购买衣服，仅支持支付宝支付"
    def get_money(self):
        print "衣服费用已支付完成"

class  snackstore(store):
    def __init__(self):
        print "正在购买零食，仅支持微信支付"
    def get_money(self):
        print "零食费用已支付完成"

#抽象工厂
class IFactory():
    def Createpay(self):
        pass
    def Createstore(self):
        pass

#创建服装商店支付工厂
class clothesFactory(IFactory):
    def Createpay(self):
        return alipay()
    def Createstore(self):
        return clothesstore()
#创建零食商店支付工厂
class snackFactory(IFactory):
    def Createpay(self):
        return wxpay()
    def Createstore(self):
        return snackstore()

#党用户发生一个购买衣服支付时，则可以
if __name__ == "__main__":
    pay= clothesFactory()#创建支付宝支付
    pay.Createpay()
    pay.Createstore()
