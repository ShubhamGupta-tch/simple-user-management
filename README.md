# Simple User Management

This is a website that manages Users, their Profiles and Allows them to view others Profile as well.<br>
<br>
##Underlying Principles:
- CRUD
- Password Management
- Authentication
- User Management
<br>

## How are Passwords Stored?
I am using the Password-Based Key Derivation Function 2 with Secure Hash Algorithm (pbkdf2_sha256) to store passwords securely.<br>
There are 180000 iterations with random salts. This all is used to create a very secure Hashed Password.<br>
This way, even the admin can not see the passwords of any user, hence promoting Password Privacy.

