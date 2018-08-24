#coding:utf-8
import sys
sys.path.append('..')

import redis_instance
from common_db_define import PUBLIC_DB
#from fish.player import Player
from robot import Robot
import random
from pb_utils import *
import pickfish_pb2
import functools
from twisted.internet.threads import deferToThread
import time
from datetime import datetime

class Robot_manager(object):

    def __init__(self,server):
        self.server = server
        self.redis = redis_instance.getInst(PUBLIC_DB)

        self.work_robot_uids = []
        self.free_robots = []
        self.work_robots = []
        self.uid_to_robot = {}

        self.taskmaster()

    def manage(self,game,player):
        return
        # 暂时只在弹头场派遣机器人
        if self.server.field_type != '1':
            return

        # 获取这个游戏房间的人数
        player_num = int(self.redis.hget('fish:%s:house:%s:info'%(self.server.ID,game.roomId),'player_num') or 0)
        print '当前房间%s,存在人员：%s'%(game.roomId,game.players)
        if player_num < 3:
            print '开始派遣机器人'
            # 派遣机器人 加入房间
            self.dispatch_robot(game,player.factory)
        else:
            print '当前房间人数%s,放弃派遣机器人'%player_num

    def dispatch_robot(self,game,factory):
        if self.free_robots:
            pass
        robot = Robot(self,factory)

        robot.join_game(game)

        # 告知房间内其他玩家
        joinResponse = pickfish_pb2.S_C_JoinRoom()
        pbPlayerInfo(joinResponse.info, game, robot.chair)
        game.sendExclude((robot,), joinResponse)

        self.redis.hincrby('fish:%s:house:%s:info'%(self.server.ID,game.roomId),'player_num',1)
        players = [ str(player.uid) for player in game.players if player]
        players = ','.join(players)
        now = str(datetime.now())[:19]
        self.redis.hmset('fish:%s:house:%s:info'%(self.server.ID,game.roomId),{'players':players,str(robot.uid):now})

        self.work_robots.append(robot)

    def taskmaster(self):
        d = deferToThread(self.taskmaster_work)

    def control_exit(self):
        # 退出条件
        cur_minute = int(str(datetime.now())[14:16])
        for robot in self.work_robots:
            rec = self.redis.get('robot:%s:exit:command'%robot.uid)
            # 发送停止开火指令
            if cur_minute%2 == 0 and not rec:
                print '当前时间%s,发送指令,机器人退出房间准备，发送机器人停止开火指令'
                self.redis.set('robot:%s:exit:command' % robot.uid, 1)
                self.redis.expire('robot:%s:exit:command' % robot.uid, 1000)
            elif rec == '2':
                print '机器人%s执行指令，退出游戏'%robot.uid
                robot.exit_game()
                self.redis.delete('robot:%s:exit:command' % robot.uid)

    def exit(self):
        pass

    def check_fire(self):
        print '开始检查机器人'
        for game in self.server.globalCtrl.gameList:
            idle_robots = []
            real_player = None
            for player in game.players:
                if player is None:
                    continue
                if player.isAI and not player.fire_sts:
                    idle_robots.append(player)
                if not player.isAI:
                    real_player = player
            # 存在真实玩家存在且机器人不开火的房间
            if idle_robots and real_player:
                print '房间%s出现机器人偷懒情况，执行操作'%game.roomId
                self.taskmaster_bark(real_player,idle_robots)
        print '检查完毕'

    def taskmaster_work(self):
        while 1:
            if not self.redis.lrange('services:game:%s'%self.server.ID,0,-1):
                print '服务器%s关闭，停止检查'%self.server.ID
                break
            time.sleep(30)
            # 检查一遍在房间内的机器人运作情况
            self.check_fire()
            # 控制机器人退出房间
            #self.control_exit()


    def taskmaster_bark(self,player,robots):
        for robot in robots:
            if self.redis.get('robot:%s:exit:command'%robot.uid):
                print '机器人%s退出准备中，跳过唤醒'
                continue
            print '开始唤醒房间%s内机器人%s'%(robot.game.roomId,robot.uid)
            deferToThread(robot.operate)








