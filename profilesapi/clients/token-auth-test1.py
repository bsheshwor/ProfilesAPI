import requests

def client():
    token_h = "Token e953479a16ef9c3d6744dba39ad08ddf65e34fa2"

    # credentials = {'username':'bshesh', 'password':'neupane1234'}

    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)

    headers = {"Authorization": token_h}

    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)
    print("Status Code: ", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()