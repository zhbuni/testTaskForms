from flask import Flask, request, jsonify
from tinydb import TinyDB, Query
import validations


app = Flask(__name__)

db = TinyDB('db.json')


@app.route('/get_form', methods=['POST'])
def get_form():
    request_data = {el[0]: el[1] for el in request.form.items()}
    if not request_data:
        return 'empty query'

    forms = list()
    form_template = Query()

    for k, v in request_data.items():
        form = db.search(form_template[k] == v)
        if form:
            forms.append(form[0])

    mx, form = 0, None

    for el in forms:
        intersection = len(request_data.keys() & el.keys())
        if intersection > mx:
            form = el
            mx = intersection

    if not form:
        dct = dict()
        for key, value in request_data.items():
            dct[key] = validations.determine_type(value)
        return jsonify(dct)

    if 'name' in form:
        return jsonify(form['name'])
    return jsonify(form)


if __name__ == '__main__':
    app.run()