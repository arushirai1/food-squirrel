from app import app
import folium

@app.route('/')
@app.route('/index')
def index():
    start_coords = (41.8333722, -87.628204)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()