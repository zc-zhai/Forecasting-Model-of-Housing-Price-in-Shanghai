var chart = Highcharts.chart('container', {
		chart: {
				type: 'spline'
		},
		title: {
				text: 'MLP_none'
		},
		subtitle: {
				text: 'Predicted VS Target'
		},
		xAxis: {
				type: 'time',
				title: {
						text: null
				}
		},
		yAxis: {
				title: {
						text: '万元'
				},
				min: 0
		},
		tooltip: {
				headerFormat: '<b>{series.name}</b><br>',
				pointFormat: '{point.x:%e. %b}: {point.y:.2f} m'
		},
		plotOptions: {
				spline: {
						marker: {
								enabled: true
						}
				}
		},
		series: [{
				name: 'Predicted',
				// Define the data points. All series have a dummy year
				// of 1970/71 in order to be compared on the same x axis. Note
				// that in JavaScript, months start at 0 for January, 1 for February etc.
				data: [203,926,591,573,213,324,308,223,1131,584,410,939,265,647,504,
							 997,274,284,486,282,361,392,357,414,933,178]
		}, {
				name: 'Target',
				data: 
				[170,1050,655,530,198,310,290,225,1410,445,485,925,209,515,598,
				 970,260,298,673,270,320,440,460,400,800,199]
		}]
});
