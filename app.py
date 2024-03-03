import os

from flask import Flask, render_template, request, send_file

flaskapp = Flask(__name__)

@flaskapp.route("/")
def index():
    htmlret = ""
    print(os.listdir())
    for x in os.listdir():
        htmlret = htmlret + f"<a href=\"/download?filename={x}\">{x}</a><br>"
    print(htmlret)
    return htmlret

@flaskapp.route("/download", methods=["GET"])
def download():
    return send_file("./" + request.args["filename"], as_attachment=True)

def main():
    flaskapp.run(host="0.0.0.0", port=5000, debug=True)

if __name__ == "__main__":
    main()