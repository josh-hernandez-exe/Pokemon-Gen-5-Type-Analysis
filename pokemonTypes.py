global TOL
global NUM_TYPES 
global TYPELIST
global WORDLIST
global TYPECHART 
global DUALCHART
global PKMNTYPELIST
global NUMPKMNCHART
global WEAKCHART 
global RESISTCHART

global POKEDEX


TOL = 0.01
NUM_TYPES = 17


class Pokemon:
    __generation = (0,151,251,386,493,649)

    #National Pokédex №
    #Name
    #Type
    #HP
    #Attack
    #Defense
    #Sp. Atk
    #Sp. Def
    #Speed
    #Total

    def __init__(self,argList):

        if len( argList ) == 11 :

            argList.reverse()
            
            self.__index = int(argList.pop() )
            self.__name = argList.pop()
            self.__type1 = argList.pop()
            self.__type2 = argList.pop()
            self.__hp = int( argList.pop() )
            self.__pAtk = int( argList.pop() )
            self.__pDef = int( argList.pop() )
            self.__sAtk = int( argList.pop() )
            self.__sDef = int( argList.pop() )
            self.__speed = int( argList.pop() )
            self.__total = int( argList.pop() )
            
        elif len(argList) == 0:
            self.__index = 0
            self.__name = ""
            self.__type1 = ""
            self.__type2 = ""
            self.__hp = 0
            self.__pAtk = 0
            self.__pDef = 0
            self.__sAtk = 0
            self.__sDef = 0
            self.__speed = 0
            self.__total = 0

    def getIndex(self):
        return self.__index

    def getName(self):
        return self.__name
    
    def getType1(self):
        return self.__type1
    
    def getType2(self):
        return self.__type2
    
    def getHP(self):
        return self.__hp
    
    def getAtk(self):
        return self.__pAtk
    
    def getDef(self):
        return self.__pDef
    
    def getSAtk(self):
        return self.__sAtk
    
    def getSDef(self):
        return self.__sDef
    
    def getSpeed(self):
        return self.__speed
    
    def getTotal(self):
        return self.__total
    



