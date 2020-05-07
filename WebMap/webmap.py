import folium
import pandas

vol = pandas.read_csv("USAvolcanoes.txt")
lat = list(vol["LAT"])
lon = list(vol["LON"])
name = list(vol["NAME"])

map = folium.Map(location = [38.58,-99.09], zoom_start=5, tiles="stamen terrain")

f = folium.FeatureGroup("Map1")

for lt,ln,nm in zip(lat,lon,name):
    f.add_child(folium.Marker(location = [lt,ln], popup=nm, icon=folium.Icon(color="red")))


map.add_child(f)
map.save("BasicMap.html")
