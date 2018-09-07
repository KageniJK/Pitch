from flask import render_template


@main.route('/')
def index():
    """
    Dispay the landing page
    :return:
    """

    title = 'Home - Pitch'

    return render_template('index.html', title=title)