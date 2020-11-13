#   # Resumen de los Capítulos 5 - 6
## Capítulo 5 - Defectos
 
### 5 - 1 Introducción al defecto
#### -1 ¿Qué es un defecto?
 
- Es una discrepancia o diferencia entre el resultado esperado de tu caso de prueba contra el resultado actual que muestra el sistema bajo prueba.
- Es un error funcional del código.
 
#### -2 ¿Qué no es un defecto?
 
- Falla del sistema por causas de configuración en el ambiente.
- Falta de datos.
- Malentendido de las reglas de negocio.
 
### 5 - 2 Defectos accionables
#### -1  Cómo levantar un defecto
 
- Debes tener una plantilla con los datos a llenar, previamente te debieron capacitar en cómo usarla.
- La plantilla puede estar en un EXCEL, WORD o una herramienta de gestión de defectos.
- Llenas la plantilla con todos los datos solicitados y la envías al desarrollador.
 
#### -2 Datos de una plantilla de defecto
 
Los más relevantes son:
- ID BUG
- Estatus
- Prioridad
- Severidad
- Responsable del área de pruebas
- Responsable del área de desarrollo en la parte de solución
- Descripción del Bug
- Ciclo encontrado
- Ciclo cerrado
- Pasos para reproducir el error
- Cómo se soluciona el error
- Fecha del reporte
- Hora del reporte
- Fecha de corrección del bug
 
#### -3 ¿Qué es un defecto accionable?
 
Es documentar claramente la información de la plantilla del defecto, para que el desarrollador responsable a corregirlo pueda accionar adecuadamente sobre el defecto.
 
#### -4 Checklist para generar el defecto
 
1. Asegurarse que es un defecto funcional y no de ambiente.
2. Reproducir el error.
3. Tomar evidencia.
4. Documentar los pasos para reproducir el error.
5. Documentar el defecto en la herramienta de gestión de defectos o Excel.
6. Asegurarse que el área de desarrollo esté enterado de este registro de defecto.
 
#### -5 Severidad vs Prioridad en un defecto
 
La severidad se enfoca en el impacto absoluto en el desarrollo.
La prioridad se enfoca en la importancia al usuario / cliente final.
 
|   | Severidad | Descripción del tipo |
|---|---|---|
|1|Baja|Error cosmético o estético, no impacto funcional.|
|2|Media|La falla tiene un error menor y no perjudica la funcionalidad crítica.|
|3|Alta|La falla tiene un error en la ruta crítica, pero hay un camino alterno para continuar las pruebas.|
|4|Bloqueante|La falla detiene las pruebas y es de la ruta crítica. Se perdieron datos y funcionalidad. No existe un camino alterno para continuar la prueba.|
 
|   | Prioridad | Descripción del tipo |
|---|---|---|
|1|Baja|No es funcional, no se visualiza fácilmente.|
|2|Media|La solución implementada como camino alterno es aceptable para largo plazo.|
|3|Alta|La solución implementada como camino alterno es aceptable para corto plazo.|
|4|Urgente|El proceso diario es severamente impactado o está detenido.|
 
### 5 - 3 Evidencias de los defectos
#### -1  Formato de Evidencias
Por cada caso de prueba tomar evidencia con estos datos:
- Proyecto
- Ejecutor de Pruebas
- Título del Caso de Prueba
- Ciclo de Prueba
- Caso de Prueba
- Paso del caso de prueba
- Video, Log o imagen
- Comentarios relevantes
 
En otros casos solo se documenta el video y no se genera una plantilla.
 
### 5 - 4 Ciclo de vida de un defecto
#### -1  Ciclo de vida de un defecto
Qué hacer después de encontrar una falla:
- Reportar la falla por los medios definidos.
- Enviarla al desarrollador
- El desarrollador la reproduce y corrige.
- El tester vuelve a revisar que esté bien aplicada la corrección.
- El tester aprueba o rechaza la corrección.
 
### 5 - 5 Matriz o herramienta para los defectos
#### -1 Matriz de defectos
 
Una matriz de defectos contiene los siguientes casos:
- Proyecto
- ID Defecto
- Clasificación
- Estatus
- Prioridad
- Severidad
- Tester
- Desarrollador
- Descripción de la falla
- Ciclo
- Fecha
 
#### -2 Herramienta de gestión de defectos
 
Debe tener las opciones para consultar defectos, registrar defectos y obtener indicadores sobre estos. Debe poder filtrar la información usando los casos de una matriz.
 
Al capturar un nuevo defecto, se debe tener la posibilidad de capturar toda la información de la plantilla en una sola pantalla.
 
En la parte de indicadores se deben tener métricas documentadas en forma de gráficos.
 
 
## Capítulo 6 - Pruebas exploratorias
 
### 6 - 1 Inducción Métodos Ágiles
#### -1 Qué es un Método Ágil
- Este tipo de ciclo de vida (iterativos e incrementales) permite al equipo del proyecto incorporar la retroalimentación e ir incrementando la experiencia del equipo durante el proyecto.
- Este tipo de ciclo de vida (iterativos e incrementales) permite al equipo del proyecto incorporar la retroalimentación e ir incrementando la experiencia del equipo durante el proyecto.
 
#### -2 Agile Manifesto
- Individuos e interacciones sobre Procesos y herramientas.
- Software funcionando sobre Documentación exhaustiva.
- Colaboración con el cliente sobre Negociación contractual
- Respuesta ante el cambio sobre Seguir un plan.
 
#### -3 Ciclo de vida incremental
- Desarrollar por partes el producto software, para después integrarlas a medida que se completan.
- Es el agregar cada vez más funcionalidad al sistema.
Un ejemplo de un desarrollo puramente incremental puede ser la agregación de módulos en diferentes fases.
 
