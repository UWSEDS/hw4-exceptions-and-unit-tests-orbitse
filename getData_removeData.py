""" Erin Orbits, DATA 515: Hmk 4
Note: I was having trouble using unittest in PyCharm and having trouble using urllib3
"""
import urllib3 # currently unused, but I did use it
import os  # the "os" module has useful operating system stuff
import requests

def get_data(url):
    # check if file exists
    filename = os.path.basename(url)
    # http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED')
    if os.path.isfile(filename): # Return True if path or path-like object is an existing regular file
        print("File already {} exists".format(filename))
        return("File already exists")
    else:
        # check if valid url
        # standardize url, wanted to add http: and/or www but had problems
        # url = url.lower()
        # if url[0:3] != "http":
        #     url = "http://" + url
        # else:
        #     url = url
        # making a request means pinging a website or portal for information
        req = requests.get(url)
        # not sure if it's better to use: req = http.request('GET', url, retries=False)
        # boolean response attribute req.ok
        if req.ok:
            with open(filename, 'wb') as f:
                f.write(req.content)
            print("File {} downloaded".format(filename))
            return("File downloaded")
        else:
            return ("Invalid url")
    # try:
    #     req = requests.get(url)
    #     # req = http.request('GET', url, retries=False)
    #     # boolean response attribute req.ok
    #     if req.ok == True:
    #         with open(filename, 'wb') as f:
    #             f.write(req.content)
    #         print("File {} downloaded".format(filename))
    #         return("File downloaded")
    # except requests.exceptions.MissingSchema as badurl:
    #     return ("Invalid url")

    # except:
    #     return ("Invalid url")
        # get the current status code of a portal with the response code dictionary look-up object
        #print("Invalid url, requests status code is {}" % req.status_code)



def remove_data(url):
    filename = os.path.basename(url)
    if os.path.exists(filename):
        # if the file is open when try to remove, results in error
        # but when I tried to close the file, I got an error
        # filename.close()
        # os.close(filename)
        # if os.open(filename):
        os.remove(filename)
        print("File {0} was removed.".format(filename))
        return ("File removed")
    else:
        print("File {0} does not exist".format(filename))
        return("File doesn't exist")

if __name__ == "__main__":
    user_url = str(input("Enter data url or copy default url \n {}: ".format(
        'https://data.seattle.gov/resource/4xy5-26gy.csv'))).upper()
    get_data(user_url)
    remove_data(user_url)

# if __name__ == "__main__":
#     # print("----------------------------------------------------------------")
#     # user_url = str(input("Enter data url or D to use default url \n {}: ".format(
#     #     'https://data.seattle.gov/resource/4xy5-26gy.csv'))).upper()
#     # print("----------------------------------------------------------------")
#     # get_data(user_url)
#     # remove_data(user_url)
#     print("----------------------------------------------------------------")
#     user_url = str(input("Enter data url or copy the default url \n {}: ".format(
#         'https://data.seattle.gov/resource/4xy5-26gy.csv'))).upper()
#     choice = int(input("Enter 0 to download file or 1 to delete file: "))
#     print("----------------------------------------------------------------")
#     if choice == 0:
#         get_data_result = get_data(user_url)
#     elif choice == 1:
#         remove_data_result = remove_data(user_url)
#     else:
#         __name__ == "__main__"