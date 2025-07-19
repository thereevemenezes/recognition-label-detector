from flask import Flask, request, jsonify
from recognition_utils import upload_image_to_s3, detect_labels_s3, delete_image_from_s3
from dotenv import load_dotenv
import os
from werkzeug.utils import secure_filename

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    filename = secure_filename(file.filename)

    try:
        upload_image_to_s3(file, filename)
        labels = detect_labels_s3(filename)
        delete_image_from_s3(filename)
        return jsonify({'labels': labels})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
