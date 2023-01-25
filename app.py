from flask import Flask, request, render_template
from enviar_email.gmail import envia_email

app = Flask(__name__, template_folder='templates')


@app.route("/query_hipo", methods=["GET"])
def query_hipo():
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
    
@app.route("/query_oposto", methods=["GET"])
def query_oposto():
    query_params = request.args
    try:
        catetoA = float(query_params.get('catetoA'))
        hipotenusa = float(query_params.get('hipotenusa'))
        quadrado_do_cateto_adjacente = catetoA**2
        quadrado_da_hipotenusa = hipotenusa**2
        passa_subtraindo = quadrado_da_hipotenusa - quadrado_do_cateto_adjacente
        cateto_oposto_final = passa_subtraindo ** (1/2) # ou 0,5
        
        return {
            "cateto_oposto":cateto_oposto_final  
            }
    
    except TypeError:
      return {"204":"no_content", "query":"faltam_parametros"}
  
    except ValueError:
        return {"400":"bod_request", "number":"apenas_float_e_int_suportados"}

@app.route("/query_adjacente", methods=["GET"])
def query_adjacente():
    query_params = request.args
    try:
        catetoO = float(query_params.get('catetoO'))
        hipotenusa = float(query_params.get('hipotenusa'))
        quadrado_do_cateto = catetoO**2
        quadrado_da_hipotenusa = hipotenusa**2
        passa_subtraindo = quadrado_da_hipotenusa - quadrado_do_cateto
        cateto_adjacente_final = passa_subtraindo ** (1/2) # ou 0,5
        
        return {
            "cateto_adjacente":cateto_adjacente_final  
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
            try:
                envia_email()
            except:
                pass
            return render_template('infos.html')
            
        elif request.form['action'] == 'oposto':
           
            return render_template('cateto_oposto.html')
        
    except:
        pass
    
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
            # co² + x² = h²
            quadrado_do_cateto = cateto_oposto**2
            quadrado_da_hipotenusa = hipotenusa**2
            # x² = h² - co²
            passa_subtraindo = quadrado_da_hipotenusa - quadrado_do_cateto
            print(passa_subtraindo)
            cateto_adjacente_final = passa_subtraindo ** (1/2) # ou 0,5
                       
            return render_template('cateto_adjacente_resposta.html', cateto_oposto=cateto_oposto, hipotenusa=hipotenusa, cateto_adjacente_final=cateto_adjacente_final)
        else:
            return render_template('index.html')
    except:
        return render_template('cateto_adjacente.html')

@app.route("/cateto_oposto", methods=['GET', 'POST'])
def cateto_oposto():
    
    try:            
        if request.form['action'] == 'form_oposto':
                    
            cateto_adjacente = float(request.form.get('cateto_adjacente'))
            hipotenusa = float(request.form.get('hipotenusa'))
            # ca² + x² = h²
            quadrado_do_cateto_adjacente = cateto_adjacente**2
            quadrado_da_hipotenusa = hipotenusa**2
            # x² = h² - ca²
            passa_subtraindo = quadrado_da_hipotenusa - quadrado_do_cateto_adjacente
            print(passa_subtraindo)
            cateto_oposto_final = passa_subtraindo ** (1/2) # ou 0,5
                       
            return render_template('cateto_oposto_resposta.html', cateto_adjacente=cateto_adjacente, hipotenusa=hipotenusa, cateto_oposto_final=cateto_oposto_final)
        else:
            return render_template('index.html')
    except:
        return render_template('cateto_oposto.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)