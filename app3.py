#-*- coding: utf-8 -*-

import os
import time
import json
import glob

from flask import Flask, render_template, request
import plagiarism 
import sys  

reload(sys)  
sys.setdefaultencoding('Cp1252')

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


json_data=""
DIRE=""


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

    if filename.endswith(".zip") != True :
            return render_template('complete.html')


    global json_data
    (result, json_data, error_dna, short_dna, good_dna)=pro(filename)
  
    return render_template('complete.html',pr=result, er=error_dna, short=short_dna)


@app.route("/complete", methods=['POST'])
def complete():
    return render_template('view_graph.html',data=json_data)

@app.route("/show_code", methods=['GET'])
def show_code():
    file1_name= request.args.get('file1')
    file2_name= request.args.get('file2')

    path_file1=DIRE+file1_name
    path_file2=DIRE+file2_name

    file1=open(path_file1,'r')
    file2=open(path_file2,'r')

    return render_template('show_code.html', File1_name=file1_name+"\n",File2_name=file2_name+"\n",File1=file1.read(), File2=file2.read())


def pro(dir_name):
    T_dir=dir_name
    T_dir=T_dir[:len(T_dir)-4]
    T_dire="./data/"+T_dir+time.strftime('%H%M%S')
    os.system('unzip ./images/'+T_dir+'.zip'+' -d '+T_dire)
    T_dire=T_dire+"/"
    global DIRE
    DIRE=T_dire
    #(re,d)=plagiarism.get_result(T_dire)

    return plagiarism.get_result(T_dire)

if __name__ == "__main__":
    app.run(port=3570, debug=True)
    

