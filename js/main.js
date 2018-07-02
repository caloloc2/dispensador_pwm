$(document).ready(function(){
	Obtener_Horarios();
})

function Obtener_Horarios(){
	$.ajax({
		url: 'php/obtener_horarios.php',		
		dataType: 'json',
		success: function(datos) {
			//console.log(datos);
			if (datos['estado']){
				document.getElementById('horario1').value = datos['dato'][0];
				document.getElementById('horario2').value = datos['dato'][1];
				document.getElementById('horario3').value = datos['dato'][2];
			}
		},
		error:function(e){
			console.log(e.responseText);
		}
	});
}

$('#horarios').submit(function(){
	$.ajax({
		url: 'php/configurar_horarios.php',		
		dataType: 'json',
		data: {
			horario1: document.getElementById('horario1').value,
			horario2: document.getElementById('horario2').value,
			horario3: document.getElementById('horario3').value,
		},
		type: 'POST',
		success: function(datos) {
			//console.log(datos);
			if (datos['estado']){
				$('#mensaje').fadeIn(150);
				setTimeout(function(){
					$('#mensaje').fadeOut(150);
				}, 2500)

				Obtener_Horarios();
			}
		},
		error:function(e){
			console.log(e.responseText);
		}
	});
	return false;
})