#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class Dumper:
	def __init__(self, filename, delim=' '):
		self.filename=filename
		self.delim=delim
		self.data = []
	def push(self, data):
		self.data.append(data)
	def dump(self):
		f = open(self.filename, "w") # 
		for dat in self.data:
			for da in dat:
				isFirst = True
				for d in da:
					if isFirst:
						f.write(str(d))
						isFirst = False
					else:
						f.write(self.delim)
						f.write(str(d))
				f.write('\n')
		f.close()
		

def load(filename, comment='#', delim='\t \n', encoding='utf-8', newline='\n'):
	dds = re.compile('['+delim+']')

	f = open(filename, encoding=encoding, newline=newline)
	nc = len(comment)
	res = [dds.split(line) for line in f if line[:nc] != comment]
#	res = []
#	for line in f:
#		if line[:nc] == comment:
#			continue
#		neko = dds.split(line)
##		neko = dds.split(line[:-1])
#		print(neko)
#		res.append(neko)
#	f.close()
	return res

def dump_old(data, filename, delim=' '):
	f = open(filename, "w") # 
#	f = open(filename, "w", encoding="utf-8") # Python 3 (?)
#	f = open(filename, 'wb')
	for dat in data:
#		f.write(dat[0])
		f.write(str(dat[0]))
#		print dat
		dat = list(dat)
#		for da in list(dat)[1:]:
		for da in dat[1:]:
			f.write(delim)
			f.write(str(da))
		f.write('\n')
	f.close()

def dump(data, filename, delim=' '):
	f = open(filename, "w") # 
	for dat in data:
		isFirst = True
		for da in dat:
			if isFirst:
				f.write(str(da))
				isFirst = False
			else:
				f.write(delim)
				f.write(str(da))
		f.write('\n')
	f.close()




class Trimmer:
	def trim(self, ddsv_data):
		return ddsv_data

class Trimmer_Space(Trimmer):
	def trim(self, ddsv_data):
		res = []
		for row in ddsv_data:
			res_row = []
			for column in row:
				if column == '':
					pass
				else:
					res_row.append(column)
			res.append(res_row)
		return res

class Trimmer_Space_Row(Trimmer):
	def trim(self, ddsv_data):
		res = []
		for row in ddsv_data:
			res_row = []
			for column in row:
				if column != '':
					res_row.append(column)
			if res_row != []:
				res.append(res_row)
		return res

trimmer1 = Trimmer_Space()
trimmer2 = Trimmer_Space_Row()