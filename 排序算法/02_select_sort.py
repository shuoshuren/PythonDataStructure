#!/usr/bin/python

# coding:utf-8


def select_sort(alist):
	'''选择排序'''
	n = len(alist)
	for j in range(0,n-1):
		min_index = j
		for i in range(j+1,n):
			if alist[i] < alist[min_index]:
				min_index = i
		alist[j],alist[min_index] = alist[min_index],alist[j]
		print(alist)


if __name__ == '__main__':
	
	alist = [54,26,93,17,77,31,44,55,20]
	select_sort(alist)
	print(alist)