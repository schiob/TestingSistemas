# Practica 7

Toma tu ejercicio de la práctica 6 y define una serie de pruebas integrales para probar las llamadas entre funciones del proyecto.

Utiliza un método de top-down para hacer las pruebas, esto definiendo un `test-driver` que ejecute la función principal a la vez que carga todos los mocks correspondientes.

Se tendrán que crear mocks para casi todas las unidades y se irán utilizando conforme avanzan las pruebas de integración.

Como vimos en el tema de pruebas de integración, cuando estamos haciendo las pruebas `Top-Down` en la primera serie de pruebas vamos a utilizar solo una dependencia real y el resto serán mocks. En nuestro ejemplo la función principal tiene 2 dependencias, así que se reemplazará una con su mock y se ejecutarán varios casos de prueba.

Luego, en el siguiente set, este mock se va a quitar y se usuará la dependencia real. Pondiendo solo mocks de segundo nivel (dependencias de las dependencias).

Se tendrán que ejecutar diferentes sets de pruebas, donde de forma incremental se vayan reemplazando mocks por dependencias reales hasta que todo el sistema esté completamente integrado y probado.
