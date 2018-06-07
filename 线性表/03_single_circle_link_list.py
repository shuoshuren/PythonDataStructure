#!/usr/bin/python
# coding:utf-8


class Node(object):
	"""节点"""

	def __init__(self,elem):
		self.elem = elem
		self.next = None



class SingleCircleLinkList(object):
	'''单链循环表'''

	def __init__(self,node = None):
		self.__head = node
		if node:
			node.next = node


	def is_empty(self):
		"""链表是否为空"""
		return self.__head == None

	def length(self):
		"""链表长度"""
		if self.is_empty():
			return 0
		# cur游标，用来移动遍历节点
		cur = self.__head
		# count 用来计数
		count = 1
		while cur.next != self.__head:
			count +=1
			cur = cur.next

		return count

	def travel(self):
		"""遍历整个链表"""
		if self.is_empty():
			return
		cur = self.__head
		while cur.next != self.__head:
			print(cur.elem,end=" ")
			cur = cur.next
		# 退出循环，cur指向尾节点，但尾节点打元素未打印
		print(cur.elem)
		

	def add(self,item):
		"""链表头部添加元素"""
		node = Node(item)
		if self.is_empty():
			self.__head = node
			node.next = node
		else:
			cur = self.__head
			while cur.next != self.__head:
				cur = cur.next
			# 退出节点，cur指向尾节点
			cur.next = node
			node.next = self.__head
			self.__head = node



	def append(self,item):
		'''链表尾部添加元素'''
		node = Node(item)
		if self.is_empty():
			self.__head = node
			node.next = node
		else:
			cur = self.__head
			while cur.next != self.__head:
				cur = cur.next
			cur.next = node
			node.next = self.__head
		

	def insert(self,pos,item):
		"""
		指定位置添加元素
		:param pos 从0开始
		"""
		if pos <= 0:
			self.add(item)
		elif pos > (self.length()-1):
			self.append(item)
		else:
			node = Node(item)
			count = 0
			pre = self.__head
			while count < (pos-1):
				count+=1
				pre = pre.next
				# 当循环退出后，pre指向pos-1的位置
			node.next = pre.next
			pre.next = node


	def remove(self,item):
		"""删除节点"""
		if self.is_empty():
			return
		cur = self.__head
		pre = None
		while cur.next != self.__head:
			if cur.elem == item:
				# 先判断此节点是否是头节点
				if cur == self.__head:
					# 头节点
					# 找尾节点
					rear = self.__head
					while rear.next != self.__head:
						rear = rear.next
						
					self.__head = cur.next
					rear.next = self.__head
					# self.__head = cur.next
				else:
					# 中间节点
					pre.next = cur.next
					cur.next = None
				return
			else:
				pre = cur
				cur = cur.next
		# 退出循环，cur指向尾节点
		if cur.elem == item:
			if cur == self.__head:
				#链表只有一个节点
				self.__head = None
			else:
				pre.next = cur.next
				cur.next = None


	def search(self,item):
		"""查找节点是否存在"""
		if self.is_empty():
			return False
		cur = self.__head
		while cur != self.__head:
			if cur.elem == item:
				return True
			else:
				cur = cur.next
		# 退出循环，cur指向尾节点
		return cur.elem == item




if __name__ == '__main__':
	
	ll = SingleCircleLinkList()
	print(ll.is_empty())
	print(ll.length())

	ll.append(1)
	print(ll.is_empty())
	print(ll.length())

	ll.append(2)
	ll.add(8)
	ll.append(3)
	ll.append(4)
	ll.append(5)
	ll.append(6)
	ll.travel()
	ll.insert(-1,9) 
	ll.travel() # 9 8 1 2 3 4 5 6
	ll.insert(2,100) 
	ll.travel() # 9 8 1 100 2 3 4 5 6
	ll.insert(10,200)
	ll.travel() # 9 8 1 100 2 3 4 5 6 200
	ll.remove(200)
	ll.travel()
	ll.remove(100)
	ll.travel()
	ll.remove(9)
	ll.travel()
	print(ll.search(6))
	print(ll.search(200))
