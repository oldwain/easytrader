# import easytrader as et
# user = et.use('zs')
# user.prepare(r'd:\gitlocal\mystrategy\config\zs.json')
# print(user.balance)


import easytrader as et
user = et.use('yh')
user.prepare(r'd:\gitlocal\mystrategy\config\yh.json')
a = user.get_ipo_limit('002830')
print(a   )
