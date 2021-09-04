from flask import Flask,render_template
import plotly
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('hello.html')
@app.route('/getImage')
def image():
    runCode()
    return render_template('map1.html')
@app.route('/getPeople')
def people():
	runCode2()
	return render_template('names.html')
def runCode():
	url='http://api.open-notify.org/iss-now.json'
	df=pd.read_json(url)
	df['latitude']=df.loc['latitude','iss_position']
	df['longitude']=df.loc['longitude','iss_position']
	df.reset_index(inplace=True)
	df=df.drop(['index','message'],axis=1)
	fig=px.scatter_geo(df,lat='latitude',lon='longitude',title='Position of International Space Station<br>(Refer blue dot in the globe)',projection='natural earth')
	plotly.offline.plot(fig,filename='C:\\Users\\Rokky\\Desktop\\Application\\templates\\map1.html',auto_open=False)

def runCode2():
	url1='http://api.open-notify.org/astros.json'
	df1=pd.read_json(url1)
	df1=df1.drop(['number','message'],axis=1)
	df2=df1.copy()
	df2['people']=[i['name'] for i in df2['people']]
	fig3=go.Figure(data=[go.Table(header=dict(values=list(df2.columns)),cells=dict(values=[df2.people]))])
	fig3.update_layout(autosize=False,width=1280,height=700,title_text="&nbsp;&nbsp;&nbsp;Name of Astronauts on ISS")
	plotly.offline.plot(fig3,filename='C:\\Users\\Rokky\\Desktop\\Application\\templates\\names.html',auto_open=False)
	    
if __name__ == '__main__':
   app.run(debug = True)
