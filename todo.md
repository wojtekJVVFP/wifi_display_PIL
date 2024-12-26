do przygotowania funkcja do zamiany obrazka do postaci str

- do napisania program c++ pobierający dane od python'a

- do napisania program c++ do zamiany obrazka do postaci do wysłania przez websocket

Jest biblioteka, która przekształca bytes na dane binarne (struct), ale wydaje się niekompatybilna z formatem bytes z
pygame

Jak przekształcić surface do postaci możliwej do przesłania przez websockets tak żeby była możliwość przekstałcenia przez kod
c++? 
+ jak są ułożone dane odnośnie pikseli i kolorów w typie surface?
+ jak odkodować bytes po stronie c++, 

+Pomiar czasu w python
- Znaleźć miejsca gdzie program jest wolniejszy i zoptymalizować
-+ Zamieniono wymianę pociętych obiektów image (bmp) na wymianę w postaci pliku jpg (zmienne io.BytesIO)

- Poprawa rozdzielczości urządzeń. W tej chwili nie uwzględniane są paski powiadomień i dolne klawisze dotykowe przez co źle się skalują obrazki
- 
- Wprowadzić obliczanie poprawek na ramki urządzeń. Fragment obrazka, który powinien być na ramce nie będzie wyświetlany, żeby zachować ciągłość obrazka