class Pokedex :
    def __init__(self):
        self.__pokedex = []
        self.__pokedex.append( Pokemon( [] ) )
        self.__makePokedex()
        self.finalize()

    def add(self,pokemon):
        if type(self.__pokedex)==list:
            self.__pokedex.append(pokemon)

    def quickSort(self,*args):
        if type(self.__pokedex)==list:
            if len(args)==0 :
                start = 0
                end = len(self.__pokedex)

                quicksort(start,end)
                

            elif len(args)==2:
                array = self.__pokedex
                start = args[0]
                end = args[1]
                pivot = (start+end-1)/2
            
                if end-start>1:
                    
                    pivotValue = array[pivot].index

                    temp = array[pivot]
                    array[pivot] = array[end-1]
                    array[end-1] = temp

                    curIndex = start

                    i=start

                    while( i<end-1 ):

                        if array[i].index < pivotValue:
                            temp = array[i]
                            array[i] = array[curIndex]
                            array[curIndex] = temp
                            curIndex+=1

                        i+=1
                        
                    temp = array[end-1]
                    array[end-1] = array[curIndex]
                    array[curIndex] = temp

                    quicksort(start,curIndex)
                    quicksort(curIndex+1,end)
            else:
                print "quicksort recived the incorrect number of args"
                raise

    def checkSorted(self):
        if type(self.__pokedex)==list:
            isSorted = True

            for i in range( len( self.__pokedex ) -1 ) :
                if( self.__pokedex[i+1].index > self.__pokedex[i].index ):
                    isSorted = False

            if not isSorted:
                quickSort()

    def finalize(self):
        self.__pokedex = tuple(self.__pokedex)

    def __getitem__(self,index):
        return self.__pokedex[index]

    def size(self):
        return len(self.__pokedex)

   
    def __makePokedex(self):
        # http://pokemondb.net/pokedex/all

        # All content © 2008-2012 Pokémon Database. Pokémon and its related entities are © 1995-2012 Nintendo.
        # This is an unofficial fansite not affiliated with Nintendo.

        #Number
        #Name
        #Type
        #HP
        #Attack
        #Defense
        #Sp. Atk
        #Sp. Def
        #Speed
        #Total

        NationalText  = '''

         001	Bulbasaur	GRASS
        POISON	45	49	49	65	65	45	318
         002	Ivysaur	GRASS
        POISON	60	62	63	80	80	60	405
         003	Venusaur	GRASS
        POISON	80	82	83	100	100	80	525
         004	Charmander	FIRE
        39	52	43	60	50	65	309
         005	Charmeleon	FIRE
        58	64	58	80	65	80	405
         006	Charizard	FIRE
        FLYING	78	84	78	109	85	100	534
         007	Squirtle	WATER
        44	48	65	50	64	43	314
         008	Wartortle	WATER
        59	63	80	65	80	58	405
         009	Blastoise	WATER
        79	83	100	85	105	78	530
         010	Caterpie	BUG
        45	30	35	20	20	45	195
         011	Metapod	BUG
        50	20	55	25	25	30	205
         012	Butterfree	BUG
        FLYING	60	45	50	80	80	70	385
         013	Weedle	BUG
        POISON	40	35	30	20	20	50	195
         014	Kakuna	BUG
        POISON	45	25	50	25	25	35	205
         015	Beedrill	BUG
        POISON	65	80	40	45	80	75	385
         016	Pidgey	NORMAL
        FLYING	40	45	40	35	35	56	251
         017	Pidgeotto	NORMAL
        FLYING	63	60	55	50	50	71	349
         018	Pidgeot	NORMAL
        FLYING	83	80	75	70	70	91	469
         019	Rattata	NORMAL
        30	56	35	25	35	72	253ß
         020	Raticate	NORMAL
        55	81	60	50	70	97	413
         021	Spearow	NORMAL
        FLYING	40	60	30	31	31	70	262
         022	Fearow	NORMAL
        FLYING	65	90	65	61	61	100	442
         023	Ekans	POISON
        35	60	44	40	54	55	288
         024	Arbok	POISON
        60	85	69	65	79	80	438
         025	Pikachu	ELECTRIC
        35	55	30	50	40	90	300
         026	Raichu	ELECTRIC
        60	90	55	90	80	100	475
         027	Sandshrew	GROUND
        50	75	85	20	30	40	300
         028	Sandslash	GROUND
        75	100	110	45	55	65	450
         029	Nidoran♀	POISON
        55	47	52	40	40	41	275
         030	Nidorina	POISON
        70	62	67	55	55	56	365
         031	Nidoqueen	POISON
        GROUND	90	82	87	75	85	76	495
         032	Nidoran♂	POISON
        46	57	40	40	40	50	273
         033	Nidorino	POISON
        61	72	57	55	55	65	365
         034	Nidoking	POISON
        GROUND	81	92	77	85	75	85	495
         035	Clefairy	NORMAL
        70	45	48	60	65	35	323
         036	Clefable	NORMAL
        95	70	73	85	90	60	473
         037	Vulpix	FIRE
        38	41	40	50	65	65	299
         038	Ninetales	FIRE
        73	76	75	81	100	100	505
         039	Jigglypuff	NORMAL
        115	45	20	45	25	20	270
         040	Wigglytuff	NORMAL
        140	70	45	75	50	45	425
         041	Zubat	POISON
        FLYING	40	45	35	30	40	55	245
         042	Golbat	POISON
        FLYING	75	80	70	65	75	90	455
         043	Oddish	GRASS
        POISON	45	50	55	75	65	30	320
         044	Gloom	GRASS
        POISON	60	65	70	85	75	40	395
         045	Vileplume	GRASS
        POISON	75	80	85	100	90	50	480
         046	Paras	BUG
        GRASS	35	70	55	45	55	25	285
         047	Parasect	BUG
        GRASS	60	95	80	60	80	30	405
         048	Venonat	BUG
        POISON	60	55	50	40	55	45	305
         049	Venomoth	BUG
        POISON	70	65	60	90	75	90	450
         050	Diglett	GROUND
        10	55	25	35	45	95	265
         051	Dugtrio	GROUND
        35	80	50	50	70	120	405
         052	Meowth	NORMAL
        40	45	35	40	40	90	290
         053	Persian	NORMAL
        65	70	60	65	65	115	440
         054	Psyduck	WATER
        50	52	48	65	50	55	320
         055	Golduck	WATER
        80	82	78	95	80	85	500
         056	Mankey	FIGHTING
        40	80	35	35	45	70	305
         057	Primeape	FIGHTING
        65	105	60	60	70	95	455
         058	Growlithe	FIRE
        55	70	45	70	50	60	350
         059	Arcanine	FIRE
        90	110	80	100	80	95	555
         060	Poliwag	WATER
        40	50	40	40	40	90	300
         061	Poliwhirl	WATER
        65	65	65	50	50	90	385
         062	Poliwrath	WATER
        FIGHTING	90	85	95	70	90	70	500
         063	Abra	PSYCHIC
        25	20	15	105	55	90	310
         064	Kadabra	PSYCHIC
        40	35	30	120	70	105	400
         065	Alakazam	PSYCHIC
        55	50	45	135	85	120	490
         066	Machop	FIGHTING
        70	80	50	35	35	35	305
         067	Machoke	FIGHTING
        80	100	70	50	60	45	405
         068	Machamp	FIGHTING
        90	130	80	65	85	55	505
         069	Bellsprout	GRASS
        POISON	50	75	35	70	30	40	300
         070	Weepinbell	GRASS
        POISON	65	90	50	85	45	55	390
         071	Victreebel	GRASS
        POISON	80	105	65	100	60	70	480
         072	Tentacool	WATER
        POISON	40	40	35	50	100	70	335
         073	Tentacruel	WATER
        POISON	80	70	65	80	120	100	515
         074	Geodude	ROCK
        GROUND	40	80	100	30	30	20	300
         075	Graveler	ROCK
        GROUND	55	95	115	45	45	35	390
         076	Golem	ROCK
        GROUND	80	110	130	55	65	45	485
         077	Ponyta	FIRE
        50	85	55	65	65	90	410
         078	Rapidash	FIRE
        65	100	70	80	80	105	500
         079	Slowpoke	WATER
        PSYCHIC	90	65	65	40	40	15	315
         080	Slowbro	WATER
        PSYCHIC	95	75	110	100	80	30	490
         081	Magnemite	ELECTRIC
        STEEL	25	35	70	95	55	45	325
         082	Magneton	ELECTRIC
        STEEL	50	60	95	120	70	70	465
         083	Farfetch'd	NORMAL
        FLYING	52	65	55	58	62	60	352
         084	Doduo	NORMAL
        FLYING	35	85	45	35	35	75	310
         085	Dodrio	NORMAL
        FLYING	60	110	70	60	60	100	460
         086	Seel	WATER
        65	45	55	45	70	45	325
         087	Dewgong	WATER
        ICE	90	70	80	70	95	70	475
         088	Grimer	POISON
        80	80	50	40	50	25	325
         089	Muk	POISON
        105	105	75	65	100	50	500
         090	Shellder	WATER
        30	65	100	45	25	40	305
         091	Cloyster	WATER
        ICE	50	95	180	85	45	70	525
         092	Gastly	GHOST
        POISON	30	35	30	100	35	80	310
         093	Haunter	GHOST
        POISON	45	50	45	115	55	95	405
         094	Gengar	GHOST
        POISON	60	65	60	130	75	110	500
         095	Onix	ROCK
        GROUND	35	45	160	30	45	70	385
         096	Drowzee	PSYCHIC
        60	48	45	43	90	42	328
         097	Hypno	PSYCHIC
        85	73	70	73	115	67	483
         098	Krabby	WATER
        30	105	90	25	25	50	325
         099	Kingler	WATER
        55	130	115	50	50	75	475
         100	Voltorb	ELECTRIC
        40	30	50	55	55	100	330
         101	Electrode	ELECTRIC
        60	50	70	80	80	140	480
         102	Exeggcute	GRASS
        PSYCHIC	60	40	80	60	45	40	325
         103	Exeggutor	GRASS
        PSYCHIC	95	95	85	125	65	55	520
         104	Cubone	GROUND
        50	50	95	40	50	35	320
         105	Marowak	GROUND
        60	80	110	50	80	45	425
         106	Hitmonlee	FIGHTING
        50	120	53	35	110	87	455
         107	Hitmonchan	FIGHTING
        50	105	79	35	110	76	455
         108	Lickitung	NORMAL
        90	55	75	60	75	30	385
         109	Koffing	POISON
        40	65	95	60	45	35	340
         110	Weezing	POISON
        65	90	120	85	70	60	490
         111	Rhyhorn	GROUND
        ROCK	80	85	95	30	30	25	345
         112	Rhydon	GROUND
        ROCK	105	130	120	45	45	40	485
         113	Chansey	NORMAL
        250	5	5	35	105	50	450
         114	Tangela	GRASS
        65	55	115	100	40	60	435
         115	Kangaskhan	NORMAL
        105	95	80	40	80	90	490
         116	Horsea	WATER
        30	40	70	70	25	60	295
         117	Seadra	WATER
        55	65	95	95	45	85	440
         118	Goldeen	WATER
        45	67	60	35	50	63	320
         119	Seaking	WATER
        80	92	65	65	80	68	450
         120	Staryu	WATER
        30	45	55	70	55	85	340
         121	Starmie	WATER
        PSYCHIC	60	75	85	100	85	115	520
         122	Mr. Mime	PSYCHIC
        40	45	65	100	120	90	460
         123	Scyther	BUG
        FLYING	70	110	80	55	80	105	500
         124	Jynx	ICE
        PSYCHIC	65	50	35	115	95	95	455
         125	Electabuzz	ELECTRIC
        65	83	57	95	85	105	490
         126	Magmar	FIRE
        65	95	57	100	85	93	495
         127	Pinsir	BUG
        65	125	100	55	70	85	500
         128	Tauros	NORMAL
        75	100	95	40	70	110	490
         129	Magikarp	WATER
        20	10	55	15	20	80	200
         130	Gyarados	WATER
        FLYING	95	125	79	60	100	81	540
         131	Lapras	WATER
        ICE	130	85	80	85	95	60	535
         132	Ditto	NORMAL
        48	48	48	48	48	48	288
         133	Eevee	NORMAL
        55	55	50	45	65	55	325
         134	Vaporeon	WATER
        130	65	60	110	95	65	525
         135	Jolteon	ELECTRIC
        65	65	60	110	95	130	525
         136	Flareon	FIRE
        65	130	60	95	110	65	525
         137	Porygon	NORMAL
        65	60	70	85	75	40	395
         138	Omanyte	ROCK
        WATER	35	40	100	90	55	35	355
         139	Omastar	ROCK
        WATER	70	60	125	115	70	55	495
         140	Kabuto	ROCK
        WATER	30	80	90	55	45	55	355
         141	Kabutops	ROCK
        WATER	60	115	105	65	70	80	495
         142	Aerodactyl	ROCK
        FLYING	80	105	65	60	75	130	515
         143	Snorlax	NORMAL
        160	110	65	65	110	30	540
         144	Articuno	ICE
        FLYING	90	85	100	95	125	85	580
         145	Zapdos	ELECTRIC
        FLYING	90	90	85	125	90	100	580
         146	Moltres	FIRE
        FLYING	90	100	90	125	85	90	580
         147	Dratini	DRAGON
        41	64	45	50	50	50	300
         148	Dragonair	DRAGON
        61	84	65	70	70	70	420
         149	Dragonite	DRAGON
        FLYING	91	134	95	100	100	80	600
         150	Mewtwo	PSYCHIC
        106	110	90	154	90	130	680
         151	Mew	PSYCHIC
        100	100	100	100	100	100	600
         152	Chikorita	GRASS
        45	49	65	49	65	45	318
         153	Bayleef	GRASS
        60	62	80	63	80	60	405
         154	Meganium	GRASS
        80	82	100	83	100	80	525
         155	Cyndaquil	FIRE
        39	52	43	60	50	65	309
         156	Quilava	FIRE
        58	64	58	80	65	80	405
         157	Typhlosion	FIRE
        78	84	78	109	85	100	534
         158	Totodile	WATER
        50	65	64	44	48	43	314
         159	Croconaw	WATER
        65	80	80	59	63	58	405
         160	Feraligatr	WATER
        85	105	100	79	83	78	530
         161	Sentret	NORMAL
        35	46	34	35	45	20	215
         162	Furret	NORMAL
        85	76	64	45	55	90	415
         163	Hoothoot	NORMAL
        FLYING	60	30	30	36	56	50	262
         164	Noctowl	NORMAL
        FLYING	100	50	50	76	96	70	442
         165	Ledyba	BUG
        FLYING	40	20	30	40	80	55	265
         166	Ledian	BUG
        FLYING	55	35	50	55	110	85	390
         167	Spinarak	BUG
        POISON	40	60	40	40	40	30	250
         168	Ariados	BUG
        POISON	70	90	70	60	60	40	390
         169	Crobat	POISON
        FLYING	85	90	80	70	80	130	535
         170	Chinchou	WATER
        ELECTRIC	75	38	38	56	56	67	330
         171	Lanturn	WATER
        ELECTRIC	125	58	58	76	76	67	460
         172	Pichu	ELECTRIC
        20	40	15	35	35	60	205
         173	Cleffa	NORMAL
        50	25	28	45	55	15	218
         174	Igglybuff	NORMAL
        90	30	15	40	20	15	210
         175	Togepi	NORMAL
        35	20	65	40	65	20	245
         176	Togetic	NORMAL
        FLYING	55	40	85	80	105	40	405
         177	Natu	PSYCHIC
        FLYING	40	50	45	70	45	70	320
         178	Xatu	PSYCHIC
        FLYING	65	75	70	95	70	95	470
         179	Mareep	ELECTRIC
        55	40	40	65	45	35	280
         180	Flaaffy	ELECTRIC
        70	55	55	80	60	45	365
         181	Ampharos	ELECTRIC
        90	75	75	115	90	55	500
         182	Bellossom	GRASS
        75	80	85	90	100	50	480
         183	Marill	WATER
        70	20	50	20	50	40	250
         184	Azumarill	WATER
        100	50	80	50	80	50	410
         185	Sudowoodo	ROCK
        70	100	115	30	65	30	410
         186	Politoed	WATER
        90	75	75	90	100	70	500
         187	Hoppip	GRASS
        FLYING	35	35	40	35	55	50	250
         188	Skiploom	GRASS
        FLYING	55	45	50	45	65	80	340
         189	Jumpluff	GRASS
        FLYING	75	55	70	55	85	110	450
         190	Aipom	NORMAL
        55	70	55	40	55	85	360
         191	Sunkern	GRASS
        30	30	30	30	30	30	180
         192	Sunflora	GRASS
        75	75	55	105	85	30	425
         193	Yanma	BUG
        FLYING	65	65	45	75	45	95	390
         194	Wooper	WATER
        GROUND	55	45	45	25	25	15	210
         195	Quagsire	WATER
        GROUND	95	85	85	65	65	35	430
         196	Espeon	PSYCHIC
        65	65	60	130	95	110	525
         197	Umbreon	DARK
        95	65	110	60	130	65	525
         198	Murkrow	DARK
        FLYING	60	85	42	85	42	91	405
         199	Slowking	WATER
        PSYCHIC	95	75	80	100	110	30	490
         200	Misdreavus	GHOST
        60	60	60	85	85	85	435
         201	Unown	PSYCHIC
        48	72	48	72	48	48	336
         202	Wobbuffet	PSYCHIC
        190	33	58	33	58	33	405
         203	Girafarig	NORMAL
        PSYCHIC	70	80	65	90	65	85	455
         204	Pineco	BUG
        50	65	90	35	35	15	290
         205	Forretress	BUG
        STEEL	75	90	140	60	60	40	465
         206	Dunsparce	NORMAL
        100	70	70	65	65	45	415
         207	Gligar	GROUND
        FLYING	65	75	105	35	65	85	430
         208	Steelix	STEEL
        GROUND	75	85	200	55	65	30	510
         209	Snubbull	NORMAL
        60	80	50	40	40	30	300
         210	Granbull	NORMAL
        90	120	75	60	60	45	450
         211	Qwilfish	WATER
        POISON	65	95	75	55	55	85	430
         212	Scizor	BUG
        STEEL	70	130	100	55	80	65	500
         213	Shuckle	BUG
        ROCK	20	10	230	10	230	5	505
         214	Heracross	BUG
        FIGHTING	80	125	75	40	95	85	500
         215	Sneasel	DARK
        ICE	55	95	55	35	75	115	430
         216	Teddiursa	NORMAL
        60	80	50	50	50	40	330
         217	Ursaring	NORMAL
        90	130	75	75	75	55	500
         218	Slugma	FIRE
        40	40	40	70	40	20	250
         219	Magcargo	FIRE
        ROCK	50	50	120	80	80	30	410
         220	Swinub	ICE
        GROUND	50	50	40	30	30	50	250
         221	Piloswine	ICE
        GROUND	100	100	80	60	60	50	450
         222	Corsola	WATER
        ROCK	55	55	85	65	85	35	380
         223	Remoraid	WATER
        35	65	35	65	35	65	300
         224	Octillery	WATER
        75	105	75	105	75	45	480
         225	Delibird	ICE
        FLYING	45	55	45	65	45	75	330
         226	Mantine	WATER
        FLYING	65	40	70	80	140	70	465
         227	Skarmory	STEEL
        FLYING	65	80	140	40	70	70	465
         228	Houndour	DARK
        FIRE	45	60	30	80	50	65	330
         229	Houndoom	DARK
        FIRE	75	90	50	110	80	95	500
         230	Kingdra	WATER
        DRAGON	75	95	95	95	95	85	540
         231	Phanpy	GROUND
        90	60	60	40	40	40	330
         232	Donphan	GROUND
        90	120	120	60	60	50	500
         233	Porygon2	NORMAL
        85	80	90	105	95	60	515
         234	Stantler	NORMAL
        73	95	62	85	65	85	465
         235	Smeargle	NORMAL
        55	20	35	20	45	75	250
         236	Tyrogue	FIGHTING
        35	35	35	35	35	35	210
         237	Hitmontop	FIGHTING
        50	95	95	35	110	70	455
         238	Smoochum	ICE
        PSYCHIC	45	30	15	85	65	65	305
         239	Elekid	ELECTRIC
        45	63	37	65	55	95	360
         240	Magby	FIRE
        45	75	37	70	55	83	365
         241	Miltank	NORMAL
        95	80	105	40	70	100	490
         242	Blissey	NORMAL
        255	10	10	75	135	55	540
         243	Raikou	ELECTRIC
        90	85	75	115	100	115	580
         244	Entei	FIRE
        115	115	85	90	75	100	580
         245	Suicune	WATER
        100	75	115	90	115	85	580
         246	Larvitar	ROCK
        GROUND	50	64	50	45	50	41	300
         247	Pupitar	ROCK
        GROUND	70	84	70	65	70	51	410
         248	Tyranitar	ROCK
        DARK	100	134	110	95	100	61	600
         249	Lugia	PSYCHIC
        FLYING	106	90	130	90	154	110	680
         250	Ho-oh	FIRE
        FLYING	106	130	90	110	154	90	680
         251	Celebi	PSYCHIC
        GRASS	100	100	100	100	100	100	600
         252	Treecko	GRASS
        40	45	35	65	55	70	310
         253	Grovyle	GRASS
        50	65	45	85	65	95	405
         254	Sceptile	GRASS
        70	85	65	105	85	120	530
         255	Torchic	FIRE
        45	60	40	70	50	45	310
         256	Combusken	FIRE
        FIGHTING	60	85	60	85	60	55	405
         257	Blaziken	FIRE
        FIGHTING	80	120	70	110	70	80	530
         258	Mudkip	WATER
        50	70	50	50	50	40	310
         259	Marshtomp	WATER
        GROUND	70	85	70	60	70	50	405
         260	Swampert	WATER
        GROUND	100	110	90	85	90	60	535
         261	Poochyena	DARK
        35	55	35	30	30	35	220
         262	Mightyena	DARK
        70	90	70	60	60	70	420
         263	Zigzagoon	NORMAL
        38	30	41	30	41	60	240
         264	Linoone	NORMAL
        78	70	61	50	61	100	420
         265	Wurmple	BUG
        45	45	35	20	30	20	195
         266	Silcoon	BUG
        50	35	55	25	25	15	205
         267	Beautifly	BUG
        FLYING	60	70	50	90	50	65	385
         268	Cascoon	BUG
        50	35	55	25	25	15	205
         269	Dustox	BUG
        POISON	60	50	70	50	90	65	385
         270	Lotad	WATER
        GRASS	40	30	30	40	50	30	220
         271	Lombre	WATER
        GRASS	60	50	50	60	70	50	340
         272	Ludicolo	WATER
        GRASS	80	70	70	90	100	70	480
         273	Seedot	GRASS
        40	40	50	30	30	30	220
         274	Nuzleaf	GRASS
        DARK	70	70	40	60	40	60	340
         275	Shiftry	GRASS
        DARK	90	100	60	90	60	80	480
         276	Taillow	NORMAL
        FLYING	40	55	30	30	30	85	270
         277	Swellow	NORMAL
        FLYING	60	85	60	50	50	125	430
         278	Wingull	WATER
        FLYING	40	30	30	55	30	85	270
         279	Pelipper	WATER
        FLYING	60	50	100	85	70	65	430
         280	Ralts	PSYCHIC
        28	25	25	45	35	40	198
         281	Kirlia	PSYCHIC
        38	35	35	65	55	50	278
         282	Gardevoir	PSYCHIC
        68	65	65	125	115	80	518
         283	Surskit	BUG
        WATER	40	30	32	50	52	65	269
         284	Masquerain	BUG
        FLYING	70	60	62	80	82	60	414
         285	Shroomish	GRASS
        60	40	60	40	60	35	295
         286	Breloom	GRASS
        FIGHTING	60	130	80	60	60	70	460
         287	Slakoth	NORMAL
        60	60	60	35	35	30	280
         288	Vigoroth	NORMAL
        80	80	80	55	55	90	440
         289	Slaking	NORMAL
        150	160	100	95	65	100	670
         290	Nincada	BUG
        GROUND	31	45	90	30	30	40	266
         291	Ninjask	BUG
        FLYING	61	90	45	50	50	160	456
         292	Shedinja	BUG
        GHOST	1	90	45	30	30	40	236
         293	Whismur	NORMAL
        64	51	23	51	23	28	240
         294	Loudred	NORMAL
        84	71	43	71	43	48	360
         295	Exploud	NORMAL
        104	91	63	91	63	68	480
         296	Makuhita	FIGHTING
        72	60	30	20	30	25	237
         297	Hariyama	FIGHTING
        144	120	60	40	60	50	474
         298	Azurill	NORMAL
        50	20	40	20	40	20	190
         299	Nosepass	ROCK
        30	45	135	45	90	30	375
         300	Skitty	NORMAL
        50	45	45	35	35	50	260
         301	Delcatty	NORMAL
        70	65	65	55	55	70	380
         302	Sableye	DARK
        GHOST	50	75	75	65	65	50	380
         303	Mawile	STEEL
        50	85	85	55	55	50	380
         304	Aron	STEEL
        ROCK	50	70	100	40	40	30	330
         305	Lairon	STEEL
        ROCK	60	90	140	50	50	40	430
         306	Aggron	STEEL
        ROCK	70	110	180	60	60	50	530
         307	Meditite	FIGHTING
        PSYCHIC	30	40	55	40	55	60	280
         308	Medicham	FIGHTING
        PSYCHIC	60	60	75	60	75	80	410
         309	Electrike	ELECTRIC
        40	45	40	65	40	65	295
         310	Manectric	ELECTRIC
        70	75	60	105	60	105	475
         311	Plusle	ELECTRIC
        60	50	40	85	75	95	405
         312	Minun	ELECTRIC
        60	40	50	75	85	95	405
         313	Volbeat	BUG
        65	73	55	47	75	85	400
         314	Illumise	BUG
        65	47	55	73	75	85	400
         315	Roselia	GRASS
        POISON	50	60	45	100	80	65	400
         316	Gulpin	POISON
        70	43	53	43	53	40	302
         317	Swalot	POISON
        100	73	83	73	83	55	467
         318	Carvanha	WATER
        DARK	45	90	20	65	20	65	305
         319	Sharpedo	WATER
        DARK	70	120	40	95	40	95	460
         320	Wailmer	WATER
        130	70	35	70	35	60	400
         321	Wailord	WATER
        170	90	45	90	45	60	500
         322	Numel	FIRE
        GROUND	60	60	40	65	45	35	305
         323	Camerupt	FIRE
        GROUND	70	100	70	105	75	40	460
         324	Torkoal	FIRE
        70	85	140	85	70	20	470
         325	Spoink	PSYCHIC
        60	25	35	70	80	60	330
         326	Grumpig	PSYCHIC
        80	45	65	90	110	80	470
         327	Spinda	NORMAL
        60	60	60	60	60	60	360
         328	Trapinch	GROUND
        45	100	45	45	45	10	290
         329	Vibrava	GROUND
        DRAGON	50	70	50	50	50	70	340
         330	Flygon	GROUND
        DRAGON	80	100	80	80	80	100	520
         331	Cacnea	GRASS
        50	85	40	85	40	35	335
         332	Cacturne	GRASS
        DARK	70	115	60	115	60	55	475
         333	Swablu	NORMAL
        FLYING	45	40	60	40	75	50	310
         334	Altaria	DRAGON
        FLYING	75	70	90	70	105	80	490
         335	Zangoose	NORMAL
        73	115	60	60	60	90	458
         336	Seviper	POISON
        73	100	60	100	60	65	458
         337	Lunatone	ROCK
        PSYCHIC	70	55	65	95	85	70	440
         338	Solrock	ROCK
        PSYCHIC	70	95	85	55	65	70	440
         339	Barboach	WATER
        GROUND	50	48	43	46	41	60	288
         340	Whiscash	WATER
        GROUND	110	78	73	76	71	60	468
         341	Corphish	WATER
        43	80	65	50	35	35	308
         342	Crawdaunt	WATER
        DARK	63	120	85	90	55	55	468
         343	Baltoy	GROUND
        PSYCHIC	40	40	55	40	70	55	300
         344	Claydol	GROUND
        PSYCHIC	60	70	105	70	120	75	500
         345	Lileep	ROCK
        GRASS	66	41	77	61	87	23	355
         346	Cradily	ROCK
        GRASS	86	81	97	81	107	43	495
         347	Anorith	ROCK
        BUG	45	95	50	40	50	75	355
         348	Armaldo	ROCK
        BUG	75	125	100	70	80	45	495
         349	Feebas	WATER
        20	15	20	10	55	80	200
         350	Milotic	WATER
        95	60	79	100	125	81	540
         351	Castform	NORMAL
        70	70	70	70	70	70	420
         352	Kecleon	NORMAL
        60	90	70	60	120	40	440
         353	Shuppet	GHOST
        44	75	35	63	33	45	295
         354	Banette	GHOST
        64	115	65	83	63	65	455
         355	Duskull	GHOST
        20	40	90	30	90	25	295
         356	Dusclops	GHOST
        40	70	130	60	130	25	455
         357	Tropius	GRASS
        FLYING	99	68	83	72	87	51	460
         358	Chimecho	PSYCHIC
        65	50	70	95	80	65	425
         359	Absol	DARK
        65	130	60	75	60	75	465
         360	Wynaut	PSYCHIC
        95	23	48	23	48	23	260
         361	Snorunt	ICE
        50	50	50	50	50	50	300
         362	Glalie	ICE
        80	80	80	80	80	80	480
         363	Spheal	ICE
        WATER	70	40	50	55	50	25	290
         364	Sealeo	ICE
        WATER	90	60	70	75	70	45	410
         365	Walrein	ICE
        WATER	110	80	90	95	90	65	530
         366	Clamperl	WATER
        35	64	85	74	55	32	345
         367	Huntail	WATER
        55	104	105	94	75	52	485
         368	Gorebyss	WATER
        55	84	105	114	75	52	485
         369	Relicanth	WATER
        ROCK	100	90	130	45	65	55	485
         370	Luvdisc	WATER
        43	30	55	40	65	97	330
         371	Bagon	DRAGON
        45	75	60	40	30	50	300
         372	Shelgon	DRAGON
        65	95	100	60	50	50	420
         373	Salamence	DRAGON
        FLYING	95	135	80	110	80	100	600
         374	Beldum	STEEL
        PSYCHIC	40	55	80	35	60	30	300
         375	Metang	STEEL
        PSYCHIC	60	75	100	55	80	50	420
         376	Metagross	STEEL
        PSYCHIC	80	135	130	95	90	70	600
         377	Regirock	ROCK
        80	100	200	50	100	50	580
         378	Regice	ICE
        80	50	100	100	200	50	580
         379	Registeel	STEEL
        80	75	150	75	150	50	580
         380	Latias	DRAGON
        PSYCHIC	80	80	90	110	130	110	600
         381	Latios	DRAGON
        PSYCHIC	80	90	80	130	110	110	600
         382	Kyogre	WATER
        100	100	90	150	140	90	670
         383	Groudon	GROUND
        100	150	140	100	90	90	670
         384	Rayquaza	DRAGON
        FLYING	105	150	90	150	90	95	680
         385	Jirachi	STEEL
        PSYCHIC	100	100	100	100	100	100	600
         386	Deoxys
        Normal form	PSYCHIC
        50	150	50	150	50	150	600
         386	Deoxys
        Attack form	PSYCHIC
        50	180	20	180	20	150	600
         386	Deoxys
        Defense form	PSYCHIC
        50	70	160	70	160	90	600
         386	Deoxys
        Speed form	PSYCHIC
        50	95	90	95	90	180	600
         387	Turtwig	GRASS
        55	68	64	45	55	31	318
         388	Grotle	GRASS
        75	89	85	55	65	36	405
         389	Torterra	GRASS
        GROUND	95	109	105	75	85	56	525
         390	Chimchar	FIRE
        44	58	44	58	44	61	309
         391	Monferno	FIRE
        FIGHTING	64	78	52	78	52	81	405
         392	Infernape	FIRE
        FIGHTING	76	104	71	104	71	108	534
         393	Piplup	WATER
        53	51	53	61	56	40	314
         394	Prinplup	WATER
        64	66	68	81	76	50	405
         395	Empoleon	WATER
        STEEL	84	86	88	111	101	60	530
         396	Starly	NORMAL
        FLYING	40	55	30	30	30	60	245
         397	Staravia	NORMAL
        FLYING	55	75	50	40	40	80	340
         398	Staraptor	NORMAL
        FLYING	85	120	70	50	50	100	475
         399	Bidoof	NORMAL
        59	45	40	35	40	31	250
         400	Bibarel	NORMAL
        WATER	79	85	60	55	60	71	410
         401	Kricketot	BUG
        37	25	41	25	41	25	194
         402	Kricketune	BUG
        77	85	51	55	51	65	384
         403	Shinx	ELECTRIC
        45	65	34	40	34	45	263
         404	Luxio	ELECTRIC
        60	85	49	60	49	60	363
         405	Luxray	ELECTRIC
        80	120	79	95	79	70	523
         406	Budew	GRASS
        POISON	40	30	35	50	70	55	280
         407	Roserade	GRASS
        POISON	60	70	55	125	105	90	505
         408	Cranidos	ROCK
        67	125	40	30	30	58	350
         409	Rampardos	ROCK
        97	165	60	65	50	58	495
         410	Shieldon	ROCK
        STEEL	30	42	118	42	88	30	350
         411	Bastiodon	ROCK
        STEEL	60	52	168	47	138	30	495
         412	Burmy	BUG
        40	29	45	29	45	36	224
         413	Wormadam
        Plant Cloak form	BUG
        GRASS	60	59	85	79	105	36	424
         413	Wormadam
        Sandy Cloak form	BUG
        GROUND	60	79	105	59	85	36	424
         413	Wormadam
        Trash Cloak form	BUG
        STEEL	60	69	95	69	95	36	424
         414	Mothim	BUG
        FLYING	70	94	50	94	50	66	424
         415	Combee	BUG
        FLYING	30	30	42	30	42	70	244
         416	Vespiquen	BUG
        FLYING	70	80	102	80	102	40	474
         417	Pachirisu	ELECTRIC
        60	45	70	45	90	95	405
         418	Buizel	WATER
        55	65	35	60	30	85	330
         419	Floatzel	WATER
        85	105	55	85	50	115	495
         420	Cherubi	GRASS
        45	35	45	62	53	35	275
         421	Cherrim	GRASS
        70	60	70	87	78	85	450
         422	Shellos	WATER
        76	48	48	57	62	34	325
         423	Gastrodon	WATER
        GROUND	111	83	68	92	82	39	475
         424	Ambipom	NORMAL
        75	100	66	60	66	115	482
         425	Drifloon	GHOST
        FLYING	90	50	34	60	44	70	348
         426	Drifblim	GHOST
        FLYING	150	80	44	90	54	80	498
         427	Buneary	NORMAL
        55	66	44	44	56	85	350
         428	Lopunny	NORMAL
        65	76	84	54	96	105	480
         429	Mismagius	GHOST
        60	60	60	105	105	105	495
         430	Honchkrow	DARK
        FLYING	100	125	52	105	52	71	505
         431	Glameow	NORMAL
        49	55	42	42	37	85	310
         432	Purugly	NORMAL
        71	82	64	64	59	112	452
         433	Chingling	PSYCHIC
        45	30	50	65	50	45	285
         434	Stunky	POISON
        DARK	63	63	47	41	41	74	329
         435	Skuntank	POISON
        DARK	103	93	67	71	61	84	479
         436	Bronzor	STEEL
        PSYCHIC	57	24	86	24	86	23	300
         437	Bronzong	STEEL
        PSYCHIC	67	89	116	79	116	33	500
         438	Bonsly	ROCK
        50	80	95	10	45	10	290
         439	Mime Jr.	PSYCHIC
        20	25	45	70	90	60	310
         440	Happiny	NORMAL
        100	5	5	15	65	30	220
         441	Chatot	NORMAL
        FLYING	76	65	45	92	42	91	411
         442	Spiritomb	GHOST
        DARK	50	92	108	92	108	35	485
         443	Gible	DRAGON
        GROUND	58	70	45	40	45	42	300
         444	Gabite	DRAGON
        GROUND	68	90	65	50	55	82	410
         445	Garchomp	DRAGON
        GROUND	108	130	95	80	85	102	600
         446	Munchlax	NORMAL
        135	85	40	40	85	5	390
         447	Riolu	FIGHTING
        40	70	40	35	40	60	285
         448	Lucario	FIGHTING
        STEEL	70	110	70	115	70	90	525
         449	Hippopotas	GROUND
        68	72	78	38	42	32	330
         450	Hippowdon	GROUND
        108	112	118	68	72	47	525
         451	Skorupi	POISON
        BUG	40	50	90	30	55	65	330
         452	Drapion	POISON
        DARK	70	90	110	60	75	95	500
         453	Croagunk	POISON
        FIGHTING	48	61	40	61	40	50	300
         454	Toxicroak	POISON
        FIGHTING	83	106	65	86	65	85	490
         455	Carnivine	GRASS
        74	100	72	90	72	46	454
         456	Finneon	WATER
        49	49	56	49	61	66	330
         457	Lumineon	WATER
        69	69	76	69	86	91	460
         458	Mantyke	WATER
        FLYING	45	20	50	60	120	50	345
         459	Snover	GRASS
        ICE	60	62	50	62	60	40	334
         460	Abomasnow	GRASS
        ICE	90	92	75	92	85	60	494
         461	Weavile	DARK
        ICE	70	120	65	45	85	125	510
         462	Magnezone	ELECTRIC
        STEEL	70	70	115	130	90	60	535
         463	Lickilicky	NORMAL
        110	85	95	80	95	50	515
         464	Rhyperior	GROUND
        ROCK	115	140	130	55	55	40	535
         465	Tangrowth	GRASS
        100	100	125	110	50	50	535
         466	Electivire	ELECTRIC
        75	123	67	95	85	95	540
         467	Magmortar	FIRE
        75	95	67	125	95	83	540
         468	Togekiss	NORMAL
        FLYING	85	50	95	120	115	80	545
         469	Yanmega	BUG
        FLYING	86	76	86	116	56	95	515
         470	Leafeon	GRASS
        65	110	130	60	65	95	525
         471	Glaceon	ICE
        65	60	110	130	95	65	525
         472	Gliscor	GROUND
        FLYING	75	95	125	45	75	95	510
         473	Mamoswine	ICE
        GROUND	110	130	80	70	60	80	530
         474	Porygon-Z	NORMAL
        85	80	70	135	75	90	535
         475	Gallade	PSYCHIC
        FIGHTING	68	125	65	65	115	80	518
         476	Probopass	ROCK
        STEEL	60	55	145	75	150	40	525
         477	Dusknoir	GHOST
        45	100	135	65	135	45	525
         478	Froslass	ICE
        GHOST	70	80	70	80	70	110	480
         479	Rotom
        Normal form	ELECTRIC
        GHOST	50	50	77	95	77	91	440
         479	Rotom
        Heat form	ELECTRIC
        FIRE	50	65	107	105	107	86	520
         479	Rotom
        Wash form	ELECTRIC
        WATER	50	65	107	105	107	86	520
         479	Rotom
        Frost form	ELECTRIC
        ICE	50	65	107	105	107	86	520
         479	Rotom
        Fan form	ELECTRIC
        FLYING	50	65	107	105	107	86	520
         479	Rotom
        Mow form	ELECTRIC
        GRASS	50	65	107	105	107	86	520
         480	Uxie	PSYCHIC
        75	75	130	75	130	95	580
         481	Mesprit	PSYCHIC
        80	105	105	105	105	80	580
         482	Azelf	PSYCHIC
        75	125	70	125	70	115	580
         483	Dialga	STEEL
        DRAGON	100	120	120	150	100	90	680
         484	Palkia	WATER
        DRAGON	90	120	100	150	120	100	680
         485	Heatran	FIRE
        STEEL	91	90	106	130	106	77	600
         486	Regigigas	NORMAL
        110	160	110	80	110	100	670
         487	Giratina
        Altered form	GHOST
        DRAGON	150	100	120	100	120	90	680
         487	Giratina
        Origin form	GHOST
        DRAGON	150	120	100	120	100	90	680
         488	Cresselia	PSYCHIC
        120	70	120	75	130	85	600
         489	Phione	WATER
        80	80	80	80	80	80	480
         490	Manaphy	WATER
        100	100	100	100	100	100	600
         491	Darkrai	DARK
        70	90	90	135	90	125	600
         492	Shaymin
        Land form	GRASS
        100	100	100	100	100	100	600
         492	Shaymin
        Sky form	GRASS
        FLYING	100	103	75	120	75	127	600
         493	Arceus	NORMAL
        120	120	120	120	120	120	720
         494	Victini	PSYCHIC
        FIRE	100	100	100	100	100	100	600
         495	Snivy	GRASS
        45	45	55	45	55	63	308
         496	Servine	GRASS
        60	60	75	60	75	83	413
         497	Serperior	GRASS
        75	75	95	75	95	113	528
         498	Tepig	FIRE
        65	63	45	45	45	45	308
         499	Pignite	FIRE
        FIGHTING	90	93	55	70	55	55	418
         500	Emboar	FIRE
        FIGHTING	110	123	65	100	65	65	528
         501	Oshawott	WATER
        55	55	45	63	45	45	308
         502	Dewott	WATER
        75	75	60	83	60	60	413
         503	Samurott	WATER
        95	100	85	108	70	70	528
         504	Patrat	NORMAL
        45	55	39	35	39	42	255
         505	Watchog	NORMAL
        60	85	69	60	69	77	420
         506	Lillipup	NORMAL
        45	60	45	25	45	55	275
         507	Herdier	NORMAL
        65	80	65	35	65	60	370
         508	Stoutland	NORMAL
        85	100	90	45	90	80	490
         509	Purrloin	DARK
        41	50	37	50	37	66	281
         510	Liepard	DARK
        64	88	50	88	50	106	446
         511	Pansage	GRASS
        50	53	48	53	48	64	316
         512	Simisage	GRASS
        75	98	63	98	63	101	498
         513	Pansear	FIRE
        50	53	48	53	48	64	316
         514	Simisear	FIRE
        75	98	63	98	63	101	498
         515	Panpour	WATER
        50	53	48	53	48	64	316
         516	Simipour	WATER
        75	98	63	98	63	101	498
         517	Munna	PSYCHIC
        76	25	45	67	55	24	292
         518	Musharna	PSYCHIC
        116	55	85	107	95	29	487
         519	Pidove	NORMAL
        FLYING	50	55	50	36	30	43	264
         520	Tranquill	NORMAL
        FLYING	62	77	62	50	42	65	358
         521	Unfezant	NORMAL
        FLYING	80	105	80	65	55	93	478
         522	Blitzle	ELECTRIC
        45	60	32	50	32	76	295
         523	Zebstrika	ELECTRIC
        75	100	63	80	63	116	497
         524	Roggenrola	ROCK
        55	75	85	25	25	15	280
         525	Boldore	ROCK
        70	105	105	50	40	20	390
         526	Gigalith	ROCK
        85	135	130	60	70	25	505
         527	Woobat	PSYCHIC
        FLYING	55	45	43	55	43	72	313
         528	Swoobat	PSYCHIC
        FLYING	67	57	55	77	55	114	425
         529	Drilbur	GROUND
        60	85	40	30	45	68	328
         530	Excadrill	GROUND
        STEEL	110	135	60	50	65	88	508
         531	Audino	NORMAL
        103	60	86	60	86	50	445
         532	Timburr	FIGHTING
        75	80	55	25	35	35	305
         533	Gurdurr	FIGHTING
        85	105	85	40	50	40	405
         534	Conkeldurr	FIGHTING
        105	140	95	55	65	45	505
         535	Tympole	WATER
        50	50	40	50	40	64	294
         536	Palpitoad	WATER
        GROUND	75	65	55	65	55	69	384
         537	Seismitoad	WATER
        GROUND	105	85	75	85	75	74	499
         538	Throh	FIGHTING
        120	100	85	30	85	45	465
         539	Sawk	FIGHTING
        75	125	75	30	75	85	465
         540	Sewaddle	BUG
        GRASS	45	53	70	40	60	42	310
         541	Swadloon	BUG
        GRASS	55	63	90	50	80	42	380
         542	Leavanny	BUG
        GRASS	75	103	80	70	70	92	490
         543	Venipede	BUG
        POISON	30	45	59	30	39	57	260
         544	Whirlipede	BUG
        POISON	40	55	99	40	79	47	360
         545	Scolipede	BUG
        POISON	60	90	89	55	69	112	475
         546	Cottonee	GRASS
        40	27	60	37	50	66	280
         547	Whimsicott	GRASS
        60	67	85	77	75	116	480
         548	Petilil	GRASS
        45	35	50	70	50	30	280
         549	Lilligant	GRASS
        70	60	75	110	75	90	480
         550	Basculin	WATER
        70	92	65	80	55	98	460
         551	Sandile	GROUND
        DARK	50	72	35	35	35	65	292
         552	Krokorok	GROUND
        DARK	60	82	45	45	45	74	351
         553	Krookodile	GROUND
        DARK	95	117	70	65	70	92	509
         554	Darumaka	FIRE
        70	90	45	15	45	50	315
         555	Darmanitan
        Standard Mode form	FIRE
        105	140	55	30	55	95	480
         555	Darmanitan
        Zen Mode form	FIRE
        PSYCHIC	105	30	105	140	105	55	540
         556	Maractus	GRASS
        75	86	67	106	67	60	461
         557	Dwebble	BUG
        ROCK	50	65	85	35	35	55	325
         558	Crustle	BUG
        ROCK	70	95	125	65	75	45	475
         559	Scraggy	DARK
        FIGHTING	50	75	70	35	70	48	348
         560	Scrafty	DARK
        FIGHTING	65	90	115	45	115	58	488
         561	Sigilyph	PSYCHIC
        FLYING	72	58	80	103	80	97	490
         562	Yamask	GHOST
        38	30	85	55	65	30	303
         563	Cofagrigus	GHOST
        58	50	145	95	105	30	483
         564	Tirtouga	WATER
        ROCK	54	78	103	53	45	22	355
         565	Carracosta	WATER
        ROCK	74	108	133	83	65	32	495
         566	Archen	ROCK
        FLYING	55	112	45	74	45	70	401
         567	Archeops	ROCK
        FLYING	75	140	65	112	65	110	567
         568	Trubbish	POISON
        50	50	62	40	62	65	329
         569	Garbodor	POISON
        80	95	82	60	82	75	474
         570	Zorua	DARK
        40	65	40	80	40	65	330
         571	Zoroark	DARK
        60	105	60	120	60	105	510
         572	Minccino	NORMAL
        55	50	40	40	40	75	300
         573	Cinccino	NORMAL
        75	95	60	65	60	115	470
         574	Gothita	PSYCHIC
        45	30	50	55	65	45	290
         575	Gothorita	PSYCHIC
        60	45	70	75	85	55	390
         576	Gothitelle	PSYCHIC
        70	55	95	95	110	65	490
         577	Solosis	PSYCHIC
        45	30	40	105	50	20	290
         578	Duosion	PSYCHIC
        65	40	50	125	60	30	370
         579	Reuniclus	PSYCHIC
        110	65	75	125	85	30	490
         580	Ducklett	WATER
        FLYING	62	44	50	44	50	55	305
         581	Swanna	WATER
        FLYING	75	87	63	87	63	98	473
         582	Vanillite	ICE
        36	50	50	65	60	44	305
         583	Vanillish	ICE
        51	65	65	80	75	59	395
         584	Vanilluxe	ICE
        71	95	85	110	95	79	535
         585	Deerling	NORMAL
        GRASS	60	60	50	40	50	75	335
         586	Sawsbuck	NORMAL
        GRASS	80	100	70	60	70	95	475
         587	Emolga	ELECTRIC
        FLYING	55	75	60	75	60	103	428
         588	Karrablast	BUG
        50	75	45	40	45	60	315
         589	Escavalier	BUG
        STEEL	70	135	105	60	105	20	495
         590	Foongus	GRASS
        POISON	69	55	45	55	55	15	294
         591	Amoonguss	GRASS
        POISON	114	85	70	85	80	30	464
         592	Frillish	WATER
        GHOST	55	40	50	65	85	40	335
         593	Jellicent	WATER
        GHOST	100	60	70	85	105	60	480
         594	Alomomola	WATER
        165	75	80	40	45	65	470
         595	Joltik	BUG
        ELECTRIC	50	47	50	57	50	65	319
         596	Galvantula	BUG
        ELECTRIC	70	77	60	97	60	108	472
         597	Ferroseed	GRASS
        STEEL	44	50	91	24	86	10	305
         598	Ferrothorn	GRASS
        STEEL	74	94	131	54	116	20	489
         599	Klink	STEEL
        40	55	70	45	60	30	300
         600	Klang	STEEL
        60	80	95	70	85	50	440
         601	Klinklang	STEEL
        60	100	115	70	85	90	520
         602	Tynamo	ELECTRIC
        35	55	40	45	40	60	275
         603	Eelektrik	ELECTRIC
        65	85	70	75	70	40	405
         604	Eelektross	ELECTRIC
        85	115	80	105	80	50	515
         605	Elgyem	PSYCHIC
        55	55	55	85	55	30	335
         606	Beheeyem	PSYCHIC
        75	75	75	125	95	40	485
         607	Litwick	GHOST
        FIRE	50	30	55	65	55	20	275
         608	Lampent	GHOST
        FIRE	60	40	60	95	60	55	370
         609	Chandelure	GHOST
        FIRE	60	55	90	145	90	80	520
         610	Axew	DRAGON
        46	87	60	30	40	57	320
         611	Fraxure	DRAGON
        66	117	70	40	50	67	410
         612	Haxorus	DRAGON
        76	147	90	60	70	97	540
         613	Cubchoo	ICE
        55	70	40	60	40	40	305
         614	Beartic	ICE
        95	110	80	70	80	50	485
         615	Cryogonal	ICE
        70	50	30	95	135	105	485
         616	Shelmet	BUG
        50	40	85	40	65	25	305
         617	Accelgor	BUG
        80	70	40	100	60	145	495
         618	Stunfisk	ELECTRIC
        GROUND	109	66	84	81	99	32	471
         619	Mienfoo	FIGHTING
        45	85	50	55	50	65	350
         620	Mienshao	FIGHTING
        65	125	60	95	60	105	510
         621	Druddigon	DRAGON
        77	120	90	60	90	48	485
         622	Golett	GROUND
        GHOST	59	74	50	35	50	35	303
         623	Golurk	GROUND
        GHOST	89	124	80	55	80	55	483
         624	Pawniard	DARK
        STEEL	45	85	70	40	40	60	340
         625	Bisharp	DARK
        STEEL	65	125	100	60	70	70	490
         626	Bouffalant	NORMAL
        95	110	95	40	95	55	490
         627	Rufflet	NORMAL
        FLYING	70	83	50	37	50	60	350
         628	Braviary	NORMAL
        FLYING	100	123	75	57	75	80	510
         629	Vullaby	DARK
        FLYING	70	55	75	45	65	60	370
         630	Mandibuzz	DARK
        FLYING	110	65	105	55	95	80	510
         631	Heatmor	FIRE
        85	97	66	105	66	65	484
         632	Durant	BUG
        STEEL	58	109	112	48	48	109	484
         633	Deino	DARK
        DRAGON	52	65	50	45	50	38	300
         634	Zweilous	DARK
        DRAGON	72	85	70	65	70	58	420
         635	Hydreigon	DARK
        DRAGON	92	105	90	125	90	98	600
         636	Larvesta	BUG
        FIRE	55	85	55	50	55	60	360
         637	Volcarona	BUG
        FIRE	85	60	65	135	105	100	550
         638	Cobalion	STEEL
        FIGHTING	91	90	129	90	72	108	580
         639	Terrakion	ROCK
        FIGHTING	91	129	90	72	90	108	580
         640	Virizion	GRASS
        FIGHTING	91	90	72	90	129	108	580
         641	Tornadus
        Incarnate form	FLYING
        79	115	70	125	80	111	580
         641	Tornadus
        Therian form	FLYING
        79	100	80	110	90	121	580
         642	Thundurus
        Incarnate form	ELECTRIC
        FLYING	79	115	70	125	80	111	580
         642	Thundurus
        Therian form	ELECTRIC
        FLYING	79	105	70	145	80	101	580
         643	Reshiram	DRAGON
        FIRE	100	120	100	150	120	90	680
         644	Zekrom	DRAGON
        ELECTRIC	100	150	120	120	100	90	680
         645	Landorus
        Incarnate form	GROUND
        FLYING	89	125	90	115	80	101	600
         645	Landorus
        Therian form	GROUND
        FLYING	89	145	90	105	80	91	600
         646	Kyurem
        Normal form	DRAGON
        ICE	125	130	90	130	90	95	660
         646	Kyurem
        White Kyurem form	DRAGON
        ICE	125	120	90	170	100	95	700
         646	Kyurem
        Black Kyurem form	DRAGON
        ICE	125	170	100	120	90	95	700
         647	Keldeo
        Usual form	WATER
        FIGHTING	91	72	90	129	90	108	580
         647	Keldeo
        Resolution form	WATER
        FIGHTING	91	72	90	129	90	108	580
         648	Meloetta
        Aria form	NORMAL
        PSYCHIC	100	77	77	128	128	90	600
         648	Meloetta
        Pirouette form	NORMAL
        FIGHTING	100	128	90	77	77	128	600
         649	Genesect	BUG
        STEEL	71	120	95	120	95	99	600


        '''

        def modifyText(string):
            newStr = ""

            for char in string:
                if 32 <= ord(char) <= 126 or char in '♀♂' :
                    newStr+=char
                else:
                    newStr+=' '

            return newStr

        def removeReferences(string):

            stack = []

            newStr = ""

            for char in string:
                if char == "[":
                    stack.append(char)

                if len(stack)==0:
                    newStr+=char
                
                if char == "]":
                    stack.pop()

            return newStr

        def prossesText():


            NOR = "NORMAL"
            FIR = "FIRE"
            WAT = "WATER"
            ELE = "ELECTRIC"
            GRA = "GRASS"
            ICE = "ICE"
            FIG = "FIGHTING"
            POI = "POISON"
            GRO = "GROUND"
            FLY = "FLYING"
            PSY = "PSYCHIC"
            BUG = "BUG"
            ROC = "ROCK"
            GHO = "GHOST"
            DRA = "DRAGON"
            DAR = "DARK"
            STE = "STEEL"
            
            typeList = (NOR,FIR,WAT,ELE,GRA,ICE,FIG,POI,GRO,FLY,PSY,BUG,ROC,GHO,DRA,DAR,STE)
            
            nTextList = list(NationalText.split() )
            nTextList.reverse()
            
            POKEDEX = self.__pokedex

            count=0




            while( len(nTextList)!=0 ):

                tempList = []
                tempStr = ""
                name = ""
                name2 = ""

                # index
                tempList.append( nTextList.pop() )
                # name

                name = nTextList.pop()
                
                tempStr = nTextList.pop()

                name2 = "("

                while not tempStr in typeList:
                    name2 += tempStr
                
                    tempStr = nTextList.pop()

                name2 += ")"

                if len(name2) > 2 :
                    tempList.append( name + " " + name2 )
                else:
                    tempList.append( name  )


                # type1
                tempList.append( tempStr  )

                
                tempStr = nTextList.pop()

                if( tempStr in typeList):
                    
                    tempList.append( tempStr )
                    
                    tempList.append( nTextList.pop() ) 
                    tempList.append( nTextList.pop() )
                    
                    tempList.append( nTextList.pop() )
                    tempList.append( nTextList.pop() )
                    
                    tempList.append( nTextList.pop() )
                    tempList.append( nTextList.pop() )
                    tempList.append( nTextList.pop() )            

                else:

                    tempList.append( "" )
            
                    tempList.append( tempStr )
                    tempList.append( nTextList.pop() )
                    
                    tempList.append( nTextList.pop() )
                    tempList.append( nTextList.pop() )
                    tempList.append( nTextList.pop() )
                    
                    tempList.append( nTextList.pop() )
                    tempList.append( nTextList.pop() )

                POKEDEX.append( Pokemon(tempList) )

                count+=1
                
        NationalText = modifyText(NationalText)
        prossesText()
        

