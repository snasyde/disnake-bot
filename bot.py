import os
import disnake
import asyncio
from disnake.ext import commands
from dotenv import load_dotenv
from logger import bot_logger

# Laden der Umgebungsvariablen aus der .env-Datei
load_dotenv()

# Pfad zum Arbeitsverzeichnis des Bots
PATH = os.getcwd()

class Bot(commands.Bot):
    def __init__(self, intents=disnake.Intents.all(), *args, **kwargs):
        super().__init__(command_prefix=f'<@{self.user.id}>', intents=intents, *args, **kwargs)

        # Entfernen des Standard-Hilfebefehls
        self.remove_command('help')

        # Eine Liste, um alle geladenen Erweiterungen zu speichern
        self.EXTENSIONS = []

        # Initialisierung des Logger-Objekts
        self.LOGS = bot_logger

    async def load_extensions(self):
        cmds_dir = os.path.join(PATH, 'extensions')

        # Asynchrone Durchführung von os.scandir() in einem separaten Thread
        async for entry in asyncio.to_thread(os.scandir, cmds_dir):
            if entry.is_file() and entry.name.endswith('.py'):
                cmd_path = os.path.join(cmds_dir, entry.name)
                cmd_module = f'extensions.{os.path.relpath(cmd_path, cmds_dir)[:-3].replace(os.sep, ".")}'
                try:
                    # Laden der Erweiterung mit load_extension()
                    self.load_extension(cmd_module)

                    # Hinzufügen der geladenen Erweiterung zur Liste
                    self.EXTENSIONS.append(cmd_module)

                    # Protokollierung der geladenen Erweiterung
                    self.LOGS.info(f'{cmd_module} geladen')
                except ImportError as e:
                    # Protokollierung von Fehlern beim Laden der Erweiterung
                    self.LOGS.warning(f'{cmd_module} kann nicht geladen werden: {e}')
                except Exception as e:
                    self.LOGS.warning(f'Fehler beim Laden von {cmd_module}: {e}')

    async def on_ready(self):
        # Protokollierung, wenn der Bot erfolgreich eingeloggt ist
        self.LOGS.info(f'Logged in as {self.user}')
        await self.load_extensions()