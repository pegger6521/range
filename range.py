# range範圍
# python內建的功能: 清單產生器
# 會自動從0開始, 結尾值不算
# range通常都是跟for loop搭配的

#range(5) # [0, 1, 2, 3, 4]
#range(3) # [0, 1, 2]
#for i in range(5):
	#print(i)

# for i in range通常是為了讓它的內容重複執行某個"固定次數"
# 可以把i在for loop內容中印出來, 就知道執行到第幾回

import random
for i in range(20):
	r = random.randint(1, 1000)
	print('這是第', i + 1, '次產生隨機數: ', r)
