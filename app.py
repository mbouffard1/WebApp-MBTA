from flask import Flask, render_template, request, redirect
from mbta_helper import get_lat_long, get_nearest_station
app = Flask(__name__)
app.run(debug=True)

@app.route("/")

def form():
    '''Opens page "mbta_html.html" which prompts the user for the input of the location
    they want to find the nearest MBTA station to.
    '''
    return render_template("mbta_html.html")


@app.route("/nearest", methods=['GET', 'POST'])
def nearest():
    '''takes the input from "mbta_html.html" and uses it to find the nearest station to that location
    then redirects to the next page for the output'''
    place_name = request.form['location']
    print('Location:', request.form['location'])
    latitude = str(get_lat_long(place_name)[0])
    longitude = str(get_lat_long(place_name)[1])
    nearest_station = get_nearest_station(latitude, longitude)
    print(nearest_station)
    return redirect('/nearest_mbta')



@app.route("/nearest_mbta", methods = ['GET','POST'])
def nearest_mbta():
    '''Opens page "mbta_station.html" and tells the user the closest station and whether or not it is 
    wheelchair accessible'''
    return render_template("mbta_station.html")
    
    

