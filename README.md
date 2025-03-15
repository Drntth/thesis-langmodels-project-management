# Szakdolgozat: Nyelvi modellek a projektmenedzsmentben

---

## Bevezetés

Szakdolgozatom témája a "Mesterséges intelligencia a webalkalmazásokban", melynek kiválasztásakor személyes és szakmai motivációk is vezéreltek.

Szakmai szempontból fontos megemlíteni, hogy a mesterséges intelligencia (továbbiakban MI) napjainkban egyik legdinamikusabban fejlődő területe, mely egyre nagyobb területen jelenik meg a webalkalmazásokban is. Az MI számos üzleti feladatot képes ellátni, melyek bizonyos szintű intelligenciát igényelnek, ennek feltétele, hogy az ehhez szükséges tudás digitálisan elérhető legyen és fel lehessen használni a modellek betanításához. Ilyen alkalmazások lehetnek például a valós idejű interakciót igénylő ügyfélszolgálati asszisztensek, melyek a természetes nyelvi feldolgozást és a gépi tanulási algoritmusokat felhasználva képesek a beszéd felismerésére, tehát az ügyfelek szándékainak megértésére. Ezen kívül hatékonyan használható intelligens személyre szabott ajánlórendszerek létrehozására, melyek a felhasználók viselkedési adatai alapján szolgáltatnak releváns termékeket és tartalmakat.[Forrás](https://www.ibm.com/think/topics/artificial-intelligence-business-use-cases) Mivel az MI integrálására egyre nagyobb az igény, így fontos a programozóknak is lépést tartani.

Személyes érdeklődésem az egyik egyetemi kurzuson alakult ki a témával kapcsolatban, az **Alkalmazások fejlesztése projekt labor II.** gyakorlati tárgy keretein belül. Itt egy csapatmunka során egy hasonló webalkalmazás fejlesztésében vettem részt, ahol az én feladatom volt a mesterséges intelligencia implementálása. Ezen időszak során olyan tudásra és tapasztalatra tettem szert, mely felkeltettem az érdeklődésem a témával kapcsolatban és eldöntöttem, hogy a szakdolgozatomat is ebben szeretném megírni, illetve később a karrierem során is ebbe az irányba szeretnék tovább haladni.

A szakdolgozatom célja egy olyan webalkalmazás létrehozása, mely elősegíti az adminisztratív feladatok elvégzését egy projekt során, különösen a dokumentációk és specifikációk elkészítését. A program egy intuitív és könnyen kezelhető felületet biztosít, ahol a felhasználók különböző nyelvi modellek segítségével gyorsan és hatékonyan hozhatnak létre dokumentációkat.

Arra a kérdésre keresem a választ, hogy az ingyenesen elérhető nyelvi modellek, hogyan használhatóak fel hatékonyan minimális hardverigény mellett, miközben a generált szöveg minősége megfelelő marad. A nagy paraméterszámú modellek futtatásához olyan erős hardver szükséges, mellyel nem rendelkezem, ezért figyeltem arra, hogy a kisebb paraméterszámú modellek esetén milyen technikákkal lehet jobb eredményt létrehozni. Ehhez különböző promptolási technikákat és programozási eszközöket használtam fel.

A legnagyobb kihívást az jelenti, hogy a generált szövegek mennyire tűnnek értelmesnek és használhatónak emberi szemmel nézve. Mivel a specifikációk tartalmát objektívan számokkal mérni nehéz, ezért a fő szempont az, hogy az eredmény mennyire felel meg a felhasználók elvárásainak és milyen mértékben segítik munkájukat. Ezt a problémát jól szemlélteti Alan Turing gondolata: "A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." Ez az idézet a Turing-teszt alapgondolatát tartalmazza, mely azt vizsgálja, hogy egy mesterséges intelligencia modell képes-e olyan módon kommunikálni, hogy az emberek azt higgyék róla, hogy egy másik emberrel beszélgetnek.[Forrás](https://plato.stanford.edu/archives/win2021/entries/turing-test/) A szakdolgozatom egyik kulcskérdése, hogy az MI által generált szövegek mennyire közelítik meg ezt az elvárást és milyen módszerekkel lehet ezt javítani.

A rendszer letölthetővé teszi a generált dokumentumokat Markdown formátumban, így biztosítva azok könnyű kezelését és szerkeszthetőségét különös tekintettel a GitHub platformmal való kompatibilitás céljából.

Ez a webalkalmazás egy hatékony eszközt kínál az olyan fejlesztőknek, akik az MI alapú dokumentumkezelést szeretnék beépíteni a munkafolyamataikba a projektfeladatok során.

Szakdolgozatom több olyan fejezetre tagolódik, melyek egymásra épülnek és logikus sorrendben vezetnek végig a kutatási, tervezési és fejlesztési folyamatokon. Ezen felépítés az alábbi:

- **Elméleti háttér**: Ebben a fejezetben mutatom be a témához kapcsolódó alapfogalmakat és ismereteket. Bemutatom webalkalmazások működését, a felhasznált mesterséges intelligencia modelleket és azok működését, a mesterséges intelligencia szerepeit a webalkalmazásokban, az informatikai projektmenedzsment alapjait, az implementált specifikációk részleteit és néhány hasonló projektet is.
- **Megvalósítandó feladat ismertetése**: Ez a rész tartalmaz egy részletes leírást a projektről, illetve meghatározza a célkitűzéseket. Ismertetem a funkcionális és a nem funkcionális követelményeket, a felhasználói eseteket és az ehhez tartozó diagramokat, valamint a rendszer architektúráját.
- **Tervezés és fejlesztés**: Itt van részletesen bemutatva az alkalmazás tervezési és fejlesztési folyamata. A fejezet magában foglalja a rendszertervet, beleértve a felhasznált technológiákat, az adatbázis terveit (sémát, diagramot), valamint azt, hogy lehet más adatbázisokra is implementálni a projektet. Röviden ismerteti a felhasználói felület tervezését, majd részletesen kifejti a felhasznált backend és frontend technológiákat. Végül a konténerizáció és a biztonsági tervezés szerepét fejti ki.
- **Tesztelés és validáció**: Azon tesztelési stratégiákat és módszereket tartalmazza, melyeket alkalmaztam, megemlíti a tesztelési típusokat és eszközöket és ismerteti a tesztelési folyamatot is.
- **Fejlesztési és felhasználói dokumentáció**: Olyan leírások szerepelnek itt, melyek hasznosan lehetnek mind a fejlesztés mind a felhasználás során. Először a rendszer felépítését ismerteti, amely megkönnyíti más fejlesztők munkáját, mivel részletesen ismerteti a projekt struktúráját és működését. Utána következik a telepítési útmutató, ami kifejti a letöltéshez és futtatáshoz szükséges lépéseket. Végül pedig egy olyan használati útmutatót tartalmaz, mely részletesen leírja a különböző szerepkörökkel történő rendszerhasználatot.
- **Összegzés**: Az utolsó fejezetben értékelem a kutatási, tervezési és fejlesztési folyamat során szerzett tapasztalataimat, majd levonom ezekből a következtetéseket és bemutatom a rendszer bővítési és továbbfejlesztési lehetőségeit.

A szakdolgozatom forráskódja elérhető ezen GitHub repozitóriumban: **[GitHub link]**  
Az alkalmazás DockerHub image-je pedig itt található: **[DockerHub link]**

---

## 1. Elméleti háttér

### 1.1. Webalkalmazások általános bemutatása

A webalkalmazás (angolul web app vagy web application) egy olyan számítógépes program, melyet egy szerver futtat, és amelyet a felhasználók webböngészőn keresztül érhetnek el. Ide sorolandó még minden interneten kínált szolgáltatás, például a közösségi médiás oldalak, a webshopok vagy a különböző streaming szolgáltatások is. Előnyei közé tartozik, hogy biztosítja a platformfüggetlenséget, tehát több különböző operációs rendszerrel is kompatibilis, mert a webböngésző biztosítja a futtatási környezetet. A webalkalmazások szinte bármilyen internetkapcsolattal rendelkező készülékről elérhetőek, valamint nem tárolódnak a felhasználók eszközén, így azokat nem kell sem letölteni sem telepíteni. Használható több különböző eszközről egyidejűleg is, ezzel támogatva a csapatmunkát, ami kifejezetten hasznos lehet bizonyos a szöveg- és képszerkesztési feladatban vagy az adminisztratív folyamatok során.[Forrás](https://www.britannica.com/topic/Web-application)

A működéshez szükség van a már említett internetre, ami egy olyan globális hálózat, amely számítógépeket és egyéb eszközöket kapcsol össze és lehetővé teszi az információk gyors áramlását. Az internetszolgáltatók biztosítják a felhasználók számára a hozzáférést, akik saját eszközeikkel kapcsolódnak ehhez a hatalmas hálózathoz. A 21. században a Wi-Fi széleskörű elterjedésével ez a vezetéknélküli kapcsolat már szinte bárhol rendelkezésre áll.[Forrás](https://www.britannica.com/technology/Internet )
Az interneten megtalálható tartalomhoz a World Wide Web (WWW) információszerző szolgáltatás biztosít hozzáférést a felhasználók számára. Ezeket az információkat hivatkozások kötik össze, így lehetővé teszik az egyes oldalak közti navigálást vagy más szerveren tárolt dokumentumok, képek, hangok, videók megtekintését.[Forrás](https://www.britannica.com/topic/World-Wide-Web)
A webböngészők olyan kliens szoftverek, melyek lekérik a szerveren tárolt adatokat és megjelenítik azokat a felhasználók számára. Feladata, hogy értelmezze HTML által definiált jelölőcímkéket és megformázva megjelenítse szabványos stílusban.[Forrás](https://www.britannica.com/technology/browser)
Az URL-eket (Uniform Resource Locator) a számítógépek a hálózatokon található erőforrások beazonosítására használják, ez egy tömör karakterlánc, mely betűkből, számokból és szimbólumokból álló egyedi cím, melyek weboldalakra, képekre, dokumentumokra vagy más egyéb szerveren tárolt fájlokra mutatnak.[Forrás](https://www.britannica.com/technology/URL)

Különböző programozási nyelvek és technológiák használatosak a webalkalmazások felhasználói felületének fejlesztésére, a főbb böngészők az alábbiakat támogatják:

- **HTML (Hypertext Markup Language)**: A weboldalak kódolására használt jelölőnyelv, olyan formázási rendszer, mely az interneten található anyagok megjelenítésére szolgál. Biztosítja weboldalak a struktúráját és a tartalmát, meghatározza az egyes elemek megjelenését és azok hierarchiáját.[Forrás](https://www.britannica.com/technology/HTML)
- **CSS (Cascading Style Sheet)**: A webtartalom stilisztikai megjelenítéséhez használt deklaratív típusú nyelv. A felhasználó számára szabályozza a megjelenő elemeket, például az elrendezést, a betűtípust, méretet és színt, illetve más egyéb vizuális elemeket.[Forrás](https://www.britannica.com/technology/CSS-programming-language)
- **JavaScript**: Dinamikus és interaktív weboldalak készítésére használatos szkript nyelv. Lehetővé teszi az eseménykezelést, az animációkat és az aszinkron adatbetöltést is.[Forrás](https://www.britannica.com/technology/JavaScript)

A háttérrendszerek azok, amik tárolják az információkat, biztosítják az adatkezelést és az üzleti logikát. Nincsenek szigorúan szabványosított fejlesztői készletek, így ezek kevésbé korlátozottak, tehát az adott alkalmazás igényei szerint választhatóak meg.

### 1.2. Felhasznált mesterséges intelligencia bemutatása

#### **Nyelvi modell (Language Model)**

#### **Transformer Architektúra**

#### **Generatív modell**

#### **Pre-training és Fine-tuning**

#### 1.2.X. Felhasznált modellek

##### **DistilGPT2**

Egy angol nyelvű modell, melyet a GPT-2 (Generative Pre-trained Transformer 2) legkisebb 124 millió paraméteres verziójának felügyelt előképzésével hoztak létre. Ezt a 82 millió paraméterrel rendelkező modellt úgynevezett "tudáslecsapolással" (angolul: knowledge distillation) segítségével fejlesztették, és úgy tervezték, hogy a GPT-2 gyorsabb és könnyebb változata legyen szöveggenerálási feladatokhoz.[Forrás](https://huggingface.co/distilbert/distilgpt2)

> **Tudáslecsapolás (knowledge distillation)**: Egy olyan tömörítési technika, melynek során egy kisebb, kompakt modellt, arra tanítanak, hogy reprodukálja egy nagyobb modell viselkedését vagy modellek összességét. Célja, hogy egy kisebb modell hasonló teljesítményt tudjon elérni kevesebb számítási erőforrással, mint egy nagyobb modell.[Forrás](https://arxiv.org/pdf/1910.01108)

*Etikai kockázatok*
A DistilGPT2, mint a GPT-2 tudáslecsapolt verziója, így az etikai kockázatok terén is mutat hasonlóságot. Az OpenAI fejlesztői a GPT-2 modell leírásában közlik, hogy a nyelvi modellek a tükrözik a betanítási adataikban megtalálható előítéleteket, így bizonyos óvatossággal kell kezelni bizonyos használati eseteket.[Forrás](https://github.com/openai/gpt-2/blob/master/model_card.md) A DistilGPT2 is tartalmazza a GPT-2-ben lévő előítélet-problémákat, ezért előfordulhat, hogy a generált szövegek erősíthetnek bizonyos sztereotípiákat vagy akár sértő tartalmakat.

*Felhasználási esetek és korlátozások*
A GPT-2 modellt kutatók számára tervezték, hogy jobban meg tudják érteni a nagy léptékű generatív nyelvi modelleket, ezen kívül még a következő felhasználási esetekre alkalmas: nyelvtani segítség, szövegkiegészítés, kreatív írás és művészetek, valamint szórakoztatás. A nagy léptékű nyelvi modellek, mint a GPT-2 nem képesek megkülönböztetni a valóságot a fikciótól, így nem támogatottak azok a felhasználási esetek, melyek során a generált szövegnek mindenképp igaznak kell lennie.[Forrás](https://huggingface.co/distilbert/distilgpt2)

*Betanítási adatállomány*
A DistiGPT2 OpenWebTextCorpus használatával lett betanítva, ami egy nyílt forráskódú másolata, az OpenAI WebText adatállományának, amit a GPT-2 betanításához használtak.
> Az **OpenWebTextCorpus** adatállomány előállításához Reddit bejegyzéseket használtak fel a végeredmény jelenleg egy 38GB méretű angol nyelvű szöveges adathalmaz.[Forrás](https://skylion007.github.io/OpenWebTextCorpus/)

*Benchmark Teszt*
A WikiText-103-as benchmarkon a GPT-2 16.3 perplexitást, míg a DistilGPT2 21.1-es perplexitást ért el.
>A **WikiText-103** egy olyan nyelvi modellezési adatállomány, mely a Wikipédia által jóváhagyott cikkekből származik és gyakran használatos a nyelvi modellek teljesítményének értékelésére, a benchmark célja, hogy tesztelje a modelleket a szöveggenerálási, megértési és egyéb nyelvi feladatokban.[Forrás](https://paperswithcode.com/dataset/wikitext-103 )
>A **perplexitás** pedig egy statisztikai mérőszám, ami a gépi tanulás és a nyelvmodellezés területein használható teljesítmény értékelésre. Megmutatja, hogy mennyire jól tudja megjósolni egy nyelvi modell a következő szavakat a szövegekben. Minél alacsonyabb ez az érték, annál hatékonyabban képes a modell értelmes szöveget generálni.[Forrás](https://lexiq.hu/perplexity)

##### **GPT-Neo 125M**

##### **Facebook OPT 125M**

facebook/opt-125m

##### **GPT-2 Medium**

openai-community/gpt2-medium

##### **Facebook OPT 350M**

facebook/opt-350m
