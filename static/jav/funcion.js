$(function(){
$("#tabla").on('click','#1',function(event){
		event.preventDefault();
		
Swal.fire ({
		title: 'Deseas modificar el archivo?',
		text: "Exitos!",
		icon: 'warning',
		showCancelButton: true,
		confirmButtonColor: '#3085d6',
		cancelButtonColor: '#d33',
		confirmButtonText: 'Si, lo modifico!',
		preConfirm:()=>{
			location.href=event.target.href;

		},
		allouOutsideClick:()=> false,
		allowEscapeKey:()=> false
	  })

	});

	
	$("#tabla").on('click','#3',function(event){
		event.preventDefault();
		console.log(event.location)
		console.log(this)
		
Swal.fire ({
		title: 'Deseas modificar el archivo?',
		text: "Exitos!",
		icon: 'warning',
		showCancelButton: true,
		confirmButtonColor: '#3085d6',
		cancelButtonColor: '#d33',
		confirmButtonText: 'Si, lo modifico!'

}).then(resultado => {
	if (resultado.value) {
		$("#3").submit();
		
	}
	else {
		console.log(" no se pudo ver el resultado");
	}

});
});
});