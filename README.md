# Discord Music Bot

Un bot de música para Discord que permite a los usuarios reproducir música en un canal de voz, pausar, reanudar y saltar canciones mediante botones interactivos.

## Contribuciones

Antes que nada dar créditos al repositorio https://github.com/Aguspium/PiumBot/tree/main. Gracias a este he podido seguir una estructura de código limpia y ordenada.


## Funcionalidades

- Reproducir música desde enlaces de YouTube.
- Pausar y reanudar la reproducción.
- Saltar canciones.
- Controlar la música mediante botones interactivos.
- Desconexión automática del canal de voz si no hay actividad.

## Requisitos

- Python 3.8 o superior
- `discord.py` (versión 2.0 o superior)
- `yt-dlp`
- `ffmpeg`

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu_usuario/discord-music-bot.git
   cd discord-music-bot
   ```

2. Crea un entorno virtual:

   ```bash
   python -m venv .venv
   ```

3. Activa el entorno virtual:

   - **Windows:**

     ```bash
     .venv\Scripts\activate
     ```

   - **Linux/MacOS:**

     ```bash
     source .venv/bin/activate
     ```

4. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

5. Asegúrate de tener `ffmpeg` instalado en tu sistema.

## Uso

1. Crea un archivo `.env` en la raíz del proyecto y añade tu token de Discord:

   ```plaintext
   DISCORD_TOKEN=tu_token_aqui
   ```

2. Ejecuta el bot:

   ```bash
   python src/main.py
   ```

3. Invita al bot a tu servidor de Discord y utiliza el comando `!controls` para ver los botones de control.

## Comandos

- !controls: Muestra los botones de control de música.

- !play `<song>`: Reproduce la la canción dada.

- !pause: Pausa la música que se está reproduciendo actualmente.

- !resume: Reanuda la reproducción de la música pausada.

- !stop: Detiene la reproducción de la música y limpia la cola.

- !skip: Salta a la siguiente canción en la cola.


