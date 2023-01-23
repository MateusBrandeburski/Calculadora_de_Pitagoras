from flask import Flask, request, render_template


app = Flask(__name__, template_folder='templates')


@app.route("/query", methods=["GET"])
def caluladora_raiz():
    query_params = request.args
    try:
        catetoB = float(query_params.get('catetoB'))
        catetoC = float(query_params.get('catetoC'))
        hipotenusa = catetoB**2 + catetoC**2
        
        return {"hipotenusa":hipotenusa}
    
    except TypeError:
      return {"204":"no_content", "query":"faltam_parametros"}
  
    except ValueError:
        return {"400":"bod_request", "number":"apenas_float_e_int_suportados"}


@app.route("/", methods=['GET', 'POST'])
def index():

    try:
        if request.method == "POST":
            catetoB = float(request.form.get('catetoB'))
            catetoC = float(request.form.get('catetoC'))
            hipotenusa = catetoB**2 + catetoC**2
            
            return render_template('hipotenusa.html', catetoB=catetoB, catetoC=catetoC, hipotenusa=hipotenusa)
    except:
        pass
        
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)