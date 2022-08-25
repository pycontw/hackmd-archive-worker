# Geospatial data processing, analysis and visualization using Python - Prakhar Srivastava

{%hackmd oY5wCMoHQp2p3JLBDTxvEA %}

<iframe src="https://app.sli.do/event/cdfx9lzu" height=450 width=100%></iframe>

> 從這開始
> 

https://github.com/prakharcode/geospatial

## Set everything up
### Clone the project
```bash
git clone https://github.com/prakharcode/geospatial.git
cd geospatial
```

### Use venv (optional)
```bash
python3 -m venv env
source env/bin/activate
```
#### Configure ipykernel to use venv
https://zhuanlan.zhihu.com/p/33257881

### Install dependencies
```bash
pip install -r requirements.txt
```
### Open jupyter notebook
```bash
jupyter notebook
```

### Fix an error

An error occur at cell `countries.plot()`.

Install `descartes` .

```bash
pip install descartes
```

## 01
### Change CRS
```python
countries.to_crs({'init': 'epsg:<epsg_num>'}) # or .to_crs(epsg=3395)
```

### Solve DriverError 
```
import fiona
from shapely.geometry import shape

with fiona.drivers():
    with fiona.open("data/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp") as collection:
        for feature in collection:
            # ... do something with geometry
            geom = shape(feature['geometry'])
            # ... do something with properties
            print(feature['properties']['name'])
```
```
DriverError: data/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp: No such file or directory
```

```
cd data
unzip ne_110m_admin_0_countries
mkdir ne_110m_admin_0_countries
mv ne_110m_admin_0_countries.* ne_110m_admin_0_countries
```

## 02

### Solve DriveError
```
countries = geopandas.read_file("zip://./data/ne_110m_admin_0_countries.zip")
cities = geopandas.read_file("zip://./data/ne_110m_populated_places.zip")
rivers = geopandas.read_file("zip://./data/ne_50m_rivers_lake_centerlines.zip")
```
```
DriverError: '/vsizip/./data/ne_110m_admin_0_countries.zip' does not exist in the file system, and is not recognized as a supported dataset name.
```
```
mv ne_110m_admin_0_countries/ne_110m_admin_0_countries.zip .
```

## 03

`.joined = geopandas.sjoin(cities, countries, op='within', how='left')` occur `ModuleNotFoundError: No module named 'rtree'`

But, if `rtree` install, `OSError: Could not find libspatialindex_c library file` will occur.

solve: https://github.com/gboeing/osmnx/issues/45

###### tags: `PyConTW2019`
