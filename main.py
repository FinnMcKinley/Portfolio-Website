from flask import Flask, render_template

app = Flask(__name__)


# basic route
@app.route('/')
def root():
  return render_template('home.html')
  

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=8080)
