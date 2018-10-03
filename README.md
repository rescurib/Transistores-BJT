# Transistores-BJT
Módulo en Python y notebooks con ejemplos para el diseño de amplificadores de baja potencia.

Funciones del modulo:

divisor.closest(R,tol = 10,err = 0.1): Retorna el valor comercial de la resistencia más cercana a R con un error = "err" (por ahora solo retorna resistecnia de 10% toleracia )

divisor.k_r(V_rate) : Retorna un valor de escalamiento para construir un divisor de voltaje dada una razón de voltajes Vout/Vin.

divisor.R1_given_R2(R2,k_r): Retorna el valor de la resistencia R1 dada R2.

divisor.R2_given_R1(R1,k_r): Retorna el valor de la resistencia R2 dada R1.
