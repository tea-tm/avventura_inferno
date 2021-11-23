from fns import write, ask, make_choice, print_abandon
import time 
from colorama import Fore, Style, init
import art as a

anteinferno = a.text2art("ANTE - INFERNO",font='fire_font-s',chr_ignore=True)
c1 = a.text2art("I. LIMBO",font='fire_font-s',chr_ignore=True)
c2 = a.text2art("II. LUSSURIA",font='fire_font-s',chr_ignore=True)
c3 = a.text2art("III. GOLA",font='fire_font-s',chr_ignore=True)
c4 = a.text2art("IV. AVARIZIA",font='fire_font-s',chr_ignore=True)
c5 = a.text2art("V. IRA",font='fire_font-s',chr_ignore=True)
c6 = a.text2art("VI. ERESIA",font='fire_font-s',chr_ignore=True)
c7 = a.text2art("VII. VIOLENZA",font='fire_font-s',chr_ignore=True)
c8 = a.text2art("VIII. FRODE",font='fire_font-s',chr_ignore=True)
c9 = a.text2art("IX. TRADIMENTO",font='fire_font-s',chr_ignore=True)

# Introduction
def start_game(info):
    print('\n'*10)
    write("Il tuo nome e' Dante Alighieri.\n")
    write("I Guelfi Neri hanno invaso a Firenze.\n")
    write("Tu sei stato esiliato. \n")
    ask("Continui")
    return wander, info

def wander(info):
    x = make_choice(["Tornare a Firenze", "Inizia il tuo viaggio"])
    if (x == 1):
        write("I Guelfi Neri ti bruciano sul rogo.")
        ask("Ricominciare?")
        return start_game, info
    
    write('Commenziamo nel mezzo del cammin di nostra vita... \n')
    write('Sei in una selva oscura. Vedi un\'alta montagna in lontanaza.')
    x = make_choice(["Continui attraverso la selva", "Vai verso la montagna"])
    if (x == 2):
        info['mtn'] = True
        write("Cammini verso la montagna, ma il tuo corso e' bloccato da tre animali: un leopardo, un leone, e una lupa. \nNon e' possibile Continuire.")
        ask("Ritorni al selva")
    return start_journey, info

def start_journey(info):
    write('Vedi una forma humana nell\'oscurita\'. \nLa forma si avvicina...\nTi riconosci il poeta, Vergil. Lui e\' l\'altissimo poeta degli Romani.')
    y = make_choice(["Scappi", "Parli a Vergil"])
    if (y == 1):
        write("Ti perdi nel selva.")
        ask("Torni indietro")
        write("Vedi nuovamente lo spirito nel selva.")
        ask("Parli a Vergil")
    write("[Vergil] Sei perso?")
    y = make_choice(["Hai paura", "Stupirsi"])
    if (y==1):
        write("[Vergil] Non abbi paura! Sono qui per aiutarti.")
    if (y==2):
        write('Non puoi parlare. Ti chiedi si questo e\' un sogno...')
        write('[Dante] Tu sei lo mio maestro... Che cosa sta succedendo?')
        write("[Vergil] Sono qui per aiutarti.")
    if (info['mtn'] == True):
        write("[Vergil] Perche' sei sceso dalla montagna?")
        ask("Lo dici delle bestie")   
    write("[Vergil] Posso mostrarti la strada sulla montagna. E\' un viaggio lungo e pericoloso. Ma incima, troverai la citta' di Dio.")
    x = make_choice(["Vai con Vergil", "Rifiutare"])
    if (x == 2):
        write('[Vergil] Va bene. La decisione è tua. Ci vediamo... ')
        write('Continui attraverso la selva. Sei stanco, quindi cessi sotto un\'albero.\n')
        write('Mentre dormi, alcuni uomi di Firenze ti trovano. I Guelfi Neri hanno promesso un premio per catturarti.\n')
        write('I uomi ti portano a Firenze, dove sei ucciso.\n')
        ask("Ricominciare?")
        return()
    write('[Vergil] Va bene. Andiamo...')
    write('Mentre camminate, la selva diventa più scuro...')
    write('.'*5 + '\n' + '.'*10)
    print_abandon()
    write('Siete arrivati alle porte dell\'inferno.')
    x = make_choice(["Hai paura", "Hai coraggio"])
    if (x == 1):
        write('Non vuoi Continuire. Provi a tornare indietro, ma Vergil ti ferma.')
        write('[Vergil] Ascolta! Sono stato inviato a aiutarti Beatrice, la Vergine Maria, e Santa Lucia. Siamo in un viaggio divino. Non puoi fermarti adesso.')
        y = make_choice(["Hai coraggio", "Scappi"])
        if (y == 1):
            write("Tu pensi a Beatrice, e senti piu' coraggioso.")
            write("Tu segui Vergil fino all'Inferno.")
        elif (y == 2):
            write("Tu scappi tra gli alberi.")
            write("Continui a vagare per molti anni. Vedi molte parti d'Italia, ma non mai torni piu' a Firenze.")
            write("Scrivi alcune poesie, ma non sono popolari. La lingua della letteratura e' ancora il Latino.")
            write("Si muori di Malaria a Ravenna.")
            ask("Ricominciare?")
            return()
    elif (x == 2):
        write("Tu segui Vergil fino all'Inferno.")
    time.sleep(2)
    return anteinferno, info
    

