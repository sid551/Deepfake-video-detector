from flask import Flask, render_template, request
import os
from utils import process_video
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        if 'video' not in request.files:
            return render_template('index.html', result="No file part")

        file = request.files['video']
        if file.filename == '':
            return render_template('index.html', result="No selected file")

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            result = process_video(filepath)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
