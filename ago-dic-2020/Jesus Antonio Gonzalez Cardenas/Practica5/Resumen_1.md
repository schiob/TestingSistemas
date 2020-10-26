# Resumen de los Capítulos 0 - 2

## Capítulo 0 - Inducción al curso
The QA testing channel es un grupo de consultores especializados en pruebas de software localizados en diferentes paìses como USA, México, España e India, entre otros.

Ellos ofrecen certificados y diplomados en:

- Ejecutor de Pruebas
- Analista de Pruebas
- Pruebas de Software Ágil
- Pruebas en Mainframe
- Entre otros

¿Qué se aprenderá en el curso?

* Las tareas que realiza un ejecutor de pruebas de software
* Las bases de prueba que debe tener un ejecutor de prueba
* Los puntos importantes requeridos en la industria para cubrir el perfil del ejecutor de prueba de software

¿A quién está dirigido el curso?

* Estudiantes por egresar de universidades y deseen prepararse en áreas de empleo de Pruebas de Software
* Todo aquel profesionista que desee especializarse en y empezar una carrera en la disciplina de Prueba de Software
* Quien ya trabaja en el área de prueba pero desea especializar las funciones que realiza este perfil

## Capítulo 1 - Perfil del ejecutor de casos de prueba

El perfil debe cumplir con lo siguiente:

* Conocer sobre el ciclo de vida de una prueba
* Seguir un plan de ejecución y ciclos de prueba
* Tener conocimiento en herramientas de gestión tipo ALM
* Puede interpretar diseños de casos de prueba
* Solicita datos para la prueba
* Puede determinar si el caso de prueba es exitoso, fallido, bloqueado o detenido por error
* Interpreta indicadores y reportes de prueba
* Escribe defectos y conoce el ciclo de vida de estos
* Documenta evidencias de prueba
* Sigue un proceso de prueba establecido por la compañía Ágile o tradicional
* Conoce sobre Pruebas Funcionales, de Regresión y UAT (Aceptación de usuario)
* Conoce Manejadores de Base de datos y SQL simple
* Entiende el plan de prueba
    
### Ruta de crecimiento
|Años | Puesto|
|-----|--------|
|0 |Universidad/entrenamiento|
|0.2 |Ejecutor de prueba|
|2 |Ingeniero de prueba|
|2 |Líder de prueba|
|2-4 |Gerente de prueba|

Se puede desviar la especialización durante la parte de Ingeniero de Prueba/ Líder de prueba

* Pruebas de desempeño
* Automatización
* Seguridad

Al alcanzar el puesto de gerente de pruebas, se puede convertir en consultor

### Las actividades de un ejecutor de pruebas:

1.  Se le asigna un proyecto.
2.  Se le dan los insumos y este los revisa.
3.  Él válida accesos a los casos de prueba y aplicativos a probar.
4.  Él revisa que tenga los datos para la prueba.
5.  Él revisa el plan de ejecución.
6.  Espera señal del líder de prueba para empezar a probar.
7.  Ejecuta los casos de prueba, siguiendo los scripts.
8.  Documenta los resultados en herramienta o Matriz de Casos de prueba.
9.  Graba la evidencia y la almacena en la ruta oficial del proyecto herramienta.
10.  En el caso de que hayan defectos él los registra y envía a desarrollo, de lo contrario el caso de prueba es pasado.
11.  Si el ejecutor tiene dudas las revisa con el líder de prueba.
12.  Asegura que los entregables estén terminados.

### Insumos y entregables

Insumos:
* Repositorio de ejecución.
* Tipo de ciclo.
* Ruta de evidencias de ejecución.
* Plan de Prueba
    * Proceso y procedimientos.
    * Reglas del proyecto y ejecución.
* Ruta CP en herramienta o Matrices de prueba.
* Rutas del aplicativo a ejecutar con usuario y claves de acceso.

Entregables:

* Evidencias de ejecución.
* Casos de prueba actualizados en herramienta o matrices de prueba.

## Capítulo 2 - Fundamentos del ejecutor de pruebas

### 2-1 Conceptos básicos de pruebas
#### -1 ¿Qué es prueba de software?
Es la validación y verificación de los requerimientos funcionales
Hay que considerar los atributos de un sistema, el trabajo de verificación se realiza con la intención de encontrar errores, mediante el uso de de procesos, procedimientos y herramientas.

