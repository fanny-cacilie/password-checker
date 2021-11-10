#  <b>PASSWORD CHECKER </b>


This application aims to check passwords using the Password API of <a href="https://haveibeenpwned.com/">Have I Been Pwned</a>.
<br><br>


# About the password API 


The API contains data that have been breached by hacker attacks or similars.
It stores close to 600.000 passwords in its database and verifies if your password appears in those lists.
And how many times it has been leaked.


The API works using the SHA1 hash and, in order to be as secure as possible, it does not send over the wire the real password or the entire SHA1 hash, that could be eventually decrypted.

The API uses the k-anonymity technique that can track your password without actually knowing it.
In this case, it uses the first five characters of the hashed password to check if matchables passwords have been breached.

<br><br>

# About the application


The current application reads the password written in a password.txt file, instead of variables or command-line arguments that can be stored in the computer logs, for example.

Then, it hashes the password into SHA1, separates the hashed password into head and tail, according to the API k-anonymity funtionality
and checks if password exists in API response

Once it is done, gets the count of leaks of the desired password by spliting the API response and communicate the user about it

You can notice that the script does not "see" or store your password during the proccess
And once the proccess is done, it cleans the password file for security.
    
<br><br>

# How to run:

* This application requires only python built-in modules<br>

1. Write the password you want to check in the password.txt file and save it<br><br>

2. In the current directory, run: <br>
``$ python3 check_password.py ``<br><br>

3. You will obtain a message including the count of the times your password was found in leaks<br><br>



# That's it!


* Change your password if it has been breched or carry on if it is (still) secure <br><br>

* Feel free to contribute to this project :)





