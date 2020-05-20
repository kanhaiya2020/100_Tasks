from flask import Flask,render_template,url_for
import os
path1 = os.getcwd()+'\\templates'
app = Flask(__name__,static_url_path="",static_folder="",template_folder=path1)
global directory
path = os.getcwd()+'\\ram'
print(path)
directory = os.listdir(path)
s="ram/"
li=[]
for var in directory:
    li.append(s+var)
@app.route("/")
def home():
    return render_template('test1.html', li=li,value=len(li))
if(__name__=="__main__"):
    app.run(host='127.0.0.1', port=5000)
