from flask import url_for, render_template, redirect

import forms
from api import tags
from loader import app, pm


@app.route('/')
def index():
    return redirect(url_for('projects'))


@app.route('/test')
def test():
    return {}


@app.route('/projects/')
def projects():
    strings = []

    for item in pm.projects():
        item_url = tags.a(item, url_for('project_item', path=item))
        strings.append(item_url)

    return tags.pre('\n'.join(strings))


@app.route('/projects/<path:path>', methods=['GET', 'POST'])
def project_item(path: str):
    form = forms.EditFile()
    path = path.strip('/')
    project_name = path.split('/')[0]

    if form.validate_on_submit():
        pm.edit(path, form.text_area.data)
        pm.deploy(project_name)
        return redirect(url_for('project_item', path=path))

    result = pm.get(path)

    if isinstance(result, list):
        strings = []

        for item in result:
            item_path = f'{path}/{item}'.strip('/')
            item_url = tags.a(item, url_for('project_item', path=item_path))
            strings.append(item_url)

        return tags.pre('\n'.join(strings))

    else:
        form.text_area.data = result
        return render_template('edit_file.html', form=form)
