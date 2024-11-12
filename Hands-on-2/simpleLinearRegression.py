class SimpleLinearRegression:
        def __init__(self,x,y):
            #Inicializar los datos
            self.x = x
            self.y = y
            self.beta_0 = 0
            self.beta_1 = 0
        
        def calcularCoeficientes(self):
              #Calcular Beta_0 y Beta_1 usando las formulas de regresión
              #Conteo de datos
              n = len(self.x)
              #Sumatoria de cuadrados
              sum_x_squared = sum(x ** 2 for x in self.x)
              #Sumatoria de productos
              sum_xy = sum(x*y for x, y in zip(self.x,self.y))
              #Sumatorias
              sum_x = sum(self.x)
              sum_y = sum(self.y)
              
              #Formulas para Beta_1 y Beta_0
              self.beta_0 = ((sum_x_squared * sum_y)-(sum_x*sum_xy))/((n*sum_x_squared)-sum_x ** 2)
              self.beta_1 = ((n*sum_xy)-(sum_x*sum_y))/((n*sum_x_squared)-sum_x ** 2)

        def imprimir_ecuación(self):
            #Imprimir la ecuación de regresión con los valores calculados
            print(f"Resultado del calculo de nuestros parametros: β0={self.beta_0:.2f} y β1={self.beta_1:.2f}")
            print(f"En nuestra formula se ve así: ŷ = {self.beta_0:.2f} + {self.beta_1:.2f}x")

#Datos hardcodeados
x = [23,26,30,34,43,48,52,57,58]
y = [651,762,856,1063,1190,1298,1421,1440,1518]

#Creamos e inicializamos el modelo
modelo = SimpleLinearRegression(x,y)

#Se calculan los coeficientes
modelo.calcularCoeficientes()

#Imprimir los resultados
modelo.imprimir_ecuación()
