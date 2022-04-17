'''Estos son constantes que configuran todo el programa, no deben ser alterados fuera de este archivo'''

#nombre de las URLs usadas para dar servicio api
URL_NRO_RESULTADOS = 'nro_resultados'
URL_PRUEBA_RESULTADOS_CHI = 'prueba_resultados_chi'
URL_PRUEBA_RESULTADOS_KS = 'prueba_resultados_ks'

#claves para formularios de seleccion de distribucion
SELEC_DISTRIBUCION = 'selectDistribucion'
SELEC_INTERVALOS = 'selectIntervalos'
INPUT_MEDIA = 'inputMedia'
INPUT_VARIANZA = 'inputVarianza'
INPUT_DESVIACION = 'inputDesviacion'
INPUT_A = 'inputA'
INPUT_B = 'inputB'

#claves para cada distribucion
UNIFORME = 'uniforme'
EXPONENCIAL = 'exponencial'
NORMAL = 'normal'
POISSON = 'poisson'

#diccionario de distribuciones
DISTRIBUCIONES = {
    UNIFORME: "Uniforme",
    EXPONENCIAL: "Exponencial",
    NORMAL: "Normal",
    POISSON: "Poisson"
}

#diccionario para los intervalos
INTERVALOS = {
    "5": 5,
    "10": 10,
    "15": 15,
    "20": 20
}
#claves para formularios de seleccion de prueba
SELEC_PRUEBA = 'selecPrueba'

#globales para las pruebas de bondad
P_CHI = "chi_c"
P_KS = "ks"

#diccionario de pruebas de bondad
PRUEBAS = {
    P_CHI: "Chi Cuadrado",
    P_KS: "Kolmogorov-Smirnov (KS)"
}