def anteinferno(info):
    print(anteinferno)
    time.sleep(2)
    write('Mentre scendete, senti i lamenti dei morti.')
    ask("Chiedi a Vergil dove siete")
    write('[Vergil] Questo e\' il ante-inferno. Questi non hanno speranza di morte... Sono loro che non hanno interessato di niente o nessuno tranne se stessi durante la vita.')
    x = make_choice(["Fermati a osservare", "Continui"])
    if (x==1):
        write("Guardi gli spiriti nel Limbo. Vedi multi insetti, vespe, e vermi, che pungono gli dannati.")
    write("Continuite verso un gran fiume nero.")
    write("[Vergil] : Questo e\' il fiume Acheronte.")
    write("Un uomo anziano vi avvicina. Lui ha i capello lungo e bianco. Quando lui ti guarda, vedi che i suoi occhi sono rossi.")
    write('[Charon] Guai a voi, anime prave!')
    write('[Charon] Cosa vuoi, vivente? Io transporto solo i morti.')
    x = make_choice(["Gli offri un denaro", "Provi a nuotare", "Lasci che Vergil parlare"])
    if (x == 2):
        write('Che cosa stai facendo? Questo e\' un\'idea horribile. Perche\' vuoi nuotare qui? Questo viaggio e\' importante! No! Ritorna!')
        x = make_choice(["Gli offri un denaro", "Lasci che Vergil parlare"])
    if (x == 1):
        write('[Charon] Solo i morti possono comprare questo biglietto.')
    write('[Vergil] Siamo in un viaggio divino. Il destino ci richiede di Continuire')
    write('Charon vi permmette a bordo. Mentre navigate, la terra comincia a tremare. Vedi una luce vermiglia...')
    write('Sei svenuto.')
    time.sleep(2)
    return limbo, info
    

# LIMBO


def limbo(info):
    print(c1)
    time.sleep(2)
    write('Ti svegli.\nSei all\'altro sponde del fiume. Non senti più urla.')
    ask('Chiudi a Vergil dove siete')
    write('[Vergil] Siamo a Limbo. Gli spiriti virtuosi chi non sono stati battezzati abitano qui. Io sono uno di loro.')
    ask('Continui')
    write('Venite su un grande castello.')
    write('[Vergil] Le grandi persone che non sapevano Dio abitano qui.') 
    
    x = make_choice(['Guardi intorno', 'Continui'])
    
    if (x==1):
        write('Vedi multi persone che riconosci...')
        x = make_choice(['Parli con i filosofi' , 'Parli con gli eroi', 'Parli con gli studiosi'])
        if (x==1):
            write('Qui vedi Socrates, Plato, Diogenes…')
            write('Diogenes ha un pollo e sta disputando con Plato.')
        elif (x==2):
            write('Qui vedi Homer, Aeneas, Caesar…')
            write('[Caesar] Veni, vidi, vici!')
        elif (x==3):
            write('Qui vedi Euclid, Ptolemy, Galen, Avicenna…')
            write('[Euclid] |d(x,z) - d(y, z)|  <= d(x,y)')
    
    ask('Continui')
    write('Diventa scuro ancora...')

    return lust, info

# LUST


def lust(info):
    print(c2)

    write('Mentre camminate, rinvenite il mostro Minos. \nLui presiede i cancelli e decide le punizioni per i dannati.')
    
    ask('Avvicini a Minos')
    write('[Minos] Non sei un\’anima condannata. Vai fuori di qui!' )
    write('[Vergil] Lui è in un viaggio divino. Fateci entrare!')
    write('Minosti permette di passare.  \nEntrate una violenta tempesta. \n\nQui vedi più persone che riconosci: Dido, Cleopatra, Helen, Paris, Aeneas… ')
    
    x = make_choice(['Parli a gli spiriti', 'Continui'])
    if (x==1):
        	write('Chiami a due degli spiriti. Loro sono Francesca di Rimini e Paolo Malatesta.\n[Francesca] Nessun maggior dolore che ricordarsi del tempo felice nella miseria…')
    write('Gli spiriti che abitano qui hanno commesso peccati di passione. Loro piangono disperati…\n\nSei sopraffatto dal loro dolore, e ancora sei svenuto.')

    return gluttony, info
    
