<?php
// Repository: php-password-hasher
// Description: A script to securely hash and verify passwords using PHP's password_hash().

// Password hashing and verification
$password = "securepassword123";

// Hash the password
$hashedPassword = password_hash($password, PASSWORD_BCRYPT);
echo "Hashed Password: $hashedPassword\n";

// Verify the password
$inputPassword = "securepassword123";
if (password_verify($inputPassword, $hashedPassword)) {
    echo "Password is valid!";
} else {
    echo "Invalid password!";
}
?>
