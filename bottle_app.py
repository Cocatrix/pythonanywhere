
from bottle import default_app, route
import random
import copy

application = default_app()

################## Main page ##################

# Main route

@route('/')
def routeHome():
    print("Test")
    return pageHome()

# Main page : home

def pageHome():
    lines = [
        '<p></p>',
        '<p><h4><font face="Verdana" size="10">',
            'Choisis ton jeu et le nombre de joueur·ses :',
        '</h4></p>',
        '<table border="0" cellpadding="20">',
            '<tr>',
                '<th><font face="Verdana" size="10">',
                    "Legendary",
                '</th>',
                '<td><font face="Verdana" size="10">',
                    '<a href="/legendary/2">',
                        "2p",
                    '</a>',
                '</td>',
                '<td><font face="Verdana" size="10">',
                    '<a href="/legendary/3">',
                        "3p",
                    '</a>',
                '</td>',
                '<td><font face="Verdana" size="10">',
                    '<a href="/legendary/4">',
                        "4p",
                    '</a>',
                '</td>',
                '<td><font face="Verdana" size="10">',
                    '<a href="/legendary/5">',
                        "5p",
                    '</a>',
                '</td>',
            '</tr>',
        '</table>',
        ]
    return "".join(lines)

################## Legendary ##################

# Legendary Assets

coreTitle = 'Jeu de base'
coreMasterminds = [
    'Dr. Doom',
    'Loki',
    'Magneto',
    'Red Skull',
    ]
coreSchemes = [
    'Midtown Bank Robbery',
    'Negative Zone Prison Breakout',
    'Portals to the Dark Dimension',
    'Replace Earth\'s Leaders with Killbots',
    'Secret Invasion of the Skrull Shapeshifters',
    'Super Hero Civil War',
    'The Legacy Virus',
    'Unleash the Power of the Cosmic Cube',
    ]
coreVillains = [
    'Brotherhood',
    'Enemies of Asgard',
    'Hydra',
    'Masters of Evil',
    'Radiation',
    'Skrulls',
    'Spider-Foes',
    ]
coreHenchmen = [
    'Doombot Legion',
    'Hand Ninjas',
    'Savage Land Mutates',
    'Sentinel',
    ]
coreHeroes = [
    'Black Widow',
    'Captain America',
    'Cyclops',
    'Deadpool',
    'Emma Frost',
    'Gambit',
    'Hawkeye',
    'Hulk',
    'Iron Man',
    'Nick Fury',
    'Rogue',
    'Spider-Man',
    'Storm',
    'Thor',
    'Wolverine',
]

rokTitle = 'Realm of Kings'
rokMasterminds = [
    'Emperor Vulcan of the Shi\'ar',
    'Epic Emperor Vulcan',
    'Epic Maximus the Mad',
    'Maximus the Mad',
    ]
rokSchemes = [
    'Devolve with Xerogen Crystals',
    'Ruin the Perfect Wedding',
    'Tornado of Terrigen Mists',
    'War of Kings',
    ]
rokVillains = [
    'Inhuman Rebellion',
    'Shi\'ar Imperial Elite',
]
rokHenchmen = []
rokHeroes = [
    'Black Bolt',
    'Crystal',
    'Gorgon',
    'Karnak',
    'Medusa',
    ]

coreRokTitle = coreTitle + " + " + rokTitle
coreRokMasterminds = coreMasterminds + rokMasterminds
coreRokSchemes = coreSchemes + rokSchemes
coreRokVillains = coreVillains + rokVillains
coreRokHenchmen = coreHenchmen + rokHenchmen
coreRokHeroes = coreHeroes + rokHeroes

# Legendary routes

@route('/legendary/<nbPlayers>')
def routeLegendaryHome(nbPlayers):
    return pageLegendaryHome(nbPlayers)

@route('/legendary/core/<nbPlayers>')
def routeLegendaryCore(nbPlayers):
    return pageLegendaryPick(nbPlayers, coreTitle, coreSchemes, coreMasterminds, coreVillains, coreHenchmen, coreHeroes)

@route('/legendary/core-rok/<nbPlayers>')
def routeLegendaryCoreRok(nbPlayers):
    return pageLegendaryPick(nbPlayers, coreRokTitle, coreRokSchemes, coreRokMasterminds, coreRokVillains, coreRokHenchmen, coreRokHeroes)

# Legendary page : home

