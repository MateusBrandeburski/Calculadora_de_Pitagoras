from flask import Blueprint, request, render_template, redirect
from classes.formula_pitagoras import TeoremaDePitagoras

calculadora_grafica = Blueprint('calculadora_grafica', __name__, template_folder='templates')


# Rota que renderiza a calculadora.
@calculadora_grafica.route("/", methods=['GET'])
def index():
         
     # verifica se o parâmetro resposta, do render_templete contém alguma string.
     global resposta
     if 'resposta' in globals() and resposta != "":
          
          return render_template('calculadora_de_pitagoras.html', resposta=resposta)  
        
     else:
          return render_template('calculadora_de_pitagoras.html')
     
          
# Rota que serve apenas para processar o formulário da Calculadora de Pitágoras 
@calculadora_grafica.route("/calculadora", methods=['POST'])
def calculadora():
     
     # verifica se o botão calcular foi clicado
     if request.form['action'] == 'calcular':
          
          # Tramento de erro para número negativo, se é calculado um lado de um retângulo retângulo, número negativo é impossível.
          try: 
               # verifica 3 ou 2 campos foram deixados em branco, além de verificar se os 3 campos foram preenchidos.
               if  (request.form.get('hipotenusa') == "") and (request.form.get('cA') == "") and  (request.form.get('cO') == "") or (request.form.get('hipotenusa') == "") and (request.form.get('cA') == "") or  (request.form.get('hipotenusa') == "") and (request.form.get('cO') == "") or (request.form.get('cA') == "") and (request.form.get('cO') == "") or (request.form.get('cA') != "") and (request.form.get('cO') != "") and  (request.form.get('hipotenusa') != ""):   
                    
                    global resposta
                    resposta = TeoremaDePitagoras.strings_teorema(name="falta_parametros")
                    return redirect('/')
               
               # Se 2 campos forem preenchidos corretamente:
               else:
                                   
                    # calcula os catetos
                    if request.form.get('hipotenusa') != "":   
                         # passando os 3 parâmetros, porque ele receber qualquer um dos lados do cateto para calcular o outro lado.
                         teorema = TeoremaDePitagoras(catetoA=request.form.get('cA'),
                                                  catetoO=request.form.get('cO'), 
                                                  hipotenusa=request.form.get('hipotenusa'))

                         resposta = teorema.calcular_catetos()
                         return redirect('/')
                    
                                
                    # calcula a hipotenusa
                    elif request.form.get('hipotenusa') == "":   
                         teorema = TeoremaDePitagoras(catetoA=request.form.get('cA'), catetoO=request.form.get('cO'))
                         resposta = teorema.calcular_hipotenusa()
                         return redirect('/')
                     
          # Tramento de erro para número negativo, se é calculado um lado de um retângulo retângulo, número negativo é impossível.         
          except TypeError:
               resposta =  TeoremaDePitagoras.strings_teorema(name="TypeError")      
               return redirect('/')
               
               