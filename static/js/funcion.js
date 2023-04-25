//#region const btnentrar = document.querySelectorAll('.btn-yo')
//#region console.log(btnentrar);

//#region if (btnentrar) {
   //#region const btnArray = Array.from(btnentrar);
    //#region ##  });
       //#region  });
   //#region  }


    /*window.addEventListener("load", cargaPagina);
    function cargaPagina() {
        var btn = document.getElementById("verificar").addEventListener("click", cambia_valores_abl);
        var btn1 = document.getElementById("verificar1").addEventListener("click", cambia_valores_aysa);
        var btn2 = document.getElementById("verificar2").addEventListener("click", cambia_valores_seguro);
        btn="";
        btn1="";
        btn2="";
    }*/
    function cambia_valores_abl(){
       
       var checkabl= document.getElementById("chekabl").checked;
        if (checkabl==0){
       document.getElementById("abl").value="0";
        
        }
           
        } 
    function cambia_valores_aysa(){
        
        var checkaysa= document.getElementById("checkaysa").checked;
         if (checkaysa ==0){
             aysa=document.getElementById("aysa").value="0";
            alert (aysa);
         } 
     } 

    /* function cambia_valores_seguro(){
        
        var checkseguro= document.getElementById("checkseguro").checked;
         if (checkseguro ==0){
             seguro=document.getElementById("seguro").value="0";
 
         } 
     }*/
     
    /*function validar_documento(){
    var validacion= document.forms["miform"]["chekabl"].checked;
    if (validacion == true)
    {
       getElementById("abl").innerHTML= "Jrecibo2.abl";
       return false
    }
    else{
        getElementById("abl").innerHTML= "0";
        return false
    }


    }*/