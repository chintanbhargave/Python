import folium

map = folium.Map(location = [38.58,-99.09], zoom_start=5, tiles="stamen terrain")

map.save("BasicMap.html")
