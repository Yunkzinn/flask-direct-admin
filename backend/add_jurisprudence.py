from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Jurisprudence

add_jurisprudence = Blueprint('add_jurisprudence', __name__, template_folder='../frontend')

@add_jurisprudence.route('/home/jurisprudences')
def show():
    page = request.args.get('page', 1, type=int)
    per_page = 10

    # Paginação da consulta
    jurisprudences = Jurisprudence.query.paginate(page=page, per_page=per_page)

    return render_template('jurisprudences.html', jurisprudences=jurisprudences)


@add_jurisprudence.route('/home/edit-jurisprudence/<int:id>', methods=['GET', 'POST'])
def edit_jurisprudence(id):
    jurisprudence = Jurisprudence.query.get_or_404(id)
    
    if request.method == 'POST':
        jurisprudence.title = request.form['title']
        jurisprudence.references = request.form['references']
        jurisprudence.city = request.form['city']
        jurisprudence.state = request.form['state']
        jurisprudence.keywords = request.form['keywords']
        jurisprudence.specialty = request.form['specialty']
        jurisprudence.content = request.form['content']
        
        db.session.commit()
        return redirect(url_for('add_jurisprudence.show', page=1))
    
    return render_template('edit_jurisprudence.html', jurisprudence=jurisprudence)

@add_jurisprudence.route('/home/delete-jurisprudence/<int:id>', methods=['POST'])
def delete_jurisprudence(id):
    jurisprudence = Jurisprudence.query.get_or_404(id)
    db.session.delete(jurisprudence)
    db.session.commit()
    return redirect(url_for('add_jurisprudence.show', page=1))
