import pyproj

#Import warnings makes it so that i dont get page full of warnings when running code. Purely for visual purposes
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


def est_to_wgs84(x, y):
    
    eesti = pyproj.Proj("+init=EPSG:3301")
    wgs84 = pyproj.Proj("+init=EPSG:4326")
    
    new_y, new_x = pyproj.transform(eesti, wgs84, y, x)
    
    
    result = (round(new_x, 3), round(new_y, 3))
    
    return result

def wgs84_to_est(new_x, new_y):

    est97 = pyproj.Proj("+init=EPSG:3301")
    wgs84 = pyproj.Proj("+init=EPSG:4326")
    
    x, y = pyproj.transform(wgs84, est97, new_y, new_x)
    
    result = result = (round(y, 3), round(x, 3))
    
    return result

#print (est_to_wgs84(6584338.65, 537735.47))
#print(wgs84_to_est(59.395312, 24.664182 ))


