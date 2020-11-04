# Resumen de los Capítulos 3 - 4
 
## Capítulo 3 - Proceso de ejecución de pruebas
 
### 3 - 1 Proceso de EJecución ERA
#### -1 Modelo ERA
 
ERA (Estabilización, Regresión y Aceptación) o en inglés SRA (Stabilization, Regression and Acceptance) es un modelo de ejecución de ciclos de casos de prueba
 
1. Estabilización: En esta etapa se ejecutan el 100% de los casos de prueba, si se obtiene una efectividad menor al 80%, entonces se repite esta etapa, pero si se alcanza la efectividad igual o mayor al 80% entonces, se entra a la etapa de Regresión.
2. Regresión: En esta etapa se prueban el 20% de los casos, los que tienen asociado un defecto. Se debe generar el 100% de efectividad del 20% para pasar a la siguiente etapa, si no se consigue esto, entonces se reinicia esta etapa a menos que se consiga menos del 15%, en este caso, se regresaría a etapa de Estabilización.
3. Aceptación: En esta etapa se prueba el 20% que proviene de la etapa de Regresión y el 80% que proviene de la etapa de Estabilización durante la ejecución. Si no se obtiene el 100% de efectividad, entonces, se regresa a la etapa de Regresión. Si se pasa esta etapa, entonces se entra a la etapa de UAT (User Acceptance Test).
 
### 3 - 2 Pre-requisitos para la ejecución
#### -1 Casos de prueba
 
1. Los CP deben estar creados dentro de una matriz de prueba o en una herramienta de gestión de prueba.
2. Deben tener al menos la trazabilidad Escenario:CP:Script:Datos.
3. Deben indicar donde están almacenados, ruta oficial del proyecto de prueba o ruta en la herramienta de gestión de prueba.
4. Los CP deben estar en con VoBo (Visto Bueno) de un experto en el negocio y con el script a detalle suficiente para la reusabilidad.
 
#### -2 Datos de prueba
 
1. Para ejecutar los CP se requieren datos estáticos y dinámicos.
2. Hay que generarlos. Cada CP requiere entradas.
3. Los datos estáticos los crea el diseñador de la prueba y los dinámicos el área de ambientes. Depende de tu organización.
4. Los datos tienen que estar visibles en tu AUT (Application Under Test) o en las bases de datos.
5. Los datos no pueden ser copias productivas, ejecuta Scrambling para protegerlos.
 
#### -3 Ventana Funcional
 
1. El área de ambientes, es responsable de cuidar el choque o correlación de pruebas, es decir, que una prueba no tome los datos de otra prueba o altere los resultados de esta.
2. Para esto, se implementa la administración de ventanas de prueba funcional.
3. Para una ventana funcional se debe tener un checklist cumplido con lo siguiente:
   1. Casos de prueba listos.
   2. Datos generados.
   3. Plan de ejecución.
   4. Aplicativo AUT instalado.
   - El plan de ejecución y el aplicativo son responsabilidades del líder de pruebas.
 
#### -4 Plan de ejecución
 
1. Es el plan a seguir por los ejecutores de prueba para determinar quién y cuando inician y terminan su prueba, revisar dependencias con otras pruebas, fechas y datos.
2. Es común en equipos de 3 o más ejecutores de prueba.
3. Lo debe generar el Líder de prueba.
4. Generalmente el Plan de ejecución cambia cada ciclo de prueba.
 
- Se puede elaborar en un MS EXCEL, o en una herramienta de gestión de pruebas.
- Lo más recomendable es que uses una herramienta.
 
Un plan de ejecución se encarga de:
 
- Secuencia de ciclos de prueba.
- Secuencia de casos de prueba.
- Responsable de ejecutar casos de prueba.
- Repositorios de casos de prueba (TestWare)
- Repositorio de evidencias
   - Pasados.
   - Fallados.
- Centro de métricas - ¿Dónde reporto mi avance?
- Mecanismo y modelo de Administración de defectos.
- Estatus de casos de prueba.
- Estatus de defectos de prueba.
 
#### -5 AUT - Aplicativo Bajo Prueba
 
1. Es el aplicativo o producto de software que vas a validar con los casos de prueba previamente diseñados y asignados a ti como ejecutor de prueba.
2. Tiene que estar instalado en tu ambiente de pruebas o QA.
3. Debe instalarlo el responsable de ambiente de pruebas.
4. Debes recibir la ruta para acceder a este aplicativo así como los usuarios y passwords respectivos.
 
### 3 - 3 Roles y Responsabilidades
 
