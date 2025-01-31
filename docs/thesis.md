## **Bevezetés**


---

## **Elméleti háttér**

### Webalkalmazások általános bemutatása

https://aws.amazon.com/what-is/web-application/
https://www.geeksforgeeks.org/what-is-web-app/

### Felhasznált mesterséges intelligencia bemutatása

#### Mesterséges intelligencia (AI - Artificial Intelligence)

https://en.wikipedia.org/wiki/Artificial_intelligence
https://www.geeksforgeeks.org/what-is-artificial-intelligence/
https://www.nasa.gov/what-is-artificial-intelligence/

**Mesterséges intelligencia** az a tudományág, amely arra összpontosít, hogy a gépeket úgy tanítja meg, hogy képesek legyenek emberi intelligenciát utánzó feladatok végrehajtására. Mindezek a modellek a mesterséges intelligencia ágazatába tartoznak.

#### Gépi Tanulás (ML - Machine Learning)

https://en.wikipedia.org/wiki/Machine_learning
https://www.geeksforgeeks.org/machine-learning/
https://www.ibm.com/think/topics/machine-learning
https://mitsloan.mit.edu/ideas-made-to-matter/machine-learning-explained

**Gépi tanulás** azon belül, hogy a gépek adatokat használva képesek tanulni és javítani a teljesítményüket. Az összes itt felsorolt modell gépi tanulási módszert használ a nyelvi feladatok megoldásához.

#### Mély Tanulás (DL - Deep Learning)

https://en.wikipedia.org/wiki/Deep_learning
https://www.geeksforgeeks.org/introduction-deep-learning/
https://www.ibm.com/think/topics/deep-learning
https://www.deeplearningbook.org/

**Mély tanulás** a gépi tanulás egyik ága, amely az **artificial neural networks** (mesterséges neurális hálózatok) segítségével képes bonyolult minták megtanulására. A felsorolt modellek mind mély tanulási alapúak.

#### Természetes nyelvfeldolgozás (NLP - Natural Language Processing)

https://en.wikipedia.org/wiki/Natural_language_processing
https://www.geeksforgeeks.org/natural-language-processing-overview/
https://www.ibm.com/think/topics/natural-language-processing

**NLP** (Natural Language Processing) az a tudományág, amely a gépek számára lehetővé teszi, hogy megértsék, értelmezzék és reagáljanak az emberi nyelv szövegeire.

#### Nyelvi modell (LM - Language Model)

https://en.wikipedia.org/wiki/Language_model
https://developers.google.com/machine-learning/resources/intro-llms

**Nyelvi modellek (Language Models, LM)** olyan modellek, amelyek a nyelvek struktúráját és valószínűségi szabályszerűségeit tanulmányozzák, például milyen szavak követhetik egymást egy mondatban. Minden modell, amelyet említesz, nyelvi modell, amely szövegeket generál, értelmez vagy fordít.

#### Nagy nyelvi modell (LLM - Large Language Model)

https://en.wikipedia.org/wiki/Large_language_model
https://developers.google.com/machine-learning/resources/intro-llms
https://www.ibm.com/think/topics/large-language-models
https://www.baeldung.com/cs/nlp-language-models
https://arxiv.org/abs/2307.06435

A **Nagy Nyelvi Modellek (Large Language Models, LLM)** azok a modellek, amelyek rendkívül nagy számú paraméterrel és adathalmazzal dolgoznak. A **Bloom, BERT, GPT-Neo, GPT-J és LLAMA** mind nagy nyelvi modellek, mivel az ilyen típusú modellek hatalmas adatbázisokon tanulnak, és több milliárd paraméterrel rendelkeznek.

#### Transformer Alapú Modellek (Transformer (deep learning architecture))

https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)
https://www.ibm.com/think/topics/transformer-model
https://huggingface.co/docs/transformers/model_summary

A **Transformer** egy modellarchitektúra, amely önálló figyelmi mechanizmusokat (self-attention) alkalmaz a szekvenciák feldolgozására. Az alábbi modellek mind **Transformer alapúak**:

- **BERT** (Google)
- **GPT-Neo** (EleutherAI)
- **GPT-J** (EleutherAI)
- **LLAMA** (Meta AI)
- **Bloom** (BigScience)

#### Autoregresszív Modellek (AR - Autoregressive Model)

https://en.wikipedia.org/wiki/Autoregressive_model
https://www.geeksforgeeks.org/autoregressive-ar-model-for-time-series-forecasting/
https://www.ibm.com/think/topics/autoregressive-model
https://www.baeldung.com/cs/autoregression

**Autoregresszív modellek** olyan modellek, amelyek a jövőbeli kimeneteket az előző kimenetek alapján generálják. A **GPT-Neo** és **GPT-J** autoregresszív modellek, mivel a generálás során figyelembe veszik a korábbi szavakat.

#### Maskolt Nyelvi Modellek (Masked Language Models)

https://web.stanford.edu/~jurafsky/slp3/11.pdf
https://www.ibm.com/think/topics/masked-language-model
https://huggingface.co/docs/transformers/main/tasks/masked_language_modeling

A **BERT** (Google) és a **LLAMA** (Meta AI) maskolt nyelvi modellek, mivel a szövegben bizonyos szavakat elrejtve tanulják meg azokat előre jelezni a kontextus alapján.

#### Nyílt Forráskódú Modellek (Open Source AI)

https://www.iguazio.com/glossary/open-source-model/
https://opensource.org/ai/open-source-ai-definition

A felsorolt modellek közül mindegyik **nyílt forráskódú**.

#### Hugging Face Hub

https://huggingface.co/docs/hub/index

A **Hugging Face Hub** egy nyílt forráskódú platform, amely a mesterséges intelligencia és a természetes nyelvi feldolgozás (NLP) közössége számára biztosít egy központi helyet a modellek, adatállományok és egyéb AI eszközök megosztására, tárolására és újrafelhasználására.

A platform célja, hogy könnyen hozzáférhetővé tegye a legkülönbözőbb AI modelleket, különösen a **transformer alapú modelleket**, mint például a BERT, GPT, T5 és más nagy nyelvi modellek, valamint különböző előre betanított modelleket különböző feladatokhoz, például szövegfeldolgozáshoz, gépi fordításhoz, képosztályozáshoz stb.

A **Hugging Face Hub** a következő funkciókat kínálja:

- **Modellek megosztása**: A fejlesztők és kutatók egyszerűen tölthetik fel, megoszthatják és újra felhasználhatják a modelleket. A modellek kereshetők és kategorizálhatók.
- **Előre betanított modellek**: A platform rengeteg előre betanított modellt tartalmaz, amelyek különböző feladatokhoz használhatók, például szövegértés, szövegképzés, érzelmi elemzés stb.
- **Integrált API**: A Hugging Face API lehetővé teszi, hogy a modelleket közvetlenül alkalmazásokban és szolgáltatásokban használják.
- **Közösségi támogatás**: A felhasználók közössége aktívan hozzájárul a modellek fejlesztéséhez, értékeléséhez és dokumentálásához.

A platform célja, hogy a mesterséges intelligencia fejlesztése nyílt, hozzáférhető és együttműködő legyen, segítve a kutatók, fejlesztők és vállalatok munkáját.

#### Hugging Face Transformers

https://huggingface.co/docs/transformers/index

A **🤗 Transformers** egy nyílt forráskódú könyvtár, amely a mesterséges intelligencia legmodernebb modelljeit biztosít a **PyTorch**, **TensorFlow**, és **JAX** keretrendszerekhez. A könyvtár célja, hogy egyszerűsítse az AI modellek letöltését, betanítását és alkalmazását, lehetővé téve a legújabb előre betanított modellek használatát, amelyek jelentősen csökkenthetik a számítási költségeket, a szénlábnyomot, és megspórolhatják azokat az idő- és erőforrásokat, amelyek a modellek nulláról történő betanításával járnak.

A **Transformers** könyvtár különböző feladatokat támogat különböző modalitásokban:

- **Természetes nyelvfeldolgozás (NLP)**: szöveg osztályozás, névazonosítás, kérdés-válasz, nyelvi modellezés, kód generálás, szövegösszegzés, fordítás, többválasztós kérdések, és szöveggenerálás.
- **Számítógépes látás**: képosztályozás, objektumfelismerés és szegmentálás.
- **Hang**: automatikus beszédfelismerés és hangosztályozás.
- **Multimodális**: táblázatos kérdés-válasz, optikai karakterfelismerés, információk kinyerése beolvasott dokumentumokból, videó osztályozás, és vizuális kérdés-válasz.

A **🤗 Transformers** lehetővé teszi a keretrendszerek közötti interoperabilitást, így ugyanazt a modellt különböző fázisokban különböző keretrendszerekkel használhatjuk (pl. egyet taníthatunk PyTorch-ban, majd betölthetjük TensorFlow-ban az inferálásra). Támogatja a modellek exportálását olyan formátumokba is, mint az **ONNX** és **TorchScript**, hogy a modellek könnyen bevethetők legyenek a gyártási környezetekben.

A könyvtárhoz aktív közösség is kapcsolódik a **Hugging Face Hub**-on, a fórumon vagy a Discord szerveren, ahol a fejlesztők és kutatók közvetlenül hozzájárulhatnak, kérdéseket tehetnek fel és megoszthatják tapasztalataikat.

#### Modellek

##### Bloom (BigSience)

https://arxiv.org/abs/2211.05100
https://en.wikipedia.org/wiki/BLOOM_(language_model)
https://bigscience.huggingface.co/blog/bloom
https://huggingface.co/bigscience/bloom

##### Bert (Google)

https://en.wikipedia.org/wiki/BERT_(language_model)
https://research.google/pubs/bert-pre-training-of-deep-bidirectional-transformers-for-language-understanding/
https://github.com/google-research/bert
https://huggingface.co/docs/transformers/model_doc/bert
https://arxiv.org/pdf/1810.04805

##### GPT-Neo (EleutherAI)

https://www.eleuther.ai/artifacts/gpt-neo
https://github.com/EleutherAI/gpt-neo
https://huggingface.co/docs/transformers/model_doc/gpt_neo
https://researcher2.eleuther.ai/projects/gpt-neo/

##### GPT-J (EleutherAI)

https://en.wikipedia.org/wiki/GPT-J
https://www.eleuther.ai/artifacts/gpt-j
https://huggingface.co/docs/transformers/model_doc/gptj

##### LLAMA (Large Language Model Meta AI)

https://www.llama.com/
https://www.llama.com/llama2/
https://www.geeksforgeeks.org/what-is-llama2-metas-ai-explained/
https://en.wikipedia.org/wiki/Llama_(language_model)

### Mesterséges intelligencia a webalkalmazásokban

https://www.geeksforgeeks.org/ai-in-web-development/
https://medium.com/theymakedesign/ai-in-web-development-9a1b5f04eee
https://www.jscholaronline.org/articles/JAIST/The-Intersection-of-Artificial-Intelligence-and-Contemporary-Web-Development.pdf
https://onlinelibrary.wiley.com/doi/full/10.1111/exsy.13505
https://www.researchgate.net/publication/383866997_The_Impact_of_AI_on_Web_Development
https://link.springer.com/chapter/10.1007/978-3-540-79140-9_2

**Mesterséges intelligencia a webalkalmazásokban** azt jelenti, hogy az AI-technológiák beépülnek a webes platformok működésébe, hogy okosabb, hatékonyabb és személyre szabottabb felhasználói élményt biztosítsanak. Az AI különböző képességei – például minták felismerése, természetes nyelv feldolgozása (NLP), prediktív elemzés vagy gépi tanulás – a webalkalmazások működésének központi elemei lehetnek. Az alábbiakban kifejtem, hogyan valósulhat ez meg, és milyen előnyökkel jár.

#### **Felhasználási területek**

1. **Felhasználói élmény személyre szabása**:
    
    - AI algoritmusok elemzik a felhasználók viselkedését (például keresési előzmények, kattintási minták), és ezek alapján személyre szabott ajánlásokat nyújtanak. Például: Netflix ajánló rendszere.
2. **Automatizált ügyfélszolgálat**:
    
    - Chatbotok és virtuális asszisztensek (pl. GPT-alapú rendszerek) valós időben válaszolnak a felhasználói kérdésekre.
    - Ezek az eszközök a természetes nyelvi feldolgozást (NLP) használják, hogy pontosan megértsék a kérdéseket és releváns válaszokat adjanak.
3. **Keresés és adatelemzés**:
    
    - Az AI intelligens keresőmotorokat hoz létre, amelyek a felhasználói szándékokat felismerve pontosabb találatokat adnak vissza.
    - Nagy mennyiségű adat gyors feldolgozására és trendek azonosítására is használható.
4. **Biztonság és csalásvédelem**:
    
    - AI modellek felismerhetik a gyanús tevékenységeket (pl. szokatlan bejelentkezési mintákat), és azonnal értesítést küldenek a felhasználóknak.
    - CAPTCHA rendszerek, arcfelismerés, és egyéb hitelesítési módszerek is használhatják az AI-t.
5. **Automatikus tartalomelemzés és generálás**:
    
    - AI segítségével képek, szövegek és egyéb tartalmak elemzése és létrehozása válik lehetővé. Például: szövegösszegzés, gépi fordítás, vagy blogtartalmak generálása.

#### **Hogyan működik?**

A mesterséges intelligencia alkalmazása a webalkalmazásokban három fő rétegre épül:

1. **Adatok gyűjtése és feldolgozása**:
    - A webalkalmazás begyűjti a felhasználói adatokat, például kattintások, keresési előzmények vagy egyéb interakciók alapján.
2. **AI modellek és algoritmusok**:
    - Ezek az algoritmusok az adatokat elemzik, felismerik a mintákat, és előrejelzéseket készítenek.
3. **Eredmények beépítése**:
    - Az AI által létrehozott eredményeket (pl. ajánlások, válaszok) a webalkalmazás frontendjén keresztül mutatják meg a felhasználóknak.

#### **Technológiák és eszközök**

- **Backend AI**: Django, Flask vagy Node.js alapú rendszerek, amelyek AI modelleket integrálnak a szerveroldalon.
- **Frontend integráció**: JavaScript keretrendszerek, mint például React vagy Angular, amelyek az AI-alapú eredményeket dinamikusan jelenítik meg.
- **AI eszközök**: Hugging Face, TensorFlow.js, és PyTorch a modellek kezelésére és futtatására.
- **Felhőszolgáltatások**: Google AI, AWS AI vagy Azure Cognitive Services biztosítják az AI képességeket felhőalapú infrastruktúrán.

#### **Előnyök**

- Hatékonyabb működés az automatizáció által.
- Jobb felhasználói elégedettség a személyre szabott szolgáltatásokkal.
- Idő- és költségmegtakarítás az automatizált ügyfélszolgálat és folyamatok révén.

#### **Példák**

1. **E-kereskedelem**: Termékajánlók, dinamikus árképzés, keresési funkciók fejlesztése.
2. **Oktatás**: Adaptív tanulási rendszerek, amelyek a diák válaszai alapján személyre szabják a tanulási tartalmat.
3. **Egészségügy**: AI-asszisztensek, amelyek segítenek az orvosoknak diagnosztikai javaslatokkal vagy időpontfoglalások kezelésével.

