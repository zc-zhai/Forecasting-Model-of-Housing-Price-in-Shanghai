var chart = Highcharts.chart('container', {
		data: {
				table: 'datatable'
		},
		chart: {
				type: 'column'
		},
		title: {
				text: ''
				// 该功能依赖 data.js 模块，详见https://www.hcharts.cn/docs/data-modules
		},
		yAxis: {
				allowDecimals: false,
				title: {
						text: '个',
						rotation: 0
				}
		},
		tooltip: {
				formatter: function () {
						return '<b>' + this.series.name + '</b><br/>' +
								this.point.y + ' 个' + this.point.name.toLowerCase();
				}
		}
});