
class TeoremaDePitagoras():
    
    # função construtora
    def __init__(self,  catetoA=0, catetoO=0, hipotenusa=0):
        
        """Explicação dessa conversão
        Essas converções e cndições são necessárias porque na rota são decalarados 3 tipos de query paramns, e quando um desses parametros não é passado, ele retorna um item None (e um item None não pode ser multiplicado, o que faz com que esse item caia no tratamento de erro). Então "float(catetoO) if catetoO is not None else 0" é a condição que faz com que, caso seja None, ele vire 0.
        
        Acima, em self, precisa ser passado como (catetoA=0, catetoO=0, hipotenusa=0) para que não precise sempre declarar todos sempre que for usar a classe, por exemplo: teorema=TeoremaDePitagoras(catetoA=catetoA, catetoO=catetoO).
        """
        self.__catetoO = catetoO
        self.__catetoO= float(catetoO) if catetoO is not None else 0
        self.__catetoA = catetoA
        self.__catetoA = float(catetoA) if catetoA is not None else 0
        self.__hipotenusa = hipotenusa
        self.__hipotenusa = float(hipotenusa) if hipotenusa is not None else 0
        
    def calcular_catetos(self):
        """Como funcinona a formula matemática dessa função:
        O Teorema de Pitágoras diz que é possível calcular qualquer um dos lados de um triângilo retângulo se soubermos o valor de 2 lados. 
        
        Os nomes dos 3 lados são: Cateto Oposto, Cateto Adjacente, Hipotenusa.
        
        cA² + cO² = h²
        
        Sendo assim, não importa a ordem dos catetos, a formula dará o mesmo valor.
        As variáveis foram contruídas como se tivesse sido calculado "na mão", primiero um lado, depois passa para o outro lado da equação seguindo as regras matemáticas...   
        """ 
        quadrado_do_cateto = self.__catetoA ** 2 or self.__catetoO ** 2
        quadrado_da_hipotenusa = self.__hipotenusa**2    
        passa_subtraindo = quadrado_da_hipotenusa - quadrado_do_cateto
        cateto_final = passa_subtraindo ** (1/2) # ou 0,5    
        return cateto_final
      
    def calcular_hipotenusa(self):
        
        quadrado_da_hipotenusa = self.__catetoO**2 + self.__catetoA**2
        hipotenusa = quadrado_da_hipotenusa ** (1/2)
        return hipotenusa
   
    

            

# teorema = TeoremaDePitagoras(catetoA=4, hipotenusa=5)
# teorema.calcular_catetos()

# teorema = TeoremaDePitagoras(catetoO=3, hipotenusa=5)
# teorema.calcular_catetos()

# teorema = TeoremaDePitagoras(catetoA=3, catetoO=4)
# teorema.calcular_hipotenusa()