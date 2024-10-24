from flask import Flask, request, jsonify
from flask_cors import CORS
import io
from modules.google_cloud_ocr.google_cloud_ocr import google_cloud_ocr
from modules.azure_cloud_ocr.azure_cloud_ocr import azure_cloud_ocr

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    ocr_engine = request.form.get('ocr_engine', 'google')

    try:
        if ocr_engine == 'google':
            google_text = google_cloud_ocr(file)
            return jsonify({'status': 'success', 'ocr_engine': 'google', 'text': google_text}), 200
        elif ocr_engine == 'azure':
            azure_text = azure_cloud_ocr(file)
            return jsonify({'status': 'success', 'ocr_engine': 'azure', 'text': azure_text}), 200
        else:
            return jsonify({'error': 'Unsupported OCR engine selected'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
