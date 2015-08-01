<?php
$salt = "JosefManu";
//print_r(hash_algos());
//print_r($_SERVER['SERVER_ADDR']);
$hashed_score = hash("sha224", $_GET['score'].$salt);
if($hashed_score === $_GET['hash']) {
	//print "passt!";
	$file = file_get_contents("highscore");
	$hs = unserialize($file);
	print_r($hs);
	if (!is_array($hs)) {
		$hs = Array();
	}
	
	$hs[microtime()] = Array('score' => $_GET['score'], 'ip' => $_SERVER['SERVER_ADDR'], 'name' => $_GET['hname']);

	$hs_serialized = serialize($hs);

	//print_r($hs_serialized);

	file_put_contents("highscore",$hs_serialized);

} else {
	print "noo!";
}
//echo $hashed_score;
