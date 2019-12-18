from flask import Flask, render_template, request, send_from_directory
from werkzeug import secure_filename
import os
import fin


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/upload'
app.config['STATIC_FOLDER'] = 'D:\OneDrive\COMPYear3Sem1\COMP3122\project'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


# No caching at all for API endpoints.
@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response
   
@app.route('/')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file1():
	if request.method == 'POST':
		f = request.files['file']
		f.save(secure_filename(f.filename))
		print(f.filename)
		return uploaded_file(f.filename)
		
def uploaded_file(filename):
   #return send_from_directory("",filename),'file uploaded successfully'
   filename='\\'+filename
   aword = fin.lip_handle(filename)
   return render_template('result.html', result_information=aword[0], result_information1=aword[1], result_information2=aword[2])

if __name__ == '__main__':
   app.run()

