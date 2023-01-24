from flask import Flask, request, render_template


app = Flask(__name__, template_folder='templates')


@app.route("/query", methods=["GET"])
def caculadora_raiz():
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
        if request.form['action'] == 'hipotenusa':
            return render_template('hipotenusa.html')           
    except:
        pass
    
    return render_template('index.html')
    
 
@app.route("/hipotenusa", methods=['GET', 'POST'])
def hipotenusa():

    try:       
        if request.method == "GET":
            return render_template('index.html')         
            
        elif request.method == "POST":
            catetoB = float(request.form.get('catetoB'))
            catetoC = float(request.form.get('catetoC'))
            quadrado_da_hipotenusa = catetoB**2 + catetoC**2
            hipotenusa = quadrado_da_hipotenusa ** (1/2)
            # hipotenusa = str(hipotenusa[0:4])
            
            return render_template('hipotenusa2.html', catetoB=catetoB, catetoC=catetoC, quadrado_da_hipotenusa=quadrado_da_hipotenusa, hipotenusa=hipotenusa)                  
    except:
         pass    
        
    return render_template('hipotenusa.html')
   
    
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)