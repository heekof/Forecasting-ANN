import plotly
import plotly.plotly as py
from plotly.tools import FigureFactory as FF
import pandas as pd
import time

plotly.tools.set_credentials_file(username='heekof', api_key='3s4cx6b8pn')




while True:
    df = pd.read_csv('Data/data_demo.csv',sep=";")
    df_sample = df.tail(10)
    #df_sample.net_out_packets_sec = df_sample.net_out_packets_sec.values.astype(int)
    #df_sample.net_in_bytes_sec = df_sample.net_in_bytes_sec.values.astype(int)
    df_sample = df_sample.set_index("Timestamp")
    table = FF.create_table(df_sample, index=True, index_title="TimeStamp")



    py.image.save_as(table, 'my_plot.png')
    py.image.ishow(table)

    time.sleep(2)
