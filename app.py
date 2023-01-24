from flask import Flask, request, render_template


app = Flask(__name__, template_folder='templates')


@app.route("/query", methods=["GET"])
def caculadora_raiz():
    query_params = request.args
    try:
        catetoB = float(query_params.get('catetoB'))
        catetoC = float(query_params.get('catetoC'))
        quadrado_da_hipotenusa = catetoB**2 + catetoC**2
        hipotenusa = quadrado_da_hipotenusa ** (1/2)
        
        return {
            "quadrado_hipotenusa": quadrado_da_hipotenusa,
            "hipotenusa":hipotenusa         
            }
    
    except TypeError:
      return {"204":"no_content", "query":"faltam_parametros"}
  
    except ValueError:
        return {"400":"bod_request", "number":"apenas_float_e_int_suportados"}


@app.route("/", methods=['GET', 'POST'])
def index():

    try:
        if request.form['action'] == 'hipotenusa':
            return render_template('hipotenusa.html')
        
        elif request.form['action'] == 'adjacente':    
            return render_template('cateto_adjacente.html') 
        
        elif request.form['action'] == 'info':
            return render_template('infos.html')
                
    except:
        pass
    
    return render_template('index.html')

@app.route("/", methods=['GET'])
def infos():
    
        if request.form['action'] == 'voltar':
            return render_template('index.html')
 
@app.route("/hipotenusa", methods=['GET', 'POST'])
def hipotenusa():
    
    try:            
        if request.form['action'] == 'form_hipotenusa':
                    
            catetoB = float(request.form.get('catetoB'))
            catetoC = float(request.form.get('catetoC'))
            quadrado_da_hipotenusa = catetoB**2 + catetoC**2
            hipotenusa = quadrado_da_hipotenusa ** (1/2)
            
            return render_template('hipotenusa_resposta.html', catetoB=catetoB, catetoC=catetoC, quadrado_da_hipotenusa=quadrado_da_hipotenusa, hipotenusa=hipotenusa)
        else:
            return render_template('index.html')
    except:
        return render_template('hipotenusa.html')

    
@app.route("/cateto_adjacente", methods=['GET', 'POST'])
def cateto_adjacente():
    
    try:            
        if request.form['action'] == 'form_adjacente':
                    
            cateto_oposto = float(request.form.get('cateto_oposto'))
            hipotenusa = float(request.form.get('hipotenusa'))
            # ca² + x² = h²
            quadrado_do_cateto = cateto_oposto**2
            quadrado_da_hipotenusa = hipotenusa**2
            # x² = h² - ca²
            passa_subtraindo = quadrado_da_hipotenusa - quadrado_do_cateto
            print(passa_subtraindo)
            cateto_adjacente_final = passa_subtraindo ** (1/2) # ou 0,5
                       
            return render_template('cateto_adjacente_resposta.html', cateto_oposto=cateto_oposto, hipotenusa=hipotenusa, cateto_adjacente_final=cateto_adjacente_final)
        else:
            return render_template('index.html')
    except:
        return render_template('cateto_adjacente.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)