def getIndex(string):

    string = string.strip()
    string = string.lower()

    if len(string)>1:

        if string[0]== 'n' and string in 'normal':
            index = 0
        elif string[0]== 'f' and string in 'fire' :
            index = 1
        elif string[0]== 'w' and string in 'water' :
            index = 2
        elif string[0]== 'e' and string in 'electric' :
            index = 3
        elif string[0]== 'g' and string in 'grass':
            index = 4
        elif string[0]== 'i' and string in 'ice' :
            index = 5
        elif string[0]== 'f' and string in 'fighting' :
            index = 6
        elif string[0]== 'p' and string in 'poison' :
            index = 7
        elif string[0]== 'g' and string in 'ground':
            index = 8
        elif string[0]== 'f' and string in 'flying':
            index = 9
        elif string[0]== 'p' and string in 'psychic':
            index = 10
        elif string[0]== 'b' and string in 'bug' :
            index = 11
        elif string[0]== 'r' and string in 'rock':
            index = 12
        elif string[0]== 'g' and string in 'ghost':
            index = 13
        elif string[0]== 'd' and string in 'dragon':
            index = 14
        elif string[0]== 'd' and string in 'dark':
            index = 15
        elif string[0]== 's' and string in 'steel':
            index = 16
        else:
            raise Exception("Did not enter in correct type name for arg of getIndex")
    else:
        raise Exception("Did not enter in correct type name for arg of getIndex")

    return index


