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

        def predecir_valor(self):
            #Imprimir la ecuación de regresión con los valores calculados
            valorUsuario=int(input("Ingresa el valor de gastos de publicidad: "))
            valorEstimado=self.beta_0 + (self.beta_1*valorUsuario)
            print(f"Resultado del calculo de nuestros parametros: β0={self.beta_0:.2f} y β1={self.beta_1:.2f}")
            print(f"En nuestra formula se ve así: ŷ = {self.beta_0:.2f} + ({self.beta_1:.2f})({valorUsuario})")
            print(f"El valor de ventas estimado es: {valorEstimado:.2f}")

#Datos hardcodeados
x = [1,2,3,4,5,6,7,8,9]
y = [2,4,6,8,10,12,14,16,18]

#Creamos e inicializamos el modelo
modelo = SimpleLinearRegression(x,y)

#Se calculan los coeficientes
modelo.calcularCoeficientes()

#Sustituir datos e imprimir resultado
modelo.predecir_valor()
