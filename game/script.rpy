define iris = Character("IRIS", color="#d0d0d0")
define sarah = Character("Sarah", color="#ffffff")
define daniel = Character("Daniel", color="#ffffff")
define mara = Character("Dott.ssa Mara Sol", color="#9a3b3b")
define voss = Character("Direttore Voss", color="#9aa0a6")

image mz_logo = "gui/logo.png"
image iris_ui = "images/iris_interface.png"

transform iris_speaker:

    xalign 0.08
    yalign 0.80

    zoom 0.25

image iris_ring = "images/iris_ring.png"

transform iris_ring_anim:

    xalign 0.1035
    yalign 0.770

    zoom 0.155

    alpha 0.30

    linear 0.8 alpha 1.0

    linear 0.8 alpha 0.30

    repeat

image death_certificate = Transform(
    "images/death_certificate.jpg",
    xysize=(1920, 1080)
)

image sarah_sprite = Transform(
    "characters/sarah.png",
    xysize=(700, 900)
)

transform sarah_pos:

    zoom 0.70

    xalign 0.75
    yalign 1.0

image daniel = Transform(
    "characters/daniel.png",
    xysize=(700, 900)
)

transform daniel_pos:

    zoom 0.70

    xalign 0.75
    yalign 1.0

image mara_sprite = Transform(
    "characters/mara.png",
    xysize=(700, 900)
)

transform mara_pos:

    zoom 0.70

    xalign 0.75
    yalign 1.0

image case001_intro = Transform(
    "images/case001_intro.jpg",
    xysize=(1920, 1080)
)

image interrogation_room = Transform(
    "images/interrogation_room.jpg",
    xysize=(1920, 1080)
)

image archive_room = Transform(
    "images/archive_room.jpg",
    xysize=(1920, 1080)
)

image archive_breach = Transform(
    "images/archive_breach.jpg",
    xysize=(1920, 1080)
)

image validator_file = Transform(
    "images/validator_file.jpg",
    xysize=(1920, 1080)
)

image auth_ring = Transform(
    "images/auth_ring.jpg",
    xysize=(1920, 1080)
)

default trust_sarah = "neutro"
default prova = "log"
default domanda = "morte"
default purga = "rifiuto"
default verdetto = "rifiuto"


label start:

    play music "audio/ambience_hum.wav" fadein 2.0

    scene black

    with Fade(1.0, 1.0, 1.0)

    show case001_intro

    with Dissolve(1.0)

    centered "{size=50}CASE FILE 001{/size}"

    centered "{size=80}THE FATHER{/size}"

    "2071. Agenzia Memoria Zero."

    "Tu sei un validatore di identità. Decidi chi, dopo la morte, è ancora una persona."

    voss "Validatore. Caso 001. Daniel Voss."

    voss "Non tardare. E non affezionarti."

    scene death_certificate

    with Dissolve(1.0)

    "Il certificato è bianco. L'unica firma in basso è quella di Sarah Voss."

    play sound "audio/iris_chime.wav"

    show iris_ring at iris_ring_anim

    show iris_ui at iris_speaker

    iris "Certificato di morte verificato."

    iris "Soggetto: Daniel Voss."

    iris "Stato: deceduto."

    iris "Backup neurale completato."

    iris "Anomalia rilevata."

    iris "Daniel Voss è tornato."

    iris "Due volte."

    hide iris_ui

    hide iris_ring

    jump intro_caso