def make():
    global TOL
    global NUM_TYPES 
    global TYPELIST
    global WORDLIST
    global TYPECHART 
    global DUALCHART
    global PKMNTYPELIST
    global NUMPKMNCHART
    global WEAKCHART 
    global RESISTCHART

    global POKEDEX

    def makeTypeList():
        NOR = "NOR"
        FIR = "FIR"
        WAT = "WAT"
        ELE = "ELE"
        GRA = "GRA"
        ICE = "ICE"
        FIG = "FIG"
        POI = "POI"
        GRO = "GRO"
        FLY = "FLY"
        PSY = "PSY"
        BUG = "BUG"
        ROC = "ROC"
        GHO = "GHO"
        DRA = "DRA"
        DAR = "DAR"
        STE = "STE"

        TYPELIST = (NOR,FIR,WAT,ELE,GRA,ICE,FIG,POI,GRO,FLY,PSY,BUG,ROC,GHO,DRA,DAR,STE)

        return TYPELIST

    def makeWordTypeList():
        NOR = "NORMAL"
        FIR = "FIRE"
        WAT = "WATER"
        ELE = "ELECTRIC"
        GRA = "GRASS"
        ICE = "ICE"
        FIG = "FIGHTING"
        POI = "POISON"
        GRO = "GROUND"
        FLY = "FLYING"
        PSY = "PSYCHIC"
        BUG = "BUG"
        ROC = "ROCK"
        GHO = "GHOST"
        DRA = "DRAGON"
        DAR = "DARK"
        STE = "STEEL"
        
        typeList = (NOR,FIR,WAT,ELE,GRA,ICE,FIG,POI,GRO,FLY,PSY,BUG,ROC,GHO,DRA,DAR,STE)

        return typeList


    def makeIntZeroesList(num):
        thisList = []

        for i in range(num):
            thisList.append(0)

        return thisList
    

    def makeFloatOnesList(num):
        thisList = []

        for i in range(num):
            thisList.append(1.0)

        return thisList

    def makeTypeChart():
        # Setting weaknesses and resistances

        nor = makeFloatOnesList(NUM_TYPES)
        fir = makeFloatOnesList(NUM_TYPES)
        wat = makeFloatOnesList(NUM_TYPES)
        ele = makeFloatOnesList(NUM_TYPES)
        gra = makeFloatOnesList(NUM_TYPES)
        ice = makeFloatOnesList(NUM_TYPES)
        fig = makeFloatOnesList(NUM_TYPES)
        poi = makeFloatOnesList(NUM_TYPES)
        gro = makeFloatOnesList(NUM_TYPES)
        fly = makeFloatOnesList(NUM_TYPES)
        psy = makeFloatOnesList(NUM_TYPES)
        bug = makeFloatOnesList(NUM_TYPES)
        roc = makeFloatOnesList(NUM_TYPES)
        gho = makeFloatOnesList(NUM_TYPES)
        dra = makeFloatOnesList(NUM_TYPES)
        dar = makeFloatOnesList(NUM_TYPES)
        ste = makeFloatOnesList(NUM_TYPES)

        resist = 0.5
        weak = 2.0
        immune = 0.0

        # atk_Type[ Def_type ] = multiplyer

        nor[getIndex("roc")] = resist
        nor[getIndex("gho")] = immune
        nor[getIndex("ste")] = resist

        fir[getIndex("fir")] = resist
        fir[getIndex("wat")] = resist
        fir[getIndex("gra")] = weak
        fir[getIndex("ice")] = weak
        fir[getIndex("bug")] = weak
        fir[getIndex("roc")] = resist
        fir[getIndex("dra")] = resist
        fir[getIndex("ste")] = weak

        wat[getIndex("fir")] = weak
        wat[getIndex("wat")] = resist
        wat[getIndex("gra")] = resist
        wat[getIndex("gro")] = weak
        wat[getIndex("roc")] = weak
        wat[getIndex("dra")] = resist

        ele[getIndex("wat")] = weak
        ele[getIndex("ele")] = resist
        ele[getIndex("gra")] = resist
        ele[getIndex("gro")] = immune
        ele[getIndex("fly")] = weak
        ele[getIndex("dra")] = resist

        gra[getIndex("fir")] = resist
        gra[getIndex("wat")] = weak
        gra[getIndex("gra")] = resist
        gra[getIndex("poi")] = resist
        gra[getIndex("gro")] = weak
        gra[getIndex("fly")] = resist
        gra[getIndex("bug")] = resist
        gra[getIndex("roc")] = weak
        gra[getIndex("dra")] = resist
        gra[getIndex("ste")] = resist

        ice[getIndex("fir")] = resist
        ice[getIndex("wat")] = resist
        ice[getIndex("gra")] = weak
        ice[getIndex("ice")] = resist
        ice[getIndex("gro")] = weak
        ice[getIndex("fly")] = weak
        ice[getIndex("dra")] = weak
        ice[getIndex("ste")] = resist

        fig[getIndex("nor")] = weak
        fig[getIndex("ice")] = weak
        fig[getIndex("poi")] = resist
        fig[getIndex("fly")] = resist
        fig[getIndex("psy")] = resist
        fig[getIndex("bug")] = resist
        fig[getIndex("roc")] = weak
        fig[getIndex("gho")] = immune
        fig[getIndex("dar")] = weak
        fig[getIndex("ste")] = weak

        poi[getIndex("gra")] = weak
        poi[getIndex("poi")] = weak
        poi[getIndex("gro")] = resist
        poi[getIndex("roc")] = resist
        poi[getIndex("gho")] = resist
        poi[getIndex("ste")] = immune

        gro[getIndex("fir")] = weak
        gro[getIndex("gra")] = weak
        gro[getIndex("ele")] = weak
        gro[getIndex("gra")] = resist
        gro[getIndex("poi")] = weak
        gro[getIndex("fly")] = immune
        gro[getIndex("bug")] = resist
        gro[getIndex("roc")] = weak
        gro[getIndex("ste")] = weak

        fly[getIndex("ele")] = resist
        fly[getIndex("gra")] = weak
        fly[getIndex("fig")] = weak
        fly[getIndex("bug")] = weak
        fly[getIndex("roc")] = resist
        fly[getIndex("ste")] = resist

        psy[getIndex("fig")] = weak
        psy[getIndex("poi")] = weak
        psy[getIndex("psy")] = resist
        psy[getIndex("dar")] = immune
        psy[getIndex("ste")] = resist

        bug[getIndex("fir")] = resist
        bug[getIndex("gra")] = weak
        bug[getIndex("fig")] = resist
        bug[getIndex("poi")] = resist
        bug[getIndex("fly")] = resist
        bug[getIndex("psy")] = weak
        bug[getIndex("gho")] = resist
        bug[getIndex("dar")] = weak
        bug[getIndex("ste")] = resist

        roc[getIndex("fir")] = weak
        roc[getIndex("ice")] = weak
        roc[getIndex("fig")] = resist
        roc[getIndex("gro")] = resist
        roc[getIndex("fly")] = weak
        roc[getIndex("bug")] = weak
        roc[getIndex("ste")] = resist

        gho[getIndex("nor")] = immune
        gho[getIndex("psy")] = weak
        gho[getIndex("gho")] = weak
        gho[getIndex("dar")] = resist
        gho[getIndex("ste")] = resist

        dra[getIndex("dra")] = weak
        dra[getIndex("ste")] = resist

        dar[getIndex("fig")] = resist
        dar[getIndex("psy")] = weak
        dar[getIndex("gho")] = weak
        dar[getIndex("dar")] = resist
        dar[getIndex("ste")] = resist

        ste[getIndex("fir")] = resist
        ste[getIndex("wat")] = resist
        ste[getIndex("ele")] = resist
        ste[getIndex("ice")] = weak
        ste[getIndex("roc")] = weak
        ste[getIndex("ste")] = resist

        nor = tuple(nor)
        fir = tuple(fir)
        wat = tuple(wat)
        ele = tuple(ele)
        gra = tuple(gra)
        ice = tuple(ice)
        fig = tuple(fig)
        poi = tuple(poi)
        gro = tuple(gro)
        fly = tuple(fly)
        psy = tuple(psy)
        bug = tuple(bug)
        roc = tuple(roc)
        gho = tuple(gho)
        dra = tuple(dra)
        dar = tuple(dar)
        ste = tuple(ste)

        # ATK X DEF
        TYPECHART = (nor,fir,wat,ele,gra,ice,fig,poi,gro,fly,psy,bug,roc,gho,dra,dar,ste)

        return TYPECHART
    

    def transpose(array):
        newArray = []
        for i in range(len(array) ):
            newArray.append(makeFloatOnesList( len(array[i]) ))

        for i in range(len(newArray) ):
            for j in range(len(newArray[i])):
                newArray[i][j]=array[j][i]

        for i in range( len(newArray) ):
            newArray[i] = tuple(newArray[i])

        newArray = tuple(newArray)

        return newArray


    def rowMultiply(list1,list2):
        newRow = []
        
        size = len(list1)

        if size==len(list2):
            newRow = makeFloatOnesList( size )
            for i in range( size ):
                newRow[i] = list1[i]*list2[i]
                
            newRow = tuple(newRow)           
        else:
            raise Exception("Error in rowMultiply. Size of the two lists do not match")

        return newRow
                

    def makeDuelTypeChart():

        TYPECHART_T = transpose(TYPECHART)
        
        # DEF TYPE1 X DEF TYPE2 X ATK
        DUALCHART = []

        for i in range(NUM_TYPES):
            tempList = []
            for j in range(NUM_TYPES):
                if i!=j:
                    tempList.append(rowMultiply(TYPECHART_T[i],TYPECHART_T[j]) )
                else:
                    tempList.append(TYPECHART_T[i])
                    
            tempList = tuple(tempList)
            DUALCHART.append(tempList)
                       
        DUALCHART = tuple(DUALCHART)

        return DUALCHART


    def makeNumWeakChart():
        weak = []

        for i in range(NUM_TYPES):
            # this makes int arrays
            weak.append( makeIntZeroesList(NUM_TYPES) )

                    
        for i in range(NUM_TYPES):
            for j in range(NUM_TYPES):
                for k in range(NUM_TYPES):
                    if DUALCHART[i][j][k]>= 2.0-TOL:
                         weak[i][j]+=1

        return weak


    def makeNumResistChart():
        resist = []

        for i in range(NUM_TYPES):
            # this makes int arrays
            resist.append(  makeIntZeroesList(NUM_TYPES) )

                    
        for i in range(NUM_TYPES):
            for j in range(NUM_TYPES):
                for k in range(NUM_TYPES):
                    if DUALCHART[i][j][k]<= 0.5+TOL:
                        resist[i][j]+=1

        return resist

    def makePkmnTypeList():
        typeList = []

        for i in range(NUM_TYPES):
            tempList = []
            for j in range(NUM_TYPES):
                tempList.append( [] )

            typeList.append(tempList)

        for i in range(1,POKEDEX.size() ):
            
            index1 = getIndex( POKEDEX[i].getType1() )

            try:
                index2 = getIndex( POKEDEX[i].getType2() )
            except Exception:
                index2 = index1

            typeList[index1][index2].append( POKEDEX[i] )

        
        for i in range(NUM_TYPES):
            for j in range(NUM_TYPES):
                typeList[i][j] = tuple( typeList[i][j] )

            typeList[i] = tuple( typeList[i] )

        typeList = tuple( typeList )

        return typeList

    def makeNumPkmnChart():
        typeList = []

        for i in range(NUM_TYPES):
            typeList.append(makeIntZeroesList(NUM_TYPES) )

        for i in range( len(typeList) ):
            for j in range( len(typeList[i] ) ):
                if i!=j :
                    typeList[i][j] = len(PKMNTYPELIST[i][j]) + len(PKMNTYPELIST[j][i])
                else:
                    typeList[i][j] = len(PKMNTYPELIST[i][j])

        for i in range( len(typeList) ):
            typeList[i] = tuple( typeList[i] )

        typeList = tuple( typeList )

        return typeList                

            
    TOL = 0.01
    
    NUM_TYPES = 17

    POKEDEX = Pokedex()
    
    TYPELIST = makeTypeList()
    WORDLIST = makeWordTypeList()
    
    TYPECHART = makeTypeChart()
    DUALCHART = makeDuelTypeChart()

    WEAKCHART = makeNumWeakChart()
    RESISTCHART = makeNumResistChart()

    PKMNTYPELIST = makePkmnTypeList()
    NUMPKMNCHART = makeNumPkmnChart()

