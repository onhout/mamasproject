requirejs.config({
	baseUrl: '../static/bower_components',
	paths: {
		jquery: 'jquery/dist/jquery',
		bootstrap: 'bootstrap/dist/js/bootstrap',
		react: 'react/react',
		react_dom: 'react/react-dom'
	},
	shim:{
		bootstrap:{
			deps: ['jquery'],
			exports: 'Bootstrap'
		},
		reactdom: {
			deps: ['react'],
			exports: ['Reactdom']
		}
	}
});

require(['jquery','bootstrap', 'react', 'react_dom'], function(){

});