A mesterséges intelligencia a webalkalmazásokban az innováció és a hatékonyság hajtóereje, amely forradalmasítja a felhasználói élményt és a vállalati működést.

### Informatikai projektmenedzsment (IT Project Management)

https://iehouse.org/wp-content/uploads/2021/07/PMBOK7.pdf
https://itmap.hu/szakterulet/it-projektmenedzsment
https://books.google.hu/books?id=4Q2yDwAAQBAJ&hl=hu
https://www.geeksforgeeks.org/phases-project-management-processes/
https://www.geeksforgeeks.org/software-development-process/
https://www.geeksforgeeks.org/requirements-gathering-introduction-processes-benefits-and-tools/
https://www.geeksforgeeks.org/software-development-life-cycle-sdlc/
https://www.nive.hu/Downloads/Szakkepzesi_dokumentumok/Bemeneti_kompetenciak_meresi_ertekelesi_eszkozrendszerenek_kialakitasa/7_1143_tartalomelem_001_munkaanyag_091231.pdf
https://pmi.hu/static/uploaded/Files/Downloads/PM-Tud%C3%A1st%C3%A1r-V1.pdf

Az informatikai projektmenedzsment az IT bármely területén futó projektek irányítását, koordinálását jelenti. Mindez magában foglalja a projektfolyamatok és erőforrások tervezését, irányítását és ellenőrzését, annak érdekében, hogy a projekt megfeleljen az előzetesen meghatározott eredményeknek, az idő és költség korlátoknak. 
Alapvetően kétféle projektmenedzsment megközelítés létezik: az egyik a klasszikus, vízesés alapú, a másik pedig az elsősorban szoftverfejlesztési területen alkalmazott agilis elvű megközelítés. Ezekhez kapcsolódóan számos módszertan érhető el (pl. Scrum, Kanban, Lean, XP, PRINCE2, stb.), melyek segítenek a projektmenedzsment kereteit és eszközeit biztosítani.

Az **informatikai projektmenedzsment** (IT project management) az IT projektek tervezését, irányítását és ellenőrzését jelenti, hogy biztosítsa a projektek sikeres végrehajtását az előre meghatározott célok, idő- és költségkeretek között. A projektmenedzsment célja az erőforrások (emberi, technikai, pénzügyi) optimális felhasználása és a projektfolyamatok zökkenőmentes működésének biztosítása.

**Főbb elemek:**

1. **Tervezés**: A célok meghatározása, az ütemterv kidolgozása, erőforrások és költségvetés felosztása.
2. **Irányítás**: Az egyes feladatok elvégzésének felügyelete, a csapat koordinálása, kommunikáció fenntartása.
3. **Ellenőrzés**: Az előrehaladás nyomon követése, kockázatok kezelése, és szükség esetén korrekciók végrehajtása.

#### Klasszikus projektmenedzsment (Waterfall)

https://www.geeksforgeeks.org/waterfall-model/

A **klasszikus projektmenedzsment** (más néven vízesés-modell) lineáris és szigorúbb folyamatokat követ, ahol a projekt minden fázisa (tervezés, kivitelezés, tesztelés, zárás) szekvenciálisan követi egymást. A projekt elején kialakított részletes specifikációk és terveken alapul, és nagyobb hangsúlyt fektet a határidők, költségek és erőforrások szigorú betartására. Az esetleges változtatások gyakran nehezen illeszthetők a már lezárt fázisokhoz.

- Lineáris és szekvenciális folyamatok.
- Minden szakasz (pl. követelmények gyűjtése, tervezés, fejlesztés, tesztelés) csak az előző befejezésével kezdődik.
- Jó választás olyan projektekhez, amelyekben a követelmények előre pontosan definiálhatóak.

#### Agilis projektmenedzsment

https://www.geeksforgeeks.org/software-engineering-agile-software-development/?ref=lbp

Az **agilis projektmenedzsment** rugalmas, iteratív megközelítést alkalmaz, amely a folyamatos visszajelzésekre és az ügyféligények gyors változtatására épít. Az agilis módszerek, mint például a Scrum vagy Kanban, kisebb, jól meghatározott munkacsoportokra és rövid időintervallumokra (sprintek) bontják a projektet, lehetővé téve a folyamatos fejlődést és a gyors alkalmazkodást.

- Iteratív és rugalmas megközelítés, elsősorban szoftverfejlesztésben használják.
- A projektek kisebb szakaszokra (sprint) vannak bontva, amelyek folyamatos fejlesztést és tesztelést biztosítanak.
- Néhány agilis módszertan:
    - **Scrum**: Rövid iterációk (sprint) és rendszeres csapatmegbeszélések (stand-ups).
    - **Kanban**: Vizualizációs táblák segítségével nyomon követhető munkafolyamatok.
    - **Lean**: A felesleges folyamatok csökkentése és a hatékonyság maximalizálása.
    - **XP (Extreme Programming)**: Kódolási gyakorlatokra összpontosít.
    - **PRINCE2**: Nagyobb, strukturált projektek esetén hasznos keretrendszer.

#### Kombinált módszertan: **Agilis keretrendszer klasszikus elemekkel**

https://www.geeksforgeeks.org/agile-vs-waterfall/?ref=shm

- **Projektindítás: Klasszikus tervezés**
    - Készíts egy részletes követelményspecifikációt és projekttervet, amely tartalmazza az alapvető célokat, a hatókört és a főbb mérföldköveket.
    - Definiáld a dokumentációs folyamatot: milyen típusú dokumentumok készülnek (pl. technikai specifikációk, API-dokumentáció, felhasználói útmutató)
- **Fejlesztési folyamat: Agilis ciklusok**
    - Oszd fel a fejlesztést kisebb iterációkra vagy sprintekre.
    - Minden sprint végén készíts részletes dokumentációt az elkészült funkciókról (pl. modulterv, interfészek specifikációi).
    - Tarts rendszeres visszajelzési köröket a csapatod és az érintettek bevonásával.
- **Folyamatos dokumentáció és karbantartás**
    - Az iterációk során gyűjtsd a változásokat, és frissítsd a specifikációkat a fejlesztési folyamat előrehaladtával.
- **Projektszállítás: Klasszikus lezárás**
    - A projekt végén készíts egy teljes, részletes dokumentációs csomagot, amely tartalmazza:
        - A végleges követelményspecifikációt.
        - A rendszertervet és az architektúrát.
        - A kód dokumentációját (pl. kódkönyvtárak és API-k leírása).

### Specifikációk

https://somnusoft.com/szoftverfejlesztes

#### adatok összegyűjtése: https://www.geeksforgeeks.org/requirements-gathering-introduction-processes-benefits-and-tools/

1. koncepcióterv: 
	1. szabadszavas leírás (Elsősorban szükséges az ötlet körülhatárolása, pár egyszerű mondatban történő leírása, ami kiindulási pontot adhat a szoftver tervezésével kapcsolatban.)
	2. ötlet kidolgozása
	3. infrastruktúra és futtatási környezet meghatározása
2. (árajánlat)
3. **szoftver követelmény specifikáció**: fejlesztéshez szükséges további pontosításokat és funkcionális specifikációt tartalmazza
4. Fejlesztés: A **szoftver követelmény specifikáció dokumentumban leírtaknak megfelelően** létrehozásra kerül a projekt a **verziókövető rendszerben** és hozzáadásra kerülnek a fő- és részfeladatok is prioritások és függőségek szerint.

#### SRS

https://www.geeksforgeeks.org/software-requirement-specification-srs-format/
https://www.perforce.com/blog/alm/how-write-software-requirements-specification-srs-document
https://github.com/jam01/SRS-Template
https://asana.com/resources/software-requirement-document-template
https://cse.msu.edu/~cse870/IEEEXplore-SRS-template.pdf
https://relevant.software/blog/software-requirements-specification-srs-document/
https://snappify.com/blog/software-requirements-specification-sample
https://www.perforce.com/blog/alm/how-write-software-requirements-specification-srs-document

### Létező hasonló projektek

https://arxiv.org/pdf/2401.08807
https://github.com/xinyi-hou/LLM4SE_SLR

Projektmenedzsment programok: https://flexi-project.com/hu/20-legjobb-projektmenedzsment-szoftver/

---

## **A megvalósítandó feladat ismertetése**

### A feladat pontos leírása és célkitűzések meghatározása

A projekt célja egy **webalapú alkalmazás** fejlesztése, amely mesterséges intelligencia alkalmazásával támogatja a projektmenedzsmentet és a dokumentációk automatizált generálását. Az alkalmazás célja, hogy a felhasználók számára egyszerűbbé, gyorsabbá és hatékonyabbá tegye a projektek dokumentációs és tervezési folyamatait, miközben javítja azok minőségét.

#### Célkitűzések

A projekt célja, hogy egy olyan **intuitív és reszponzív felhasználói felületet** biztosítson, amely megfelel a modern webes alkalmazások elvárásainak. Az alkalmazás:
- **Könnyen integrálható** a projektmenedzsment munkafolyamatokba.
- **Felhasználóbarát**, így a projektmenedzserek, csapatok és fejlesztők gyorsan elsajátíthatják használatát.
- **Időt és költséget takarít meg**, miközben növeli a dokumentációs folyamat hatékonyságát és pontosságát.

Ezáltal az alkalmazás nemcsak a dokumentációk elkészítését forradalmasítja, hanem jelentősen hozzájárul a projektek sikeres megvalósításához is.

### Funkcionális követelmények 

https://www.geeksforgeeks.org/functional-vs-non-functional-requirements/
https://en.wikipedia.org/wiki/Functional_requirement
https://www.geeksforgeeks.org/what-are-functional-requirements-in-system-design-examples-definition/

Annak a konkrét meghatározása, hogy mit kell tudnia az alkalmazásnak.

- Felhasználók regisztrációja és bejelentkezése.
- Projekt létrehozása, szerkesztése és törlése.
- Dokumentumok generálása projektenként.
- **Adatok exportálása különböző formátumokban (pl. PDF, Word)**
	- **Formátumok kiválasztása és előállítása:** Részletesebb technikai magyarázat, hogyan történik a különböző formátumok generálása és miért van szükség ezekre a funkciókra.
- Keresés a projektek és dokumentumok között.
- Adminisztrátori funkciók (pl. felhasználók kezelése).
- **Projektek létrehozása és kezelése**
	- A felhasználók új projekteket hozhatnak létre, módosíthatják azokat, valamint nyomon követhetik a projektek előrehaladását.
	- A projektekhez kapcsolódó adatokat könnyen rendszerezhetik, és azok bármikor elérhetők lesznek.
- **Adatgyűjtés a specifikációk elkészítéséhez**
	- **Felhasználói input kezelése:** A rendszer interaktív kérdésekkel segíti a felhasználókat az alapvető projekttel kapcsolatos adatok megadásában.
	- **Beszélgetés nyelvi modellel:** A mesterséges intelligencia beszélgetés-alapú interfészen keresztül támogatja az ötletelést és az adatok pontosítását.
- **Automatizált dokumentáció-generálás**
	- **Specifikációk:** A projekt céljainak, követelményeinek és funkcióinak részletes leírása.
	- ***Időtervek:** A projekthez tartozó feladatok ütemezése és határidők meghatározása.*
	- ***Technikai tervek:** Részletek a fejlesztés technikai aspektusairól, például architektúrák és adatbázis-tervek.*
	- ***Fejlesztési dokumentumok:** A projekt kódjának és működésének leírása, beleértve a fejlesztői útmutatókat.*
- **Dokumentáció-generálás főbb jellemzői**:
	- **Automatizált dokumentációs eszközök előnyei:** A folyamat gyorsabbá és hibamentesebbé válik, miközben csökkenti az emberi erőforrás szükségességét.
	- **Specifikációk és dokumentációk szerepe:** A rendszer biztosítja, hogy minden szükséges dokumentum strukturáltan, megfelelő részletezettséggel készüljön el.
	- **Dinamikus generálás:** Az alkalmazás a felhasználó igényeinek megfelelően, valós időben hoz létre testreszabott dokumentumokat.
	- **Minőségjavítás mesterséges intelligenciával:** Az MI képes javítani a dokumentáció nyelvezetén, helyesírási hibáin, valamint konzisztens és professzionális formátumot biztosítani.
- **Dokumentumformátumok testreszabása**
	- Az alkalmazás lehetőséget nyújt az előállított dokumentumok különböző formátumokba történő exportálására (például Markdown, *PDF, vagy Word*).
	- Ezzel megkönnyíti a dokumentumok integrálását más rendszerekbe vagy platformokba.
- **Dokumentációk minőségének növelése**
	- **Automatikus hibajavítás:** A rendszer képes észlelni és kijavítani az esetleges logikai vagy helyesírási hibákat.
	- **Tartalmi kiegészítések:** Az MI javaslatokat tehet további elemek hozzáadására, például részletesebb leírásokra, példákra vagy háttérinformációkra.
- **Tanácsadás a dokumentációk kialakításában**: A rendszer segíti a felhasználókat a legjobb gyakorlatok alkalmazásában, például a dokumentáció struktúrájának és tartalmának kialakításában.

### Felhasználói esetek és folyamatok

https://www.geeksforgeeks.org/use-case-diagram/
https://www.uml-diagrams.org/use-case-diagrams.html
https://en.wikipedia.org/wiki/Use_case_diagram
https://www.ibm.com/docs/en/dmrt/9.5?topic=diagrams-use-case
https://rtt.koczka.com/uml.html

- **Use case diagram:**
    - Milyen típusú felhasználók vannak (normál felhasználó, adminisztrátor).
    - Milyen műveleteket végezhetnek (pl. projekt létrehozása, törlése, dokumentumok generálása).
- **Felhasználói folyamatok részletezése:**
    - Pl. Hogyan működik a regisztrációs folyamat?
    - Mi történik egy projekt létrehozásakor?

### Nem-funkcionális követelmények

https://www.geeksforgeeks.org/functional-vs-non-functional-requirements/
https://www.geeksforgeeks.org/what-are-non-functional-requirements-in-system-design-examples-definition/?ref=ml_lbp
https://en.wikipedia.org/wiki/Non-functional_requirement

A rendszer teljesítményével, biztonságával és skálázhatóságával kapcsolatos követelmények

- Rendszer biztonsága és titkosítási eljárások
	- titkosítási algoritmusok bemutatása (pl. bcrypt, AES).

- Kliens- és szerveroldali hibakezelés megvalósítása.

### A tervezett megoldás részletezése

1. **Felhasználói modul**:
	- **Autentikáció**: A felhasználók bejelentkezésének és azonosításának folyamata, beleértve a jelszóhashelést és a biztonságos hitelesítési mechanizmusokat.
	- **Profilkezelés**: A felhasználók adatainak kezelése, például név, e-mail, profilkép, beállítások. Az adatvédelmi szabályok betartása (GDPR).
	- **Jogosultságok és szerepkörök**: A különböző felhasználói szerepkörök és azok jogosultságainak kezelése (admin, normál felhasználó, vendég, stb.).
	- ***Jelszó visszaállítás**: Rendelkezésre áll egy egyszerű és biztonságos jelszó-visszaállító mechanizmus e-mail vagy SMS alapú azonosítással.*
