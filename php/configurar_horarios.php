<?php 

$respuesta['estado'] = false;

try{
	require 'funciones.php';

	$datos = $_POST;
	
	$respuesta['estado'] = Escribe($datos);

}catch(Exception $e){
	$respuesta['error'] = $e->getMessage();
}

echo json_encode($respuesta);