#### -2 Tipos de prueba
Funcionales:
* Manual - Es la prueba funcional que hacemos para validar que el sistema haga lo que tiene que hacer en apego a los requerimientos funcionales del usuario.
* Automática - Es la prueba funcional que programamos con lenguajes de programación asociados a marcos de trabajo llamados Frameworks que permite automatizar las acciones que un usuario realiza en su aplicación o sistema y reproducirla "n" veces. Es recomendable automatizar las rutas criticas.

No funcionales:
* Desempeño - Tiene un enfoque a los atributos del sistema, buscando leer el uso de recursos que el aplicativo utiliza para operar, CPU, ancho de banda, usuarios concurrentes, tiempos de respuesta, y validando que no se degrade el servicio mientras se realiza este tipo de pruebas.
* Seguridad - Prueba que utilizamos para detectar las vulnerabilidades de los sistemas WEB. Se corren una serie de algoritmos predefinidos de hackeo para identificar los huecos en los sistemas.

#### 3 Ciclo de vida de una prueba de software
1. Análisis - Fase para identificar la estrategia y estimación para la atención del proyecto
2. Planeación - Fase para identificar el plan detallado para la atención del proyecto. Este puede contener el plan de trabajo, equipo, método, alcance entre otros.
3. Diseño -  En esta etapa se construye toda la materia de prueba llamada TestWare: Casos de prueba, datos de prueba, defectos estáticos.
4. Ambiente - Es la etapa final para tener todo listo para el ambiente de prueba: instalar el software a probar, generar los datos para la prueba y hacer pruebas de humo. Es todo lo relacionado a hardware y software para realizar la prueba.
5. Ejecución - En esta fase inicia la ejecución de la prueba, tomamos todo el testware diseñado previamente, y ejecutamos cada caso de prueba. Se documentan defectos y evidencias de la prueba.
6. UAT (User Acceptance Test) - Fase para ejecutar las pruebas de usuario, en este momento alcanzamos a tener el software estable.
7. Cierre - En este momento cerramos toda la documentación del proyecto y generamos el certificado de prueba que avala el trabajo realizado durante la ejecución y UAT.

#### -4 ¿Qué es un caso de prueba?
Consiste de:

* Entradas: Dato o evento externo que se inyecta en el sistema.
* Precondiciones: Estado en el que tiene que estar el sistema para capturar la entrada.

Si las precondiciones son adecuadas, se ejercita el sistema se obtendrá:
* Salida: Dato que sale del sistema o mensaje de resultado.
* Poscondición: Estado en el que queda el sistema después de ejecutar la entrada y precondición.

Un caso de prueba consiste en encaminar las rutas críticas, alternas y excepcionales de un producto de software para validar que pueda generarse la prueba de lo que el sistema debe hacer y lo que no debe hacer.

#### -5 ¿Qué es un script de pruebas?
* Es el paso a paso o conjuntos de pasos, para reproducir un caso de prueba.
* Es el medio para validar un caso de prueba.
* Este debe tener todos los detalles para poder ejecutarse sin ayuda del tester que lo creo.

Reglas de un procedimiento de pruebas:
* No contener datos duros.
* Debe tener al menos 6 pasos básicos:
    1. Cómo acceder a la aplicación
    2. Cómo colocar las precondiciones
    3. Cómo ejecutar el caso
    4. Cómo validar el resultado esperado
    5. Cómo validar las post-condiciones
    6. Cómo salir del sistema

#### -6 Datos de prueba
* Son aquellos datos que se requieren para ejecutar una prueba.
* Datos requeridos para el set de prueba.
* Cada Test Case requiere de entrada
* Tipos de datos:
    * Estáticos (No se queman)
    * Dinámicos (Se queman)

#### -7 ¿Qué es TestWare?
Elementos producidos durante el proceso de prueba necesarios para planificar, diseñar y ejecutar pruebas, tales como documentación, scripts, entradas, resultados esperados, procedimientos de configuración y aclaración, archivos, bases de datos, entorno y cualquier software o utilidades adicionales que se utilicen en las pruebas.

Un proceso de negocio tiene requerimientos los cuales tienen escenarios los cuales tienen casos de pruebas, hay una relación de N a 1 por cada entre cada nivel. Los procedimientos de pruebas son el paso a paso para reproducir los casos de prueba. Un procedimiento de prueba puede tener de 1 a N casos de prueba.

Set de pruebas: Conjunto de casos de prueba relacionados que tienen características similares. El objetivo es integrarlos en ciclos de prueba para su ejecución

