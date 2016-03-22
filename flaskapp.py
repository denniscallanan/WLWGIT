from flask import Flask
import jinja2, os, random

#import MySQLdb as mysql
# mysql.connect(host='127.5.239.2',user="adminIChJ87N",passwd="9XHzRbXK1359",db = "python")

print 'setting up jinja environment'
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
print 'done'


app = Flask(__name__)

@app.route('/')
def hello_world():

	template = JINJA_ENVIRONMENT.get_template('index.html')

	return template.render()

@app.route('/get')
def sendBackData():

        return 'animal:mammals:dogs:static/dog.png:Dachschund:General household regions' + str(random.randint(1,56))+'_plant:flowers:static/panda.png:Birch Tree:Ireland<br>and other areas!' + str(random.randint(1,4))+random.choice(['','~'])


if __name__ == '__main__':
    app.run()
