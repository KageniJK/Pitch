from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Pitch, User
from flask_login import login_required, current_user
from .forms import PitchForm, UpdateProfile
from .. import db, photos




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

    pitches = Pitch.query.filter_by(user_id=user.id).all()
    return render_template("profile/profile.html", user = user, pitches=pitches)


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


@main.route('/user/<uname>/update/pic', methods = ['POST'])
@login_required
def update_pic(uname):
    user= User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename= photos.save(request.files['photo'])
        path=f'profile_pics/{filename}'
        user.avatar = path
        db.session.commit()

    return redirect(url_for('main.profile', uname=uname))


@main.route('/new_pitch', methods=['GET', 'POST'])
@login_required
def new_pitch():
    """
    route to new pitch form
    :return:
    """
    form = PitchForm()

    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data

        fresh_pitch = Pitch(title=title, pitch_actual=pitch, user_id=current_user.id)

        fresh_pitch.save_pitch()

        return redirect(url_for('main.profile(current_user)'))
    title = 'New pitch'
    return render_template('new_pitch.html' , title=title, pitch_form=form, user = current_user)