2. **Projektmenedzsment modul**: 
	- **Projektadatok rögzítése**: A projektek létrehozása, módosítása, státuszok, határidők és egyéb projektinformációk tárolása.
	- **Feladatok és projekt státuszok**: A feladatok különböző státuszokban lehetnek, mint pl. "Függőben", "Folyamatban", "Befejezett", és ezeket könnyen nyomon lehet követni a rendszerben.
	- ***Felhasználói jogosultságok**: Az adminisztrátorok és egyéb szerepkörök (pl. projektvezetők, felhasználók) számára megfelelő jogosultságokat biztosítunk a rendszer különböző funkcióinak elérésére (hozzáférés-profil módosítás, projekt létrehozás, stb.).*
	- ***Kollaborációs funkciók**: A projektcsapatok közötti hatékony együttműködést elősegítő funkciók, mint például a dokumentummegosztás, kommentelés, értesítések és csevegési lehetőségek.*
	- ***Integrált kommunikációs rendszer**: A projektekhez tartozó értekezletek, chat funkciók és értesítési rendszerek, amelyek javítják a csapatok közötti kommunikációt.*
3. **AI dokumentációs modul**: 
	- **Szöveges tartalom automatikus generálása**: Az AI képes a rendszer által gyűjtött információk és adatok alapján automatikusan javaslatokat tenni vagy akár teljes dokumentumokat generálni, mint például jelentések, specifikációk vagy tervezési dokumentációk.
	- **Téma alapú generálás és testreszabás**: A felhasználók számára testreszabható AI-alapú szövegkiegészítés és generálás lehetősége, figyelembe véve a dokumentációs igényeket és a vállalati szabványokat.
	- **Generatív mesterséges intelligencia modellek**: A különböző AI modellek (pl. GPT, BERT) alkalmazása dokumentáció generálására, javítására, valamint a felhasználói igények alapján történő módosításokra.
	- **Automatizált szövegkiegészítés**: A dokumentációs tartalom automatikus kiegészítése, javaslatok generálása, szövegek átfogalmazása.
	- **Visszajelzés alapú dokumentációjavítás**: A felhasználói visszajelzések alapján a rendszer képes a generált dokumentumok javítására, pontosítására.
	- ***Fordítási és lokalizálási támogatás**: Az AI támogatja a dokumentáció többnyelvű verzióinak létrehozását, hogy a rendszer különböző nyelveken is elérhető legyen.*
4. **Adminisztrációs modul**: 
	- **Statisztikák**: Részletes analitikai adatok és riportok a rendszer használatáról, felhasználói aktivitásról, projekt előrehaladásról, stb.
		- **Felhasználói aktivitás nyomon követése**: Az adminisztrátorok részletes statisztikákat és jelentéseket kaphatnak a felhasználói aktivitásról, beleértve a bejelentkezéseket, adatfrissítéseket és egyéb tevékenységeket.
	- **Naplózás**: Az alkalmazás eseményeinek naplózása (pl. felhasználói tevékenységek, hibák, rendszerhiba-jelentések) a későbbi elemzéshez és hibaelhárításhoz.
	- **Hibakezelés**: Az alkalmazás hibáinak nyomon követése, automatikus riasztások és hibafigyelés implementálása a problémák gyors és hatékony kezelésére.
	- **Rendszerbiztonság**: Biztonsági események és próbálkozások naplózása, hogy az adminisztrátorok azonnal észleljék az esetleges támadásokat vagy biztonsági réseket.
5. ***Értesítési és értesítési menedzsment modul**:*
	- ***E-mail értesítések**: Automatikusan generált e-mail értesítések a felhasználók számára fontos eseményekről (pl. jelszóváltoztatás, új üzenet, projekt határidők).*
6. ***Analitika és jelentéskészítő modul**:*
	- ***Projekt- és teljesítményanalízis**: A rendszer automatikusan gyűjti a projektadatokat és készít vizuális jelentéseket a haladásról, erőforrás-használatról, költségekről stb.*
	- ***Teljesítménymutatók (KPI)**: Az adminisztrátorok és projektvezetők számára hasznos statisztikai mutatók, mint például a projekt hatékonyság, költségvetés követés, feladatok elvégzése stb.*
	- ***Adatvizualizációs eszközök**: Grafikonok, táblázatok, diagramok formájában nyújtott vizuális elemzések, amelyek segítenek az adat alapú döntéshozatalban.*
7. **Dokumentációs és tudásbázis modul**:
	- **Használati útmutatók és segédletek**: A rendszerben elérhetőek a felhasználók számára készült dokumentációk, FAQ-k, és útmutatók, amelyek segítenek a rendszer használatában.
	- **Kereső funkció**: A dokumentációban és tudásbázisban való könnyű keresés biztosítása, hogy gyorsan megtalálják a felhasználók a számukra fontos információkat.

---

## **Tervezés és fejlesztés**

### Rendszerterv

- **Architektúra kiválasztása:** Django egy monolitikus webalkalmazás-keretrendszer, amely ideális a kisebb és közepes méretű alkalmazások számára, mivel gyorsan fejleszthető, és erőteljes eszközkészletet kínál a backend és frontend integrálására.
- **Diagram**: kapcsolat a backend-frontend-adatbázis között

#### **Fejlesztési környezet**

