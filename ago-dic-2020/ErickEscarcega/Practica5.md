# Práctica 5 | QA testing Channel primeros capítulos | Erick Escárcega

## Introduccion al curso.
El *QA Testing channel* es un grupo especializado en pruebas de software
localizado en varias partes del mundo el cual certifica el rol y el perfil
para ejecutrar las diferentes tareas del dia a dia en las pruebas, esto
mediante diferentes certificaciones como:
- ejecutor de pruebas
- Analista de pruebas
- Lider de pruebas
- Prueba de software agil

todo con el fin de aprender las bases que debe tener y las tareas que realiza
un ejecutor de prueba, asi como los puntos requeridos para cubrir este perfil

## Perfil del ejecutor de pruebas
El ejecutor de prueba tiene que saber muchas cosas, este capitulo nos ayudara
mucho a saber que tiene que hacer este ejecutor de pruebas, asi como el desarrollo
de este y su camino a seguir a travez de su camino.
Algunas de las cosas mas importantes que debe saber el ejecutor de pruebas son:
- El ciclo de vida de una prueba
- Entender el plan de prubea
- Seguir el plan de ejecucion y ciclos de prueba
- Documentar evidencias de pruebas
- Determinar si el caso de prueba es exitoso o fallido

Dentro de este capitulo se nos muestra un ejemplo de un perfil que busca la industria
y este campo laboral para los Testers, el cual por ahora suena un poco complicado y 
estresante pero se dice que al final de el curso se entendera todo lo que se busca.
Tambien se muestrea a el temario completo que estaremos cubriendo dentro de esta 
certificion para cubrir el perfil del ejecutor de pruebas y despues se describe el 
camino laboral y ruta que sigue un tester para lograr ser un especialista y como 
esta certificacion nos ayudara a conseguir toda esa informacion y conocimiento.
Las actividades del ejecutor de pruebas se pueden resumir como
- Revisar los insumos
- Validar los accesos a casos de prueba y aplicativos
- Revisar el tener datos para la prueba
- Revisar el plan de ejecucion
- Ejecutar los casos de prueba
- Documentar los resultados en herramienta
- Asegurar los entregables

## Fundamentos del ejecutor de prueba
### *Conceptos basicos*
Una prueba de software es la validacion y verificacion de los requerimientos funcionales con la intencion de encontrar errores y defectos mediante el uso de procesos, procedimientos y herramientas para garantizar un producto eficiente.
Existen dos tipos de pruebas: **Funcional** y **No Funcional**; 
La prueba funcional se divide en manual la cual es ejecutado personalmente y Automatizada la cual es ejecutada mediante software. La ventaja entre la manual y automatizada es el tiempo.
Las pruebas no funcionales se dividen en desempeno y seguridad. ambas son muy interesantes pero basicamente la de desempeno se enfoca a los atributos del sistema y la de seguridad busca detectar las vulnerabilidades de los sistemas.
El ciclo de vida de un proyecto de prueba es muy autodescriptible, los paseos que siguen son: **Analisis -> Planeacion -> Diseno -> Ambiente -> Ejecuccion -> UAT -> Cierre**.
- **Analisis**: Identifica la estrategia y estimacion para la atencion del proyecto.
- **Planeacio**: Se identifica el plan detallado para la atencion del proyecto.
- **Diseno**: En esta estapa se construye el TestWare.
- **Ambiente**: Es todo lo relacionado a Hardware y Software para realizar la prueba.
- **Ejecucion**: En esta fase se inicia la ejecucion de prueba, se documentan defectos y evidencias.
- **UAT**: en el User Acceptance Test se ejecutan solamente los casos de prueba criticos.
- **Cierre**: Aqui se cierra toda la documentacion del proyecto y se genera el certificado de prueba.

Un Script de pruebas es el medio para validar de un caso de prueba el cual debe tener todos los detalles para poder ejecutarse sin ayuda del tester que lo creo. para crear un script de pruebas se ocupan seguir diferentes reglas como:
- No tener hardcode
- tener almenos 6 pasos basicos:

    1. Como acceder a la aplicacion.
    2. como colocar las precondiciones.
    3. como ejecutar el caso.
    4. como validar el resultado esperado.
    5. Como validar las post condiciones.
    6. Como salir del sistema.

Despues se nos muestra y explica un ejemplo de script de pruebas el cual es muy util para entender como realizar uno de forma propia.

