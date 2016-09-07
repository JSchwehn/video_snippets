#!/usr/bin/env python

# Video mit Text erzeugen, hineinzoomen (Text wird groesser) und rotieren

# Einstellungen
text = 'Text'               # Text
textgroesse = 150           # Textgroesse in Pixel
textfarbe_r = 0             # Textfarbe R
textfarbe_g = 0             # Textfarbe G
textfarbe_b = 0             # Textfarbe B
schrift = 'FreeSans'        # Schriftart
hgfarbe_r = 1               # Hintergrundfarbe R
hgfarbe_g = 1               # Hintergrundfarbe G
hgfarbe_b = 1               # Hintergrundfarbe B
videobreite = 1280          # in Pixel
videohoehe = 720            # in Pixel
videolaenge = 5             # in Sekunden   
videodatei = 'text.ogv'     # Videodatei
frames = 25                 # Frames pro Sekunde

# Modul moviepy importieren
from moviepy.editor import *
# Modul gizeh importieren
import gizeh

# Funktion um Frames zu erzeugen, t ist die Zeit beim jeweiligen Frame
def create_frame(t):
    img = gizeh.Surface(videobreite,videohoehe,bg_color=(hgfarbe_r,hgfarbe_g,hgfarbe_b))
    text_img = gizeh.text(text, fontfamily=schrift, fontsize=t*(textgroesse/videolaenge),
               fill=(textfarbe_r,textfarbe_g,textfarbe_b),
               xy=(videobreite/2,videohoehe/2))
    text_rotation = text_img.rotate(t*(2*3.14/videolaenge), center=[videobreite/2,videohoehe/2])
    text_rotation.draw(img)
    return img.get_npimage()

# Video erzeugen
video = VideoClip(create_frame, duration=videolaenge) 

# Video schreiben
video.write_videofile(videodatei, fps=frames)


# Hilfe fuer moviepy: https://zulko.github.io/moviepy/index.html
# Hilfe fuer gizeh: https://github.com/Zulko/gizeh

# text_hineinzoomen_rotieren.py
# Lizenz: http://creativecommons.org/publicdomain/zero/1.0/
# Author: openscreencast.de

