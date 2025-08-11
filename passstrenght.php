<?php
// Repository: php-password-hasher
// New Feature: Verify password strength

function isStrongPassword($password) {
    return strlen($password) >= 8 &&
           preg_match('/[A-Z]/', $password) &&
           preg_match('/[a-z]/', $password) &&
           preg_match('/[0-9]/', $password) &&
           preg_match('/[^a-zA-Z0-9]/', $password);
}

$password = "SecurePass123!";
if (isStrongPassword($password)) {
    echo "Password is strong.";
} else {
    echo "Password is weak.";
}
?>
