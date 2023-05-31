from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(r'C:\Users\AJAIKRISHNA.S\OneDrive\Desktop\AJAI workspace\finally\HTRPipeline\data\\' + file.filename)
    return 'File uploaded successfully'

if __name__ == '__main__':
    app.run()