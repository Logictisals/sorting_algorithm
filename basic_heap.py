#初始化小根堆
import heapq

min_heap,flag1=[],1
#初始化大根堆
max_heap,flag2=[],-1
#python中的heapq模块默认实现小根堆
#考虑将"元素取负" 后再入堆,这样就可以大小关系颠倒,从而实现大顶堆
#在本例中,flag=1 是对应小根堆,flag=-1 时对应大根堆

#元素入堆
heapq.heappush(max_heap,flag1*1)
heapq.heappush(max_heap,flag1*3)
heapq.heappush(max_heap,flag1*2)
heapq.heappush(max_heap,flag1*5)
heapq.heappush(max_heap,flag1*4)
peek:int=flag1*max_heap[0]#获取堆顶的元素
#堆顶元素出堆
#出堆元素会形成一个从大到小的序列
val=flag1*heapq.heappop(max_heap)
val=flag1*heapq.heappop(max_heap)
val=flag1*heapq.heappop(max_heap)
val=flag1*heapq.heappop(max_heap)
val=flag1*heapq.heappop(max_heap)
#获取堆大小
#判断是否为空
is_empty:bool=not max_heap
#输入列表并且舰堆
min_heap:list[int]=[1,3,2,5,4]
heapq.heapify(min_heap)
print(heapq)

import heapq

# 创建一个空堆
heap = []

# 插入元素到堆中
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 10)
heapq.heappush(heap, 3)

print("最小堆：", heap)

# 弹出堆中的最小元素
min_element = heapq.heappop(heap)
print("弹出的最小元素：", min_element)

print("剩余的堆：", heap)

import heapq

# 创建一个空堆
heap = []

# 插入元素的相反数到堆中
heapq.heappush(heap, -5)
heapq.heappush(heap, -2)
heapq.heappush(heap, -10)
heapq.heappush(heap, -3)

print("大根堆：", [-x for x in heap])

# 弹出堆中的最大元素
max_element = -heapq.heappop(heap)
print("弹出的最大元素：", max_element)

print("剩余的堆：", [-x for x in heap])
