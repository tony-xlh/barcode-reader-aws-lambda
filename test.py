import base64
import json
import requests

endpoint = "" #like https://*****.execute-api.us-east-2.amazonaws.com/default/BarcodeReader

def get_picture_base64_data(image_path):
    with open(image_path, 'rb') as image_file:
        base64_data = base64.b64encode(image_file.read())
    return base64_data.decode('utf-8')
    
def decode():
    base64 = get_picture_base64_data("./sample_qr.png")
    body = {"base64": base64}
    json_data = json.dumps(body)
    headers = {'Content-type': 'application/json'}
    r = requests.post(endpoint, data=json_data, headers=headers)
    print(r.json())

def get_endpoint_from_cli():
    print("Please input the endpoint:")
    global endpoint
    endpoint = input()

if __name__ == "__main__":
    if endpoint == "":
        get_endpoint_from_cli()
    decode()