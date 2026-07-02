PRVA LABORATORIJSKA VJEŽBA: SIMETRIČNA KRIPTOGRAFIJA

1. MEHANIZAM ZAŠTITE ZAPORKI

Sustav osigurava pohranjene zaporke kombinacijom suvremenih 
kriptografskih algoritama:

a) PBKDF2:
Glavna zaporka (master password) se ne koristi izravno kao 
ključ. Umjesto toga, sustav koristi PBKDF2 s fiksnom soli 
(salt) kako bi generirao 128-bitni AES ključ. Ovo štiti 
sustav od brute-force napada.

b) AES-EAX:
Za enkripciju se koristi AES u EAX načinu rada. EAX pruža 
autentičnu enkripciju, što znači da osim povjerljivosti 
(da nitko ne vidi lozinku), sustav jamči i integritet 
(da nitko nije mijenjao podatke). Svaki unos ima svoj 
jedinstveni 'nonce' i 'tag'.

c) SHA-256:
Adrese servisa (npr. google.com) pohranjuju se kao SHA-256 
sažeci s dodatkom tajnog niza. Time je onemogućeno da 
napadač jednostavnim pregledom datoteke ne sazna koje servise 
korisnik koristi.

2. SIGURNOSNI ZAHTJEVI

Sustav zadovoljava sljedeće zahtjeve:

-POVJERLJIVOST ZAPORKI: Zaporke su kriptirane algoritmom AES. Bez 
poznavanja master zaporke, sadržaj je nečitljiv. Ne mpže odrediti jesu li zaporke za 
dvije različite adrese jednake, duljinu zaporke te pri promjeni zaporke
za adresu ne može odrediti je li ostala ista.
POVJERLJIVOST ADRESA: Napadač ne može odrediti adrese jer su pohranjene kao
SHA-256 sažeci.
OTPORNOST NA ANALIZU: Zbog korištenja nasumičnog nonce-a, 
ista zaporka spremljena za dva različita servisa rezultirat 
će potpuno različitim kriptogramima u datoteci.

3. STRUKTURA POHRANE

Podaci se u 'lab1passwords.txt' pohranjuju u formatu:
[Hash adrese] [Kriptogram zaporke] [Tag] [Nonce]

4. UPUTE ZA KORIŠTENJE I AUTOMATSKO TESTIRANJE

Master password je lab1mp.

Sustav podržava naredbe:
get [Master password] [adresa] (dohvat adrese)
put [Master password] [adresa] [zaporka] (dodavanje adrese u bazu)
delete [Master password] ("resetiranje" baze)
exit (izlaz)


Za automatsko testiranje, pozicionirati se unutar mape i pokrenuti automatic.sh s naredbom ./autimatic.sh.

Opis naredbi unutar testnog primjera:

put lab1mp google.com 123	-- Ispravan unos zaporke
get lab1mp google.coM		-- Ispravan dohvat zaporke
put lab1mp google.com 12345	-- Ispravna zamjena zaporke 
get lab1mp google.com		-- Dohvat koji potvrđuje zamjenu zaporke
put lab1mp instagram.com sifra	-- Ispravan unos druge zaporke
get lab1mp instagram.com sifra	-- Ispravan dohvat druge zaporke
put labospas instagram.com provjera	-- Unos zaporke s krivim masterom
get labospas google.com		-- Dohvat zaporke s krivim masterom
uzmi labmp1 google.com		-- Nepostojeća naredba
get lab1mp facebook.com		-- Dohvat nepostojeće adrese
delete lab1mp				-- Brisanje baze
Y
exit						-- Izlaz

Sustav je testiran na Ubuntu 24.04.2



