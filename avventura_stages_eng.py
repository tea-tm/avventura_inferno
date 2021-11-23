from fns_eng import *
import time

def start_game(info):
    print('\n'*10)
    write('Your name is Dante Alighieri.\n')
    write('The Black Guelfs have invaded Florence.')
    write('You have been exiled. \n')
    ask('Continue')
    return wander, info


def wander(info):
    x = make_choice(['Return to Florence', 'Start your journey'])
    if (x == 1):
        write('The Black Guelfs burn you at the stake.')
        ask('Restart?')
        return start_game, info
    else:
      write('We begin in the middle of the journey of our lives... \n')
      write('You are in a dark forest. You see a great mountain in the distance.')
      y = make_choice(['Continue through the woods',
                      'Go towards the mountain'])
      if (y == 2):
        write('You walk up the mountain, but your path is blocked by three beasts: a leopard, a lion, and a wolf. \nIt is not possible to continue.')
        info['mtn'] = True
        ask('Return to the woods')
      return start_journey, info

# VERGIL

def start_journey(info):
    write('You see a human shape in the darkness. \nThe figure approaches you...\nYou recognize the poet, Vergil. \nHe was the greatest poet of the Romans.')
    y = make_choice(['Run away', 'Speak to Vergil'])
    if (y == 1):
        write('You get lost in the woods.')
        ask('Turn back')
        write('You see the spirit in the woods again.')
        ask('Talk to Vergil')
    write('[Vergil] Are you lost?')
    y = make_choice(['Be afraid', 'Be starstruck'])
    if (y == 1):
        write('[Vergil] Don\'t be scared! I\'m here to help you.')
    if (y == 2):
        write('You can\'t speak. You wonder if this is a dream...')
        write('[Dante] You are my greatest teacher... What is happening?')
        write('[Vergil] I\'m here to help you.')
    if (info['mtn'] == True):
        write('[Vergil] Why did you come back down from the mountain?')
        ask('Tell him about the beasts')
    write('[Vergil] I can show you the way up the mountain. It is a long and dangerous journey. But at the top, you will find the Kingdom of God...')
    x = make_choice(['Go with Vergil', 'Refuse'])
    if (x == 2):
        write('[Vergil] It is fine. The choice is yours. Goodbye... ')
        write('You continue through the woods. You are tired, so you stop to rest under a tree.\n')
        write('While you sleep, some men from Florence find you. The Black Guelfs have put a bounty on your capture.\n')
        write('The men bring you to Florence, where you are killed.\n')
        ask('Restart?')
        return start_game, info
    write('[Vergil] Good. Let\'s go...')
    write('As you walk, the forest gets darker...')
    write('.'*5 + '\n' + '.'*10)
    write('ABANDON ALL HOPE, YOU WHO ENTER HERE...')
    write('You have reached the gates to the Inferno.')
    x = make_choice(['Be afraid', 'Have courage'])
    if (x == 1):
        write('You do not want to go on. You try to turn back, but Vergil stops you.')
        write('[Vergil] Listen! I was sent to help you by Beatrice, the Virgin Mary, and Saint Lucia. We are on a divine quest. We cannot stop now.')
        y = make_choice(['Have courage', 'Escape'])
        if (y == 1):
            write('You think of Beatrice, and you feel more courageous.')
            write('You follow Vergil into the Inferno.')
        elif (y == 2):
            write('Tu scappi tra gli alberi.')
            write('You continue to wander for many years. You see many parts of Italy, but never return to Florence.')
            write('You write some poems, but they do not become popular. The language of literature is still Latin.')
            write('You die of Malaria in Ravenna.')
            ask('Restart?')
            return start_game, info
    elif (x == 2):
        write('You follow Vergil into the Inferno.')
    time.sleep(2)
    return ante, info

# ANTE-INFERNO


def ante(info):
    write('ANTE-INFERNO')
    time.sleep(2)
    write('As you descend, you hear the cries of the Damned.')
    ask('Ask Vergil where you are')
    write('[Vergil] This is the ante-inferno. These souls have no hope of death... They are those who cared for nothing but themselves during their lives.')
    x = make_choice(['Stop to look around', 'Continue'])
    if (x == 1):
        write('You look at the spirits in Limbo. You see many insects, wasps, and worms, which are biting and stinging the Damned.')
    write('You continue towards a great black river.')
    write('[Vergil] This is the river Acheron.')
    write('An old man approaches you. He has long, white hair. When he looks at you, you see his eyes are red.')
    write('[Charon] Woe to you, depraved souls!')
    write('[Charon] What do you want, living soul? I only transport the dead.')
    x = make_choice(['Offer him a coin', 'Try to swim across', 'Let Vergil talk to him'])
    if (x == 2):
      write('What are you doing? That is a terrible idea. Why do you want to swim here? This journey is important! No! Go back!')
      return ante, info
    elif (x == 1):
      write('[Charon] Only the dead can buy this ticket.')
      write('[Vergil] This is a divine quest. Let us cross.')
      write('Charon lets you board. As you sail, the earth begins to shake. You see a bright flash of red light...')
      write('You faint.')
      time.sleep(2)
      return limbo, info

