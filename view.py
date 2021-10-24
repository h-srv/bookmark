from flask import current_app as app

def health_check():
    return {}