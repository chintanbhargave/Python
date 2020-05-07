import folium

map = folium.Map(location = [38.58,-99.09], zoom_start=5, tiles="stamen terrain")

f = folium.FeatureGroup("Map1")
f.add_child(folium.Marker(location = [38.58,-99.09], popup="MyMarker", icon=folium.Icon(color="red")))

map.add_child(f)
map.save("BasicMap.html")
