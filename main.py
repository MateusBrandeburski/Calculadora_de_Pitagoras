from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')


# @app.route("/query", methods=["GET"])
# def helloWorld():
#     args = request.args
#     hipotenusa = args.get('hipotenusa')
#     cateto = args.get('cateto')

@app.route("/")
def index():
    if request.method == "POST":
        pass
    
    
    
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)