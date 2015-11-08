// Lizenz: Creative Commons Zero 1.0

void setup() {
  size(1280,720);  //Display-Groesse bestimmen
  background(255,255,255);  //Hintergrundfarbe festlegen, weiß
  textSize(96);  // Text-Groeße bestimmen
  fill(0);  // Text-Farbe schwarz
  text("Screencast-Titel",250,300);  // Text
}

void draw() {
  for (int i=1; i<150000; i+=1) {
     point(random(1280),random(720));   // Punkte zeichnen
  }
}