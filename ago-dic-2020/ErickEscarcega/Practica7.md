# Práctica 7 | QA testing Channel siguientes capítulos: 5 y 6 | Erick Escárcega

## 5 - Defectos

### Introduccion al defecto
Se le denomina como defecto a un error funcional del codigo, una diferencia entre el resultado esperado del caso de prueba contra el resultado actual que muestra el sistema bajo prueba. y al contrario, una falla del sistema por cuasas de configuracion en el ambiente, la falta de datos y los malentendidos no son considerados como defectos.

### Defetos Accionables
Para registrar o levantar un defecto primero se debe tener una plantilla con los datos a llenar la cual previamente se debio capacitar el uso de esta, despues se llena la plantilla con todos los datos solicitados y debe ser enviada al desarrollador.
Que datos contiene una plantilla de defectos?
- Paquete
- Origen
- No. de error
- Clasificacion de errores
- estatus
- Id Bug
- Prioridad 
- Severidad
- Responsable de Pruebas
- Responsable de Solucion
- Descripcion

Donde cabe mencionar que el *Id del bug* es el numero unico del defecto con el qcual se trabajo, el *estatus* puede ser cerrado, corregido, en revision, basicamente nos dice el ciclo de vida del defecto, la *severidad* nos habla de como impactara al negocio.

Se le denomina Defecto accionable al documentar claramente la informacion de la plantilla del defecto, para que que el desarrollador pueda accionar adecuadamente sobre la correccion.

Para documentar un defecto se debe:
1. Asegurar que es un defecto funcional y no de ambiente
2. Reproducir el error antes de registrarlo
3. Tomar evidencia
4. Documentar los pasos para reproducir el error
5. Documentar el defecto en la herramienta
6. Asegurarse que el desarrollador esta enterado y darle seguimiento

La severidad se enfoca en el impacto absoluto en el desarrollo y la prioridad es enfocada en la importancia al usuario/cliente. Ambas se miden con niveles de escalabilidad **Baja**, **Media**, **Alta** y **Bloqueante** o **urgente**.

Para cada caso de prueba se deben tomar los datos en el siguiente formato:
- Proyecto
- Ejecutor de pruebas
- Titulo del CP
- Ciclo de Prueba
- Caso de Prueba
- Paso del CP
- Video Evidencia
- Comentarios

### Ciclo de vida de un Defecto
Despues de reportar la falla de la manera de la que previamente hablamos, esta se envia al desarrollador para que el pueda entenderala, reproducirla y corregirla, entonces el tester vuelve a revisar que este bien aplicada la correccion y este aprueba o rechaza la correccion.

### Matriz de Defectos
Una matriz de defectos debe contener la siguiente informacion.
1. Proyecto: Nombre del proyecto al que pertenece
2. ID defecto: Un numero unico para el defecto
3. Clasificacion: Si es un defecto de codigo, ambiente, funcional, de requeriemiento o de diseno
4. Estatus: Abierto, cerrado, corregido
5. Prioridad: La prioridad del defecto
6. Severidad: La severidad del defecto
7. Tester: Quien realizo las pruebas
8. Desarrollador: Quien es el desarrollador que lo solucionara
9. Descripcion de falla: El paso a paso para reproducir la falla
10. Ciclo: El ciclo de pruebas donde se ejecuto
11. Fecha: La fecha en la que se llevo a cabo

Tambien una buena herramienta debe tener las opciones para consultar los defectos, generar un nuevo defecto, ver los indicadores, filtrar de diferentes maneras.

## 6 - Ejecucion Agil

### Introduccion a metodos agiles
Se le llama metodo agil al llevar un proyecto de forma rapida con dos puntos: ciclo de vida iterativo e incremental, lo cual permite al equipo del proyecto incorporar la retroalimentacion e ir incrementando la experiencia del equipo.

El Agile manifiesto prefiere individuos e interacciones sobre procesos y herramientas, software funcional y completo sobre Documentacion exhaustiva, Colaboracion con el cliente sobre la negociacion contractual, respuesta ante el cambio sobre seguir el plan.

El ciclo de vida incremental desarrolla por partes el producto para despues integrarlas a medida que se completan a diferencia del ciclo iterativo donde se revisa y mejora el producto. y de la union de estos dos procesos al final de cada iteracion se consigue una version mas estable del software, donde se agregan nuevas funcionalidades respecgto a versiones anteriores.

Los frameworks agiles son metodos que se crearon para apoyar el modelo de trabajo.
Centrados en ciclos iterativos e incrementales:
- Scrum
- DevOps
- LSD
- XP
- TDD

Centrados en el flujo:
- Kanban

### Pruebas Exploratorias
Las pruebas exploratorias son las que involucran aprendizaje, planeacion, ejecucion de pruebas y reportar resultados de forma simultanea. La combinacion de hacer ejecucion y diseno de pruebas en forma concurrente. Lo que no es exploratory testing es seguir un procedimiento de pruebas.

Tecnicas de exploratory testing:
- **Freestyle**: No hay reglas, son buenas para detectar problemas de usabilidad
- **Scenario Based ET**: Escenarios de prueba, casos de uso y lista de combinaciones a ejecutar
- **Feedback ET**: Derivado del freestyle, la historia construye tu futuro, requiere herramientas
- **Strategy based**: Utiliza el ADHOC combinado con metodos estandar, analisis de valores al limite y clases de partiipacion equivalente
- **Session based**: Testeo basado en metas, los requerimientos del cliente son informales.

Un posible proceso es:
Crea un modelo de conjetura -> crea una o dos pruebas que no aprueban esa conjetura -> ejecuta la prueba y observa el resultado -> Evalua la salida contra tu conjetura -> repite hasta quesea aprobada y/o Rechazada