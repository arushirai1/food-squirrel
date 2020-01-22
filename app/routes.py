from app import app
import folium
import csv
import sys
import numpy as np
import pandas as pd
import pdb

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
    boundaries_path = "app/static/neighborhoods.geojson"
    data = pd.read_csv(filepath)
    data = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data.LONGITUDE, data.LATITUDE))
    data.info()
    #print(data['LOCATION'][0])
    data.crs={'init': 'epsg:4326'}
    boundaries_df = gpd.read_file(boundaries_path)
    boundaries_df['neighborhood'] = boundaries_df.sec_neigh.astype('category')
    #import pdb 
    data_and_nbhood = gpd.sjoin(data, boundaries_df, op="within")
    data_and_nbhood.info()
    #boundaries_df.info()
    #print(boundaries_df['geometry'][0])
    #data = np.loadtxt(filename, delimiter=",", skiprows=1, dtype=np.unicode_)
    #data = np.fromregex(filename, r'(\d+),"(.+)",(\d+)', np.object)
    #print(data[0])
    #pandas use
    '''
    for row in data:
        print(','.join(row))
    '''
    #print(data['LATITUDE'][0])
    print(data.shape[0])
    #test_data = [(41.8333722, -87.628204), (42.8333722, -87.628204), (41.84722, -87.628204)]
    
    for store in data_and_nbhood.iterrows():
        #clean the location data here
        #pdb.set_trace()
        store = store[1]
        folium.Marker(
            location=[store['LATITUDE'], store['LONGITUDE']],
            popup=store['STORE NAME'],
            icon=folium.Icon(color='green'),
            clustered_marker=True
        ).add_to(folium_map)
    '''
    for nb in boundaries_df.iterrows():
        folium_map.add_child(folium.GeoJson(data=nb)))
    '''
    #folium.GeoJson(data_and_nbhood).add_to(folium_map)

    folium.GeoJson(boundaries_df).add_to(folium_map)
    folium_map.save('app/templates/map.html')

    return render_template('index.html')

    #return folium_map._repr_html_()