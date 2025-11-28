import json
import base64
import os
from dbr import *

folder_path = "/tmp/dynamsoft"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
# Sets a directory path for saving the license cache.
BarcodeReader.set_license_cache_path(folder_path)
error = BarcodeReader.init_license("DLS2eyJoYW5kc2hha2VDb2RlIjoiMjAwMDAxLTE2NDk4Mjk3OTI2MzUiLCJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSIsInNlc3Npb25QYXNzd29yZCI6IndTcGR6Vm05WDJrcEQ5YUoifQ==") #one-day public trial

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
        