#!/usr/bin/env python

# Text ausblenden (mit Hintergrund)

# Einstellungen
text = 'Text'               # Text
textgroesse = 150           # Textgroesse in Pixel
textfarbe = 'black'         # Textfarbe
textposition = 'center'     # Textposition
schrift = 'FreeSans'        # Schriftart
hintergrundfarbe = 'white'  # Hintergrundfarbe
videobreite = 1280          # in Pixel
videohoehe = 720            # in Pixel
videolaenge = 5             # in Sekunden   
videodatei = 'text.ogv'     # Videodatei
frames = 25                 # Frames pro Sekunde
ausblenden_zeit = 5         # Einblenden in Sekunden


# Modul moviepy importieren
from moviepy.editor import *

# TextClip erzeugen
video = TextClip(text, bg_color=hintergrundfarbe, font=schrift, align=textposition, fontsize=textgroesse, color=textfarbe, size=(videobreite,videohoehe))

# Videolaenge bestimmen
video = video.set_duration(videolaenge)

# Textclip langsam einblenden
# video = CompositeVideoClip([video.crossfadeout(ausblenden_zeit)])
video = vfx.fadeout(video,ausblenden_zeit)

# Videodatei schreiben
video.write_videofile(videodatei, fps=frames)


# Hilfe fuer moviepy: https://zulko.github.io/moviepy/index.html
# Textclip - https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html#textclip

# text_ausblenden.py
# Lizenz: http://creativecommons.org/publicdomain/zero/1.0/
# Author: openscreencast.de