#### -4 Ciclo de vida Iterativo
- En cada ciclo, iteración (en cascada), se revisa y mejora el producto.
- Es importante señalar que este ciclo no implica añadir funcionalidades en el producto, pero si revisión y mejora.
Un ejemplo de desarrollo iterativo es aquel basado en refactorizaciones, en el que cada ciclo mejora más la calidad del producto.
 
#### -5 Ciclo de vida Iterativo e Incremental
De la unión del ciclo de vida iterativo y el incremental al final de cada iteración se consigue una versión más estable del software, de más calidad, y añadiendo además nuevas funcionalidades respecto a versiones anteriores.
 
#### -6 Concepto Iterativo e Incremental
- El producto se desarrolla por incrementos en el que cada iteración obtiene una versión funcional del producto.
- El sistema se desarrolla poco a poco, y obtiene una retroalimentación continua por parte del usuario.
 
#### -7 Ciclo de vida Ágil
Consiste de 3 fases:
1. Plan: En un plan existen product owners los cuales definen requerimientos del sistema y lo plasman en una lista de tareas llamada "Product Backlog" y se genera una hoja de ruta de plan de liberaciones en el cual se define como se liberará el Product Backlog.
2. Colaboración: La hoja de ruta plasma las liberaciones en periodos cortos de entregables, los cuales se desarrollan en la colaboración donde son de 2 - 4 semanas el desarrollo de los entregables.
3. Entrega: Después se entrega el producto a los Product Owners quienes revisan si se aceptan las entregas ya funcionales y completas, si todo sale bien, el producto se entrega al cliente y además se afecta el Backlog, eliminando de esta la parte que ya se entregó. y se va reduciendo la lista de tareas que tenemos en los requerimientos del sistema.
 
#### -8 Iteración Ágil
Se tiene una lista de control del proyecto (Product Backlog) la cual se inserta en un proceso ágil que en un tiempo fijo (time boxing) que es de 2 -4 semanas,
1. Etapa de inicialización: En esta etapa se diseña la iteración, se refina el product backlog, se define un objetivo en el cual se va a trabajar sobre un sprint.
2. Etapa de iteración: En los sprint se generaron varios módulos, se construye con análisis, diseño, ejecución , modificación, pruebas y se empiezan a generar los entregables cortos y se muestran directamente al cliente. Se hace un DEMO.
3. DEMO: En esta etapa se hace un sprint review, se revisa lo que se generó en la etapa de Iteración, es la parte del sprint donde nosotros generamos o recibimos una retroalimentación por parte del usuario.
 
#### -9 Frameworks Ágiles
Son los métodos que se crearon para apoyar a este modelo de trabajo. Pueden estar centrados en:
 
Ciclos iterativos e incrementales:
- Scrum
- DevOps
- Lean Software Development (LSD)
- XP (Extreme Programming)
- Cristal
- TDD (Test Driven Development)
 
Centrados en el flujo (concurrencia de actividades):
- Kanban
 
### 6 - 2 Pruebas Exploratorias
#### -1 ¿Qué es Exploratory Testing?
- Pruebas Exploratorias (Exploratory Testing) involucra el aprendizaje, planeación, ejecución de pruebas y reportar resultados de forma simultánea. El autor es el Dr. Cem Kaner 2001.
- Es un proceso interactivo de exploración concurrente del producto, diseño de prueba y ejecución de prueba. Extendiendo esto, la siguiente prueba que nosotros hacemos se verá influenciada por el resultado de la última prueba que realizamos haciendo Exploratory Testing. El autor es James Bach, 2001.
 
#### -2 ¿Qué no es Exploratory Testing?
Seguir un script.
 
#### -3 Exploratory Testing vs Scripted Testing
- ET es un método de prueba que es muy diferente de las pruebas con un script o procedimiento de prueba.
- Scripted Testing, es un examen secuencial de los requisitos, seguido por el diseño y la documentación de los casos de prueba, seguido de la ejecución.
- Pruebas exploratorias: aprendizaje simultáneo, diseño de pruebas y ejecución de pruebas.
 
#### -4 Técnicas de Exploratory Testing
- Freestyle
   - Adhoc (A la medida)
   - No hay reglas 
   - Son buenas cuando:
       - Te familiarizas por ti mismo con la aplicación
       - Para detectar problemas de usabilidad.
   - El Agile Tester, detectará al menos > 80% de los defectos.
 
- Scenario based ET
   - Escenarios de Prueba.
   - Casos de Uso.
   - Lista de combinaciones para ejecutar.
 
- Feedback ET
   - Es un derivado de FREESTYLE.
       - Construyes tu historia
       - La historia te guía lo que sigue, el futuro.
   - Frecuentemente usa herramientas.
 
- Strategy based
   - Utiliza ADHOC combinado con métodos estándar.
       - Análisis de valores al límite.
       - Clases de partición Equivalente.
   - Asegura que el tester tenga tips y trucos para detectar defectos.
 
- Session based
   - Testeo basado en Metas.
       - Requerimientos del cliente informales
       - Identificar Riesgos
       - Crear un Charter.
           - Se crea antes de la prueba, el objetivo y puede cambiar en base a pruebas anteriores.
       - Selección Heurística.
 
#### -5 Proceso de Exploratory Testing
 
1. Crea una conjetura o modelo mental.
2. Crea una o dos pruebas que no aprueban esa conjetura.
3. Ejecuta la prueba y observa el resultado.
4. Evalúa la salida contra tu conjetura.
5. Repite el proceso hasta que la conjetura es aprobada y rechazada.