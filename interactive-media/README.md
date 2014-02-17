study-it
========

Im Fach Interaktive Medien, sollte ein MP3-Player in Java realisiert werden. Da ich dieses Fach erst später belegt hatte und mit Absprache des Professors, mir es erlaubt war, eine andere Technologie einzusetzen, als Java-Swing, entschied ich
mich für eine RCP-Anwendung mit den noch als incubation gesetzten Eclipse-e4-Tools (4.3).

Da Java gerade im Medienbereich nicht so geeignet ist, JMF wird schon länger nicht mehr weiter entwickelt, versuchte ich
meine Anwendung, mittels gstreamer und dem MLT-Framework umzusetzen, daneben habe ich noch folgende Technologien eingesetzt: Eclipse-Link für das Object-Relation-Mapping zu einer dateibasierten Datenbank (sqlite3) und zur Visualisierung eines Displays, die Programmiersprache Processing. Anfangs versuchte ich, das ganze als vaad-clipse zu realisieren, da aber die Umstellung von dem Plugin zu Vaadin7, sowie eine Umstellung auf Eclipse 4.3, noch nicht fertig war, dachte ich zunächst das Projekt, als JavaFX e(fx)clipse umzusetzen, da mir aber dafür allmählich die Zeit davon lief, blieb das Projekt ein SWT-Projekt.


Die Anwendung hat 3 Perspektiven: eine für das Abspielen von Musik und Videodateien mit der Möglichkeit Playlisten zu erstellen und besitzt eine Albensicht, welche automatisch, auf Grund der jeweiligen ID3Tags, zusammengestellt werden und
nicht selbst angelegt werden kann. Zum selbst Anlegen eines eigens definierten Albums besitzt, die Anwendung ein virtuelles Dateisystem. ID3Tags können angezeigt und bearbeitet werden.

Die 2. Perspektive gibt die Möglichkeit Filme von flashTV zu schauen und sich hier Kategorien anzulegen, momentan ist es noch so realisiert, dass der User selbst die Hash-Wert des Onlinestreamer zufügen muss.

Die 3. Perspektive beinhaltet einen Youtube-Flashplayer mit Suchfunktion und auch hier kann man sich wieder Kategorien anlegen und per Drag 'N Drop Youtube-Videos zu den Kategorien zufügen.


#HINWEIS: Da neben MLT auch gstreamer eingesetzt wird, sind momentan nur die zugehörigen .so-Dateien integriert, was heisst, dass das Programm unter Windows nicht vollständig lauffähig ist.

#TODO:  
 - Aubauens des MLT-Framework
 - Integration von OpenCV
 - Auch auf Windows vollständig zum laufen bringen
 - TV schauen ermöglichen mittels gstreamer
 - Streaming-Server integrieren
 - Zugehöriges Android App erstellen (zur Steuerung sowie Content-Streaming)
