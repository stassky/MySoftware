from flask import Flask, jsonify

app = Flask('helloworld')

# Decorator defines a route
# http://localhost:5000/
@app.route('/')
def index():
    return jsonify({ 'text': 'Hello World!' })

if __name__ == '__main__':
    app.run()