from app import app
import folium
import csv
import sys
import numpy as np
from flask import render_template
import os
@app.route('/')
@app.route('/index')
def index():
    #print(os.getcwd())
    start_coords = (41.8333722, -87.628204)
    folium_map = folium.Map(location=start_coords, tiles="Stamen Toner", zoom_start=14)

    filename = "app/static/Nearby_Independent_Cook_County_Grocery_Stores.csv"
    #data = np.loadtxt(filename, delimiter=",", skiprows=1, dtype=np.unicode_)
    data = np.fromregex(filename, r'(\d+),"(.+)",(\d+)', np.object)
    #print(data[0])
    for row in data:
        print(','.join(row))
    test_data = [(41.8333722, -87.628204), (42.8333722, -87.628204), (41.84722, -87.628204)]
    for item in test_data:
        #clean the location data here
        folium.Marker(
            location=[item[0], item[1]],
            popup='Test',
            icon=folium.Icon(color='green')
        ).add_to(folium_map)
    folium_map.save('app/template/map.html')

    return render_template('app/template/home.html')

    #return folium_map._repr_html_()