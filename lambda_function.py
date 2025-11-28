import json
import base64
from dynamsoft_barcode_reader_bundle import *


DynamsoftLicense = "DLS2eyJoYW5kc2hha2VDb2RlIjoiMjAwMDAxLTE2NDk4Mjk3OTI2MzUiLCJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSIsInNlc3Npb25QYXNzd29yZCI6IndTcGR6Vm05WDJrcEQ5YUoifQ==" #one-day public trial

folder_path = "/tmp/dynamsoft"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

LicenseManager.set_license_cache_path(folder_path)
errorCode, errorMsg = LicenseManager.init_license(DynamsoftLicense)

def lambda_handler(event, context):
    if errorCode != EnumErrorCode.EC_OK and errorCode != EnumErrorCode.EC_LICENSE_CACHE_USED:
        return ("License error: "+ errorMsg)

    cvr_instance = CaptureVisionRouter()
    request_body = event["body"]
    base64_string = json.loads(request_body)["base64"]
    image_bytes = base64.b64decode(base64_string)
    result = cvr_instance.capture(image_bytes, EnumPresetTemplate.PT_READ_BARCODES.value)
    print(result)
    barcode_result = result.get_decoded_barcodes_result()
    result_dict = {}
    results = []

    if barcode_result != None:
        for br in barcode_result.get_items():
            result = {}
            result["barcodeFormat"] = br.get_format_string()
            result["barcodeText"] = br.get_text()
            result["barcodeBytes"] = str(base64.b64encode(br.get_bytes()))[2:-1]
            result["confidence"] = br.get_confidence()
            quad = br.get_location()
            points = quad.points
            result["x1"] = points[0].x
            result["y1"] = points[0].y
            result["x2"] = points[1].x
            result["y2"] = points[1].y
            result["x3"] = points[2].x
            result["y3"] = points[2].y
            result["x4"] = points[3].x
            result["y4"] = points[3].y
            results.append(result)
    result_dict["results"] = results
    return {
        "statusCode": 200,
        "body": json.dumps(result_dict)
    }

        