# LIMBO


def limbo(info):
    write('LIMBO')
    time.sleep(2)
    write('You wake up.')
    write('You are on the other side of the river. You hear no screams.')
    ask('Ask Vergil where you are now')
    write('[Vergil] This is Limbo. The virtuous souls who were never baptized live here. I am one of them.')
    ask('Continue walking')
    write('You come upon a great castle.')
    write('[Vergil] Here live the great people of history who never knew of God.')
    x = make_choice(['Look around', 'Continue'])
    if(x == 1):
      write('You look around and see many people you recognize… ')
    x = make_choice(['Talk to the philosophers', 'Talk to the poets', 'Talk to the Heroes', 'Talk to the politicians', 'Talk to the scholars'])
    if (x == 1):
      write('Here you see Socrates, Plato, Diogenes…')
      write('Diogenes appears to be holding a chicken and in a heated argument with Plato.')
    elif (x == 2):
      write('Here you see Socrates, Plato, Diogenes…')
      write('Diogenes appears to be holding a chicken and in a heated argument with Plato.')
    elif (x == 3):
      write('Here you see Homer, Aeneas, Caesar…')
      write('Diogenes appears to be holding a chicken and in a heated argument with Plato.')
    elif (x == 4):
      write('Here you see Ovid, …')
      write('Diogenes appears to be holding a chicken and in a heated argument with Plato.')
    elif (x == 5):
      write('Here you see Euclid, Ptolmey, Galen, Avicenna…')
      write('[Euclid] | d(x, z) - d(y, z) | <= d(x, y)')

    ask('Continue')
    write('The path grows dark again…')
    return lust, info

# LUST


def lust(info):
    write('II. LUST')

    write('As you walk, you come upon the monster Minos. \nHe stands at a gate, and as new souls approach, he decides their punishments.')
    ask('Approach Minos')
    write('[Minos] You are not a condemned soul. Go back!')
    write('[Vergil] His path is pre-ordained. Let us enter.')
    write('Minos allows you to pass.\nYou enter a violent storm. \n\nHere you see more people you recognize: Dido, Cleopatra, Helen, Paris, Aeneas… ')

    x = make_choice(['Speak to one of the spirits', 'Continue'])
    if (x == 1):
        write('You call out to two spirits. They are Francesca di Rimini and Paolo Malatesta.')
        write('[Francesca] Nessun maggior dolore che ricordasi del tempo felice nella miseria…')
    write('The souls here committed sins of passion in their lives. They cry out in desperation…\n\nYou are overwhelmed by their pain and you faint again.')
    return gluttony, info
    
# GLUTTONY
def gluttony(info):
    write('III. GLUTTONY')
    
    write('You wake up in a rainstorm. \nCerberus is in front of you. He claws at the spirits of the dead and tears at their bodies.')
    write('He looks at you.')
    x = make_choice(['Throw him a biscotto', 'Try to evade him'])
    if (x==1):
        	write('Cerberus eats the biscotto and allows you to pass.')
    if (x==2):
        	write('Vergil throws a chunk of mud at Cerberus.\nCerberus is distracted and you pass. ')
    write('A spirit approaches you.')
    
    c = make_choice('Talk to him', 'Ignore the spirit and continue')
    if(c==1):
      write('[Ciacco] I predict the white guelfs will return to power…. \n[Ciacco] Remember me…')
      info['ciacco'] = True
    write('You continue through the freezing swamp.')
    return greed, info
    
# GREED
def greed(info):
    write('IV. GREED')
    write('You come upon the demon Plutus.\n')
    time.sleep(.5)
    write('[Plutus]  Pape Satàn, pape Satàn aleppe…')
    write('Here you see the spirits of the greedy: the hoarders on one side, and the lavish on the other. They fight each other using great bags of coins as weapons. \nMany popes and cardinals dwell here.')
    ask('Continue')


def wrath(info):
  write('V. WRATH')
  write('You arrive at the river Styx. \nThe spirits of the wrathful are buried in the swamp, fighting each other. \nYou arrive at the foot of a tower.')
  ask('Let Vergil go ahead')
  
  write('Vergil goes ahead. The demons block his way.\n\nA hoard of furies appear. \nThey see you.\n[FURY] Bring out the head of Medusa!')
  
  x = make_choice(['Look', 'Let Vergil block your view'])
  if (x==1):
  	write('The furies fly out with the head of Medusa. You feel yourself growing stiff…')
  	write('Why would you look at Medusa? Everyone knows what happens when you do that. Don’t do that again!')
  	return wrath, info
  write('Vergil covers your eyes.\nYou hear the furies yell...')
  write('A light appears.\nThe demons scatter.\nAn angel descends from above…')
  ask('Bow to the angel')
  write('The gate opens. You have reached the city of Dis.')
  return heresy, info

def heresy(info):
    write('VI. HERESY')
        