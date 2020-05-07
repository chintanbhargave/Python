import folium
import pandas

vol = pandas.read_csv("USAvolcanoes.txt")
lat = list(vol["LAT"])
lon = list(vol["LON"])
name = list(vol["NAME"])
elev = list(vol["ELEV"])

def color(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation <= 3000:
        return "orange"
    else:
        return "red"


map = folium.Map(location = [38.58,-99.09], zoom_start=5, tiles="stamen terrain")

f = folium.FeatureGroup("Map1")

for lt,ln,nm,el in zip(lat,lon,name,elev):
    f.add_child(folium.CircleMarker(location = [lt,ln], radius=8, popup=str(el)+"\n"+nm, fill_color = color(el), color="grey", fill_opacity=0.7))

#  To add polygons GeoJson is used. polygon coordinates are in the worldpop.json
f.add_child(folium.GeoJson(data=open("worldpop.json", 'r', encoding='utf-8-sig').read()))

map.add_child(f)
map.save("BasicMap.html")
