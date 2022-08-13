
from turtle import color
import matplotlib.pyplot as plt

""" x = [1, 2, 3, 4]
y = [2, 4, 6, 8]



plt.plot(x, y, color="r")

plt.axis([0, 5,0,10])


plt.show()
 """
 
 
#创建画板1
fig = plt.figure(1)  # 如果不传入参数默认画板1

plt.f
#第2步创建画纸，并选择画纸1
ax1 = plt.subplot(2, 1, 1)
#在画纸1上绘图
plt.plot([1, 2, 3])
#选择画纸2
ax2 = plt.subplot(2, 1, 2)
#在画纸2上绘图
plt.plot([4, 5, 6])
#显示图像
plt.show()
