'''
@author: Administrator
'''
from dao import CoinSqlite3 , BlockchainDao
from pip._vendor.distlib import database
from model.Block import Block


if __name__ == '__main__':
#    CoinSqlite3.CoinSqlite3()
#     Datacenter.conn_.init_table_blockTest()
    
    block = Block(111, 111, 111, 111, 111, 111, [], 0)
    