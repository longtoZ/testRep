from matplotlib import pyplot as plt


plt.style.use('dark_background')
x = [1,2,3,4,5,6,7,8,9,10]
y = [2,5,7,9,11,15,19,22,36,40]

plt.bar(x,y, label='Line 1')

y2 = [7,8,9,10,11,12,13,14,15,50]

plt.bar(x,y2, label="Line 2")

plt.title("Test plot")
plt.xlabel('Number')
plt.ylabel('Height')

plt.legend()

#plt.tight_layout()
#plt.grid(True)

plt.show()