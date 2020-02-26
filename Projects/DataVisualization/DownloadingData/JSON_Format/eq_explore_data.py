import json

# Explore the structure of the data.
filename = 'Projects/DataVisualization/DownloadingData/JSON_Format/data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, longs, lats  = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    long = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    longs.append(long)
    lats.append(lat)

print(mags[:10])
print(longs[:5])
print(lats[:5])
