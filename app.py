from flask import Flask, render_template, request, jsonify
import os
import sys
from werkzeug.utils import secure_filename
from models.predict import analyze_file

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'temp_uploads'

# Create upload folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'cpp', 'java', 'py', 'c', 'cc', 'cxx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze_code():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'File type not supported. Supported: .cpp, .java, .py, .c, .cc, .cxx'}), 400
        
        # Save file temporarily
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Analyze the file
            results = analyze_file(filepath)
            
            return jsonify({
                'success': True,
                'filename': filename,
                'results': {
                    'readability': round(results['readability'], 1),
                    'maintainability': round(results['maintainability'], 1),
                    'complexity': round(results['complexity'], 1),
                    'security': round(results['security'], 1),
                    'overall': round(results['overall'], 1),
                    'metrics': results['metrics']
                }
            })
        finally:
            # Clean up temp file
            if os.path.exists(filepath):
                os.remove(filepath)
    
    except Exception as e:
        return jsonify({'error': f'Analysis failed: {str(e)}'}), 500

@app.route('/api/info')
def info():
    return jsonify({
        'name': 'AI-Powered Code Quality Reviewer',
        'version': '1.0.0',
        'description': 'Analyzes code quality across C++, Python, and Java',
        'supported_languages': ['C++', 'Python', 'Java'],
        'metrics': ['Readability', 'Maintainability', 'Complexity', 'Security']
    })

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
