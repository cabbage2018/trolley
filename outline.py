
import numpy as np
import matplotlib.pyplot as plt
coordinates = np.array([[2, 5], [1, 4]])
o = np.array([[0, 0], [2, 5]])
plt.quiver(*o, coordinates[:, 0], coordinates[:, 1], color=['blue', 'green'], scale=20)
plt.ylim(-100,100)
plt.xlim(-100,100)
plt.show()

fig, ax = plt.subplots()
# 以水平轴按照 angles 参数逆时针旋转得到箭头方向， units='xy' 指出了箭头长度计算方法
ax.quiver((0, 0), (0, 0), (1, 0), (1, 3), angles=[60, 300], units='xy', scale=1, color='r')
plt.axis('equal')
plt.xticks(range(-5, 6))
plt.yticks(range(-5, 6))
plt.grid()
plt.show()

#
X, Y = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))
U, V = np.cos(X), np.sin(Y)
fig, ax = plt.subplots()

ax.set_title("pivot='mid'; every third arrow; units='inches'")
Q = ax.quiver(X[::3, ::3], Y[::3, ::3], U[::3, ::3], V[::3, ::3], units='inches', pivot='mid', color='g')
qk = ax.quiverkey(Q, 0.9, 0.9, 1, r'$1 \frac{m}{s}$', labelpos='E',
                   coordinates='figure')
ax.scatter(X[::3, ::3], Y[::3, ::3], color='r', s=5)
plt.show()

#
X, Y = np.meshgrid(np.arange(0, 2 * np.pi, .2), np.arange(0, 2 * np.pi, .2))
U, V = np.cos(X), np.sin(Y)
fig, ax = plt.subplots()
# M 为颜色矩阵
M = np.hypot(U, V)
ax.set_title("pivot='tip'; scales with x view")
Q = ax.quiver(X, Y, U, V, M, units='xy', scale=1 / 0.15, pivot='tip')
qk = ax.quiverkey(Q, 0.9, 0.9, 1, r'$1 \frac{m}{s}$', labelpos='E',
                  coordinates='figure')
ax.scatter(X, Y, color='r', s=1)
plt.show()

##
import numpy as np
Velo = np.array([[5,8],[4,9]])
Elsp = np.array([0.3, 0.2])
Combo = [Velo, Elsp]
for x in Combo:
    for y in x:
        #Base = [[3, 4], []]
        print(y)
#枚举实现 a = [,,,,,]
for i,j in enumerate(Velo):
    print (i, j) #结果

# Calculate with trolley's start position, step velocity, step elapsed-milliseconds.
colours = ["red", "green", "blue"]
Base = [[0, 0]]
for i in range(0, len(Velo)):
    displace = Velo[i] * Elsp[i]
    print("delta: ", displace)
    cartesian = Base[i] + displace
    print("coor forward: ", cartesian)
    Base.append(cartesian)
print(Base, Velo, Elsp)

# 0 red
# 1 green
# 2 blue