# GLUTTONY
def gluttony(info):
    print(c3)
    
    write('Svegli in un temporale. \nCerberus è davanti a te. Lui sbrana i corpi dei morti.')
    write('Lui ti guarda.')
    x = make_choice(['Dagli un biscotto', 'Lo eviti'])
    if (x==1):
        	write('Cerberus mangia il biscotto e ti permette di passare.')
    if (x==2):
        	write('Vergil lancia un pezzo di fango al cane.\nCerberus è distratto e ti permette di passare.')
    write('Un spirito ti avvincia.')
    
    c = make_choice('Parli con lui', 'Lo ignori e Continui')
    if(c==1):
      write('[Ciacco] I guelfi bianchi torneranno al potere... \n[Ciacco] Ricorda me…')
      info['ciacco'] = True
    write('Continuite attraverso la tempesta gelida.')
    return greed, info
    
# GREED
def greed(info):
    print(c4)
    write('Vedi il demone Plutus.\n')
    time.sleep(.5)
    write('[Plutus]  Pape Satàn, pape Satàn aleppe…')
    write('Qui vedi gli spiriti degli avidi. Combattono tra loro con gran sachhi di monete come armi. \nMulti papi e cardinali abitano qui.')
    ask('Continui')
    return wrath, info


def wrath(info):
  print(c5)
  write('Siete arrivato all fiume Styx. \nGli spiriti de l\'iracondo sono sepolti nella plaude, combattono tra loro. \nVedi un\'alta torre.')
  
  write('Vergil procede. Un gruppo di demoni lo fermano.\n\nTre furie appaiono. \nTi vedono.\n\n[FURY] Porta fuori la testa di Medusa!\n')
  
  x = make_choice(['Guardi', 'Permetti Vergil di bloccare la tua vista'])
  if (x==1):
  	write('Le furie volano fuora con la testa di Medusa. Ti senti irrigidirti…')
  	write('Perché lo hai fatto? Tutti sanno cosa succede ora...')
  	return wrath, info
  write('Vergil copri i sui ochhi.\nSenti le furie urlare...')
  write('Appare una luce.\nI demoni disperdono.\nUn angelo discende dall\'alto.')
  ask('Ti inchini all\'angelo.')
  write('Il cancello si apre. Avete arrivato nella città di Dis.')
  return heresy, info

def heresy(info):
    print(c6)
    write('Gli spiriti degli eretici stanno bruciando nelle loro tombe.')

    if (info["ciacco"] == True):
        write('Vedi il padre del tuo amico, Guido Cavalcanti.')
        x = make_choice(['Chiedi della profezia di Ciacco', 'Continui'])
        if (x==1):
            write('[Spirit] Vediamo solo il futuro, non sappiamo nulla delle presente…')

    write('Vedi una tomba.') 
    x = make_choice(['Lo leggi', 'Continui'])
    if (x==1):
        write('Si dice: Anastasio papa guardo, lo qual trasse Fotin de la via dritta.')
    ask('Continui')

    return violence, info

#VIOLENCE

def violence(info):
    print(c7)
    
    write('Tu scendi. Vedi il Minotauro davanti a te…')
    write('[Vergil] Non è Teseo! Lasciamoci passare!')
    ask('Eviti il minotauro')
    write('Vedi laghi di sangue bollente…\n[Vergil] Questi sono gli spiriti che erano violenti mentre vivevano.')
    ask('Continui')
    write('Entri in un bosco... \n[Vergil] Questi sono gli spiriti che si sono suicidati. Hanno rifiutato la vita e i loro corpi per sempre... \n')
    ask('Continui')
    write('Entri in un deserto dove piove fuoco.')
    write('[Vergil] Questi sono gli spiriti che erano violenti contro natura.')
    write('Vedi tre figure. Riconosci i Fiorentini: Iacopo Rusticucci, Guido Guerra e Tegghiaio Aldobrandi. \nSei triste di vederli qui.')
    write('Ad un tratto, un grande mostro emerge dalla scogliera dietro di te. Ha un viso umano, ma il corpo di un grande rettile.')
    write('[Vergil] Questo è Gerione. Ci porterà giù per la scogliera.')
    ask('Continui')
    return fraud, info

#FRAUD
    
