# Website basierend auf  Flask
Mithilfe dem Webframework Flask wird hier eine Blog-Website erstellt. Neben einem Login und einer Registration, soll es auch die Funktion geben, über den Frontend die Blogs erstellen, bearbeiten und löschen zu können (via Datenbank). Zurzeit wird es über eine Liste, die ein Dictionary enthält, gemacht. Für die UI wird Boostrap genutzt.

## Version 1
Eine einfach gehaltene Navbar besitzt die Website mittlerweile. Die Posts werden über Cards angezeigt. Highlight Posts (Beiträge, die mehr Aufmerksamkeit bekommen sollen), werden ganz oben angezeigt.

<img src="https://github.com/BassamxMednini/Website-mit-Python-Flask/blob/master/images/screenshot_1.png?raw=true" width="300" height="150" />

## Fortschritte
Die Registration-Page ist nun fertig. Je nachdem ob alle Felder ausgefüllt sind oder Angaben fehlen, wird via Bootstrap entsprechende Hinweise angezeigt. Bei einer erfolgreichen Registration wird der Benutzer zunächst einmal zur Startseite weitergeleitet und erhält dort anschließend eine success-Meldung. 

<img src="https://github.com/BassamxMednini/Website-mit-Python-Flask/blob/master/images/registration.png?raw=true" width="300" height="150" /> <img src="https://github.com/BassamxMednini/Website-mit-Python-Flask/blob/master/images/registration_fail.png?raw=true" width="300" height="150" /> <img src="https://github.com/BassamxMednini/Website-mit-Python-Flask/blob/master/images/registration_success.png?raw=true" width="300" height="150" />

## Weitere Details
Nach jeder Registration wird der User (Benutzername, Email und Passwort) in die Datenbank gespeichert. Beim Login wird überprüft, ob der User existiert und falls dies der Fall ist, wird überprüft ob die Daten (Email und Passwort) richtig sind. Hat sich der User angemeldet, wird oben im Navbar die beiden Nav-items 'Login' und 'Registrieren' entfernt und mit dem Nav-item 'Logout' ersetzt. Je nachdem ob man sich erfolgreich angemeldet hat oder nicht, wird eine entsprechende Meldung angezeigt.

<img src="https://github.com/BassamxMednini/Website-mit-Python-Flask/blob/master/images/python_login_out.gif?raw=true" width="600" height="375" />