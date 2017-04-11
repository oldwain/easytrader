# import easytrader as et
# user = et.use('zs')
# user.prepare(r'd:\gitlocal\mystrategy\config\zs.json')
# print(user.balance)


import easytrader as et
user = et.use('remote')
user.prepare(r'd:\gitlocal\mystrategy\config\xqremote.json')
#a = user.get_ipo_limit('002830')
print(user.balance())