### 2-2 ¿Qué es ejecución de prueba?
#### -1 ¿Qué es la ejecución de la prueba?
* Es tomar cada caso de prueba previamente diseñado por un tester analista o ingeniero de prueba y seguir el guión del procedimiento de prueba (Script manual) para reproducirlo con los datos requeridos en esa casuística.
* Si el resultado esperado es igual al actual el caso es pasado, de lo contrario se falla y levanta un defecto al desarrollador.
* Siempre se documenta una evidencia de la ejecución de la prueba.
* Los casos de prueba se agrupan y se ejecutan en ciclos de prueba.
* Hay una línea del tiempo para realizar esta ejecución, así como una duración estimada para cada caso de prueba.

#### -2 Parte del proceso donde se detona
Entre la fase de diseño de prueba y la fase de UAT.

#### -3 Test Set o grupo de casos de prueba
* Es el conjunto de casos de prueba relacionados que tienen características similares.
* El objetivo es integrarlos en ciclos de prueba para su ejecución.

#### -4 ¿Qué es un ciclo de prueba?
* Es un conjunto de set de pruebas.
* Se ejecuta el 100% de los casos de prueba programados.

#### -5 Estatus de un caso de prueba
Estados que puede tomar un caso de prueba durante se ejecución. El tester ejecutor es el que cambia el estatus del caso de prueba durante su ejecución.

* No-Ejecutado: El caso de prueba no se ha iniciado en su ejecución.
* Pasado: El resultado esperado es igual al actual que arrojo el sistema durante la ejecución.
* Fallado: El resultado esperado NO es igual al actual que arrojo el sistema durante la ejecución.
* Detenido por error o bloqueado: Debido a un caso de prueba fallado este caso no se puede ejecutar.

### 2-3 Proyectos de prueba
#### -1 Tipos de Proyectos de prueba
* Nuevos
    * Desarrollos grandes
* Mantenimientos
    * Modificaciones y actualizaciones a desarrollos existentes
* Incidentes
    * Problemas productivos

Cuando se va a dar de alta un proyecto en un sistema, al menos se debe de tener:
* Nombre del proyecto
* Tipo de proyecto
* Estatus del proyecto
* Unidad de negocios a la que pertenece
* Fecha de inicio y fin
* El nombre del coordinador del área de la unidad de negocios
* El nombre del desarrollador
* El nombre del ejecutivo de pruebas
* El nombre del ingeniero de prueba
* El número de cambio
* Si tiene proyecto padre y el proyecto al que pertenece
* El número de ciclos de prueba planeados
* El tipo de proyecto que es
* En qué país se ejecuta
* Ruta del repositorio oficial del proyecto
* Descripción de la estrategia de prueba.

#### -2 Estatus de proyectos
1. Pro-estimación
2. Estimación
3.  Planificación
4. Línea Base
5. Abierto
En cualquier momento puede pasar a los siguientes estados:
    * Suspendido
    * Cancelado
6. Terminado

#### -3 Clasificación de proyectos
* Evolutivos - Son los que se requieren para operar la empresa.
* Normativos - Son regulaciones de entidades externas (principalmente gubernamentales) que nos obligan a generar esas acciones en nuestro sistema y reportarlas a ellos.
* Administrativos - Son proyectos internos para gestiones operacionales de la misma empresa.

### 2-4 Áreas de prueba
En un área de pruebas normalmente hay un coordinador de pruebas, quien coordina las áreas de pruebas funcionales y no-funcionales, Ambiente y Governance. Este tiene las siguientes características:
* Responsable de coordinar áreas de prueba.
* Define las estrategias de cobertura anuales.
* Responsable de la calidad de los productos.
* Establece las políticas de calidad en el área.
* Define el plan de capacitación anual.
* Monitorea el desempeño de las sub-áreas de prueba.

#### -1 Funcionales
* Valida los requerimientos funcionales del software
* Valida lo que el sistema debe hacer y lo que no debe hacer.

#### -2 No-Funcionales
* Valida los requerimientos de calidad de software.
* Valida todos los atributos del sistema.

#### -3 Ambiente
* Mantiene el ambiente de pruebas disponible para los proyectos.
* Vigila la integridad del ambiente.
* Proporciona datos para la prueba.
* Da soporte de antes, durante y al final de la prueba.
* Genera accesos y permisos especiales para acceder al ambiente.
* Cuida correlaciones y administra las ventanas de tiempo de prueba.

#### -4 Control o Governance
* Monitorea el desempeño de las áreas.
* Monitorea el uso de las herramientas.
* Monitorea el apego a los procesos.
* Vigila el uso de los recursos.
* Lleva la facturación.
* Vigila SLAs (Service Level Agreement).
* Ofrece indicadores para la toma de decisiones.
* A veces es mentor.