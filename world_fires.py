import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

from datetime import datetime


filename = "world_fires_1_day.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    lats, lons, brights = [], [], []

    def append_lists():
        lats.append(float(row[0]))
        lons.append(float(row[1]))
        brights.append(float(row[2]))
        # dates.append(datetime.strptime(row[5], "%Y-%m-%d"))
        # times.append(datetime.strptime(row[6], "%H-%M-%S"))

    for row in reader:
        append_lists()

data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats,
    "marker": {
        "size": [1/30*bright for bright in brights],
        "color": brights,
        "colorscale": "YlOrBr",
        "reversescale": False,
        "colorbar": {"title": "Brightness"}
    }
}]

my_layout = Layout(title="Global Fires")

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="global_fires.html")
