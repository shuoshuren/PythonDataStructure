#!/usr/bin/python
# coding:utf-8

class Deque(object):
	"""双端队列"""

	def __init__(self):
		self.__list = []

	def add_front(self,item):
		"""向队头添加一个item元素"""
		self.__list.insert(0,item)

	def add_rear(self,item):
		"""向队尾添加一个item元素"""
		self.__list.append(item)
	
	def pop_front(self):
		"""从队列头部删除一个元素"""
		return self.__list.pop(0)

	def pop_rear(self):
		"""从队列尾部删除一个元素"""
		return self.__list.pop()

	def is_empty(self):
		"""判断是否为空"""
		return self.size() == 0
		
	def size(self):
		"""返回队列元素个数"""
		return len(self.__list)

