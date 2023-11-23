from flask import Flask, render_template, request
import pyproj

from koordinaadid_hejoes.konverter import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/est_to_wgs', methods=['POST'])

def convert():
    est97_x = float(request.form['est97_x'])
    est97_y = float(request.form['est97_y'])

    result = str(est_to_wgs84(est97_x, est97_y))
    
    return result

@app.route('/wgs_to_est', methods=['POST'])

def reverse():
    wgs84_x = float(request.form['wgs84_x'])
    wgs84_y = float(request.form['wgs84_y'])
    
    result = str(wgs84_to_est(wgs84_x, wgs84_y))
    
    return result

if __name__ == '__main__':
    app.run(debug=True)

