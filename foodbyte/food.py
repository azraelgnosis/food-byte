from flask import (
    Blueprint, render_template
)

from foodbyte.db import get_db, get_recipes

bp = Blueprint('food', __name__)

@bp.route('/')
def index():
    recipes = get_recipes()

    return render_template('food/index.html', recipes=recipes)

@bp.route('/create_recipe')
def create_recipe(): ...