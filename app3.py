import os
import plagiarism
import time

from flask import Flask, render_template, request


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
	target = os.path.join(APP_ROOT, 'images/')
	print(target)

	if not os.path.isdir(target):
		os.mkdir(target)

	for file in request.files.getlist("file"):
		print(file)
		filename = file.filename
		destination = "/".join([target, filename])
		print(destination)
		file.save(destination)

	filename_size=len(filename)
	is_zip=filename[filename_size-4:filename_size]
	if is_zip != ".zip":
		return render_template('complete.html',pr="type is wrong")

	rr=pro(filename)
	
	return render_template('complete.html',pr=rr)

def pro(dir_name):
	T_dir=dir_name
	T_dir=T_dir[:len(T_dir)-4]
	T_dire="./data/"+T_dir+time.strftime('%H%M%S')
	os.system('unzip ./images/'+T_dir+'.zip'+' -d '+T_dire)
	T_dire=T_dire+"/"
	re=plagiarism.get_result(T_dire)

	#for i in re:
		#print(i)
	return re

if __name__ == "__main__":
	app.run(port=3567, debug=True)
	

