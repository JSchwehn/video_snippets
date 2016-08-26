#!/usr/bin/env python

# Text ausblenden

# Einstellungen
text = 'Text'               # Text
textgroesse = 150           # Textgroesse in Pixel
textfarbe = 'black'         # Textfarbe
textposition = 'center'     # Textposition
schrift = 'FreeSans'        # Schriftart
hgfarbe_r = 255             # Hintergrundfarbe R
hgfarbe_g = 255             # Hintergrundfarbe G
hgfarbe_b = 255             # Hintergrundfarbe B
videobreite = 1280          # in Pixel
videohoehe = 720            # in Pixel
videolaenge = 5             # in Sekunden   
videodatei = 'text.ogv'     # Videodatei
frames = 25                 # Frames pro Sekunde
ausblenden_zeit = 5         # Einblenden in Sekunden


# Modul moviepy importieren
from moviepy.editor import *

# ColorClip erzeugen (Hintergrundfarbe)
hgfarbe = ColorClip((videobreite,videohoehe), (hgfarbe_r,hgfarbe_g,hgfarbe_b))

# TextClip erzeugen
text = TextClip(text, font=schrift, align=textposition, fontsize=textgroesse, color=textfarbe, size=(videobreite,videohoehe))

# Videolaenge bestimmen
hgfarbe = hgfarbe.set_duration(videolaenge)
text = text.set_duration(videolaenge)

# Hintergrundfarbe und Text mischen, Textclip langsam ausblenden
video = CompositeVideoClip([hgfarbe,text.crossfadeout(ausblenden_zeit)])

# Videodatei schreiben
video.write_videofile(videodatei, fps=frames)


# Hilfe fuer moviepy: https://zulko.github.io/moviepy/index.html
# TextClip - https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html#textclip
# ColorClip - https://zulko.github.io/moviepy/ref/VideoClip/VideoClip.html#colorclip

# text_ausblenden2.py
# Lizenz: http://creativecommons.org/publicdomain/zero/1.0/
# Author: openscreencast.de

