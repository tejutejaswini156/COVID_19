import COVID19Py
import matplotlib.pyplot as plt
covid19=COVID19Py.COVID19()
location=covid19.getLocationByCountryCode("IN")
loc_data=location[0]
virusdata=dict(loc_data["latest"])
names=list(virusdata.keys())
values=list(virusdata.values())
plt.bar(range(len(virusdata)),values,tick_label=names)
plt.show()
