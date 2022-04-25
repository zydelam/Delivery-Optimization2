from geopy.distance import geodesic
import pandas as pd
import numpy as np


def lat_long_format(x):
    """This function converts given 'longitude/latitude' string to 'latitude, longitude' string"""    
    tmp_list = x[1:-1].split('/') # split the string based on '/'
    long = tmp_list[0] # longitude
    lat = tmp_list[1] # latitude
    x = lat + ',' + long # 'latitude, langitude'
    return x
    

def prediction(model, kmeans_store, kmeans_cust, in_arr):
    print(in_arr)
    order_date = in_arr[0].split('-')
    weight = float(in_arr[1])
    width = float(in_arr[2])
    store_add = lat_long_format(in_arr[3])
    cust_add = lat_long_format(in_arr[4])
    distance = geodesic(store_add, cust_add).km
    store_lat, store_long = [float(i) for i in store_add.split(',')]
    cust_lat, cust_long = [float(i) for i in cust_add.split(',')]
    cust_cluster = np.random.randint(1,5)
    store_cluster = np.random.randint(1,5)
    in_model = pd.DataFrame([[distance, weight, store_cluster, cust_cluster, in_arr[-1], width, in_arr[-2]]], columns=['distance','Size of the box weight','store_cluster','cust_cluster','Weather', 'Size of the box width', 'Courier'])
    print(in_model)
    s_days = model.predict(in_model)
    order_date[2] = str(int(order_date[2]) + int(s_days))
    d_date = '-'.join(order_date)
    
    return d_date
