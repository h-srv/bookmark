from flask import Flask
from health_check.api import check

# flas application
app = Flask(__name__)

# setup routes
app.add_url_rule(
    '/health',
    view_func=check,
    methods=['GET'])
