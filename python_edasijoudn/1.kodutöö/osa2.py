 
# Link to download: https://test.pypi.org/project/koordinaadid-hejoes/0.0.4/
# or by: pip install -i https://test.pypi.org/simple/ koordinaadid-hejoes==0.0.4
from koordinaadid_hejoes.konverter import *

# Function that converts L-Est97 to WGS84 :
# est_to_wgs84(param1, param2)
# ex: est_to_wgs84(6584338.65, 537735.47) >>> "Tulemuseks on 59.395312° 24.664182° WGS84 süsteemis"

# Function that converts WGS84 to L-Est97:
# wgs84_to_est(param1, param2)
# ex: wgs84_to_est(59.395312, 24.664182) >>> "Tulemuseks on 6584338.655863° 537735.466861° eesti süsteemis"




print(est_to_wgs84(6584338.65, 537735.47))

print(wgs84_to_est(59.395312, 24.664182))