import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

measurements = Base.classes.measurements
stations = Base.classes.stations

session = Session(engine)

app = Flask(__name__)

@app.route("/api/v1.0/precipitation")
def precipitation():
	precip = session.query(measurements.tobs, measurements.date)
	return jsonify(precip)

@app.route("api/v1.0/stations")
def stations():
	station = session.query(stations.station)
	return station

@app.route("api/v1.0/tobs")
def tobs():
	tobs = session.query(measurements.tobs)
	return tobs

start_date = input('enter start date')
@app.route("api/v1.0/<start>")
def start():
	start = session.query(func.max(measurements.tobs),
						  func.min(measurements.tobs,
						  func.mean(measurements.tobs),
						  measurements.date WHEN > start_date)

	return jsonify(start)




