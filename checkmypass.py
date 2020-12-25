import requests
import hashlib
import sys

def request_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res


def my_pass(hashes, to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for hash, count in hashes:
        if hash == to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1pass[:5], sha1pass[5:]
    response = request_data(first5)
    return my_pass(response, tail)


def main(args):
    count_list = []
    for password in args:
        count_list.append(pwned_api_check(password))

    for count, password in zip(count_list, args):
        if not count:
            print(f'Good news "{password}" wasn\'t found.')
        else:
            print(f'{password} has been used {count} times, you should change it')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        check = input('Enter the password you want to check: ')
        c = pwned_api_check(check)
        if c:
            print(f'{check} has been used {c} times, you should change it')
        else:
            print(f'Good news "{check}" wasn\'t found.')
    else:
        main(sys.argv[1:])
