'''

@author: Administrator
'''
import sqlite3
import Constants


class CoinSqlite3(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.db = sqlite3.connect(Constants.DB_PATH)
        self._init_tables()

    def _exec_sql(self, sql, *args):
        c = self.db.cursor()
        c.execute(sql, args)
        return c
    
    def exec_sql(self, sql, *args):
        c = self.db.cursor()
        c.execute(sql, args)
        self.commit()
    
    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()
        
    def _init_tables(self):
        self._init_table_block()
        self._init_table_tx()
        self._init_table_tx_in()
        self._init_table_tx_out()
        self._init_table_net()
        self._init_table_addr()
        self._init_table_secretkey()
        self._init_other_tables()
    
        
    def _init_table_secretkey(self):
        SQL = """create table if not exists SecretKeyInfo (
                id integer primary key,
                publicKey text not null,
                privateKey text,
                pubicAddress text not null,
                cert text
                );"""
        c = self._exec_sql(SQL)
        self.db.commit()   
                
    
    def _init_table_block(self):
        SQL = """create table if not exists BlockInfo (
                id integer primary key,
                hash text not null,
                version integer not null,
                previous_block_hash text not null,
                merkle_root text not null,
                timestamp integer not null,
                difficulty integer not null,
                nonce integer not null,
                state integer not null,
                next_block_hash text,
                height integer
                );"""
        c = self._exec_sql(SQL)
        self.db.commit()   
                
    def _init_table_tx(self):
        SQL = """create table if not exists TransactionInfo (
                id integer primary key,
                hash text not null,
                version integer not null,
                lock_time integer not null,
                parentBlockId text,
                unspents text,
                state integer not null,                
                type integer not null,
                
                original_hash text,
                target_amount integer,
                pubkey integer,
                end_time integer,
                pre_hash text,
                lack_amount integer,
                cert text
                );"""
        c = self._exec_sql(SQL)
        self.db.commit()   
        
    def _init_table_tx_in(self):
        SQL = """create table if not exists TransactionInfoIn (
                id integer primary key,
                previous_hash text not null,
                previous_index integer not null,
                script text not null,
                sequence integer not null,
                parentBlockId text,
                parentTxId text not null,
                state integer not null,
                `index` integer not null,
                isMyTx integer
                );"""
        c = self._exec_sql(SQL)
        self.db.commit()   
    def _init_table_tx_out(self):
        SQL = """create table if not exists TransactionInfoOut (
                id integer primary key,
                coin_value integer not null,
                script text not null,
                parentBlockId text,
                parentTxId text not null,
                state integer not null,
                `index` integer not null,
                pubicAddress integer,
                isToMe integer,
                usedState integer,                
                end_time integer,
                isMyTx integer
                );"""
        c = self._exec_sql(SQL)
        self.db.commit()
    def _init_table_net(self):
#         SQL = """create table if not exists NetInfo (
#                 id integer primary key,
#                 slug text not null unique,
#                 as_text text not null
#                 );"""
#         c = self._exec_sql(SQL)
#         self.db.commit()
        pass
    def _init_table_addr(self): 
        SQL = """create table if not exists AddressInfo (
                id integer primary key,
                ip text not null,
                port text not null
                );"""
        c = self._exec_sql(SQL)
        self.db.commit()  
    def _init_other_tables(self):
        pass 
