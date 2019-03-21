# Capítulo 5: Defectos

### ¿Qué es un defecto?
Un defecto es una discrepancia o diferencia entre el resultado esperado de tu caso de prueba contra el
resultado actual que muestra el sistema bajo prueba. Es un error funcional del código.

### ¿Qué no es un defecto?
  - Falla del sistema por causas de configuración en el ambiente.
  - Falta de datos.
  - Malos entendidos de las reglas de negocio.

### ¿Cómo registrar un defecto?
Al registrar un defecto es bueno que el desarrollador tenga toda la información necesaria. Debes tener
una plantilla con los datos a llenar, puede estar en excel, word o en una herramienta de administración de
defectos. La información en la plantilla debe estar completa.

### Datos de la plantilla de Defectos
  - Paquete
  - Origen
  - Número de desarrollador
  - Clasificación de erorres
  - Estatus
  - Prioridad
  - Severidad
  - Ciclo encontrados
  - Ciclo cerrado
  - Pasos para reproducir el error
  - Fecha de corrección del bug

### ¿Qué es un defecto accionable?
Un defecto accionable es enviar toda la información del defecto en forma clara, completa en la plantilla
del defecto para que el desarrollador responsable a corregirlo pueda accionar adecuadamente sobre la corrección

### Checklist para documentar un defecto
1.- Asegurarse que es un defecto funcional y no de ambiente
2.- Reproducir el error
3.- Tomar evidencias
4.- Documentar los pasos para reproducir el error
5.- Documentar el defecto
6.- Asegurarse que el desarrollador esté enterado de este registro de defecto

### Severidad vs Prioridad
La **severidad** se enfoca en el impacto absoluto en el desarrollo, la **prioridad** se enfoca en la importancia
al cliente final o al usuario. Para clasificarlas es importante tomar en cuenta cuatro clasificaciones.
Para la *severidad*:
  - Baja: error cosmético o estético, no hay un impacto funcional.
  - Media: la falla tiene un error menor y no perjudica la funcionalidad crítica.
  - Alta: la falla tiene un error en la ruta crítica, pero hay un camino alterno para continuar las pruebas.
  - Bloqueante: La falla detiene las pruebas. No existe un camino alterno para continuar la prueba.

Para la *prioridad*:
  - Baja: no es funcional, no se visualiza fácilmente.
  - Media: la solución implementada como camino alterno es aceptable para largo plazo.
  - Alta: la solución implementada como camino alterno es aceptable para corto plazo.
  - Urgente: El proceso diario es severamente impactado o está detenido.

Para determinar el peso del defecto tienes que multiplicar el peso de la severidad contra el peso
de la prioridad.

### Formato de Evidencias
Por cada caso de prueba tomar evidencia por lo menos de:
  - Proyecto
  - Ejecutor de pruebas
  - Título del caso de prueba
  - Ciclo de pruebas
  - Caso de prueba
  - Paso del caso de prueba
  - Video, log o imagen
  - Comentarios relevantes de la evidencia
En otros casos sólo se documenta el video y no se genera una plantilla.

### Ciclo de vida del defecto
Reportar la falla por los medio definidos, enviarla al desarrollado, el desarrollador la reproduce y corrige,
el tester vuelve a revisar que esté bien aplicada la correción y aprueba o rechaza la corrección.

El ejecutor de pruebas encuentra un *hallazgo*, si es un defecto captura el caso de prueba como no pasado. Al
registrar el defecto, se envía una notificación al líder de desarrollo y *asigna a un responsable de desarrollo*.
Al desarrollador que se le asignó el defecto, *valida que sea defecto*, si es defecto, lo corrige y lo deja en estado
contestado y notifica la solución del defecto, si no lo corrige porque no es un defecto lo rechaza y notifica que
no era un defecto. El ejecutor de pruebas *valida el defecto que esté bien corregido*. Si todo está bien, cierra el 
defecto, si no, queda en estado reincidente y se va al punto número dos.

### Matriz de defectos
Datos que debe llevar: nombre del proyecto, Id defecto, clasificación (de código, de diseño, funcional, de
requerimientos), estatus, prioridad, severidad, tester, desarrollador, descripción de la falla, ciclo de pruebas
en que se detectó el defecto, fecha en que se detectó.

### Herramienta de administración de defectos
Debe tener las opciones para poder consultar los defectos, generar nuevos defectos, ver los indicadores de los
defectos reportados. Ver descripciones de fallas. En los indicadores es importante tener métricas documentadas en
gráficos, todos los tipos de defectos.