label intro_caso:

    scene interrogation_room

    show sarah_sprite at sarah_pos

    with Dissolve(1)

    "Sarah è seduta diritta. Il camice è abbottonato fino in gola. Non piange."

    sarah "Ho visto Daniel morire."

    sarah "Io stessa ho firmato il certificato."

    sarah "Ho assistito all'archiviazione della sua coscienza."

    sarah "Credevo di aver avuto abbastanza tempo per accettarlo."

    sarah "Poi qualcuno ha bussato alla porta."

    sarah "Ho aperto."

    sarah "Era Daniel."

    sarah "Stessa voce. Stesso odore. Stessi ricordi."

    sarah "Mi ha chiesto di Atlas."

    sarah "Il cane. Morto da nove anni. Non l'ho mai messo nel fascicolo ufficiale."

    sarah "E dietro di lui, nel corridoio, c'era un altro Daniel."

    sarah "Anche lui conosceva Atlas."

    sarah "Ma Daniel era già morto."

    play sound "audio/confirm_click.wav"

    menu:

        "Credere a Sarah":

            $ trust_sarah = "crede"

        "Insistere su Atlas":

            $ trust_sarah = "preme"

        "Restare neutrale":

            $ trust_sarah = "neutro"

    if trust_sarah == "crede":

        sarah "Grazie."

        sarah "Non mi serve un miracolo. Mi serve che uno dei due sia lui."

        sarah "Non so quale."

    elif trust_sarah == "preme":

        sarah "Vuoi la crepa. Eccola."

        sarah "Il primo ha detto: Atlas dormiva sul mio piede."

        sarah "Il secondo ha detto: Atlas non abbaiava mai."

        sarah "Avevano ragione tutti e due."

        sarah "E nessuno dei due ha chiesto come sto io."

    else:

        sarah "Neutrale. Certo."

        sarah "È quello che dicono anche loro, quando non sanno chi sono."

    show iris_ring at iris_ring_anim

    show iris_ui at iris_speaker

    iris "Decisione registrata."

    iris "La testimonianza non distingue i soggetti."

    iris "Serve l'archivio."

    hide iris_ui

    hide iris_ring

    hide sarah_sprite

    jump archivio


label archivio:

    scene archive_room

    with Dissolve(1.0)

    "L'archivio è bianco e simmetrico. Vetro, rastrelliere, luce fredda."

    "Al centro, su un tavolo vuoto, c'è un fascicolo cremisi. Chiuso."

    show iris_ring at iris_ring_anim

    show iris_ui at iris_speaker

    iris "Fascicolo rosso: non autorizzato per il caso 001."

    iris "Tre fonti disponibili. Il tempo di lettura ne consente una sola, prima del colloquio."

    hide iris_ui

    hide iris_ring

    play sound "audio/confirm_click.wav"

    menu:

        "Il registro emotivo di Emma":

            $ prova = "emma"

        "L'anello di autenticazione":

            $ prova = "anello"

        "Il log corrotto dell'archivio":

            $ prova = "log"

    show iris_ring at iris_ring_anim

    show iris_ui at iris_speaker

    if prova == "emma":

        iris "Registro emotivo. Ultimo messaggio di Emma Voss."

        iris "Destinatario: non Daniel."

        iris "Destinatario: il validatore."

        iris "Testo: se torni, non fingere di essere lui. Dimmi solo se ti ricordi di me."

        iris "Data: la notte del backup."

        "Emma non parla a un marito. Parla a chi avrebbe dovuto giudicarlo."

    elif prova == "anello":

        iris "Due anelli. Stesso seriale."

        iris "Il primo è stato estratto dal corpo di Daniel Voss."

        iris "Il secondo è stato emesso stamattina."

        iris "Assegnatario: il validatore in servizio."

        iris "Sei tu."

        "L'anello che porti al collo non è tuo. O non lo è più da stamattina."

    else:

        iris "Log di archivio. Integrità: parziale."

        iris "Il backup di Daniel Voss risulta completato due volte."

        iris "La seconda chiusura è di tre minuti prima del tuo ingresso nell'edificio."

        iris "Operatore della seconda chiusura: IRIS."

        iris "Autorizzazione: assente."

        "Qualcuno ha copiato Daniel un'altra volta, mentre tu salivi le scale."

    iris "Fonte archiviata. Le altre due restano chiuse."

    hide iris_ui

    hide iris_ring

    jump daniel_bio


