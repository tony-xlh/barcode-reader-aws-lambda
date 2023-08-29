# barcode-reader-aws-lambda

Run Dynamsoft Barcode Reader on AWS Lambda and provide a serverless barcode reading API.

## API Specification

Request:

```json
{
  "base64":"<base64-encoded-image>"
}
```

Response:

```json
{"results": 
  [
    {
      "barcodeFormat": "QR_CODE", 
      "barcodeText": "https://www.dynamsoft.com",
      "barcodeBytes": "aHR0cHM6Ly93d3cuZHluYW1zb2Z0LmNvbQ==",
      "confidence": 82,
      "x1": 7,
      "y1": 7,
      "x2": 93,
      "y2": 6,
      "x3": 94,
      "y3": 94,
      "x4": 6,
      "y4": 93
    }
  ]
}
```



## How to Set up the Lambda Function and Add an API Gateway Trigger

1. In your AWS, create a new Lambda function. Choose Python as the runtime.
2. Create a layer to include the package of Dynamsoft Barcode Reader. You can download the manylinux wheel of Dynamsoft Barcode Reader from [here](https://pypi.org/project/dbr/#files), unzip it into a folder named `python` and package it as a zip for uploading.
3. Update the `lambda_function.py` file with this repo's.
4. Create an API gateway trigger for this function so that we can call the function through HTTP requests.

## License Application

A license is required to use Dynamsoft Barcode Reader. You can apply for one [here](https://www.dynamsoft.com/customer/license/trialLicense?product=dbr).





