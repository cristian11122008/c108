import random
import plotly.express as px
import plotly.figure_factory as ff
dicetotal=[]
count=[]
for i in range(0,100):
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    dicetotal.append(d1+d2)
    count.append(i)
print(d1,d2, dicetotal)
fig=ff.create_distplot([dicetotal],["results"])
fig.show()