# end def make():


def printChart(*args):

    print "======================================== SINGLE TYPE CHART ======================================="
    
    print "ATK / DEF"

    text="Type| "

    for typ in TYPELIST:
        text+=typ+"| "
    

    print text

    if len(args) == 0:
        for i in range(NUM_TYPES):
            text="|"
            for j in range(NUM_TYPES):
                if 1-TOL <= TYPECHART[i][j] <= 1+TOL:
                    text+="    |"
                else:
                    text+= "%01.2f|" % TYPECHART[i][j]

            print "%s %s" % (TYPELIST[i],text)
    elif len(args) == 1:
        try:
            text="|"
            i=getIndex(args[0])
            
            for j in range(NUM_TYPES):

                if 1-TOL <= TYPECHART[i][j] <= 1+TOL:
                    text+="    |"
                else:
                    text+= "%01.2f|" % TYPECHART[i][j]

            print "%s %s" % (TYPELIST[i],text)
        except AttributeError:
            print "Did not enter in correct type name"
            
    print "=================================================================================================="



def printDualChart(*args):



    def printDualChartSlice(*args):

        
        if len(args)==1:
        
            i = args[0]

            for k in range(NUM_TYPES):
                text="|"

                text+= "  %02d|" % NUMPKMNCHART[i][k]

                for j in range(NUM_TYPES):

                        multiplier = DUALCHART[i][k][j]

                        if 1-TOL <= multiplier <= 1+TOL:
                            text+="    |"
                        else:
                            text+= "%01.2f|" % multiplier
                                        
                if i==k:
                    print "%s %s %s" % (TYPELIST[i],"---",text)
                else:
                    print "%s %s %s" %(TYPELIST[i],TYPELIST[k],text)
                    
        elif len(args)==2:

            i=args[0]
            k=args[1]

            text="|"

            text+= "  %02d|" % NUMPKMNCHART[i][k]

            for j in range(NUM_TYPES):

                multiplier = DUALCHART[i][k][j]

                if 1-TOL <= multiplier <= 1+TOL:
                    text+="    |"
                else:
                    text+= "%01.2f|" % multiplier
                    
            if i==k:
                print "%s %s %s" % (TYPELIST[i],"---",text)
            else:
                print "%s %s %s" % (TYPELIST[i],TYPELIST[k],text)


        # end def printDualChartSlice(*args)



    bigHeader = "========================================= DUAL TYPE CHART ========================================="
    cloHeader = "==================================================================================================="


    header = ""
    header+= cloHeader
    header+= "\n"
    header+= "Typ/Typ |PKMN|"

    for typ in TYPELIST:
        header+=" "+typ+"|"

    header+= "\n"
    header+= cloHeader    

    if len(args)==0:

        print bigHeader
        print " DEF   / ATK"
        print header
        
        for i in range(NUM_TYPES):
            
            printDualChartSlice(i)
            print header
    elif len(args)==1:
        print bigHeader
        print " DEF   / ATK"
        print header
        try:
            index = getIndex(args[0])
            printDualChartSlice(index)
        except AttributeError:
            print "Did not enter in correct type name"
    elif len(args)==2:
        print header
        try:
            index1 = getIndex(args[0])
            try:
                index2 = getIndex(args[1])
            except AttributeError:
                index2=index1
            printDualChartSlice(index1,index2)
        except AttributeError:
            print "Did not enter in correct type name"

    print cloHeader

