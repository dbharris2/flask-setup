import pip

def install(package):
    pip.main(['install', package])

install('flask')
install('requests')
install('gunicorn')

runtime_file = open('runtime.txt', 'w')
runtime_file.write('python-3.6.2\n')

requirements_file = open('requirements.txt', 'w')
requirements_file.write('Flask\n')
requirements_file.write('gunicorn\n')
requirements_file.write('requests\n')

procfile_file = open('Procfile', 'w')
procfile_file.write('web: gunicorn example:app\n')

example_file = open('example.py', 'w')
example_file.write('from flask import Flask\n')
example_file.write('import requests\n\n')
example_file.write('app = Flask(__name__)\n\n')
example_file.write("@app.route(\"/\")\n")
example_file.write('def joke():\n')
example_file.write("    response = requests.get('http://api.icndb.com/jokes/random')\n")
example_file.write("    json = response.json()\n")
example_file.write("    return json['value']['joke']\n")

print("Done! Run `heroku local web` to try out your new Flask server!")
