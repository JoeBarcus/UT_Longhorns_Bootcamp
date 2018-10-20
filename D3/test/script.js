d3.csv('data.csv', function (data) {
	// Variables
	var body = d3.select('body')
	var margin = { top: 50, right: 50, bottom: 50, left: 50}
	var h = 700 - margin.top - margin.bottom
	var w = 700 - margin.left - margin.right
	var formatPercent = d3.format('.2%')
	// Scales
	var colorScale = d3.scale.category20()
	var xScale = d3.scale.linear()
		.domain([
			d3.min([0, d3.min(data,function (d) { return d.income})]),
			d3.max([0, d3.max(data,function (d) { return d.income})]),
			])
		.range([0,w])
	var yScale = d3.scale.linear()
		.domain([
			d3.min([0, d3.min(data,function (d) { return d.drink})]),
			d3.max([0, d3.max(data,function (d) { return d.drink})]),
			])
		.range([h,0])
	// SVG
	var svg = body.append('svg')
	    .attr('height',h + margin.top + margin.bottom)
	    .attr('width',w + margin.left + margin.right)
	  .append('g')
	    .attr('transform','translate(' + margin.left + ',' + margin.top + ')')
	// X-axis
	var xAxis = d3.svg.axis()
	  	.scale(xScale)
	  	.ticks(6)
	  	.orient('bottom')
	// Y-axis
	var yAxis = d3.svg.axis()
	  	.scale(yScale)
	  	.tickFormat(formatPercent)
	  	.ticks(5)
	  	.orient('left')
	 // Circles
	var circles = svg.selectAll('circle')
		.data(data)
		.enter()
	  .append('circle')
	  	.attr('cx', function (d) {return xScale(d.income)})
	  	.attr('cy', function (d) {return yScale(d.drink)})
	  	.attr('r', '9')
	  	.attr('stroke', 'black')
	  	.attr('stroke-width',1)
	  	.attr('fill', function (d,i) {return colorScale(i)})
	  	// .attr('fill', '#4286f4')
	  	.on('mouseover', function () {
	  		d3.select(this)
	  			.transition()
	  			.duration(200)
	  			.attr('r',11)
	  			.attr('stroke-width', 3)
	  	})
	  	.on('mouseout', function () {
	  		d3.select(this)
	  			.transition()
	  			.duration(200)
	  			.attr('r',9)
	  			.attr('stroke-width', 1)
	  	})
	  	.append('title')  // Tooltip
	  	 	.text(function (d) {return d.state +
	  	 						'\nIncome: ' + d.income + 
	  	 						'\nAlcoholic ' + formatPercent(d.drink) })
	var abbrev = svg.selectAll('text')
		.data(data)
		.enter()
		.append('text')
		.text(function(d) {return d.abbr} )
		.attr('x', function(d) {return xScale(d.income)})
		.attr('y', function(d) {return yScale(d.drink)})
		.attr('font-size', '10px')
		.attr('text-anchor', 'middle')
		.attr('class', 'svg-text')


	// X-axis
	svg.append('g')
		.attr('class','axis')
		.attr('transform', 'translate(0,' + h + ')')
		.call(xAxis)
		.append('text') // X-axis Label
		.attr('class','label')
		.attr('y',-10)
		.attr('x',w)
		.attr('dy','.71em')
		.style('text-anchor','end')
		.text('Income')
	// Y-axis
	svg.append('g')
		.attr('class', 'axis')
		.call(yAxis)
		.append('text') // y-axis Label
		.attr('class','label')
		.attr('transform','rotate(-90)')
		.attr('x',0)
		.attr('y',5)
		.attr('dy','.71em')
		.style('text-anchor','end')
		.text('Alcoholic')
})	
