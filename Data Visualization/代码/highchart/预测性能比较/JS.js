Highcharts.chart('container', {
		chart: {
				type: 'column'
		},
		title: {
				text: '预测模型性能比较'
		},
		subtitle: {
				text: ''
		},
		xAxis: {
				type: 'category'
		},
		yAxis: {
				title: {
						text: 'R-squared'
				}
		},
		legend: {
				enabled: false
		},
		plotOptions: {
				series: {
						borderWidth: 0,
						dataLabels: {
								enabled: true,
								format: '{point.y:.2f}'
						}
				}
		},
		tooltip: {
				headerFormat: '<span style="font-size:11px">{series.name}</span><br>',
				pointFormat: '<span style="color:{point.color}">{point.name}</span>: <b>{point.y:.2f}%</b> of total<br/>'
		},
		series: [{
				name: '预测模型',
				colorByPoint: true,
				data: [{
						name: 'BayesianRidge_none',
						y: 0.68,
						drilldown: 'BayesianRidge_none'
				}, {
						name: 'Lasso_alfa0.1',
						y: 0.77,
						drilldown: 'Lasso_alfa0.1'
				}, {
						name: 'LassoLarsCV_none',
						y: 0.73,
						drilldown: 'LassoLarsCV_none'
				}, {
						name: 'Linear_none',
						y: 0.71,
						drilldown: 'Linear_none'
				},  {
						name: 'MLP_none',
						y: 0.86,
						drilldown: 'MLP_none'
				},{
						name: 'PassiveAggressiveRegressor_none',
						y: 0.65,
						drilldown: 'PassiveAggressiveRegressor_none'
				},
							 {
									 name: 'Randomforest_depth10',
									 y: 0.84,
									 drilldown: 'Randomforest_depth10'
							 },
							 {
									 name: 'Randomforest_depth20',
									 y: 0.87,
									 drilldown: 'Randomforest_depth20'
							 }]
		}],
}
								)