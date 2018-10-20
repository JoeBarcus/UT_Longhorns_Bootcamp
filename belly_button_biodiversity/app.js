function loadDropDown() {
	var dropdownOptions = {
		sample_id: ["<option default value=''>all</option"]
	};

	var sample_dropdown = d3.select("#selDataset");

	var names_url = "/names"

	for (var i = 0; i < url.length; i++) {
		var sample_name = url[0];
		var optionHTML = "<option value='" + sample_name + "'>" + sample_name + "</option>";
	}

	sample_dropdown.html(dropdownOptions.sample_id.join(""))
}

function piePlot() {
	var bubble_chart_data_url = "/samples/<sample>"
	var 

	var data = [{
		values: [bubble_chart_data_url: sample_value],
		labels: [bubble_chart_data_url: otu_ids],
		type: 'pie'
	}];

	var layout = {
		height: 400,
		width: 400
	};

	var update = {
		data = sample
	}

	Plotly.newPlot('belly_chart', data, layout)
	Plotly.restyle(graphDiv, update)
}

function bubblePlot() {

}
