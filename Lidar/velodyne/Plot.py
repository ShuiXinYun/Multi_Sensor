import csv
import matplotlib.pyplot as plt

dist = '6.0'
with open("./data/%s.csv" % dist) as f:
    x = []
    y = []
    reader = csv.reader(f)
    next(reader)
    for line in reader:
        x.append(float(line[0]))
        y.append(float(line[6]))
    plt.scatter(x, y, s=10, alpha=1, edgecolors='None', marker='^')
    plt.ylim(-0.03, 0.03)
    plt.title('Distance = %sm' % dist, fontsize=20)  # 显示图表标题
    plt.xlabel('time(s)', fontsize=18)  # x轴名称
    plt.ylabel('error(m)', fontsize=18)  # y轴名称
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.grid(True)  # 显示网格线
    plt.show()
