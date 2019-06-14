import matplotlib.pyplot as plt
#随机漫步
from random import  choice
class RanddomWalk():
    def __init__(self,num_points=5000):
        self.num_points=num_points
        #设置漫步次数
        #所有随机漫步开始于0,0
        self.x_values=[0]
        self.y_values=[0]
    def fill_walk(self):
        #计算随机漫步包含的所有点
        while len(self.x_values)<self.num_points:
            x_direction=choice([1,-1])
            x_distance=choice([1,2,3,4,0])
            x_step=x_direction * x_distance
            #决定前进方向和前近距离
            y_direction = choice([1, -1])
            y_distance = choice([1, 2, 3, 4, 0])
            y_step = y_direction * y_distance

            if x_step==0 and y_step==0:
                continue
            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
if __name__=='__main__':
    while True:
        rw=RanddomWalk()#可以给点数
        rw.fill_walk()
        #plt.figure(figsize=(10,6))  #图纸大小,屏幕尺寸
        point_nums=list(range(rw.num_points))
        plt.scatter(rw.x_values,rw.y_values,c=point_nums,cmap=plt.cm.Reds,s=15)

        plt.scatter(0,0,c='green',s=100)
        plt.scatter(rw.x_values[-1],rw.y_values[-1],c='blue',s=100)
        #起点和终点  green  blue
        #隐藏坐标轴
        plt.axes().get_xaxis().set_visible(False)
        plt.axes().get_yaxis().set_visible(False)

        plt.show()
        keep=input('make another walk?(y/n):')
        if keep=='n':
            break
        elif keep=='y':
            continue
        else:
            input('error')
            continue



