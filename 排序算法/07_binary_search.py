#!/usr/bin/python
# coding:utf-8



def binary_search(alist,item):
	'''二分查找,递归'''
	print("递归")
	n = len(alist)
	if n >0 :
		mid = n // 2 
		if alist[mid] == item:
			return True
		elif item < alist[mid]:
			return binary_search(alist[:mid],item)
		else:
			return binary_search(alist[mid+1:],item)
	else:
		return False

def binary_search(alist,item):
	"""二分查找，非递归"""
	print("非递归")
	n = len(alist)
	first = 0
	last = n-1
	while first <= last:
		mid = (first+last) // 2
		if alist[mid] == item:
			return True
		elif item < alist[mid]:
			last = mid-1
		else:
			first = mid+1
	return False
	
		


if __name__ == '__main__':
	
	alist = [17, 20, 26, 26, 31, 44, 54, 55, 77, 93]
	print(binary_search(alist,20))
	print(binary_search(alist,100))