# [PL] Projekt "WIKI"
[English README.md - soon](https://github.com/robi2212/project-wiki)<br>
**Projekt "WIKI"**[^first] to kryptonim bota[^second] do komunikatora [Discord](https://discord.com).

## Cel (Po co?)
Bot powstał w celu:
1. Rozwoju umiejętności programistycznych autora,
2. Dostarczenia niestandardowej rozrywki na serwerach, która nie jest możliwa u innych botów,
3. Automatyzacja niektórych elementów moderacyjnych, usprawniających zarządzanie dużymi serwerami.

Bot nie posiada konkretnej nazwy, ale jego kryptonim nawiązuje do imienia zwierzęcia (w tym przypadku psa). Zaleca się, aby nazwy kolejnych instacji nawiązywały do zwierząt.

## Uruchomienie i aktualizacja
### Uruchomienie
Zalecane jest skonfigurowanie i uruchomienie instancji bota na serwerze dedykowanym (VPS) z wykorzystaniem oprogramowania [Docker](https://docker.com), aby bot działał 24/7.
1. Wszystkie pliki należy pobrać i przenieść do jednego katalogu (np. discord-bot).
2. W pliku `main.py` w linijce `client.run('BOT_TOKEN_HERE')` wkleić token z utworzonej aplikacji bota w [Discord Developer Portal](https://discord.com/developers/home).<br> ([Skąd wziąć token do bota?](https://docs.discord.com/developers/quick-start/getting-started#fetching-your-credentials)).
3. Wykonać poniższe polecenie do zbudowania obrazu kontenera z botem `docker build -t nazwa_obrazu`.
4. Wykonać poniższe polecenie do uruchomienia kontenera `docker compose up -d`.
### Aktualizacja
Jeżeli pojawią się zmiany w kodzie bota, te nie zostaną automatycznie wykonywane przez kontener. 
Aby zaktualizować kod w kontenerze wymagany jest jego restart:
```docker restart nazwa_obrazu```.<br>
Aktualizacja kodu może chwilę potrwać. Jeżeli zostały wprowadzane zmiany w poleceniach lub zostały dodane nowe, te mogą potrzebować jeszcze więcej czasu do wdrożenia.

## Roadmap
Czyli co bot umie robić lub co będzie umiał robić.

### 1. Etap 0 - Witaj świecie! (ZAKOŃCZONY)
- [x] Witanie się
- [x] Żegnanie się
- [x] Polecenie /ping - gra "ping-pong"
- [x] Aktywność bota
- [x] Pierwsze easter eggi
- [x] Hostowanie bota na serwerze 24/7

### 2. Etap 1 - Komunikacja i informacja zwrotna
- [x] Bieżąca aktualizacja kodu bez konieczności budowania obrazu na nowo
- [x] Zapisywanie logów w określonym pliku na serwerze
- [ ] Wprowadzenie poleceń
    - [ ] /help - lista dostępnych komend
    - [ ] /info - podstawowe informacje o bocie
    - [ ] /user - informacje o użytkowniku
    - [x] /send_message - wysłanie wiadomości na wskazany kanał na serwerze
    - [x] /ping - rozbudowa polecenia o szybkość reakcji (w ms)
- [ ] Odpowiadanie na określone słowa + swoje imię
- [x] Rozdzielenie kodu na osobne pliki
- [ ] Witanie nowych osób na serwerze
- [ ] Żegnanie osób opuszczających serwer
- [ ] Zmiana aktywności w ustalonych odstępach czasu

### 3. Etap 2 - integracje, webhooki i API
- [ ] Zliczanie wiadomości użytkowników[^third]
- [ ] Integracja z systemem Uptime Kuma przez webhook
- [ ] Informacja o opublikowanych filmach na wskazanym kanale [YouTube](https://youtube.com)[^third]
- [ ] Liczenie "streak" codziennych opublikowanych filmów[^third]
- [ ] Pingowanie youtubera, gdy ten nie wstawi w przeciągu dnia przynajmniej jednego filmu[^third]
- [ ] Informacja o rozpoczęciu streama w serwisie [Twitch.tv](https://twitch.tv)[^third]

### 4. Etap 3 - Baza danych, cykliczne wydarzenia
- [ ] Gra "Co ja pacze?"
- [ ] Tematyczne nicki
- [ ] Wykonywanie kodu z GitHuba ze wskazanego brancha

### 5. Etap 4 - Administracja
- [ ] System warnów (ostrzeżeń dla użytkowników)[^third]
- [ ] Polecenia administracyjne (/kick, /ban itp.)
- [ ] Wstępna konfiguracja bota na nowym serwerze (możliwość wyboru dostępnych modułów)

Roadmapa może być na bieżaco aktualizowana. Etapy oznaczone jako (ZAKOŃCZONE) nie będą aktualizowane.

[^first]: Nazwa pochodzi od psa, z którym autor bawił się w dzieciństwie. Pies należał do dziadków autora.
[^second]: Bot został przygotowany w ramach realizacji próby instruktorskiej na stopień podharcmistrza 💚
[^third]: Pomysł na funkcję "zapożyczony" od bota "Sappy" z Kosmicznej Floty Jedenastka v6.9

