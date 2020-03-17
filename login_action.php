<?php
session_start();
$con = mysqli_connect('localhost', 'root', 'mysql','test');
$id = $_GET['id'];
$pw = $_GET['pw'];
$query = "select * from test where id='$id'";
$result = mysqli_query($con,$query);
$rows = mysqli_fetch_assoc($result);
if(mysqli_num_rows($result)==1){
	
	if($rows['pw']==$pw){ 
	$_SESSION['id']=$id;
	?>
	<script>
                alert("Success!!");
                location.replace("./index.php");
        </script>
	<?php}
	else{ ?>
        <script>
                alert("Invaild PW!!");
                location.replace("./test.html");
        </script>

	<?php }
}
else{ ?>
	<script>
		alert("Invaild ID!!");
		location.replace("./test.html");
	</script>
<?php }

?>
