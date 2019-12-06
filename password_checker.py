from tkinter import *
import requests
import hashlib


def request_api_data(query_data):
    """
    connects to api, sends part of hashed password and gets response of matching hashes
    """
    url = 'https://api.pwnedpasswords.com/range/' + query_data
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check and try again')
    return res


def read_response(response):
    """
    formats matches returned by api
    """
    result = response.text.splitlines()
    result = [i.split(':') for i in result]
    return result


def hashed_password_check(password):
    """
    compares password to data returned by api for matches
    """
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    split_response = read_response(response)
    for hashed in split_response:
        if hashed[0] == tail:
            return hashed[1]
    return 0


def check(password):

    count = hashed_password_check(password)
    if count:
        return f'Hacked {count} times, \nconsider changing it'
    else:
        return 'Not been hacked. \nCarry on!'


def submit_command():
    T1.delete('1.0', END)
    if password_text.get():
        result = check(password_text.get())
        T1.insert(END, result)
    else:
        T1.insert(END, 'Please enter a password')


window = Tk()
window.wm_title('Password Checker')


l1 = Label(window, text='Password')
l1.grid(row=0, column=0, pady=(20, 0), padx=(20, 0))

b1 = Button(window, text='Submit', width=12, command=submit_command)
b1.grid(row=2, column=0, pady=(20, 20), padx=(20, 0))
b1.config(background='DarkSeaGreen1', activebackground='lime green')

b2 = Button(window, text='Close', width=12, command=window.destroy)
b2.grid(row=2, column=1, pady=(20, 20), padx=(0, 20))
b2.config(background='IndianRed1', activebackground='red')

password_text = StringVar()
e1 = Entry(window, textvariable=password_text, show='*')
e1.grid(row=0, column=1, pady=(20, 0), padx=(0, 12))

T1 = Text(window, height=2, width=30)
T1.grid(row=1, column=0, columnspan=2, pady=(20, 0), padx=(20, 20))


window.mainloop()

