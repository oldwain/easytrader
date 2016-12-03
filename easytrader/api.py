# coding=utf-8
import logging

from .gftrader import GFTrader
from .httrader import HTTrader
from .joinquant_follower import JoinQuantFollower
from .log import log
from .xq_follower import XueQiuFollower
from .xqtrader import XueQiuTrader
from .yhtrader import YHTrader
from .yjbtrader import YJBTrader
from .zstrader import ZSTrader
from .tdxtrader import TDXTrader

def use(broker, debug=True, **kwargs):
    """用于生成特定的券商对象
    :param broker:券商名支持 ['ht', 'HT', '华泰’] ['yjb', 'YJB', ’佣金宝'] ['yh', 'YH', '银河'] ['gf', 'GF', '广发']
    :param debug: 控制 debug 日志的显示, 默认为 True
    :param initial_assets: [雪球参数] 控制雪球初始资金，默认为一百万
    :param remove_zero: [ht参数]，是否移除 08 账户开头的 0, 默认 True
    :return the class of trader

    Usage::

        >>> import easytrader
        >>> user = easytrader.use('ht')
        >>> user.prepare('ht.json')
    """
    if not debug:
        log.setLevel(logging.INFO)
    if broker.lower() in ['ht', '华泰']:
        return HTTrader(**kwargs)
    elif broker.lower() in ['yjb', '佣金宝']:
        return YJBTrader()
    elif broker.lower() in ['yh', '银河']:
        return YHTrader()
    elif broker.lower() in ['xq', '雪球']:
        return XueQiuTrader()
    elif broker.lower() in ['gf', '广发']:
        return GFTrader()
    elif broker.lower() in ['zs', '招商']:
        return ZSTrader()
    elif broker.lower() in ['yh_client', '银河客户端']:
        from .yh_clienttrader import YHClientTrader
        return YHClientTrader()
    elif broker.lower() in ['tdxxd', 'xdtdx', '信达tdx']:
        return TDXTrader('tdxxd')
    elif broker.lower() in ['yjbtdx', 'tdxyjb', '佣金宝tdx']:
        return TDXTrader('tdxyjb')


def follower(platform, **kwargs):
    """用于生成特定的券商对象
    :param platform:平台支持 ['jq', 'joinquant', '聚宽’]
    :param initial_assets: [雪球参数] 控制雪球初始资金，默认为一万, 总资金由 initial_assets * 组合当前净值 得出
    :param total_assets: [雪球参数] 控制雪球总资金，无默认值, 若设置则覆盖 initial_assets
    :return the class of follower

    Usage::

        >>> import easytrader
        >>> user = easytrader.use('xq')
        >>> user.prepare('xq.json')
        >>> jq = easytrader.follower('jq')
        >>> jq.login(user='username', password='password')
        >>> jq.follow(users=user, strategies=['strategies_link'])
    """
    if platform.lower() in ['jq', 'joinquant', '聚宽']:
        return JoinQuantFollower()
    if platform.lower() in ['xq', 'xueqiu', '雪球']:
        return XueQiuFollower(**kwargs)
