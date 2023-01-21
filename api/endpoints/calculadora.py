from flask import Flask

app = Flask("Calculadora Teorema de Pitágoras")


@app.route("/", methods=["GET"])
def helloWorld():
    return "Hello World!"



app.run()