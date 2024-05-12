# Radiación electromagnética en la tierra usando métodos de Montecarlo y optimización en paralelo

## Resumen

El presente proyecto desarrolla un algoritmo basado en el método de Montecarlo para estimar la radiación solar que alcanza la atmósfera terrestre con programación en paralelo utilizando MPI para Python.

## Autores

* Lucas Quiceno
* Jhoan Eusse


## Archivos

* [Plots.ipynb: ](https://github.com/EusseJhoan/Irradiacia_Paralelo/blob/main/Plots.ipynb) Notebook para graficar los datos obtenidos en los diferentes scripts.
* [SerialMontecarlo.py: ](https://github.com/EusseJhoan/Irradiacia_Paralelo/blob/main/SerialMontecarlo.py) Script para calcular la irradiancia usando computación en serie.
* [ParallelMontecarlo.py: ](https://github.com/EusseJhoan/Irradiacia_Paralelo/blob/main/ParallelMontecarlo.py) Script para calcular la irradiancia usando computación en paralelo.
* [Local_Plot.png: ](https://github.com/EusseJhoan/Irradiacia_Paralelo/blob/main/Local_Plot.png) Gráfica del tiempo computacional y el error relativo para la irradiancia en computador personal.
* [Server_Plot.png: ](https://github.com/EusseJhoan/Irradiacia_Paralelo/blob/main/Server_Plot.png) Gráfica del tiempo computacional y el error relativo para la irradiancia en servidor.


## Ejecución

Se deben ejecutar los scripts [SerialMontecarlo.py ](https://github.com/EusseJhoan/Irradiacia_Paralelo/blob/main/SerialMontecarlo.py) y [ParallelMontecarlo.py ](https://github.com/EusseJhoan/Irradiacia_Paralelo/blob/main/ParallelMontecarlo.py) para obtener los datos de la irradiancia. Con el Notebook [Plots.ipynb ](https://github.com/EusseJhoan/Irradiacia_Paralelo/blob/main/Plots.ipynb) de Jupyter se grafican los resultados obtenidos en los scripts

## Conclusiones

Usando métodos de Montecarlo con computación en paralelo se obtiene un valor de irradiancia de $4238~ W/m^2$. Este resultado no coincide con el valor teórico esperado debido a las incertidumbres que se tienen respecto al valor teórico de referencia. Nuestros resultados indican que la computación en paralelo reduce  significativamente el tiempo de cómputo. Esto es una ventaja considerable para problemas de gran escala o para situaciones donde el tiempo de respuesta es crítico. Para nuestro caso particular observamos que la convergencia del cálculo se alcanza rápidamente. Esto implica que, para nuestro problema específico, la implementación de métodos en paralelo puede no ser demasiado útil. 