def fraud(info):
    print(c8)
    write('Sotto le scogliere, vedi dieci grande fosse nella terra.\n\n[Vergil] Questi sono gli spiriti chi hanno commesso il dolo.')
    x = make_choice(['Guardati intorno','Continui'])
    if(x==1):
        write('Guardi gli abitanti delle fosse. Vedi Ulysses, che ha usato il cavallo di Troia per conquistare Troia. Vedi multi politici e stregoni.') 
    ask('Un spirito ti avvincia.')
    write( 'Lo riconosci come Guido de Montefera.')
    ask('[Guido] Non c\'è perdono senza penitenza…')
    ask('Avvincete il centro del burrone.')
    write('I giganti stanno dentro il burrone. Le loro braccia sono incatenate, e le loro gamba bloccata nel fango.')
    x = make_choice(['Fermi a ascoltare','Continui'])
    if (x == 1):
        write('Senti uno strillo: \nRaphèl mai amècche zabì almi...')
    write('Uno degli giganti è libero.')
    ask('[Vergil] Questo è Antaeus.')
    write('Antaeus stende il suo mano.')
    ask('Sali su il mano')
    write('Vi abassa nella fossa finale.')
    return treachery, info

#TREACHERY

def treachery(info):
    print(c9)
    ask('Sei su un grande un lago ghiacciato.')
    write('[Vergil] Questi spiriti hanno respinto l\'amore di Dio. I loro cuori erano freddi, e hanno tradito chi si fida a loro. Adesso sono congelati.')

    x = make_choice(['Continui', 'Guardati intorno'])

    if (x == 2):
        write('I corpi del peccatori sono congelato nel ghiaccio fino al collo. Chinare il capo contra il vento.')

    write('Continuite attraverso il freddo. I corpi sono piu sotto il ghiaccio. Loro non possono piangere. Tutti e silenzioso.')

    write('[Vergil] Vexilla regis prodeunt inferni…')

    ask('Continui')

    write('Siete nel centro del Inferno. Davanti a tu, un gran monstro è imprigionato nel ghiaccio. In front of you is a great monster trapped in the ice.')
    
    x = make_choice(['Sei terrorizzato','Osservi'])
    if (x == 1):
        write('Lucifer batte le sue sei ali nere. Il vento quasi ti butta a terra. Tu lo fissi, terrorizzato, mentre lui mastica un corpo in bocca del ognuno dei suoi tre teste.')

    elif (x == 2):
        write('Il diavolo ha tre teste. In ogni bocca, lui mastica un corpo. Ha sei ali come pipistrello: sono la fonte del vento.')

    write('I corpi sono grande traditori: Marcus Junius Brutus, Gaius Cassius Longinus, e al centro, Judas Iscariot.')

    write('[Vergil] Questo è la nostra fuga…')

    x = make_choice(['Sei confuso', 'Seguilo'])
    if (x == 1):
        write('[Vergil] Seguimi. L\'uscita è avanti.')

    write('Segui a Vergil. Lui avvincia a Lucifer e afferra il suo pelliccia. Lui inizia a scalare il corpo del mostro, e attraverso un buoco nella roccia.')

    write('Scalate per molte ore...\n You climb for hours…\Ad un tratto, Vergil cambia direzione.')

    ask('Chiedi perchè')

    write('[Vergil] Abbiamo passato attraverso il centro della Terra.')

    write('Continui')

    return end, info
    
def end(info):
    write('Uscite dalla Terra su una grande montagna. \nÈ presto mattina.') 
    write('[Vergil] Abbiamo arrivato alla montagna del Purgatorio. La prima parte del nostro viaggo è completo.')
    write('Tu guardi il cielo e vedi le stelle...')

    time.sleep(3)
    print_stars()
    time.sleep(3)
    return creds, info
    
def print_stars():
    write('★ ° . .　　　　.　 °☆ 　. * ● ¸ .　　　★　° :.　 . • ○ ° ★　 .　 *　.　　　　　. 　 ° 　. ● .　　　　°  °☆ 　¸. ● .　　★　　★ °  ☆ ¸. ¸ 　★　 :.　 . • ○ ° ★　 .　 *　.　.　　¸ .　　 ° 　¸. * ● ¸ .　　　　°  ° 　¸. ● ¸ .　　★　° :.　 . • ° 　 .　 *　:.　.　¸ . ● ¸ 　　　★　　★ °★ . 　　　　.　 °☆ 　. ● ¸ .　　　★　° .　 • ○ ° ★　 .　 　　　　　　*　.　 ° 　¸. * ● ¸ 　　　　°  °☆ 　. * ¸.　　　★　★ ° . .　　　　.　 °☆ 　. * ● ¸ .　　　★　° :.　 . • ○ ° ★　 .　 *　.　　　　　. 　 ° 　. ● .　　　　°  °☆ 　¸. ● .　　★　　★ °  ☆ ¸. ¸ 　★　 :.　 . • ○ ° ★　 .　 *　.　.　　¸ .　　 ° 　¸. * ● ¸ .　　　')
    
def creds(info):
    print('Fatto da Dorotea Macrì in 2021\nInspirato all\'Inferno di Dante')
    info = {'mtn': False, 'ciacco': False}
    ask('Per Ricominciare, premere \'Enter\'')
    return start_game, info