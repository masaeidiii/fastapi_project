import requests


def get_all_item():
    url = "http://127.0.0.1:8000/getall/"

    response = requests.get(url)

    if response.status_code!= 200:
        return 'error'
    else:
        response = response.json()
        return response


def add_item(new_item):
    url = f"http://127.0.0.1:8000/add/{new_item}"
    response = requests.post(url)
    if response.status_code != 200 :
        return 'error'
    else:
        response = response.json()
        return response








     
if __name__ == '__main__':
    #print(get_all_item())
    print(add_item(500))# خط 16