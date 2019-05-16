'''
Convert Geographic Coordinates (longitude/latitude) to Map Projection
Geographic coordinate systems (GCS) most commonly have units in decimal degrees measuring degrees of longitude (x-coordinates) and degrees of latitude (y-coordinates).
The location of data is expressed as positive or negative numbers: positive x- and y-values for north of the equator and east of the prime meridian, and negative values for south of the equator and west of the prime meridian.

Spatial data can also be expressed using projected coordinate systems (PCS).
Coordinates are expressed using linear measurements rather than angular degrees.
Finally, some data may be expressed in a local coordinate system with a false origin (0, 0 or other values) in an arbitrary location that can be anywhere on earth.

A projection is the means by which you display the coordinate system and your data on a flat surface, such as a piece of paper or a digital screen.

Universal Transverse Mercator (UTM)

https://spatialreference.org/
https://en.m.wikipedia.org/wiki/Spatial_reference_system
https://en.wikipedia.org/wiki/World_Geodetic_System
https://en.wikipedia.org/wiki/Web_Mercator_projection

Spherical Mercato
Transverse Mercator： https://proj4.org/operations/projections/tmerc.html

MGA (Map Grid Australia) EPSG Codes
'''

'''

https://proj4.org/operations/projections/tmerc.html
'''


from pyproj import Geod, Proj, pj_ellps, pj_list, transform
from pyproj.crs import CRSError

# Define a projection with Proj4 notation
# Eastern Ridge - Newman Operations
er94 = Proj("+proj=tmerc +lon_0=120.95 +x_0=446904.02 +y_0=2879827.84 +k_0=0.9999 +lat_0=0")  # +init=epsg:4283
# Jimblebar -Eastern Pilbara Grid
epg94 = Proj("+proj=tmerc +lon_0=120.0833333333333 +x_0=50000 +y_0=2800000 +k_0=1.0000786 +lat_0=0")  # +init=epsg:4283
# Yandi - Yandi Grid
yan94 = Proj("+proj=tmerc +lon_0=117 +x_0=-200122.216 +y_0=2599668.04 +k_0=0.99953 +lat_0=0")  # +init=epsg:4283
# Whaleback - Newman Operations
wb94 = Proj("+proj=tmerc +lon_0=120.95 +x_0=446901.042 +y_0=2879773.273 +k_0=0.999879 +lat_0=0")  # +init=epsg:4283
# Area C and SouthFlank - Central Pilbara Grid
cpg94 = Proj(
    "+proj=tmerc +lon_0=119.1666666666667 +x_0=69861.89999999999 +y_0=2699844.13 +k_0=1.000099 +lat_0=0")  # +init=epsg:4283
# Alternate Area C and SouthFlank - Some Errors came from the Above cod use alternate for a better Conversion.
cpg94_ALT = Proj(
    "+proj=tmerc +lon_0=119.166666666 +x_0=69861.900 +y_0=2699844.130 +k_0=1.000099 +lat_0=0 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0")  # +init=epsg:4283

# convert Mine Grid to Latitude and Longitude in Decimal Degrees
print(er94(331359.2527, 301156.5724, inverse=True))

# convert Latitude and Longitude to Mine Grid Coordinates
print(er94(119.82035314830647, -23.306474155846807))
