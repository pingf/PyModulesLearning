import os
from flask import Flask, request, redirect, render_template, url_for
from werkzeug import secure_filename

UPLOAD_FOLDER = '.'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'py'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload_post', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['fileupload']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'okay, uploaded'


@app.route('/get_test')
def get_test():
    user = request.args.get('user')
    return render_template('get_test.html', user=user)


@app.route('/post_test', methods=['GET', 'POST'])
def post_test():
    if request.method == 'GET':
        return render_template('post_test.html')
    else:
        return redirect(url_for('get_test', user=request.form['username']))


if __name__ == '__main__':
    app.run(debug=True)