Los datos de prueba son aquellos datos que se requieren para ejecutar un prueba, requeridos para el set del ciclo de pruebas los cuales se dividen en **Estaticos** y **Dinamicos**:
los *estaticos* son aquellos cuales no desaparecen o no se queman y los *dinamicos* son los que van desapareciendo con cada test case.

Y se le llama testware a el conjunto de casos de prueba relacionados que tienen caracteristicas similares con el objetivo de integrarlos en ciclos de prueba para ser ejecutados.

### *Que es Ejecucion de Prueba?*
Se le llama ejecucion de prueba a el tomar cada caso de prueba previo y seguir un guion del procedimiento de prueba llamado Script manual para reproducirlo con los datos requeridos en esa casuistica, despues se toman cada una de ella, ya sea en matriz o herramienta y se comparan cada resultado esperado con el resultado actual. si el resultado es es diferente al esperado se levanta un defecto, si no es el caso, se continuan con las otras pruebas. Recordar siempre documentar la evidencia es muy importante. Todos estos pasos se realizan entre el diseno y el UAT.

Los test set o conjunto de casos de pruebas son como su nombre lo explica agrupaciones de casos de pruebas relacionados que tienen caracteristicas similares con el objetivo de ser integrados en ciclos de prueba para despues ser ejecutados y a diferrencia el ciclo de prueba es un conjunto de sets de pruebas los cuales son ejecutados con el 100% de los casos programados.

los estados de los casos de prueba se pueden agrupar de diferentes formas:
- **No ejecutado**: Cuando el caso de prueba no ha sido ejecutado.
- **Pasado**: el resultado del caso de prueba ejecutado es igual a el esperado.
- **Fallado**: el resultado del caso de prueba ejecutado **NO** es igual a el esperado.
- **Bloqueado**: debido a un caso fallido, el caso no puede ser ejecutado.

De igual manera se toman diferentes acciones dependiendo de los diferentes estados, por ejemplo si el estado es pasado, entonces se pasa al siguiente caso de prueba, pero si el estado es fallado entonces se levanta un defecto, mientras que si el caso es bloqueado, este se ejecutara en el siguiente ciclo de prueba.

### *Proyectos de prueba*
Hay diferentes tipos de proyectos de prueba
- **Nuevos**: Cuando se empieza a desarrollar un producto nuevo de software
- **Mantenimiento**: son modificaciones o actualizacioes a los proyectos de software ya existentes
- **Incidentes**: Son problemas productivos los cuales deben atenderse de forma inmediata

Los proyectos pasan por un estado de pre-estimacion donde se estima el proyecto general despues pasan la estimacion donde ya se refinan y detallan las pruebas y se ponen en horas, despues de hace el plan de pruebas en la planificacion, y se genera una linea base para cumplir con las horas cerradas, despues el proyecto se pone abierto y finaliza en la etapa de terminado. cabe mencionar que en cualquier momento, el proyecto puede caer supendido o cerrado por razones varias.

Los proyectos se clasifican en:
- **Administrativos**: Son proyectos internos dentro de la misma empreza
- **Evolutivos**: Son requeridos para operar la empresa
- **Normativos**: regulaciones de entidades externas 

### *Area de prueba*
estas se pueden dividir de 4 formas:
**Funcionales, No funcionales, Ambiente y Control** todas estas son cordinadas por el cordinador de pruebas el cual es responasable de:
- Definir las estrategias
- Establecer las politicas de calidad
- Define el plan de capacitacion anual
- Monitorea el desempeno de las sub-areas de prueba.

El area de pruebas funcionales valida los requerimientos funcionales del software y valida lo que el sistema debe hacer y lo que no se debe hacer.

El area de pruebas no funcionales es responsable de validar todos los requerimientos y atributos de calidad de software, valida la seguridad del sistema, valida el uso de recursos realizando pruebas de estres, de volumen, etc. para que la parte no funcional sea estable.

El area de ambiente de prueba es el area responsable de mantener el ambiente disponible para los proyectos 24/7, ademas de vigilar el ambiente validando que no entre ningun desarollador o tester sin permiso. En este ambiente se proporcionan los datos para las pruebas y se tiene un soporte antes, durante y al finalizar las pruebas.

El area de control de pruebas monitorea el desempeno de todas las areas previamente mencionadas, valida que todo se haga en tiempo, eficientemente. Monitorea el uso de herramientas, recursos y el apego a los procesos asi como son los encargados de llevar la facturacion.