from flask import Flask, render_template
app = Flask(__name__) 


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', defaults = {'num':3, 'color': 'rgb(74, 178, 243)'})
@app.route('/play/<int:num>', defaults = {'color': 'rgb(74, 178, 243)'})
@app.route('/play/<int:num>/<color>')
def play(num, color):
    return render_template('play.html', num=num, color=color)


if __name__=="__main__":   
    app.run(debug=True) 
    
