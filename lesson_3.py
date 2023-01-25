import time
from datetime import datetime as dt

host_path = r"D:\Development\Python\Pycharm\hosts"
website_list = ["www.netflix.com", "www.facebook.com", "www.google.ru"]
redirect = "127.0.0.1"

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 11) < dt.now() < \
            dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Rihanna")
        with open(host_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + '\n')
    else:
        print("Drake")
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                file.truncate()
    time.sleep(5)
