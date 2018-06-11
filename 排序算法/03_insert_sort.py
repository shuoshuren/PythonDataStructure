#!/usr/bin/python

# coding:utf-8


def insert_sort(alist):
	'''插入排序'''
	n = len(alist)
	for i in range(1,n):
		# i代表内层循环打起始值
		# 执行从右边打无序序列中取出第一元素
		while i > 0:
			if alist[i] < alist[i-1]:
				alist[i], alist[i-1] = alist[i-1], alist[i]
				i -= 1
			else:
				break
		print(alist)



if __name__ == '__main__':
	
	alist = [54,26,93,17,77,31,44,55,20]
	insert_sort(alist)
	print(alist)