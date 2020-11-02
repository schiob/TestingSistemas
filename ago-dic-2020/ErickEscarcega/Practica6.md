# Práctica 6 | QA testing Channel siguientes capítulos | Erick Escárcega

## 3 - Proceso de Ejecucion de prueba

### Proceso de Ejeccuion de SRA
El modelo *Stabilization Regression and Acceptance* es un modelo de testing que consta de 3 ciclos donde en el primer ciclo de **Estabilizacion** se realizan el 100% de los casos de prueba, si el menos del 80% de los casos fallan se vuelve a realizar este ciclo, si mas del 80% entonces continua al ciclo de **Regresion** donde se prueba el 20% de los casos que puedieran tener asociado un defecto, este ciclo se realizara las veces necesarias para poder llegar al 100% de los casos de prueba, si se alcanza un menor al 15% se regresa al ciclo de estabilizacion pero de lo contrario y se completa el 100% brincamos al siguiente ciclo de **Aceptacion** donde se prueban todos los casos de prueba de ejeccucion, si obtenemos menos del 100% en este ciclo se regresa al ciclo pasado, pero si se obtiene lo contrario pasamos al *User Acceptance Test* o por sus siglas **UAT**.

### Pre-requisitos para la Ejecucion.
1. Los caso de prueba deben estar creado en una matriz de prueba o una herramienta de gestion de prueba como lo es TC ONE.
2. Deben tener al menos la trazabilidad Escenario, ya sean estaticos o dinamicos.
3. Deben indicar donde estan almacenados.
4. Los CP deben estar con VoBo de un analista experto y con el script a detalle suficiente.

Para ejecutar los datos de prueba son necesarios los datos estaticos y dinamicos, los datos estaticos los crea el disenador durante el diseno de la prueba y los dinamicos los crea el responsable del ambiente. Estos tienen que estar visibles en los **AUT** y no pueden ser copias productivas.

Para que los datos estaticos no sean quemados o que una prueba no tome los datos de otra, se realizan **Ventanas de prueba funcional** las cuales deben tener los siguentes requisitos
- Casos de prueba listos.
- Datos generados.
- Plan de ejecucion.
- Aplicativo AUT instalado.

El aplicativo bajo prueba es el producto de prueba que vas a validar con los casos de prueba previamente disenados y asignados a ti como ejecutor de prueba. Este tiene que estar instalado en tu ambiente de pruebas

### Roles y Responsabilidades
- **Ejecutor de Pruebas**: Ejecuta la prueba siguiendo el script de pruebas utilizando herramientas donde esten documentados los CP asi como tambien conocer del negocio de lo que va a probar.
- **Ingeniero de Pruebas**: Conoce y entiende el negocio para poder generar y disenar las epecificaciones y casos de pruebas, asi como tambien disenar los scripts de prueba manuales y procedimientos.
- **Lider de Pruebas**: Conoce el contexto general de los escenario, requerimientos y analizis. Define el esfuerzo de hora y el equipo de trabajo asi como tambien se encarga de disenar las estrategias y plan de pruebas. El tambien se encarga de monitorear el desempeno e indicadores de prueba.
- **Lider No Funcial**: El unicamente tiene que entender donde realizar sus pruebas, determina las horas y equipo de trabajo, asi como disenar estrategia y plan de pruebas no funcional. El puede suspender y reanudar las pruebas no funcionales. Consigue la aprobacion de PRE-PRODUCCION.
- **Ingeniero de pruebas de Desempeno**: Define las definiciones de calidad, disena los escenarios no funcionales y los scripts de prueba no funcionales. tambien ejecuta los escenarios disenados y obtiene las metricas.
- **Lider de Automatizacion**: Entiende que aplicativos son ejecutados frecuentemente, conoce de arquitecturas de automatizacion, implementa frameworks, disena la estrategia y plan de pruebas automatizadas, determina las horas y equipo de trabajo.
- **Ingeniero de Automatizacion**: Ejecuta los robots y automatiza todos los procedimientos, disena los scripts de automatizacion y ejecuta esos scripts.
- **Lider de Ambiente**: Define la arquitectura de prueba, da seguimiento a las necesidas del area y monitorea el desempeno del area y ambiente de prueba.
- **Dispatcher**: Recibe las solicitudes de ambiente de prueba y canaliza a los resolutores especificos.
- **Resolutor**: Recibe las solicitudes de ambiente del dispatcher, las atiende y da respuestas.
- **Desarrollador de Software**: Desarrolla el codigo relacionado al producto de software que esta probando, es responsable de corregir los defectos que detecta el ejecutor de pruebas.

## 4 - Herramientas para la Ejecucion.
### Organizacion de pruebas en herramientas ALM.
La herramiente de gestion de pruebas es una herramienta utilizada para automatizar los procesos de prueba, ayudar a gestionar los procedimientos tales como: Testware, Defectos, Indicadores, Requerimientos.

Para organizar las herramientas de prueba, al menos se deben revisar que la herramienta a adquirir tenga estos modulos, pueden tener diferentes diferentes nombre pero con el mismo proposito tales como:
- **Requerimientos**: Administra los requerimientos del proyecto.
- **Test Plan**: Administra los casos de prueba.
- **Test Lab**: Administra la ejecucion de los casos de prueba.
- **Defects**: Administra los defectos detectados durante la prueba.
- **Dashboard**: Administra los indicadores requeridos para la toma de decisiones en tiempo real.

### Evidencias de prueba.
Sirven para grabar la evidencia de la prueba que se esta realizando, ya sea exitosa o fallida

### Administracion de defectos.
Es importante registrar defectos, documentar evidencia, ciclos de vida un defectos, roles incluyendo desarrollador y tester, y los indicadores

### Administracion de ambiente.
Es importante mantener los datos siempre vivos, los diagramas de base de Datos, diagramas de servidores, diagramas de aplicativos por servidor, y la hora de ejeccucion.