# end def printDualChart(*args):


def quicksort(*args):
    if len(args)==1 :
        array = args[0]
        start = 0
        end = len(array)

        quicksort(array,start,end)
        

    elif len(args)==3:
        array = args[0]
        start = args[1]
        end = args[2]
        pivot = (start+end-1)/2
    
        if end-start>1:
            
            pivotValue = array[pivot][2]

            temp = array[pivot]
            array[pivot] = array[end-1]
            array[end-1] = temp

            curIndex = start

            i=start

            while( i<end-1 ):

                if array[i][2]<pivotValue:
                    temp = array[i]
                    array[i] = array[curIndex]
                    array[curIndex] = temp
                    curIndex+=1

                i+=1
                
            temp = array[end-1]
            array[end-1] = array[curIndex]
            array[curIndex] = temp

            quicksort(array,start,curIndex)
            quicksort(array,curIndex+1,end)
    else:
        print "quicksort recived the incorrect number of args"
        raise
            
    

def resistAnalysis(*args):
    print "====================================== RESISTANCE ANALYSIS ======================================="

    if len(args)==0:
        print ""
        print "Number of resistances for type combination"
        print ""

        output = ""
        
        text="Type|"

        for typ in TYPELIST:
            text+=" "+typ+"|"
        

        output += text+"\n"

        for i in range(NUM_TYPES):
            text="|"

            for j in range(NUM_TYPES):
                if WEAKCHART[i][j]!= 0:
                    text+= "  %02d|" % WEAKCHART[i][j]
                else:
                    text+= "    |"

            output +=  ""+TYPELIST[i]+" "+text+"\n"

        print output
        
        maxNum = 0

                    
        for i in range(NUM_TYPES):
            for j in range(NUM_TYPES):
                if RESISTCHART[i][j] >= maxNum:
                    maxNum = RESISTCHART[i][j]

        print ""


        numWeak = []

        for i in range(maxNum+1):
            numWeak.append([])


        for i in range(NUM_TYPES):
            for j in range(NUM_TYPES):
                if i>=j:
                    if i!=j:
                         numWeak[ RESISTCHART[i][j] ].append( (TYPELIST[i],TYPELIST[j],WEAKCHART[i][j]) )
                    else:
                         numWeak[ RESISTCHART[i][j] ].append( (TYPELIST[i],"---",WEAKCHART[i][j]) )
            
        
        for i in range(maxNum):
            quicksort(numWeak[i])

        for i in range(len(numWeak)):
            print "Types with %d resistance(s) sorted by number of weaknesses" % i

            for j in range(len(numWeak[i]) ):

                int1 = getIndex(numWeak[i][j][0])

                try:
                    int2 = getIndex(numWeak[i][j][1])
                except Exception:
                    int2=int1
                
                print "%s %s (%d weaknesses) (%d pokemon exsist)"%(numWeak[i][j][0],numWeak[i][j][1],numWeak[i][j][2],NUMPKMNCHART[int1][int2] )
                                                          
            print ""

    elif( len(args)==1 ):

        resistList = []

        index = getIndex( args[0] )

        resist = 0.5

        for i in range(NUM_TYPES):
            for j in range(NUM_TYPES):
                if i>= j:
                    if DUALCHART[i][j][index] <= resist + TOL:
                        resistList.append( (i,j) )

        print "Here are the type combinations that are resistant or immune to %s" % WORDLIST[index]

        for i in range( len(resistList) ):

            index1 = resistList[i][0]
            index2 = resistList[i][1]

            if index1!=index2:
                print " %s %s (%d pokemon exsist)" %( TYPELIST[index1], TYPELIST[index2], NUMPKMNCHART[index1][index2] )
            else:
                print " %s %s (%d pokemon exsist)" %( TYPELIST[index1], "---", NUMPKMNCHART[index1][index1] )
            

    print "=================================================================================================="
    
    
