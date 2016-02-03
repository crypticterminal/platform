import traceback
import sys
import convertible
from flask import Flask, jsonify, send_from_directory, request, Response
from syncloud_app.main import PassthroughJsonError

from syncloud_platform.di.injector import get_injector
from syncloud_platform.rest.facade.common import rest_prefix, html_prefix
from syncloud_platform.rest.flask_decorators import nocache

injector = get_injector()
internal = injector.internal
device = injector.device

app = Flask(__name__)


@app.route(html_prefix + "/<path:filename>")
@nocache
def static_file(filename):
    return send_from_directory(internal.www_dir, filename)


@app.route(rest_prefix + "/id", methods=["GET"])
def identification():
    return jsonify(success=True, message='', data=convertible.to_dict(internal.identification())), 200


@app.route(rest_prefix + "/activate", methods=["POST"])
def activate():

    # TODO: validation

    main_domain = None
    if 'main_domain' in request.form:
        main_domain = request.form['main_domain']

    if main_domain is None:
        main_domain = "syncloud.it"

    internal.activate(
        request.form['redirect_email'],
        request.form['redirect_password'],
        request.form['user_domain'],
        request.form['device_username'],
        request.form['device_password'],
        main_domain
    )
    return identification()


@app.route(rest_prefix + "/send_log", methods=["GET"])
def send_log():
    device.send_logs()
    return jsonify(success=True), 200


@app.errorhandler(Exception)
def handle_exception(error):
    status_code = 500
    if isinstance(error, PassthroughJsonError):
        return Response(error.json, status=status_code, mimetype='application/json')
    else:
        print '-'*60
        traceback.print_exc(file=sys.stdout)
        print '-'*60
        return jsonify(message=error.message), status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)
