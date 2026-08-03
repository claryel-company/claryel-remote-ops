# CLARYEL RemoteOps — instalación y configuración privada

RemoteOps gestiona tu propio ordenador Windows, Ubuntu/Linux o macOS mediante el chat de IA que tú elijas.

## 1. Instalar

- [Instalador de Windows](../../installers/install-windows.ps1)
- [Instalador de macOS](../../installers/install-macos.sh)
- [Instalador de Ubuntu](../../installers/install-ubuntu.sh)

Ejecuta el archivo descargado. RemoteOps se instala en tu perfil de usuario, crea un espacio local privado y no desactiva la seguridad del sistema operativo.

## 2. Crear tu repositorio personal Private

Instala GitHub CLI, ejecuta `gh auth login` y después el comando que muestra el instalador:

```text
remoteops connect --path TU-RUTA-PRIVADA --create-private remoteops-mi-ordenador
```

El repositorio se crea en tu cuenta de GitHub con visibilidad `Private`. RemoteOps no lo hace público ni añade colaboradores.

Private significa oculto al público. Aun así pueden acceder tú, las personas o aplicaciones que autorices y GitHub como operador del servicio. Protege la cuenta con passkey o autenticación de dos factores.

Nunca guardes en Git contraseñas, tokens, claves, códigos de recuperación, archivos personales, chats, registros sin filtrar, bases de datos o copias de seguridad.

## 3. Verificar la privacidad

```text
remoteops privacy-check --path TU-RUTA-PRIVADA
```

Continúa solo si aparece `"ok": true`, `"visibility": "PRIVATE"` y ninguna incidencia.

## 4. Conectar ChatGPT

1. Abre **ChatGPT > Configuración > Apps > GitHub**.
2. Elige **Solo repositorios seleccionados**.
3. Selecciona únicamente `remoteops-mi-ordenador`.
4. Revisa los permisos antes de aceptar.
5. Revisa **Configuración > Controles de datos > Mejorar el modelo para todos**.
6. Nunca pegues secretos ni archivos personales en el chat.

La disponibilidad de la app GitHub y la escritura dependen del plan y el modo de ChatGPT. Una conexión de solo lectura no puede aplicar cambios.

## Límite de comunicaciones

RemoteOps contacta GitHub solo cuando conectas o sincronizas tu repositorio privado, ChatGPT solo cuando eliges usarlo y las fuentes de paquetes solo para operaciones aprobadas. Los instaladores no añaden publicidad ni analítica ajena.

Guías detalladas: [repositorio privado](../../docs/PRIVATE_REPOSITORY_SETUP.md), [ChatGPT](../../docs/CHATGPT_SETUP.md), [privacidad y red](../../docs/PRIVACY_AND_NETWORK.md).
