# Proyecto Final

El proyecto final es una aplicación que se conecte a una API y a una base de datos. En conjunto con las pruebas de la aplicación y la integración con un servicio de CI.

La aplicación está dividida en:

 1. El dominio de la app, con las clases principales y las 2 interfaces (clases abstractas), de la API y la Base de Datos
 2. La implementación de la interfaz de la API
 3. La implementación de la interfaz de la base de datos.
 4. Las pruebas, tanto las unitarias como las de integración.

La integración puede ser con cualquier API para extraer información. Luego se manipule de alguna manera, agregando campos, uniendo objectos, transformadolos. Luego esos objetos guardándolos en la base de datos para obtenerlos después.

La base de datos puede ser cualquiera, pero para facilitar las pruebas les recomiendo SQLite.

## Evaluación
La evalueción del proyecto es de 30 puntos, la cuál está dividida en:

 - 10 puntos en la integración con Travis, o algún servicio de CI.
 - 10 puntos el la cobertura del código con las pruebas unitarias y de integración
 - 10 puntos en la calidad general de las pruebas.
 

