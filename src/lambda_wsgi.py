import base64
import os
import sys
from io import BytesIO, StringIO
from urllib.parse import urlencode, urlparse


# Convert bytes to str, if required
def convert_str(s):
    try:
        return s.decode("utf-8")
    except UnicodeDecodeError:
        return s


def response(app, event, context):
    sr = StartResponse()
    output = app(environ(event, context), sr)
    return sr.response(output)


class StartResponse:
    def __init__(self):
        self.status = 500
        self.headers = []
        self.body = StringIO()

    def __call__(self, status, headers, exc_info=None):
        self.status = status.split()[0]
        self.headers[:] = headers
        return self.body.write

    def response(self, output):
        print(f"StartResponse.{__name__} Invoked with payload:: {output}")
        headers = dict(self.headers)
        print(f"StartResponse.{__name__} Invoked with headers:: {output}")
        if headers.get("Content-Type") in [
            "image/png",
            "image/gif",
            "application/octet-stream",
        ]:
            is_base64 = True
            body = base64.b64encode(b"".join(output)).decode("ascii")
        else:
            is_base64 = False
            body = self.body.getvalue() + "".join(map(convert_str, output))
        return {
            "statusCode": int(self.status),
            "headers": headers,
            "body": body,
            "isBase64Encoded": is_base64,
        }


def process_event(event):
    return {
        "request_body_args": {},
        "request_method": event["requestContext"]["httpMethod"],
        "request_uri": event["requestContext"]["path"],
        "request_body": "",
        "request_body_base64": True,
        "request_headers": {
            "host": "localhost:8000",
            "cookie": "",
            "connection": "close",
            "accept-language": "en-US,en;q=0.9,hi;q=0.8",
            "upgrade-insecure-requests": "1",
            "accept-encoding": "gzip, deflate, br",
            "sec-fetch-mode": "navigate",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        },
        "request_uri_args": {},
    }


def environ(event, context):
    print("orgi event ", event)
    event = process_event(event=event)
    print("process event ", event)
    body = b""
    str_body = event.get("request_body")
    if str_body:
        body = bytes(str_body, "utf-8")

    # Parse Request Path
    url_parsed = urlparse(event["request_uri"])
    request_path = url_parsed.path
    strip_path = os.environ.get("STRIP_PATH", None)
    if strip_path and (
        request_path.startswith(
            strip_path) or request_path.startswith("/" + strip_path)
    ):
        request_path = request_path.replace(strip_path, "", 1)

    environ = {
        "REQUEST_METHOD": event["request_method"],
        "SCRIPT_NAME": "",
        "PATH_INFO": request_path,
        "QUERY_STRING": urlencode(event["request_uri_args"] or {}),
        "REMOTE_ADDR": "127.0.0.1",
        "CONTENT_LENGTH": str(len(body) or ""),
        "HTTP": "on",
        "HTTPS": "on",
        "SERVER_NAME": "test-django",
        "SERVER_PROTOCOL": "HTTP/1.1",
        "wsgi.version": (1, 0),
        "wsgi.url_scheme": "https",
        "wsgi.input": BytesIO(body),
        "wsgi.errors": sys.stderr,
        "wsgi.multithread": False,
        "wsgi.multiprocess": False,
        "wsgi.run_once": False,
    }
    headers = event.get("request_headers", {})
    if headers:
        for k, v in headers.items():
            k = k.upper().replace("-", "_")

            if k == "CONTENT_TYPE":
                environ["CONTENT_TYPE"] = v
            elif k == "HOST":
                environ["SERVER_NAME"] = "https://" + v
            elif k == "X_FORWARDED_FOR":
                environ["REMOTE_ADDR"] = v.split(", ")[0]
            elif k == "X_FORWARDED_PROTO":
                environ["wsgi.url_scheme"] = v
            elif k == "X_FORWARDED_PORT":
                environ["SERVER_PORT"] = v

            environ["HTTP_" + k] = v

    return environ
