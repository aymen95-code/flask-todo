from flask import render_template, redirect, url_for, request, session
from crud import app, db
from crud.forms import TodoForm
from crud.models import List

@app.route('/')
def home():
    errors = session.get('form_content_error')
    if request.method == 'GET':
        session.pop('form_content_error', None)
    form = TodoForm()
    update_form = UpdateTaskForm()
    items = List.query.all()
    return render_template('index.html', form=form, update_form=update_form, items=items, errors=errors)

@app.route('/create', methods=['POST'])
def create():
    form = TodoForm()
    if form.validate_on_submit():
        item = List(item=form.content.data)
        db.session.add(item)
        db.session.commit()
    if form.content.errors:
        session['form_content_error'] = form.content.errors
    return redirect(url_for('home'))

@app.route('/update', methods=['POST'])
def update():
    form = TodoForm()
    if form.validate_on_submit():
        task_id = request.form['taskid']
        item = List.query.filter_by(id=task_id).first()
        item.item = form.content.data
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        task_id = request.form['taskid']
        item = List.query.get_or_404(task_id)
        print(item)
        db.session.delete(item)
        db.session.commit()
    return redirect(url_for('home'))

