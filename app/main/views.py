from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Pitch, User
from flask_login import login_required, current_user
from .forms import PitchForm, UpdateProfile



@main.route('/')
def index():
    """
    Display the landing page
    :return:
    """

    title = 'Home - Pitch'

    return render_template('index.html', title=title)


@main.route('/user/<uname>')
def profile(uname):
    """
    display user profiles
    :param uname:
    :return:
    """
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update', methods = ['GET', 'POST'])
@login_required
def update_profile(uname):
    """
    update user profiles
    :param uname:
    :return:
    """
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)


    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio =  form.bio.data


        db.session.add(user)
        db.session.commit()


        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form = form)


