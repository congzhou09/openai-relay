from flask import Flask, request, Response
import requests
from libs.logger import logger


app = Flask(__name__)
OPENAI_BASE_URL = "https://api.openai.com/v1"


@app.before_request
def proxy():
    method = request.method
    path = request.full_path
    data = request.get_data().decode('utf-8')
    mimetype = request.mimetype
    headers = {"Content-Type": mimetype}
    authorization = request.authorization
    token = "invalid token."
    if authorization is not None and authorization.token is not None:
        token = authorization.token
    else:
        logger.error(token)

    # test value
    # method = "POST"
    # path = '/chat/completions?'
    # data = '{"messages": [{"role": "user", "content": "Say this is a test"}, {"role": "user", "content": "What is my last question."}], "stream": false, "max_tokens": 3986, "model": "gpt-3.5-turbo", "n": 1, "temperature": 0.5, "frequency_penalty": 0, "presence_penalty": 0}'
    # mimetype = 'application/json'
    # headers = {"Content-Type": mimetype}
    # token = 'sess-geKtJdf5z1NtMr72tnsWOeQuZdZlMFtP7jEwc44k'

    res = {"status_code": 400, "reason": f"unanticipated method {method}"}
    res = requests.request(
        method=method,
        url=OPENAI_BASE_URL + path,
        headers=headers,
        data=data,
        auth=(str('bearer'), token),
    )

    return Response(response=res.content, status=res.status_code, headers=res.headers)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    print(request)
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run(port=8885)
