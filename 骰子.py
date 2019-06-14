from random import randint
import pygal
class Die():
    def __init__(self,num_sides=6):
        self.num_sides=num_sides
    def roll(self):
        return randint(1,self.num_sides)
die1=Die()
die2=Die()
results=[]
for roll_num in range(100):#扔的次数
    result=die1.roll()+die2.roll()
    results.append(result)
frequences=[]#单个点数出现次数
max_result=die1.num_sides+die2.num_sides
for value in range(2,max_result+1):
    frequence=results.count(value)
    frequences.append(frequence)
hist=pygal.Bar()
hist.title='results of rolling two D6 1000 times'
hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title='result'
hist.y_title='frequence of result'

hist.add('D6+D6',frequences)
hist.render_to_file('die2_visual.svg')
