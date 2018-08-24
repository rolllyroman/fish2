#coding:utf-8

from fish.player import Player
import random
import pickfish_pb2
import time
from twisted.internet.threads import deferToThread
#from threading import Thread
import functools

class Robot(Player):
    def __init__(self,manager,factory):
        super(Robot, self).__init__()

        self.isAI = 1
        self.manager = manager
        self.server = manager.server
        self.redis = manager.redis

        self.factory = factory
        self.ip = ""

        self.loadDB()
        self.dirX = 0
        self.dirY = 1

        self.fire_sts = 0

    def loadDB(self):
        uid = random.randint(1000000,1010001)
        while True:
            if uid not in [int(work_uid) for work_uid in self.manager.work_robot_uids]:
                break
            uid = random.randint(1000000,1010001)

        super(Robot, self).loadDB('users:%s'%uid)

    def join_game(self,game):
        self.game = game

        self.chair = game.getEmptyChair()
        self.resetGoldTime()
        game.players[self.chair] = self

        print '机器人%s加入游戏，房间号%s'%(self.uid,game.roomId)

        self.manager.work_robot_uids.append(self.uid)
        self.manager.work_robots.append(self)
        self.manager.uid_to_robot[str(self.uid)] = self

        # 加入游戏后操作

        d = deferToThread(self.operate)
        #c = functools.partial(self.callback)
        #d.addCallback(c)

    def callback(self):
        print '房间号%s机器人%s defer回调结束'%(self.game.roomId,self.uid)

    def leave(self):
        pass

    def operate(self):
        self.fire_sts = 1
        print '机器人%s开火准备'%self.uid
        x=random.randint(1,20)
        for i in range(x):
            print '机器人%s开火倒计时剩余%s秒'%(self.uid,x+1-i)
            time.sleep(1)
        print '机器人%s开火!'%self.uid
        while 1:
            self.onFire()
            time.sleep(0.34)
            if self.check_over():
                break
        self.fire_sts = 0

    def check_over(self):
        if self.redis.get('robot:%s:exit:command'%self.uid):
            print '检测到上级下达让机器人%s停止开火指令'%self.uid
            self.redis.set('robot:%s:exit:command'%self.uid,2)
            self.redis.expire('robot:%s:exit:command'%self.uid,1000)
            return True
        if not self.redis.lrange('services:game:%s'%self.server.ID,0,-1):
            print '游戏场%s关闭,机器人%s结束游戏'%(self.server.ID,self.uid)
            return True
        for player in self.game.players:
            if player is None:
                continue
            if not player.isAI:
                return False
        print '房间号%s无真实玩家，机器人%s停止开火'%(self.game.roomId,self.uid)
        return True


    def onFire(self):
        if self.game.bulletMgr.bulletIds:
            bulletId = max(self.game.bulletMgr.bulletIds.keys()) + 1
        else:
            bulletId = 1

        bulletIds = [bulletId]
        timestamp = int(time.time()*1000)
        dirX,dirY = self.get_dirs()
        self.game.onFire(self, timestamp, dirX, dirY, bulletIds, self.gunType)

    def get_dirs(self):
        if self.chair in [2,3]:
            self.dirY = -1
        if random.random() > 0.5:
            self.dirX += random.random()/random.randint(1,10)*2
        else:
            self.dirX -= random.random()/random.randint(1,10)*2

        if self.dirX > 1 or self.dirX < -1:
            self.dirX = random.random()

        return self.dirX,self.dirY

    def hitFish(self,bulletId,fishIds,timestamp):
        self.game.onHitFish(self, timestamp, bulletId, fishIds)




