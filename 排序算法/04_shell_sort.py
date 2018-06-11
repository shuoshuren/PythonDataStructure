#!/usr/bin/python
# coding:utf-8




def shell_sort(alist):
	'''希尔排序'''
	n = len(alist)
	gap = n // 2

	while gap > 0:
		# 希尔插入算法和普通打插入算法的区别是gap的步长
		for i in range(gap,n):
			# j代表内层循环打起始值
			# 执行从右边打无序序列中取出第一元素,比较交换元素
			while i > 0:
				if alist[i] < alist[i-gap]:
					alist[i], alist[i-gap] = alist[i-gap], alist[i]
					i = i - gap
				else:
					break
		# print(alist)
		# 缩短gap步长
		gap //= 2



if __name__ == '__main__':
	
	alist = [54,26,93,17,77,31,44,55,20]
	shell_sort(alist)
	print(alist)