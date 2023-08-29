import base64
import json
import requests

def get_picture_base64_data(image_path):
    with open(image_path, 'rb') as image_file:
        base64_data = base64.b64encode(image_file.read())
    return base64_data.decode('utf-8')
    
def decode():
    base64 = get_picture_base64_data("./sample_qr.png")
    body = {"base64": base64}
    json_data = json.dumps(body)
    headers = {'Content-type': 'application/json'}
    print(json_data)
    r = requests.post('https://toln285pca.execute-api.us-east-2.amazonaws.com/default/BarcodeReader', data=json_data, headers=headers)
    print(dir(r))
    print(r.json())


if __name__ == "__main__":
    decode()