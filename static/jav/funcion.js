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

	$("#tabla").on('sumite','#for',function(event){
		event.preventDefault();
		console.log(event.target);
		
Swal.fire ({
		title: 'Deseas modificar el archivo?',
		text: "Exitos!",
		icon: 'warning',
		showCancelButton: true,
		confirmButtonColor: '#3085d6',
		cancelButtonColor: '#d33',
		confirmButtonText: 'Si, lo modifico!'
		
	  })

	});

});