def pageLegendaryHome(nbPlayers):
    lines = [
        '<p></p>',
        '<p><h4><font face="Verdana" size="10">',
            'Legendary - ' + nbPlayers + 'p - Choisis avec ou sans extensions :',
        '</h4></p>',
        '<table border="0" cellpadding="20">',
            '<tr>',
                '<td><font face="Verdana" size="10">',
                    '<a href="/legendary/core/' + nbPlayers + '">',
                        coreTitle,
                    '</a>',
                '</td>',
            '</tr>',
            '<tr>',
                '<td><font face="Verdana" size="10">',
                    '<a href="/legendary/core-rok/' + nbPlayers + '">',
                        coreRokTitle,
                    '</a>',
                '</td>',
            '</tr>',
        '</table>',
        ]
    return "".join(lines)

# Legendary page : pick

def pageLegendaryPick(nbPlayers, title, schemes, masterminds, villains, henchmen, heroes):

    # Setup default number of villains, henchmen, bystanders, heroes, twists

    if(nbPlayers=='2'):
        nbVillains, nbHenchmen, nbBystanders, nbHeroes = 2, 1, 2, 5
    elif(nbPlayers=='3'):
        nbVillains, nbHenchmen, nbBystanders, nbHeroes = 3, 1, 8, 5
    elif(nbPlayers=='4'):
        nbVillains, nbHenchmen, nbBystanders, nbHeroes = 3, 2, 8, 5
    else:
        nbVillains, nbHenchmen, nbBystanders, nbHeroes = 4, 2, 12, 6

    nbTwists = 8

    # Pick Mastermind and Scheme

    pickedMastermind = random.choice(masterminds)
    pickedScheme = random.choice(schemes)
    print("Picked: ", pickedMastermind, pickedScheme)

    # Update according to Mastermind

    forcedVillain = ''
    forcedHenchman = ''
    xerogenHenchman = ''

    if (pickedMastermind==coreMasterminds[0]):  # Dr. Doom
        forcedHenchman = coreHenchmen[0]            # Doombot Legion
    elif(pickedMastermind==coreMasterminds[1]): # Loki
        forcedVillain = coreVillains[1]             # Enemies of Asgard
    elif(pickedMastermind==coreMasterminds[2]): # Magneto
        forcedVillain = coreVillains[0]             # Brotherhood
    elif(pickedMastermind==coreMasterminds[3]): # Red Skull
        forcedVillain = coreVillains[2]             # Hydra
    elif(pickedMastermind in (rokMasterminds[0], rokMasterminds[1])): # Emperor Vulcan
        forcedVillain = rokVillains[1]                                  # Shi'ar Imperial Elite
    elif(pickedMastermind in (rokMasterminds[2], rokMasterminds[3])): # Maximus the Mad
        forcedVillain = rokVillains[0]                                  # Inhuman Rebellion
    else:
        pass

    # Update according to Scheme

    if(pickedScheme==coreSchemes[0]):   # Midtown Bank Robbery
        nbBystanders = 12
    elif(pickedScheme==coreSchemes[1]): # Negative Zone Prison Breakout
        nbHenchmen += 1
    elif(pickedScheme==coreSchemes[2]): # Portals to the Dark Dimension
        nbTwists = 7
    elif(pickedScheme==coreSchemes[3]): # Replace Earth's Leaders with Killbots
        nbTwists = 5
        nbBystanders = 18
    elif(pickedScheme==coreSchemes[4]): # Secret Invasion of the Skrull Shapeshifters
        nbHeroes += 1
    elif(pickedScheme==coreSchemes[5]): # Super Hero Civil War
        if(nbPlayers=='2'):
            nbHeroes = 4
        elif(nbPlayers in ['4', '5']):
            nbTwists = 5
        else:
            pass
    elif(pickedScheme in (coreSchemes[6], coreSchemes[7])): # The Legacy Virus, Unleash the Power of the Cosmic Cube
        pass
    elif(pickedScheme==rokSchemes[0]): # Devolve with Xerogen Crystals
        nbTwists = int(nbPlayers) + 3
        nbHenchmen += 1
        xerogenHenchman = 'yes'
    elif(pickedScheme==rokSchemes[1]): # Ruin the Perfect Wedding
        nbTwists = 11
        nbHeroes += 2 # TODO: should be displayed as extra
    elif(pickedScheme==rokSchemes[2]): # Tornado of Terrigen Mists
        nbTwists = 10
    elif(pickedScheme==rokSchemes[3]): # War of Kings
        nbTwists = 11
    else:
        pass

    # Now everthing is setup
    # nbVillains, nbHenchmen, nbBystanders, nbHeroes, nbTwists, nbBystanders, forcedVillain, forcedHenchman

    print("Setup:", nbVillains, nbHenchmen, nbBystanders, nbHeroes, nbTwists, nbBystanders, forcedVillain, forcedHenchman)

    # Force villain

    if forcedVillain != '':
        copyVillains = copy.deepcopy(villains)
        copyVillains.remove(forcedVillain)
        print("Villains:", copyVillains, nbVillains)
        randomVillains = random.sample(copyVillains, nbVillains-1)
        randomVillains.append(forcedVillain.upper())
        pickedVillains = '<br>'.join(randomVillains)
    else:
        print("Villains:", villains, nbVillains)
        pickedVillains = '<br>'.join(random.sample(villains, nbVillains))

    # Force henchmen

    if (forcedHenchman != '') and (xerogenHenchman != ''):
        copyHenchmen = copy.deepcopy(henchmen)
        copyHenchmen.remove(forcedHenchman)
        xerogenHenchman = random.choice(copyHenchmen)
        copyHenchmen.remove(xerogenHenchman)
        randomHenchmen = random.sample(copyHenchmen, nbHenchmen-2)
        randomHenchmen.append(forcedHenchman.upper())
        randomHenchmen.append("Xerogen Experiment : " + xerogenHenchman)
        pickedHenchmen = '<br>'.join(randomHenchmen)
    elif (forcedHenchman != '') and (xerogenHenchman == ''):
        copyHenchmen = copy.deepcopy(henchmen)
        copyHenchmen.remove(forcedHenchman)
        randomHenchmen = random.sample(copyHenchmen, nbHenchmen-1)
        randomHenchmen.append(forcedHenchman.upper())
        pickedHenchmen = '<br>'.join(randomHenchmen)
    elif (forcedHenchman == '') and (xerogenHenchman != ''):
        xerogenHenchman = random.choice(henchmen)
        copyHenchmen = copy.deepcopy(henchmen)
        copyHenchmen.remove(xerogenHenchman)
        randomHenchmen = random.sample(copyHenchmen, nbHenchmen-1)
        randomHenchmen.append("Xerogen Experiment : " + xerogenHenchman)
        pickedHenchmen = '<br>'.join(randomHenchmen)
    else:
        pickedHenchmen = '<br>'.join(random.sample(henchmen, nbHenchmen))

    # Pick heroes

    pickedHeroes = '<br>'.join(random.sample(heroes, nbHeroes))

    # Display the result in a table

    lines = [
        '<p></p>',
        '<p><h4><font face="Verdana" size="10">',
            '&emsp;&emsp;&emsp;Legendary - ' + nbPlayers + 'p - ' + title,
        '</h4></p>',
        '<table border="1" cellpadding="20">',
            '<tr>',
                '<th align="right"><font face="Verdana" size="10">',
                    'Mastermind',
                '</th>',
                '<td><font face="Verdana" size="10">',
                    pickedMastermind,
                '</td>',
            '</tr>',
            '<tr style="background-color:#eab676;">',
                '<th align="right"><font face="Verdana" size="10">',
                    'Scheme',
                '</th>',
                '<td><font face="Verdana" size="10">',
                    pickedScheme,
                '</td>',
            '</tr>',
            '<tr>',
                '<th align="right"><font face="Verdana" size="10">',
                    'Villains',
                '</th>',
                '<td><font face="Verdana" size="10">',
                    pickedVillains,
                '</td>',
            '</tr>',
            '<tr style="background-color:#eab676;">',
                '<th align="right"><font face="Verdana" size="10">',
                    'Henchmen',
                '</th>',
                '<td><font face="Verdana" size="10">',
                    pickedHenchmen,
                '</td>',
            '</tr>',
            '<tr>',
                '<th align="right"><font face="Verdana" size="10">',
                    'Heroes',
                '</th>',
                '<td><font face="Verdana" size="10">',
                    pickedHeroes,
                '</td>',
            '</tr>',
            '<tr style="background-color:#eab676;">',
                '<th align="right"><font face="Verdana" size="10">',
                    'Bystanders',
                '</th>',
                '<td><font face="Verdana" size="10">',
                    str(nbBystanders),
                '</td>',
            '</tr>',
            '<tr>',
                '<th align="right"><font face="Verdana" size="10">',
                    'Scheme Twists',
                '</th>',
                '<td><font face="Verdana" size="10">',
                    str(nbTwists),
                '</td>',
            '</tr>',
        '</table>',
        ]
    return "".join(lines)

