from flask import render_template
from . import main


@main.route('/')
def index():
    """
    Display the landing page
    :return:
    """

    title = 'Home - Pitch'

    return render_template('index.html', title=title)
