from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Pitch, User, Comment
from flask_login import login_required, current_user
from .forms import PitchForm, CommentForm
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
        category = form.category.data

        fresh_pitch = Pitch(title=title, pitch_actual=pitch, category=category, user_id=current_user.id)

        fresh_pitch.save_pitch()

        return redirect(url_for('.profile', uname=current_user.username))
    title = 'New pitch'
    return render_template('new_pitch.html' , title=title, pitch_form=form)


@main.route('/single_pitch/<pitch_id>')
def single_pitch(pitch_id):
    """
    route to a single post
    :return:
    """
    form = CommentForm()
    pitch = Pitch.query.filter_by(id=pitch_id).first()

    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(comment=comment, pitch_id=pitch_id)

        new_comment.save_comment()

        return redirect(url_for('.pitch', pitch_id=pitch.id))

    return render_template('lonely_pitch.html', pitch_id=pitch.id, pitch=pitch, comment_form=form)

@main.route('/category/coding')
def deals():
    """
    route to deals category
    :return:
    """
    category = Pitch.query.filter_by(category='coding').all()
    title = 'deals'

    return render_template('category.html', category=category, title=title)



