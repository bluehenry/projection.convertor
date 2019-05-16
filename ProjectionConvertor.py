from pyproj import Geod, Proj, pj_ellps, pj_list, transform
from pyproj.crs import CRSError

# Define a projection with Proj4 notation
# Minge Grade
er94 = Proj("+proj=tmerc +lon_0=120.95 +x_0=446904.02 +y_0=2879827.84 +k_0=0.9999 +lat_0=0")  # +init=epsg:4283

# Alternate - Some Errors came from the Above cod use alternate for a better Conversion.
cpg94_ALT = Proj(
    "+proj=tmerc +lon_0=119.166666666 +x_0=69861.900 +y_0=2699844.130 +k_0=1.000099 +lat_0=0 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0")  # +init=epsg:4283

# convert Mine Grid to Latitude and Longitude in Decimal Degrees
print(er94(331359.2527, 301156.5724, inverse=True))

# convert Latitude and Longitude to Mine Grid Coordinates
print(er94(119.82035314830647, -23.306474155846807))