- **VS Code**: A Visual Studio Code (VS Code) a legfontosabb fejlesztési környezet, amit a projektben használtam. Ez egy könnyen használható, ingyenes, nyílt forráskódú kódszerkesztő, amely támogatja a Python, JavaScript, HTML/CSS, és más programozási nyelvek fejlesztését.
    - [VS Code hivatalos oldal](https://code.visualstudio.com/)
    - [Wikipedia: Visual Studio Code](https://en.wikipedia.org/wiki/Visual_Studio_Code)
    - [VS Code GitHub oldal](https://github.com/microsoft/vscode)
- **Integrációk és bővítmények**: Az VS Code több hasznos bővítményt kínál a fejlesztéshez, mint például a Python és Django bővítmények, amelyek segítik a kód szintaxisának kiemelését, hibák keresését és a gyors fejlesztést.

#### **Verziókezelés és együttműködés**

- **Git**: A Git verziókezelő rendszer alapvető fontosságú a kód védelme érdekében. A Git lehetővé teszi a kód különböző állapotainak biztonságos mentését, és visszaállítást biztosít a korábbi verziókhoz, ha szükséges. Ezen kívül egyszerűsíti a kód módosításainak nyomon követését, így könnyen visszakövetheted, hogy mely változtatások történtek és miért.
    - [Git hivatalos oldal](https://git-scm.com/)
    - [Git guides](https://github.com/git-guides)
    - [Wikipedia: Git](https://en.wikipedia.org/wiki/Git)
- **GitHub**: A GitHub online tárolót biztosít, amely lehetővé teszi a kód biztonságos tárolását és bárhonnan való elérését. Az alábbi eszközöket kínálja a GitHub:
    - **Commit History**: A kód minden módosításának részletes nyomon követése.
    - **Issues**: Feladatok, fejlesztési szempontok és projekt állapotának nyilvántartása.
    - **Branching**: A GitHub branching funkciójával új funkciók fejlesztése külön ágakon történhet, amelyek később egyesíthetők a fő ággal, így nem zavarják meg a már meglévő működő kódot.
    - [Wikipedia: GitHub](https://en.wikipedia.org/wiki/GitHub)
- **GitHub Desktop**: A GitHub Desktop grafikus felületet biztosít a Git verziókezelés kezelésére, amelyet könnyebb használni, mint a parancssori eszközt, különösen, ha vizuális felületet preferálsz.
    - [GitHub Desktop letöltés](https://github.com/apps/desktop)
- **GitHub Projects**: A GitHub Projects lehetővé teszi, hogy Kanban stílusú táblázatokat hozz létre, ahol kategorizálhatod a feladatokat (issue-kat, pull requesteket) különböző státuszokba, mint **To Do**, **In Progress**, **Done**.
    - [GitHub Projects dokumentáció](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)
    - [GitHub blog: Project planning](https://github.blog/developer-skills/github/getting-started-with-project-planning-on-github/)
- **.gitignore**: A `.gitignore` fájl segít abban, hogy kizárjuk azokat a fájlokat és mappákat, amelyeket nem szeretnénk verziókezelésbe venni. Ezek a fájlok lehetnek például ideiglenes fájlok, lokális konfigurációk vagy titkos kulcsok, amelyek nem szükségesek a kód verziókezelésében, és elkerülik az érzékeny információk véletlenszerű megosztását. A `.gitignore` fájlt a projekt gyökérkönyvtárában kell elhelyezni
	- https://git-scm.com/docs/gitignore
	- https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/
	- https://kaykobadreza.com/blog/ultimate-gitignore-file-for-your-django-project/

#### **Külső szolgáltatások**

- **Email küldés**:
    - Django beépített email küldési lehetőségei, SMTP szolgáltatók (pl. SendGrid, Mailgun) használata.
        - [Django Email Documentation](https://docs.djangoproject.com/en/5.1/topics/email/)
        - [Email Setup in Django (GeeksforGeeks)](https://www.geeksforgeeks.org/setup-sending-email-in-django-project/)
- **Dokumentum formázás**:
    - Markdown konvertálás.
        - [Django Markdown Tutorial](https://learndjango.com/tutorials/django-markdown-tutorial)
    - _PDF generálás Django-val (WeasyPrint, ReportLab)_:
        - [Django PDF Output](https://docs.djangoproject.com/en/5.1/howto/outputting-pdf/)
- **Hugging Face Hub** (`huggingface-hub==0.26.2`):
    - A Hugging Face modelljeinek és adatkészleteinek elérésére szolgáló eszköz.
- **Requests** (`requests==2.32.3`):
    - HTTP-kérések küldése külső API-khoz.
- **Fsspec** (`fsspec==2024.10.0`):
    - Fájlrendszerek kezelése, beleértve a felhőalapú tárolókat is.
- **Whitenoise** (`whitenoise==6.7.0`):
    - Statikus fájlok kiszolgálására optimalizált, CDN-ekkel is használható.
- **Transformers** (`transformers==4.46.1`):
    - Gyakran kapcsolódik a Hugging Face API-jához a modellbetöltéshez.
- **Accelerate** (`accelerate==1.1.0`):
    - Több GPU és felhőalapú erőforrások kezelésére használható.
- **Safetensors** (`safetensors==0.4.5`):
    - Gépi tanulási modellek biztonságos tárolására és távoli modellek betöltésére.
- **urllib3**:
    - HTTP-klienskönyvtár külső API-hívásokhoz.
- **certifi**:
    - Hitelesítési tanúsítványok biztosítása HTTP(S) kapcsolatokhoz, külső API-k eléréséhez.

### Adatbázis tervezés

#### **Adatbázis fogalma és szerepe webalkalmazásokban**

https://www.ramotion.com/blog/database-in-web-app-development/
https://www.geeksforgeeks.org/how-to-design-a-database-for-web-applications/
https://medium.com/@vansh.khandelwal06/the-role-of-databases-in-development-an-essential-guide-3b51af9ee99b
https://rtt.koczka.com/db.html

Az adatbázis olyan rendszerek összessége, amelyek a webalkalmazások adatainak tárolásáért és kezeléséért felelősek. A webalkalmazások számára az adatbázis a háttérrendszer, amelyben a felhasználói információk, projektek, dokumentumok és minden egyéb adat tárolódik. Az adatbázis lehetővé teszi az alkalmazás számára, hogy strukturált módon kezelje az adatokat, gyors hozzáférést biztosítson, és biztosítsa azok biztonságos tárolását.

#### **Entitás-kapcsolat diagram (ERD)**

https://www.lucidchart.com/pages/er-diagrams
https://www.geeksforgeeks.org/how-to-draw-entity-relationship-diagrams/
https://www.databasestar.com/entity-relationship-diagram/

A rendszer adatbázisának struktúráját az **Entitás-kapcsolat diagram (ERD)** mutatja be, amely szemlélteti a táblák közötti kapcsolatokat és azok relációit. Példa egy ERD-re:

- **Felhasználók**: ID, név, email, jelszó
- **Projektek**: ID, név, leírás, felhasználó_id (kapcsolódik a Felhasználók táblához)
- **Dokumentumok**: ID, cím, projekt_id (kapcsolódik a Projektek táblához), tartalom

#### **Adatbázis-struktúra és ORM**

https://docs.djangoproject.com/en/5.1/ref/databases/

- **Táblák és kapcsolatok**: A táblák közötti kapcsolatokat az **ORM** (Object-Relational Mapping) kezeli, amely lehetővé teszi a Python kódon keresztüli interakciót az adatbázissal anélkül, hogy közvetlenül SQL lekérdezéseket kellene írni.
- **Migrációk és adatbázis-kezelés**: A Django ORM támogatja az adatbázis migrációs rendszerét, amely lehetővé teszi az adatbázis verziók kezelését, így könnyedén frissíthetők a táblák, vagy új adatbázis-struktúrák építhetők be anélkül, hogy adatvesztés történne.
- Az adatbázisok közötti áttérés viszonylag egyszerű a **Django ORM (Object-Relational Mapping)** és migrációs rendszerének köszönhetően.
	- https://www.geeksforgeeks.org/django-orm-inserting-updating-deleting-data/
	- https://docs.djangoproject.com/en/5.1/topics/db/queries/
	- https://docs.djangoproject.com/en/5.1/ref/migration-operations/
- ***Példa adatmodellre:***
	- *Táblák és oszlopok bemutatása (pl. Felhasználók: ID, név, email, jelszó).*

#### **DIP (Dependency Inversion Principle)**

https://www.geeksforgeeks.org/dependecy-inversion-principle-solid/
https://www.baeldung.com/cs/dip

A **Dependency Inversion Principle** (DIP) az objektum-orientált tervezés egyik alapelve, amely biztosítja, hogy az alkalmazás moduljai ne függjenek közvetlenül az adatbázis implementációjától. Ez lehetővé teszi, hogy az adatbázis kezelését a rendszer más részeiről függetlenül lehessen cserélni vagy frissíteni, csökkentve a kód szoros kapcsolódásának kockázatát.

Több adatbázis használata: https://docs.djangoproject.com/en/5.1/topics/db/multi-db/

#### **Táblák közötti kapcsolat és normalizálás**

A táblák közötti kapcsolatok (pl. 1:1, 1:n, n:m) kialakítása során ezeket a normálformákat figyelembe véve biztosíthatjuk az adatbázis hatékony és redundanciától mentes felépítését.

https://www.geeksforgeeks.org/relationships-in-sql-one-to-one-one-to-many-many-to-many/

- **1:n kapcsolat**: A **Felhasználók** és a **Projektek** táblák közötti kapcsolat, ahol egy felhasználó több projektet is létrehozhat. Ezt a kapcsolatot a 2NF biztosítja, ahol a projektek táblájában a felhasználó azonosítója szerepel idegen kulcsként.
- **n:m kapcsolat**: A **Dokumentumok** és a **Projektek** táblák közötti kapcsolat, ahol egy dokumentum több projekthez is kapcsolódhat. Ennek kezelésére egy köztes táblát (pl. **Dokumentumok_Projektek**) alkalmazunk, amely tartalmazza mindkét táblát összekapcsoló idegen kulcsokat, így biztosítva az 3NF szerinti tiszta kapcsolatot.

A **normalizálás** a relációs adatbázisok tervezésében alkalmazott eljárás, amely a táblák struktúrájának optimalizálására és a redundancia minimalizálására szolgál. A normalizálás során a táblák kapcsolatai az adatbázis normálformáit követve kerülnek kialakításra. A normálformák (1NF, 2NF, 3NF) célja, hogy az adatok ne tartalmazzanak felesleges ismétlődéseket, és az adatkezelés hatékonyabbá váljon.

https://www.geeksforgeeks.org/introduction-of-database-normalization/
https://www.freecodecamp.org/news/database-normalization-1nf-2nf-3nf-table-examples/

- **1NF (Első normálforma)**: Az adatokat atomikus (oszthatatlan) értékekre bontja, megszüntetve a többszörös értékeket és tömböket.
- **2NF (Második normálforma)**: Az 1NF-t teljesíti, és biztosítja, hogy minden nem kulcsos attribútum függjön az elsődleges kulcstól.
- **3NF (Harmadik normálforma)**: A 2NF-t teljesíti, és megszünteti az olyan tranzitív függőségeket, ahol egy nem kulcsos attribútum másik nem kulcsos attribútumtól függ.

#### **SQLite**

Könnyű, beágyazott relációs adatbázis, amely ideális kisebb alkalmazásokhoz, fejlesztési környezetekhez és prototípusokhoz. 
- https://www.sqlite.org/index.html
- https://en.wikipedia.org/wiki/SQLite
- https://www.geeksforgeeks.org/sqlite-tutorial/
- https://sqldocs.org/sqlite-database/django-sqlite/

### *Felhasználói felület (UI) tervezés*

- ***Drótvázak (wireframes):***
    - *Alapvető képernyők vizuális megjelenítése (pl. kezdőlap, bejelentkezés, főoldal).*
    - https://careerfoundry.com/en/blog/ux-design/how-to-create-your-first-wireframe/
- ***Reszponzív design megtervezése:***
    - *Hogyan jelenik meg a UI különböző eszközökön (mobil, tablet, asztali gép).*
    - https://www.uxpin.com/studio/blog/best-practices-examples-of-excellent-responsive-design/
- ***UI/UX szempontok:***
    - *Felhasználóbarát elrendezés és interakciók.*
    - *Színek, tipográfia, ikonok szerepe.*
    - https://en.wikipedia.org/wiki/User_experience_design

### Backend

#### **Backend fogalma és szerepe a webalkalmazásokban**

https://builtin.com/software-engineering-perspectives/back-end-development
https://www.geeksforgeeks.org/frontend-vs-backend/
https://www.geeksforgeeks.org/backend-development/
https://www.applify.com.sg/blog/what-is-backend-in-web-development/
https://www.freecodecamp.org/news/learn-backend-development/

A backend felelős a webalkalmazás szerveroldali logikájáért és adatkezeléséért. Feladata az üzleti logika implementálása, az adatbázis-kezelés, valamint a frontend számára szükséges adatok kiszolgálása. A backend a felhasználói kéréseket dolgozza fel, és biztosítja az alkalmazás működését a háttérben.

#### **Django keretrendszer bemutatása**

 Django egy robusztus és biztonságos keretrendszer, amely gyors fejlesztést tesz lehetővé. A projekt számára ideális, mivel rendelkezik beépített adminisztrációs felülettel, ORM-mel, és jól dokumentált. A projekt backendje a **Django keretrendszer** lesz, amely Python nyelven alapul. A Django az egyik legnépszerűbb webfejlesztői keretrendszer, amely robusztus adatkezelési és skálázhatósági lehetőségeket biztosít.
- https://www.djangoproject.com/
- https://en.wikipedia.org/wiki/Django_(web_framework)
- https://www.w3schools.com/django/django_intro.php

- **Python**: Python egy magas szintű, értelmezett programozási nyelv, amelyet egyszerűsége és olvashatósága miatt széles körben használnak. Django teljes mértékben Python nyelven íródott, így a fejlesztéshez elengedhetetlen a Python alapjainak ismerete
	- https://www.python.org/doc/essays/blurb/
	- https://www.geeksforgeeks.org/what-is-python/
	- https://en.wikipedia.org/wiki/Python_(programming_language)
- **Parancssor (CLI)**: A Django fejlesztése során a parancssor (Command Line Interface, CLI) kulcsszerepet játszik, mivel számos adminisztratív és fejlesztési feladatot ezen keresztül lehet végrehajtani. A `manage.py` script segítségével indítható a fejlesztőszerver, alkalmazhatóak az adatbázis-migrációk és kezelhetők a felhasználók.
	- https://docs.djangoproject.com/en/5.1/ref/django-admin/
	- https://www.geeksforgeeks.org/custom-django-management-commands/
	- **Gyakran használt Django parancsok:**
	    - `python manage.py runserver` – Fejlesztőszerver indítása
        - `python manage.py makemigrations` – Adatbázis migrációk létrehozása
        - `python manage.py migrate` – Adatbázis frissítése
        - `python manage.py createsuperuser` – Admin felhasználó létrehozása
- **Virtuális környezet (virtualenv)**: Ajánlott egy elszigetelt környezet létrehozása a projekt számára, hogy elkerüljük a függőségek ütközését más projektekkel. A virtualenv segítségével különálló környezetet hozhatunk létre minden egyes projekthez.
	- https://docs.python.org/3/library/venv.html
	- **Virtuális környezet létrehozása és aktiválása:**
        - `python -m venv myenv` – Új virtuális környezet létrehozása
        - `source myenv/bin/activate` (Mac/Linux) vagy `myenv\Scripts\activate` (Windows) – Virtuális környezet aktiválása
        - `deactivate` – Virtuális környezet kikapcsolása
- **MVC vs. MTV**: Django az **MTV** (Model-Template-View) architektúrára épít, amely a **Model-View-Controller** (MVC) mintához hasonló, de a sablonok és nézetek kezelésében különbözik.
	- https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller
	- https://www.geeksforgeeks.org/mvc-framework-introduction/
	- https://www.geeksforgeeks.org/mvc-design-pattern/
	- https://www.geeksforgeeks.org/django-project-mvt-structure/
- **Class-Based Views (CBV) vs. Function-Based Views (FBV)**: A projektben dönteni kell a **Class-Based Views** és **Function-Based Views** között, ahol a CBV-k modulárisabbak és újrahasználhatók, míg az FBV-k egyszerűbbek és gyorsabban implementálhatók.
	- https://docs.djangoproject.com/en/5.1/topics/class-based-views/generic-display/
	- https://docs.djangoproject.com/en/5.1/topics/class-based-views/
	- https://learndjango.com/tutorials/django-best-practices-function-based-views-vs-clas
	- https://dev.to/codeitmichael/lets-talk-about-django-cbv-and-fbv-55ki
	- https://dev.to/ark7/class-and-function-based-views-in-django-3i41
- **View dekorátorok**: A **view dekorátorok** (view decorators) a Django-ban olyan függvények, amelyeket a nézetek (views) köré alkalmazunk, hogy módosítsuk azok működését. A dekorátorok egyfajta egyszerűsítést, kiterjesztést vagy ellenőrzést tesznek lehetővé anélkül, hogy magát a nézetet kellene módosítani. A dekorátorok a nézetek függvényére alkalmazott funkciók, amelyek valamilyen kiegészítő funkcióval látják el azokat.
	- https://docs.djangoproject.com/en/5.1/topics/http/decorators/
	- https://dev.to/ismailsoftdev/explaining-decorators-in-django-a-guide-for-beginners-9gl
	- **View dekorátorok használata Class-Based Views (CBV) esetén**:
		- A **View dekorátorok** a Django-ban olyan eszközök, amelyek lehetővé teszik, hogy a nézetek működését módosítsuk vagy kiegészítsük anélkül, hogy közvetlenül változtatnánk magán a nézet osztályán. A **Class-Based Views** (CBV) használatakor a dekorátorok alkalmazása kicsit eltér a **Function-Based Views** (FBV) esetétől, de alapvetően ugyanazokat a funkciókat biztosítják.
		- **`method_decorator` használata:** A CBV-k esetén a dekorátorok nem alkalmazhatóak közvetlenül az osztályra, mivel az osztály nem függvény. Azonban a **`method_decorator`** segítségével a dekorátorokat a CBV különböző metódusaira (pl. `get`, `post`) vagy a `dispatch` metódusra alkalmazhatjuk.
		- A `dispatch` metódus az a pont, ahol a kérés típusától függően (GET, POST stb.) meghívódik a megfelelő nézetmetódus. Ezért a dekorátorokat leggyakrabban itt szokás alkalmazni.
		- **Dekorátorok alkalmazása konkrét metódusokra:** Ha nem a teljes `dispatch` metódust szeretnénk védeni, hanem csak egy adott HTTP metódust (pl. `get` vagy `post`), akkor azt az egyes metódusokhoz is hozzáadhatjuk.
		- **Több dekorátor alkalmazása egy CBV-nél:** Ha több dekorátorra van szükség, például egyidejűleg szeretnénk érvényesíteni a bejelentkezési követelményt és a CSRF védelmet, akkor egyszerűen kombinálhatjuk őket.
		- https://www.geeksforgeeks.org/how-to-use-permission-required-decorators-with-django-class-based-views/
- **Middleware**: A Django middleware rendszere biztosítja az alkalmazás különböző rétegeiben végrehajtandó köztes műveletek kezelését.
	- https://docs.djangoproject.com/en/5.1/topics/http/middleware/
	- https://medium.com/scalereal/everything-you-need-to-know-about-middleware-in-django-2a3bd3853cd6
	- https://www.geeksforgeeks.org/middleware-in-django-image-video-error/
- **Django Admin felület**: A Django beépített admin felülete, amely lehetővé teszi az alkalmazás adatainak könnyű kezelését, felhasználók és csoportok kezelését, valamint a különböző modellek adminisztrálását.
	- https://docs.djangoproject.com/en/5.1/ref/contrib/admin/
	- https://www.w3schools.com/django/django_admin.php
	- https://medium.com/django-unleashed/how-to-use-django-admin-a-complete-walkthrough-for-beginners-in-2024-0f88fd0d79e9
- **Forms**: A Django forms modulja egyszerűsíti az adatbevitel kezelését és validálását a felhasználói felületen. Különféle formák létrehozásával és kezelésekkel gyorsan hozzáadhatók új adatbeviteli mechanizmusok.
	- https://www.geeksforgeeks.org/django-forms/
- **Models**: A Django modellek az adatbázis struktúráját reprezentálják, és segítenek az adatok tárolásában, lekérdezésében, valamint azok manipulálásában az ORM (Object-Relational Mapping) rendszerén keresztül.
	- https://www.w3schools.com/django/django_models.php
- **Authentikáció és autorizáció**: **Django Authentication**: A Django beépített autentikációs rendszere biztosítja a felhasználói regisztrációt, bejelentkezést, jogosultságok kezelését és jelszókezelést.
    - [Django Authentication dokumentáció](https://docs.djangoproject.com/en/5.1/topics/auth/default/)
    - [Learn Django: Login and Logout tutorial](https://learndjango.com/tutorials/django-login-and-logout-tutorial)
    - [GeeksforGeeks: User Authentication System using Django](https://www.geeksforgeeks.org/user-authentication-system-using-django/)

**Don’t Repeat Yourself (DRY) filozófia**:
- A Django egyik alappillére a DRY elv, amely arra ösztönöz, hogy a kódot ne ismételjük meg, hanem újrahasználható komponenseket és funkciókat építsünk. A DRY célja a kód ismétlésének minimalizálása, így biztosítva a könnyebb karbantartást és bővítést.
- A Django lehetőséget biztosít arra, hogy a modellek, nézetek és sablonok közötti kódot megoszthassuk, ami javítja a kód olvashatóságát és karbantartását.
- Például a **Class-Based Views (CBV)** használatával a funkciók újrafelhasználhatók, és az ismétlődő kódot központi helyeken lehet kezelni. A Django **Form** és **Model** rendszerei is segítenek az adatok kezelésében anélkül, hogy manuálisan kellene ismételni azokat a különböző helyeken.
- A **Django ORM** rendszerén keresztül az adatbázis-interakciók is újrahasználhatók és könnyen bővíthetők, ami minimalizálja a redundanciát.
- A DRY elv előnyei közé tartozik a kódkezelés egyszerűsítése, a hibák csökkentése és a gyorsabb fejlesztés.

#### **Backend programozási módszerek**

- **TDD (Test-Driven Development) szerepe a fejlesztési folyamatban**  
    A TDD (Test-Driven Development) módszer a fejlesztési folyamatban biztosítja, hogy minden egyes funkció és szolgáltatás tesztelhető legyen. A TDD célja, hogy a kódírás előtt először megírjuk a teszteket, amelyek meghatározzák a kívánt funkcionalitást. A tesztek alapján fejlesztjük a kódot, hogy azok sikeresen lefussanak, így biztosítva a stabilitást és a hibák korai felismerését. A módszer segít abban is, hogy a kód könnyen karbantartható és bővíthető legyen, hiszen a tesztelés folyamatos visszajelzést ad a kód minőségéről.
	- Használt tesztelési keretrendszerek: `pytest` és `unittest` a Python környezetben.
	- https://www.geeksforgeeks.org/test-driven-development-tdd/
	- https://en.wikipedia.org/wiki/Test-driven_development
    
- **BDD (Behavior-Driven Development)**  
	- https://www.geeksforgeeks.org/behavioral-driven-development-bdd-in-software-engineering/
    A BDD (Behavior-Driven Development) a TDD továbbfejlesztett változata, amely a felhasználói történetek és viselkedések megértésére összpontosít. A BDD célja, hogy a fejlesztők, tesztelők és nem technikai érintettek között egy közös nyelvet biztosítson, hogy mindenki számára világos legyen a rendszer kívánt működése. A BDD-t gyakran a "Given-When-Then" szintaxis segítségével alkalmazzák, amely segít abban, hogy a rendszer viselkedését egyértelműen és érthetően dokumentálják.
    - **Given**: Az alkalmazás aktuális állapota, a környezet vagy a kiinduló helyzet.
    - **When**: A felhasználó által végrehajtott művelet vagy esemény.
    - **Then**: Az alkalmazás várható reakciója vagy eredménye a művelet után.
    A BDD előnye, hogy az üzleti logika és a fejlesztési folyamatok közötti kommunikációt javítja, és lehetővé teszi a tesztelők számára, hogy jobban megértsék a projekt céljait. A Django esetében a BDD gyakran együtt használható a **pytest-bdd** vagy a **Behave** eszközökkel, amelyek segítenek a tesztek írásában a BDD elveinek megfelelően.

#### **A backend és az adatbázis kapcsolata**

**ORM (Object-Relational Mapping) magyarázata Django-ban** A Django ORM lehetővé teszi, hogy Python osztályok segítségével kezeljük az adatbázist, anélkül hogy SQL lekérdezéseket írnánk. Az ORM biztosítja az adatok egyszerű manipulálását és lekérdezését.
- https://docs.djangoproject.com/en/5.1/ref/databases/

### Frontend

#### **Frontend fogalma**

https://www.geeksforgeeks.org/front-end-development/
https://en.wikipedia.org/wiki/Front-end_web_development

A **frontend** az a rész, amely a webalkalmazások vagy weboldalak felhasználói felületének kialakításáért felelős. Az alapvető frontend technológiák közé tartozik a **HTML (HyperText Markup Language)**, **CSS (Cascading Style Sheets)** és **JavaScript**, amelyek lehetővé teszik, hogy a weboldal vagy alkalmazás vizuálisan és funkcionálisan megfelelően működjön a felhasználók számára.

- **HTML:** Az oldal struktúrájának meghatározásáért felelős, például a szövegeket, képeket, táblázatokat, listákat és más tartalmakat elhelyező markup nyelv.
- **CSS:** Az oldal vizuális megjelenését szabályozza, például a színek, betűtípusok, margók, elrendezések és animációk meghatározásával.
- **JavaScript:** A dinamikus viselkedést biztosítja, lehetővé téve az interaktív elemeket, mint a gombok, menük, űrlapok validálása, adatfeldolgozás és aszinkron műveletek végrehajtása.

A frontend az, amit a felhasználó közvetlenül lát és amivel interakcióba lép, tehát a felhasználói élmény (UX) szempontjából kulcsfontosságú.

#### **Frontend szerepe a felhasználói élmény biztosításában:**

https://moldstud.com/articles/p-what-is-the-role-of-front-end-web-developers-in-user-experience-design
https://simomhasan.com/the-role-of-frontend-frameworks-in-enhancing-user-interface-and-user-experience/
https://medium.com/@infocampus2000/the-importance-of-front-end-development-in-shaping-digital-experiences-c91f10117b9e

A frontend feladata, hogy a felhasználóknak olyan élményt nyújtson, amely egyszerű, kényelmes és élvezetes. A felhasználói élmény (UX) nem csupán azt jelenti, hogy az alkalmazás szép vagy jól néz ki, hanem azt is, hogy az alkalmazás könnyen használható, és megfelel a felhasználók igényeinek.

1. **Vizuális megjelenés (UI Design):** A frontend elsődleges szerepe a felhasználói felület (UI) létrehozása. Ez magában foglalja a színek, betűtípusok, ikonok, képek és egyéb vizuális elemek megfelelő használatát annak érdekében, hogy az alkalmazás esztétikailag vonzó legyen. A jól megtervezett UI segít abban, hogy a felhasználók könnyedén eligazodjanak az oldalon, és gyorsan megtalálják a számukra szükséges információkat.
2. **Reszponzív dizájn:** Mivel a felhasználók különböző eszközöket használnak (mobiltelefonok, táblagépek, asztali számítógépek), a reszponzív dizájn biztosítja, hogy az alkalmazás felülete minden eszközön optimálisan jelenjen meg. A frontendnek képesnek kell lennie arra, hogy automatikusan alkalmazkodjon a képernyő méretéhez, és biztosítja, hogy a felhasználói élmény ne csorbuljon, bárhonnan is érkezzenek.
3. **Interaktivitás és dinamikus tartalom:** Az interaktív elemek, mint a gombok, menük, formák, segítenek a felhasználóknak az alkalmazással való aktív kapcsolódásban. A frontend dinamikus funkciókat is biztosít, mint például az adatbeviteli űrlapok validálása, a menük lebegtetése vagy az animált elemek. A dinamikus viselkedés és a gyors válaszidő kulcsfontosságú a pozitív felhasználói élményhez.
4. **Navigáció és struktúra:** A frontend felületek intuitív navigációt biztosítanak, amely segít a felhasználóknak könnyen áttekinteni az alkalmazást és gyorsan elérni a kívánt funkciókat. A jól megtervezett navigáció nemcsak az esztétikát, hanem a funkcionalitást is szolgálja, így a felhasználók nem tévednek el, és gyorsan végrehajthatják az általuk kívánt műveleteket.
5. **Sebesség és teljesítmény:** A frontend szintén felelős az alkalmazás betöltési sebességéért és válaszidejéért. A lassú vagy hibásan működő frontend csökkentheti a felhasználói élményt, ezért a frontend fejlesztésénél figyelembe kell venni a teljesítményt. A képek optimalizálása, az aszinkron JavaScript használata és a gyors betöltést segítő eszközök mind hozzájárulnak a gördülékeny felhasználói élményhez.
6. **Szórakoztató és felhasználóbarát élmény:** A frontend segíthet a webalkalmazás élvezetessé tételében azáltal, hogy szórakoztató interakciókat, animációkat és visszajelzéseket kínál a felhasználónak. Ezek az élvezetes és figyelmes interakciók növelhetik a felhasználók elégedettségét, és ösztönözhetik őket arra, hogy hosszabb ideig használják az alkalmazást.

#### **HTML, CSS és JavaScript szerepe:**

- **HTML (HyperText Markup Language):** A weboldal struktúráját adja meg. Az alkalmazás elemeit (például fejlécek, bekezdések, képek, hivatkozások) HTML-ben helyezzük el.
	- https://developer.mozilla.org/en-US/docs/Web/HTML
	- https://en.wikipedia.org/wiki/HTML
	- **HTML5 szemantikai elemek alkalmazása:** A `<header>`, `<footer>`, `<article>`, `<section>`, nemcsak az oldal struktúrájának világosabbá tételében segítenek, hanem javítják a SEO (Search Engine Optimization) eredményeket is. Azáltal, hogy az oldal elemeit megfelelően címkézzük és elrendezzük, a keresőmotorok könnyebben megértik az oldal tartalmát, így jobb keresési rangsort érhetünk el.
		- https://en.wikipedia.org/wiki/HTML5
		- https://www.geeksforgeeks.org/html5/
		- https://www.geeksforgeeks.org/html5-introduction/
- **CSS (Cascading Style Sheets):** A CSS szabályozza az alkalmazás vizuális megjelenését, például a színeket, betűtípusokat, elrendezéseket. A CSS segít a reszponzív dizájnban is, amely biztosítja, hogy az oldal különböző eszközökön (mobil, tablet, asztali gép) jól jelenjen meg.
	- https://en.wikipedia.org/wiki/CSS
	- https://developer.mozilla.org/en-US/docs/Web/CSS
	- https://www.w3.org/Style/CSS/Overview.en.html
- **JavaScript:** A JavaScript dinamikus viselkedést ad az alkalmazásnak. A frontend interaktív funkcióit JavaScript biztosítja, például űrlapok validálása, dinamikus menük és interaktív tartalom megjelenítése. A JavaScript segíti a felhasználói élmény javítását azáltal, hogy a felhasználó által végzett műveletek az oldal frissítése nélkül is hatással vannak az alkalmazás működésére (például AJAX használatával).
	- https://en.wikipedia.org/wiki/JavaScript
	- https://www.w3schools.com/js/js_intro.asp

#### **Bootstrap szerepe a felhasználói élmény javításában**

- https://getbootstrap.com/
- https://en.wikipedia.org/wiki/Bootstrap_%28front-end_framework%29

A **Bootstrap** egy rendkívül népszerű front-end keretrendszer, amely lehetővé teszi a gyors és hatékony felhasználói felület fejlesztést. A Bootstrap segítségével a fejlesztők könnyen alkalmazhatják a reszponzív dizájn elveit és egyszerűsített komponens-alapú megközelítést alkalmazhatnak a felületek megtervezésében. A keretrendszer előre definiált CSS osztályokat és JavaScript komponenseket biztosít, amelyek segítenek a felhasználói élmény fokozásában az alábbiak révén:

1. **Reszponzív dizájn:** A Bootstrap grid rendszere automatikusan alkalmazkodik a különböző képernyőméretekhez, így biztosítva a felhasználói felület optimális megjelenését bármely eszközön (mobil, tablet, desktop). Ez segít abban, hogy a felhasználói élmény ne csökkenjen a különböző platformokon való használat során.
2. **Beépített komponensek:** A Bootstrap számos előre elkészített komponenst kínál, mint például navigációs sávok (navbar), legördülő menük, gombok, formázott űrlapok és értesítések. Ezek a komponensek egyszerűsítik a felhasználói interakciók kialakítását, és biztosítják, hogy a felületek esztétikailag és funkcionálisan is jól működjenek.
3. **Könnyen használható formák:** A Bootstrap űrlapok, bemenetek és validációs mechanizmusok megkönnyítik a felhasználói adatbevitelt. A formák intuitív módon lettek kialakítva, segítve a felhasználókat abban, hogy gyorsan és pontosan kitöltsék azokat.
4. **Esztétikai egység:** A keretrendszer biztosítja a konzisztens dizájnt, beleértve a színeket, tipográfiát és elrendezéseket, amelyek biztosítják, hogy az alkalmazás minden képernyőn és eszközön vonzó és könnyen kezelhető maradjon.
5. **Testreszabhatóság:** A Bootstrap lehetőséget ad arra, hogy a fejlesztők testreszabják a stílusokat a saját igényeiknek megfelelően, anélkül, hogy teljesen újra kellene alkotniuk az alapvető dizájnelemeket.

#### ***Interaktív elemek és dinamikus tartalom:***

*A frontendnek képesnek kell lennie interaktív elemek kezelésére. A JavaScript segítségével lehetőség van **űrlapok validálására** (ellenőrzés, hogy a felhasználó helyesen adta-e meg az adatokat), **dinamikus menük** kialakítására (a menü elemek interaktívan változnak attól függően, hogy a felhasználó hova kattint), és más frontend logikák alkalmazására. Az interaktív elemek segítenek a felhasználói élmény fokozásában, miközben egyszerűsítik a navigálást és az adatbevitelt.*

#### **Django Template rendszer**

A Django templating rendszerének célja, hogy dinamikus HTML tartalmat generáljon a backend és frontend közötti adatátvitel révén. A **Django templating** rendszere lehetővé teszi dinamikus tartalom generálását HTML-ben. A Django template nyelve segítségével változókat, ciklusokat és feltételeket alkalmazhatunk az oldalon. A frontend és a backend közötti adatküldés és megjelenítés hatékony módja.
- https://docs.djangoproject.com/en/5.1/ref/templates/language/
- https://www.geeksforgeeks.org/django-templates/

**Template Inheritance (Sablon öröklés)**
A **template inheritance** a Django templating rendszerének egyik alapvető jellemzője, amely lehetővé teszi a sablonok újrahasználatát és a kód ismétlődésének minimalizálását. Ezzel a megoldással egy alap sablont (pl. `base.html`) hozunk létre, amely tartalmazza a közös elemeket (például fejléc, lábléc, navigációs menük), és ezt az alapot örökölhetik a különböző oldalak. Ezáltal, ha egy közös elem megváltozik (pl. a fejléc módosul), nem kell minden egyes oldalt külön frissíteni, elég az alapértelmezett sablont módosítani.
- https://www.geeksforgeeks.org/django-templates/
- https://docs.djangoproject.com/en/5.1/ref/templates/language/
- https://www.askpython.com/django/django-template-inheritance
- **extends**: Az `extends` tagot a sablonok öröklésére használják Django-ban. Így elkerülhető, hogy ugyanazt a kódot újra és újra meg kelljen ismételni. Az `extends` segítségével sablonokat és változókat is örökölhetünk. https://www.geeksforgeeks.org/extends-django-template-tags/

**Partials fájlok alkalmazása a HTML struktúra felépítésében**
A **partials fájlok** lehetővé teszik a HTML kód modularizálását. Ezek a fájlok olyan közös elemeket tartalmaznak, mint például a fejléc, lábléc vagy navigációs menük. Ahelyett, hogy minden oldalra újraírnánk ezeket az elemeket, a partials fájlok segítségével egyszerűen beilleszthetjük őket az oldalba. Ezáltal elkerülhetjük a kód ismétlését, és javíthatjuk a karbantarthatóságot.
A Django templating rendszerével könnyedén beilleszthetők ezek az elemek a fő sablonokba, biztosítva ezzel a konzisztenciát és a könnyű frissíthetőséget az alkalmazás különböző részei között.
- **include:** Az `include` tag segítségével egy másik sablont ágyazhatunk be a fő sablonba, így újrahasznosíthatjuk a közös komponenseket, például a fejlécet vagy a láblécet. https://www.geeksforgeeks.org/include-django-template-tags/

**Django elemek integrálása HTML kódban**
A **Django templating** rendszere lehetővé teszi dinamikus tartalom generálását HTML-ben, ahol különféle **template tag-ek** segítségével hozhatunk létre logikai műveleteket és strukturálhatjuk a tartalmat. A template nyelvben használhatók **változók**, **ciklusok**, **feltételek**, valamint komplex vezérlési szerkezetek, amelyek lehetővé teszik a backendről érkező adatok dinamikus megjelenítését a frontend oldalakon. https://www.geeksforgeeks.org/django-template-tags/
- **Változók:** 
	- A Django sablonokban a változók segítségével dinamikusan jeleníthetjük meg a backendről érkező adatokat. Például egy változó beillesztésével jeleníthetjük meg a felhasználó nevét, vagy egy lista elemeit. A változókat a `{{ }}` szintaxissal használjuk. https://www.geeksforgeeks.org/variables-django-templates/
- **Ciklusok**: 
	- **for loop** :  A `for` tag minden elemre iterál egy tömbben, és az elemet elérhetővé teszi egy kontextusváltozóban. https://www.geeksforgeeks.org/for-loop-django-template-tags/
	- **for … empty loop** : A `for` tag minden elemre iterál egy tömbben, és az elemet elérhetővé teszi egy kontextusváltozóban. A `for` tag opcionálisan tartalmazhat egy `{% empty %}` záradékot, amely akkor jelenik meg, ha a megadott tömb üres vagy nem található. Ez alapvetően egy feltételként használható, hogy ellenőrizzük, üres-e a lekérdezés, és milyen műveletet kell végrehajtani az adott helyzetben. https://www.geeksforgeeks.org/for-empty-loop-django-template-tags/
- **Feltételek**:
	- **if** : A `{% if %}` tag értékeli egy változó értékét, és ha az a változó "igaz" (azaz létezik, nem üres, és nem hamis logikai érték), akkor a blokk tartalmát kiírja. https://www.geeksforgeeks.org/if-django-template-tags/
	- **Logikai operátorok**: A `{% if %}` tag használatakor különböző logikai operátorok alkalmazhatók. A Django sablon rendszerében az `and`, `or` és `not` operátorok segítségével összetettebb feltételeket hozhatunk létre, lehetővé téve bonyolultabb logikai kifejezések kiértékelését. https://www.geeksforgeeks.org/boolean-operators-django-template-tags/
- **Egyéb műveletek**
	- **Comment:** A `{% comment %}` és `{% endcomment %}` közötti szöveget a sablon figyelmen kívül hagyja. Ez hasznos lehet a kód dokumentálásához vagy ideiglenes kód blokkok letiltásához. https://www.geeksforgeeks.org/comment-django-template-tags/
	- **Cycle:** A `{% cycle %}` tag ciklikusan ismétel különböző értékeket minden találkozáskor. https://www.geeksforgeeks.org/cycle-django-template-tags/
	- **Firstof:** A `{% firstof %}` tag visszaadja az első olyan változót, amely nem "hamis" (létezik, nem üres, nem nulla, nem hamis logikai érték). https://www.geeksforgeeks.org/firstof-django-template-tags/
	- **lorem**: A `{% lorem %}` tag véletlenszerű "lorem ipsum" latin szöveget jelenít meg. Hasznos sablonokban mintaműveletekhez. https://www.geeksforgeeks.org/lorem-django-template-tags/
	- **now**: A `{% now %}` tag a jelenlegi dátumot és/vagy időt jeleníti meg a megadott formátum szerint. Az ilyen formátum sztring tartalmazhat formátum specifikátor karaktereket. https://www.geeksforgeeks.org/now-django-template-tags/
	- **url**: Az `{% url '%}` tag egy abszolút elérési utat ad vissza (URL domain név nélküli része), amely egy adott nézetet és opcionális paramétereket tartalmaz. Ez lehetővé teszi a hivatkozások kiírását anélkül, hogy megsértenénk a DRY elvet, mivel nem szükséges keménykódolni az URL-eket a sablonokban. https://www.geeksforgeeks.org/url-django-template-tag/

#### **MVT kapcsolata a frontenddel:**

A **Model-View-Template (MVT)** architektúra, amelyet a Django alkalmaz, szintén segít az alkalmazás különböző részeinek elválasztásában. A frontend a **View** és a **Template** részeket érinti, amelyek közvetlenül kapcsolódnak a felhasználói felülethez.
- **View (Nézet):** A frontend része, amely az adatokat jeleníti meg a felhasználónak. Az alkalmazás adatainak megjelenítéséért a View felelős, és lehetővé teszi a felhasználóval való interakciót.
- **Template (Sablon):** A Django sablonmotorját használja a frontend a HTML és dinamikus adatkezelés összehangolására. A Template felelős a statikus HTML oldalak dinamikus tartalommal való feltöltéséért, amelyet a View küld a felhasználónak. A sablonban helyezkednek el az olyan helyettesítő elemek, mint a változók és ciklusok, amelyek a backend által küldött adatokat jelenítik meg.

### Konténerizáció (Docker)

A **konténerizáció** a fejlesztési környezetek gyors és egyszerű beállítását, valamint a különböző környezetek közötti zökkenőmentes átállást biztosítja. A **Docker** és **Docker Compose** eszközök segítségével a fejlesztési és tesztelési környezetek elkülönítése és egyszerű kezelése válik lehetővé.

- https://www.docker.com/
- https://en.wikipedia.org/wiki/Docker_(software)
- https://www.freecodecamp.org/news/what-is-docker-compose-how-to-use-it/
- https://docs.docker.com/compose/
- https://rtt.koczka.com/docker.html
- https://docker.koczka.com/

#### Docker szerepe:

- **Környezeti izoláció**: A Docker lehetővé teszi a különböző fejlesztési és tesztelési környezetek izolálását, biztosítva, hogy a rendszer minden komponense függetlenül, mégis együttműködve működjön. Ez segít elkerülni a verzióbeli inkompatibilitásokat és a környezeti problémákat, amelyek a különböző rendszerek között jelentkezhetnek.

#### Dockerfile és docker-compose.yml:

- **Dockerfile**: A Dockerfile segítségével konténereket hozhatunk létre, amelyek minden szükséges környezetet és alkalmazást tartalmaznak a fejlesztési és tesztelési folyamatokhoz. A Dockerfile egy szöveges fájl, amely tartalmazza a szükséges parancsokat és beállításokat, hogy az adott környezetet a kívánt módon telepítse és konfigurálja.
- **docker-compose.yml**: A Docker Compose egy eszköz, amely lehetővé teszi több konténer összefogását és kezelését egyetlen fájlban. A `docker-compose.yml` fájlban definiálhatjuk a különböző szolgáltatásokat, azok kapcsolatát és az indításhoz szükséges beállításokat, így egyetlen parancs futtatásával az egész rendszer elindítható.

A konténerizáció előnyei közé tartozik a gyorsabb fejlesztési ciklus, a jobb skálázhatóság, és a különböző környezetek közötti zökkenőmentes átállás, amelyek mind hozzájárulnak a fejlesztési és deploy folyamatok hatékonyságához.

### Biztonsági tervezés

#### **Adatbiztonság**

Adatbiztonság alatt értjük minden olyan technikai és szervezeti intézkedést, amelyek biztosítják az alkalmazásban kezelt adatok védelmét a jogosulatlan hozzáférés, módosítás, törlés és elvesztés ellen. A legfontosabb elemei:

**SSL/TLS és HTTPS**
A webalkalmazás titkosítása elengedhetetlen az adatbiztonság szempontjából. A HTTPS protokoll használatával biztosítható, hogy az alkalmazás titkosítva továbbítsa az adatokat, megakadályozva ezzel a harmadik felek általi lehallgatást és manipulációt.
A Django alapból támogatja az SSL/TLS titkosítást, amely biztosítja az internetes adatforgalom titkosítását. Az SSL/TLS biztosítja, hogy az adatok titkosítva legyenek, amikor azok a szerver és a kliens között áramlanak. Az SSL/TLS beállítása általában a webszerver (pl. Nginx, Apache) konfigurálásánál történik, és a Django alkalmazásban az alábbi beállításokat találjuk:
- **SECURE_SSL_REDIRECT**: Ha engedélyezve van, a Django automatikusan átirányítja a HTTP kéréseket HTTPS-re.
- **SECURE_HSTS_SECONDS**: HTTP Strict Transport Security (HSTS) támogatás, amely biztosítja, hogy a böngészők csak HTTPS-t használjanak a domainhez való kapcsolódáskor.
- **SECURE_BROWSER_XSS_FILTER**: Biztosítja, hogy a böngésző titkosított kapcsolatok esetén engedélyezze az XSS szűrést.

- https://docs.djangoproject.com/en/stable/ref/settings/#secure-ssl-redirect

- https://en.wikipedia.org/wiki/HTTPS
- https://www.geeksforgeeks.org/difference-between-http-and-https-2/
- https://www.geeksforgeeks.org/explain-working-of-https/
- https://www.digicert.com/what-is-ssl-tls-and-https
- https://www.ssl.com/hu/article/what-is-an-ssl-tls-certificate/
- https://hu.wikipedia.org/wiki/Transport_Layer_Security
- https://www.geeksforgeeks.org/difference-between-secure-socket-layer-ssl-and-transport-layer-security-tls/

**Fájlok biztonságos kezelése**  
A fájlok biztonságos kezelése magában foglalja azok megfelelő tárolását, validálását és titkosítását. A felhasználók által feltöltött fájlokat át kell vizsgálni vírusok, malware-ek után, és biztosítani kell, hogy a fájlok ne tartalmazzanak semmilyen kártékony kódot. Emellett a fájlok tárolása biztonságos módon történik, például titkosított adatbázisban vagy fájlrendszeren. Az érzékeny információkat – például banki adatokat vagy személyes dokumentumokat – mindig titkosított formában kell tárolni, hogy megakadályozzuk azok illetéktelen hozzáférését.
	- **Fájlok validálása**: Django rendelkezik a `FileField` és `ImageField` mezőkkel, amelyek lehetővé teszik fájlok feltöltését és azok típusának validálását. Azonban a fájlok vírusellenőrzése és egyéb biztonsági szempontok nem tartoznak a beépített funkcionalitások közé. A fájlok validálására például egyéni validátorokat készíthetsz, amik ellenőrzik a fájlok típusát, méretét, vagy egyéb tulajdonságait, például hogy ne töltsenek fel végrehajtható fájlokat.
	- **Fájlok vírusellenőrzése**: Mivel a Django nem tartalmaz beépített vírusellenőrzési mechanizmust, a fájlok vírusellenőrzését külső szolgáltatásokkal kell megoldani. Az egyik lehetőség a vírusellenőrző eszközök, mint például a **ClamAV**, amelyet a Django alkalmazásba integrálhatsz a fájlok biztonságos feltöltése érdekében.
	- **Fájlok titkosítása**: Django nem kínál beépített megoldást a fájlok titkosítására, de számos külső csomagot találhatsz, mint például a `django-encrypted-filefield`, amely lehetővé teszi fájlok titkosítását az adatbázisban történő tárolás előtt. Az ilyen titkosítást általában az alkalmazás fejlesztői oldalon kell megvalósítani, például titkosítási könyvtárak, mint a **Fernet** (a cryptography csomag részeként) használatával.

**Jelszavak titkosítása**  
A jelszavak biztonságos kezelése alapvető a rendszer védelme érdekében. A jelszavakat soha nem szabad tárolni tiszta szövegként, hanem egyirányú titkosítással (hashing) kell tárolni őket. A leggyakoribb és legbiztonságosabb eljárások közé tartozik a bcrypt, Argon2 vagy PBKDF2, amelyek megnehezítik a jelszavak visszafejtését. Az alkalmazásnak emellett biztosítania kell a megfelelő jelszószabályokat, mint például a minimális hosszúságot, a karakterek variálását (kis- és nagybetűk, számok, speciális karakterek), valamint a jelszó újragenerálásának kötelezettségét meghatározott időnként.
- **Jelszó titkosítás**: A Django automatikusan titkosítja a jelszavakat a beépített `User` modellek használatával, ezzel biztosítva azok biztonságos tárolását. A Django beépített **PBKDF2** vagy **bcrypt** titkosítással biztosítja a jelszavak titkosítását.
Django beépített támogatást nyújt a jelszavak biztonságos tárolásához. A jelszavakat a következő algoritmusokkal titkosítja:
- **PBKDF2** (Alapértelmezett)
- **bcrypt** (Ha telepítve van a `django-bcrypt` csomag)
- **Argon2** (Ha telepítve van a `argon2` csomag)
Ez a titkosítás egyirányú, tehát a jelszó visszafejtése nem lehetséges. A Django `PASSWORD_HASHERS` beállítása lehetővé teszi, hogy más titkosítási módszert válasszunk. További részletek: [Django password management](https://docs.djangoproject.com/en/stable/topics/auth/passwords/)
- https://docs.djangoproject.com/en/4.2/topics/auth/passwords//

**django-cryptography**
https://django-cryptography.readthedocs.io/en/latest/index.html
A **django-cryptography** egy Django alkalmazás, amely egyszerűsíti a titkosítást az adatbázisban tárolt érzékeny adatok számára. A csomag lehetővé teszi a titkosított mezők egyszerű kezelését a Django modellekben. 

**Környezeti változók kezelése**  
A környezeti változók használata segít a biztonságos tárolásban, mivel az érzékeny adatokat nem tároljuk közvetlenül a kódban. A titkos kulcsok, adatbázis hitelesítési adatok és egyéb érzékeny információk a környezeti változók segítségével kerülnek biztonságos módon a rendszerbe. A `settings.py` fájlban való tárolás helyett a környezeti változók használata biztosítja, hogy az érzékeny adatokat ne lehessen könnyen hozzáférni a kód publikálása során.
- **django-environ**: A **django-environ** a Django közösség körében népszerű eszköz, amely lehetővé teszi, hogy környezeti változókat és `.env` fájlokat használjunk a projekt beállításaihoz. Az eszköz egyszerűsíti az érzékeny adatok tárolását és az adatbázis-beállítások, titkos kulcsok, valamint egyéb konfigurációs elemek környezeti változókon keresztüli kezelését. https://djangocentral.com/environment-variables-in-django/

#### **Hozzáférés-ellenőrzés**

A Django beépített hitelesítési és jogosultsági rendszere lehetővé teszi, hogy a felhasználókat különböző szerepkörökhöz rendeljük, és minden szerepkörhöz más jogosultságokat biztosítsunk.

**Felhasználói szerepkörök és jogosultságok**
A Django alapértelmezetten támogatja a felhasználói szerepköröket és jogosultságokat. A `User` modell és az `auth` alkalmazás segítségével kezelhetők a felhasználói adatok és jogosultságok.
- **Felhasználói szerepkörök kezelése**: A Django-ban minden felhasználó rendelkezhet különböző szerepkörökkel, mint például adminisztrátor, normál felhasználó, vendég stb. A `User` modellhez rendelhetők jogosultságok a `Group` és `Permission` osztályokkal.

**Hitelesítés és jogosultság kezelés**
A Django beépített hitelesítési mechanizmusa (mint például a `django.contrib.auth`) automatikusan kezeli a felhasználói bejelentkezést, a regisztrációt, és a jogosultságokat. https://docs.djangoproject.com/en/5.1/topics/auth/default/
- **Bejelentkezés**: Az alapértelmezett bejelentkezési mechanizmus a `login()` és `logout()` függvényekkel valósítható meg.
- **Felhasználói jogosultságok ellenőrzése**: Django-ban a hozzáférési jogosultságok kezelése a **dekorátorok** segítségével könnyen megoldható. A leggyakrabban használt dekorátorok, mint például a `@login_required` és a `@permission_required`, közvetlenül kapcsolódnak a felhasználók hozzáférésének szabályozásához, biztosítva, hogy csak a megfelelő jogosultsággal rendelkező személyek férhessenek hozzá egyes nézetekhez vagy alkalmazásrészekhez.
	- `@login_required`: Az egyik leggyakrabban alkalmazott dekorátor, amely biztosítja, hogy a felhasználó be legyen jelentkezve, mielőtt hozzáférne a védett nézetekhez. Ha a felhasználó nincs bejelentkezve, a dekorátor átirányítja őt a bejelentkezési oldalra.
	- `@permission_required`: Ez a dekorátor biztosítja, hogy a felhasználó rendelkezzen a szükséges jogosultságokkal (pl. adminisztrátori jogosultságok, szerkesztési jogok) a nézet végrehajtásához. Különböző jogosultságokat ellenőrizhetünk vele, amelyeket a felhasználók csoportokhoz vagy egyéni felhasználói jogokhoz rendelhetnek.
	- `@user_passes_test`: Ez a dekorátor lehetővé teszi, hogy egyéni teszteket hajtsunk végre a felhasználói hozzáférés ellenőrzésekor. Alkalmazásával bonyolultabb logikát is megvalósíthatunk, például egyedi feltételek alapján (pl. ha a felhasználó bizonyos csoportban van).

**Session kezelés és cookie biztonság**  
A session kezelés és a cookie biztonsága kulcsfontosságú a webalkalmazások biztonságában, mivel a session információk és a cookie-k tárolják a felhasználói állapotot és az autentikációs adatokat. A Django automatikusan kezeli a session állapotokat, amelyeket a bejelentkezett felhasználók számára használunk. A session információk tárolásához egy egyedi azonosítót rendelünk minden felhasználóhoz, amelyet a böngésző cookie-jai tárolnak.

**Session kezelés**  
A session biztosítja, hogy a felhasználó bejelentkezése után a rendszer megjegyezze az ő interakcióit anélkül, hogy minden egyes kéréskor újra hitelesítenie kellene magát. A session azonosítók biztonságos tárolása és kezelése elengedhetetlen. A legjobb gyakorlatok közé tartozik a session azonosítók titkosítása, élettartamuk korlátozása és a session lejáratának kezelése.
A Django alapértelmezett session mechanizmusa a `django.contrib.sessions` alkalmazásban található. Az alapértelmezett beállítások a következők:
- **Session időtartama**: A session lejáratának időtartamát a `SESSION_COOKIE_AGE` beállítással lehet meghatározni (alapértelmezetten 300 másodperc). A session lejáratát úgy kezelhetjük, hogy a felhasználók automatikusan kijelentkeznek, amikor a session időtartama lejár.
- **Session titkosítás**: A session azonosítót titkosítva tárolhatjuk a böngésző cookie-jában a `SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'` beállítással.

**Cookie biztonság**  
A cookie-k gyakran tárolják a felhasználói hitelesítési adatokat. Ahhoz, hogy ezek ne kerüljenek illetéktelen kezekbe, fontos biztosítani, hogy a cookie-kat csak HTTPS kapcsolaton keresztül lehessen továbbítani (Secure flag), és hogy csak a szükséges időre legyenek érvényesek (HttpOnly és SameSite cookie beállítások). Az HttpOnly biztosítja, hogy a cookie-k ne legyenek elérhetők JavaScript által, míg a SameSite megakadályozza, hogy a cookie-kat más domainről lehessen felhasználni (CSRF támadások megelőzése).
A Django lehetőséget biztosít a cookie-k biztonságos kezelésére, például a hitelesítési adatok tárolására a `django.contrib.auth` alkalmazás által használt `sessionid` cookie-ban.
- **HTTPS**: A cookie-kat csak HTTPS kapcsolaton keresztül kell továbbítani, amelyhez a `SESSION_COOKIE_SECURE` beállítást kell használni. Ez biztosítja, hogy a cookie-k nem kerülnek továbbításra HTTP-n keresztül, ami megelőzi az adatlopásokat.
- **HttpOnly**: Az `HttpOnly` beállítás megakadályozza, hogy a cookie-k JavaScript által elérhetők legyenek. Ezt a beállítást a `SESSION_COOKIE_HTTPONLY` használatával érhetjük el.
- **SameSite**: A `SameSite` beállítás a cross-site request forgery (CSRF) támadások megelőzésére szolgál. A `SESSION_COOKIE_SAMESITE` beállítással meghatározható, hogy a cookie-k csak ugyanarról a domainről legyenek használhatók.

#### **Sebezhetőségek kezelése**

A rendszer megóvása érdekében elengedhetetlen a gyakori webes támadások, mint az SQL injection, XSS (Cross-Site Scripting) és CSRF (Cross-Site Request Forgery) elleni védekezés. A megfelelő biztonsági intézkedések alkalmazásával csökkenthető a támadási felület és megakadályozható a sérülékenységek kihasználása.

A Django beépített biztonsági funkciói segítenek a webalkalmazás védelmében, ideértve a CSRF, SQL injection és XSS támadások elleni védelmet, a session kezelését és a cookie biztonságot.

- **SQL Injection védelem**: A Django ORM automatikusan védi az alkalmazásokat az SQL injekció támadásoktól, mivel nem közvetlenül SQL lekérdezéseket írunk, hanem Python objektumokkal manipuláljuk az adatokat.

- https://docs.djangoproject.com/en/5.1/topics/security/
- https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/web_application_security
- https://cheatsheetseries.owasp.org/cheatsheets/Django_Security_Cheat_Sheet.html
- https://medium.com/django-unleashed/how-to-secure-django-applications-with-https-and-ssl-a-comprehensive-guide-in-2024-f56b4ce11810
- https://learndjango.com/tutorials/django-best-practices-security
- https://dev.to/mostafij/securing-your-django-application-best-practices-for-preventing-xss-csrf-and-more-27me

#### **Folyamatos monitorozás, hibakazelés és logolás**

A rendszer biztonságának fenntartása érdekében elengedhetetlen a folyamatos monitorozás, naplózás és hibaelhárítás. A logok segítségével a biztonsági események gyorsan észlelhetők és megfelelő válaszlépés alkalmazható.

- **Kivételkezelés**: A kezelése `try-except` blokkok segítségével történik. A megfelelő kivételkezelési technikák alkalmazásával elkerülhetők a nem kezelt hibák, és biztosítható, hogy a rendszer megfelelő visszajelzést adjon a felhasználónak és fejlesztőnek.
	- https://www.geeksforgeeks.org/exception-handing-in-django/
	- https://dev.to/ebereplenty/mastering-try-except-blocks-in-django-simplified-python-error-handling-3nj8
- **GUI hibák kezelése**: A felhasználói felületen a hibák kezelése és megjelenítése elengedhetetlen a jó felhasználói élményhez. A hibákat és figyelmeztetéseket vizuálisan is jelezni kell az alkalmazásban, például:
	- Form-validációs hibaüzenetek megjelenítése (pl. kötelező mezők).
	- Egyéni üzenetek a felhasználó számára (`Django messages` segítségével).
	- A `Django messages` használata a felhasználói interakciók során.
		- Üzenetek megjelenítése sikeres műveletek, hibák vagy figyelmeztetések esetén.
		- A rendszer visszajelzései, például: sikeres regisztráció, hibaüzenetek formázása és testreszabása.
		- https://docs.djangoproject.com/en/5.1/ref/contrib/messages/
		- https://dev.to/ahmed__elboshi/django-messages-framework-a-guide-to-displaying-messages-3m53
- **Logolás**: 
	- https://docs.djangoproject.com/en/5.1/howto/logging/
	- https://docs.djangoproject.com/en/5.1/topics/logging/
	- Hibák és rendszeres események logolása: A Django **logging rendszere** a Python **standard logging** moduljára épül, és lehetővé teszi az alkalmazás eseményeinek naplózását. Ezzel nyomon követhetők a hibák, figyelmeztetések és egyéb fontos információk a fejlesztés és üzemeltetés során. A Django naplózási rendszere négy fő komponensből áll: 
	1. **Loggerek (Loggers)** – Naplóüzenetek létrehozásáért felelnek.
	2. **Handlerek (Handlers)** – A logüzenetek célhelyére továbbítják az adatokat (pl. fájlba vagy konzolra).
	3. **Szűrők (Filters)** – Segítségükkel eldönthető, hogy egy adott üzenet továbbításra kerüljön-e.
	4. **Formázók (Formatters)** – Meghatározzák a naplóbejegyzések kinézetét.

---

## **Tesztelés és validáció**

A tesztelési és validálási folyamat célja, hogy biztosítsa az alkalmazás megbízhatóságát, funkcionalitását és biztonságát. A tesztelés során a különböző tesztelési típusok és eszközök alkalmazása kulcsfontosságú a kódminőség fenntartásában.

- https://docs.djangoproject.com/en/5.1/topics/testing/overview/
- https://docs.djangoproject.com/en/5.1/topics/testing/
- https://medium.com/@rahadianpanjipanji/unit-testing-in-django-95442b38b67b
- https://learndjango.com/tutorials/django-testing-tutorial

### Tesztelési típusok és eszközök

1. **Unit tesztek**:
    - Az alkalmazás legkisebb egységeinek tesztelése, mint például modellek, segédfunkciók, vagy backend logika.
    - A tesztelés segítségével biztosítható, hogy minden egyes kódrészlet megfelelően működjön a vártnak megfelelően.
    - A tesztelést a Python beépített **unittest** keretrendszere vagy a rugalmasabb **PyTest** használatával végezhetjük el. Az utóbbi könnyen integrálható Django projektekbe is.
    - Tesztek futtatása a backend és frontend logika tesztelésére, párhuzamosan az adatbázis műveletek izolálásával.
    - Hasznos források:
	    - https://rtt.koczka.com/unittest.html
        - [Django tesztelés áttekintés](https://docs.djangoproject.com/en/5.1/topics/testing/)
        - [PyTest hivatalos dokumentáció](https://docs.pytest.org/en/stable/)
        - https://www.geeksforgeeks.org/pytest-tutorial-testing-python-application-using-pytest/
		- https://en.wikipedia.org/wiki/Pytest
2. **End-to-End tesztelés (E2E)**:
    - Az E2E tesztelés a felhasználói folyamatok teljes körű tesztelésére szolgál. A cél a rendszer összes funkciójának, mint a regisztráció, bejelentkezés vagy projekt létrehozásának, tesztelése.
    - Ezt a tesztelést például a **Cypress** eszközzel végezhetjük el, amely kiváló a felhasználói interakciók és a böngésző alapú teszteléshez.
    - Hasznos források:
        - [Cypress hivatalos dokumentáció](https://docs.cypress.io/app/end-to-end-testing/writing-your-first-end-to-end-test)
        - [Cypress tesztelés alapjai](https://www.geeksforgeeks.org/introduction-to-cypress-testing-framework/)
        - https://www.geeksforgeeks.org/introduction-to-cypress-testing-framework/
		- https://docs.cypress.io/app/end-to-end-testing/writing-your-first-end-to-end-test
		- https://docs.cypress.io/app/get-started/why-cypress
		- https://www.cypress.io/
		- https://rtt.koczka.com/cypress.html#
3. ***Funkcionális tesztelés**:*
    - *A rendszer funkcionális elvárásainak és a felhasználói történetek validálása.*
    - *Biztosítja, hogy a rendszer az üzleti igényeknek megfelelően működjön.*
4. ***Biztonsági tesztek**:*
    - *Behatolásos tesztelés (penetration testing) és a rendszer sebezhetőségeinek feltérképezése.*
    - *Különböző támadások szimulálása, mint SQL injection vagy XSS támadások.*
    - *Az adatvédelmi és titkosítási megoldások tesztelése.*
5. ***Integrációs tesztek (Integration tests)**: A különböző rendszerelemek közötti interakciók tesztelése annak biztosítására, hogy a komponensek együttműködjenek.*

### Tesztelési folyamat

1. **TDD (Test-Driven Development)**:
    - A TDD egy fejlesztési megközelítés, amelyben a tesztelést mindig a kód fejlesztése előtt végezzük el. A tesztelési ciklus a **Red-Green-Refactor** módszert követi: először írunk egy hibás tesztet (Red), majd megírjuk a kódot, hogy a teszt sikeresen lefusson (Green), végül a kódot refaktoráljuk (Refactor).
    - A TDD előnyei: biztosítja a kód minőségét és gyorsabb hibafelismerést.
2. **Párhuzamos tesztelés**:
    - A különböző tesztelési típusok párhuzamos futtatása segíthet az alkalmazás hatékonyságának és megbízhatóságának biztosításában.
    - Az adatbázis műveletek és az alkalmazás logikájának tesztelését külön-külön végezhetjük, hogy minimalizáljuk az esetleges interferenciákat.

---

## **Fejlesztési- és felhasználói dokumentáció**

### **Rendszer felépítése**

A rendszer felépítése az alkalmazás struktúráját és az egyes komponensek közötti kapcsolódást írja le. 

A Django alapelve a modularitás és az újrahasznosíthatóság. Egy **projekt** az egész webalkalmazást jelenti, amely tartalmazza a beállításokat, konfigurációkat és az összes szükséges alkalmazást. Egy **alkalmazás** ezzel szemben egy kisebb, önálló modul a projekten belül, amely egy adott funkciót lát el (pl. felhasználói autentikáció, blog, webshop stb.).

https://medium.com/django-unleashed/django-project-structure-a-comprehensive-guide-4b2ddbf2b6b8

#### **A fő projektmappa (langmodels_project_management)**

A Django fő projektmappája magában foglalja az alkalmazás lényegét. Ez az a központi hely, ahonnan minden funkció kiindul, formálva a webalkalmazás egészét. Ebben a mappában több kulcsfontosságú fájl található, mindegyiknek megvan a maga jelentősége a fejlesztési folyamat irányításában:

- **manage.py**: Ez a kicsi, de hatékony szkript a különböző Django kezelőparancsok kapuja. Ezen keresztül indítható a fejlesztői szerver, hozhatók létre alkalmazások, futtathatók migrációk, és még sok más. A manage.py a karmesteri pálca, amely irányítja a projekt tevékenységeit.
- **langmodels_project_management/settings.py**: Ahogy a neve is sugallja, ebben a fájlban találhatók azok a beállítások, amelyek konfigurálják a Django projektet. A beállítások között szerepelnek adatbázis-konfigurációk, middleware listák, és itt határozhatjuk meg, hogyan működik az alkalmazás. Ez hasonló egy tervrajzhoz, amely meghatározza a projekt működésének struktúráját.
- **langmodels_project_management/urls.py**: Az URL-diszpatcher — amely a **urls.py** fájlban található — térképezi fel az URL-eket a nézetekhez. Ez a fájl határozza meg, melyik nézet jelenik meg, amikor egy adott URL-t elérnek. Olyan, mint egy térkép, amely navigálja a felhasználókat az alkalmazás oldalainak bonyolult rendszerein.
- **langmodels_project_management/wsgi.py**: A Web Server Gateway Interface (WSGI) rövidítése, a wsgi.py a belépési pont az alkalmazás számára, amikor azt egy produkciós szerveren futtatják. Ez a híd, amely összeköti az alkalmazást a webszerverrel, lehetővé téve, hogy kezelje a beérkező kéréseket.
- **langmodels_project_management/asgi.py**: Hasonlóan a wsgi.py fájlhoz, az asgi.py a belépési pont aszinkron webszerverek számára. Az Asynchronous Server Gateway Interface (ASGI) rövidítése, és segíti az aszinkron HTTP-kérések kezelését.
- **langmodels_project_management/**init**.py**: Ez a látszólag jelentéktelen fájl tartalmazza azt a varázslatot, amely egy mappát Python csomaggá alakít. Elengedhetetlen a modulok rendezéséhez és importálásához a projektben.
- - **static/**: Ebben a mappában tároljuk az alkalmazás statikus fájljait, például CSS, JavaScript, képek és egyéb fájlok, amelyek nem változnak a felhasználói interakció során. A `static/` mappa szerkezetét és tartalmát gondosan kell kezelni, hogy a webalkalmazás vizuális megjelenése és interaktivitása biztosítva legyen.
- **media/**: A felhasználók által feltöltött fájlok, mint például képek, dokumentumok, videók, itt kerülnek tárolásra. A `media/` mappa megfelelő kezelése szükséges ahhoz, hogy az alkalmazás adatokat fogadhasson, tárolhasson és megjeleníthessen.
- **templates/**: Itt találhatók a Django sablonfájlok (HTML). Az alkalmazás vizuális rétege és a felhasználói felület itt van definiálva. A `templates/` mappa tartalmazza a sablonokat, amelyeket a Django a nézetekhez renderel, biztosítva ezzel az oldal dinamikus generálását.
- **utils/**: A `utils/` mappa segédfunkciók és osztályok tárolására szolgál, amelyeket több alkalmazás vagy modul is használhat. Itt helyezkednek el azok a kódok, amelyek nem specifikusak egy alkalmazásra, de más részekben újrahasznosíthatók (például dátumformázás, adatellenőrzés, segédfüggvények).

```
langmodels_project_management/
├── manage.py
├── langmodels_project_management/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── static/  
├── media/  
├── templates/
├── utils/
```


#### **Alkalmazás mappa**

A Django világában az alkalmazások szervezése nemcsak a koncepcionális struktúrára épít, hanem az alkalmazásokat életre keltő fájlok elrendezésére is. Minden alkalmazás mappájában olyan fájlok találhatók, amelyek összességükben meghatározzák annak működését és funkcióit.

- **models.py**: Minden alkalmazás szíve a **models.py** fájl. Itt definiálod az adatstruktúrákat a Django ORM (Object-Relational Mapping) segítségével. Minden model osztály egy adatbázis-táblát képvisel. Ez a fájl képezi az alkalmazás adatkezelésének alapját.
- **views.py**: A **views.py** fájl tartalmazza azt a logikát, amely meghatározza, hogyan lép kapcsolatba az alkalmazás a felhasználói kérésekkel. A nézetek kezelik az adatfeldolgozást, a sablonok renderelését és a válaszadásokat. Ez a fájl alakítja át a felhasználói interakciókat kézzelfogható válaszokká.
- **tests.py**: A teszt-vezérelt fejlesztés ereje a **tests.py** fájlban rejlik. Itt írjuk meg az egységteszteket, hogy biztosítsuk az alkalmazás komponenseinek megfelelő működését. Ezek a tesztek növelik a kód megbízhatóságát és stabilitását.
- **admin.py**: Az **admin.py** fájl nemcsak az adminisztrátorok számára van, hanem azt is konfigurálja, hogyan jelennek meg az alkalmazás modeljei a Django admin felületén. Ez a fájl lehetővé teszi az adminisztrátorok számára, hogy könnyedén kezeljék az adatokat.
- **migrations**: Ez a mappa tartalmazza az alkalmazás modeljeiben történt összes változás tervét.
- **Egyéb fájlok**: További fájlok is megjelenhetnek az alkalmazás szükségletei alapján. Például a **forms.py** form osztályokat tartalmaz az adatbeviteli mezőkhöz, a **urls.py** az URL-eket társítja a nézetekhez, és az **apps.py** kezeli az alkalmazás-specifikus konfigurációkat.

```
├── app/
	├── migrations/  
    │   └── __init__.py  
    ├── __init__.py  
    ├── admin.py  
    ├── apps.py  
    ├── forms.py
    ├── models.py  
    ├── tests.py  
    ├── urls.py  
    └── views.py
```

#### **Könyvtárhierarchia:** 

https://medium.com/django-unleashed/django-project-structure-a-comprehensive-guide-4b2ddbf2b6b8

```
langmodels_project_management/  # A projekt gyökérkönyvtára
├── manage.py  
├── langmodels_project_management/  # Ez a belső könyvtár tartalmazza a projekt alapbeállításait és konfigurációit.
│   ├── __init__.py  
│   ├── asgi.py  
│   ├─ settings.py  
│   ├─ urls.py  
│   ├── wsgi.py  
├── users/  # Alkalmazás
├── project_management/  # Alkalmazás
├── ai_documentation/  # Alkalmazás
  ...  
├── static/  # Statisztikus fájlok (CSS, JavaScript, képek)
├── media/  # Felhasználók által feltöltött fájlok tárolása
├── templates/  # Django HTML sablonok
├── utils/ # Segédfunkciók és osztályok
```

#### ***Kód dokumentáció***

*A **kód dokumentálása** kulcsfontosságú a fejlesztési folyamatban, mivel segít megérteni a kód működését és döntéseit. A **docstringek** függvények, osztályok és modulok mellett elhelyezett szövegek, amelyek részletesen leírják a kód funkcióját, bemeneteit és kimeneteit. A **kommentek** rövid magyarázatok, amelyek a kód bonyolult részeit tisztázzák. A dokumentált kód könnyebben karbantartható, hibaelhárítható és fejleszthető, mivel más fejlesztők számára is érthetővé válik.*
- *https://www.python.org/dev/peps/pep-0257/*
- *https://docs.djangoproject.com/en/stable/internals/contributing/writing-documentation/*
- *https://www.sphinx-doc.org/*

#### **Routing kezelése:**  

A routing a `urls.py` fájlokban történik, ahol minden URL-hez hozzárendelésre kerül egy nézet (view). A rendszer támogatja a dinamikus URL-kezelést, amely lehetővé teszi a változókat tartalmazó URL-eket, valamint az URL-ek és a nézetek közötti megfelelő összefüggések kialakítását.
- https://www.geeksforgeeks.org/django-url-dispatcher-tutorial/
- https://docs.djangoproject.com/en/5.1/ref/urls/

**URL minták létrehozása**
A Django-ban az URL minták (URL patterns) a `urls.py` fájlban kerülnek definiálásra. Ezek segítségével rendelhetjük hozzá a megfelelő nézeteket (views) az egyes URL-ekhez, és meghatározhatjuk, hogy milyen URL-eket hogyan kezeljenek a rendszerben.
Az `urlpatterns` listában egy `path()` függvényt használunk, amelyben megadjuk az URL-t és a hozzá tartozó nézetet.

**Dinamikus URL-ek használata**
A dinamikus URL-ek lehetővé teszik a változókat tartalmazó URL-ek kezelését. Ez különösen hasznos, amikor az URL-ben szereplő értékeket szeretnénk átadni a nézeteknek.
A dinamikus URL-eket az URL mintában változók (pl. `<int:id>`) formájában adhatjuk meg. Az URL-ben szereplő változókat a nézet automatikusan átveszi argumentumként.

**URL-ek elnevezése**
Az URL-ek elnevezése segít a kód karbantartásában, mivel így nem kell kézzel megadni az URL-t mindenhol. Ehelyett a név alapján hivatkozhatunk rá, ami egyszerűsíti a változtatások kezelését is.
Az `path()` függvény `name` paraméterével elnevezhetjük az URL mintákat. Ezt később hivatkozhatjuk a `{% url %}` template tag-gel vagy a `reverse()` függvénnyel.

**Névterek használata**
A névterek (namespaces) segítségével lehet rendszerezni az URL mintákat, és elkerülni a névütközéseket, amikor több alkalmazást integrálunk egyetlen projektbe. A névterek lehetővé teszik, hogy egy adott alkalmazás URL-jeit egy specifikus névtér vagy előtag alá csoportosítsuk, így könnyebben kezelhetjük és megkülönböztethetjük az alkalmazás különböző részeit.

**Class-Based Views (CBV) alkalmazása**
A Class-Based Views (CBV) alkalmazása során az URL-eket a `as_view()` metódussal kell összekapcsolni a megfelelő osztályokkal. Ez lehetővé teszi, hogy az osztályokat nézetekként használjuk, és a `urls.py` fájlban ugyanúgy hozzárendelhetjük őket az URL-ekhez, mint a funkciókat.
A CBV-t az URL mintákban az `as_view()` metódus hívásával regisztráljuk, amely a CBV osztály egy példányát adja vissza, és a Django számára lehetővé teszi a megfelelő HTTP kérések kezelését.

#### **Kapcsolat az adatbázissal:**  

https://docs.djangoproject.com/en/5.1/ref/databases/
https://sqldocs.org/sqlite-database/django-sqlite/

Az adatbázis kapcsolatot az `settings.py` fájl tartalmazza, ahol beállíthatók az adatbázis típusai (pl. SQLite, PostgreSQL) és a hozzá szükséges paraméterek (felhasználó, jelszó, host, stb.). A rendszer az ORM (Object-Relational Mapping) segítségével kezeli az adatbázist, így a modell objektumokon keresztül történik az adatbázissal való kommunikáció.

A Django projektben az adatbázis kapcsolat beállításait az `settings.py` fájlban találjuk. Az SQLite adatbázis használatakor az adatbázis fájl elérési útját kell megadnunk. A környezeti változók segítségével dinamikusan beállíthatjuk az adatbázis paramétereit, például az adatbázis fájl elérési útját vagy a titkos kulcsokat.
- **SQLite beállítása az `settings.py` fájlban:** Az SQLite alapértelmezett adatbázis, amely nem igényel különösebb beállítást az adatbázis típusához, csupán egy fájl elérési utat kell megadni.
- **.env fájlban környezeti változók:** A `.env` fájl tartalmazza a különböző környezeti változókat, amelyek segítségével dinamikusan beállíthatók az adatbázis paraméterek. A Django az `os.getenv()` függvény segítségével tölti be a változókat.
- **ORM (Object-Relational Mapping):** Az ORM lehetővé teszi, hogy az adatbázissal való kommunikáció objektumokkal történjen, így a Python kódban definiált modellek (osztályok) automatikusan leképeződnek az adatbázis tábláira. A Django ORM segítségével könnyedén végrehajthatunk műveleteket az adatbázison anélkül, hogy közvetlen SQL-t írnánk.

#### **Kapcsolat az oldalak között:**  

https://docs.djangoproject.com/en/5.1/ref/urls/#including-other-urlconfs

A különböző oldalak közötti navigációt a `urls.py` fájlokban és a nézetekben (views) kezeljük. Az oldalak közötti kapcsolatokat az URL-ek és a sablonokban lévő linkek biztosítják. Az alkalmazás dinamikus, így a felhasználók könnyen navigálhatnak a rendszer különböző szakaszaiban.

A Django projektben több alkalmazás (app) is lehet, és minden alkalmazásnak saját `urls.py` fájlja van, amelyben az adott alkalmazás URL-jeit definiálhatjuk. Az összes alkalmazás URL-jeit azonban egy központi fájlban, a fő projekt `urls.py` fájljában kell összegyűjteni és összekapcsolni, hogy a rendszer képes legyen az összes URL-t helyesen kezelni.
- **Fő projekt `urls.py`:** A fő projektben található `urls.py` fájl felelős az összes alkalmazás URL-jeinek összekapcsolásáért. Ez tartalmazza azokat az URL-eket, amelyek az egyes alkalmazások URL-gyűjteményeit beágyazzák. Az alkalmazásokat az `include()` függvénnyel kell hozzáadni a projekt URL-struktúrájához.
- **Alkalmazás URL-jeinek kezelése (`urls.py`-ban):** Az egyes alkalmazásokban található `urls.py` fájlok felelősek a saját URL-jeik definiálásáért. Itt adjuk meg, hogy egy adott URL-hez melyik nézet (view) tartozik.
- **URL névkonvenciók és dinamikus hivatkozások:** A Django biztosítja, hogy az alkalmazások URL-jei ne ütközzenek, ha különböző névterekben dolgozunk. Mivel az URL-eket a `name` attribútumokkal láthatjuk el, ugyanazokat a neveket használhatjuk különböző alkalmazásokban is. Az URL-eket a sablonokban és a nézetekben az URL neveivel hivatkozhatjuk meg.
- **Az alkalmazások és a projekt közötti kapcsolat:** Az alkalmazások URL-jeinek központi kezelése lehetővé teszi, hogy a különböző alkalmazások URL-struktúráját egyszerűen bővítsük vagy módosítsuk anélkül, hogy az egész projektet újra kellene konfigurálnunk. Az `include()` függvény segítségével könnyen kezelhetjük az alkalmazások URL-jeit, és biztosíthatjuk, hogy azok helyesen működjenek a projekt részeként.

### **Telepítés**

#### 1. **Letöltés és futtatás DockerHub-ról**
- **Docker telepítése:** Töltsd le és telepítsd a Docker alkalmazást a [hivatalos weboldalról](https://www.docker.com/get-started).
- **Konténer letöltése:** `docker pull drntth/thesis-langmodels-project-management:latest`
- **Konténer elindítása:**`docker run -d -p 8000:8000 drntth/thesis-langmodels-project-management`
	- `-d`: A konténer háttérben történő futtatását biztosítja (detached mode).
	- `-p 8000:8000`: A konténer belső 8000-es portját a helyi gép 8000-es portjára irányítja, így a szolgáltatás elérhető lesz kívülről is.
- **Elérés a böngészőben:** Nyisd meg a `http://localhost:8000` címet.

#### 2. **Letöltés GitHubról és futtatás Docker segítségével**

- **Projekt klónozása:** `git clone https://github.com/Drntth/thesis-langmodels-project-management.git`
- **Konténerek indítása Docker Compose segítségével:** `docker-compose up --build`
    - `--build`: Újraépíti a konténereket a legfrissebb beállításokkal.
- **Adatbázis inicializálása:** `docker-compose exec web python manage.py migrate`
	- `exec web`: A `web` nevű konténeren belül futtat egy parancsot.
    - `python manage.py migrate`: Lefuttatja az adatbázis migrációkat, hogy a táblák létrejöjjenek.
- **Elérés a böngészőben:** Nyisd meg a `http://localhost:8000` címet.

#### 3. **Letöltés GitHubról és manuális futtatás**

- **Projekt klónozása:** `git clone https://github.com/Drntth/thesis-langmodels-project-management.git`
- **Virtuális környezet létrehozása és aktiválása:**
    ```
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
    ```
- **Függőségek telepítése:** `pip install -r requirements.txt`
- **Környezeti változók beállítása:** Töltsd ki a `.env` fájlt a megfelelő értékekkel.
- **Adatbázis inicializálása:** `python manage.py migrate`
- **Alkalmazás indítása:** `python manage.py runserver`
- **Elérés a böngészőben:** Nyisd meg a `http://127.0.0.1:8000` címet.

### **Használati útmutató**

#### Normál felhasználó 

A felhasználói dokumentáció részletes útmutatót tartalmaz a rendszer használatához. Ez az útmutató segíti a végfelhasználókat abban, hogy hogyan lépjenek be, hogyan hozzanak létre projekteket, hogyan kezeljék az adatokat, és hogyan generáljanak dokumentációkat. A következő témákat tartalmazza:

- **Bejelentkezés és regisztráció:**  
    Részletes leírás a felhasználók számára a regisztrációs és bejelentkezési folyamatokhoz.
- **Projekt létrehozása és kezelése:**  
    A felhasználók lépésről lépésre megtanulják, hogyan hozhatnak létre új projekteket, módosíthatják azokat, és hogyan generálhatnak projekt-specifikus dokumentációkat.
- **Dokumentációk előállítása:**  
    Hogyan használhatják az automatizált eszközöket a szükséges dokumentumok (pl. specifikációk, időtervek) előállításához.
- **Hibakezelés:**  
    A rendszer hibakezelési folyamatának ismertetése, hogy a felhasználók könnyen megértsék, hogyan kezelhetők a rendszer által felvetett hibák vagy problémák.
- **Támogatás:**  
    Elérhetőségek és gyakori kérdések (FAQ), amelyek segítenek a felhasználóknak a rendszer gyorsabb és hatékonyabb használatában.

#### Adminisztrátor

Az adminisztrátori dokumentáció részletes útmutatót tartalmaz a rendszer felügyeletéhez és konfigurálásához. Az adminisztrátoroknak lehetőségük van a felhasználók kezelésére, jogosultságok beállítására, valamint a rendszer működésének monitorozására és karbantartására. A következő témákat tartalmazza:

- **Felhasználók kezelése:**
    - Új felhasználók regisztrációjának engedélyezése vagy tiltása
    - Jogosultsági szintek beállítása (normál felhasználó, adminisztrátor)
    - Felhasználói fiókok módosítása vagy törlése
- **Rendszerbeállítások és konfiguráció:**
    - Alapvető rendszerparaméterek módosítása
    - Adatkezelési és biztonsági beállítások finomhangolása
- **Projekt- és adatkezelés:**
    - Felhasználók által létrehozott projektek és dokumentációk felügyelete
    - Adatok exportálása, archiválása és törlése
- **Hibakeresés és naplózás:**
    - Rendszernaplók megtekintése és elemzése
    - Gyakori problémák azonosítása és megoldása
    - Hibaüzenetek és értesítések kezelése
- **Biztonsági mentés és visszaállítás:**
    - Adatmentési eljárások ismertetése
    - Rendszer-visszaállítás lépései egy korábbi állapotra
- **Támogatás és karbantartás:**
    - Kapcsolattartás a technikai támogatással
    - Rendszerfrissítések és verziókezelés

---

## **Összegzés



---

## **Irodalomjegyzék**

