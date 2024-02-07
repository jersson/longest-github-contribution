from flask import Flask, jsonify, render_template

from src.infrastructure.github_client import GitHubClient
from src.infrastructure.html_parser import HtmlParser

app = Flask(__name__)


@app.route("/longest-contribution/<username>", methods=["GET"])
def longest_contribution(username=None):
    parser = HtmlParser()
    client = GitHubClient(parser)
    contributions = client.longest_contribution(username)

    return jsonify(contributions)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
