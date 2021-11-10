import hashlib
import os
import requests
import sys

path = os.getcwd() + '/password.txt'

def get_api_data(query_char):
    # Receive the 5 initial char of the hashed password
    # Return a list of the tails of passwords that matches the initial chars
    # And also return the count of how many times the password was found in leaks
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again.')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    # Get the count of leaks by spliting the API response
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def check_pwned_password(password):
    # Hash the password into SHA1 
    # Separate the hashed password in head and tail, according to the API
    # Check if password exists in API response
    password_sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    sha1_head, sha1_tail = password_sha1[:5], password_sha1[5:]
    response = get_api_data(sha1_head)
    return get_password_leaks_count(response, sha1_tail)


def read_password_file():
    # Read the password written in the password.txt file
    with open(path, 'r') as f:
        data = f.read()
    return data


def main(password):
    # Get the count of leaks of the desired password
    # Communicate the user about it
    # Clean the password file for security
    # End the process
    count = check_pwned_password(password)
    if count:
        print(f'Current password was found {count} times, you should probably change it.')
    else:
        print('Password not found in leaks lists. Carry on!')

    with open(path, "w") as f:
        f.write("")
    return 'Done!'


if __name__ == '__main__':
    sys.exit(main(read_password_file()))
