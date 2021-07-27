import requests
import random
import logging

PACKAGE_NAME = "Free"
X_AUTH_ID = "100155"
X_AUTH_KEY = "45c369183f978b5640027d04f06ea65e8074c293dfe5759d1effc26fefb58aec"
RSOCKS_URL = "https://rsocks.net/api/v1/file/get-proxy"

def get_proxies():
    proxy= random.choice([
        "http://Z3yq35SA:wRVNw7AS9DBxnQYc6n4qDqnajKqMUeYvq2OuWxrArekKGLpzDagz9GORJMXfTVYQdZ887-Z76FE98ON9@www.proxustr24.resi.ocu.privresi.com:47433",
        "http://Z3yq35SA:wRVNw7AS9DBxnQYc6n4qDqnajKqMUeYvq2OuWxrArekKGLpzDagz9GORJMXfTVYQdZ887-VknBIuxyST@ustr24.resi.ocu.privresi.com:47539",
        "http://Z3yq35SA:wRVNw7AS9DBxnQYc6n4qDqnajKqMUeYvq2OuWxrArekKGLpzDagz9GORJMXfTVYQdZ887-JocyaxVJYa@ustr24.resi.ocu.privresi.com:43592",
        "http://Z3yq35SA:wRVNw7AS9DBxnQYc6n4qDqnajKqMUeYvq2OuWxrArekKGLpzDagz9GORJMXfTVYQdZ887-Dnt68G5KNt@ustr24.resi.ocu.privresi.com:44298",
        "http://Z3yq35SA:wRVNw7AS9DBxnQYc6n4qDqnajKqMUeYvq2OuWxrArekKGLpzDagz9GORJMXfTVYQdZ887-WlAvC0qXRV@ustr24.resi.ocu.privresi.com:47162",
        "http://Z3yq35SA:wRVNw7AS9DBxnQYc6n4qDqnajKqMUeYvq2OuWxrArekKGLpzDagz9GORJMXfTVYQdZ887-ddmbOeQhGW@ustr24.resi.ocu.privresi.com:39284",
        "http://Z3yq35SA:wRVNw7AS9DBxnQYc6n4qDqnajKqMUeYvq2OuWxrArekKGLpzDagz9GORJMXfTVYQdZ887-Q2Di2TFPWr@ustr24.resi.ocu.privresi.com:47627",
        "http://Z3yq35SA:wRVNw7AS9DBxnQYc6n4qDqnajKqMUeYvq2OuWxrArekKGLpzDagz9GORJMXfTVYQdZ887-TZi1ZnIHdZ@ustr24.resi.ocu.privresi.com:47465",
        "http://Z3yq35SA:wRVNw7AS9DBxnQYc6n4qDqnajKqMUeYvq2OuWxrArekKGLpzDagz9GORJMXfTVYQdZ887-gcHLeK4txO@ustr24.resi.ocu.privresi.com:42207",
        "http://Z3yq35SA:wRVNw7AS9DBxnQYc6n4qDqnajKqMUeYvq2OuWxrArekKGLpzDagz9GORJMXfTVYQdZ887-HUFdmUdo3G@ustr24.resi.ocu.privresi.com:39178",
        ""
    ])
    
    if proxy == "":
        return {}
    return {"http": proxy}
    # headers = {
    #     "X-Auth-ID": X_AUTH_ID,
    #     "X-Auth-Key": X_AUTH_KEY
    # }
    # response = requests.post(RSOCKS_URL, headers=headers)
    # result = response.json()
    # if 'result' in  result and result['result'] == True:
    #     for key in result["packages"]:
    #         if result["packages"][key]["name"] == PACKAGE_NAME:
    #             return {
    #                 "https": "https://{}".format(random.choice(result["packages"][key]["ips"]))
    #             }
    # return {}

if __name__ == "__main__":
    print(get_proxies())
