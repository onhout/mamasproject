requirejs.config({
	baseUrl: 'static/bower_components',
	paths: {
		jquery: 'jquery/dist/jquery',
		bootstrap: 'bootstrap/dist/js/bootstrap'
	},
	shim:{
		bootstrap:{
			deps: ['jquery'],
			exports: 'Bootstrap'
		}
	}
})

require(['jquery','bootstrap'], function(){
	
})