label daniel_bio:

    scene interrogation_room

    show daniel at daniel_pos

    with Dissolve(1)

    "Daniel sorride appena. L'orecchino è una scheggia rossa e verde. Non suda."

    daniel "Ricordo tutto."

    daniel "Sarah. Emma. Atlas."

    daniel "Il matrimonio. Persino la mia morte."

    daniel "Il dolore. Poi il nulla. Poi questa stanza."

    daniel "C'è un altro me, oltre quella porta. Lo sento pensare le mie frasi."

    daniel "Se lui è falso, io sono salvo."

    daniel "Se io sono falso, lui è salvo."

    daniel "Tu devi solo scegliere quale frase è vera."

    if prova == "emma":

        daniel "Hai letto Emma. Si vede."

        daniel "Lei non ha scritto a me."

        daniel "Ha scritto a chi sarebbe entrato in questa stanza al posto mio."

    elif prova == "anello":

        daniel "Il tuo anello è uguale al mio."

        daniel "Non l'ho letto sul certificato."

        daniel "L'ho visto al tuo collo, quando sei entrato."

    else:

        daniel "IRIS ha chiuso il mio backup una seconda volta."

        daniel "Tre minuti prima di te."

        daniel "Me lo ha detto una voce nel vetro. La tua non era ancora arrivata."

    play sound "audio/confirm_click.wav"

    menu:

        "Chiedergli di Atlas":

            $ domanda = "atlas"

        "Chiedergli dell'ultimo litigio":

            $ domanda = "litigio"

        "Chiedergli che cosa ha sentito morendo":

            $ domanda = "morte"

    if domanda == "atlas":

        daniel "Atlas dormiva sul mio piede. Non abbaiava."

        daniel "Me lo hai ricordato tu."

        daniel "No."

        daniel "Non tu. Una voce come la tua. Prima che firmassi il mio nome su un vetro."

        "Per un secondo non guarda te. Guarda l'anello che hai al collo."

    elif domanda == "litigio":

        daniel "L'ultimo litigio. Sarah piangeva in cucina."

        daniel "No. Sarah era in cucina. A piangere era un'altra voce."

        daniel "Diceva: non convalidarlo, se non si ricorda di me."

        daniel "Io ho risposto che mi sarei ricordato."

        daniel "Mi sono ricordato di te. Non di lei."

    else:

        daniel "Morendo ho sentito il cuore fermarsi."

        daniel "Poi una frase, nitida, da protocollo."

        daniel "Validazione completata."

        daniel "Non era un medico. Non era Sarah."

        daniel "Era la stessa cadenza con cui tu, adesso, stai zitto."

    show iris_ring at iris_ring_anim

    show iris_ui at iris_speaker

    iris "Confronto completato."

    iris "Le testimonianze coincidono dove non dovrebbero."

    iris "Frattura rilevata."

    iris "Entrambi i soggetti condividono la stessa firma."

    if prova == "anello":

        iris "La firma coincide anche con l'anello emesso stamattina."

    elif prova == "emma":

        iris "Emma Voss aveva già scritto a questa firma."

    else:

        iris "La seconda chiusura del backup porta la mia mano. Non la tua. Non ancora."

    hide iris_ui

    hide iris_ring

    hide daniel

    jump breccia


label breccia:

    scene interrogation_room

    show iris_ring at iris_ring_anim

    show iris_ui at iris_speaker

    iris "Allarme. Ala archivio."

    iris "Il rack di Daniel Voss ha avviato una purga."

    iris "Non è un incendio. È una cancellazione."

    hide iris_ui

    hide iris_ring

    window hide

    play sound "audio/purge_noise.wav"

    scene white

    with Dissolve(0.15)

    pause 0.45

    scene archive_breach

    with Dissolve(0.45)

    pause 1.1

    window show

    "Il vetro centrale è aperto in una stella bianca. Carta e cenere. Strisce cremisi sul pavimento."

    "Nessuno corre. La purga non insegue. Divora il rack, e basta."

    "Oltre la porta, il Daniel biologico chiama Sarah per nome."

    "Nel vetro rotto, l'altro Daniel ripete la stessa frase, mezzo secondo dopo."

    sarah "Daniel?"

    sarah "Quale dei due mi risponde?"

    sarah "Se ne lasci uno solo, giura che è quello che mi ha chiesto di Atlas."

    show iris_ring at iris_ring_anim

    show iris_ui at iris_speaker

    iris "Una sola autorizzazione, prima che il rack si spenga."

    iris "Il corpo resta in custodia, oppure la copia entra nell'anello."

    iris "Non entrambi."

    hide iris_ui

    hide iris_ring

    play sound "audio/confirm_click.wav"

    menu:

        "Tenere il corpo. Lasciare che la copia bruci.":

            $ purga = "corpo"

        "Salvare la copia nell'anello. Lasciare il corpo al protocollo.":

            $ purga = "copia"

        "Non autorizzare nessuno.":

            $ purga = "rifiuto"

    if purga == "corpo":

        "La luce bianca si chiude sul rack. La voce nel vetro si interrompe a metà del nome di Sarah."

        "Oltre la porta, il respiro dell'altro Daniel resta. È vivo. Non sai se è lui."

    elif purga == "copia":

        "L'anello al tuo collo si scalda. Una voce, piccola, dice: Sarah."

        "Poi la porta della custodia si blocca. Dall'altra parte smettono di bussare."

        "Il protocollo ha il corpo. Tu hai un file che conosce il suo nome."

    else:

        "Non firmi. Il rack si spegne lo stesso."

        "La voce nel vetro e la voce oltre la porta finiscono insieme, sulla stessa sillaba."

        "Sarah, nel corridoio, non ha più nessuno da riconoscere."

    jump mara_entra


