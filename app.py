from flask import Flask,render_template,request
from bing_image_downloader import downloader


app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results',methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        result=request.form
        s= result['search']
        l=result['limit']
        d=downloader.download(s, limit=int(l),verbose=True)
        return render_template('results.html',result=result,s=s,l=l)


if __name__=='__main__':
    app.run(debug=True)