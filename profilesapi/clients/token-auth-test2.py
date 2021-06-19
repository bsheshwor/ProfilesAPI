import requests

def client():

    # data = {
    #     'username':'sister', 
    #     'email': 'sister@gmail.com',
    #     'password1':'neupane1234',
    #     'password2':'neupane1234'}

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/", data=data)

    # print("Status Code: ", response.status_code)
    # response_data = response.json()
    # print(response_data)

    token_h = "Token 727b495ad0f9553b63e438d058a86ac402ca0b70"

    headers = {"Authorization": token_h}

    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)
    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()