import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mplcursors
import base64
import folium
import IPython
import ipywidgets as widgets
from IPython.display import clear_output


def bar_global(data: pd.core.frame.DataFrame) -> None:
    '''
    Plotting function that gets the temperature timeseries dataframe as input
    and creates and interactive bar plot with the average differences per year from 1880 to 2021.

    data: Wide timeseries dataframe with temperature for multiple weather stations in Celsius. Stations are in the rows,
    years are in the columns.
    '''

    values = np.array(data.mean())  # get global average difference per year
    clrs = ["blue" if (x < 0) else "red" for x in values]  # colors for positive and negative differences
    fig, ax = plt.subplots(figsize=(9, 4))  # set plot size
    line = ax.bar(np.array(range(1880, 2022, 1)), values, color=clrs)  # bar plot
    ax.set_xlim(1879, 2022)  # set axis limits
    plt.title("Station network temperature difference \nwith respect to 1850-1900 average", fontsize=12)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Temperature ($ ^{\circ}$C)", fontsize=12)

    # cursor interaction for creating labels
    cursor = mplcursors.cursor()

    @cursor.connect("add")
    def on_add(sel):
        x, y, width, height = sel.artist[sel.index].get_bbox().bounds
        sel.annotation.get_bbox_patch().set(fc="white", alpha=1)
        sel.annotation.set(
            text=f"Year {int(x) + 1} \n {values[int(x) - 1880 + 1]:.2f}" + "C" + "$^{\circ}$",
            position=(0, 20),
            anncoords="offset points",
        )
        sel.annotation.xy = (x + width / 2, height)
        sel.axvline(x=x, color="k")

    # show plot
    plt.show()


def local_temp_map(df: pd.core.frame.DataFrame) -> folium.Map:
    '''
    Plotting function that gets the temperature timeseries dataframe with additional information and returns an interactive map
    with bar plots for each station.

    df: Wide timeseries dataframe with temperature for multiple weather stations in Celsius. Stations are in the rows,
    years are in the columns. Contains geographical coordinates and station names.
    '''

    folium_map = folium.Map(
        location=[35, 0],
        zoom_start=1.5,
        tiles="cartodb positron",
        max_bounds=False,
    )
    loc = df[["LATITUDE", "LONGITUDE"]]
    width, height = 500, 230

    for index, location_info in loc.iterrows():
        png = f"plots/{df['STATION'].loc[index]}.png"
        encoded = base64.b64encode(open(png, "rb").read())
        html = '<img src="data:image/png;base64,{}" style="height:100%";>'.format
        iframe = folium.IFrame(
            html(encoded.decode("UTF-8")), width=width, height=height
        )
        popup = folium.Popup(iframe, max_width=2650)
        folium.Marker(
            [location_info['LATITUDE'], location_info['LONGITUDE']],
            popup=popup,
            icon=folium.Icon(color='black', icon_color='white'),
        ).add_to(folium_map)

    return folium_map


def slider_global_temp() -> None:
    '''
    Creates an interactive slider that shows the global temperature around the globe from 1884 to 2020
    '''

    # set up plot
    out = widgets.Output()

    def update(Year=1884):
        with out:
            clear_output(wait=True)
            display(IPython.display.Image(f'data/NASA/{Year}.png'))

    slider = widgets.IntSlider(
        min=1884, max=2020, layout=widgets.Layout(width='95%')
    )
    widgets.interactive(update, Year=slider)

    layout = widgets.Layout(
        flex_flow='column', align_items='center', width='700px'
    )

    wid = widgets.HBox(children=(slider, out), layout=layout)
    display(wid)
