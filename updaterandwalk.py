import matplotlib.pyplot as plt
#随机漫步  用了一种比较蠢的方法。。但是总归成功了 但是 多此一举了 。。这可能不是更新
from random import  choice
class RanddomWalk():
    def __init__(self,num_points=5000):
        self.num_points=num_points
        #设置漫步次数
        #所有随机漫步开始于0,0
        self.x_values=[0]
        self.y_values = [0]
        self.xy_values=[]#放置总共的移动情况 0->x   1->y
        self.ystep=[0]
        self.xstep=[0]
    def fill_walk(self):
        self.xstep=self.get_step()[0]
        self.ystep=self.get_step()[1]
    def get_step(self):
        #计算随机漫步包含的所有点
        while len(self.x_values)<self.num_points:
            x_direction=choice([1,-1])
            x_distance=choice([1,2,3,4,0])
            x_step=x_direction * x_distance
            y_direction = choice([1, -1])
            y_distance = choice([1, 2, 3, 4, 0])
            y_step = y_direction * y_distance

            if x_step==0 and y_step==0:
                continue
            next_x=self.x_values[-1]+x_step
            self.x_values.append(next_x)
            next_y = self.y_values[-1] + y_step
            self.y_values.append(next_y)
            self.xy_values=[self.x_values,self.y_values]
        return self.xy_values

if __name__=='__main__':
    while True:
        rw=RanddomWalk()#可以给点数
        rw.fill_walk()
        #plt.figure(figsize=(10,6))  #图纸大小,屏幕尺寸
        point_nums=list(range(rw.num_points))
        plt.scatter(rw.xstep,rw.ystep,c=point_nums,cmap=plt.cm.Reds,s=15)

        plt.scatter(0,0,c='green',s=100)
        plt.scatter(rw.xstep[-1],rw.ystep[-1],c='blue',s=100)
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



