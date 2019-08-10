from flask import Flask

app = Flask(__name__)

@app.route('/<names>')
def hello_world(names):
    
    return "Hi, what is you name?"
    name=names
    return "Hi "+ name +"!"

    return " Ok well, It was nice meeting you."
    return "Bye!"


        
   


if __name__ == '__main__':
  app.run(host='0.0.0.0')
