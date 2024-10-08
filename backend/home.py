from flask import Blueprint, render_template, request
from flask_login import login_required
from models import Article, Jurisprudence, Recommendation
import os

home = Blueprint('home', __name__, template_folder=os.path.abspath('../frontend'))

@home.route('/home/articles', methods=['GET'])
@login_required
def articles():
    page = request.args.get('page', 1, type=int)
    per_page = 10

    # Obter o parâmetro de ordenação da URL
    sort_by = request.args.get('sort_by', 'title_asc')

    # Configurar a ordenação com base no parâmetro
    if sort_by == 'title_asc':
        order = Article.title.asc()
    elif sort_by == 'title_desc':
        order = Article.title.desc()
    elif sort_by == 'date_asc':
        order = Article.created_at.asc()
    elif sort_by == 'date_desc':
        order = Article.created_at.desc()
    else:
        order = Article.title.asc()  # Ordenação padrão

    articles = Article.query.order_by(order).paginate(page=page, per_page=per_page)

    return render_template('articles.html', articles=articles, sort_by=sort_by)

@home.route('/home/jurisprudences', methods=['GET'])
@login_required
def jurisprudences():
    page = request.args.get('page', 1, type=int)
    per_page = 10

    # Obter o parâmetro de ordenação da URL
    sort_by = request.args.get('sort_by', 'title_asc')

    # Configurar a ordenação com base no parâmetro
    if sort_by == 'title_asc':
        order = Jurisprudence.title.asc()
    elif sort_by == 'title_desc':
        order = Jurisprudence.title.desc()
    elif sort_by == 'date_asc':
        order = Jurisprudence.created_at.asc()
    elif sort_by == 'date_desc':
        order = Jurisprudence.created_at.desc()
    else:
        order = Jurisprudence.title.asc()  # Ordenação padrão

    jurisprudences = Jurisprudence.query.order_by(order).paginate(page=page, per_page=per_page)

    return render_template('jurisprudences.html', jurisprudences=jurisprudences, sort_by=sort_by)

@home.route('/home/recommendations', methods=['GET'])
@login_required
def recommendations():
    page = request.args.get('page', 1, type=int)
    per_page = 10

    # Obter o parâmetro de ordenação da URL
    sort_by = request.args.get('sort_by', 'theme_asc')

    # Configurar a ordenação com base no parâmetro
    if sort_by == 'theme_asc':
        order = Recommendation.theme.asc()
    elif sort_by == 'theme_desc':
        order = Recommendation.theme.desc()
    elif sort_by == 'date_asc':
        order = Recommendation.created_at.asc()
    elif sort_by == 'date_desc':
        order = Recommendation.created_at.desc()
    else:
        order = Recommendation.theme.asc()  # Ordenação padrão

    recommendations = Recommendation.query.order_by(order).paginate(page=page, per_page=per_page)

    return render_template('recommendations.html', recommendations=recommendations, sort_by=sort_by)
