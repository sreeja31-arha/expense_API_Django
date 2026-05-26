def success_response(message, data=None, status_code=200):
    response = {
        "status": "success",
        "message": message,
    }
    if data is not None:
        response["data"] = data
    return response

def error_response(message, errors=None):
    response = {
        "status": "error",
        "message": message,
    }
    if errors is not None:
        response["errors"] = errors
    return response