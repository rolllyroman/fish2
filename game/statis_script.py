#coding:utf-8
import redis
import time

redisdb = redis.ConnectionPool(host="127.0.0.1", port=6379, db=1, password='Fkkg65NbRwQOnq01OGMPy5ZREsNUeURm')
r = redis.Redis(connection_pool=redisdb)

def caculate():
    produce_coin = int(r.get('produce:coin:sum') or 0)
    produce_warhead = int(r.get('produce:warhead:sum') or 0)

    earnings_coin = int(r.get('earnings:coin:sum') or 0)
    earnings_warhead = int(r.get('earnings:warhead:sum') or 0)

    coin_rate = round(float(produce_coin)/earnings_coin,3)
    warhead_rate = round(float(produce_warhead)/earnings_warhead,3)

    r.set('fish:coin:rate',coin_rate)
    r.set('fish:warhead:rate',warhead_rate)

def main():
    while 1:
        caculate()
        time.sleep(10)

if __name__ == '__main__':
    main()


