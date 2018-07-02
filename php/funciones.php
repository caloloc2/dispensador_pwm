<?php 

function Escribe($dato){
	$dato = $dato['horario1']."/".$dato['horario2']."/".$dato['horario3'];
	$fp = fopen("../horarios.rasp", "w");
	fputs($fp, $dato);
	fclose($fp);

	return true;
}

function Lee(){
	$fp = fopen("../horarios.rasp", "r+");
	$dato = fgets($fp);
	fclose($fp);

	return $dato;
}