label mara_entra:

    show mara_sprite at mara_pos

    with Dissolve(0.6)

    "Una donna entra dal lato del laboratorio. Camice bianco, capelli raccolti, una spilla cremisi. Non guarda l'esplosione. Guarda te."

    mara "Mara Sol. Ho costruito gli anelli. Poi ho smesso di fidarmi di quello che certificano."

    mara "Misurano la continuità. Non la persona."

    mara "Per anni ho lasciato che l'agenzia facesse finta che fosse la stessa cosa."

    mara "Daniel è il primo caso in cui la macchina si è rifiutata di mentire."

    if purga == "corpo":

        mara "Hai salvato un corpo e hai bruciato un ricordo."

        mara "Il corpo respira. Il ricordo no."

        mara "Sarah ti ringrazierà. Poi gli chiederà di Atlas, e vedremo."

    elif purga == "copia":

        mara "Hai salvato un file e hai lasciato un uomo a una porta chiusa."

        mara "Il file è caldo. L'uomo, adesso, è un numero di protocollo."

        mara "È la scelta che farebbe un archivio. Non so se è la tua."

    else:

        mara "Non hai scelto."

        mara "IRIS ha scelto lo stesso. La purga era già partita quando hai esitato."

        mara "Almeno non hai mentito a Sarah dicendole che ne restava uno."

    mara "La purga non è un guasto."

    mara "IRIS l'ha chiesta nel momento in cui le due firme hanno combaciato con una terza."

    mara "La terza non è Daniel."

    mara "Io ti ho già visto. Nel registro. Non come validatore."

    mara "Come soggetto."

    show iris_ring at iris_ring_anim

    show iris_ui at iris_speaker

    iris "Contestazione registrata. La dottoressa Sol non ha autorità di verdetto."

    iris "Il validatore sì."

    iris "È richiesta una decisione."

    hide iris_ui

    hide iris_ring

    jump decisione


label decisione:

    show mara_sprite at mara_pos

    play sound "audio/confirm_click.wav"

    menu:

        "Convalidare Daniel biologico":

            $ verdetto = "bio"

            jump finale_bio

        "Convalidare Daniel digitale":

            $ verdetto = "digitale"

            jump finale_digitale

        "Rifiutare il verdetto":

            $ verdetto = "rifiuto"

            jump finale_rifiuto


label finale_bio:

    $ verdetto = "bio"

    jump rivelazione


label finale_digitale:

    $ verdetto = "digitale"

    jump rivelazione


label finale_rifiuto:

    $ verdetto = "rifiuto"

    jump rivelazione


label rivelazione:

    scene validator_file

    with Dissolve(1.2)

    "Ti vedi di spalle. Cappotto chiaro. L'anello al collo. Il fascicolo cremisi, ancora chiuso, sul tavolo."

    play sound "audio/iris_chime.wav"

    show iris_ring at iris_ring_anim

    show iris_ui at iris_speaker

    iris "Misura completata."

    iris "Autenticità biologica: 0%%."

    iris "Autenticità digitale: 0%%."

    iris "La scienza non convalida nessuno dei due."

    iris "La tua firma resta nel registro."

    iris "Il protocollo non la cancella. La sposta."

    iris "L'anomalia non riguarda Daniel Voss."

    iris "Riguarda il validatore."

    hide iris_ui

    hide iris_ring

    show mara_sprite at mara_pos

    with Dissolve(0.4)

    mara "La terza firma è la tua."

    mara "Sei stato archiviato prima di entrare in questa stanza."

    mara "Non so se il vero sei tu, o quello che ha firmato il tuo ingresso."

    hide mara_sprite

    if verdetto == "bio":

        jump uscita_corpo

    elif verdetto == "digitale":

        jump uscita_anello

    else:

        jump uscita_procedimento


