$(function(){
    $("#tabla").on('click','#1',function(event){
		event.preventDefault();
		
    Swal.fire ({
		title: 'Deseas modificar el archivo?',
		text: "Exitos!",
		icon: 'warning',
		showCancelButton: true,
		width:'18em',
		confirmButtonColor: '#3085d6',
		cancelButtonColor: '#d33',
		confirmButtonText: 'Si, lo modifico!',
		preConfirm:()=>{
			location.href=event.target.href;

		}
		
	  })

	});

	
	$("#tabla").on('click','#2',function(event){
		event.preventDefault();
				
    Swal.fire ({
		title: 'Deseas ELIMINAR el archivo?',
		text: "Si lo eliminas no hay vuelta atrás!",
		icon: 'error',
		iconColor:'red',
		width:'18em',
		showCancelButton: true,
		confirmButtonColor: '#3085d6',
		cancelButtonColor: '#d33',
		confirmButtonText: 'Si, lo elimino!',
        preConfirm:()=>{
	        location.href=event.target.href;
            }
    });
    });
	$("#tabla").on('click','#3',function(event){
		event.preventDefault();
				
    Swal.fire ({
		title: 'Deseas GUARDAR el archivo?',
		text: "Si !",
		icon: 'error',
		iconColor:'green',
		width:'18em',
		showCancelButton: true,
		confirmButtonColor: '#3085d6',
		cancelButtonColor: '#d33',
		confirmButtonText: 'Si',
        preConfirm:()=>{
	        location.href=event.target.href;
            }
    });
    });
	
	});
	
		
	
		

	
	    


