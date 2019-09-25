#!/usr/bin/env python
# -*- coding:utf-8 -*-

import paramiko


class LinuxTool:

    def __init__(self, ip, username, password):
        self.ip = ip
        self.username = username
        self.password = password

    def run(self, command):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.ip, 22, self.username, self.password)
            stdin, stdout, stderr = ssh.exec_command(command)
            res = stdout.read().decode('utf-8')
            print('结果为：', res)
        except Exception as e:
            print("ERROR{}".format(format(e)))
        finally:
            ssh.close()


if __name__ == '__main__':
    ip = '129.28.162.62'
    username = 'root'
    password = 'wfq_950612'
    linuxtool = LinuxTool(ip, username, password)
    command = 'cd /opt && ls -l'
    linuxtool.run(command)