La línea de coordinaciones es esta:
- Test Manager coordina a:
   - Líder de prueba que coordina a:
       - Tester.
       - Ingeniero de prueba.
   - Líder no funcional que coordina a:
       - Ingeniero de prueba de desempeño.
       - Analista no funcional.
   - Líder Automatización que coordina a:
       - Ingeniero de prueba de automatización.
 
#### -1 Ejecutor de pruebas
 
- Ejecuta la prueba siguiendo el Script de prueba.
- Puede utilizar herramientas donde este documentados los test cases.
- Debe conocer del negocio de lo que va a probar.
 
#### -2 Ingeniero de pruebas
 
- Conoce el negocio.
- Diseña especificaciones y casos de prueba.
- Diseña procedimientos/scripts de prueba manuales.
 
#### -3 Líder de Pruebas
 
- Conoce el negocio.
- Define el esfuerzo de horas.
- Determina el equipo de trabajo.
- Diseña estrategias y plan de pruebas.
- Monitorea el desempeño e indicadores de la prueba.
- Puede suspender y reanudar la prueba.
- Cierra la prueba y genera el certificado de liberación a producción.
 
#### -4 Líder no Funcional
 
- Conoce el negocio.
- Define el esfuerzo de horas.
- Determina el equipo de trabajo.
- Diseña estrategias y plan de pruebas no funcionales.
- Monitorea el desempeño e indicadores de la prueba no funcional.
- Puede suspender y reanudar la prueba no funcional.
- Consigue la aprobación de pre-producción.
- Cierra la prueba no funcional y genera su parte del certificado de liberación a producción.
 
#### -5 Ingeniero de Pruebas de Desempeño
 
- Interpreta las necesidades cuantitativas de calidad del proyecto y el plan de prueba no funcional.
- Diseña los escenarios no funcionales.
- Diseña y construye los scripts de prueba no funcional.
- Ejecuta los escenarios diseñados.
- Obtiene las métricas.
- Interpreta las métricas.
 
#### -6 Líder de Automatización
 
- Conoce el negocio.
- Conoce arquitecturas de automatización.
- Implementa Frameworks.
- Define el esfuerzo de horas 
- Determina el equipo de trabajo.
- Diseña estrategias y plan de pruebas automatizadas.
- Monitorea el desempeño e indicadores de la prueba automatizada.
- Puede suspender y reanudar la prueba automatizada.
- Ofrece métricas y resultados de la prueba automatizada.
 
#### -7 Ingeniero de Automatización
 
- Conoce el negocio.
- Diseña scripts de automatización.
- Ejecuta Scripts de automatización.
- Conoce Frameworks.
 
#### -8 Líder de Ambiente
 
- Define la arquitectura de prueba.
- Da seguimiento a las necesidades del área.
- Monitorea el desempeño del área y ambiente de prueba.
- Define la periodicidad de actualización de datos y scrambling.
- Define el equipo, roles y responsabilidades.
 
#### -9 Dispatcher

- Recibe las solicitudes de ambiente de prueba.
- Las canaliza a los resultores específicos.
- Monitorea el desempeño de la solicitud, que se termine de forma adecuada y la atención a esta.
 
#### -10 Ingeniero de Datos o Resolutor
 
- Recibe las solicitudes de ambiente de prueba asignadas por el Dispatcher.
- Las atiende, dando respuesta y atención.
- Sea de:
   - Datos
   - Usuarios
   - Soporte
   - Accesos
   - etc.

#### -11 Desarrollador de Software
 
- Ingeniero que desarrolla el código relacionado al producto de software que estás probando.
- Responsable de corregir los defectos.
- Conoce de reglas de negocio y estructuras internas del sistema.
 
#### -12 Matriz De Escalamiento
 
1. Cuando el tester tiene algún problema y no puede continuar, escala el problema a el Ingeniero de prueba.
2. Si el Ingeniero detecta algún problema, lo escala al canal adecuado los cuales pueden ser:
   - Líder de prueba.
   - Líder de Ambiente.
   - Líder de PNP (Pruebas no funcionales).
   - Líder de automatización.
3. En el caso de que se haya escalado a cualquiera de los últimos cuatro, si estos aún tienen el problema, entonces lo escalan al Test Manager/Coordinador de la prueba.
4. El Test Manager/Coordinador de la prueba si no puede resolver el problema y necesita escalarlo, lo escala al Director de QA y de prueba de software.
5.  Si el Director de QA/Pruebas de software no puede resolver el problema, entonces, lo escala a la Dirección General de TI.