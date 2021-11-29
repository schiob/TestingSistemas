# Las pruebas de software: Ayer hoy y mañana
### Áreas principales
-*Prueba funcional:* Validar casos donde nos cercioramos que el software haga lo que tenga que hacer.

-*Prueba no funcional:* Pruebas de desempeño. ¿Hasta dónde opera mi software antes de caerse?

-*Automatización:* No sustituye a las pruebas funcionales. Si hago algún cambio, debo cerciorarme que eso no afecte alguna otra parte de mi programa.

-Seguridad:* Donde se mide la vulnerabilidad del software.

### Técnicas de prueba
-*Caja negra:* Nivel código.

-*Caja gris:* Nivel código, pero un poco más **encima**. Manejo de bases de datos y entender la funcionalidad.

-*Caja blanca:* Nivel API, a través del front. Son más comunes.

### Caso de prueba
Cada una de las funciones unitarias.

-*Entrada:* Dato o evento externo que se inyecta al sistema.

-*Precondiciones:* Estado en el que tiene que estar el sistema para capturar la entrada.

-*Salida:* Dato que sale del sistema o mensaje de resultado.

-*Postcondiciones:* Estado en el que queda un sistema después de ejecutar la entrada y las precondiciones.
Se puede validar un caso negativo. Por ejemplo poner datos erróneos en un login y eso ocasiona que no pueda entrar en el sistema. El resultado es positivo porque el software está cumpliendo su función.

### Cualidades de un tester
-*Actitud*

-*Innovar*

-*Proactivo*

-*Entendimiento rápido del negocio:* Siempre busca ejecutar mejor el trabajo, mejor cobertura de pruebas.

-*Liderar equipo de trabajo*

-*Habilidades de negociación*

**La única constante es el cambio**

### Tipos de prueba
-*Pruebas de desempeño*

-*Pruebas móviles:* Las pruebas se aplican a cualquier software sin importar la plataforma.

-*Automatización de software*

-*Prueba de seguridad:* Vulnerabilidad del software.

-*Pruebas manuales (Funcionales):* El tester evalúa entradas y salidas.

-*Administración de datos:* Para hacer pruebas se necesitan datos.

### Dimensiones de la prueba de software
-*Probador  de software*

-*Cobertura:* Encontrar la parte fallida del software con pruebas detalladas.

-*Actividades:* Evalúan probabilidad de fallo. ¿Dónde está el problema en el software? A partir de ahí nos podemos enfocaren el problema. Evaluamos el softaware para saber si cumple con los requerimientos para ser acentuada.

-*Probabilidad de fallo*

-*Evaluación:* Empezar a enfocar la estabilización software. Estar conscientes donde está el fallo con el sw.

### Pruebas estáticas
| Análisis                                  | Planeación                 | Diseño                       | 
|-------------------------------------------|----------------------------|------------------------------|
| Escenarios que se van a validar           | Plan de pruebas            | Hallazgos con el programador |
| Cantidad de casos de pruebas              | Estimación a detalle       | Reportar fallas              |      
| Estimación de lo que se va a requerir     | Tiempo en que se realiza   | Se genera el Testware        |  
| Perfiles que participan                   | Software limpio            |                              | 
| Análisis de riesgos que hay que controlar | Probabilidad de fallo baja |                              |

### Automatización 
Automatizar y sistematizar todas las actividades que se llevan de una forma manual, a través del uso de herramientas especializadas que nos ayudas a sistematizar las acciones y eventos que se verifican en una prueba de software. 
##### ¿Para qué sirve?
Sirve para pruebas de regresión. Valida que otros flujos no sean afectados en caso de hacer modificaciones. Los scripts nos ayudan a validar cada caso para no hacerlo manual. 

### Perfiles en pruebas automatizadas
-*Arquitecto de automatización:* Define procesos de automatización.

-*Analista automatizador:* Determina qué casos de prueba se automatizan y cuáles no.

-*Líder automatización:* Desarrolla plan de prueba de automatización. Ofrece avances y reportes.

-*Scripter automatizador:* Reutiliza o diseña nuevos scripts.

-*Soporte:* Da soporte en ambientes, herramientas.

-*Lider de pruebas de software:* Solicita una regresión automatizada o datos automatizados.

### Conclusiones
Algunos de los temas que se abordaron en la conferencia ya había tenido la oportunidad de estudiarlos, pero fue bueno saber que lo ya aprendido realmente son unas grandes bases para el testing, sin embargo, unos más fue muy interesante conocerlos. Como por ejemplo una de las cosas que me parecieron muy importantes e interesantes, fue el tema de la *automatización* que se mencionó en más de una ocasión, además que añadieron los perfiles de esta rama. Me gustó mucho esta conferencia, fue muy completa a pesar del poco tiempo que se es daba para explicar lo más importante de este tema.




