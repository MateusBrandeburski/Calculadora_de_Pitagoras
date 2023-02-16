from flask import Flask, request, render_template
from classes.formula_pitagoras import TeoremaDePitagoras
from classes.gmail import Email
import os

# classes instânciadas
app = Flask(__name__, template_folder='templates')
enviar = Email(os.environ["EMAIL"], os.environ["SENHA"])


@app.route("/teorema_de_pitagoras", methods=["GET"])
def query_teorema():
    
    hipotenusa = request.args.get("hipotenusa")
    catetoA = request.args.get("catetoA")
    catetoO = request.args.get("catetoO") 
     
    try:
        if (catetoA and hipotenusa) or (catetoO and hipotenusa): 
            """Como funciona essa rota:
            O aplicativo está sendo desenvolvido usando POO, por isso, os parâmetros são passado na instância da classe TeoremaDePitagoras. 
            
            O round, dentro do return, serve para limitar o número de casa decimais. Sendo que 2, correponde == 2.22. Se tivesse 3, correponderia == 3.333
            """    
            teorema = TeoremaDePitagoras(catetoA=catetoA, catetoO=catetoO,hipotenusa=hipotenusa)
            return { "Cateto": round(teorema.calcular_catetos(), 2) }
        
        elif catetoA and catetoO:      
            teorema = TeoremaDePitagoras(catetoA=catetoA, catetoO=catetoO)       
            return { "Hipotenusa": round(teorema.calcular_hipotenusa(), 2)}
      
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
                enviar.envia_email()
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
    app.run( host='0.0.0.0', port=8000, debug=True)