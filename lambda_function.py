import json
import base64
from dbr import *
# Sets a directory path for saving the license cache.
folder_path = "/tmp/my-folder"
# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
BarcodeReader.set_license_cache_path(folder_path)
# Initialize license.
# The string "DLS2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSJ9" here is a free public trial license. Note that network connection is required for this license to work.
# You can also request a 30-day trial license in the customer portal: https://www.dynamsoft.com/customer/license/trialLicense?product=dbr&utm_source=samples&package=python
error = BarcodeReader.init_license("DLS2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSJ9")

def lambda_handler(event, context):
    try:
        if error[0] != EnumErrorCode.DBR_OK:
            return ("License error: "+ error[1])

        dbr = BarcodeReader()
        request_body = event["body"]
        base64_string = json.loads(request_body)["base64"]

        text_results = dbr.decode_base64_string(base64_string)
        result_dict = {}
        results = []

        if text_results != None:
            for tr in text_results:
                result = {}
                result["barcodeFormat"] = tr.barcode_format_string
                result["barcodeText"] = tr.barcode_text
                result["barcodeBytes"] = str(base64.b64encode(tr.barcode_bytes))[2:-1]
                result["confidence"] = tr.extended_results[0].confidence
                points = tr.localization_result.localization_points
                result["x1"] = points[0][0]
                result["y1"] = points[0][1]
                result["x2"] = points[1][0]
                result["y2"] = points[1][1]
                result["x3"] = points[2][0]
                result["y3"] = points[2][1]
                result["x4"] = points[3][0]
                result["y4"] = points[3][1]
                results.append(result)
        result_dict["results"] = results
        return {
            "statusCode": 200,
            "body": json.dumps(result_dict)
        }
        return 
    except BarcodeReaderError as bre:
        print(bre)
        return bre.error_info
        