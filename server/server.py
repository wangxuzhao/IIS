#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socketserver
import json
import os

class MyServer(socketserver.BaseRequestHandler):
	def handle(self):
		print(self.request,self.client_address,self.server)
		conn = self.request
		raw_data = conn.recv(1024).decode()
		data = json.loads(raw_data)
		print(data,'receive')
		if data['type'] == 'get':
			os.system('./tools/ini2json config.ini')
			with open('config.json','r') as f:
				respons = json.loads(f.read())
				respons = json.dumps(respons)
		elif data['type'] == 'control':
			pass

		conn.sendall(respons.encode())
		print(respons,'sended')

if __name__ == '__main__':
	server = socketserver.ThreadingTCPServer(('localhost',6666),MyServer)
	server.serve_forever()
