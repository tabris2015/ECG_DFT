import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import thinkdsp as dsp

# funciones utiles
PI2 = np.pi * 2  

# funcion para leer los datos del archivo CSV en un array de numpy
def getArray(file):
    array = np.genfromtxt(file, delimiter=',')
    array = array[2:]
    array = array[:, 1]
    return array
# devuelve una matriz con exponenciales complejas para valores de tiempos y frecuencias
def syn_matrix(N):
	ts = np.arange(N) / N # array de tiempos
	fs = np.arange(N)	  # array de frecuencias
	args = np.outer(ts, fs)		# matriz cuadrada con tiempos y frecuencias
	M = np.exp(1j * PI2 * args)	# matriz exponencial compleja aplicada a nuestra matriz de tiempos
	return M

## transformada discreta de fourier, devuelve un array con los valores complejos para cada frecuencia 
# correspondiente
def dft(ys):
	N = float(len(ys))
	M = syn_matrix(N)
	# primero hallamos el complejo conjugado de la matriz de exponenciales
	# luego transponemos la matriz
	# y luego realizamos un producto escalar con las muestras de nuestra señal 

	amps = M.conj().transpose().dot(ys)
	return amps

## transformada inversa
def idft(fs):
	N = float(len(fs))
	M = syn_matrix(N) # matriz de exponenciales
	# simplemente calculamos el producto escalar de nuestras frecuencias complejas
	# para cada muestra
	amps = M.dot(fs) / N
	return amps