def weaknessAnalysis(*args):

    print "======================================== WEAKNESS ANALYSIS ======================================="

    if( len(args)==0 ):
        print ""

        print "Number of weaknesses for type combination"
        print ""

        output = ""
        
        text="Type| "

        for typ in TYPELIST:
            text+=typ+"| "
        

        output += text+"\n"

        for i in range(NUM_TYPES):
            text="|"

            for j in range(NUM_TYPES):
                if RESISTCHART[i][j]!= 0:
                    text+= "  %02d|" % RESISTCHART[i][j]
                else:
                    text+= "    |"

            output += TYPELIST[i]+" "+text+"\n"

        print output

        
        
        maxNum = 0

                    
        for i in range(NUM_TYPES):
            for j in range(NUM_TYPES):
                if WEAKCHART[i][j] >= maxNum:
                    maxNum = WEAKCHART[i][j]

        print ""

        numResist = []

        for i in range(maxNum+1):
            numResist.append([])


        for i in range(NUM_TYPES):
            for j in range(NUM_TYPES):
                if i>=j:
                    if i!=j:
                         numResist[ WEAKCHART[i][j] ].append( (TYPELIST[i],TYPELIST[j],RESISTCHART[i][j]) )
                    else:
                         numResist[ WEAKCHART[i][j] ].append( (TYPELIST[i],"---",RESISTCHART[i][j]) )
            
        
        for i in range(maxNum):
            quicksort(numResist[i])

        for i in range(len(numResist)):
            print "Types with %d weeknesse(s) sorted by number of resistances" % i

            for j in range(len(numResist[i]) ):
                int1 = getIndex(numResist[i][j][0])

                try:
                    int2 = getIndex(numResist[i][j][1])
                except Exception:
                    int2=int1
                        
                print "%s %s (%d resist) (%d pokemon exsist)"%(numResist[i][j][0],numResist[i][j][1],numResist[i][j][2],NUMPKMNCHART[int1][int2])
            print ""



    elif( len(args)==1 ):


        weakList = []

        index = getIndex( args[0] )

        weak = 2.0

        for i in range(NUM_TYPES):
            for j in range(NUM_TYPES):
                if i>= j:
                    if DUALCHART[i][j][index] >= weak-TOL:
                        weakList.append( (i,j) )

        print "Here are the type combinations that are weak to %s" % WORDLIST[index]

        for i in range( len(weakList) ):

            index1 = weakList[i][0]
            index2 = weakList[i][1]

            if index1!=index2:
                print " %s %s (%d pokemon exsist)" %( TYPELIST[index1], TYPELIST[index2], NUMPKMNCHART[index1][index2] )
            else:
                print " %s %s (%d pokemon exsist)" %( TYPELIST[index1], "---", NUMPKMNCHART[index1][index1] )


    print "=================================================================================================="


