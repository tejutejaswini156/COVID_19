import COVID19Py
import matplotlib.pyplot as plt
covid19=COVID19Py.COVID19()
data=covid19.getAll(timelines=True)
virusdata=dict(data["latest"])
names=list(virusdata.keys())
values=list(virusdata.values())
plt.bar(range(len(virusdata)),values,tick_label=names)
plt.show()
