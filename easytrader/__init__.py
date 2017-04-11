# coding: utf-8
from .api import *
try:
	from .httrader import HTTrader
except:
	pass
from .webtrader import WebTrader
try:
	from .yhtrader import YHTrader
except:
	pass
	
try:
	from .yjbtrader import YJBTrader
except:
	pass
try:
	from .gftrader import GFTrader
except:
	pass
try:
	from .joinquant_follower import JoinQuantFollower
except:
	pass
try:
	from .zstrader import ZSTrader
except:
	pass
try:
	from .tdxdll import TDXDLL
except:
	pass
try:
	from .tdxtrader import TDXTrader
except:
	pass
try:
    from .remotetrader import RemoteTrader
except:
    pass

__version__ = '0.9.9'
__author__ = 'shidenggui'
