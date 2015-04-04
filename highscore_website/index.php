<?php
//print_r(hash_algos());
//print_r($_SERVER['SERVER_ADDR']);
	$file = file_get_contents("highscore");
	$hs = unserialize($file);
	//print_r($hs);
    
    foreach ($hs as $time => $score) {
        $time_strings = explode(' ', $time);
        
        $hs[$time]['seconds'] = $time_strings[1];
        $hs[$time]['miliseconds'] = $time_strings[0];
    
        $score_value[$time] = $score['score'];
        $score_seconds[$time] = $time_strings[1];
    }
    
    array_multisort($score_value, SORT_DESC, $score_seconds, SORT_DESC, $hs);

    $pos = 1;

    foreach ($hs as $key => $score_entry) {
        
        $hs[$key]['pos'] = $pos;
        $score_seconds_2[$key] = $score_entry['seconds'];
        $pos++;
    }

    $hs_time = $hs;
    array_multisort($score_seconds_2, SORT_DESC, $hs_time);
    
	//foreach($hs as $score) {
	//	echo $score['score'] . ' - ' . $score['ip'] . ' - ' . $score['name']  .  '</br>'; 
	//}
?>
<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title></title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- Place favicon.ico and apple-touch-icon.png in the root directory -->

		<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <!--[if lt IE 7]>
            <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->

        <!-- Add your site or application content here -->
        
        <div class="container">
            
        <h1>Party Hard Highscore</h1>
        
        <div class="row">
            
        <div class="col-md-6">
        <h2>Highest Scores</h2>
        <table class="table">
        <thead>
	        <tr>
	            <th>Position</th>
	        	<th>Score</th>
	        	<th>Time</th>
	        	<th>HostName</th>
	        </tr>
        </thead>

		<?php

			foreach($hs as $score) {
			    
				echo "<tr>";
				echo '<td>' . $score['pos']
				. ' </td><td> ' . $score['score'] 
				. ' </td><td> ' . date('r', $score['seconds']) 
				. ' </td><td> ' . $score['name']  .  '</td>'; 
				echo "</tr>";

			}
    
		
		?>

		</table>
		</div>


        <div class="col-md-6">
        <h2>Newest Entries</h2>
        <table class="table">
        <thead>
	        <tr>
	            <th>Position</th>
	        	<th>Score</th>
	        	<th>Time</th>
	        	<th>HostName</th>
	        </tr>
        </thead>

		<?php

			foreach($hs_time as $score) {
			    
				echo "<tr>";
				echo '<td>' . $score['pos']
				. ' </td><td> ' . $score['score'] 
				. ' </td><td> ' . date('r', $score['seconds']) 
				. ' </td><td> ' . $score['name']  .  '</td>'; 
				echo "</tr>";

			}
    
		
		?>

		</table>
		</div>
		
		
		</div>
		</div>
        <!-- Google Analytics: change UA-XXXXX-X to be your site's ID. -->
        <script>
            (function(b,o,i,l,e,r){b.GoogleAnalyticsObject=l;b[l]||(b[l]=
            function(){(b[l].q=b[l].q||[]).push(arguments)});b[l].l=+new Date;
            e=o.createElement(i);r=o.getElementsByTagName(i)[0];
            e.src='//www.google-analytics.com/analytics.js';
            r.parentNode.insertBefore(e,r)}(window,document,'script','ga'));
            ga('create','UA-XXXXX-X');ga('send','pageview');
        </script>
    </body>
</html>

<?php


//print_r($hs);
//ksort($new_hs);
//print_r($new_hs);