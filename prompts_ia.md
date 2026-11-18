# Bitácora de uso de IA

Asistente utilizado: Codex. Las citas recogen solicitudes reales de la conversación. Los campos RTCF reconstruyen el contexto y el resultado esperado de cada solicitud.

## 1. Diagnóstico del catálogo

Solicitud: «No se ve bien el front end, por que?», con una captura de la página inicial de Django.

- **Rol:** Asistente de depuración de Django.
- **Tarea:** Identificar por qué la página principal no muestra el catálogo.
- **Contexto:** El CRUD ya tenía rutas y plantillas en EVA_3. Se veía la página inicial de Django en el puerto 8000.
- **Formato:** Diagnóstico breve, comando de reinicio y forma de verificar el resultado.
- **Resultado:** Se comprobaron los archivos de rutas y plantillas e indicó reiniciar Django. La siguiente captura mostró la grilla del catálogo.

## 2. Comprobación del error 404

Solicitud: «Sobre el 404 abri un detalle de id 12 que no existe y mira», con una captura de la respuesta de Django.

- **Rol:** Asistente de revisión de pruebas del CRUD.
- **Tarea:** Determinar si la pantalla demuestra el manejo correcto de un videojuego inexistente.
- **Contexto:** La URL /juegos/12/ coincidía con la ruta del detalle y el registro no existía. Django tenía DEBUG activo.
- **Formato:** Resultado de la comprobación y explicación breve de la pantalla.
- **Resultado:** La captura mostró que VideojuegoDetailView encontró la ruta y respondió 404 al no encontrar el registro.
