from flask import Flask,request,redirect
import jinja2, os, random

import MySQLdb as mysql

print 'setting up jinja environment'
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

app = Flask(__name__)

@app.route('/')
def hello_world():

	template = JINJA_ENVIRONMENT.get_template('index.html')

	return template.render()

@app.route('/test')
def greg():

	return "TEST GREG"

@app.route('/get')
def sendBackData():

    return 'animal:mammals:dogs:static/dog.png:Dachschund:General household regions' + str(random.randint(1,56))+'_plant:flowers:static/panda.png:Birch Tree:Ireland<br>and other areas!' + str(random.randint(1,4))+random.choice(['','~'])

@app.route('/insertanimal')
def insertAnimal():

	return JINJA_ENVIRONMENT.get_template('insertanimal.html').render()

@app.route('/insertdata', methods=['POST'])
def inputData():

	print 'requesting name'
	name = request.form['name']
	print 'requesting image'
	imurl = request.form.get("imurl")
	print 'requesting lc'
	lc = request.form.get("lc")
	hc = request.form.get("hc")
	locs = request.form.get("locs")
	info = request.form.get("info")
	wiki = request.form.get("wiki")
	land = request.form.get("land")
	water = request.form.get("water")
	print 'form data requested successfully'

	print 'connecting to databse'
	conn = mysql.connect(host='127.5.239.2',user="adminIChJ87N",passwd="9XHzRbXK1359",db = "python")
	print 'connected to database succesfully'
	print 'creating db cursor'
	x = conn.cursor()
	print 'cursor success'

	try:
		print 'executing sql'
		x.execute("""INSERT INTO animal (name,imurl,lc,hc,locs,info,wikilink,land,water) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(name,imurl,lc,hc,locs,info,wiki,int(land),int(water)))
		conn.commit()
		print 'execution success'
	except:
		conn.rollback()
		print 'execution fail'

	print 'closing db connection'
	conn.close()
	print 'closed'
	print 'returning'
	return "DATA SUBMITTED"




if __name__ == '__main__':
    app.run()
