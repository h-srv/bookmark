from flask import Flask
import view

# flas application
app = Flask(__name__)

# setup routes
app.add_url_rule('/health',
    view_func=view.health_check,
    methods=['GET'])
