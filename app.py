import os

templates = 'templates'
static = 'static'
file_name = input(">>")

boiler_plate = """from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def hello():
\treturn render_template('index.html')
if __name__ == '__main__':
\tapp.run(debug=True)
"""

dev_info = '''<h4>Flask Boilerplate v0.1</h4>
<h5>developed by Lazarus Gumbi</h5>
<h5>email: gumbimelusi2@gmail.com</h5>
<h5>facebook:<a href='https://www.facebook.com/lazarus.somkhanda/'>Melusi Gumbi</a></h5>
'''
with open(file_name+'.py','w') as f:
    f.writelines(boiler_plate)
    f.close()

os.mkdir(f'./{templates}')
os.mkdir(f'./{static}')

with open('./templates/index.html','w') as f:
    f.writelines(dev_info)
    f.close()

with open('./static/styles.css','w') as f:
    f.writelines(dev_info)
    f.close()

print("Done...")
