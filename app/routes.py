from app import app
import folium
import csv
import sys
import numpy as np
import pandas as pd

from flask import render_template
import os
import geopandas as gpd

@app.route('/')
@app.route('/index')
def index():
    print(os.getcwd())
    start_coords = (41.8333722, -87.628204)
    folium_map = folium.Map(width=500,height=500, location=start_coords, tiles="Stamen Toner", zoom_start=10)

    filepath = "app/static/Grocery_Stores_-_2013.csv"
    boundaries_path = "app/static/boundaries.geojson"
    data = pd.read_csv(filepath)
    data.info()

    boundaries_df = gpd.read_file(boundaries_path)
    print(boundaries_df['geometry'][0])
    #data = np.loadtxt(filename, delimiter=",", skiprows=1, dtype=np.unicode_)
    #data = np.fromregex(filename, r'(\d+),"(.+)",(\d+)', np.object)
    #print(data[0])
    #pandas use
    '''
    for row in data:
        print(','.join(row))
    '''
    print(data['LATITUDE'][0])
    print(data.shape[0])
    #test_data = [(41.8333722, -87.628204), (42.8333722, -87.628204), (41.84722, -87.628204)]
    for item in range(data.shape[0]):
        #clean the location data here
        folium.Marker(
            location=[data['LATITUDE'][item], data['LONGITUDE'][item]],
            popup=data['STORE NAME'][item],
            icon=folium.Icon(color='green')
        ).add_to(folium_map)

    #folium_map.add_child(folium.GeoJson(data=open(boundaries_path)))
    folium_map.save('app/templates/map.html')

    return render_template('index.html')

    #return folium_map._repr_html_()