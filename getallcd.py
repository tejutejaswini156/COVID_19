import COVID19Py
covid19=COVID19Py.COVID19()
data=covid19.getAll(timelines=True)
virusdata=dict(data["latest"])
names=list(virusdata.keys())
values=list(virusdata.values())
print(virusdata)
