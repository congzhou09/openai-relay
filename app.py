from flask import Flask, request, Response
import requests
from libs.logger import logger


app = Flask(__name__)
OPENAI_BASE_URL = "https://api.openai.com/v1"


@app.before_request
def proxy():
    method = request.method
    path = request.full_path
    data = request.get_data()
    params = request.args
    headers = {"Content-Type": request.content_type}
    authorization = request.authorization
    token = "invalid token."
    if authorization is not None and authorization.token is not None:
        token = authorization.token
    else:
        logger.error(token)

    isStream = False
    if request.json is not None and type(request.json["stream"]) is bool:
        isStream = request.json["stream"]

    res = requests.request(
        method=method,
        url=OPENAI_BASE_URL + path,
        headers=headers,
        data=data,
        auth=(str('bearer'), token),
        stream=isStream,
    )

    # res_headers = list(res.headers)
    # final_headers = {}
    # for one_header in res_headers:
    #     final_headers[one_header] = res.headers[one_header]
    final_headers = res.headers.items()

    if isStream:
        return Response(
            response=res.iter_content(chunk_size=1024),
            status=res.status_code,
            headers=final_headers,
        )
    else:
        return Response(
            response=res.content,
            status=res.status_code,
        )


# @app.route("/", methods=["GET", "POST"])
# def hello_world():
#     print(request)
#     return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(port=8885, host="0.0.0.0")
