import numpy as np
import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#Flask Setup
app = Flask(__name__)

#read the csv files into dataframes
metadata = pd.read_csv("Belly_Button_Biodiversity_Metadata.csv")
otu_id = pd.read_csv("Belly_Button_biodiversity_otu_id.csv")
samples = pd.read_csv("belly_button_biodiversity_samples.csv")

#create route to render index.html
@app.route("/")
def home():
	return render_template("index.html")

#returns a list of sample names
@app.route('/names')
def names():
	samples_list = samples.columns.values.tolist()
	samples_list.pop(0)
	return render_template (results_list)

#returns a list of OTU descriptions
@app.route('/otu')
def otu():
	otu_list = otu_id['lowest_taxonomic_unit_found'].tolist()
	return render_template (otu_list)

#returns metadata for a given sample
@app.route('/metadata/<sample>')
def metadata_id(sample):
    samples_id = int(samples_id[3:])
    metadata_condensed = metadata[['AGE', 'BBTYPE', 'ETHNICITY', 'GENDER', 'LOCATION', 'SAMPLEID']]
    for itr, row in metadata_condensed.iterrows():
        if samples_id == row['SAMPLEID']:
            metadata_json = row.to_json(orient='index')
            break
    return metadata_json

#returns weekly washing frequency as a number
@app.route('/wfreq/<sample>')
def wash_id(sample):
	samples_id = float(samples_id2[3:])
	for itr, row in metadata.iterrows():
		if samples_id2 == row['SAMPLEID']:
			wash_freq = row['WFREQ']
			break
	return wash_freq

#returns OTU id's and sample values for a given sample
@app.route('/samples/<sample>')
def samples_dict(sample):
    id_to_dict_df = samples[['otu_id', sample]]
    id_to_dict_df.sort_values(by=[sample], ascending = False, inplace = True)
    BB_list = id_to_dict_df['otu_id'].tolist()
    BB_dict = {'otu_ids': BB_list}
    id_list = id_to_dict_df[sample].tolist()
    id_dict = {'sample_values': id_list}
    samples_dict_to_list = []
    samples_dict_to_list.append(BB_dict)
    samples_dict_to_list.append(id_dict)
    return(samples_dict_to_list)


if __name__ == "__main__":
    app.run(debug=True)