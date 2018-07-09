var chart = Highcharts.chart('container',{
		chart: {
				type: 'column'
		},
		title: {
				text: '二手房地区分布图'
		},
		subtitle: {
				text: '数据来源:https://bj.lianjia.com/'
		},
		xAxis: {
				categories: [
						'bs','cn','fx','hk','hp',
						'ja','js','cm','shzb',
						'jd','qf','sj','yp','zb',
						'mh','pdq','pt','xh',
				],
				crosshair: true
		},
		yAxis: {
				min: 0,
				title: {
						text: '二手房数量'
				}
		},
		tooltip: {
				// head + 每个 point + footer 拼接成完整的 table
				headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
				pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
				'<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
				footerFormat: '</table>',
				shared: true,
				useHTML: true
		},
		plotOptions: {
				column: {
						borderWidth: 0
				}
		},
		series: [{
				name: '朝向',
				data: [2996,3000,1171,
							 2851,2201,1311,
							 106,47,31,
							 2899,2550,2641,
							 3100,2756,2500,
							 2912,3025,2853]
		}]
});