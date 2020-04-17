<?php
session_start();
$con = mysqli_connect('localhost', 'root', 'mysql','test');
$id = $_GET['id'];
$pw = $_GET['pw'];
$query = "select * from test where id='$id'";
$result = mysqli_query($con,$query);
$rows = mysqli_fetch_assoc($result);
if(mysqli_num_rows($result)==1){ ?>

	<script>
                alert("Error");
                location.replace("./register.html");
        </script>

        <?php 
}
else{
 
	$query = "insert into test (id,pw) values('$id', '$pw')";
	$result = mysqli_query($con,$query);
	?>
	<script>
		alert("success");
		location.replace("./test.html");
	</script>
<?php }
?>

