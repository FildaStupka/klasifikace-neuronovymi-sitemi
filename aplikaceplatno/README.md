**Manuál ke spuštění aplikace platno.py ke středoškolské odborné práci Filipa Stupky o neuronových sítích:**

1. Je potřeba mít nainstalovaný Python. Instrukce k instalaci: https://www.python.org/downloads/
2. Pokud jsou soubor platno.py a složka parametry-939 uložené v komprimovaném souboru typu .zip pojmenovaném aplikaceplatno.zip, extrahujte je.
3. Program platno.py a složka parametry-939 musí být umístěny ve stejné složce.
4. Pro správné spuštění bude možná potřeba nainstalovat některé Python knihovny. Jejich výčet i s internetovými odkazy s instrukcemi pro instalaci uvádím zde:
	- Tkinter - https://www.geeksforgeeks.org/how-to-install-tkinter-in-windows/
	- NumPy - https://numpy.org/install/
	- PIL - https://pillow.readthedocs.io/en/latest/installation.html
	- Matplotlib - https://matplotlib.org/stable/users/installing/index.html
	- OpenCV - https://pypi.org/project/opencv-python/
	- Ghostscript (64bit) - Ghostscript AGPL Release - https://www.ghostscript.com/releases/gsdnld.html

5. Aby fungovala knihovna Ghostscript, je potřeba v nastavení počítače nastavit v proměnné prostředí Path cestu do složky bin a temp, kde se knihovna nachází. U mě například cesta do složky bin vypadá následovně: C:\Program Files\gs\gs10.01.1\bin\. Postup pro Windows: Nastavení -> Systém -> O aplikaci -> Upřesnit nastavení systému -> Proměnné prostředí -> V Uživatelské proměnné uživatele (jméno uživatele) otevřete proměnnou Path -> Zadejte nové cesty C:\Program Files\gs\gs(verze Ghostscript)\bin\ a C:\Program Files\gs\gs(verze Ghostscript)\temp\ (verzi Ghostscript naleznete na stránce, kde jste ghostscript stáhnuli, viz https://www.ghostscript.com/releases/gsdnld.html) -> Stiskněte OK -> Stiskněte OK -> Stiskněte OK -> Restartujte počítač

6. Nyní by již měl program jít bez problému spustit třeba z prostředí IDLE stiknutím klávesy F5, případně přes tlačítko Run -> Run Module
