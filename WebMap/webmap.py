import folium
import pandas

vol = pandas.read_csv("USAvolcanoes.txt")
lat = list(vol["LAT"])
lon = list(vol["LON"])
name = list(vol["NAME"])
elev = list(vol["ELEV"])

map = folium.Map(location = [38.58,-99.09], zoom_start=5, tiles="stamen terrain")

f = folium.FeatureGroup("Map1")

for lt,ln,nm,el in zip(lat,lon,name,elev):
    f.add_child(folium.Marker(location = [lt,ln], popup=str(el)+"\n"+nm, icon=folium.Icon(color="red")))


map.add_child(f)
map.save("BasicMap.html")
