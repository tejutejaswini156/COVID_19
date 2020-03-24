import COVID19Py
covid19=COVID19Py.COVID19()
location=covid19.getLocationByCountryCode("IN")
loc_data=location[0]
virusdata=dict(loc_data["latest"])
print(virusdata)
