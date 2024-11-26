# Závěrečný project na automatizované testování
Automatizované testování webu společnosti **Thajské masáže Kiwi**

Pro závěrečný projekt orientovaný na automatizované testování pomocí Pytest a Playwright jsem si vybrala webové stránky společnosti Thajské masáže Kiwi. Vzhledem k integrované ochraně proti robotům (reCaptcha) jsem nemohla otestovat vše, co by si stránky zasloužily. Vybrala jsem však 5 oblastí, které testování umožňovaly. Testy jsem prováděla na prohlížečích Chromium, Firefox a Webkit. 

## Test 1 - Testování online rezervace
Jako první oblast pro testování jsem zvolila online rezervaci, což považuji za obchodně nejdůležitější prvek na stránce, který je oproti konkurenci navíc poměrně vzácný. Testovala jsem funkčnost dropdown menu u Tradiční masáže s výběrem délky masáže (60, 90 a 120 minut) a správný přepis vybrané možnosti na stránku s vygenerovanými návrhy konkrétního volného časového slotu. Zde jsem test zastavila, jelikož se v čase následující položky mění. Testy prošly v pořádku.

## Test 2 - Testování funkčnosti košíku pro nákupu voucheru
Pro druhý test jsem vybrala funkčnost košíku pro nákup voucheru na konkrétní typ masáže pomocí parametrizovaných testů. Testy prošly v pořádku.

## Test 3 - Testování zobrazení chybové hlášky v kontaktním formuláři při vyplnění nevalidních vstupů
Třetí test se zaměřuje na kontaktní formulář, kde je třeba vyplnit jméno, email a text dotazu. Pomocí parametrizovaných testů s nevalidními vstupy jsem ověřila zobrazení chybové hlášky. Pro všechny nevalidní vstupy používá stránka stejný text chybové hlášky, proto jsem pouze ověřila její zobrazení. Testy prošly v pořádku.

## Test 4 - Testování navigace hlavního panelu
Čtvrtým testem ověřuji, zda položky navigace hlavního panelu odkazují na očekávanou URL. Testuji opět pomocí parametrizovaných testů. Testy prošly v pořádku.

## Test 5 - Testování přepnutí na anglickou verzi stránek
Pro pátý test jsem vybrala přepnutí na anglickou verzi stránek. Test prošel v pořádku.
