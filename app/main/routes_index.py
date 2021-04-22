from app import db
from flask_login import current_user, login_required
from app.main import bp
from app.models import User, UserRoles
from flask import render_template, redirect, url_for, flash, request
from app.main.utils import role_required, role_forbidden

@bp.route('/')
@bp.route('/index/')
@login_required
@role_forbidden([UserRoles.default])
def ShowIndex():
	return render_template('index.html')
