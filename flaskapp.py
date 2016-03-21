from flask import Flask
import jinja2
import os

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


if __name__ == '__main__':
    app.run()