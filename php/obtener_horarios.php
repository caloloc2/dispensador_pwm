<?php 

$respuesta['estado'] = false;

try{
	require 'funciones.php';

	$respuesta['dato'] = split("/", Lee());
	$respuesta['estado'] = true;

}catch(Exception $e){
	$respuesta['error'] = $e->getMessage();
}

echo json_encode($respuesta);