#!/usr/bin/python
# coding:utf-8



def quick_sort(alist,first,last):
	'''快速排序'''

	if first >= last:
		return

	mid_value = alist[first]
	low = first
	high = last

	while low < high:
		# high游标左移
		while low < high and alist[high] >= mid_value:
			high -= 1
		alist[low] = alist[high]

		# low游标右移
		while low < high and alist[low] < mid_value:
			low += 1 
		alist[high] = alist[low]
	#从循环退出时，low==high
	alist[low] = mid_value

	# 对low左边的列表进行快速排序
	quick_sort(alist,first,low-1)
	# 对low右边的列表进行快速排序
	quick_sort(alist,low+1,last)





if __name__ == '__main__':
	
	alist = [54,26,93,17,77,31,44,55,20]
	quick_sort(alist,0,len(alist)-1)
	print(alist)