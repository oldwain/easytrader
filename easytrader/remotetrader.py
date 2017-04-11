# -*- coding: utf-8 -*-

import requests
import json
import os
from .log import log

from . import helpers


class RemoteTrader:
    """
    交易客户端
    """
    config_path = os.path.dirname(__file__) + '/config/remote.json'

    def __init__(self, broker=None):
        self.account_config = None
        self.ip = None
        self.port = None
        self.url = None
        self.token = None
        self.name = None

    def prepare(self, need_data):
        """登录的统一接口
        :param need_data 登录所需数据
        """
        self.read_config(need_data)
        # self.autologin()
        self.name = self.account_config['name']
        self.ip = self.account_config['ip']
        self.port = self.account_config['port']
        self.url = "http://{}:{}/".format(self.ip, self.port)
        self.token = self.account_config['token'] + ":" + self.account_config['account'] + ":" + self.account_config['password']
        if 'portfolio_code' in self.account_config.keys():
            self.token = self.token + ":" + self.account_config['portfolio_code']
        if 'tradeaccount' in self.account_config.keys():
            self.token = self.token + ":" + self.account_config['tradeaccount']

        return self._request('prepare')

    def _request(self, fuc, params={}):
        params['token'] = self.token
        response = requests.post(self.url + fuc, data=params)
        if response.status_code != 200:
            print(response.text)
            return {"error": response.text}
        #print(response.text)
        try:
            return json.loads(response.text)
        except json.decoder.JSONDecodeError:
            print(response.text)
            return {"error": response.text}
    @property
    def balance(self):
        return self._request('balance')

    @property
    def entrust(self):
        return self._request('entrust')

    @property
    def position(self):
        return self._request('position')

    def buy(self, stock_code, price=0, amount=0, volume=0, entrust_prop=0):
    #def buy(self, stock_code, price, volume):
        return self._request('buy', {
            'stock_code': stock_code,
            'price': price,
            'amount':amount,
            'volume': volume,
            'entrust_prop':entrust_prop
        })

    def sell(self, stock_code, price=0, amount=0, volume=0, entrust_prop=0):
    #def sell(self, stock_code, price, volume):
        print ('sell '+ stock_code)
        return self._request('sell', {
            'stock_code': stock_code,
            'price': price,
            'amount':amount,
            'volume': volume,
            'entrust_prop':entrust_prop
        })

    def cancel_entrust(self, entrust_no):
        return self._request('cancel_entrust', {
            'entrust_no': entrust_no
        })

    def read_config(self, path):
        try:
            self.account_config = helpers.file2dict(path)
        except ValueError:
            log.error('配置文件格式有误，请勿使用记事本编辑，推荐使用 notepad++ 或者 sublime text')
        for v in self.account_config:
            if type(v) is int:
                log.warn('配置文件的值最好使用双引号包裹，使用字符串类型，否则可能导致不可知的问题')


