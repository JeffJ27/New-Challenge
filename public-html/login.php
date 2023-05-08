<?php

if(isset($_POST['user']) && isset($_POST['pass'])) 
{
  $username = $_POST['user'];
  $password = $_POST['pass'];

  if($username == 'admin' && $password == 'futuristic') 
  {
    // Successful login - set a session variable and redirect to the home page
    session_start();
    $_SESSION['username'] = $username;
    header('Location: flagpage.html');
    exit();
  } 
  else 
  {
    // Incorrect username or password - display an error message
    $errorMessage = 'Incorrect username or password';
  }
}

//reorderT415N0w
//carnegiemellon
//picoctfpass
//Cy1abAfr1cA
//cyLabU5At35T
//hungergames2
//washedtools
//piratesofafrica
//thisisamzing
//CongRaTSUw0N
//5tArwAr5PaSs
//fuTu415t1C
//CArn3g1Em3LL0nuN1vEr51tY
//alB37rTp45aRK1ARenA
//J3ryT3k7TYggT7D3WadU1i

?>