def showAll():
    printChart()
    printDualChart()
    resistAnalysis()
    weaknessAnalysis()

def pleaseHelp():

    text = '''

    List of all functions:

    make
    pleaseHelp
    printChart
    printDualChart
    resistAnalysis
    showAll
    weaknessAnalysis


    List of all type names:

        Normal
        Fire
        Water
        Electric
        Grass
        Ice
        Fighting
        Poison
        Ground
        Flying
        Pshycic
        Bug
        Rock
        Ghost
        Dragon
        Dark
        Steel

    List of classes that are created:
        Pokemon
        Pokedex

    List of important variables (do not modify):

        NUM_TYPES = 17

        TYPELIST
        WORDLIST
        TYPECHART 
        DUALCHART
        PKMNTYPELIST
        NUMPKMNCHART
        WEAKCHART 
        RESISTCHART

        POKEDEX

    Help text for each function:

    make()

        This function will initilize all the global variables.

    pleaseHelp()

        pleaseHelp displays this text that you are reading.

    printChart()
    printChart("type")

        printChart will print the entire single type chart if passed no arguments.

        But if passed a string argunmnet of the type then the function will print
        the row in the type chart that coresponds to an attack of that type.

        Note that the string must contain at least the first two letters of the type
        name and can be as long as the full word. The argunment is NOT case sensitive.

    printDualChart()
    printDualChart("type1")
    printDualChart("type1","type2")

        printDualChart will print the entire dual type chart if passed no arguments.

        But if passed a string argunmnet of the type then the function will print
        a segment of the dual type chart that corresponds to a defending pokemon having
        the passed type.

        If passed two string argunments, both of which are types, then it will print one
        row of the dual type chart corresponding to a defending pokemon with that type
        comination.

        Note that the string must contain at least the first two letters of the type
        name and can be as long as the full word. The argunment is NOT case sensitive.        

    resistAnalysis()
    resistAnalysis("type")

        resistAnalysis will display a chart with rows being the first type on a pokemon
        and the second row being the second type. The entries in the chart are how many
        resistances a pokemon type comination have. Immunities are counted as resistances.
        Then a list is printed of pokemon type comination in order in increasing number of
        resisitances. Within  each section of the list, the type comination are sorted in
        increasing number of weaknesses. You will also get the number of pokemon who have
        each type combination.

        If passed an argunment of a type. Then you will get all the type combinations
        that are resistant to that type. You will also get the number of pokemon who have
        each type combination.

    showAll()

        showAll runs the following functions in the following order:
        
            printChart()
            printDualChart()
            resistAnalysis()
            weaknessAnalysis()

    weaknessAnalysis()
    weaknessAnalysis("type")

        weaknessAnalysis will display a chart with rows being the first type on a pokemon
        and the second row being the second type. The entries in the chart are how many
        weaknesses a pokemon type comination have.
        Then a list is printed of pokemon type comination in order in increasing number of
        weaknesses. Within each section of the list, the type comination are sorted in 
        increasing number of resisitances. You will also get the number of pokemon who have
        each type combination.

        If passed an argunment of a type. Then you will get all the type combinations
        that are weak to that type. You will also get the number of pokemon who have
        each type combination.
    
    '''

    print text


make()
pleaseHelp()


#showAll()
#printChart()
#printChart("Normal")
#printDualChart()
#printDualChart("Normal")
#printDualChart("Normal","Ele")
#resistAnalysis()
#weaknessAnalysis()