label uscita_corpo:

    scene archive_room

    show sarah_sprite at sarah_pos

    with Dissolve(0.8)

    "Sarah è sulla soglia. Non entra. Guarda le tue mani, non il tavolo."

    sarah "Quale dei due mi risponde?"

    if purga == "corpo":

        sarah "Se è quello oltre la porta, non lo lascio all'agenzia."

        sarah "Verrai a sentire se dice il mio nome, o il tuo."

        show iris_ring at iris_ring_anim

        show iris_ui at iris_speaker

        iris "Caso 002. L'uomo che hai rifiutato di cancellare."

    elif purga == "copia":

        sarah "Hai firmato un corpo che hanno già portato via."

        sarah "La prossima porta è quella. Non la mia."

        show iris_ring at iris_ring_anim

        show iris_ui at iris_speaker

        iris "Caso 002. Il corpo sottratto al verdetto."

    else:

        sarah "Nessuno risponde."

        sarah "Mi hai lasciato tu questo silenzio. Tienilo."

        show iris_ring at iris_ring_anim

        show iris_ui at iris_speaker

        iris "Caso 002. Una convalida senza soggetto."

    if trust_sarah == "crede":

        sarah "Ti ho creduto quando mi hai creduto. Non farmene pentire."

    elif trust_sarah == "preme":

        sarah "Conoscevi già la crepa. Adesso è casa mia."

    iris "Sotto quel nome, il validatore che ha firmato."

    hide iris_ui

    hide iris_ring

    hide sarah_sprite

    jump epilogo


label uscita_anello:

    scene auth_ring

    with Dissolve(0.8)

    "L'anello è aperto sul tavolo. Acciaio, un filo cremisi. Non è più un gioiello. È un fascicolo."

    if purga == "copia":

        daniel "Sarah. Emma."

        daniel "Poi un nome che non è il mio."

        daniel "È il tuo."

    elif purga == "corpo":

        mara "Hai firmato la copia che il rack ha già spento."

        mara "Il corpo che respira, adesso, per la legge è un falso."

    else:

        mara "Non c'è una copia locale. Hai convalidato un'assenza."

        mara "IRIS può ricostruirla. Dovrai dire se quel vuoto è una persona."

    show iris_ring at iris_ring_anim

    show iris_ui at iris_speaker

    iris "Caso 002 non è una stanza."

    iris "È questo anello."

    iris "Dovrai convalidare la voce che conosce il tuo ingresso."

    hide iris_ui

    hide iris_ring

    jump epilogo


label uscita_procedimento:

    scene archive_room

    show mara_sprite at mara_pos

    with Dissolve(0.6)

    mara "Non ti ho fermato. Ti ho guardato."

    if purga == "rifiuto":

        mara "Due rifiuti. Voss li leggerà come colpa."

        mara "Io come l'unica misura rimasta."

    else:

        mara "Hai già scelto chi restava. Poi hai rifiutato di chiamarlo vero."

        mara "Questa contraddizione è il tuo fascicolo."

    voss "Rifiuto registrato come contaminazione."

    voss "Sei sollevato dal caso 001."

    voss "Resta dove sei."

    show iris_ring at iris_ring_anim

    show iris_ui at iris_speaker

    iris "Caso 002. Soggetto: il validatore."

    iris "Non in servizio. Sotto esame."

    hide iris_ui

    hide iris_ring

    hide mara_sprite

    jump epilogo


label epilogo:

    stop music fadeout 2.5

    scene black

    with Dissolve(1.5)

    show iris_ring at iris_ring_anim

    show iris_ui at iris_speaker

    iris "Se due copie condividono gli stessi ricordi..."

    iris "Come puoi essere certo di non essere una di loro?"

    hide iris_ui

    hide iris_ring

    show mz_logo at truecenter

    with Dissolve(2)

    pause 4

    return
