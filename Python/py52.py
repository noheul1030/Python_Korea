import matplotlib.pyplot as plt

figure = plt.figure()
axes =  figure.add_subplot(111)
x = [0,1,2,3,4]
y = [4,1,3,5,2]
axes.plot(x,y)
plt.show()

# pyinstaller -w -F "py52.py"