"""This file has a list of article name comparisons and the expected outcome.
These have been individually looked at by a real person to determine the 
expected outcome of each. The current version of NameComparator has a high 
level of accuracy at predicting the expected outcome, though it is not 
perfect."""

articleNames = [
    {
		'name_one': 'a bertram lemon',
		'name_two': 'a. bertram lemon', 
		'expected': True, 
		'description': 'a bertram lemon comparison with article'
	},
    {
		'name_one': 'a c la follette',
		'name_two': 'arthur c. la follette', 
		'expected': True, 
		'description': 'a c la follette comparison with article'
	},
    {
		'name_one': 'a harold lancour',
		'name_two': 'harold lancour', 
		'expected': True, 
		'description': 'a harold lancour comparison with article'
	},
    {
		'name_one': 'a henry detweiler',
		'name_two': 'albert henry detweiler', 
		'expected': True, 
		'description': 'a henry detweiler comparison with article'
	},
    {
		'name_one': 'a laurence mortensen',
		'name_two': 'alfred laurence mortensen', 
		'expected': True, 
		'description': 'a laurence mortensen comparison with article'
	},
    {
		'name_one': 'a lee dunlap',
		'name_two': 'archibald lee dunlap', 
		'expected': True, 
		'description': 'a lee dunlap comparison with article'
	},
    {
		'name_one': 'a leland beam',
		'name_two': 'a. leland beam', 
		'expected': True, 
		'description': 'a leland beam comparison with article'
	},
    {
		'name_one': 'a leo oppenheim',
		'name_two': 'adolf leo oppenheim', 
		'expected': True, 
		'description': 'a leo oppenheim comparison with article'
	},
    {
		'name_one': 'a m de la torre',
		'name_two': 'antonio marcial de la torre', 
		'expected': True, 
		'description': 'a m de la torre comparison with article'
	},
    {
		'name_one': 'a michael deluca',
		'name_two': 'a. michael de luca', 
		'expected': True, 
		'description': 'a michael deluca comparison with article'
	},
    {
		'name_one': 'a willis dearing',
		'name_two': 'a. willis dearing', 
		'expected': True, 
		'description': 'a willis dearing comparison with article'
	},
    {
		'name_one': 'aaron donnelly',
		'name_two': 'aaron van donnelly', 
		'expected': True, 
		'description': 'aaron donnelly comparison with article'
	},
    {
		'name_one': 'abba p lerner',
		'name_two': 'abba p. lerner', 
		'expected': True, 
		'description': 'abba p lerner comparison with article'
	},
    {
		'name_one': 'able levitt',
		'name_two': 'abel levitt', 
		'expected': True, 
		'description': 'able levitt comparison with article'
	},
    {
		'name_one': 'abraham h levy',
		'name_two': 'abraham h. levy', 
		'expected': True, 
		'description': 'abraham h levy comparison with article'
	},
    {
		'name_one': 'abraham levinson',
		'name_two': 'abraham levinson', 
		'expected': True, 
		'description': 'abraham levinson comparison with article'
	},
    {
		'name_one': 'abram l sachar',
		'name_two': 'abram leon sachar', 
		'expected': True, 
		'description': 'abram l sachar comparison with article'
	},
    {
		'name_one': 'abram william vander meer',
		'name_two': 'abram w. vandermeer', 
		'expected': True, 
		'description': 'abram william vander meer comparison with article'
	},
    {
		'name_one': 'ada lee hawkins',
		'name_two': 'ada hawkins', 
		'expected': True, 
		'description': 'ada lee hawkins comparison with article'
	},
    {
		'name_one': 'adah lewis',
		'name_two': 'adah lewis', 
		'expected': True, 
		'description': 'adah lewis comparison with article'
	},
    {
		'name_one': 'addison e lee',
		'name_two': 'addison e. lee', 
		'expected': True, 
		'description': 'addison e lee comparison with article'
	},
    {
		'name_one': 'adelaide e deters',
		'name_two': 'emma e. deters', 
		'expected': False, 
		'description': 'adelaide e deters comparison with article'
	},
    {
		'name_one': 'adelle h land',
		'name_two': 'adelle h. land', 
		'expected': True, 
		'description': 'adelle h land comparison with article'
	},
    {
		'name_one': 'adolph desanctis',
		'name_two': 'adolph g. desanctis', 
		'expected': True, 
		'description': 'adolph desanctis comparison with article'
	},
    {
		'name_one': 'adolph dettloff',
		'name_two': 'adolph mansen dettloff', 
		'expected': True, 
		'description': 'adolph dettloff comparison with article'
	},
    {
		'name_one': 'adolph ladru jensen',
		'name_two': 'adolph ladru jensen', 
		'expected': True, 
		'description': 'adolph ladru jensen comparison with article'
	},
    {
		'name_one': 'adolph leschnitzer',
		'name_two': 'adolf f. leschnitzer', 
		'expected': True, 
		'description': 'adolph leschnitzer comparison with article'
	},
    {
		'name_one': 'adrian r legault',
		'name_two': 'adrian r. legault', 
		'expected': True, 
		'description': 'adrian r legault comparison with article'
	},
    {
		'name_one': 'agnes gregory',
		'name_two': 'agnes lee gregory', 
		'expected': True, 
		'description': 'agnes gregory comparison with article'
	},
    {
		'name_one': 'agnes k michels',
		'name_two': 'agnes kirsopp lake michels', 
		'expected': True, 
		'description': 'agnes k michels comparison with article'
	},
    {
		'name_one': 'agnes m. larson',
		'name_two': 'agnes m. larson', 
		'expected': True, 
		'description': 'agnes m. larson comparison with article'
	},
    {
		'name_one': 'agnes o leindorff',
		'name_two': 'agnes olson leindorff', 
		'expected': True, 
		'description': 'agnes o leindorff comparison with article'
	},
    {
		'name_one': 'alan v mcgee',
		'name_two': 'alan van keuren mcgee', 
		'expected': True, 
		'description': 'alan v mcgee comparison with article'
	},
    {
		'name_one': 'albert a la plante, a. jr',
		'name_two': 'albert aurel la plante', 
		'expected': True, 
		'description': 'albert a la plante, a. jr comparison with article'
	},
    {
		'name_one': 'albert b m lewis',
		'name_two': 'albert dale milton lewis', 
		'expected': True, 
		'description': 'albert b m lewis comparison with article'
	},
    {
		'name_one': 'albert c vandusen',
		'name_two': 'albert clarence van dusen', 
		'expected': True, 
		'description': 'albert c vandusen comparison with article'
	},
    {
		'name_one': 'albert d kirwan',
		'name_two': 'albert dennis kirwan', 
		'expected': True, 
		'description': 'albert d kirwan comparison with article'
	},
    {
		'name_one': 'albert d lebau',
		'name_two': 'albert c. baugh', 
		'expected': False, 
		'description': 'albert d lebau comparison with article'
	},
    {
		'name_one': 'albert degroat',
		'name_two': 'albert degroat', 
		'expected': True, 
		'description': 'albert degroat comparison with article'
	},
    {
		'name_one': 'albert delisle',
		'name_two': 'albert l. delisle', 
		'expected': True, 
		'description': 'albert delisle comparison with article'
	},
    {
		'name_one': 'albert e babb',
		'name_two': 'albert leslie babb', 
		'expected': False, 
		'description': 'albert e babb comparison with article'
	},
    {
		'name_one': 'albert fritz',
		'name_two': 'karl albert kurt von fritz', 
		'expected': True, 
		'description': 'albert fritz comparison with article'
	},
    {
		'name_one': 'albert hyler',
		'name_two': 'albert leroy hilliard', 
		'expected': False, 
		'description': 'albert hyler comparison with article'
	},
    {
		'name_one': 'albert j latham',
		'name_two': 'albert j. latham', 
		'expected': True, 
		'description': 'albert j latham comparison with article'
	},
    {
		'name_one': 'albert l demaree',
		'name_two': 'albert lowther demaree', 
		'expected': True, 
		'description': 'albert l demaree comparison with article'
	},
    {
		'name_one': 'albert l franzke',
		'name_two': 'albert leonard franzke', 
		'expected': True, 
		'description': 'albert l franzke comparison with article'
	},
    {
		'name_one': 'albert l hoffman',
		'name_two': 'elbert lee hoffman', 
		'expected': True, 
		'description': 'albert l hoffman comparison with article'
	},
    {
		'name_one': 'albert l leduc, jr',
		'name_two': 'albert l. leduc', 
		'expected': True, 
		'description': 'albert l leduc, jr comparison with article'
	},
    {
		'name_one': 'albert l sturm',
		'name_two': 'albert lee sturm', 
		'expected': True, 
		'description': 'albert l sturm comparison with article'
	},
    {
		'name_one': 'albert laubengayer',
		'name_two': 'albert w. laubengayer', 
		'expected': True, 
		'description': 'albert laubengayer comparison with article'
	},
    {
		'name_one': 'albert lazan',
		'name_two': 'albert lazan', 
		'expected': True, 
		'description': 'albert lazan comparison with article'
	},
    {
		'name_one': 'albert le mieux',
		'name_two': 'albert a lemieux', 
		'expected': True, 
		'description': 'albert le mieux comparison with article'
	},
    {
		'name_one': 'albert le roy taylor',
		'name_two': 'albert leroy taylor', 
		'expected': True, 
		'description': 'albert le roy taylor comparison with article'
	},
    {
		'name_one': 'albert levine',
		'name_two': 'samuel albert levine', 
		'expected': True, 
		'description': 'albert levine comparison with article'
	},
    {
		'name_one': 'albert levy',
		'name_two': 'albert w. levi', 
		'expected': True, 
		'description': 'albert levy comparison with article'
	},
    {
		'name_one': 'albert r lamb',
		'name_two': 'albert r. lamb', 
		'expected': True, 
		'description': 'albert r lamb comparison with article'
	},
    {
		'name_one': 'albert r lang',
		'name_two': 'albert ray lang', 
		'expected': True, 
		'description': 'albert r lang comparison with article'
	},
    {
		'name_one': 'albert s dealaman, jr',
		'name_two': 'gellert s. alleman', 
		'expected': True, 
		'description': 'albert s dealaman, jr comparison with article'
	},
    {
		'name_one': 'albert s lada',
		'name_two': 'milan s. la du', 
		'expected': False, 
		'description': 'albert s lada comparison with article'
	},
    {
		'name_one': 'albert w van ness',
		'name_two': 'albert w. van ness', 
		'expected': True, 
		'description': 'albert w van ness comparison with article'
	},
    {
		'name_one': 'alberta k levine',
		'name_two': 'albert k. levine', 
		'expected': True, 
		'description': 'alberta k levine comparison with article'
	},
    {
		'name_one': 'alberta m price',
		'name_two': 'm. lawrence price', 
		'expected': False, 
		'description': 'alberta m price comparison with article'
	},
    {
		'name_one': 'alden crittenden',
		'name_two': 'alden larue crittenden', 
		'expected': True, 
		'description': 'alden crittenden comparison with article'
	},
    {
		'name_one': 'aldon s lang',
		'name_two': 'aldon s. lang', 
		'expected': True, 
		'description': 'aldon s lang comparison with article'
	},
    {
		'name_one': 'alex lawrie',
		'name_two': 'alex laurie', 
		'expected': True, 
		'description': 'alex lawrie comparison with article'
	},
    {
		'name_one': 'alex s levens',
		'name_two': 'alexander s. levens', 
		'expected': True, 
		'description': 'alex s levens comparison with article'
	},
    {
		'name_one': 'alexander a rowell, sr',
		'name_two': 'gillie a. larew', 
		'expected': False, 
		'description': 'alexander a rowell, sr comparison with article'
	},
    {
		'name_one': 'alexander h lighton',
		'name_two': 'alexander h. leighton', 
		'expected': True, 
		'description': 'alexander h lighton comparison with article'
	},
    {
		'name_one': 'alexander kreisler',
		'name_two': 'alexander von kreisler', 
		'expected': True, 
		'description': 'alexander kreisler comparison with article'
	},
    {
		'name_one': 'alexander l geisenheimer',
		'name_two': 'alexander leopold geisenheimer', 
		'expected': True, 
		'description': 'alexander l geisenheimer comparison with article'
	},
    {
		'name_one': 'alexander leitch',
		'name_two': 'alexander leitch', 
		'expected': True, 
		'description': 'alexander leitch comparison with article'
	},
    {
		'name_one': 'alexander levine',
		'name_two': 'alexander levine', 
		'expected': True, 
		'description': 'alexander levine comparison with article'
	},
    {
		'name_one': 'alexander popov',
		'name_two': 'alexander van popov', 
		'expected': True, 
		'description': 'alexander popov comparison with article'
	},
    {
		'name_one': 'alfa c latzke',
		'name_two': 'alpha corinne latzke', 
		'expected': True, 
		'description': 'alfa c latzke comparison with article'
	},
    {
		'name_one': 'alfred a devellio',
		'name_two': 'claude alvin villee', 
		'expected': False, 
		'description': 'alfred a devellio comparison with article'
	},
    {
		'name_one': 'alfred biggs',
		'name_two': 'alfred debard biggs', 
		'expected': True, 
		'description': 'alfred biggs comparison with article'
	},
    {
		'name_one': 'alfred d longhouse',
		'name_two': 'alfred delbert longhouse', 
		'expected': True, 
		'description': 'alfred d longhouse comparison with article'
	},
    {
		'name_one': 'alfred d simpson',
		'name_two': 'alfred dexter simpson', 
		'expected': True, 
		'description': 'alfred d simpson comparison with article'
	},
    {
		'name_one': 'alfred l burt',
		'name_two': 'alfred leroy burt', 
		'expected': True, 
		'description': 'alfred l burt comparison with article'
	},
    {
		'name_one': 'alfred l clapp',
		'name_two': 'alfred lester clapp', 
		'expected': True, 
		'description': 'alfred l clapp comparison with article'
	},
    {
		'name_one': 'alfred l edwards',
		'name_two': 'alfred leroy edwards', 
		'expected': True, 
		'description': 'alfred l edwards comparison with article'
	},
    {
		'name_one': 'alfred l gausewitz',
		'name_two': 'alfred leroy gausewitz', 
		'expected': True, 
		'description': 'alfred l gausewitz comparison with article'
	},
    {
		'name_one': 'alfred l lomax',
		'name_two': 'alfred lewis lomax', 
		'expected': True, 
		'description': 'alfred l lomax comparison with article'
	},
    {
		'name_one': 'alfred l miller',
		'name_two': 'alfred lawrence miller', 
		'expected': True, 
		'description': 'alfred l miller comparison with article'
	},
    {
		'name_one': 'alfred l wilds',
		'name_two': 'alfred lawrence wilds', 
		'expected': True, 
		'description': 'alfred l wilds comparison with article'
	},
    {
		'name_one': 'alfred lande',
		'name_two': 'alfred lande', 
		'expected': True, 
		'description': 'alfred lande comparison with article'
	},
    {
		'name_one': 'alfred leimdorfer',
		'name_two': 'alfred leimdorfer', 
		'expected': True, 
		'description': 'alfred leimdorfer comparison with article'
	},
    {
		'name_one': 'alfred m lee',
		'name_two': 'alfred mcclung lee', 
		'expected': True, 
		'description': 'alfred m lee comparison with article'
	},
    {
		'name_one': 'alfred s lazarus',
		'name_two': 'alfred s. lazarus', 
		'expected': True, 
		'description': 'alfred s lazarus comparison with article'
	},
    {
		'name_one': 'alfred schmied',
		'name_two': 'alfred leo schmied', 
		'expected': True, 
		'description': 'alfred schmied comparison with article'
	},
    {
		'name_one': 'alfred vacchio',
		'name_two': 'alfred del vecchio', 
		'expected': True, 
		'description': 'alfred vacchio comparison with article'
	},
    {
		'name_one': 'alice j vandermeulen',
		'name_two': 'alice john vandermeulen', 
		'expected': True, 
		'description': 'alice j vandermeulen comparison with article'
	},
    {
		'name_one': 'alice l hodgson',
		'name_two': 'linwood lamb hodgdon', 
		'expected': False, 
		'description': 'alice l hodgson comparison with article'
	},
    {
		'name_one': 'alice lazerowitz',
		'name_two': 'alice loman ambrose lazerowitz', 
		'expected': True, 
		'description': 'alice lazerowitz comparison with article'
	},
    {
		'name_one': 'alice m demeritt',
		'name_two': 'm. mauritia', 
		'expected': True, 
		'description': 'alice m demeritt comparison with article'
	},
    {
		'name_one': 'alice m vau de voort',
		'name_two': 'alice van de voort', 
		'expected': True, 
		'description': 'alice m vau de voort comparison with article'
	},
    {
		'name_one': 'alice w leland',
		'name_two': 'thomas w. leland', 
		'expected': False, 
		'description': 'alice w leland comparison with article'
	},
    {
		'name_one': 'allan c de lacy',
		'name_two': 'allan clark delacy', 
		'expected': True, 
		'description': 'allan c de lacy comparison with article'
	},
    {
		'name_one': 'allan l strout',
		'name_two': 'alan lang strout', 
		'expected': True, 
		'description': 'allan l strout comparison with article'
	},
    {
		'name_one': 'allen a lasko',
		'name_two': 'alvin a. lasko', 
		'expected': True, 
		'description': 'allen a lasko comparison with article'
	},
    {
		'name_one': 'allen b lambdin',
		'name_two': 'allen b. lambdin', 
		'expected': True, 
		'description': 'allen b lambdin comparison with article'
	},
    {
		'name_one': 'allen d cooper',
		'name_two': 'allen lamar cooper', 
		'expected': False, 
		'description': 'allen d cooper comparison with article'
	},
    {
		'name_one': 'allen l king',
		'name_two': 'allen lewis king', 
		'expected': True, 
		'description': 'allen l king comparison with article'
	},
    {
		'name_one': 'allen l lorincz',
		'name_two': 'allan levente lorincz', 
		'expected': True, 
		'description': 'allen l lorincz comparison with article'
	},
    {
		'name_one': 'allen lein',
		'name_two': 'allen lein', 
		'expected': True, 
		'description': 'allen lein comparison with article'
	},
    {
		'name_one': 'alonzo a leifeste',
		'name_two': 'a. a. liefeste', 
		'expected': True, 
		'description': 'alonzo a leifeste comparison with article'
	},
    {
		'name_one': 'alva l kerbow',
		'name_two': 'alva lee kerbow', 
		'expected': True, 
		'description': 'alva l kerbow comparison with article'
	},
    {
		'name_one': 'alva leroy prickett',
		'name_two': 'alva leroy prickett', 
		'expected': True, 
		'description': 'alva leroy prickett comparison with article'
	},
    {
		'name_one': 'alvah l newcomb',
		'name_two': 'alvah lay newcomb', 
		'expected': True, 
		'description': 'alvah l newcomb comparison with article'
	},
    {
		'name_one': 'alvan l barach',
		'name_two': 'alvan leroy barach', 
		'expected': True, 
		'description': 'alvan l barach comparison with article'
	},
    {
		'name_one': 'alvin d etlers',
		'name_two': 'alvin derald etler', 
		'expected': True, 
		'description': 'alvin d etlers comparison with article'
	},
    {
		'name_one': 'alvin g law',
		'name_two': 'alvin g. law', 
		'expected': True, 
		'description': 'alvin g law comparison with article'
	},
    {
		'name_one': 'alvin l lang',
		'name_two': 'alvin l. lang', 
		'expected': True, 
		'description': 'alvin l lang comparison with article'
	},
    {
		'name_one': 'amance a desautels',
		'name_two': 'agnes de st louis', 
		'expected': False, 
		'description': 'amance a desautels comparison with article'
	},
    {
		'name_one': 'amanda l forkner',
		'name_two': 'hamden landon forkner', 
		'expected': False, 
		'description': 'amanda l forkner comparison with article'
	},
    {
		'name_one': 'amelia delrio',
		'name_two': 'amelia a. de del rio', 
		'expected': True, 
		'description': 'amelia delrio comparison with article'
	},
    {
		'name_one': 'amos p leib',
		'name_two': 'amos p. leib', 
		'expected': True, 
		'description': 'amos p leib comparison with article'
	},
    {
		'name_one': 'amy l turner',
		'name_two': 'amy lee turner', 
		'expected': True, 
		'description': 'amy l turner comparison with article'
	},
    {
		'name_one': 'anastasia vanbebber',
		'name_two': 'anastasia van bebber', 
		'expected': True, 
		'description': 'anastasia vanbebber comparison with article'
	},
    {
		'name_one': 'anastasia vanburkalow',
		'name_two': 'anastasia van burkalow', 
		'expected': True, 
		'description': 'anastasia vanburkalow comparison with article'
	},
    {
		'name_one': 'andre c leveque',
		'name_two': 'andre camille leveque', 
		'expected': True, 
		'description': 'andre c leveque comparison with article'
	},
    {
		'name_one': 'andre von gronicka',
		'name_two': 'andre von gronicka', 
		'expected': True, 
		'description': 'andre von gronicka comparison with article'
	},
    {
		'name_one': 'andree de c heller',
		'name_two': 'andree heller', 
		'expected': True, 
		'description': 'andree de c heller comparison with article'
	},
    {
		'name_one': 'andrew l papailion',
		'name_two': 'laura van pappelendam', 
		'expected': False, 
		'description': 'andrew l papailion comparison with article'
	},
    {
		'name_one': 'andrew malon',
		'name_two': 'peter andrew van der meulen', 
		'expected': True, 
		'description': 'andrew malon comparison with article'
	},
    {
		'name_one': 'andrew p van hook',
		'name_two': 'andrew p. van hook', 
		'expected': True, 
		'description': 'andrew p van hook comparison with article'
	},
    {
		'name_one': 'andrew p vanderpoel',
		'name_two': 'priscilla paine van der poel', 
		'expected': False, 
		'description': 'andrew p vanderpoel comparison with article'
	},
    {
		'name_one': 'andrew w lawson, jr',
		'name_two': 'andrew werner lawson', 
		'expected': True, 
		'description': 'andrew w lawson, jr comparison with article'
	},
    {
		'name_one': 'angel delrio',
		'name_two': 'angel del rio', 
		'expected': True, 
		'description': 'angel delrio comparison with article'
	},
    {
		'name_one': 'angela d oglesby',
		'name_two': 'dwayne la vergne oglesby', 
		'expected': False, 
		'description': 'angela d oglesby comparison with article'
	},
    {
		'name_one': 'angela g lardner',
		'name_two': 'gerhart ladner', 
		'expected': True, 
		'description': 'angela g lardner comparison with article'
	},
    {
		'name_one': 'angelina la piana',
		'name_two': 'angeline la piana', 
		'expected': True, 
		'description': 'angelina la piana comparison with article'
	},
    {
		'name_one': 'angelo degennaro',
		'name_two': 'angelo a. de gennaro', 
		'expected': True, 
		'description': 'angelo degennaro comparison with article'
	},
    {
		'name_one': 'angie t king',
		'name_two': 'angie lena turner king', 
		'expected': True, 
		'description': 'angie t king comparison with article'
	},
    {
		'name_one': 'ann deeds',
		'name_two': 'ann catherine deeds', 
		'expected': True, 
		'description': 'ann deeds comparison with article'
	},
    {
		'name_one': 'ann k ann k,',
		'name_two': 'nancy van anne', 
		'expected': False, 
		'description': 'ann k ann k, comparison with article'
	},
    {
		'name_one': 'ann l diem',
		'name_two': 'william l. deam', 
		'expected': False, 
		'description': 'ann l diem comparison with article'
	},
    {
		'name_one': 'ann lankford',
		'name_two': 'ann elizabeth lankford', 
		'expected': True, 
		'description': 'ann lankford comparison with article'
	},
    {
		'name_one': 'ann s lettle',
		'name_two': 'elizabeth ann liddle', 
		'expected': False, 
		'description': 'ann s lettle comparison with article'
	},
    {
		'name_one': 'anna c lageragen',
		'name_two': 'anna constantia lagergren', 
		'expected': True, 
		'description': 'anna c lageragen comparison with article'
	},
    {
		'name_one': 'anna e. lange',
		'name_two': 'e. o. lange', 
		'expected': False, 
		'description': 'anna e. lange comparison with article'
	},
    {
		'name_one': 'anna j de armond',
		'name_two': 'anna janney dearmond', 
		'expected': True, 
		'description': 'anna j de armond comparison with article'
	},
    {
		'name_one': 'anna l cochran',
		'name_two': 'elmer lendell cockrum', 
		'expected': False, 
		'description': 'anna l cochran comparison with article'
	},
    {
		'name_one': 'anna p lauterbur',
		'name_two': 'anna p. lauterbur', 
		'expected': True, 
		'description': 'anna p lauterbur comparison with article'
	},
    {
		'name_one': 'anne b lay',
		'name_two': 'anne brownlee lay', 
		'expected': True, 
		'description': 'anne b lay comparison with article'
	},
    {
		'name_one': 'anne l lewis',
		'name_two': 'anne louise lewis', 
		'expected': True, 
		'description': 'anne l lewis comparison with article'
	},
    {
		'name_one': 'annita delano',
		'name_two': 'annita delano', 
		'expected': True, 
		'description': 'annita delano comparison with article'
	},
    {
		'name_one': 'anthonie van harreveld, jr',
		'name_two': 'anthonie van harreveld', 
		'expected': True, 
		'description': 'anthonie van harreveld, jr comparison with article'
	},
    {
		'name_one': 'anthony de michele',
		'name_two': 'laurence anthony michel', 
		'expected': True, 
		'description': 'anthony de michele comparison with article'
	},
    {
		'name_one': 'anthony de oreo',
		'name_two': 'gerard anthony de oreo', 
		'expected': True, 
		'description': 'anthony de oreo comparison with article'
	},
    {
		'name_one': 'anthony j defilipps',
		'name_two': 'a. j. defilipps', 
		'expected': True, 
		'description': 'anthony j defilipps comparison with article'
	},
    {
		'name_one': 'anthony j del mastro',
		'name_two': 'anthony j. del mastro', 
		'expected': True, 
		'description': 'anthony j del mastro comparison with article'
	},
    {
		'name_one': 'anthony l turkevich',
		'name_two': 'anthony leonid turkevich', 
		'expected': True, 
		'description': 'anthony l turkevich comparison with article'
	},
    {
		'name_one': 'anton lang',
		'name_two': 'anton lang', 
		'expected': True, 
		'description': 'anton lang comparison with article'
	},
    {
		'name_one': 'arch lauterer',
		'name_two': 'arch lauterer', 
		'expected': True, 
		'description': 'arch lauterer comparison with article'
	},
    {
		'name_one': 'archbald laforte',
		'name_two': 'archibald smith foord', 
		'expected': False, 
		'description': 'archbald laforte comparison with article'
	},
    {
		'name_one': 'archibald s dean',
		'name_two': 'archibald s. dean', 
		'expected': True, 
		'description': 'archibald s dean comparison with article'
	},
    {
		'name_one': 'archie l leonard',
		'name_two': 'archie leroy leonard', 
		'expected': True, 
		'description': 'archie l leonard comparison with article'
	},
    {
		'name_one': 'ariel f lausche',
		'name_two': 'luverne frederick lausche', 
		'expected': False, 
		'description': 'ariel f lausche comparison with article'
	},
    {
		'name_one': 'arman j lawrence',
		'name_two': 'armon jay lawrence', 
		'expected': True, 
		'description': 'arman j lawrence comparison with article'
	},
    {
		'name_one': 'armand desautel',
		'name_two': 'armand h. desautels', 
		'expected': True, 
		'description': 'armand desautel comparison with article'
	},
    {
		'name_one': 'arnand b leavelle',
		'name_two': 'arnaud b. leavelle', 
		'expected': True, 
		'description': 'arnand b leavelle comparison with article'
	},
    {
		'name_one': 'arno t lenz',
		'name_two': 'arno thomas lenz', 
		'expected': True, 
		'description': 'arno t lenz comparison with article'
	},
    {
		'name_one': 'arnold lazerow',
		'name_two': 'arnold lazarow', 
		'expected': True, 
		'description': 'arnold lazerow comparison with article'
	},
    {
		'name_one': 'arnold w lapp',
		'name_two': 'arnold w. lapp', 
		'expected': True, 
		'description': 'arnold w lapp comparison with article'
	},
    {
		'name_one': 'arthur a lewis',
		'name_two': 'arthur o. lewis', 
		'expected': False, 
		'description': 'arthur a lewis comparison with article'
	},
    {
		'name_one': 'arthur b leible',
		'name_two': 'arthur blank leible', 
		'expected': True, 
		'description': 'arthur b leible comparison with article'
	},
    {
		'name_one': 'arthur b lewis',
		'name_two': 'arthur beverly lewis', 
		'expected': True, 
		'description': 'arthur b lewis comparison with article'
	},
    {
		'name_one': 'arthur brandon',
		'name_two': 'arthur leon brandon', 
		'expected': True, 
		'description': 'arthur brandon comparison with article'
	},
    {
		'name_one': 'arthur d butterfield',
		'name_two': 'arthur dexter butterfield', 
		'expected': True, 
		'description': 'arthur d butterfield comparison with article'
	},
    {
		'name_one': 'arthur d les?eut',
		'name_two': 'arthur m. lassek', 
		'expected': False, 
		'description': 'arthur d les?eut comparison with article'
	},
    {
		'name_one': 'arthur d moore',
		'name_two': 'arthur dearth moore', 
		'expected': True, 
		'description': 'arthur d moore comparison with article'
	},
    {
		'name_one': 'arthur delez',
		'name_two': 'arthur louis delez', 
		'expected': True, 
		'description': 'arthur delez comparison with article'
	},
    {
		'name_one': 'arthur denney',
		'name_two': 'arthur c. denney', 
		'expected': True, 
		'description': 'arthur denney comparison with article'
	},
    {
		'name_one': 'arthur e lamb',
		'name_two': 'arthur e. lamb', 
		'expected': True, 
		'description': 'arthur e lamb comparison with article'
	},
    {
		'name_one': 'arthur f deam',
		'name_two': 'arthur f. deam', 
		'expected': True, 
		'description': 'arthur f deam comparison with article'
	},
    {
		'name_one': 'arthur f watkins',
		'name_two': 'arthur lancaster watkins', 
		'expected': False, 
		'description': 'arthur f watkins comparison with article'
	},
    {
		'name_one': 'arthur h leavitt',
		'name_two': 'arthur h. leavitt', 
		'expected': True, 
		'description': 'arthur h leavitt comparison with article'
	},
    {
		'name_one': 'arthur herbert levy, jr',
		'name_two': 'arthur herbert levy', 
		'expected': True, 
		'description': 'arthur herbert levy, jr comparison with article'
	},
    {
		'name_one': 'arthur j lopovsky',
		'name_two': 'arthur j. lapovsky', 
		'expected': True, 
		'description': 'arthur j lopovsky comparison with article'
	},
    {
		'name_one': 'arthur l albert',
		'name_two': 'arthur lemuel albert', 
		'expected': True, 
		'description': 'arthur l albert comparison with article'
	},
    {
		'name_one': 'arthur l anderson',
		'name_two': 'arthur lawrence anderson', 
		'expected': True, 
		'description': 'arthur l anderson comparison with article'
	},
    {
		'name_one': 'arthur l benton',
		'name_two': 'arthur lester benton', 
		'expected': True, 
		'description': 'arthur l benton comparison with article'
	},
    {
		'name_one': 'arthur l derring',
		'name_two': 'arthur l. deering', 
		'expected': True, 
		'description': 'arthur l derring comparison with article'
	},
    {
		'name_one': 'arthur l goodrich',
		'name_two': 'arthur leonard goodrich', 
		'expected': True, 
		'description': 'arthur l goodrich comparison with article'
	},
    {
		'name_one': 'arthur l neal',
		'name_two': 'arthur leslie neal', 
		'expected': True, 
		'description': 'arthur l neal comparison with article'
	},
    {
		'name_one': 'arthur l searles',
		'name_two': 'arthur langley searles', 
		'expected': True, 
		'description': 'arthur l searles comparison with article'
	},
    {
		'name_one': 'arthur l svenson',
		'name_two': 'arthur lee svenson', 
		'expected': True, 
		'description': 'arthur l svenson comparison with article'
	},
    {
		'name_one': 'arthur l tatum',
		'name_two': 'arthur lawrie tatum', 
		'expected': True, 
		'description': 'arthur l tatum comparison with article'
	},
    {
		'name_one': 'arthur l townsend',
		'name_two': 'arthur lawrence townsend', 
		'expected': True, 
		'description': 'arthur l townsend comparison with article'
	},
    {
		'name_one': 'arthur l vollman',
		'name_two': 'ludwig von sallmann', 
		'expected': False, 
		'description': 'arthur l vollman comparison with article'
	},
    {
		'name_one': 'arthur l young',
		'name_two': 'arthur leighton young', 
		'expected': True, 
		'description': 'arthur l young comparison with article'
	},
    {
		'name_one': 'arthur lamay',
		'name_two': 'mark arthur may', 
		'expected': True, 
		'description': 'arthur lamay comparison with article'
	},
    {
		'name_one': 'arthur larson',
		'name_two': 'arthur larson', 
		'expected': True, 
		'description': 'arthur larson comparison with article'
	},
    {
		'name_one': 'arthur lawrence bakke',
		'name_two': 'arthur lawrence bakke', 
		'expected': True, 
		'description': 'arthur lawrence bakke comparison with article'
	},
    {
		'name_one': 'arthur lenhoff',
		'name_two': 'arthur lenhoff', 
		'expected': True, 
		'description': 'arthur lenhoff comparison with article'
	},
    {
		'name_one': 'arthur lesser',
		'name_two': 'arthur lesser', 
		'expected': True, 
		'description': 'arthur lesser comparison with article'
	},
    {
		'name_one': 'arthur lewis',
		'name_two': 'arthur lewis', 
		'expected': True, 
		'description': 'arthur lewis comparison with article'
	},
    {
		'name_one': 'arthur prince',
		'name_two': 'arthur leslie prince', 
		'expected': True, 
		'description': 'arthur prince comparison with article'
	},
    {
		'name_one': 'arthur r fisher',
		'name_two': 'arthur lawrence fisher', 
		'expected': False, 
		'description': 'arthur r fisher comparison with article'
	},
    {
		'name_one': 'arthur s levine',
		'name_two': 'arthur sidney levine', 
		'expected': True, 
		'description': 'arthur s levine comparison with article'
	},
    {
		'name_one': 'arthur van mehren',
		'name_two': 'arthur taylor von mehren', 
		'expected': True, 
		'description': 'arthur van mehren comparison with article'
	},
    {
		'name_one': 'arthur w leighton',
		'name_two': 'arthur w. leighton', 
		'expected': True, 
		'description': 'arthur w leighton comparison with article'
	},
    {
		'name_one': 'arvo vanalstyne',
		'name_two': 'arvo van alstyne', 
		'expected': True, 
		'description': 'arvo vanalstyne comparison with article'
	},
    {
		'name_one': 'ashton welsh',
		'name_two': 'ashton leroy welsh', 
		'expected': True, 
		'description': 'ashton welsh comparison with article'
	},
    {
		'name_one': 'aubrey landers',
		'name_two': 'aubrey w. landers', 
		'expected': True, 
		'description': 'aubrey landers comparison with article'
	},
    {
		'name_one': 'august d lang',
		'name_two': 'arch d. lang', 
		'expected': False, 
		'description': 'august d lang comparison with article'
	},
    {
		'name_one': 'august r leisner',
		'name_two': 'a. roberts leisner', 
		'expected': True, 
		'description': 'august r leisner comparison with article'
	},
    {
		'name_one': 'augustin cosgrove',
		'name_two': 'augustin lawrence cosgrove', 
		'expected': True, 
		'description': 'augustin cosgrove comparison with article'
	},
    {
		'name_one': 'austin lamont',
		'name_two': 'austin lamont', 
		'expected': True, 
		'description': 'austin lamont comparison with article'
	},
    {
		'name_one': 'avis graham',
		'name_two': 'avis exalee lair graham', 
		'expected': True, 
		'description': 'avis graham comparison with article'
	},
    {
		'name_one': 'babette levy',
		'name_two': 'babette m. levy', 
		'expected': True, 
		'description': 'babette levy comparison with article'
	},
    {
		'name_one': 'barbara lee',
		'name_two': 'barbara lee', 
		'expected': True, 
		'description': 'barbara lee comparison with article'
	},
    {
		'name_one': 'barboar l herrington',
		'name_two': 'barbour lawson herrington', 
		'expected': True, 
		'description': 'barboar l herrington comparison with article'
	},
    {
		'name_one': 'barclay leathem',
		'name_two': 'barclay s. leathem', 
		'expected': True, 
		'description': 'barclay leathem comparison with article'
	},
    {
		'name_one': 'barnes f lathrop',
		'name_two': 'barnes f. lathrop', 
		'expected': True, 
		'description': 'barnes f lathrop comparison with article'
	},
    {
		'name_one': 'barnet m levy',
		'name_two': 'barnet m. levy', 
		'expected': True, 
		'description': 'barnet m levy comparison with article'
	},
    {
		'name_one': 'basil l sherrill',
		'name_two': 'basil lamar sherrill', 
		'expected': True, 
		'description': 'basil l sherrill comparison with article'
	},
    {
		'name_one': 'beatrice m la vigne',
		'name_two': 'beatrice lavigne', 
		'expected': True, 
		'description': 'beatrice m la vigne comparison with article'
	},
    {
		'name_one': 'beatrice von keller',
		'name_two': 'beatrice von keller', 
		'expected': True, 
		'description': 'beatrice von keller comparison with article'
	},
    {
		'name_one': 'beautine h de costa',
		'name_two': 'beautine h. decosta', 
		'expected': True, 
		'description': 'beautine h de costa comparison with article'
	},
    {
		'name_one': 'ben f lemert',
		'name_two': 'benjamin franklin lemert', 
		'expected': True, 
		'description': 'ben f lemert comparison with article'
	},
    {
		'name_one': 'ben l. love',
		'name_two': 'ben del love', 
		'expected': True, 
		'description': 'ben l. love comparison with article'
	},
    {
		'name_one': 'benjamin averbook',
		'name_two': 'benjamin lewis averbach', 
		'expected': False, 
		'description': 'benjamin averbook comparison with article'
	},
    {
		'name_one': 'benjamin d leith',
		'name_two': 'benjamin donald leith', 
		'expected': True, 
		'description': 'benjamin d leith comparison with article'
	},
    {
		'name_one': 'benjamin h lehman',
		'name_two': 'benjamin h. lehman', 
		'expected': True, 
		'description': 'benjamin h lehman comparison with article'
	},
    {
		'name_one': 'benjamin l smits',
		'name_two': 'benjamin levi smits', 
		'expected': True, 
		'description': 'benjamin l smits comparison with article'
	},
    {
		'name_one': 'benjamin lease',
		'name_two': 'benjamin lease', 
		'expected': True, 
		'description': 'benjamin lease comparison with article'
	},
    {
		'name_one': 'benjimine r lacy',
		'name_two': 'benjamin rice lacy', 
		'expected': True, 
		'description': 'benjimine r lacy comparison with article'
	},
    {
		'name_one': 'benno landsberger',
		'name_two': 'benno landsberger', 
		'expected': True, 
		'description': 'benno landsberger comparison with article'
	},
    {
		'name_one': 'benson j. lamp',
		'name_two': 'benson j. lamp', 
		'expected': True, 
		'description': 'benson j. lamp comparison with article'
	},
    {
		'name_one': 'bernard h larsen, jr',
		'name_two': 'bernard boysen larsen', 
		'expected': False, 
		'description': 'bernard h larsen, jr comparison with article'
	},
    {
		'name_one': 'bernard karten',
		'name_two': 'bernard leon kartin', 
		'expected': True, 
		'description': 'bernard karten comparison with article'
	},
    {
		'name_one': 'bernard lander',
		'name_two': 'bernard lander', 
		'expected': True, 
		'description': 'bernard lander comparison with article'
	},
    {
		'name_one': 'bernard lemann',
		'name_two': 'bernard lemann', 
		'expected': True, 
		'description': 'bernard lemann comparison with article'
	},
    {
		'name_one': 'bernard levy',
		'name_two': 'bernard levy', 
		'expected': True, 
		'description': 'bernard levy comparison with article'
	},
    {
		'name_one': 'bernard liebman',
		'name_two': 'o. bernard leibman', 
		'expected': True, 
		'description': 'bernard liebman comparison with article'
	},
    {
		'name_one': 'bernhardt lemmel',
		'name_two': 'bernhardt lemmel', 
		'expected': True, 
		'description': 'bernhardt lemmel comparison with article'
	},
    {
		'name_one': 'bernt o larson',
		'name_two': 'bernt o. larson', 
		'expected': True, 
		'description': 'bernt o larson comparison with article'
	},
    {
		'name_one': 'bertha m levy',
		'name_two': 'bertha marion levy', 
		'expected': True, 
		'description': 'bertha m levy comparison with article'
	},
    {
		'name_one': 'bertha v lederar',
		'name_two': 'bertha v. lederer', 
		'expected': True, 
		'description': 'bertha v lederar comparison with article'
	},
    {
		'name_one': 'bertina laborde',
		'name_two': 'bertina anne laborde', 
		'expected': True, 
		'description': 'bertina laborde comparison with article'
	},
    {
		'name_one': 'bertram levinson',
		'name_two': 'bertram levinson', 
		'expected': True, 
		'description': 'bertram levinson comparison with article'
	},
    {
		'name_one': 'bessie g campbell',
		'name_two': 'bessie lee gambrill', 
		'expected': False, 
		'description': 'bessie g campbell comparison with article'
	},
    {
		'name_one': 'betty a land',
		'name_two': 'betty aiken land', 
		'expected': True, 
		'description': 'betty a land comparison with article'
	},
    {
		'name_one': 'betty c delavan',
		'name_two': 'betty c. delavan', 
		'expected': True, 
		'description': 'betty c delavan comparison with article'
	},
    {
		'name_one': 'bevin lewis',
		'name_two': 'bevan blau lewis', 
		'expected': True, 
		'description': 'bevin lewis comparison with article'
	},
    {
		'name_one': 'bianca del vecchio',
		'name_two': 'bianca del vecchio', 
		'expected': True, 
		'description': 'bianca del vecchio comparison with article'
	},
    {
		'name_one': 'billy j van gundy',
		'name_two': 'justine van gundy', 
		'expected': True, 
		'description': 'billy j van gundy comparison with article'
	},
    {
		'name_one': 'blaine de lancey',
		'name_two': 'blaine delancey', 
		'expected': True, 
		'description': 'blaine de lancey comparison with article'
	},
    {
		'name_one': 'blake ragsdale von leer',
		'name_two': 'blake ragsdale van leer', 
		'expected': True, 
		'description': 'blake ragsdale von leer comparison with article'
	},
    {
		'name_one': 'boni j delaureal',
		'name_two': 'boni james delaureal', 
		'expected': True, 
		'description': 'boni j delaureal comparison with article'
	},
    {
		'name_one': 'boris leaf',
		'name_two': 'boris leaf', 
		'expected': True, 
		'description': 'boris leaf comparison with article'
	},
    {
		'name_one': 'boris levinson',
		'name_two': 'boris m. levinson', 
		'expected': True, 
		'description': 'boris levinson comparison with article'
	},
    {
		'name_one': 'borisz deballa',
		'name_two': 'borisz de balla', 
		'expected': True, 
		'description': 'borisz deballa comparison with article'
	},
    {
		'name_one': 'boyd l o\'dell',
		'name_two': 'boyd lee o\'dell', 
		'expected': True, 
		'description': 'boyd l o\'dell comparison with article'
	},
    {
		'name_one': 'bradley d thompson',
		'name_two': 'bradley deforrest thompson', 
		'expected': True, 
		'description': 'bradley d thompson comparison with article'
	},
    {
		'name_one': 'bror l grondal',
		'name_two': 'bror leonard grondal', 
		'expected': True, 
		'description': 'bror l grondal comparison with article'
	},
    {
		'name_one': 'bruce despelder',
		'name_two': 'bruce e. despelder', 
		'expected': True, 
		'description': 'bruce despelder comparison with article'
	},
    {
		'name_one': 'bruce g dearing',
		'name_two': 'bruce dearing', 
		'expected': True, 
		'description': 'bruce g dearing comparison with article'
	},
    {
		'name_one': 'bruce l cartter',
		'name_two': 'bruce lanpher cartter', 
		'expected': True, 
		'description': 'bruce l cartter comparison with article'
	},
    {
		'name_one': 'bruce weidner',
		'name_two': 'bruce van scoyoc weidner', 
		'expected': True, 
		'description': 'bruce weidner comparison with article'
	},
    {
		'name_one': 'brunell d faris',
		'name_two': 'brunel debost faris', 
		'expected': True, 
		'description': 'brunell d faris comparison with article'
	},
    {
		'name_one': 'bryan c landreth',
		'name_two': 'catherine landreth', 
		'expected': True, 
		'description': 'bryan c landreth comparison with article'
	},
    {
		'name_one': 'burtis lawson',
		'name_two': 'burtis carl lawson', 
		'expected': True, 
		'description': 'burtis lawson comparison with article'
	},
    {
		'name_one': 'byron e lauer',
		'name_two': 'bryon elmer lauer', 
		'expected': True, 
		'description': 'byron e lauer comparison with article'
	},
    {
		'name_one': 'byron l jr burford',
		'name_two': 'bryon leslie burford', 
		'expected': True, 
		'description': 'byron l jr burford comparison with article'
	},
    {
		'name_one': 'c lee harwell',
		'name_two': 'c. lee harwell', 
		'expected': True, 
		'description': 'c lee harwell comparison with article'
	},
    {
		'name_one': 'c leonard huskins',
		'name_two': 'charles leonard huskins', 
		'expected': True, 
		'description': 'c leonard huskins comparison with article'
	},
    {
		'name_one': 'c lewis hafermekl',
		'name_two': 'charles louis hafermehl', 
		'expected': True, 
		'description': 'c lewis hafermekl comparison with article'
	},
    {
		'name_one': 'c lowell lees',
		'name_two': 'c. lowell lees', 
		'expected': True, 
		'description': 'c lowell lees comparison with article'
	},
    {
		'name_one': 'c marshall lee',
		'name_two': 'c. marshall lee', 
		'expected': True, 
		'description': 'c marshall lee comparison with article'
	},
    {
		'name_one': 'c theodore larson',
		'name_two': 'c. theodore larson', 
		'expected': True, 
		'description': 'c theodore larson comparison with article'
	},
    {
		'name_one': 'camile j le vois',
		'name_two': 'camille joseph le vois', 
		'expected': True, 
		'description': 'camile j le vois comparison with article'
	},
    {
		'name_one': 'carl a leopold',
		'name_two': 'aldo carl leopold', 
		'expected': True, 
		'description': 'carl a leopold comparison with article'
	},
    {
		'name_one': 'carl a. lamey',
		'name_two': 'carl a. lamey', 
		'expected': True, 
		'description': 'carl a. lamey comparison with article'
	},
    {
		'name_one': 'carl de zeeuw',
		'name_two': 'carl h. dezeeuw', 
		'expected': True, 
		'description': 'carl de zeeuw comparison with article'
	},
    {
		'name_one': 'carl e liangenhop',
		'name_two': 'carl e. langenhop', 
		'expected': True, 
		'description': 'carl e liangenhop comparison with article'
	},
    {
		'name_one': 'carl frank lagler',
		'name_two': 'karl f. lagler', 
		'expected': True, 
		'description': 'carl frank lagler comparison with article'
	},
    {
		'name_one': 'carl g debono',
		'name_two': 'gabriel bonno', 
		'expected': True, 
		'description': 'carl g debono comparison with article'
	},
    {
		'name_one': 'carl g van buskirk',
		'name_two': 'carl george van buskirk', 
		'expected': True, 
		'description': 'carl g van buskirk comparison with article'
	},
    {
		'name_one': 'carl h lenhart',
		'name_two': 'carl h. lenhart', 
		'expected': True, 
		'description': 'carl h lenhart comparison with article'
	},
    {
		'name_one': 'carl l de graff',
		'name_two': 'edwin charles greif', 
		'expected': False, 
		'description': 'carl l de graff comparison with article'
	},
    {
		'name_one': 'carl l gillies',
		'name_two': 'carl lewis gillies', 
		'expected': True, 
		'description': 'carl l gillies comparison with article'
	},
    {
		'name_one': 'carl l heyerdahl',
		'name_two': 'carl lewis heyerdahl', 
		'expected': True, 
		'description': 'carl l heyerdahl comparison with article'
	},
    {
		'name_one': 'carl l huffaker',
		'name_two': 'carl leo huffaker', 
		'expected': True, 
		'description': 'carl l huffaker comparison with article'
	},
    {
		'name_one': 'carl landauer',
		'name_two': 'carl landauer', 
		'expected': True, 
		'description': 'carl landauer comparison with article'
	},
    {
		'name_one': 'carl w lawton',
		'name_two': 'carl william lawton', 
		'expected': True, 
		'description': 'carl w lawton comparison with article'
	},
    {
		'name_one': 'carl w schwette',
		'name_two': 'karl de schweinitz', 
		'expected': False, 
		'description': 'carl w schwette comparison with article'
	},
    {
		'name_one': 'carlo l lastrucci',
		'name_two': 'carlo l. lastrucci', 
		'expected': True, 
		'description': 'carlo l lastrucci comparison with article'
	},
    {
		'name_one': 'carlton h larrabee, male',
		'name_two': 'carlton h. larrabee', 
		'expected': True, 
		'description': 'carlton h larrabee, male comparison with article'
	},
    {
		'name_one': 'carlyn c delavan',
		'name_two': 'carlyn c. delavan', 
		'expected': True, 
		'description': 'carlyn c delavan comparison with article'
	},
    {
		'name_one': 'carmela d laskin',
		'name_two': 'd. s. laskin', 
		'expected': False, 
		'description': 'carmela d laskin comparison with article'
	},
    {
		'name_one': 'carney landis',
		'name_two': 'carney landis', 
		'expected': True, 
		'description': 'carney landis comparison with article'
	},
    {
		'name_one': 'caroline a lester',
		'name_two': 'caroline a. lester', 
		'expected': True, 
		'description': 'caroline a lester comparison with article'
	},
    {
		'name_one': 'caroll meeks',
		'name_two': 'carroll louis vanderslice meeks', 
		'expected': True, 
		'description': 'caroll meeks comparison with article'
	},
    {
		'name_one': 'carolyn l widmer',
		'name_two': 'carolyn ladd widmer', 
		'expected': True, 
		'description': 'carolyn l widmer comparison with article'
	},
    {
		'name_one': 'carrol l. birch',
		'name_two': 'carroll la fleur birch', 
		'expected': True, 
		'description': 'carrol l. birch comparison with article'
	},
    {
		'name_one': 'carroll l christenson',
		'name_two': 'carroll lawrence christenson', 
		'expected': True, 
		'description': 'carroll l christenson comparison with article'
	},
    {
		'name_one': 'carroll l. mann',
		'name_two': 'carroll lamb mann', 
		'expected': True, 
		'description': 'carroll l. mann comparison with article'
	},
    {
		'name_one': 'carroll v glines',
		'name_two': 'carroll vane glines', 
		'expected': True, 
		'description': 'carroll v glines comparison with article'
	},
    {
		'name_one': 'carroll. l. shartle',
		'name_two': 'carroll leonard shartle', 
		'expected': True, 
		'description': 'carroll. l. shartle comparison with article'
	},
    {
		'name_one': 'carter marshall, jr',
		'name_two': 'carter lee marshall', 
		'expected': True, 
		'description': 'carter marshall, jr comparison with article'
	},
    {
		'name_one': 'catherine j phelps',
		'name_two': 'catherine denny phelps', 
		'expected': False, 
		'description': 'catherine j phelps comparison with article'
	},
    {
		'name_one': 'catherine l lipscomb',
		'name_two': 'winifred lawrence lipscomb', 
		'expected': False, 
		'description': 'catherine l lipscomb comparison with article'
	},
    {
		'name_one': 'catherine lawlor',
		'name_two': 'anna catherine lawlor', 
		'expected': True, 
		'description': 'catherine lawlor comparison with article'
	},
    {
		'name_one': 'cecil y lang',
		'name_two': 'cecil tavener lane', 
		'expected': False, 
		'description': 'cecil y lang comparison with article'
	},
    {
		'name_one': 'cecil y lang',
		'name_two': 'cecil yelverton lang', 
		'expected': True, 
		'description': 'cecil y lang comparison with article'
	},
    {
		'name_one': 'cecile debanke',
		'name_two': 'cecile de banke', 
		'expected': True, 
		'description': 'cecile debanke comparison with article'
	},
    {
		'name_one': 'cecilie leuchtenberger',
		'name_two': 'cecilie leuchtenberger', 
		'expected': True, 
		'description': 'cecilie leuchtenberger comparison with article'
	},
    {
		'name_one': 'charle leonard lundin',
		'name_two': 'charles leonard lundin', 
		'expected': True, 
		'description': 'charle leonard lundin comparison with article'
	},
    {
		'name_one': 'charles a lee',
		'name_two': 'charles a. lee', 
		'expected': True, 
		'description': 'charles a lee comparison with article'
	},
    {
		'name_one': 'charles a nelson',
		'name_two': 'charles leblanc nelson', 
		'expected': False, 
		'description': 'charles a nelson comparison with article'
	},
    {
		'name_one': 'charles a roover',
		'name_two': 'raymond a. de roover', 
		'expected': False, 
		'description': 'charles a roover comparison with article'
	},
    {
		'name_one': 'charles b deibel',
		'name_two': 'wallace b. diboll', 
		'expected': False, 
		'description': 'charles b deibel comparison with article'
	},
    {
		'name_one': 'charles c flick',
		'name_two': 'charles lewis fluke', 
		'expected': False, 
		'description': 'charles c flick comparison with article'
	},
    {
		'name_one': 'charles c lasater',
		'name_two': 'chas. crawford lasater', 
		'expected': True, 
		'description': 'charles c lasater comparison with article'
	},
    {
		'name_one': 'charles c lauritsen',
		'name_two': 'charles christian lauritsen', 
		'expected': True, 
		'description': 'charles c lauritsen comparison with article'
	},
    {
		'name_one': 'charles c lawrence',
		'name_two': 'charles e. lawrence', 
		'expected': False, 
		'description': 'charles c lawrence comparison with article'
	},
    {
		'name_one': 'charles c leib',
		'name_two': 'charles c. lieb', 
		'expected': True, 
		'description': 'charles c leib comparison with article'
	},
    {
		'name_one': 'charles d de long',
		'name_two': 'charles clifton delong', 
		'expected': False, 
		'description': 'charles d de long comparison with article'
	},
    {
		'name_one': 'charles d lamond',
		'name_two': 'charles lamond', 
		'expected': True, 
		'description': 'charles d lamond comparison with article'
	},
    {
		'name_one': 'charles d spotts',
		'name_two': 'charles dewey spotts', 
		'expected': True, 
		'description': 'charles d spotts comparison with article'
	},
    {
		'name_one': 'charles d van cleave',
		'name_two': 'charles durward van cleave', 
		'expected': True, 
		'description': 'charles d van cleave comparison with article'
	},
    {
		'name_one': 'charles d. davis',
		'name_two': 'charles deforest davis', 
		'expected': True, 
		'description': 'charles d. davis comparison with article'
	},
    {
		'name_one': 'charles debartolo',
		'name_two': 'karl t. barthelmess', 
		'expected': False, 
		'description': 'charles debartolo comparison with article'
	},
    {
		'name_one': 'charles debruler',
		'name_two': 'charles debruler', 
		'expected': True, 
		'description': 'charles debruler comparison with article'
	},
    {
		'name_one': 'charles derleth, jr',
		'name_two': 'charles derleth', 
		'expected': True, 
		'description': 'charles derleth, jr comparison with article'
	},
    {
		'name_one': 'charles e deckbar',
		'name_two': 'p. e. dicker', 
		'expected': False, 
		'description': 'charles e deckbar comparison with article'
	},
    {
		'name_one': 'charles e decker',
		'name_two': 'charles elijah decker', 
		'expected': True, 
		'description': 'charles e decker comparison with article'
	},
    {
		'name_one': 'charles e dewey',
		'name_two': 'charles s. dewey', 
		'expected': False, 
		'description': 'charles e dewey comparison with article'
	},
    {
		'name_one': 'charles e hubbs',
		'name_two': 'carl leavitt hubbs', 
		'expected': False, 
		'description': 'charles e hubbs comparison with article'
	},
    {
		'name_one': 'charles e hurd',
		'name_two': 'charles dewitt hurd', 
		'expected': False, 
		'description': 'charles e hurd comparison with article'
	},
    {
		'name_one': 'charles e landon',
		'name_two': 'charles earl landon', 
		'expected': True, 
		'description': 'charles e landon comparison with article'
	},
    {
		'name_one': 'charles e lane',
		'name_two': 'charles e. lane', 
		'expected': True, 
		'description': 'charles e lane comparison with article'
	},
    {
		'name_one': 'charles e lauer',
		'name_two': 'charles e. lauer', 
		'expected': True, 
		'description': 'charles e lauer comparison with article'
	},
    {
		'name_one': 'charles e leach',
		'name_two': 'charles edward leach', 
		'expected': True, 
		'description': 'charles e leach comparison with article'
	},
    {
		'name_one': 'charles f dean',
		'name_two': 'robert charles dean', 
		'expected': False, 
		'description': 'charles f dean comparison with article'
	},
    {
		'name_one': 'charles f deiss',
		'name_two': 'charles frederick deiss', 
		'expected': True, 
		'description': 'charles f deiss comparison with article'
	},
    {
		'name_one': 'charles f lewis',
		'name_two': 'charles frederick lewis', 
		'expected': True, 
		'description': 'charles f lewis comparison with article'
	},
    {
		'name_one': 'charles f van cleve',
		'name_two': 'charles f. van cleve', 
		'expected': True, 
		'description': 'charles f van cleve comparison with article'
	},
    {
		'name_one': 'charles g decker',
		'name_two': 'charles garfield decker', 
		'expected': True, 
		'description': 'charles g decker comparison with article'
	},
    {
		'name_one': 'charles g lencaln',
		'name_two': 'charles g. lincoln', 
		'expected': True, 
		'description': 'charles g lencaln comparison with article'
	},
    {
		'name_one': 'charles h desgrey',
		'name_two': 'arthur h. desgrey', 
		'expected': False, 
		'description': 'charles h desgrey comparison with article'
	},
    {
		'name_one': 'charles h lange',
		'name_two': 'charles h. lange', 
		'expected': True, 
		'description': 'charles h lange comparison with article'
	},
    {
		'name_one': 'charles h lawshe',
		'name_two': 'charles hubert lawshe', 
		'expected': True, 
		'description': 'charles h lawshe comparison with article'
	},
    {
		'name_one': 'charles h lehman',
		'name_two': 'charles h lehman', 
		'expected': True, 
		'description': 'charles h lehman comparison with article'
	},
    {
		'name_one': 'charles h lesesne, jr',
		'name_two': 'charles haynesworth lesesne', 
		'expected': True, 
		'description': 'charles h lesesne, jr comparison with article'
	},
    {
		'name_one': 'charles h vanduzer',
		'name_two': 'charles h. van duzer', 
		'expected': True, 
		'description': 'charles h vanduzer comparison with article'
	},
    {
		'name_one': 'charles j fawcett',
		'name_two': 'charles dev. fawcett', 
		'expected': False, 
		'description': 'charles j fawcett comparison with article'
	},
    {
		'name_one': 'charles j lakofsky',
		'name_two': 'charles j. lakofsky', 
		'expected': True, 
		'description': 'charles j lakofsky comparison with article'
	},
    {
		'name_one': 'charles l allen',
		'name_two': 'charles laurel allen', 
		'expected': True, 
		'description': 'charles l allen comparison with article'
	},
    {
		'name_one': 'charles l brown',
		'name_two': 'charles lafayette brown', 
		'expected': True, 
		'description': 'charles l brown comparison with article'
	},
    {
		'name_one': 'charles l carroll',
		'name_two': 'charles lemuel carroll', 
		'expected': True, 
		'description': 'charles l carroll comparison with article'
	},
    {
		'name_one': 'charles l jamison',
		'name_two': 'charles laselle jamison', 
		'expected': True, 
		'description': 'charles l jamison comparison with article'
	},
    {
		'name_one': 'charles l latimer',
		'name_two': 'charles trowbridge latimer', 
		'expected': False, 
		'description': 'charles l latimer comparison with article'
	},
    {
		'name_one': 'charles l ozer',
		'name_two': 'charles leonard ozer', 
		'expected': True, 
		'description': 'charles l ozer comparison with article'
	},
    {
		'name_one': 'charles l parmenter',
		'name_two': 'charles leroy parmenter', 
		'expected': True, 
		'description': 'charles l parmenter comparison with article'
	},
    {
		'name_one': 'charles l peacock, sr',
		'name_two': 'charles leroy peacock', 
		'expected': True, 
		'description': 'charles l peacock, sr comparison with article'
	},
    {
		'name_one': 'charles l remington',
		'name_two': 'charles lee remington', 
		'expected': True, 
		'description': 'charles l remington comparison with article'
	},
    {
		'name_one': 'charles l sherman',
		'name_two': 'charles lawton sherman', 
		'expected': True, 
		'description': 'charles l sherman comparison with article'
	},
    {
		'name_one': 'charles l stewart',
		'name_two': 'charles leslie stewart', 
		'expected': True, 
		'description': 'charles l stewart comparison with article'
	},
    {
		'name_one': 'charles larocco',
		'name_two': 'charles gerald la rocco', 
		'expected': True, 
		'description': 'charles larocco comparison with article'
	},
    {
		'name_one': 'charles lassiter',
		'name_two': 'charles albert lassiter', 
		'expected': True, 
		'description': 'charles lassiter comparison with article'
	},
    {
		'name_one': 'charles leroy atkinson',
		'name_two': 'charles l. atkinson', 
		'expected': True, 
		'description': 'charles leroy atkinson comparison with article'
	},
    {
		'name_one': 'charles lewis rasor',
		'name_two': 'charles lewis rasor', 
		'expected': True, 
		'description': 'charles lewis rasor comparison with article'
	},
    {
		'name_one': 'charles m wildes',
		'name_two': 'karl leland wildes', 
		'expected': False, 
		'description': 'charles m wildes comparison with article'
	},
    {
		'name_one': 'charles n lanier, jr',
		'name_two': 'charles n. lanier', 
		'expected': True, 
		'description': 'charles n lanier, jr comparison with article'
	},
    {
		'name_one': 'charles n lebeaux',
		'name_two': 'charles n. lebeaux', 
		'expected': True, 
		'description': 'charles n lebeaux comparison with article'
	},
    {
		'name_one': 'charles r deprima',
		'name_two': 'charles r. deprima', 
		'expected': True, 
		'description': 'charles r deprima comparison with article'
	},
    {
		'name_one': 'charles r masters',
		'name_two': 'charles a. lemaistre', 
		'expected': False, 
		'description': 'charles r masters comparison with article'
	},
    {
		'name_one': 'charles s lane',
		'name_two': 'cecelia s. lane', 
		'expected': False, 
		'description': 'charles s lane comparison with article'
	},
    {
		'name_one': 'charles schalwitz',
		'name_two': 'karl de schweinitz', 
		'expected': False, 
		'description': 'charles schalwitz comparison with article'
	},
    {
		'name_one': 'charles stone',
		'name_two': 'charles leonard stone', 
		'expected': True, 
		'description': 'charles stone comparison with article'
	},
    {
		'name_one': 'charles t lester',
		'name_two': 'charles t. lester', 
		'expected': True, 
		'description': 'charles t lester comparison with article'
	},
    {
		'name_one': 'charles vanbuskirk',
		'name_two': 'chas. van buskirk', 
		'expected': True, 
		'description': 'charles vanbuskirk comparison with article'
	},
    {
		'name_one': 'charles vanderkar',
		'name_two': 'charles william cares', 
		'expected': False, 
		'description': 'charles vanderkar comparison with article'
	},
    {
		'name_one': 'charles w devier',
		'name_two': 'charles w. devier', 
		'expected': True, 
		'description': 'charles w devier comparison with article'
	},
    {
		'name_one': 'charles w lawrence',
		'name_two': 'charles wilson lawrence', 
		'expected': True, 
		'description': 'charles w lawrence comparison with article'
	},
    {
		'name_one': 'charles z lesher',
		'name_two': 'charles zaner lesher', 
		'expected': True, 
		'description': 'charles z lesher comparison with article'
	},
    {
		'name_one': 'charlotte i lee',
		'name_two': 'charlotte i. lee', 
		'expected': True, 
		'description': 'charlotte i lee comparison with article'
	},
    {
		'name_one': 'chas a. larwood',
		'name_two': 'charles h. larwood', 
		'expected': False, 
		'description': 'chas a. larwood comparison with article'
	},
    {
		'name_one': 'chase kearl',
		'name_two': 'chase delmar kearl', 
		'expected': True, 
		'description': 'chase kearl comparison with article'
	},
    {
		'name_one': 'chauncey d harris',
		'name_two': 'chauncy dennison harris', 
		'expected': True, 
		'description': 'chauncey d harris comparison with article'
	},
    {
		'name_one': 'chauncey d holmes',
		'name_two': 'chauncey deppew holmes', 
		'expected': True, 
		'description': 'chauncey d holmes comparison with article'
	},
    {
		'name_one': 'chester a dow',
		'name_two': 'chester laurens dawes', 
		'expected': False, 
		'description': 'chester a dow comparison with article'
	},
    {
		'name_one': 'chester a palmer',
		'name_two': 'chester leroy palmer', 
		'expected': False, 
		'description': 'chester a palmer comparison with article'
	},
    {
		'name_one': 'chester d lee',
		'name_two': 'chester daniel lee', 
		'expected': True, 
		'description': 'chester d lee comparison with article'
	},
    {
		'name_one': 'chester f lay',
		'name_two': 'chester f. lay', 
		'expected': True, 
		'description': 'chester f lay comparison with article'
	},
    {
		'name_one': 'chester m destler',
		'name_two': 'chester mcarthur destler', 
		'expected': True, 
		'description': 'chester m destler comparison with article'
	},
    {
		'name_one': 'chet h lamoure',
		'name_two': 'chet harmon lamore', 
		'expected': True, 
		'description': 'chet h lamoure comparison with article'
	},
    {
		'name_one': 'chiles b van antwerp',
		'name_two': 'chiles van antwerp', 
		'expected': True, 
		'description': 'chiles b van antwerp comparison with article'
	},
    {
		'name_one': 'christian j lambertien',
		'name_two': 'christian j. lambertsen', 
		'expected': True, 
		'description': 'christian j lambertien comparison with article'
	},
    {
		'name_one': 'churchill p lathrop',
		'name_two': 'churchill pierce lathrop', 
		'expected': True, 
		'description': 'churchill p lathrop comparison with article'
	},
    {
		'name_one': 'clair v langton',
		'name_two': 'c. v. langton', 
		'expected': True, 
		'description': 'clair v langton comparison with article'
	},
    {
		'name_one': 'clair v langton',
		'name_two': 'c. v. n. langton', 
		'expected': True, 
		'description': 'clair v langton comparison with article'
	},
    {
		'name_one': 'claire m van leeuven',
		'name_two': 'myron james van leeuwen', 
		'expected': False, 
		'description': 'claire m van leeuven comparison with article'
	},
    {
		'name_one': 'clara l de land',
		'name_two': 'clara hockridge de land', 
		'expected': False, 
		'description': 'clara l de land comparison with article'
	},
    {
		'name_one': 'clara l van nins',
		'name_two': 'l. nanni', 
		'expected': False, 
		'description': 'clara l van nins comparison with article'
	},
    {
		'name_one': 'clara lee tanner',
		'name_two': 'clara lee tanner', 
		'expected': True, 
		'description': 'clara lee tanner comparison with article'
	},
    {
		'name_one': 'clarance vanepps',
		'name_two': 'clarence van epps', 
		'expected': True, 
		'description': 'clarance vanepps comparison with article'
	},
    {
		'name_one': 'clare l marquette',
		'name_two': 'clare leslie marquette', 
		'expected': True, 
		'description': 'clare l marquette comparison with article'
	},
    {
		'name_one': 'clare russell',
		'name_two': 'clare dewitt russell', 
		'expected': True, 
		'description': 'clare russell comparison with article'
	},
    {
		'name_one': 'clarence b hogan',
		'name_two': 'clarence lester hogan', 
		'expected': False, 
		'description': 'clarence b hogan comparison with article'
	},
    {
		'name_one': 'clarence b lafromboise',
		'name_two': 'clarence brown lafromboise', 
		'expected': True, 
		'description': 'clarence b lafromboise comparison with article'
	},
    {
		'name_one': 'clarence c lee',
		'name_two': 'clarence pendleton lee', 
		'expected': False, 
		'description': 'clarence c lee comparison with article'
	},
    {
		'name_one': 'clarence d dieter',
		'name_two': 'clarence dewey dieter', 
		'expected': True, 
		'description': 'clarence d dieter comparison with article'
	},
    {
		'name_one': 'clarence d thorpe',
		'name_two': 'clarence dewitt thorpe', 
		'expected': True, 
		'description': 'clarence d thorpe comparison with article'
	},
    {
		'name_one': 'clarence e deakins',
		'name_two': 'clarence earl deakins', 
		'expected': True, 
		'description': 'clarence e deakins comparison with article'
	},
    {
		'name_one': 'clarence f lewis',
		'name_two': 'clarence flavius lewis', 
		'expected': True, 
		'description': 'clarence f lewis comparison with article'
	},
    {
		'name_one': 'clarence i lewis',
		'name_two': 'clarence irving lewis', 
		'expected': True, 
		'description': 'clarence i lewis comparison with article'
	},
    {
		'name_one': 'clarence l miller',
		'name_two': 'clarence lee miller', 
		'expected': True, 
		'description': 'clarence l miller comparison with article'
	},
    {
		'name_one': 'clarence l nystrom',
		'name_two': 'clarence leroy nystrom', 
		'expected': True, 
		'description': 'clarence l nystrom comparison with article'
	},
    {
		'name_one': 'clarence l turner',
		'name_two': 'clarence lester turner', 
		'expected': True, 
		'description': 'clarence l turner comparison with article'
	},
    {
		'name_one': 'clarence l van sickle',
		'name_two': 'clarence l. vansickle', 
		'expected': True, 
		'description': 'clarence l van sickle comparison with article'
	},
    {
		'name_one': 'clarence lee furrow',
		'name_two': 'clarence lee furrow', 
		'expected': True, 
		'description': 'clarence lee furrow comparison with article'
	},
    {
		'name_one': 'clarence n oliver',
		'name_two': 'clarence leslie oliver', 
		'expected': False, 
		'description': 'clarence n oliver comparison with article'
	},
    {
		'name_one': 'clark j laus',
		'name_two': 'clark john laus', 
		'expected': True, 
		'description': 'clark j laus comparison with article'
	},
    {
		'name_one': 'clark l allen',
		'name_two': 'clark lee allen', 
		'expected': True, 
		'description': 'clark l allen comparison with article'
	},
    {
		'name_one': 'clark l thayer',
		'name_two': 'clark leonard thayer', 
		'expected': True, 
		'description': 'clark l thayer comparison with article'
	},
    {
		'name_one': 'clark o lamberton',
		'name_two': 'clark d. lamberton', 
		'expected': False, 
		'description': 'clark o lamberton comparison with article'
	},
    {
		'name_one': 'claude e lett, jr',
		'name_two': 'martin e. lichte', 
		'expected': False, 
		'description': 'claude e lett, jr comparison with article'
	},
    {
		'name_one': 'claude k deischer',
		'name_two': 'claude knauss deischer', 
		'expected': True, 
		'description': 'claude k deischer comparison with article'
	},
    {
		'name_one': 'claude l finney',
		'name_two': 'claude lee finney', 
		'expected': True, 
		'description': 'claude l finney comparison with article'
	},
    {
		'name_one': 'claude s la dow',
		'name_two': 'claude s. ladow', 
		'expected': True, 
		'description': 'claude s la dow comparison with article'
	},
    {
		'name_one': 'claudine mason',
		'name_two': 'claudine van cleave mason', 
		'expected': True, 
		'description': 'claudine mason comparison with article'
	},
    {
		'name_one': 'clayton l farrar',
		'name_two': 'clayton leon farrar', 
		'expected': True, 
		'description': 'clayton l farrar comparison with article'
	},
    {
		'name_one': 'clem a. leonard',
		'name_two': 'a. byron leonard', 
		'expected': False, 
		'description': 'clem a. leonard comparison with article'
	},
    {
		'name_one': 'clifford barrett',
		'name_two': 'clifford leslie barrett', 
		'expected': True, 
		'description': 'clifford barrett comparison with article'
	},
    {
		'name_one': 'clifford e lampman',
		'name_two': 'clifford e. lampman', 
		'expected': True, 
		'description': 'clifford e lampman comparison with article'
	},
    {
		'name_one': 'clifford l whitman',
		'name_two': 'clifford ler. whitman', 
		'expected': True, 
		'description': 'clifford l whitman comparison with article'
	},
    {
		'name_one': 'clifford l. brownell',
		'name_two': 'clifford lee brownell', 
		'expected': True, 
		'description': 'clifford l. brownell comparison with article'
	},
    {
		'name_one': 'clifton e. van sickle',
		'name_two': 'c. e. vansickle', 
		'expected': True, 
		'description': 'clifton e. van sickle comparison with article'
	},
    {
		'name_one': 'clinton f larson',
		'name_two': 'clinton f. larson', 
		'expected': True, 
		'description': 'clinton f larson comparison with article'
	},
    {
		'name_one': 'clinton l compere',
		'name_two': 'clinton lee compere', 
		'expected': True, 
		'description': 'clinton l compere comparison with article'
	},
    {
		'name_one': 'clyde d mueller',
		'name_two': 'clyde dewey mueller', 
		'expected': True, 
		'description': 'clyde d mueller comparison with article'
	},
    {
		'name_one': 'clyde deming, jr',
		'name_two': 'clyde leroy deming', 
		'expected': True, 
		'description': 'clyde deming, jr comparison with article'
	},
    {
		'name_one': 'clyde l colson',
		'name_two': 'clyde lemuel colson', 
		'expected': True, 
		'description': 'clyde l colson comparison with article'
	},
    {
		'name_one': 'clyde l farrar',
		'name_two': 'clyde leo farrar', 
		'expected': True, 
		'description': 'clyde l farrar comparison with article'
	},
    {
		'name_one': 'clyde v lee',
		'name_two': 'clyde v. lee', 
		'expected': True, 
		'description': 'clyde v lee comparison with article'
	},
    {
		'name_one': 'constant van de wall',
		'name_two': 'constant van de wall', 
		'expected': True, 
		'description': 'constant van de wall comparison with article'
	},
    {
		'name_one': 'cora lee coleman',
		'name_two': 'amoss lee coleman', 
		'expected': False, 
		'description': 'cora lee coleman comparison with article'
	},
    {
		'name_one': 'cristo g coutsibos',
		'name_two': 'r. g. lacount', 
		'expected': False, 
		'description': 'cristo g coutsibos comparison with article'
	},
    {
		'name_one': 'curt leben',
		'name_two': 'curt charles leben', 
		'expected': True, 
		'description': 'curt leben comparison with article'
	},
    {
		'name_one': 'curtis l farrington',
		'name_two': 'curtis leon farrington', 
		'expected': True, 
		'description': 'curtis l farrington comparison with article'
	},
    {
		'name_one': 'cyril l vance',
		'name_two': 'cyril vance', 
		'expected': True, 
		'description': 'cyril l vance comparison with article'
	},
    {
		'name_one': 'cyril r delaney',
		'name_two': 'cyril r. delaney', 
		'expected': True, 
		'description': 'cyril r delaney comparison with article'
	},
    {
		'name_one': 'cyrus l day',
		'name_two': 'cyrus lawrence day', 
		'expected': True, 
		'description': 'cyrus l day comparison with article'
	},
    {
		'name_one': 'd leo hayes',
		'name_two': 'daniel leo hayes', 
		'expected': True, 
		'description': 'd leo hayes comparison with article'
	},
    {
		'name_one': 'd, jack rogers,',
		'name_two': 'jack dean rogers', 
		'expected': True, 
		'description': 'd, jack rogers, comparison with article'
	},
    {
		'name_one': 'dagobert de levie',
		'name_two': 'dagobert de levie', 
		'expected': True, 
		'description': 'dagobert de levie comparison with article'
	},
    {
		'name_one': 'dallas m lancaster',
		'name_two': 'dallas m. lancaster', 
		'expected': True, 
		'description': 'dallas m lancaster comparison with article'
	},
    {
		'name_one': 'dana j. demorest',
		'name_two': 'dana j. demorest', 
		'expected': True, 
		'description': 'dana j. demorest comparison with article'
	},
    {
		'name_one': 'danial m laskin',
		'name_two': 'd. m. laskin', 
		'expected': True, 
		'description': 'danial m laskin comparison with article'
	},
    {
		'name_one': 'daniel d linglebach',
		'name_two': 'daniel dee linglebach', 
		'expected': True, 
		'description': 'daniel d linglebach comparison with article'
	},
    {
		'name_one': 'daniel e vandraegan',
		'name_two': 'daniel vandraegen', 
		'expected': True, 
		'description': 'daniel e vandraegan comparison with article'
	},
    {
		'name_one': 'daniel h levan',
		'name_two': 'daniel jacob levinson', 
		'expected': False, 
		'description': 'daniel h levan comparison with article'
	},
    {
		'name_one': 'daniel l delakas',
		'name_two': 'daniel lindviko delakes', 
		'expected': True, 
		'description': 'daniel l delakas comparison with article'
	},
    {
		'name_one': 'daniel v hageman',
		'name_two': 'daniel vanbrunt hegeman', 
		'expected': True, 
		'description': 'daniel v hageman comparison with article'
	},
    {
		'name_one': 'daris g lafferty',
		'name_two': 'daris grover lafferty', 
		'expected': True, 
		'description': 'daris g lafferty comparison with article'
	},
    {
		'name_one': 'darrell l spriggs',
		'name_two': 'darrell leonard spriggs', 
		'expected': True, 
		'description': 'darrell l spriggs comparison with article'
	},
    {
		'name_one': 'david a ledet',
		'name_two': 'david a. ledet', 
		'expected': True, 
		'description': 'david a ledet comparison with article'
	},
    {
		'name_one': 'david a mac lennan',
		'name_two': 'david alexander maclennan', 
		'expected': True, 
		'description': 'david a mac lennan comparison with article'
	},
    {
		'name_one': 'david b dekker',
		'name_two': 'david bliss dekker', 
		'expected': True, 
		'description': 'david b dekker comparison with article'
	},
    {
		'name_one': 'david d law',
		'name_two': 'david barclay law', 
		'expected': False, 
		'description': 'david d law comparison with article'
	},
    {
		'name_one': 'david f farley',
		'name_two': 'david la bauve farley', 
		'expected': False, 
		'description': 'david f farley comparison with article'
	},
    {
		'name_one': 'david f strain',
		'name_two': 'david o. van strien', 
		'expected': False, 
		'description': 'david f strain comparison with article'
	},
    {
		'name_one': 'david j lamotte',
		'name_two': 'david joseph lamothe', 
		'expected': True, 
		'description': 'david j lamotte comparison with article'
	},
    {
		'name_one': 'david k detweiler',
		'name_two': 'david k. detweiler', 
		'expected': True, 
		'description': 'david k detweiler comparison with article'
	},
    {
		'name_one': 'david l anderson',
		'name_two': 'david leonard anderson', 
		'expected': True, 
		'description': 'david l anderson comparison with article'
	},
    {
		'name_one': 'david l arm',
		'name_two': 'david lehr arm', 
		'expected': True, 
		'description': 'david l arm comparison with article'
	},
    {
		'name_one': 'david l clark',
		'name_two': 'david lee clark', 
		'expected': True, 
		'description': 'david l clark comparison with article'
	},
    {
		'name_one': 'david l dodd',
		'name_two': 'david le fevre dodd', 
		'expected': True, 
		'description': 'david l dodd comparison with article'
	},
    {
		'name_one': 'david l farley',
		'name_two': 'david la bauve farley', 
		'expected': True, 
		'description': 'david l farley comparison with article'
	},
    {
		'name_one': 'david l lawson',
		'name_two': 'edwin david lawson', 
		'expected': False, 
		'description': 'david l lawson comparison with article'
	},
    {
		'name_one': 'david l mackintosh',
		'name_two': 'david leslie mackintosh', 
		'expected': True, 
		'description': 'david l mackintosh comparison with article'
	},
    {
		'name_one': 'david lewis',
		'name_two': 'david lewis', 
		'expected': True, 
		'description': 'david lewis comparison with article'
	},
    {
		'name_one': 'david m deforest',
		'name_two': 'david m. deforest', 
		'expected': True, 
		'description': 'david m deforest comparison with article'
	},
    {
		'name_one': 'david m dennison',
		'name_two': 'david mathias dennison', 
		'expected': True, 
		'description': 'david m dennison comparison with article'
	},
    {
		'name_one': 'david t lapkin',
		'name_two': 'david t. lapkin', 
		'expected': True, 
		'description': 'david t lapkin comparison with article'
	},
    {
		'name_one': 'david v lawrence',
		'name_two': 'david lawrence', 
		'expected': True, 
		'description': 'david v lawrence comparison with article'
	},
    {
		'name_one': 'david van meter',
		'name_two': 'david van meter', 
		'expected': True, 
		'description': 'david van meter comparison with article'
	},
    {
		'name_one': 'david van vactor',
		'name_two': 'david g. vanvactor', 
		'expected': True, 
		'description': 'david van vactor comparison with article'
	},
    {
		'name_one': 'dean d pearl',
		'name_two': 'herbert dean pearl', 
		'expected': False, 
		'description': 'dean d pearl comparison with article'
	},
    {
		'name_one': 'dean e babbage',
		'name_two': 'e. dean babbage', 
		'expected': True, 
		'description': 'dean e babbage comparison with article'
	},
    {
		'name_one': 'deane l lawrence',
		'name_two': 'laszlo lorand', 
		'expected': False, 
		'description': 'deane l lawrence comparison with article'
	},
    {
		'name_one': 'deane lent',
		'name_two': 'deane lent', 
		'expected': True, 
		'description': 'deane lent comparison with article'
	},
    {
		'name_one': 'delbert l rutledge',
		'name_two': 'delbert leroy rutledge', 
		'expected': True, 
		'description': 'delbert l rutledge comparison with article'
	},
    {
		'name_one': 'delight m maughan',
		'name_two': 'h. delight maughan', 
		'expected': False, 
		'description': 'delight m maughan comparison with article'
	},
    {
		'name_one': 'della lehman',
		'name_two': 'della lehman', 
		'expected': True, 
		'description': 'della lehman comparison with article'
	},
    {
		'name_one': 'delmar leighton, jr',
		'name_two': 'delmar leighton', 
		'expected': True, 
		'description': 'delmar leighton, jr comparison with article'
	},
    {
		'name_one': 'dennis anderson',
		'name_two': 'ira dennis anderson', 
		'expected': True, 
		'description': 'dennis anderson comparison with article'
	},
    {
		'name_one': 'denoe leedy',
		'name_two': 'charles denoe leedy', 
		'expected': True, 
		'description': 'denoe leedy comparison with article'
	},
    {
		'name_one': 'dexter j hill',
		'name_two': 'j. levan hill', 
		'expected': False, 
		'description': 'dexter j hill comparison with article'
	},
    {
		'name_one': 'dexter levy',
		'name_two': 'dexter s. levy', 
		'expected': True, 
		'description': 'dexter levy comparison with article'
	},
    {
		'name_one': 'diane j de lotto',
		'name_two': 'marcel j. de lotto', 
		'expected': False, 
		'description': 'diane j de lotto comparison with article'
	},
    {
		'name_one': 'dick s vanfleet',
		'name_two': 'dick scott van fleet', 
		'expected': True, 
		'description': 'dick s vanfleet comparison with article'
	},
    {
		'name_one': 'dietrich hildebrand',
		'name_two': 'dietrich von hildebrand', 
		'expected': True, 
		'description': 'dietrich hildebrand comparison with article'
	},
    {
		'name_one': 'dinna p lipkin',
		'name_two': 'peter p. lapiken', 
		'expected': False, 
		'description': 'dinna p lipkin comparison with article'
	},
    {
		'name_one': 'dixy lee ray',
		'name_two': 'dixy lee ray', 
		'expected': True, 
		'description': 'dixy lee ray comparison with article'
	},
    {
		'name_one': 'don d lescohier',
		'name_two': 'don divance lescohier', 
		'expected': True, 
		'description': 'don d lescohier comparison with article'
	},
    {
		'name_one': 'don l good',
		'name_two': 'don ladoyt good', 
		'expected': True, 
		'description': 'don l good comparison with article'
	},
    {
		'name_one': 'don l. demorest',
		'name_two': 'don l. demorest', 
		'expected': True, 
		'description': 'don l. demorest comparison with article'
	},
    {
		'name_one': 'don lewis',
		'name_two': 'don lewis', 
		'expected': True, 
		'description': 'don lewis comparison with article'
	},
    {
		'name_one': 'donald a lentz',
		'name_two': 'donald a. lentz', 
		'expected': True, 
		'description': 'donald a lentz comparison with article'
	},
    {
		'name_one': 'donald b lawrence',
		'name_two': 'donald b. lawrence', 
		'expected': True, 
		'description': 'donald b lawrence comparison with article'
	},
    {
		'name_one': 'donald darickson',
		'name_two': 'donald derickson', 
		'expected': True, 
		'description': 'donald darickson comparison with article'
	},
    {
		'name_one': 'donald deford',
		'name_two': 'donald dale deford', 
		'expected': True, 
		'description': 'donald deford comparison with article'
	},
    {
		'name_one': 'donald devault',
		'name_two': 'don devault', 
		'expected': True, 
		'description': 'donald devault comparison with article'
	},
    {
		'name_one': 'donald e stewart',
		'name_two': 'donald dean stewart', 
		'expected': False, 
		'description': 'donald e stewart comparison with article'
	},
    {
		'name_one': 'donald e. lowell',
		'name_two': 'edgar lafayette lowell', 
		'expected': False, 
		'description': 'donald e. lowell comparison with article'
	},
    {
		'name_one': 'donald f lake',
		'name_two': 'donald frederick lach', 
		'expected': True, 
		'description': 'donald f lake comparison with article'
	},
    {
		'name_one': 'donald fabian',
		'name_two': 'donald leroy fabian', 
		'expected': True, 
		'description': 'donald fabian comparison with article'
	},
    {
		'name_one': 'donald g lee',
		'name_two': 'donald g. lee', 
		'expected': True, 
		'description': 'donald g lee comparison with article'
	},
    {
		'name_one': 'donald g. decker',
		'name_two': 'donald gilmore decker', 
		'expected': True, 
		'description': 'donald g. decker comparison with article'
	},
    {
		'name_one': 'donald i augustine',
		'name_two': 'donald leslie augustine', 
		'expected': False, 
		'description': 'donald i augustine comparison with article'
	},
    {
		'name_one': 'donald j dettinger',
		'name_two': 'donald j. dettinger', 
		'expected': True, 
		'description': 'donald j dettinger comparison with article'
	},
    {
		'name_one': 'donald j lewis',
		'name_two': 'donald joseph lewis', 
		'expected': True, 
		'description': 'donald j lewis comparison with article'
	},
    {
		'name_one': 'donald l heinemeyer',
		'name_two': 'donald leroy heinemeyer', 
		'expected': True, 
		'description': 'donald l heinemeyer comparison with article'
	},
    {
		'name_one': 'donald l katz',
		'name_two': 'donald laverne katz', 
		'expected': True, 
		'description': 'donald l katz comparison with article'
	},
    {
		'name_one': 'donald lake',
		'name_two': 'donald l. lake', 
		'expected': True, 
		'description': 'donald lake comparison with article'
	},
    {
		'name_one': 'donald le tendre',
		'name_two': 'donald henry letendre', 
		'expected': True, 
		'description': 'donald le tendre comparison with article'
	},
    {
		'name_one': 'donald murphy',
		'name_two': 'donald van dale murphy', 
		'expected': True, 
		'description': 'donald murphy comparison with article'
	},
    {
		'name_one': 'donald r larsen',
		'name_two': 'donald r. larson', 
		'expected': True, 
		'description': 'donald r larsen comparison with article'
	},
    {
		'name_one': 'donald w del carlo',
		'name_two': 'donald w. de carle', 
		'expected': True, 
		'description': 'donald w del carlo comparison with article'
	},
    {
		'name_one': 'doris e lees',
		'name_two': 'doris estabrook lees', 
		'expected': True, 
		'description': 'doris e lees comparison with article'
	},
    {
		'name_one': 'doris f larsen',
		'name_two': 'bent f. larsen', 
		'expected': False, 
		'description': 'doris f larsen comparison with article'
	},
    {
		'name_one': 'dorothy c lee',
		'name_two': 'shu-ching lee', 
		'expected': False, 
		'description': 'dorothy c lee comparison with article'
	},
    {
		'name_one': 'dorothy dean',
		'name_two': 'dorothy dean', 
		'expected': True, 
		'description': 'dorothy dean comparison with article'
	},
    {
		'name_one': 'dorothy delany',
		'name_two': 'dorothy celia delany', 
		'expected': True, 
		'description': 'dorothy delany comparison with article'
	},
    {
		'name_one': 'dorothy f deach',
		'name_two': 'dorothy f. deach', 
		'expected': True, 
		'description': 'dorothy f deach comparison with article'
	},
    {
		'name_one': 'dorothy jean laubacher',
		'name_two': 'dorothy laubacher', 
		'expected': True, 
		'description': 'dorothy jean laubacher comparison with article'
	},
    {
		'name_one': 'dorothy l fuller',
		'name_two': 'dorothy langford fuller', 
		'expected': True, 
		'description': 'dorothy l fuller comparison with article'
	},
    {
		'name_one': 'dorothy l large',
		'name_two': 'dorothy large', 
		'expected': True, 
		'description': 'dorothy l large comparison with article'
	},
    {
		'name_one': 'dorothy leahy',
		'name_two': 'dorothy leahy', 
		'expected': True, 
		'description': 'dorothy leahy comparison with article'
	},
    {
		'name_one': 'dorothy lee hayes',
		'name_two': 'dorothy hayes', 
		'expected': True, 
		'description': 'dorothy lee hayes comparison with article'
	},
    {
		'name_one': 'dorothy levine',
		'name_two': 'dorothy levens', 
		'expected': False, 
		'description': 'dorothy levine comparison with article'
	},
    {
		'name_one': 'dorothy m lasalle',
		'name_two': 'dorothy m. lasalle', 
		'expected': True, 
		'description': 'dorothy m lasalle comparison with article'
	},
    {
		'name_one': 'dorothy mac lean',
		'name_two': 'dorothy g. maclean', 
		'expected': True, 
		'description': 'dorothy mac lean comparison with article'
	},
    {
		'name_one': 'dorothy v a fuller',
		'name_two': 'dorothy van arsdale fuller', 
		'expected': True, 
		'description': 'dorothy v a fuller comparison with article'
	},
    {
		'name_one': 'dorothy w dennis',
		'name_two': 'dorothy warner dennis', 
		'expected': True, 
		'description': 'dorothy w dennis comparison with article'
	},
    {
		'name_one': 'dorsey d jones',
		'name_two': 'dorsey dee jones', 
		'expected': True, 
		'description': 'dorsey d jones comparison with article'
	},
    {
		'name_one': 'dorsey e lane',
		'name_two': 'dorsey e. lane', 
		'expected': True, 
		'description': 'dorsey e lane comparison with article'
	},
    {
		'name_one': 'dorval d despres',
		'name_two': 'solveig d. preus', 
		'expected': False, 
		'description': 'dorval d despres comparison with article'
	},
    {
		'name_one': 'douglas d martin',
		'name_two': 'douglas deveny martin', 
		'expected': True, 
		'description': 'douglas d martin comparison with article'
	},
    {
		'name_one': 'douglas e lawson',
		'name_two': 'douglas e. lawson', 
		'expected': True, 
		'description': 'douglas e lawson comparison with article'
	},
    {
		'name_one': 'douglas h lawrence',
		'name_two': 'douglas howard lawrence', 
		'expected': True, 
		'description': 'douglas h lawrence comparison with article'
	},
    {
		'name_one': 'douglas l kraus',
		'name_two': 'douglas lawrence kraus', 
		'expected': True, 
		'description': 'douglas l kraus comparison with article'
	},
    {
		'name_one': 'douglass lathwell',
		'name_two': 'douglas j. lathwell', 
		'expected': True, 
		'description': 'douglass lathwell comparison with article'
	},
    {
		'name_one': 'dr alphonse vonderahe',
		'name_two': 'alphonse r. vonderahe', 
		'expected': True, 
		'description': 'dr alphonse vonderahe comparison with article'
	},
    {
		'name_one': 'dr howard l alt',
		'name_two': 'howard lang alt', 
		'expected': True, 
		'description': 'dr howard l alt comparison with article'
	},
    {
		'name_one': 'dr leonard aguilino',
		'name_two': 'leonard m. aquilino', 
		'expected': True, 
		'description': 'dr leonard aguilino comparison with article'
	},
    {
		'name_one': 'dr. lester r cahn',
		'name_two': 'lester r. cahn', 
		'expected': True, 
		'description': 'dr. lester r cahn comparison with article'
	},
    {
		'name_one': 'dudley d carroll',
		'name_two': 'dudley dewitt carroll', 
		'expected': True, 
		'description': 'dudley d carroll comparison with article'
	},
    {
		'name_one': 'dwight e lee',
		'name_two': 'dwight erwin lee', 
		'expected': True, 
		'description': 'dwight e lee comparison with article'
	},
    {
		'name_one': 'dwight l ling',
		'name_two': 'dwight leroy ling', 
		'expected': True, 
		'description': 'dwight l ling comparison with article'
	},
    {
		'name_one': 'dwight l spencer, jr',
		'name_two': 'guilford lawson spencer', 
		'expected': False, 
		'description': 'dwight l spencer, jr comparison with article'
	},
    {
		'name_one': 'dwight m delong',
		'name_two': 'dwight m. delong', 
		'expected': True, 
		'description': 'dwight m delong comparison with article'
	},
    {
		'name_one': 'e donald lawrence',
		'name_two': 'e. donald lawrence', 
		'expected': True, 
		'description': 'e donald lawrence comparison with article'
	},
    {
		'name_one': 'e harold laws',
		'name_two': 'e. harold laws', 
		'expected': True, 
		'description': 'e harold laws comparison with article'
	},
    {
		'name_one': 'e lane davis',
		'name_two': 'edward lane davis', 
		'expected': True, 
		'description': 'e lane davis comparison with article'
	},
    {
		'name_one': 'e lee goldsborough',
		'name_two': 'e. lee goldsborough', 
		'expected': True, 
		'description': 'e lee goldsborough comparison with article'
	},
    {
		'name_one': 'e lee kinsey',
		'name_two': 'e. lee kinsey', 
		'expected': True, 
		'description': 'e lee kinsey comparison with article'
	},
    {
		'name_one': 'e lewis morris',
		'name_two': 'lewis r. morris', 
		'expected': False, 
		'description': 'e lewis morris comparison with article'
	},
    {
		'name_one': 'e richard larson',
		'name_two': 'e. richard larson', 
		'expected': True, 
		'description': 'e richard larson comparison with article'
	},
    {
		'name_one': 'e virginia lewis',
		'name_two': 'virginia e. lewis', 
		'expected': True, 
		'description': 'e virginia lewis comparison with article'
	},
    {
		'name_one': 'earl l butz',
		'name_two': 'earl lauer butz', 
		'expected': True, 
		'description': 'earl l butz comparison with article'
	},
    {
		'name_one': 'earl l core',
		'name_two': 'earl lemley core', 
		'expected': True, 
		'description': 'earl l core comparison with article'
	},
    {
		'name_one': 'earl l farmer',
		'name_two': 'earl leroy farmer', 
		'expected': True, 
		'description': 'earl l farmer comparison with article'
	},
    {
		'name_one': 'earl l griggs',
		'name_two': 'earl leslie griggs', 
		'expected': True, 
		'description': 'earl l griggs comparison with article'
	},
    {
		'name_one': 'earl l martin',
		'name_two': 'earl leslie martin', 
		'expected': True, 
		'description': 'earl l martin comparison with article'
	},
    {
		'name_one': 'earl l stone, jr',
		'name_two': 'earl lewis stone', 
		'expected': True, 
		'description': 'earl l stone, jr comparison with article'
	},
    {
		'name_one': 'earl l vance',
		'name_two': 'earl lynn vance', 
		'expected': True, 
		'description': 'earl l vance comparison with article'
	},
    {
		'name_one': 'earl latham',
		'name_two': 'earl latham', 
		'expected': True, 
		'description': 'earl latham comparison with article'
	},
    {
		'name_one': 'earl p lasher, jr',
		'name_two': 'earl parsons lasher', 
		'expected': True, 
		'description': 'earl p lasher, jr comparison with article'
	},
    {
		'name_one': 'earl r leng',
		'name_two': 'earl r. leng', 
		'expected': True, 
		'description': 'earl r leng comparison with article'
	},
    {
		'name_one': 'earl s howard',
		'name_two': 'earl dean howard', 
		'expected': False, 
		'description': 'earl s howard comparison with article'
	},
    {
		'name_one': 'earnest langley',
		'name_two': 'ernest felix langley', 
		'expected': True, 
		'description': 'earnest langley comparison with article'
	},
    {
		'name_one': 'edgar l lazier',
		'name_two': 'edgar l. lazier', 
		'expected': True, 
		'description': 'edgar l lazier comparison with article'
	},
    {
		'name_one': 'edgar l mcgowan',
		'name_two': 'edgar leon mcgowan', 
		'expected': True, 
		'description': 'edgar l mcgowan comparison with article'
	},
    {
		'name_one': 'edgar lewis winfrey',
		'name_two': 'lewis edgar winfrey', 
		'expected': True, 
		'description': 'edgar lewis winfrey comparison with article'
	},
    {
		'name_one': 'edgar w lacy',
		'name_two': 'edgar wilson lacy', 
		'expected': True, 
		'description': 'edgar w lacy comparison with article'
	},
    {
		'name_one': 'edith a laue',
		'name_two': 'edith a. laue', 
		'expected': True, 
		'description': 'edith a laue comparison with article'
	},
    {
		'name_one': 'edith layer',
		'name_two': 'edith e. layer', 
		'expected': True, 
		'description': 'edith layer comparison with article'
	},
    {
		'name_one': 'edith m branin',
		'name_two': 'm. lelyn branin', 
		'expected': False, 
		'description': 'edith m branin comparison with article'
	},
    {
		'name_one': 'edith m derrick',
		'name_two': 'lawrence m. derickier', 
		'expected': False, 
		'description': 'edith m derrick comparison with article'
	},
    {
		'name_one': 'edmund d lewandowski',
		'name_two': 'edmund d. lewandowski', 
		'expected': True, 
		'description': 'edmund d lewandowski comparison with article'
	},
    {
		'name_one': 'edmund h campbell',
		'name_two': 'edmund lee gamble', 
		'expected': False, 
		'description': 'edmund h campbell comparison with article'
	},
    {
		'name_one': 'edmund p learned',
		'name_two': 'edmund philip learned', 
		'expected': True, 
		'description': 'edmund p learned comparison with article'
	},
    {
		'name_one': 'edmund v laitone',
		'name_two': 'edmund v. laitone', 
		'expected': True, 
		'description': 'edmund v laitone comparison with article'
	},
    {
		'name_one': 'edna landros',
		'name_two': 'edna landros', 
		'expected': True, 
		'description': 'edna landros comparison with article'
	},
    {
		'name_one': 'edna m lawrence',
		'name_two': 'edna w. lawrence', 
		'expected': False, 
		'description': 'edna m lawrence comparison with article'
	},
    {
		'name_one': 'edna w lewis',
		'name_two': 'edna lewis', 
		'expected': True, 
		'description': 'edna w lewis comparison with article'
	},
    {
		'name_one': 'edward a gibbs',
		'name_two': 'edward delmar gibbs', 
		'expected': False, 
		'description': 'edward a gibbs comparison with article'
	},
    {
		'name_one': 'edward a lavin',
		'name_two': 'edward a. levin', 
		'expected': True, 
		'description': 'edward a lavin comparison with article'
	},
    {
		'name_one': 'edward b lawton, jr',
		'name_two': 'edward b. lawton', 
		'expected': True, 
		'description': 'edward b lawton, jr comparison with article'
	},
    {
		'name_one': 'edward b lewis',
		'name_two': 'edward b. lewis', 
		'expected': True, 
		'description': 'edward b lewis comparison with article'
	},
    {
		'name_one': 'edward bassett',
		'name_two': 'edward lewis bassett', 
		'expected': True, 
		'description': 'edward bassett comparison with article'
	},
    {
		'name_one': 'edward c lambert',
		'name_two': 'edward c. lambert', 
		'expected': True, 
		'description': 'edward c lambert comparison with article'
	},
    {
		'name_one': 'edward c lambert',
		'name_two': 'edward charles lambert', 
		'expected': True, 
		'description': 'edward c lambert comparison with article'
	},
    {
		'name_one': 'edward c lesch',
		'name_two': 'edward c. a. lesch', 
		'expected': True, 
		'description': 'edward c lesch comparison with article'
	},
    {
		'name_one': 'edward d lafferty',
		'name_two': 'd. lafferty', 
		'expected': True, 
		'description': 'edward d lafferty comparison with article'
	},
    {
		'name_one': 'edward d myers',
		'name_two': 'edward delos myers', 
		'expected': True, 
		'description': 'edward d myers comparison with article'
	},
    {
		'name_one': 'edward d seeber',
		'name_two': 'edward derbyshire seeber', 
		'expected': True, 
		'description': 'edward d seeber comparison with article'
	},
    {
		'name_one': 'edward de s matthews,s',
		'name_two': 'edward desaunhac matthews', 
		'expected': True, 
		'description': 'edward de s matthews,s comparison with article'
	},
    {
		'name_one': 'edward dean christensen',
		'name_two': 'edward l. christensen', 
		'expected': False, 
		'description': 'edward dean christensen comparison with article'
	},
    {
		'name_one': 'edward e landis',
		'name_two': 'edward everett landis', 
		'expected': True, 
		'description': 'edward e landis comparison with article'
	},
    {
		'name_one': 'edward erikson',
		'name_two': 'edward leerdrup eriksen', 
		'expected': True, 
		'description': 'edward erikson comparison with article'
	},
    {
		'name_one': 'edward g lewis',
		'name_two': 'edward g. lewis', 
		'expected': True, 
		'description': 'edward g lewis comparison with article'
	},
    {
		'name_one': 'edward g van bibber',
		'name_two': 'george van bibber', 
		'expected': True, 
		'description': 'edward g van bibber comparison with article'
	},
    {
		'name_one': 'edward h davis',
		'name_two': 'edward smith deevey', 
		'expected': False, 
		'description': 'edward h davis comparison with article'
	},
    {
		'name_one': 'edward h la forge',
		'name_two': 'edward h. lafarge', 
		'expected': True, 
		'description': 'edward h la forge comparison with article'
	},
    {
		'name_one': 'edward h leach',
		'name_two': 'mac edward leach', 
		'expected': False, 
		'description': 'edward h leach comparison with article'
	},
    {
		'name_one': 'edward h lepper',
		'name_two': 'm. h. lepper', 
		'expected': False, 
		'description': 'edward h lepper comparison with article'
	},
    {
		'name_one': 'edward j larkin',
		'name_two': 'edward j larkin', 
		'expected': True, 
		'description': 'edward j larkin comparison with article'
	},
    {
		'name_one': 'edward j lawrence',
		'name_two': 'edward j. lorenze', 
		'expected': True, 
		'description': 'edward j lawrence comparison with article'
	},
    {
		'name_one': 'edward j lazear, jr',
		'name_two': 'edward j. lazear', 
		'expected': True, 
		'description': 'edward j lazear, jr comparison with article'
	},
    {
		'name_one': 'edward j van liere',
		'name_two': 'edward gerald van liere', 
		'expected': False, 
		'description': 'edward j van liere comparison with article'
	},
    {
		'name_one': 'edward j vanloon',
		'name_two': 'edward j. van loon', 
		'expected': True, 
		'description': 'edward j vanloon comparison with article'
	},
    {
		'name_one': 'edward k lebohner',
		'name_two': 'edward k. lebohner', 
		'expected': True, 
		'description': 'edward k lebohner comparison with article'
	},
    {
		'name_one': 'edward l clark',
		'name_two': 'edward lester clark', 
		'expected': True, 
		'description': 'edward l clark comparison with article'
	},
    {
		'name_one': 'edward l emling',
		'name_two': 'edward langhoff emling', 
		'expected': True, 
		'description': 'edward l emling comparison with article'
	},
    {
		'name_one': 'edward l howes',
		'name_two': 'edward lee howes', 
		'expected': True, 
		'description': 'edward l howes comparison with article'
	},
    {
		'name_one': 'edward l jenkins',
		'name_two': 'edward lealand jenkinson', 
		'expected': True, 
		'description': 'edward l jenkins comparison with article'
	},
    {
		'name_one': 'edward l king',
		'name_two': 'edward lacy king', 
		'expected': True, 
		'description': 'edward l king comparison with article'
	},
    {
		'name_one': 'edward l tatum',
		'name_two': 'edward lawrie tatum', 
		'expected': True, 
		'description': 'edward l tatum comparison with article'
	},
    {
		'name_one': 'edward lathrop',
		'name_two': 'edward flint lathrop', 
		'expected': True, 
		'description': 'edward lathrop comparison with article'
	},
    {
		'name_one': 'edward lecomte',
		'name_two': 'edward s. le comte', 
		'expected': True, 
		'description': 'edward lecomte comparison with article'
	},
    {
		'name_one': 'edward lee dorsett',
		'name_two': 'edward lee dorsett', 
		'expected': True, 
		'description': 'edward lee dorsett comparison with article'
	},
    {
		'name_one': 'edward leonard, jr',
		'name_two': 'edward leonard', 
		'expected': True, 
		'description': 'edward leonard, jr comparison with article'
	},
    {
		'name_one': 'edward lowson',
		'name_two': 'edward f. lewison', 
		'expected': False, 
		'description': 'edward lowson comparison with article'
	},
    {
		'name_one': 'edward p lana',
		'name_two': 'edward p. lana', 
		'expected': True, 
		'description': 'edward p lana comparison with article'
	},
    {
		'name_one': 'edward r dezurko',
		'name_two': 'e. r. dezurko', 
		'expected': True, 
		'description': 'edward r dezurko comparison with article'
	},
    {
		'name_one': 'edward t ladd',
		'name_two': 'edward taylor ladd', 
		'expected': True, 
		'description': 'edward t ladd comparison with article'
	},
    {
		'name_one': 'edward van ormer',
		'name_two': 'edward b. van ormer', 
		'expected': True, 
		'description': 'edward van ormer comparison with article'
	},
    {
		'name_one': 'edward van winkle',
		'name_two': 'edward hasbrouck van winkle', 
		'expected': True, 
		'description': 'edward van winkle comparison with article'
	},
    {
		'name_one': 'edward wallace',
		'name_two': 'edward leon wallace', 
		'expected': True, 
		'description': 'edward wallace comparison with article'
	},
    {
		'name_one': 'edwin a lee',
		'name_two': 'edwin a. lee', 
		'expected': True, 
		'description': 'edwin a lee comparison with article'
	},
    {
		'name_one': 'edwin b langston',
		'name_two': 'beach langston', 
		'expected': True, 
		'description': 'edwin b langston comparison with article'
	},
    {
		'name_one': 'edwin h lewis',
		'name_two': 'edwin h lewis', 
		'expected': True, 
		'description': 'edwin h lewis comparison with article'
	},
    {
		'name_one': 'edwin j lamont',
		'name_two': 'edwin i. lamont', 
		'expected': False, 
		'description': 'edwin j lamont comparison with article'
	},
    {
		'name_one': 'edwin j lanwerth',
		'name_two': 'edwin j lanwerth', 
		'expected': True, 
		'description': 'edwin j lanwerth comparison with article'
	},
    {
		'name_one': 'edwin l lame',
		'name_two': 'edwin l. lame', 
		'expected': True, 
		'description': 'edwin l lame comparison with article'
	},
    {
		'name_one': 'edwin l levy',
		'name_two': 'edwin l. levy', 
		'expected': True, 
		'description': 'edwin l levy comparison with article'
	},
    {
		'name_one': 'edwin l miller',
		'name_two': 'edwin lawrence miller', 
		'expected': True, 
		'description': 'edwin l miller comparison with article'
	},
    {
		'name_one': 'edwin l theiss',
		'name_two': 'edwin leodgar theiss', 
		'expected': True, 
		'description': 'edwin l theiss comparison with article'
	},
    {
		'name_one': 'edwin l williams',
		'name_two': 'edwin lea williams', 
		'expected': True, 
		'description': 'edwin l williams comparison with article'
	},
    {
		'name_one': 'edwin m larsen',
		'name_two': 'edwin merritt larsen', 
		'expected': True, 
		'description': 'edwin m larsen comparison with article'
	},
    {
		'name_one': 'edwin mclean',
		'name_two': 'martin edwin lean', 
		'expected': True, 
		'description': 'edwin mclean comparison with article'
	},
    {
		'name_one': 'edwin n. lassettre',
		'name_two': 'edwin n. lassettre', 
		'expected': True, 
		'description': 'edwin n. lassettre comparison with article'
	},
    {
		'name_one': 'elbert persons',
		'name_two': 'elbert lapsley persons', 
		'expected': True, 
		'description': 'elbert persons comparison with article'
	},
    {
		'name_one': 'elbridge p vance',
		'name_two': 'elbridge putnam vance', 
		'expected': True, 
		'description': 'elbridge p vance comparison with article'
	},
    {
		'name_one': 'elden e leasure, 2nd',
		'name_two': 'elden emanuel leasure', 
		'expected': True, 
		'description': 'elden e leasure, 2nd comparison with article'
	},
    {
		'name_one': 'eleanor a rhodes',
		'name_two': 'arnold densmore rhodes', 
		'expected': False, 
		'description': 'eleanor a rhodes comparison with article'
	},
    {
		'name_one': 'eleanor delfs',
		'name_two': 'eleanor delfs', 
		'expected': True, 
		'description': 'eleanor delfs comparison with article'
	},
    {
		'name_one': 'eleanor leek',
		'name_two': 'eleanor leek', 
		'expected': True, 
		'description': 'eleanor leek comparison with article'
	},
    {
		'name_one': 'eleanor lewis',
		'name_two': 'eleanor lewis', 
		'expected': True, 
		'description': 'eleanor lewis comparison with article'
	},
    {
		'name_one': 'eli m levine',
		'name_two': 'eli m. levine', 
		'expected': True, 
		'description': 'eli m levine comparison with article'
	},
    {
		'name_one': 'eline m von borries',
		'name_two': 'eline von borries', 
		'expected': True, 
		'description': 'eline m von borries comparison with article'
	},
    {
		'name_one': 'elizabeth h leduc',
		'name_two': 'elizabeth h. leduc', 
		'expected': True, 
		'description': 'elizabeth h leduc comparison with article'
	},
    {
		'name_one': 'elizabeth hanscom',
		'name_two': 'elizabeth deering hanscom', 
		'expected': True, 
		'description': 'elizabeth hanscom comparison with article'
	},
    {
		'name_one': 'elizabeth lanham',
		'name_two': 'elizabeth lanham', 
		'expected': True, 
		'description': 'elizabeth lanham comparison with article'
	},
    {
		'name_one': 'elizabeth lawrence',
		'name_two': 'elizabeth lawrence', 
		'expected': True, 
		'description': 'elizabeth lawrence comparison with article'
	},
    {
		'name_one': 'elizabeth m lasley',
		'name_two': 'mary elizabeth lasley', 
		'expected': True, 
		'description': 'elizabeth m lasley comparison with article'
	},
    {
		'name_one': 'elizabeth n barkett',
		'name_two': 'nasry fayad vander barkett', 
		'expected': False, 
		'description': 'elizabeth n barkett comparison with article'
	},
    {
		'name_one': 'elizabeth s moths',
		'name_two': 'miltiades s. demos', 
		'expected': False, 
		'description': 'elizabeth s moths comparison with article'
	},
    {
		'name_one': 'ella a ray',
		'name_two': 'ella de los reyes', 
		'expected': True, 
		'description': 'ella a ray comparison with article'
	},
    {
		'name_one': 'ella ray',
		'name_two': 'ella de los reyes', 
		'expected': True, 
		'description': 'ella ray comparison with article'
	},
    {
		'name_one': 'ellen dearing',
		'name_two': 'ellen l deering', 
		'expected': True, 
		'description': 'ellen dearing comparison with article'
	},
    {
		'name_one': 'elliott diller',
		'name_two': 'elliot van nostrand diller', 
		'expected': True, 
		'description': 'elliott diller comparison with article'
	},
    {
		'name_one': 'ellis a lasky',
		'name_two': 'mortimer a. lasky', 
		'expected': False, 
		'description': 'ellis a lasky comparison with article'
	},
    {
		'name_one': 'ellis p leonard',
		'name_two': 'ellis pierson leonard', 
		'expected': True, 
		'description': 'ellis p leonard comparison with article'
	},
    {
		'name_one': 'ellis t. demars',
		'name_two': 'e. theodore demars', 
		'expected': True, 
		'description': 'ellis t. demars comparison with article'
	},
    {
		'name_one': 'ellwood d rushworth',
		'name_two': 'ellwood derrick rushworth', 
		'expected': True, 
		'description': 'ellwood d rushworth comparison with article'
	},
    {
		'name_one': 'elmer a leslie',
		'name_two': 'elmer archibald leslie', 
		'expected': True, 
		'description': 'elmer a leslie comparison with article'
	},
    {
		'name_one': 'elmer de gowin',
		'name_two': 'elmer louis degowin', 
		'expected': True, 
		'description': 'elmer de gowin comparison with article'
	},
    {
		'name_one': 'elmer l lucas',
		'name_two': 'elmer lawrence lucas', 
		'expected': True, 
		'description': 'elmer l lucas comparison with article'
	},
    {
		'name_one': 'elmer l mcbride',
		'name_two': 'elmer leon mcbride', 
		'expected': True, 
		'description': 'elmer l mcbride comparison with article'
	},
    {
		'name_one': 'elmer l whitman',
		'name_two': 'elmer leroy whitman', 
		'expected': True, 
		'description': 'elmer l whitman comparison with article'
	},
    {
		'name_one': 'elsa dehaas',
		'name_two': 'elsa de haas', 
		'expected': True, 
		'description': 'elsa dehaas comparison with article'
	},
    {
		'name_one': 'elsie h leicester',
		'name_two': 'katherine h. leicester', 
		'expected': False, 
		'description': 'elsie h leicester comparison with article'
	},
    {
		'name_one': 'elta vannorman',
		'name_two': 'c. elta van norman', 
		'expected': True, 
		'description': 'elta vannorman comparison with article'
	},
    {
		'name_one': 'elton l quinn',
		'name_two': 'elton leroy quinn', 
		'expected': True, 
		'description': 'elton l quinn comparison with article'
	},
    {
		'name_one': 'elva leawton',
		'name_two': 'elva lawton', 
		'expected': True, 
		'description': 'elva leawton comparison with article'
	},
    {
		'name_one': 'elvin r latty',
		'name_two': 'elvin remus latty', 
		'expected': True, 
		'description': 'elvin r latty comparison with article'
	},
    {
		'name_one': 'emanual delgado',
		'name_two': 'jose manuel rodriguez delgado', 
		'expected': True, 
		'description': 'emanual delgado comparison with article'
	},
    {
		'name_one': 'emanuel levin',
		'name_two': 'emanuel jack levin', 
		'expected': True, 
		'description': 'emanuel levin comparison with article'
	},
    {
		'name_one': 'emeric a lawrence',
		'name_two': 'emeric a. lawrence', 
		'expected': True, 
		'description': 'emeric a lawrence comparison with article'
	},
    {
		'name_one': 'emery leffel',
		'name_two': 'emory c. leffel', 
		'expected': True, 
		'description': 'emery leffel comparison with article'
	},
    {
		'name_one': 'emil jordan',
		'name_two': 'emil leopold jordan', 
		'expected': True, 
		'description': 'emil jordan comparison with article'
	},
    {
		'name_one': 'emil lengyel',
		'name_two': 'emil lengyel', 
		'expected': True, 
		'description': 'emil lengyel comparison with article'
	},
    {
		'name_one': 'emil r wesa',
		'name_two': 'pierre emile deguise', 
		'expected': False, 
		'description': 'emil r wesa comparison with article'
	},
    {
		'name_one': 'emil w lehmann',
		'name_two': 'emil wilhelm lehmann', 
		'expected': True, 
		'description': 'emil w lehmann comparison with article'
	},
    {
		'name_one': 'emilia larson',
		'name_two': 'henrietta melia larson', 
		'expected': True, 
		'description': 'emilia larson comparison with article'
	},
    {
		'name_one': 'emily k landrum',
		'name_two': 'emily k. landrum', 
		'expected': True, 
		'description': 'emily k landrum comparison with article'
	},
    {
		'name_one': 'emily l. stogdill',
		'name_two': 'emily leatherman stogdill', 
		'expected': True, 
		'description': 'emily l. stogdill comparison with article'
	},
    {
		'name_one': 'emmerich von haam',
		'name_two': 'emmerich von haam', 
		'expected': True, 
		'description': 'emmerich von haam comparison with article'
	},
    {
		'name_one': 'emmett l bennett',
		'name_two': 'emmett leslie bennett', 
		'expected': True, 
		'description': 'emmett l bennett comparison with article'
	},
    {
		'name_one': 'emmy l wolff',
		'name_two': 'emmy land wolff', 
		'expected': True, 
		'description': 'emmy l wolff comparison with article'
	},
    {
		'name_one': 'erastus h lee',
		'name_two': 'erastus h. lee', 
		'expected': True, 
		'description': 'erastus h lee comparison with article'
	},
    {
		'name_one': 'eric b degroat',
		'name_two': 'eric brooks degroat', 
		'expected': True, 
		'description': 'eric b degroat comparison with article'
	},
    {
		'name_one': 'erich l lehmann',
		'name_two': 'erich leo lehmann', 
		'expected': True, 
		'description': 'erich l lehmann comparison with article'
	},
    {
		'name_one': 'ernest a dean',
		'name_two': 'marshall a. dean', 
		'expected': False, 
		'description': 'ernest a dean comparison with article'
	},
    {
		'name_one': 'ernest e leisy',
		'name_two': 'ernest erwin leisy', 
		'expected': True, 
		'description': 'ernest e leisy comparison with article'
	},
    {
		'name_one': 'ernest g gardner',
		'name_two': 'ernest dean gardner', 
		'expected': False, 
		'description': 'ernest g gardner comparison with article'
	},
    {
		'name_one': 'ernest j. monica',
		'name_two': 'j. ernest delmonico', 
		'expected': True, 
		'description': 'ernest j. monica comparison with article'
	},
    {
		'name_one': 'ernest l highbarger',
		'name_two': 'ernest leslie highbarger', 
		'expected': True, 
		'description': 'ernest l highbarger comparison with article'
	},
    {
		'name_one': 'ernest l luther',
		'name_two': 'ernest leonard luther', 
		'expected': True, 
		'description': 'ernest l luther comparison with article'
	},
    {
		'name_one': 'ernest leavitt',
		'name_two': 'ernest e. leavitt', 
		'expected': True, 
		'description': 'ernest leavitt comparison with article'
	},
    {
		'name_one': 'ernest leveque',
		'name_two': 'ernest j. leveque', 
		'expected': True, 
		'description': 'ernest leveque comparison with article'
	},
    {
		'name_one': 'ernest mader',
		'name_two': 'ernest lee mader', 
		'expected': True, 
		'description': 'ernest mader comparison with article'
	},
    {
		'name_one': 'ernest o lawrence',
		'name_two': 'ernest o. lawrence', 
		'expected': True, 
		'description': 'ernest o lawrence comparison with article'
	},
    {
		'name_one': 'ernest p lane',
		'name_two': 'ernest preston lane', 
		'expected': True, 
		'description': 'ernest p lane comparison with article'
	},
    {
		'name_one': 'ernest s larson',
		'name_two': 'ernest s. larson', 
		'expected': True, 
		'description': 'ernest s larson comparison with article'
	},
    {
		'name_one': 'ernest t de wald',
		'name_two': 'ernest theodore dewald', 
		'expected': True, 
		'description': 'ernest t de wald comparison with article'
	},
    {
		'name_one': 'ernestine d guelich',
		'name_two': 'ernestine dewes guelich', 
		'expected': True, 
		'description': 'ernestine d guelich comparison with article'
	},
    {
		'name_one': 'ernst levy',
		'name_two': 'ernst levy', 
		'expected': True, 
		'description': 'ernst levy comparison with article'
	},
    {
		'name_one': 'erskine morse',
		'name_two': 'erskine vance morse', 
		'expected': True, 
		'description': 'erskine morse comparison with article'
	},
    {
		'name_one': 'ervin denisen',
		'name_two': 'ervin loren denisen', 
		'expected': True, 
		'description': 'ervin denisen comparison with article'
	},
    {
		'name_one': 'erving a leonard',
		'name_two': 'irving a. leonard', 
		'expected': True, 
		'description': 'erving a leonard comparison with article'
	},
    {
		'name_one': 'estelle lacy',
		'name_two': 'estelle allen delacy', 
		'expected': True, 
		'description': 'estelle lacy comparison with article'
	},
    {
		'name_one': 'esther d carlson',
		'name_two': 'esther dewitz carlson', 
		'expected': True, 
		'description': 'esther d carlson comparison with article'
	},
    {
		'name_one': 'esther lee',
		'name_two': 'esther lee', 
		'expected': True, 
		'description': 'esther lee comparison with article'
	},
    {
		'name_one': 'esther leigeber',
		'name_two': 'esther marie leihgeber', 
		'expected': True, 
		'description': 'esther leigeber comparison with article'
	},
    {
		'name_one': 'ethel b lamore',
		'name_two': 'ethel b. lamore', 
		'expected': True, 
		'description': 'ethel b lamore comparison with article'
	},
    {
		'name_one': 'eugene delwiche',
		'name_two': 'eugene albert delwiche', 
		'expected': True, 
		'description': 'eugene delwiche comparison with article'
	},
    {
		'name_one': 'eugene f vanepps',
		'name_two': 'eugene francis van epps', 
		'expected': True, 
		'description': 'eugene f vanepps comparison with article'
	},
    {
		'name_one': 'eugene j landry',
		'name_two': 'eugene markley landis', 
		'expected': False, 
		'description': 'eugene j landry comparison with article'
	},
    {
		'name_one': 'eugene l shrader',
		'name_two': 'eugene lee shrader', 
		'expected': True, 
		'description': 'eugene l shrader comparison with article'
	},
    {
		'name_one': 'eugene m lewis',
		'name_two': 'floyd eugene lewis', 
		'expected': False, 
		'description': 'eugene m lewis comparison with article'
	},
    {
		'name_one': 'eugene w lepeschkin',
		'name_two': 'eugene lepeschkin', 
		'expected': True, 
		'description': 'eugene w lepeschkin comparison with article'
	},
    {
		'name_one': 'eugene walsh',
		'name_two': 'eugene lawrence walsh', 
		'expected': True, 
		'description': 'eugene walsh comparison with article'
	},
    {
		'name_one': 'eva l goble',
		'name_two': 'eva lenora goble', 
		'expected': True, 
		'description': 'eva l goble comparison with article'
	},
    {
		'name_one': 'evald b lawson',
		'name_two': 'evald b. lawson', 
		'expected': True, 
		'description': 'evald b lawson comparison with article'
	},
    {
		'name_one': 'evan l lewis',
		'name_two': 'evan l. lewis', 
		'expected': True, 
		'description': 'evan l lewis comparison with article'
	},
    {
		'name_one': 'evans a. laroche',
		'name_two': 'e. a. laroche', 
		'expected': True, 
		'description': 'evans a. laroche comparison with article'
	},
    {
		'name_one': 'evelyn h lewis',
		'name_two': 'evelyn hodges lewis', 
		'expected': True, 
		'description': 'evelyn h lewis comparison with article'
	},
    {
		'name_one': 'evelyn l way',
		'name_two': 'evelyn lee way', 
		'expected': True, 
		'description': 'evelyn l way comparison with article'
	},
    {
		'name_one': 'evelyn r landon',
		'name_two': 'r. d. landon', 
		'expected': False, 
		'description': 'evelyn r landon comparison with article'
	},
    {
		'name_one': 'everett l keener',
		'name_two': 'everett lee keener', 
		'expected': True, 
		'description': 'everett l keener comparison with article'
	},
    {
		'name_one': 'everett lee',
		'name_two': 'everett s. lee', 
		'expected': True, 
		'description': 'everett lee comparison with article'
	},
    {
		'name_one': 'everett lewis',
		'name_two': 'everett vernon lewis', 
		'expected': True, 
		'description': 'everett lewis comparison with article'
	},
    {
		'name_one': 'evert f van maanen',
		'name_two': 'e. f. van maanen', 
		'expected': True, 
		'description': 'evert f van maanen comparison with article'
	},
    {
		'name_one': 'ewell j lytton',
		'name_two': 'j. leon lichtin', 
		'expected': False, 
		'description': 'ewell j lytton comparison with article'
	},
    {
		'name_one': 'ezra l howell',
		'name_two': 'ezra lewis howell', 
		'expected': True, 
		'description': 'ezra l howell comparison with article'
	},
    {
		'name_one': 'f dean mcclusky',
		'name_two': 'f. dean mcclusky', 
		'expected': True, 
		'description': 'f dean mcclusky comparison with article'
	},
    {
		'name_one': 'f devere smith',
		'name_two': 'fenelon devere smith', 
		'expected': True, 
		'description': 'f devere smith comparison with article'
	},
    {
		'name_one': 'f lee benns',
		'name_two': 'f. lee benns', 
		'expected': True, 
		'description': 'f lee benns comparison with article'
	},
    {
		'name_one': 'faith l. gorrell',
		'name_two': 'faith lanman gorrell', 
		'expected': True, 
		'description': 'faith l. gorrell comparison with article'
	},
    {
		'name_one': 'fanny a lahti',
		'name_two': 'aarre kotivalo lahti', 
		'expected': False, 
		'description': 'fanny a lahti comparison with article'
	},
    {
		'name_one': 'faust c dewalsh',
		'name_two': 'faust charles dewalsh', 
		'expected': True, 
		'description': 'faust c dewalsh comparison with article'
	},
    {
		'name_one': 'ferdinand lessing',
		'name_two': 'ferdinand d. lessing', 
		'expected': True, 
		'description': 'ferdinand lessing comparison with article'
	},
    {
		'name_one': 'fitzhugh l carmichael',
		'name_two': 'fitzhugh lee carmichael', 
		'expected': True, 
		'description': 'fitzhugh l carmichael comparison with article'
	},
    {
		'name_one': 'fitzhugh l mcree, jr',
		'name_two': 'fitzhugh lee mcree', 
		'expected': True, 
		'description': 'fitzhugh l mcree, jr comparison with article'
	},
    {
		'name_one': 'flaria h frain',
		'name_two': 'h. larue frain', 
		'expected': False, 
		'description': 'flaria h frain comparison with article'
	},
    {
		'name_one': 'florence alden',
		'name_two': 'florence delia alden', 
		'expected': True, 
		'description': 'florence alden comparison with article'
	},
    {
		'name_one': 'florence b leaver',
		'name_two': 'florence b. leaver', 
		'expected': True, 
		'description': 'florence b leaver comparison with article'
	},
    {
		'name_one': 'florence p lewis',
		'name_two': 'florence parthenia lewis', 
		'expected': True, 
		'description': 'florence p lewis comparison with article'
	},
    {
		'name_one': 'flornece leiser',
		'name_two': 'florine j. leiser', 
		'expected': True, 
		'description': 'flornece leiser comparison with article'
	},
    {
		'name_one': 'floy de lancey',
		'name_two': 'floy w. delancey', 
		'expected': True, 
		'description': 'floy de lancey comparison with article'
	},
    {
		'name_one': 'floyd j. leblanc',
		'name_two': 'floyd j. leblanc', 
		'expected': True, 
		'description': 'floyd j. leblanc comparison with article'
	},
    {
		'name_one': 'floyd l mcelroy',
		'name_two': 'floyd lester mcelroy', 
		'expected': True, 
		'description': 'floyd l mcelroy comparison with article'
	},
    {
		'name_one': 'floyd lamb james',
		'name_two': 'floyd lamb james', 
		'expected': True, 
		'description': 'floyd lamb james comparison with article'
	},
    {
		'name_one': 'floyd lear',
		'name_two': 'floyd s. lear', 
		'expected': True, 
		'description': 'floyd lear comparison with article'
	},
    {
		'name_one': 'floyd s de lashmutt',
		'name_two': 'floyd delashmutt', 
		'expected': True, 
		'description': 'floyd s de lashmutt comparison with article'
	},
    {
		'name_one': 'ford louis battles',
		'name_two': 'ford lewis battles', 
		'expected': True, 
		'description': 'ford louis battles comparison with article'
	},
    {
		'name_one': 'forest l shoemaker',
		'name_two': 'forest leroy shoemaker', 
		'expected': True, 
		'description': 'forest l shoemaker comparison with article'
	},
    {
		'name_one': 'forrest n lake',
		'name_two': 'forrest unna lake', 
		'expected': False, 
		'description': 'forrest n lake comparison with article'
	},
    {
		'name_one': 'forrest w lancaster',
		'name_two': 'forrest wesley lancaster', 
		'expected': True, 
		'description': 'forrest w lancaster comparison with article'
	},
    {
		'name_one': 'france g fell',
		'name_two': 'germaine lafeuille', 
		'expected': False, 
		'description': 'france g fell comparison with article'
	},
    {
		'name_one': 'frances d scott',
		'name_two': 'frances dean scott', 
		'expected': True, 
		'description': 'frances d scott comparison with article'
	},
    {
		'name_one': 'frances e craft',
		'name_two': 'frances de graaff', 
		'expected': False, 
		'description': 'frances e craft comparison with article'
	},
    {
		'name_one': 'frances j dieg',
		'name_two': 'francis j. deig', 
		'expected': False, 
		'description': 'frances j dieg comparison with article'
	},
    {
		'name_one': 'frances l cox',
		'name_two': 'cyrus lafayette cox', 
		'expected': False, 
		'description': 'frances l cox comparison with article'
	},
    {
		'name_one': 'frances l tyler',
		'name_two': 'frances landrum tyler', 
		'expected': True, 
		'description': 'frances l tyler comparison with article'
	},
    {
		'name_one': 'frances m graef',
		'name_two': 'frances de graaff', 
		'expected': True, 
		'description': 'frances m graef comparison with article'
	},
    {
		'name_one': 'frances v holton',
		'name_two': 'frances virginia lee holton', 
		'expected': True, 
		'description': 'frances v holton comparison with article'
	},
    {
		'name_one': 'frances van duyne',
		'name_two': 'frances o. van duyne', 
		'expected': True, 
		'description': 'frances van duyne comparison with article'
	},
    {
		'name_one': 'frances vanvoorhis',
		'name_two': 'frances van voorhis', 
		'expected': True, 
		'description': 'frances vanvoorhis comparison with article'
	},
    {
		'name_one': 'francis a laine',
		'name_two': 'francis anthony laine', 
		'expected': True, 
		'description': 'francis a laine comparison with article'
	},
    {
		'name_one': 'francis c lanning',
		'name_two': 'francis chowing lanning', 
		'expected': True, 
		'description': 'francis c lanning comparison with article'
	},
    {
		'name_one': 'francis c lathrop',
		'name_two': 'francis child lathrop', 
		'expected': True, 
		'description': 'francis c lathrop comparison with article'
	},
    {
		'name_one': 'francis d lazanby',
		'name_two': 'francis d. lazenby', 
		'expected': True, 
		'description': 'francis d lazanby comparison with article'
	},
    {
		'name_one': 'francis deleo',
		'name_two': 'francis x. dileo', 
		'expected': True, 
		'description': 'francis deleo comparison with article'
	},
    {
		'name_one': 'francis e lejeune, jr',
		'name_two': 'francis ernest le jeune', 
		'expected': True, 
		'description': 'francis e lejeune, jr comparison with article'
	},
    {
		'name_one': 'francis g lee',
		'name_two': 'francis g. lee', 
		'expected': True, 
		'description': 'francis g lee comparison with article'
	},
    {
		'name_one': 'francis h friedman',
		'name_two': 'francis lee friedman', 
		'expected': False, 
		'description': 'francis h friedman comparison with article'
	},
    {
		'name_one': 'francis l castleman',
		'name_two': 'francis lee castleman', 
		'expected': True, 
		'description': 'francis l castleman comparison with article'
	},
    {
		'name_one': 'francis l harmon',
		'name_two': 'francis lelande harmon', 
		'expected': True, 
		'description': 'francis l harmon comparison with article'
	},
    {
		'name_one': 'francis l k hsu',
		'name_two': 'francis lang-kwang hsu', 
		'expected': True, 
		'description': 'francis l k hsu comparison with article'
	},
    {
		'name_one': 'francis l lederer',
		'name_two': 'francis loeffler lederer', 
		'expected': True, 
		'description': 'francis l lederer comparison with article'
	},
    {
		'name_one': 'francis l. childs',
		'name_two': 'francis lane childs', 
		'expected': True, 
		'description': 'francis l. childs comparison with article'
	},
    {
		'name_one': 'francis l. utley',
		'name_two': 'francis lee utley', 
		'expected': True, 
		'description': 'francis l. utley comparison with article'
	},
    {
		'name_one': 'francis lee',
		'name_two': 'leon francis lee', 
		'expected': True, 
		'description': 'francis lee comparison with article'
	},
    {
		'name_one': 'francis m la fleur',
		'name_two': 'francis m. la fleur', 
		'expected': True, 
		'description': 'francis m la fleur comparison with article'
	},
    {
		'name_one': 'francis m lamb',
		'name_two': 'francis lamb', 
		'expected': True, 
		'description': 'francis m lamb comparison with article'
	},
    {
		'name_one': 'francis r delfeld',
		'name_two': 'francis delfeld', 
		'expected': True, 
		'description': 'francis r delfeld comparison with article'
	},
    {
		'name_one': 'francis weille',
		'name_two': 'francis lee weille', 
		'expected': True, 
		'description': 'francis weille comparison with article'
	},
    {
		'name_one': 'francis x lake',
		'name_two': 'francis x. lake', 
		'expected': True, 
		'description': 'francis x lake comparison with article'
	},
    {
		'name_one': 'francisco dela sala',
		'name_two': 'francesco della-sala', 
		'expected': True, 
		'description': 'francisco dela sala comparison with article'
	},
    {
		'name_one': 'frank a de costa,jr',
		'name_two': 'frank a. decosta', 
		'expected': True, 
		'description': 'frank a de costa,jr comparison with article'
	},
    {
		'name_one': 'frank a demars',
		'name_two': 'frank addison demars', 
		'expected': True, 
		'description': 'frank a demars comparison with article'
	},
    {
		'name_one': 'frank a evger',
		'name_two': 'frank e. vandiver', 
		'expected': False, 
		'description': 'frank a evger comparison with article'
	},
    {
		'name_one': 'frank a laurie',
		'name_two': 'frank a. laurie', 
		'expected': True, 
		'description': 'frank a laurie comparison with article'
	},
    {
		'name_one': 'frank b mcclelland',
		'name_two': 'frank deloss mcclelland', 
		'expected': False, 
		'description': 'frank b mcclelland comparison with article'
	},
    {
		'name_one': 'frank c larson',
		'name_two': 'frank clark larson', 
		'expected': True, 
		'description': 'frank c larson comparison with article'
	},
    {
		'name_one': 'frank d watson',
		'name_two': 'frank dekker watson', 
		'expected': True, 
		'description': 'frank d watson comparison with article'
	},
    {
		'name_one': 'frank delano, jr',
		'name_two': 'frank lanni', 
		'expected': True, 
		'description': 'frank delano, jr comparison with article'
	},
    {
		'name_one': 'frank e legg',
		'name_two': 'frank evariste legg', 
		'expected': True, 
		'description': 'frank e legg comparison with article'
	},
    {
		'name_one': 'frank e lentz',
		'name_two': 'frank edwin lentz', 
		'expected': True, 
		'description': 'frank e lentz comparison with article'
	},
    {
		'name_one': 'frank g lankard',
		'name_two': 'frank g. lankard', 
		'expected': True, 
		'description': 'frank g lankard comparison with article'
	},
    {
		'name_one': 'frank h lee',
		'name_two': 'frank h. lee', 
		'expected': True, 
		'description': 'frank h lee comparison with article'
	},
    {
		'name_one': 'frank j roberts',
		'name_two': 'frank lester roberts', 
		'expected': False, 
		'description': 'frank j roberts comparison with article'
	},
    {
		'name_one': 'frank l day',
		'name_two': 'frank leighton day', 
		'expected': True, 
		'description': 'frank l day comparison with article'
	},
    {
		'name_one': 'frank l guest',
		'name_two': 'dominic l. degiusti', 
		'expected': False, 
		'description': 'frank l guest comparison with article'
	},
    {
		'name_one': 'frank l howard',
		'name_two': 'frank leslie howard', 
		'expected': True, 
		'description': 'frank l howard comparison with article'
	},
    {
		'name_one': 'frank l jennings',
		'name_two': 'frank lamont jennings', 
		'expected': True, 
		'description': 'frank l jennings comparison with article'
	},
    {
		'name_one': 'frank l meleney',
		'name_two': 'frank lamont meleney', 
		'expected': True, 
		'description': 'frank l meleney comparison with article'
	},
    {
		'name_one': 'frank l myers',
		'name_two': 'frank lewis myers', 
		'expected': True, 
		'description': 'frank l myers comparison with article'
	},
    {
		'name_one': 'frank l weston',
		'name_two': 'frank laurance weston', 
		'expected': True, 
		'description': 'frank l weston comparison with article'
	},
    {
		'name_one': 'frank laguori',
		'name_two': 'frank e. liguori', 
		'expected': True, 
		'description': 'frank laguori comparison with article'
	},
    {
		'name_one': 'frank m de giacomo',
		'name_two': 'frank degiacomo', 
		'expected': True, 
		'description': 'frank m de giacomo comparison with article'
	},
    {
		'name_one': 'frank m lescher',
		'name_two': 'frank mills lescher', 
		'expected': True, 
		'description': 'frank m lescher comparison with article'
	},
    {
		'name_one': 'frank n van buren',
		'name_two': 'frank newman van buren', 
		'expected': True, 
		'description': 'frank n van buren comparison with article'
	},
    {
		'name_one': 'frank r lacy',
		'name_two': 'frank r. lacy', 
		'expected': True, 
		'description': 'frank r lacy comparison with article'
	},
    {
		'name_one': 'frank s schwartz',
		'name_two': 'frank leroy schwartz', 
		'expected': False, 
		'description': 'frank s schwartz comparison with article'
	},
    {
		'name_one': 'frank t hitchcock',
		'name_two': 'frank lauren hitchcock', 
		'expected': False, 
		'description': 'frank t hitchcock comparison with article'
	},
    {
		'name_one': 'frank t lane',
		'name_two': 'frank lane', 
		'expected': True, 
		'description': 'frank t lane comparison with article'
	},
    {
		'name_one': 'frank w dewolf',
		'name_two': 'frank w. dewolf', 
		'expected': True, 
		'description': 'frank w dewolf comparison with article'
	},
    {
		'name_one': 'frank w lewis',
		'name_two': 'frank mendell lewis', 
		'expected': False, 
		'description': 'frank w lewis comparison with article'
	},
    {
		'name_one': 'frank walter clark',
		'name_two': 'walter van tilburg clark', 
		'expected': False, 
		'description': 'frank walter clark comparison with article'
	},
    {
		'name_one': 'frank x keller',
		'name_two': 'frank leuer keller', 
		'expected': False, 
		'description': 'frank x keller comparison with article'
	},
    {
		'name_one': 'franklin c latcham',
		'name_two': 'franklin chester latcham', 
		'expected': True, 
		'description': 'franklin c latcham comparison with article'
	},
    {
		'name_one': 'franklin l baumer',
		'name_two': 'franklin levan baumer', 
		'expected': True, 
		'description': 'franklin l baumer comparison with article'
	},
    {
		'name_one': 'franklyn vanhouten',
		'name_two': 'franklyn bosworth van houten', 
		'expected': True, 
		'description': 'franklyn vanhouten comparison with article'
	},
    {
		'name_one': 'franz landsderbel',
		'name_two': 'franz landsbsrger', 
		'expected': False, 
		'description': 'franz landsderbel comparison with article'
	},
    {
		'name_one': 'fred b deknatel',
		'name_two': 'frederick brockway deknatel', 
		'expected': True, 
		'description': 'fred b deknatel comparison with article'
	},
    {
		'name_one': 'fred d cochran',
		'name_two': 'fred derward cochran', 
		'expected': True, 
		'description': 'fred d cochran comparison with article'
	},
    {
		'name_one': 'fred e. deatherage',
		'name_two': 'fred e. deatherage', 
		'expected': True, 
		'description': 'fred e. deatherage comparison with article'
	},
    {
		'name_one': 'fred fontes',
		'name_two': 'fred e. lafon', 
		'expected': False, 
		'description': 'fred fontes comparison with article'
	},
    {
		'name_one': 'fred j lewis',
		'name_two': 'fred j. lewis', 
		'expected': True, 
		'description': 'fred j lewis comparison with article'
	},
    {
		'name_one': 'fred l humphrey',
		'name_two': 'fred lasalle humphrey', 
		'expected': True, 
		'description': 'fred l humphrey comparison with article'
	},
    {
		'name_one': 'fred l kerr',
		'name_two': 'frederick laird kerr', 
		'expected': True, 
		'description': 'fred l kerr comparison with article'
	},
    {
		'name_one': 'fred l stetson',
		'name_two': 'fred lea stetson', 
		'expected': True, 
		'description': 'fred l stetson comparison with article'
	},
    {
		'name_one': 'fred l walkey',
		'name_two': 'fred leslie walkey', 
		'expected': True, 
		'description': 'fred l walkey comparison with article'
	},
    {
		'name_one': 'fred m moreau',
		'name_two': 'fred l. lamoreau', 
		'expected': False, 
		'description': 'fred m moreau comparison with article'
	},
    {
		'name_one': 'fred m moreau',
		'name_two': 'fred lamoreau', 
		'expected': True, 
		'description': 'fred m moreau comparison with article'
	},
    {
		'name_one': 'frederic h leavitt',
		'name_two': 'frederic headley leavitt', 
		'expected': True, 
		'description': 'frederic h leavitt comparison with article'
	},
    {
		'name_one': 'frederich deibler',
		'name_two': 'frederick shipp deibler', 
		'expected': True, 
		'description': 'frederich deibler comparison with article'
	},
    {
		'name_one': 'frederick c lane',
		'name_two': 'frederic chapin lane', 
		'expected': True, 
		'description': 'frederick c lane comparison with article'
	},
    {
		'name_one': 'frederick c leonard',
		'name_two': 'frederick c. leonard', 
		'expected': True, 
		'description': 'frederick c leonard comparison with article'
	},
    {
		'name_one': 'frederick c. landsittel',
		'name_two': 'frederick c. landsittel', 
		'expected': True, 
		'description': 'frederick c. landsittel comparison with article'
	},
    {
		'name_one': 'frederick d geist',
		'name_two': 'frederick denkmar geist', 
		'expected': True, 
		'description': 'frederick d geist comparison with article'
	},
    {
		'name_one': 'frederick d heald',
		'name_two': 'frederick deforest heald', 
		'expected': True, 
		'description': 'frederick d heald comparison with article'
	},
    {
		'name_one': 'frederick d miller',
		'name_two': 'frederick dewolfe miller', 
		'expected': True, 
		'description': 'frederick d miller comparison with article'
	},
    {
		'name_one': 'frederick d tootell',
		'name_two': 'frederic delmont tootell', 
		'expected': True, 
		'description': 'frederick d tootell comparison with article'
	},
    {
		'name_one': 'frederick deuschle',
		'name_two': 'frederick m. deuschle', 
		'expected': True, 
		'description': 'frederick deuschle comparison with article'
	},
    {
		'name_one': 'frederick l hovde',
		'name_two': 'frederick lawson hovde', 
		'expected': True, 
		'description': 'frederick l hovde comparison with article'
	},
    {
		'name_one': 'frederick l test',
		'name_two': 'frederick laurent test', 
		'expected': True, 
		'description': 'frederick l test comparison with article'
	},
    {
		'name_one': 'frederick lehner',
		'name_two': 'frederick lehner', 
		'expected': True, 
		'description': 'frederick lehner comparison with article'
	},
    {
		'name_one': 'frederick lewis',
		'name_two': 'frederick d. lewis', 
		'expected': True, 
		'description': 'frederick lewis comparison with article'
	},
    {
		'name_one': 'frederick w edwards',
		'name_two': 'frederick lee edwards', 
		'expected': False, 
		'description': 'frederick w edwards comparison with article'
	},
    {
		'name_one': 'frederick w lenz',
		'name_two': 'frederick walter lenz', 
		'expected': True, 
		'description': 'frederick w lenz comparison with article'
	},
    {
		'name_one': 'frederick w vanname',
		'name_two': 'frederick w. van name', 
		'expected': True, 
		'description': 'frederick w vanname comparison with article'
	},
    {
		'name_one': 'fredrica shattuck',
		'name_two': 'fredrica van trice shattuck', 
		'expected': True, 
		'description': 'fredrica shattuck comparison with article'
	},
    {
		'name_one': 'fredrick l rodkey',
		'name_two': 'frederick lee rodkey', 
		'expected': True, 
		'description': 'fredrick l rodkey comparison with article'
	},
    {
		'name_one': 'fredrick lacy',
		'name_two': 'frederic j. lacy', 
		'expected': True, 
		'description': 'fredrick lacy comparison with article'
	},
    {
		'name_one': 'fredrick w vanbuskirk',
		'name_two': 'frederick william van buskirk', 
		'expected': True, 
		'description': 'fredrick w vanbuskirk comparison with article'
	},
    {
		'name_one': 'friderico deonis',
		'name_two': 'federico de onis', 
		'expected': True, 
		'description': 'friderico deonis comparison with article'
	},
    {
		'name_one': 'fritz h laves',
		'name_two': 'fritz laves', 
		'expected': True, 
		'description': 'fritz h laves comparison with article'
	},
    {
		'name_one': 'fritz l hoffmann',
		'name_two': 'fritz leo hoffmann', 
		'expected': True, 
		'description': 'fritz l hoffmann comparison with article'
	},
    {
		'name_one': 'fritz v lenel',
		'name_two': 'fritz v. lenel', 
		'expected': True, 
		'description': 'fritz v lenel comparison with article'
	},
    {
		'name_one': 'g alvin le page',
		'name_two': 'gerald alvin lepage', 
		'expected': True, 
		'description': 'g alvin le page comparison with article'
	},
    {
		'name_one': 'g geoffrey langsam',
		'name_two': 'gert geoffrey langsam', 
		'expected': True, 
		'description': 'g geoffrey langsam comparison with article'
	},
    {
		'name_one': 'g leslie miller',
		'name_two': 'g. leslie miller', 
		'expected': True, 
		'description': 'g leslie miller comparison with article'
	},
    {
		'name_one': 'g v lantzeff',
		'name_two': 'george v. lantzeff', 
		'expected': True, 
		'description': 'g v lantzeff comparison with article'
	},
    {
		'name_one': 'g. joseph delor',
		'name_two': 'c. joseph delor', 
		'expected': False, 
		'description': 'g. joseph delor comparison with article'
	},
    {
		'name_one': 'gabriel lasker',
		'name_two': 'gabriel w. lasker', 
		'expected': True, 
		'description': 'gabriel lasker comparison with article'
	},
    {
		'name_one': 'gail e densmore',
		'name_two': 'gail ernest densmore', 
		'expected': True, 
		'description': 'gail e densmore comparison with article'
	},
    {
		'name_one': 'gardner leslie warner',
		'name_two': 'c. gardner warner', 
		'expected': False, 
		'description': 'gardner leslie warner comparison with article'
	},
    {
		'name_one': 'garnette l fittro',
		'name_two': 'garnette leona fittro', 
		'expected': True, 
		'description': 'garnette l fittro comparison with article'
	},
    {
		'name_one': 'garth l lee',
		'name_two': 'garth l. lee', 
		'expected': True, 
		'description': 'garth l lee comparison with article'
	},
    {
		'name_one': 'garvin l. von eschen',
		'name_two': 'garvin l. von eschen', 
		'expected': True, 
		'description': 'garvin l. von eschen comparison with article'
	},
    {
		'name_one': 'gendolynde m demchuk',
		'name_two': 'esther m. dimchevsky', 
		'expected': False, 
		'description': 'gendolynde m demchuk comparison with article'
	},
    {
		'name_one': 'gene l hemmle',
		'name_two': 'gene leclair hemmle', 
		'expected': True, 
		'description': 'gene l hemmle comparison with article'
	},
    {
		'name_one': 'genieve a w lamson',
		'name_two': 'genieve lamson', 
		'expected': True, 
		'description': 'genieve a w lamson comparison with article'
	},
    {
		'name_one': 'george a adsit',
		'name_two': 'george depue hadzsits', 
		'expected': False, 
		'description': 'george a adsit comparison with article'
	},
    {
		'name_one': 'george a dean',
		'name_two': 'george a. dean', 
		'expected': True, 
		'description': 'george a dean comparison with article'
	},
    {
		'name_one': 'george a laisner',
		'name_two': 'george a. laisner', 
		'expected': True, 
		'description': 'george a laisner comparison with article'
	},
    {
		'name_one': 'george b denton',
		'name_two': 'george bion denton', 
		'expected': True, 
		'description': 'george b denton comparison with article'
	},
    {
		'name_one': 'george b lacey, jr',
		'name_two': 'jorgen laessoe', 
		'expected': False, 
		'description': 'george b lacey, jr comparison with article'
	},
    {
		'name_one': 'george b van schaack',
		'name_two': 'george b. van schaack', 
		'expected': True, 
		'description': 'george b van schaack comparison with article'
	},
    {
		'name_one': 'george deaver',
		'name_two': 'george g. deaver', 
		'expected': True, 
		'description': 'george deaver comparison with article'
	},
    {
		'name_one': 'george deckey',
		'name_two': 'george deckey', 
		'expected': True, 
		'description': 'george deckey comparison with article'
	},
    {
		'name_one': 'george e beick',
		'name_two': 'george e. vander beke', 
		'expected': True, 
		'description': 'george e beick comparison with article'
	},
    {
		'name_one': 'george e lamaitre',
		'name_two': 'georges eduoard lemaitre', 
		'expected': True, 
		'description': 'george e lamaitre comparison with article'
	},
    {
		'name_one': 'george e leedham',
		'name_two': 'george edwin leedham', 
		'expected': True, 
		'description': 'george e leedham comparison with article'
	},
    {
		'name_one': 'george e. large',
		'name_two': 'george e. large', 
		'expected': True, 
		'description': 'george e. large comparison with article'
	},
    {
		'name_one': 'george f deasy',
		'name_two': 'george f. deasy', 
		'expected': True, 
		'description': 'george f deasy comparison with article'
	},
    {
		'name_one': 'george f depuy',
		'name_two': 'george f. depuy', 
		'expected': True, 
		'description': 'george f depuy comparison with article'
	},
    {
		'name_one': 'george f smith',
		'name_two': 'george van siclen smith', 
		'expected': False, 
		'description': 'george f smith comparison with article'
	},
    {
		'name_one': 'george f taylor',
		'name_two': 'george vanderbeck taylor', 
		'expected': False, 
		'description': 'george f taylor comparison with article'
	},
    {
		'name_one': 'george f. lawlor',
		'name_two': 'george f. lawlor', 
		'expected': True, 
		'description': 'george f. lawlor comparison with article'
	},
    {
		'name_one': 'george g lamb',
		'name_two': 'george goodrich lamb', 
		'expected': True, 
		'description': 'george g lamb comparison with article'
	},
    {
		'name_one': 'george h dell',
		'name_two': 'geo h. dell', 
		'expected': True, 
		'description': 'george h dell comparison with article'
	},
    {
		'name_one': 'george h dession',
		'name_two': 'george hathaway dession', 
		'expected': True, 
		'description': 'george h dession comparison with article'
	},
    {
		'name_one': 'george h larson',
		'name_two': 'george herbert larson', 
		'expected': True, 
		'description': 'george h larson comparison with article'
	},
    {
		'name_one': 'george j la lande',
		'name_two': 'george albert lanyi', 
		'expected': False, 
		'description': 'george j la lande comparison with article'
	},
    {
		'name_one': 'george l abernethy',
		'name_two': 'george lawrence abernethy', 
		'expected': True, 
		'description': 'george l abernethy comparison with article'
	},
    {
		'name_one': 'george l barnett',
		'name_two': 'george leonard barnett', 
		'expected': True, 
		'description': 'george l barnett comparison with article'
	},
    {
		'name_one': 'george l clarke',
		'name_two': 'george leonard clarke', 
		'expected': True, 
		'description': 'george l clarke comparison with article'
	},
    {
		'name_one': 'george l horner',
		'name_two': 'george lewis horner', 
		'expected': True, 
		'description': 'george l horner comparison with article'
	},
    {
		'name_one': 'george l leffler',
		'name_two': 'george l. leffler', 
		'expected': True, 
		'description': 'george l leffler comparison with article'
	},
    {
		'name_one': 'george l matuschka',
		'name_two': 'george leslie matuschka', 
		'expected': True, 
		'description': 'george l matuschka comparison with article'
	},
    {
		'name_one': 'george l shuster',
		'name_two': 'george lee schuster', 
		'expected': True, 
		'description': 'george l shuster comparison with article'
	},
    {
		'name_one': 'george l sullivan',
		'name_two': 'george leonard sullivan', 
		'expected': True, 
		'description': 'george l sullivan comparison with article'
	},
    {
		'name_one': 'george lefevre, jr',
		'name_two': 'george lefevre', 
		'expected': True, 
		'description': 'george lefevre, jr comparison with article'
	},
    {
		'name_one': 'george lehner',
		'name_two': 'george f. j. lehner', 
		'expected': True, 
		'description': 'george lehner comparison with article'
	},
    {
		'name_one': 'george lensen',
		'name_two': 'george alexander lensen', 
		'expected': True, 
		'description': 'george lensen comparison with article'
	},
    {
		'name_one': 'george leuca',
		'name_two': 'george leuca', 
		'expected': True, 
		'description': 'george leuca comparison with article'
	},
    {
		'name_one': 'george m landrock',
		'name_two': 'george m. landrock', 
		'expected': True, 
		'description': 'george m landrock comparison with article'
	},
    {
		'name_one': 'george n lauer',
		'name_two': 'george n. lauer', 
		'expected': True, 
		'description': 'george n lauer comparison with article'
	},
    {
		'name_one': 'george p deyoe',
		'name_two': 'george p. deyoe', 
		'expected': True, 
		'description': 'george p deyoe comparison with article'
	},
    {
		'name_one': 'george r lacy',
		'name_two': 'george rufus lacy', 
		'expected': True, 
		'description': 'george r lacy comparison with article'
	},
    {
		'name_one': 'george r santillo',
		'name_two': 'giorgio diaz de santillana', 
		'expected': False, 
		'description': 'george r santillo comparison with article'
	},
    {
		'name_one': 'george s lane',
		'name_two': 'george sherman lane', 
		'expected': True, 
		'description': 'george s lane comparison with article'
	},
    {
		'name_one': 'george s lasher',
		'name_two': 'george starr lasher', 
		'expected': True, 
		'description': 'george s lasher comparison with article'
	},
    {
		'name_one': 'george s lewis',
		'name_two': 'george s. lewis', 
		'expected': True, 
		'description': 'george s lewis comparison with article'
	},
    {
		'name_one': 'george t lewis',
		'name_two': 'george t. lewis', 
		'expected': True, 
		'description': 'george t lewis comparison with article'
	},
    {
		'name_one': 'george t pynne',
		'name_two': 'george la piana', 
		'expected': False, 
		'description': 'george t pynne comparison with article'
	},
    {
		'name_one': 'george t vane',
		'name_two': 'george thomas vane', 
		'expected': True, 
		'description': 'george t vane comparison with article'
	},
    {
		'name_one': 'george v leroy',
		'name_two': 'george v. leroy', 
		'expected': True, 
		'description': 'george v leroy comparison with article'
	},
    {
		'name_one': 'george vander noot',
		'name_two': 'george w. vander noot', 
		'expected': True, 
		'description': 'george vander noot comparison with article'
	},
    {
		'name_one': 'george vandyke',
		'name_two': 'george d. van dyke', 
		'expected': True, 
		'description': 'george vandyke comparison with article'
	},
    {
		'name_one': 'george vanhorn',
		'name_two': 'george a. van horn', 
		'expected': True, 
		'description': 'george vanhorn comparison with article'
	},
    {
		'name_one': 'george vlahabis',
		'name_two': 'willis george labes', 
		'expected': False, 
		'description': 'george vlahabis comparison with article'
	},
    {
		'name_one': 'george w ladd',
		'name_two': 'george e. ladd', 
		'expected': False, 
		'description': 'george w ladd comparison with article'
	},
    {
		'name_one': 'george w le maire',
		'name_two': 'george w. lemaire', 
		'expected': True, 
		'description': 'george w le maire comparison with article'
	},
    {
		'name_one': 'george w lees',
		'name_two': 'george winchester lees', 
		'expected': True, 
		'description': 'george w lees comparison with article'
	},
    {
		'name_one': 'george w vien',
		'name_two': 'george levene', 
		'expected': True, 
		'description': 'george w vien comparison with article'
	},
    {
		'name_one': 'georgia b leach',
		'name_two': 'georgia belle leach', 
		'expected': True, 
		'description': 'georgia b leach comparison with article'
	},
    {
		'name_one': 'georgia bell',
		'name_two': 'georgia laxson bell', 
		'expected': True, 
		'description': 'georgia bell comparison with article'
	},
    {
		'name_one': 'georgia k del franco',
		'name_two': 'georgia del franco', 
		'expected': True, 
		'description': 'georgia k del franco comparison with article'
	},
    {
		'name_one': 'georgia l shaffer',
		'name_two': 'george lewis shaffer', 
		'expected': True, 
		'description': 'georgia l shaffer comparison with article'
	},
    {
		'name_one': 'gerald a leonards',
		'name_two': 'gerald allen leonards', 
		'expected': True, 
		'description': 'gerald a leonards comparison with article'
	},
    {
		'name_one': 'gerald d meyer',
		'name_two': 'gerald dennis meyer', 
		'expected': True, 
		'description': 'gerald d meyer comparison with article'
	},
    {
		'name_one': 'gerald desmond',
		'name_two': 'gerald desmond', 
		'expected': True, 
		'description': 'gerald desmond comparison with article'
	},
    {
		'name_one': 'gerald langford',
		'name_two': 'gerald langford', 
		'expected': True, 
		'description': 'gerald langford comparison with article'
	},
    {
		'name_one': 'gerald w lawlor',
		'name_two': 'gerald w. lawlor', 
		'expected': True, 
		'description': 'gerald w lawlor comparison with article'
	},
    {
		'name_one': 'gerhard e von glahn',
		'name_two': 'gerhard e. von glahn', 
		'expected': True, 
		'description': 'gerhard e von glahn comparison with article'
	},
    {
		'name_one': 'gerrit de jong,jr',
		'name_two': 'gerrit de jong', 
		'expected': True, 
		'description': 'gerrit de jong,jr comparison with article'
	},
    {
		'name_one': 'gertrude a ncdounough',
		'name_two': 'agnes crawford leaycraft donohugh', 
		'expected': False, 
		'description': 'gertrude a ncdounough comparison with article'
	},
    {
		'name_one': 'gertrude e leich',
		'name_two': 'gertrude leich', 
		'expected': True, 
		'description': 'gertrude e leich comparison with article'
	},
    {
		'name_one': 'gertrude e way',
		'name_two': 'e. leong way', 
		'expected': False, 
		'description': 'gertrude e way comparison with article'
	},
    {
		'name_one': 'gertrude leighton',
		'name_two': 'gertrude c. k. leighton', 
		'expected': True, 
		'description': 'gertrude leighton comparison with article'
	},
    {
		'name_one': 'gertrude m levy',
		'name_two': 'nissim m. levy', 
		'expected': False, 
		'description': 'gertrude m levy comparison with article'
	},
    {
		'name_one': 'gertrude van zandt',
		'name_two': 'gertrude van zandt', 
		'expected': True, 
		'description': 'gertrude van zandt comparison with article'
	},
    {
		'name_one': 'geza de takats',
		'name_two': 'geza de takats', 
		'expected': True, 
		'description': 'geza de takats comparison with article'
	},
    {
		'name_one': 'gilbert levine',
		'name_two': 'gilbert levine', 
		'expected': True, 
		'description': 'gilbert levine comparison with article'
	},
    {
		'name_one': 'gilbert w lambert',
		'name_two': 'gilbert w. lambert', 
		'expected': True, 
		'description': 'gilbert w lambert comparison with article'
	},
    {
		'name_one': 'gilman d. kirk',
		'name_two': 'gilman deering kirk', 
		'expected': True, 
		'description': 'gilman d. kirk comparison with article'
	},
    {
		'name_one': 'gladys e leonard',
		'name_two': 'gladys leonard', 
		'expected': True, 
		'description': 'gladys e leonard comparison with article'
	},
    {
		'name_one': 'gladys m leahy',
		'name_two': 'kathleen m. leahy', 
		'expected': False, 
		'description': 'gladys m leahy comparison with article'
	},
    {
		'name_one': 'gladys vanarsdale',
		'name_two': 'gladys van arsdale', 
		'expected': True, 
		'description': 'gladys vanarsdale comparison with article'
	},
    {
		'name_one': 'glen a lagrange',
		'name_two': 'glen a. lagrange', 
		'expected': True, 
		'description': 'glen a lagrange comparison with article'
	},
    {
		'name_one': 'glend vanwormer',
		'name_two': 'glenn i. van wormer', 
		'expected': True, 
		'description': 'glend vanwormer comparison with article'
	},
    {
		'name_one': 'glenn devine',
		'name_two': 'glenn daniel devine', 
		'expected': True, 
		'description': 'glenn devine comparison with article'
	},
    {
		'name_one': 'glenn j lawlor, sr',
		'name_two': 'glenn j. lawlor', 
		'expected': True, 
		'description': 'glenn j lawlor, sr comparison with article'
	},
    {
		'name_one': 'glenn l alt',
		'name_two': 'glenn leslie alt', 
		'expected': True, 
		'description': 'glenn l alt comparison with article'
	},
    {
		'name_one': 'gloria dela vega',
		'name_two': 'gloria de la vega', 
		'expected': True, 
		'description': 'gloria dela vega comparison with article'
	},
    {
		'name_one': 'gordon f lee',
		'name_two': 'gordon canfield lee', 
		'expected': False, 
		'description': 'gordon f lee comparison with article'
	},
    {
		'name_one': 'gordon r dewart',
		'name_two': 'gordon r. dewart', 
		'expected': True, 
		'description': 'gordon r dewart comparison with article'
	},
    {
		'name_one': 'gottfried delatour',
		'name_two': 'gottfried delatour', 
		'expected': True, 
		'description': 'gottfried delatour comparison with article'
	},
    {
		'name_one': 'grace e lampe',
		'name_two': 'e. w. lampe', 
		'expected': False, 
		'description': 'grace e lampe comparison with article'
	},
    {
		'name_one': 'grace j lawrence',
		'name_two': 'bertram j. lawrence', 
		'expected': False, 
		'description': 'grace j lawrence comparison with article'
	},
    {
		'name_one': 'grace langford',
		'name_two': 'grace langford', 
		'expected': True, 
		'description': 'grace langford comparison with article'
	},
    {
		'name_one': 'grace leathurby',
		'name_two': 'grace c. leathurby', 
		'expected': True, 
		'description': 'grace leathurby comparison with article'
	},
    {
		'name_one': 'grant h laing',
		'name_two': 'grant harrison laing', 
		'expected': True, 
		'description': 'grant h laing comparison with article'
	},
    {
		'name_one': 'gray l hunter',
		'name_two': 'guy leroy hunner', 
		'expected': False, 
		'description': 'gray l hunter comparison with article'
	},
    {
		'name_one': 'graydon s deland, jr',
		'name_two': 'graydon skerritt deland', 
		'expected': True, 
		'description': 'graydon s deland, jr comparison with article'
	},
    {
		'name_one': 'graydon s deland,jr',
		'name_two': 'graydon skerritt deland', 
		'expected': True, 
		'description': 'graydon s deland,jr comparison with article'
	},
    {
		'name_one': 'gregory g la grone',
		'name_two': 'gregory g. lagrone', 
		'expected': True, 
		'description': 'gregory g la grone comparison with article'
	},
    {
		'name_one': 'gregory j derschug',
		'name_two': 'gregory j. derschug', 
		'expected': True, 
		'description': 'gregory j derschug comparison with article'
	},
    {
		'name_one': 'greta a lash',
		'name_two': 'greta alecia lash', 
		'expected': True, 
		'description': 'greta a lash comparison with article'
	},
    {
		'name_one': 'gussie l teague',
		'name_two': 'gussie lee teague', 
		'expected': True, 
		'description': 'gussie l teague comparison with article'
	},
    {
		'name_one': 'gustav a lehman',
		'name_two': 'gustav adolf lehman', 
		'expected': True, 
		'description': 'gustav a lehman comparison with article'
	},
    {
		'name_one': 'gustave e von grunebaum',
		'name_two': 'gustave e. von grunebaum', 
		'expected': True, 
		'description': 'gustave e von grunebaum comparison with article'
	},
    {
		'name_one': 'gustave w larson',
		'name_two': 'philip gustave laurson', 
		'expected': False, 
		'description': 'gustave w larson comparison with article'
	},
    {
		'name_one': 'guy j desimone',
		'name_two': 'guy j. de simone', 
		'expected': True, 
		'description': 'guy j desimone comparison with article'
	},
    {
		'name_one': 'guy j lemieux',
		'name_two': 'guy j. lemieux', 
		'expected': True, 
		'description': 'guy j lemieux comparison with article'
	},
    {
		'name_one': 'guy l bryan',
		'name_two': 'guy lee bryan', 
		'expected': True, 
		'description': 'guy l bryan comparison with article'
	},
    {
		'name_one': 'guy l jones',
		'name_two': 'guy langston jones', 
		'expected': True, 
		'description': 'guy l jones comparison with article'
	},
    {
		'name_one': 'guy l odom',
		'name_two': 'guy leary odom', 
		'expected': True, 
		'description': 'guy l odom comparison with article'
	},
    {
		'name_one': 'gwendolyn tinklin',
		'name_two': 'gwendolyn laverne tinklin', 
		'expected': True, 
		'description': 'gwendolyn tinklin comparison with article'
	},
    {
		'name_one': 'h dean burdick',
		'name_two': 'h. dean burdick', 
		'expected': True, 
		'description': 'h dean burdick comparison with article'
	},
    {
		'name_one': 'h jerry lavender',
		'name_two': 'h. jerry lavender', 
		'expected': True, 
		'description': 'h jerry lavender comparison with article'
	},
    {
		'name_one': 'h leland vaughan',
		'name_two': 'h. leland vaughan', 
		'expected': True, 
		'description': 'h leland vaughan comparison with article'
	},
    {
		'name_one': 'h leroy baumgartner',
		'name_two': 'h. leroy baumgartner', 
		'expected': True, 
		'description': 'h leroy baumgartner comparison with article'
	},
    {
		'name_one': 'h lewis batts',
		'name_two': 'lewis batts', 
		'expected': True, 
		'description': 'h lewis batts comparison with article'
	},
    {
		'name_one': 'h p lankelma',
		'name_two': 'herman p. lankelma', 
		'expected': True, 
		'description': 'h p lankelma comparison with article'
	},
    {
		'name_one': 'h roger baker',
		'name_two': 'roger denio baker', 
		'expected': False, 
		'description': 'h roger baker comparison with article'
	},
    {
		'name_one': 'haley d worthy',
		'name_two': 'haley dewey worthy', 
		'expected': True, 
		'description': 'haley d worthy comparison with article'
	},
    {
		'name_one': 'hampden lawson',
		'name_two': 'hampden c. lawson', 
		'expected': True, 
		'description': 'hampden lawson comparison with article'
	},
    {
		'name_one': 'hanpt g bower',
		'name_two': 'holle g. deboer', 
		'expected': False, 
		'description': 'hanpt g bower comparison with article'
	},
    {
		'name_one': 'hans lewy',
		'name_two': 'hans lewy', 
		'expected': True, 
		'description': 'hans lewy comparison with article'
	},
    {
		'name_one': 'hardin c van duerson',
		'name_two': 'hardin van deursen', 
		'expected': True, 
		'description': 'hardin c van duerson comparison with article'
	},
    {
		'name_one': 'harlen l hagman',
		'name_two': 'harlan lawrence hagman', 
		'expected': True, 
		'description': 'harlen l hagman comparison with article'
	},
    {
		'name_one': 'harold a decker',
		'name_two': 'harold a. decker', 
		'expected': True, 
		'description': 'harold a decker comparison with article'
	},
    {
		'name_one': 'harold c davis',
		'name_two': 'harold leicester davis', 
		'expected': False, 
		'description': 'harold c davis comparison with article'
	},
    {
		'name_one': 'harold c deutsch',
		'name_two': 'harold c. deutsch', 
		'expected': True, 
		'description': 'harold c deutsch comparison with article'
	},
    {
		'name_one': 'harold c van horne',
		'name_two': 'harold cornelius van horne', 
		'expected': True, 
		'description': 'harold c van horne comparison with article'
	},
    {
		'name_one': 'harold de mott hughes',
		'name_two': 'harold demott hughes', 
		'expected': True, 
		'description': 'harold de mott hughes comparison with article'
	},
    {
		'name_one': 'harold f deutsch',
		'name_two': 'harold francis deutsch', 
		'expected': True, 
		'description': 'harold f deutsch comparison with article'
	},
    {
		'name_one': 'harold f laroe',
		'name_two': 'harold f. laroe', 
		'expected': True, 
		'description': 'harold f laroe comparison with article'
	},
    {
		'name_one': 'harold f lenz',
		'name_two': 'harold lenz', 
		'expected': True, 
		'description': 'harold f lenz comparison with article'
	},
    {
		'name_one': 'harold j lang',
		'name_two': 'harold locke lang', 
		'expected': False, 
		'description': 'harold j lang comparison with article'
	},
    {
		'name_one': 'harold j lewis',
		'name_two': 'harold merrills lewis', 
		'expected': False, 
		'description': 'harold j lewis comparison with article'
	},
    {
		'name_one': 'harold l bond',
		'name_two': 'harold lewis bond', 
		'expected': True, 
		'description': 'harold l bond comparison with article'
	},
    {
		'name_one': 'harold l cohen',
		'name_two': 'harold larry cohen', 
		'expected': True, 
		'description': 'harold l cohen comparison with article'
	},
    {
		'name_one': 'harold l haley',
		'name_two': 'harold leroy haley', 
		'expected': True, 
		'description': 'harold l haley comparison with article'
	},
    {
		'name_one': 'harold l harris',
		'name_two': 'harold leo harris', 
		'expected': True, 
		'description': 'harold l harris comparison with article'
	},
    {
		'name_one': 'harold l. yochum',
		'name_two': 'harold leland yochum', 
		'expected': True, 
		'description': 'harold l. yochum comparison with article'
	},
    {
		'name_one': 'harold laufman',
		'name_two': 'harold laufman', 
		'expected': True, 
		'description': 'harold laufman comparison with article'
	},
    {
		'name_one': 'harold lewis',
		'name_two': 'harold gregg lewis', 
		'expected': True, 
		'description': 'harold lewis comparison with article'
	},
    {
		'name_one': 'harold m devolt',
		'name_two': 'harold m. devolt', 
		'expected': True, 
		'description': 'harold m devolt comparison with article'
	},
    {
		'name_one': 'harold n lee',
		'name_two': 'harold newton lee', 
		'expected': True, 
		'description': 'harold n lee comparison with article'
	},
    {
		'name_one': 'harold r kugler',
		'name_two': 'harold leroy kugler', 
		'expected': False, 
		'description': 'harold r kugler comparison with article'
	},
    {
		'name_one': 'harold r laycock',
		'name_two': 'harold r. laycock', 
		'expected': True, 
		'description': 'harold r laycock comparison with article'
	},
    {
		'name_one': 'harold r laycock',
		'name_two': 'ralph g. laycock', 
		'expected': False, 
		'description': 'harold r laycock comparison with article'
	},
    {
		'name_one': 'harold r leith',
		'name_two': 'harold r. leith', 
		'expected': True, 
		'description': 'harold r leith comparison with article'
	},
    {
		'name_one': 'harold w dean',
		'name_two': 'w. t. dean', 
		'expected': False, 
		'description': 'harold w dean comparison with article'
	},
    {
		'name_one': 'harold w lee',
		'name_two': 'harold w. lee', 
		'expected': True, 
		'description': 'harold w lee comparison with article'
	},
    {
		'name_one': 'harold w levin',
		'name_two': 'harold levin', 
		'expected': True, 
		'description': 'harold w levin comparison with article'
	},
    {
		'name_one': 'harold w lewis',
		'name_two': 'harold walter lewis', 
		'expected': True, 
		'description': 'harold w lewis comparison with article'
	},
    {
		'name_one': 'harold wolf',
		'name_two': 'l. harold dewolf', 
		'expected': True, 
		'description': 'harold wolf comparison with article'
	},
    {
		'name_one': 'harriet b denham',
		'name_two': 'wallace brett donham', 
		'expected': False, 
		'description': 'harriet b denham comparison with article'
	},
    {
		'name_one': 'harriet c woodward',
		'name_two': 'c. vann woodward', 
		'expected': False, 
		'description': 'harriet c woodward comparison with article'
	},
    {
		'name_one': 'harriet herring',
		'name_two': 'harriet laura herring', 
		'expected': True, 
		'description': 'harriet herring comparison with article'
	},
    {
		'name_one': 'harriet m lewis',
		'name_two': 'g. m. lewis', 
		'expected': False, 
		'description': 'harriet m lewis comparison with article'
	},
    {
		'name_one': 'harris s langeler',
		'name_two': 'georg harris langeler', 
		'expected': False, 
		'description': 'harris s langeler comparison with article'
	},
    {
		'name_one': 'harris w dean',
		'name_two': 'harris william dean', 
		'expected': True, 
		'description': 'harris w dean comparison with article'
	},
    {
		'name_one': 'harrison d le baron',
		'name_two': 'h. d. lebaron', 
		'expected': True, 
		'description': 'harrison d le baron comparison with article'
	},
    {
		'name_one': 'harrison l chance',
		'name_two': 'harrison levi chance', 
		'expected': True, 
		'description': 'harrison l chance comparison with article'
	},
    {
		'name_one': 'harrison l harley',
		'name_two': 'harrison leroy harley', 
		'expected': True, 
		'description': 'harrison l harley comparison with article'
	},
    {
		'name_one': 'harry b decook',
		'name_two': 'harry b. decook', 
		'expected': True, 
		'description': 'harry b decook comparison with article'
	},
    {
		'name_one': 'harry b van dyke',
		'name_two': 'harry b. van dyke', 
		'expected': True, 
		'description': 'harry b van dyke comparison with article'
	},
    {
		'name_one': 'harry d taft',
		'name_two': 'harry derward taft', 
		'expected': True, 
		'description': 'harry d taft comparison with article'
	},
    {
		'name_one': 'harry d wolf',
		'name_two': 'harry demerle wolf', 
		'expected': True, 
		'description': 'harry d wolf comparison with article'
	},
    {
		'name_one': 'harry e dassau',
		'name_two': 'walter edward dessauer', 
		'expected': False, 
		'description': 'harry e dassau comparison with article'
	},
    {
		'name_one': 'harry e. le fever',
		'name_two': 'harry lefever', 
		'expected': True, 
		'description': 'harry e. le fever comparison with article'
	},
    {
		'name_one': 'harry g laforge',
		'name_two': 'harry g. laforge', 
		'expected': True, 
		'description': 'harry g laforge comparison with article'
	},
    {
		'name_one': 'harry h leonard',
		'name_two': 'harry wesley leonard', 
		'expected': False, 
		'description': 'harry h leonard comparison with article'
	},
    {
		'name_one': 'harry i leddel',
		'name_two': 'harry edwall', 
		'expected': False, 
		'description': 'harry i leddel comparison with article'
	},
    {
		'name_one': 'harry j deuel',
		'name_two': 'harry j. deuel', 
		'expected': True, 
		'description': 'harry j deuel comparison with article'
	},
    {
		'name_one': 'harry j digirolamo,sr',
		'name_two': 'harry j. de girolamo', 
		'expected': True, 
		'description': 'harry j digirolamo,sr comparison with article'
	},
    {
		'name_one': 'harry l chant',
		'name_two': 'harry leddy chant', 
		'expected': True, 
		'description': 'harry l chant comparison with article'
	},
    {
		'name_one': 'harry l hoffee',
		'name_two': 'harry lee hoffee', 
		'expected': True, 
		'description': 'harry l hoffee comparison with article'
	},
    {
		'name_one': 'harry l lantz',
		'name_two': 'harry lantz', 
		'expected': True, 
		'description': 'harry l lantz comparison with article'
	},
    {
		'name_one': 'harry l solberg',
		'name_two': 'harry leland solberg', 
		'expected': True, 
		'description': 'harry l solberg comparison with article'
	},
    {
		'name_one': 'harry l taylor',
		'name_two': 'harry leroy taylor', 
		'expected': True, 
		'description': 'harry l taylor comparison with article'
	},
    {
		'name_one': 'harry landis',
		'name_two': 'harry m. landis', 
		'expected': True, 
		'description': 'harry landis comparison with article'
	},
    {
		'name_one': 'harry lee',
		'name_two': 'douglas harry kedgwin lee', 
		'expected': True, 
		'description': 'harry lee comparison with article'
	},
    {
		'name_one': 'harry levy',
		'name_two': 'harry levy', 
		'expected': True, 
		'description': 'harry levy comparison with article'
	},
    {
		'name_one': 'harry m jr langsford',
		'name_two': 'harry langsford', 
		'expected': True, 
		'description': 'harry m jr langsford comparison with article'
	},
    {
		'name_one': 'harry r larson',
		'name_two': 'r. a. larson', 
		'expected': False, 
		'description': 'harry r larson comparison with article'
	},
    {
		'name_one': 'harry s bowman',
		'name_two': 'harry lake bowman', 
		'expected': False, 
		'description': 'harry s bowman comparison with article'
	},
    {
		'name_one': 'harry s duerow',
		'name_two': 'harry aaron derow', 
		'expected': False, 
		'description': 'harry s duerow comparison with article'
	},
    {
		'name_one': 'harry s legum',
		'name_two': 'samuel legum', 
		'expected': True, 
		'description': 'harry s legum comparison with article'
	},
    {
		'name_one': 'harry s vandiver',
		'name_two': 'harry schultz vandiver', 
		'expected': True, 
		'description': 'harry s vandiver comparison with article'
	},
    {
		'name_one': 'harry t levin',
		'name_two': 'harry tuchman levin', 
		'expected': True, 
		'description': 'harry t levin comparison with article'
	},
    {
		'name_one': 'harry v langeluttig',
		'name_two': 'h. v. langeluttig', 
		'expected': True, 
		'description': 'harry v langeluttig comparison with article'
	},
    {
		'name_one': 'harry w le fevre, iii',
		'name_two': 'harry wilson lefevre', 
		'expected': True, 
		'description': 'harry w le fevre, iii comparison with article'
	},
    {
		'name_one': 'harry w leacock',
		'name_two': 'emory w. luccock', 
		'expected': False, 
		'description': 'harry w leacock comparison with article'
	},
    {
		'name_one': 'harry w. vanneman',
		'name_two': 'harry walter vanneman', 
		'expected': True, 
		'description': 'harry w. vanneman comparison with article'
	},
    {
		'name_one': 'harvey b densmore',
		'name_two': 'harvey bruce densmore', 
		'expected': True, 
		'description': 'harvey b densmore comparison with article'
	},
    {
		'name_one': 'harvey b vanderford',
		'name_two': 'harvey birch vanderford', 
		'expected': True, 
		'description': 'harvey b vanderford comparison with article'
	},
    {
		'name_one': 'harvey c lehman',
		'name_two': 'harvey christian lehman', 
		'expected': True, 
		'description': 'harvey c lehman comparison with article'
	},
    {
		'name_one': 'harvey e lehman',
		'name_two': 'harvey eugene lehman', 
		'expected': True, 
		'description': 'harvey e lehman comparison with article'
	},
    {
		'name_one': 'harvey j brown',
		'name_two': 'harvey de bruine', 
		'expected': True, 
		'description': 'harvey j brown comparison with article'
	},
    {
		'name_one': 'harvey l carter',
		'name_two': 'harvey lewis carter', 
		'expected': True, 
		'description': 'harvey l carter comparison with article'
	},
    {
		'name_one': 'harvey l sweetman',
		'name_two': 'harvey leroy sweetman', 
		'expected': True, 
		'description': 'harvey l sweetman comparison with article'
	},
    {
		'name_one': 'harvey lee lantz',
		'name_two': 'harvey lee lantz', 
		'expected': True, 
		'description': 'harvey lee lantz comparison with article'
	},
    {
		'name_one': 'harwood l childs',
		'name_two': 'harwood lawrence childs', 
		'expected': True, 
		'description': 'harwood l childs comparison with article'
	},
    {
		'name_one': 'hazel b shands',
		'name_two': 'hazel lee shands', 
		'expected': False, 
		'description': 'hazel b shands comparison with article'
	},
    {
		'name_one': 'hazel d howe',
		'name_two': 'hazel dell howe', 
		'expected': True, 
		'description': 'hazel d howe comparison with article'
	},
    {
		'name_one': 'hazel g vance',
		'name_two': 'g. a. vance', 
		'expected': False, 
		'description': 'hazel g vance comparison with article'
	},
    {
		'name_one': 'hazel l morrison',
		'name_two': 'l. leotus morrison', 
		'expected': False, 
		'description': 'hazel l morrison comparison with article'
	},
    {
		'name_one': 'hazel m. lewis',
		'name_two': 'hazel m. lewis', 
		'expected': True, 
		'description': 'hazel m. lewis comparison with article'
	},
    {
		'name_one': 'hazel van ness',
		'name_two': 'hazel van ness', 
		'expected': True, 
		'description': 'hazel van ness comparison with article'
	},
    {
		'name_one': 'hector h lee',
		'name_two': 'hector lee', 
		'expected': True, 
		'description': 'hector h lee comparison with article'
	},
    {
		'name_one': 'heinz m vonfoerster',
		'name_two': 'heinz vonfoerster', 
		'expected': True, 
		'description': 'heinz m vonfoerster comparison with article'
	},
    {
		'name_one': 'helen a denyes',
		'name_two': 'helen arliss denyes', 
		'expected': True, 
		'description': 'helen a denyes comparison with article'
	},
    {
		'name_one': 'helen c deibert',
		'name_two': 'franklin c. daiber', 
		'expected': False, 
		'description': 'helen c deibert comparison with article'
	},
    {
		'name_one': 'helen g harris',
		'name_two': 'gould leach harris', 
		'expected': False, 
		'description': 'helen g harris comparison with article'
	},
    {
		'name_one': 'helen h law',
		'name_two': 'helen hull law', 
		'expected': True, 
		'description': 'helen h law comparison with article'
	},
    {
		'name_one': 'helen l richey',
		'name_two': 'helen lenore richey', 
		'expected': True, 
		'description': 'helen l richey comparison with article'
	},
    {
		'name_one': 'helen l smith',
		'name_two': 'helen leonore smith', 
		'expected': True, 
		'description': 'helen l smith comparison with article'
	},
    {
		'name_one': 'helen l stevens',
		'name_two': 'helen larson stevens', 
		'expected': True, 
		'description': 'helen l stevens comparison with article'
	},
    {
		'name_one': 'helen l van gilder',
		'name_two': 'helen louise van gilder', 
		'expected': True, 
		'description': 'helen l van gilder comparison with article'
	},
    {
		'name_one': 'helen l wikoff',
		'name_two': 'helen landman wikoff', 
		'expected': True, 
		'description': 'helen l wikoff comparison with article'
	},
    {
		'name_one': 'helen lamprechet',
		'name_two': 'helen lamprecht', 
		'expected': True, 
		'description': 'helen lamprechet comparison with article'
	},
    {
		'name_one': 'helen loskiewicz',
		'name_two': 'helen r. washkovich', 
		'expected': False, 
		'description': 'helen loskiewicz comparison with article'
	},
    {
		'name_one': 'helen ward',
		'name_two': 'helen lavina ward', 
		'expected': True, 
		'description': 'helen ward comparison with article'
	},
    {
		'name_one': 'helmit h vonerfe',
		'name_two': 'helmut h. von erffa', 
		'expected': True, 
		'description': 'helmit h vonerfe comparison with article'
	},
    {
		'name_one': 'helmit h vonerfer',
		'name_two': 'helmut h. von erffa', 
		'expected': True, 
		'description': 'helmit h vonerfer comparison with article'
	},
    {
		'name_one': 'heman l ibsen',
		'name_two': 'heman lauritz ibsen', 
		'expected': True, 
		'description': 'heman l ibsen comparison with article'
	},
    {
		'name_one': 'henning larson',
		'name_two': 'henning larsen', 
		'expected': True, 
		'description': 'henning larson comparison with article'
	},
    {
		'name_one': 'henry a lardy',
		'name_two': 'henry arnold lardy', 
		'expected': True, 
		'description': 'henry a lardy comparison with article'
	},
    {
		'name_one': 'henry a lasch',
		'name_two': 'henry lasch', 
		'expected': True, 
		'description': 'henry a lasch comparison with article'
	},
    {
		'name_one': 'henry a lepper',
		'name_two': 'henry albert lepper', 
		'expected': True, 
		'description': 'henry a lepper comparison with article'
	},
    {
		'name_one': 'henry a melander',
		'name_two': 'axel leonard melander', 
		'expected': False, 
		'description': 'henry a melander comparison with article'
	},
    {
		'name_one': 'henry a vandiest',
		'name_two': 'alice e. van diest', 
		'expected': False, 
		'description': 'henry a vandiest comparison with article'
	},
    {
		'name_one': 'henry b. lacey',
		'name_two': 'henry b. lacey', 
		'expected': True, 
		'description': 'henry b. lacey comparison with article'
	},
    {
		'name_one': 'henry d bockus, sr',
		'name_two': 'henry leroy bockus', 
		'expected': False, 
		'description': 'henry d bockus, sr comparison with article'
	},
    {
		'name_one': 'henry d cay',
		'name_two': 'henry george dekay', 
		'expected': False, 
		'description': 'henry d cay comparison with article'
	},
    {
		'name_one': 'henry d lederer',
		'name_two': 'henry david lederer', 
		'expected': True, 
		'description': 'henry d lederer comparison with article'
	},
    {
		'name_one': 'henry d smyth',
		'name_two': 'henry dewolf smyth', 
		'expected': True, 
		'description': 'henry d smyth comparison with article'
	},
    {
		'name_one': 'henry de vries,jr',
		'name_two': 'henry p. de vries', 
		'expected': True, 
		'description': 'henry de vries,jr comparison with article'
	},
    {
		'name_one': 'henry g lew',
		'name_two': 'henry g. lew', 
		'expected': True, 
		'description': 'henry g lew comparison with article'
	},
    {
		'name_one': 'henry h bergmann',
		'name_two': 'henry leonard birge', 
		'expected': False, 
		'description': 'henry h bergmann comparison with article'
	},
    {
		'name_one': 'henry k metcalf',
		'name_two': 'keyes dewitt metcalf', 
		'expected': False, 
		'description': 'henry k metcalf comparison with article'
	},
    {
		'name_one': 'henry l clarke',
		'name_two': 'henry leland clarke', 
		'expected': True, 
		'description': 'henry l clarke comparison with article'
	},
    {
		'name_one': 'henry l dean',
		'name_two': 'henry lee dean', 
		'expected': True, 
		'description': 'henry l dean comparison with article'
	},
    {
		'name_one': 'henry l kragbill',
		'name_two': 'henry lawrence kraybill', 
		'expected': True, 
		'description': 'henry l kragbill comparison with article'
	},
    {
		'name_one': 'henry l langhaar',
		'name_two': 'henry l. langhaar', 
		'expected': True, 
		'description': 'henry l langhaar comparison with article'
	},
    {
		'name_one': 'henry l lucas, jr',
		'name_two': 'henry lawrence lucas', 
		'expected': True, 
		'description': 'henry l lucas, jr comparison with article'
	},
    {
		'name_one': 'henry l marlowe',
		'name_two': 'l. dennis marlowe', 
		'expected': False, 
		'description': 'henry l marlowe comparison with article'
	},
    {
		'name_one': 'henry l miller',
		'name_two': 'henry laurence miller', 
		'expected': True, 
		'description': 'henry l miller comparison with article'
	},
    {
		'name_one': 'henry l robinson',
		'name_two': 'henry leon robinson', 
		'expected': True, 
		'description': 'henry l robinson comparison with article'
	},
    {
		'name_one': 'henry l seaver',
		'name_two': 'henry latimer seaver', 
		'expected': True, 
		'description': 'henry l seaver comparison with article'
	},
    {
		'name_one': 'henry l smith',
		'name_two': 'henry ladd smith', 
		'expected': True, 
		'description': 'henry l smith comparison with article'
	},
    {
		'name_one': 'henry l swint',
		'name_two': 'henry lee swint', 
		'expected': True, 
		'description': 'henry l swint comparison with article'
	},
    {
		'name_one': 'henry l van mater',
		'name_two': 'henry lear van mater', 
		'expected': True, 
		'description': 'henry l van mater comparison with article'
	},
    {
		'name_one': 'henry l warfres',
		'name_two': 'l. s. vander werf', 
		'expected': False, 
		'description': 'henry l warfres comparison with article'
	},
    {
		'name_one': 'henry leffert',
		'name_two': 'henry leffert', 
		'expected': True, 
		'description': 'henry leffert comparison with article'
	},
    {
		'name_one': 'henry negro',
		'name_two': 'enrico de negri', 
		'expected': True, 
		'description': 'henry negro comparison with article'
	},
    {
		'name_one': 'henry p lang',
		'name_two': 'paul henry lang', 
		'expected': True, 
		'description': 'henry p lang comparison with article'
	},
    {
		'name_one': 'henry r lefevre',
		'name_two': 'reginald r. lefebvre', 
		'expected': False, 
		'description': 'henry r lefevre comparison with article'
	},
    {
		'name_one': 'henry t van lith',
		'name_two': 'thomas henry leith', 
		'expected': True, 
		'description': 'henry t van lith comparison with article'
	},
    {
		'name_one': 'henry t van lith',
		'name_two': 'thomas henry lith', 
		'expected': True, 
		'description': 'henry t van lith comparison with article'
	},
    {
		'name_one': 'henry w vonholt',
		'name_two': 'henry w. von holt', 
		'expected': True, 
		'description': 'henry w vonholt comparison with article'
	},
    {
		'name_one': 'henry wilkins lewis',
		'name_two': 'henry wilkins lewis', 
		'expected': True, 
		'description': 'henry wilkins lewis comparison with article'
	},
    {
		'name_one': 'herbert a deane',
		'name_two': 'herbert a. deane', 
		'expected': True, 
		'description': 'herbert a deane comparison with article'
	},
    {
		'name_one': 'herbert a laitinen',
		'name_two': 'herbert a. laitinen', 
		'expected': True, 
		'description': 'herbert a laitinen comparison with article'
	},
    {
		'name_one': 'herbert c vandeventer',
		'name_two': 'herbert c. van deventer', 
		'expected': True, 
		'description': 'herbert c vandeventer comparison with article'
	},
    {
		'name_one': 'herbert d landahl',
		'name_two': 'herbert daniel landahl', 
		'expected': True, 
		'description': 'herbert d landahl comparison with article'
	},
    {
		'name_one': 'herbert denny orth',
		'name_two': 'herbert denny orth', 
		'expected': True, 
		'description': 'herbert denny orth comparison with article'
	},
    {
		'name_one': 'herbert deresiewicz',
		'name_two': 'herbert deresiewicz', 
		'expected': True, 
		'description': 'herbert deresiewicz comparison with article'
	},
    {
		'name_one': 'herbert f langdon',
		'name_two': 'herbert f. langdon', 
		'expected': True, 
		'description': 'herbert f langdon comparison with article'
	},
    {
		'name_one': 'herbert i bon haden',
		'name_two': 'herbert ira von haden', 
		'expected': True, 
		'description': 'herbert i bon haden comparison with article'
	},
    {
		'name_one': 'herbert j langen',
		'name_two': 'herbert j. langen', 
		'expected': True, 
		'description': 'herbert j langen comparison with article'
	},
    {
		'name_one': 'herbert l anderson',
		'name_two': 'herbert lawrence anderson', 
		'expected': True, 
		'description': 'herbert l anderson comparison with article'
	},
    {
		'name_one': 'herbert l bridges',
		'name_two': 'herbert lee bridges', 
		'expected': True, 
		'description': 'herbert l bridges comparison with article'
	},
    {
		'name_one': 'herbert l creek',
		'name_two': 'herbert le sourd creek', 
		'expected': True, 
		'description': 'herbert l creek comparison with article'
	},
    {
		'name_one': 'herbert l gilman',
		'name_two': 'herbert lester gilman', 
		'expected': True, 
		'description': 'herbert l gilman comparison with article'
	},
    {
		'name_one': 'herbert l sherman',
		'name_two': 'herbert leroy sherman', 
		'expected': True, 
		'description': 'herbert l sherman comparison with article'
	},
    {
		'name_one': 'herbert lattig',
		'name_two': 'herbert e lattig', 
		'expected': True, 
		'description': 'herbert lattig comparison with article'
	},
    {
		'name_one': 'herbert ler steele',
		'name_two': 'herbert l. steele', 
		'expected': True, 
		'description': 'herbert ler steele comparison with article'
	},
    {
		'name_one': 'herbert meritt',
		'name_two': 'herbert dean meritt', 
		'expected': True, 
		'description': 'herbert meritt comparison with article'
	},
    {
		'name_one': 'herbert w beckerath',
		'name_two': 'herbert von beckerath', 
		'expected': True, 
		'description': 'herbert w beckerath comparison with article'
	},
    {
		'name_one': 'herman donovan',
		'name_two': 'herman lee donovan', 
		'expected': True, 
		'description': 'herman donovan comparison with article'
	},
    {
		'name_one': 'herman g laughlin',
		'name_two': 'herman gleyn laughlin', 
		'expected': True, 
		'description': 'herman g laughlin comparison with article'
	},
    {
		'name_one': 'herman w larson',
		'name_two': 'curtis w. r. larson', 
		'expected': False, 
		'description': 'herman w larson comparison with article'
	},
    {
		'name_one': 'herman w larson',
		'name_two': 'herman w. larson', 
		'expected': True, 
		'description': 'herman w larson comparison with article'
	},
    {
		'name_one': 'herold l kooser',
		'name_two': 'herold lang kooser', 
		'expected': True, 
		'description': 'herold l kooser comparison with article'
	},
    {
		'name_one': 'herrell degraff',
		'name_two': 'herrell franklin degraff', 
		'expected': True, 
		'description': 'herrell degraff comparison with article'
	},
    {
		'name_one': 'herschel l roman',
		'name_two': 'herschel lewis roman', 
		'expected': True, 
		'description': 'herschel l roman comparison with article'
	},
    {
		'name_one': 'hilmer h laude',
		'name_two': 'hilmer henry laude', 
		'expected': True, 
		'description': 'hilmer h laude comparison with article'
	},
    {
		'name_one': 'homer r dehoney',
		'name_two': 'r. w. dehoney', 
		'expected': False, 
		'description': 'homer r dehoney comparison with article'
	},
    {
		'name_one': 'homer r lewis',
		'name_two': 'homer collier lewis', 
		'expected': False, 
		'description': 'homer r lewis comparison with article'
	},
    {
		'name_one': 'horace b vanvalkenburgh',
		'name_two': 'horace b. van valkenburgh', 
		'expected': True, 
		'description': 'horace b vanvalkenburgh comparison with article'
	},
    {
		'name_one': 'horace l barnett',
		'name_two': 'horace leslie barnett', 
		'expected': True, 
		'description': 'horace l barnett comparison with article'
	},
    {
		'name_one': 'horace l friess',
		'name_two': 'horace leland friess', 
		'expected': True, 
		'description': 'horace l friess comparison with article'
	},
    {
		'name_one': 'horace w leet',
		'name_two': 'horace w. leet', 
		'expected': True, 
		'description': 'horace w leet comparison with article'
	},
    {
		'name_one': 'horton laude',
		'name_two': 'horton m. laude', 
		'expected': True, 
		'description': 'horton laude comparison with article'
	},
    {
		'name_one': 'howard a lane',
		'name_two': 'howard a. lane', 
		'expected': True, 
		'description': 'howard a lane comparison with article'
	},
    {
		'name_one': 'howard boatwright',
		'name_two': 'howard leake boatwright', 
		'expected': True, 
		'description': 'howard boatwright comparison with article'
	},
    {
		'name_one': 'howard d smethers',
		'name_two': 'howard dewight smethers', 
		'expected': True, 
		'description': 'howard d smethers comparison with article'
	},
    {
		'name_one': 'howard l dunlap',
		'name_two': 'howard leroy dunlap', 
		'expected': True, 
		'description': 'howard l dunlap comparison with article'
	},
    {
		'name_one': 'howard l hall',
		'name_two': 'howard lewis hall', 
		'expected': True, 
		'description': 'howard l hall comparison with article'
	},
    {
		'name_one': 'howard l hamilton',
		'name_two': 'howard laverne hamilton', 
		'expected': True, 
		'description': 'howard l hamilton comparison with article'
	},
    {
		'name_one': 'howard l lange',
		'name_two': 'howard l. lange', 
		'expected': True, 
		'description': 'howard l lange comparison with article'
	},
    {
		'name_one': 'howard l nostrand',
		'name_two': 'howard lee nostrand', 
		'expected': True, 
		'description': 'howard l nostrand comparison with article'
	},
    {
		'name_one': 'howard levene',
		'name_two': 'howard levene', 
		'expected': True, 
		'description': 'howard levene comparison with article'
	},
    {
		'name_one': 'howard levi',
		'name_two': 'howard levi', 
		'expected': True, 
		'description': 'howard levi comparison with article'
	},
    {
		'name_one': 'howard mckinney',
		'name_two': 'howard decker mckinney', 
		'expected': True, 
		'description': 'howard mckinney comparison with article'
	},
    {
		'name_one': 'howard o deming',
		'name_two': 'howard o. deming', 
		'expected': True, 
		'description': 'howard o deming comparison with article'
	},
    {
		'name_one': 'howard o. deay',
		'name_two': 'howard owen deay', 
		'expected': True, 
		'description': 'howard o. deay comparison with article'
	},
    {
		'name_one': 'howard r lamar',
		'name_two': 'howard roberts lamar', 
		'expected': True, 
		'description': 'howard r lamar comparison with article'
	},
    {
		'name_one': 'howard r mitchell',
		'name_two': 'howard lee mitchell', 
		'expected': False, 
		'description': 'howard r mitchell comparison with article'
	},
    {
		'name_one': 'howard w larsh',
		'name_two': 'howard william larsh', 
		'expected': True, 
		'description': 'howard w larsh comparison with article'
	},
    {
		'name_one': 'howard w lattin',
		'name_two': 'gerald w. lattin', 
		'expected': False, 
		'description': 'howard w lattin comparison with article'
	},
    {
		'name_one': 'howard w lewis',
		'name_two': 'howard thompson lewis', 
		'expected': False, 
		'description': 'howard w lewis comparison with article'
	},
    {
		'name_one': 'hubert g dearicks',
		'name_two': 'hubert g. derrick', 
		'expected': True, 
		'description': 'hubert g dearicks comparison with article'
	},
    {
		'name_one': 'hubert olin',
		'name_two': 'hubert leonard olin', 
		'expected': True, 
		'description': 'hubert olin comparison with article'
	},
    {
		'name_one': 'hubert w lamb',
		'name_two': 'hubert weldon lamb', 
		'expected': True, 
		'description': 'hubert w lamb comparison with article'
	},
    {
		'name_one': 'huey kesing ay lee',
		'name_two': 'kwan hua lee', 
		'expected': False, 
		'description': 'huey kesing ay lee comparison with article'
	},
    {
		'name_one': 'hugh d. laughlin',
		'name_two': 'hugh donald laughlin', 
		'expected': True, 
		'description': 'hugh d. laughlin comparison with article'
	},
    {
		'name_one': 'hugh hodgson',
		'name_two': 'hugh leslie hodgson', 
		'expected': True, 
		'description': 'hugh hodgson comparison with article'
	},
    {
		'name_one': 'hugh t lefler',
		'name_two': 'hugh talmage lefler', 
		'expected': True, 
		'description': 'hugh t lefler comparison with article'
	},
    {
		'name_one': 'hugo l blownquist',
		'name_two': 'hugo leander blomquist', 
		'expected': True, 
		'description': 'hugo l blownquist comparison with article'
	},
    {
		'name_one': 'hulda garrett',
		'name_two': 'hulda van steeter garrett', 
		'expected': True, 
		'description': 'hulda garrett comparison with article'
	},
    {
		'name_one': 'ida o haigh',
		'name_two': 'ida deck haigh', 
		'expected': False, 
		'description': 'ida o haigh comparison with article'
	},
    {
		'name_one': 'ike f. deeter',
		'name_two': 'ike deeter', 
		'expected': True, 
		'description': 'ike f. deeter comparison with article'
	},
    {
		'name_one': 'ina leone strom',
		'name_two': 'ina l. strom', 
		'expected': True, 
		'description': 'ina leone strom comparison with article'
	},
    {
		'name_one': 'ina van stan',
		'name_two': 'ina vanstan', 
		'expected': True, 
		'description': 'ina van stan comparison with article'
	},
    {
		'name_one': 'ira d porterfield',
		'name_two': 'ira deward porterfield', 
		'expected': True, 
		'description': 'ira d porterfield comparison with article'
	},
    {
		'name_one': 'ira l collier',
		'name_two': 'ira leonard collier', 
		'expected': True, 
		'description': 'ira l collier comparison with article'
	},
    {
		'name_one': 'ira la rivers',
		'name_two': 'ira larivers', 
		'expected': True, 
		'description': 'ira la rivers comparison with article'
	},
    {
		'name_one': 'ira v lee',
		'name_two': 'ira d. lee', 
		'expected': False, 
		'description': 'ira v lee comparison with article'
	},
    {
		'name_one': 'ira williams',
		'name_two': 'ira lawson williams', 
		'expected': True, 
		'description': 'ira williams comparison with article'
	},
    {
		'name_one': 'irene e van osdel',
		'name_two': 'edgar bates van osdel', 
		'expected': False, 
		'description': 'irene e van osdel comparison with article'
	},
    {
		'name_one': 'irene s lashey',
		'name_two': 'karl spencer lashley', 
		'expected': False, 
		'description': 'irene s lashey comparison with article'
	},
    {
		'name_one': 'irene s lavant',
		'name_two': 'leopoldo santiago lavandero', 
		'expected': False, 
		'description': 'irene s lavant comparison with article'
	},
    {
		'name_one': 'irving h lepow',
		'name_two': 'irwin howard lepow', 
		'expected': False, 
		'description': 'irving h lepow comparison with article'
	},
    {
		'name_one': 'irving j lee',
		'name_two': 'irving j. lee', 
		'expected': True, 
		'description': 'irving j lee comparison with article'
	},
    {
		'name_one': 'irving l janis',
		'name_two': 'irving lester janis', 
		'expected': True, 
		'description': 'irving l janis comparison with article'
	},
    {
		'name_one': 'irving o dein',
		'name_two': 'irving o. dein', 
		'expected': True, 
		'description': 'irving o dein comparison with article'
	},
    {
		'name_one': 'irving peterson',
		'name_two': 'irving leonard peterson', 
		'expected': True, 
		'description': 'irving peterson comparison with article'
	},
    {
		'name_one': 'irwin i levine',
		'name_two': 'l. i. levine', 
		'expected': False, 
		'description': 'irwin i levine comparison with article'
	},
    {
		'name_one': 'isaac leroy domingus',
		'name_two': 'isaac leroy domingos', 
		'expected': True, 
		'description': 'isaac leroy domingus comparison with article'
	},
    {
		'name_one': 'isaac lewin',
		'name_two': 'isaac lewin', 
		'expected': True, 
		'description': 'isaac lewin comparison with article'
	},
    {
		'name_one': 'isabel lewis',
		'name_two': 'isabel boyd lewis', 
		'expected': True, 
		'description': 'isabel lewis comparison with article'
	},
    {
		'name_one': 'isabelle r lebreton',
		'name_two': 'dagmar renshaw lebreton', 
		'expected': False, 
		'description': 'isabelle r lebreton comparison with article'
	},
    {
		'name_one': 'isidore l robbins',
		'name_two': 'isidore leon robbins', 
		'expected': True, 
		'description': 'isidore l robbins comparison with article'
	},
    {
		'name_one': 'ivan l hill',
		'name_two': 'ivan leroy hill', 
		'expected': True, 
		'description': 'ivan l hill comparison with article'
	},
    {
		'name_one': 'ivan l little',
		'name_two': 'ivan lee little', 
		'expected': True, 
		'description': 'ivan l little comparison with article'
	},
    {
		'name_one': 'ivan m lee',
		'name_two': 'ivan m. lee', 
		'expected': True, 
		'description': 'ivan m lee comparison with article'
	},
    {
		'name_one': 'ivor d spencer',
		'name_two': 'ivor debenham spencer', 
		'expected': True, 
		'description': 'ivor d spencer comparison with article'
	},
    {
		'name_one': 'j andreas (joseph andreas) de marco',
		'name_two': 'rene j. marcou', 
		'expected': False, 
		'description': 'j andreas (joseph andreas) de marco comparison with article'
	},
    {
		'name_one': 'j dean swift',
		'name_two': 'j. dean swift', 
		'expected': True, 
		'description': 'j dean swift comparison with article'
	},
    {
		'name_one': 'j deryl hart',
		'name_two': 'julian deryl hart', 
		'expected': True, 
		'description': 'j deryl hart comparison with article'
	},
    {
		'name_one': 'j howard demar',
		'name_two': 'howard h. lamar', 
		'expected': False, 
		'description': 'j howard demar comparison with article'
	},
    {
		'name_one': 'j lawton ellis',
		'name_two': 'j. lawton ellis', 
		'expected': True, 
		'description': 'j lawton ellis comparison with article'
	},
    {
		'name_one': 'j layton fraser',
		'name_two': 'thomas layton fraser', 
		'expected': False, 
		'description': 'j layton fraser comparison with article'
	},
    {
		'name_one': 'j leonard brandt',
		'name_two': 'j. leonard brandt', 
		'expected': True, 
		'description': 'j leonard brandt comparison with article'
	},
    {
		'name_one': 'j leonard goldner',
		'name_two': 'joseph leonard goldner', 
		'expected': True, 
		'description': 'j leonard goldner comparison with article'
	},
    {
		'name_one': 'j leroy anderson',
		'name_two': 'leray j. anderson', 
		'expected': True, 
		'description': 'j leroy anderson comparison with article'
	},
    {
		'name_one': 'j lewis allison',
		'name_two': 'joseph lewis allison', 
		'expected': True, 
		'description': 'j lewis allison comparison with article'
	},
    {
		'name_one': 'j lewis maynard',
		'name_two': 'j. lewis maynard', 
		'expected': True, 
		'description': 'j lewis maynard comparison with article'
	},
    {
		'name_one': 'j paul leonard',
		'name_two': 'j paul leonard', 
		'expected': True, 
		'description': 'j paul leonard comparison with article'
	},
    {
		'name_one': 'j s ladd thomas',
		'name_two': 'j. s. ladd thomas', 
		'expected': True, 
		'description': 'j s ladd thomas comparison with article'
	},
    {
		'name_one': 'j warren lee',
		'name_two': 'james warren lee', 
		'expected': True, 
		'description': 'j warren lee comparison with article'
	},
    {
		'name_one': 'j. murray lee',
		'name_two': 'j. murray lee', 
		'expected': True, 
		'description': 'j. murray lee comparison with article'
	},
    {
		'name_one': 'j. raymond derby',
		'name_two': 'j. raymond derby', 
		'expected': True, 
		'description': 'j. raymond derby comparison with article'
	},
    {
		'name_one': 'j. wayne ley',
		'name_two': 'j. wayne ley', 
		'expected': True, 
		'description': 'j. wayne ley comparison with article'
	},
    {
		'name_one': 'jack a denison',
		'name_two': 'jack a. denison', 
		'expected': True, 
		'description': 'jack a denison comparison with article'
	},
    {
		'name_one': 'jack j detzler',
		'name_two': 'jack j. detzler', 
		'expected': True, 
		'description': 'jack j detzler comparison with article'
	},
    {
		'name_one': 'jack layton',
		'name_two': 'jack malcolm layton', 
		'expected': True, 
		'description': 'jack layton comparison with article'
	},
    {
		'name_one': 'jack lenhart',
		'name_two': 'jack lenhart', 
		'expected': True, 
		'description': 'jack lenhart comparison with article'
	},
    {
		'name_one': 'jack levine',
		'name_two': 'jack levine', 
		'expected': True, 
		'description': 'jack levine comparison with article'
	},
    {
		'name_one': 'jack r leonards',
		'name_two': 'jack ralph leonards', 
		'expected': True, 
		'description': 'jack r leonards comparison with article'
	},
    {
		'name_one': 'jacob a o larsen',
		'name_two': 'jakob aall ottesen larsen', 
		'expected': True, 
		'description': 'jacob a o larsen comparison with article'
	},
    {
		'name_one': 'jacob f leibald',
		'name_two': 'f. l. liebolt', 
		'expected': False, 
		'description': 'jacob f leibald comparison with article'
	},
    {
		'name_one': 'jacob haas',
		'name_two': 'jacob anton de haas', 
		'expected': True, 
		'description': 'jacob haas comparison with article'
	},
    {
		'name_one': 'jacob levine',
		'name_two': 'jacob levine', 
		'expected': True, 
		'description': 'jacob levine comparison with article'
	},
    {
		'name_one': 'jacob levitt',
		'name_two': 'jacob levitt', 
		'expected': True, 
		'description': 'jacob levitt comparison with article'
	},
    {
		'name_one': 'jacob van ek',
		'name_two': 'jacob van ek', 
		'expected': True, 
		'description': 'jacob van ek comparison with article'
	},
    {
		'name_one': 'jacob vanderzee',
		'name_two': 'jacob van der zee', 
		'expected': True, 
		'description': 'jacob vanderzee comparison with article'
	},
    {
		'name_one': 'jacqueline a rochelle',
		'name_two': 'augustine larochelle', 
		'expected': True, 
		'description': 'jacqueline a rochelle comparison with article'
	},
    {
		'name_one': 'jacqueline e delaharp',
		'name_two': 'jacqueline de la harpe', 
		'expected': True, 
		'description': 'jacqueline e delaharp comparison with article'
	},
    {
		'name_one': 'jadan g jr lee',
		'name_two': 'jordan g. lee', 
		'expected': False, 
		'description': 'jadan g jr lee comparison with article'
	},
    {
		'name_one': 'james b lewis',
		'name_two': 'b. roland lewis', 
		'expected': False, 
		'description': 'james b lewis comparison with article'
	},
    {
		'name_one': 'james b ley',
		'name_two': 'b. james ley', 
		'expected': True, 
		'description': 'james b ley comparison with article'
	},
    {
		'name_one': 'james c landon',
		'name_two': 'f. c. lendrum', 
		'expected': False, 
		'description': 'james c landon comparison with article'
	},
    {
		'name_one': 'james c mc leod',
		'name_two': 'james currie mcleod', 
		'expected': True, 
		'description': 'james c mc leod comparison with article'
	},
    {
		'name_one': 'james d decker',
		'name_two': 'james d. decker', 
		'expected': True, 
		'description': 'james d decker comparison with article'
	},
    {
		'name_one': 'james d heard',
		'name_two': 'james delaven heard', 
		'expected': True, 
		'description': 'james d heard comparison with article'
	},
    {
		'name_one': 'james d. wilson',
		'name_two': 'james dean wilson', 
		'expected': True, 
		'description': 'james d. wilson comparison with article'
	},
    {
		'name_one': 'james derr',
		'name_two': 'james g. derr', 
		'expected': True, 
		'description': 'james derr comparison with article'
	},
    {
		'name_one': 'james dewey',
		'name_two': 'james edwin dewey', 
		'expected': True, 
		'description': 'james dewey comparison with article'
	},
    {
		'name_one': 'james e deese',
		'name_two': 'james earle deese', 
		'expected': True, 
		'description': 'james e deese comparison with article'
	},
    {
		'name_one': 'james e dew',
		'name_two': 'james e. dew', 
		'expected': True, 
		'description': 'james e dew comparison with article'
	},
    {
		'name_one': 'james e lebensohn',
		'name_two': 'james elzer lebensohn', 
		'expected': True, 
		'description': 'james e lebensohn comparison with article'
	},
    {
		'name_one': 'james e legates',
		'name_two': 'james edward legates', 
		'expected': True, 
		'description': 'james e legates comparison with article'
	},
    {
		'name_one': 'james e lewis',
		'name_two': 'james e. lewis', 
		'expected': True, 
		'description': 'james e lewis comparison with article'
	},
    {
		'name_one': 'james f campbell',
		'name_two': 'james lawder gamble', 
		'expected': False, 
		'description': 'james f campbell comparison with article'
	},
    {
		'name_one': 'james g vanderpool',
		'name_two': 'james g. vanderpool', 
		'expected': True, 
		'description': 'james g vanderpool comparison with article'
	},
    {
		'name_one': 'james h decker',
		'name_two': 'james h. decker', 
		'expected': True, 
		'description': 'james h decker comparison with article'
	},
    {
		'name_one': 'james h leathem',
		'name_two': 'james h. leathem', 
		'expected': True, 
		'description': 'james h leathem comparison with article'
	},
    {
		'name_one': 'james j de costa',
		'name_two': 'edwin j. decosta', 
		'expected': False, 
		'description': 'james j de costa comparison with article'
	},
    {
		'name_one': 'james j devine',
		'name_two': 'james j. devine', 
		'expected': True, 
		'description': 'james j devine comparison with article'
	},
    {
		'name_one': 'james j devlin',
		'name_two': 'james j. devlin', 
		'expected': True, 
		'description': 'james j devlin comparison with article'
	},
    {
		'name_one': 'james j lawlor',
		'name_two': 'james joseph lawlor', 
		'expected': True, 
		'description': 'james j lawlor comparison with article'
	},
    {
		'name_one': 'james j leahy',
		'name_two': 'james j. leahy', 
		'expected': True, 
		'description': 'james j leahy comparison with article'
	},
    {
		'name_one': 'james l botsford',
		'name_two': 'james lawrence botsford', 
		'expected': True, 
		'description': 'james l botsford comparison with article'
	},
    {
		'name_one': 'james l carrico',
		'name_two': 'james leon carrico', 
		'expected': True, 
		'description': 'james l carrico comparison with article'
	},
    {
		'name_one': 'james l cate',
		'name_two': 'james lea cate', 
		'expected': True, 
		'description': 'james l cate comparison with article'
	},
    {
		'name_one': 'james l cronin',
		'name_two': 'james lawrence cronin', 
		'expected': True, 
		'description': 'james l cronin comparison with article'
	},
    {
		'name_one': 'james l deegan',
		'name_two': 'james wayne deegan', 
		'expected': False, 
		'description': 'james l deegan comparison with article'
	},
    {
		'name_one': 'james l guenveur',
		'name_two': 'james lapenne guenveur', 
		'expected': True, 
		'description': 'james l guenveur comparison with article'
	},
    {
		'name_one': 'james l hall',
		'name_two': 'james lester hall', 
		'expected': True, 
		'description': 'james l hall comparison with article'
	},
    {
		'name_one': 'james l leach',
		'name_two': 'james l. leach', 
		'expected': True, 
		'description': 'james l leach comparison with article'
	},
    {
		'name_one': 'james l lee',
		'name_two': 'luther james lee', 
		'expected': True, 
		'description': 'james l lee comparison with article'
	},
    {
		'name_one': 'james l leggett',
		'name_two': 'james llewellyn leggett', 
		'expected': True, 
		'description': 'james l leggett comparison with article'
	},
    {
		'name_one': 'james l leroy',
		'name_two': 'l. w. leroy', 
		'expected': False, 
		'description': 'james l leroy comparison with article'
	},
    {
		'name_one': 'james l meriam',
		'name_two': 'james lathrop meriam', 
		'expected': True, 
		'description': 'james l meriam comparison with article'
	},
    {
		'name_one': 'james l moore',
		'name_two': 'james legrand moore', 
		'expected': True, 
		'description': 'james l moore comparison with article'
	},
    {
		'name_one': 'james l morrill',
		'name_two': 'james lewis morrill', 
		'expected': True, 
		'description': 'james l morrill comparison with article'
	},
    {
		'name_one': 'james l reycroft, jr',
		'name_two': 'james leonard reycraft', 
		'expected': True, 
		'description': 'james l reycroft, jr comparison with article'
	},
    {
		'name_one': 'james l sellers',
		'name_two': 'james lee sellers', 
		'expected': True, 
		'description': 'james l sellers comparison with article'
	},
    {
		'name_one': 'james l whittenberger',
		'name_two': 'james laverre whittenberger', 
		'expected': True, 
		'description': 'james l whittenberger comparison with article'
	},
    {
		'name_one': 'james lape',
		'name_two': 'james l lapoe', 
		'expected': True, 
		'description': 'james lape comparison with article'
	},
    {
		'name_one': 'james lawrence',
		'name_two': 'james vantine lawrence', 
		'expected': True, 
		'description': 'james lawrence comparison with article'
	},
    {
		'name_one': 'james lechay',
		'name_two': 'james lechay', 
		'expected': True, 
		'description': 'james lechay comparison with article'
	},
    {
		'name_one': 'james levitt',
		'name_two': 'james d. levitt', 
		'expected': True, 
		'description': 'james levitt comparison with article'
	},
    {
		'name_one': 'james m lamb',
		'name_two': 'marion m. lamb', 
		'expected': False, 
		'description': 'james m lamb comparison with article'
	},
    {
		'name_one': 'james m lavin',
		'name_two': 'james m. lavin', 
		'expected': True, 
		'description': 'james m lavin comparison with article'
	},
    {
		'name_one': 'james m leavey',
		'name_two': 'james m. leavey', 
		'expected': True, 
		'description': 'james m leavey comparison with article'
	},
    {
		'name_one': 'james m ledanard',
		'name_two': 'james lawrence lardner', 
		'expected': False, 
		'description': 'james m ledanard comparison with article'
	},
    {
		'name_one': 'james mahler',
		'name_two': 'james lewis mahler', 
		'expected': True, 
		'description': 'james mahler comparison with article'
	},
    {
		'name_one': 'james r degroat',
		'name_two': 'james r. degroat', 
		'expected': True, 
		'description': 'james r degroat comparison with article'
	},
    {
		'name_one': 'james r latimer',
		'name_two': 'richmond lattimore', 
		'expected': True, 
		'description': 'james r latimer comparison with article'
	},
    {
		'name_one': 'james r van dyke',
		'name_two': 'james r. van dyke', 
		'expected': True, 
		'description': 'james r van dyke comparison with article'
	},
    {
		'name_one': 'james robert hall',
		'name_two': 'robert leon hall', 
		'expected': False, 
		'description': 'james robert hall comparison with article'
	},
    {
		'name_one': 'james s howe',
		'name_two': 'james lewis howe', 
		'expected': False, 
		'description': 'james s howe comparison with article'
	},
    {
		'name_one': 'james s lemen',
		'name_two': 'janice speer lemen', 
		'expected': False, 
		'description': 'james s lemen comparison with article'
	},
    {
		'name_one': 'james t lapsley, jr',
		'name_two': 'james t. lapsley', 
		'expected': True, 
		'description': 'james t lapsley, jr comparison with article'
	},
    {
		'name_one': 'james v delgiudace',
		'name_two': 'valentine l. telegdi', 
		'expected': False, 
		'description': 'james v delgiudace comparison with article'
	},
    {
		'name_one': 'james v newman',
		'name_two': 'james leet valentine newman', 
		'expected': True, 
		'description': 'james v newman comparison with article'
	},
    {
		'name_one': 'james v rice',
		'name_two': 'james van nostran rice', 
		'expected': True, 
		'description': 'james v rice comparison with article'
	},
    {
		'name_one': 'james van ness',
		'name_two': 'james edward van ness', 
		'expected': True, 
		'description': 'james van ness comparison with article'
	},
    {
		'name_one': 'james w haun',
		'name_two': 'james r. dehaan', 
		'expected': False, 
		'description': 'james w haun comparison with article'
	},
    {
		'name_one': 'james w. lesley',
		'name_two': 'james w. lesley', 
		'expected': True, 
		'description': 'james w. lesley comparison with article'
	},
    {
		'name_one': 'jan a vanden brook',
		'name_two': 'jan abram van den broek', 
		'expected': True, 
		'description': 'jan a vanden brook comparison with article'
	},
    {
		'name_one': 'jane a lawson',
		'name_two': 'jane sorrie lawson', 
		'expected': False, 
		'description': 'jane a lawson comparison with article'
	},
    {
		'name_one': 'jane b van deusen',
		'name_two': 'jayne c. van deusen', 
		'expected': False, 
		'description': 'jane b van deusen comparison with article'
	},
    {
		'name_one': 'jane f desforges',
		'name_two': 'jane f. desforges', 
		'expected': True, 
		'description': 'jane f desforges comparison with article'
	},
    {
		'name_one': 'jane g demarest',
		'name_two': 'g. stuart demarest', 
		'expected': False, 
		'description': 'jane g demarest comparison with article'
	},
    {
		'name_one': 'jane l gardner',
		'name_two': 'jane lester gardner', 
		'expected': True, 
		'description': 'jane l gardner comparison with article'
	},
    {
		'name_one': 'janice a lazarre',
		'name_two': 'arnold lazarow', 
		'expected': False, 
		'description': 'janice a lazarre comparison with article'
	},
    {
		'name_one': 'janice vanderwater',
		'name_two': 'janice o. van de water', 
		'expected': True, 
		'description': 'janice vanderwater comparison with article'
	},
    {
		'name_one': 'jasper l callaway',
		'name_two': 'jasper lamar callaway', 
		'expected': True, 
		'description': 'jasper l callaway comparison with article'
	},
    {
		'name_one': 'jasper stuckey',
		'name_two': 'jasper leonidas stuckey', 
		'expected': True, 
		'description': 'jasper stuckey comparison with article'
	},
    {
		'name_one': 'jay c vankirk',
		'name_two': 'jay calvin van kirk', 
		'expected': True, 
		'description': 'jay c vankirk comparison with article'
	},
    {
		'name_one': 'jay laurence lush',
		'name_two': 'jay laurence lush', 
		'expected': True, 
		'description': 'jay laurence lush comparison with article'
	},
    {
		'name_one': 'jean blattel',
		'name_two': 'jean van bladel', 
		'expected': True, 
		'description': 'jean blattel comparison with article'
	},
    {
		'name_one': 'jean c gallaher',
		'name_two': 'clark van galder', 
		'expected': False, 
		'description': 'jean c gallaher comparison with article'
	},
    {
		'name_one': 'jean hansen',
		'name_two': 'jean lee hansen', 
		'expected': True, 
		'description': 'jean hansen comparison with article'
	},
    {
		'name_one': 'jean j demorest',
		'name_two': 'jean-jacques demorest', 
		'expected': True, 
		'description': 'jean j demorest comparison with article'
	},
    {
		'name_one': 'jean johnston',
		'name_two': 'jean vance johnston', 
		'expected': True, 
		'description': 'jean johnston comparison with article'
	},
    {
		'name_one': 'jean labatut',
		'name_two': 'jean labatut', 
		'expected': True, 
		'description': 'jean labatut comparison with article'
	},
    {
		'name_one': 'jean m demos',
		'name_two': 'jean m. demos', 
		'expected': True, 
		'description': 'jean m demos comparison with article'
	},
    {
		'name_one': 'jean p lesperance',
		'name_two': 'jean paul lesperance', 
		'expected': True, 
		'description': 'jean p lesperance comparison with article'
	},
    {
		'name_one': 'jeanette o laflamme',
		'name_two': 'floyd o. flom', 
		'expected': False, 
		'description': 'jeanette o laflamme comparison with article'
	},
    {
		'name_one': 'jeannette laguaite',
		'name_two': 'jeannette katherine laguaite', 
		'expected': True, 
		'description': 'jeannette laguaite comparison with article'
	},
    {
		'name_one': 'jennie l epps',
		'name_two': 'jennie lee epps', 
		'expected': True, 
		'description': 'jennie l epps comparison with article'
	},
    {
		'name_one': 'jeremiah d ford',
		'name_two': 'jeremiah denis matthias ford', 
		'expected': True, 
		'description': 'jeremiah d ford comparison with article'
	},
    {
		'name_one': 'jeremonah c lehane',
		'name_two': 'jeremiah lehane', 
		'expected': True, 
		'description': 'jeremonah c lehane comparison with article'
	},
    {
		'name_one': 'jerome j. dee',
		'name_two': 'jerome j. dee', 
		'expected': True, 
		'description': 'jerome j. dee comparison with article'
	},
    {
		'name_one': 'jerome l le master',
		'name_two': 'jerome lloyd lemaster', 
		'expected': True, 
		'description': 'jerome l le master comparison with article'
	},
    {
		'name_one': 'jesse deboer',
		'name_two': 'jesse deboer', 
		'expected': True, 
		'description': 'jesse deboer comparison with article'
	},
    {
		'name_one': 'jesse l charlton',
		'name_two': 'jesse laurence charlton', 
		'expected': True, 
		'description': 'jesse l charlton comparison with article'
	},
    {
		'name_one': 'jesse l rader',
		'name_two': 'jesse lee rader', 
		'expected': True, 
		'description': 'jesse l rader comparison with article'
	},
    {
		'name_one': 'jesse l rose',
		'name_two': 'jesse lee rose', 
		'expected': True, 
		'description': 'jesse l rose comparison with article'
	},
    {
		'name_one': 'jesse lefforge',
		'name_two': 'jess h. lefforge', 
		'expected': True, 
		'description': 'jesse lefforge comparison with article'
	},
    {
		'name_one': 'jessie l p delprat',
		'name_two': 'jessie l. p. delprat', 
		'expected': True, 
		'description': 'jessie l p delprat comparison with article'
	},
    {
		'name_one': 'jessie l paul',
		'name_two': 'jessie leonore paul', 
		'expected': True, 
		'description': 'jessie l paul comparison with article'
	},
    {
		'name_one': 'jessie larson',
		'name_two': 'jessie larsen', 
		'expected': True, 
		'description': 'jessie larson comparison with article'
	},
    {
		'name_one': 'jimmy lee larue',
		'name_two': 'jimmae larue', 
		'expected': True, 
		'description': 'jimmy lee larue comparison with article'
	},
    {
		'name_one': 'joe dennis',
		'name_two': 'joe dennis', 
		'expected': True, 
		'description': 'joe dennis comparison with article'
	},
    {
		'name_one': 'joe l haddon',
		'name_two': 'joe leon haddon', 
		'expected': True, 
		'description': 'joe l haddon comparison with article'
	},
    {
		'name_one': 'joe l lawson, jr',
		'name_two': 'joe l. lawson', 
		'expected': True, 
		'description': 'joe l lawson, jr comparison with article'
	},
    {
		'name_one': 'joel p dean',
		'name_two': 'joel dean', 
		'expected': True, 
		'description': 'joel p dean comparison with article'
	},
    {
		'name_one': 'joesph p lasalle',
		'name_two': 'joseph p. lasalle', 
		'expected': True, 
		'description': 'joesph p lasalle comparison with article'
	},
    {
		'name_one': 'joffre l coe',
		'name_two': 'joffre lanning coe', 
		'expected': True, 
		'description': 'joffre l coe comparison with article'
	},
    {
		'name_one': 'johannis l boysen',
		'name_two': 'joh. lassen boysen', 
		'expected': True, 
		'description': 'johannis l boysen comparison with article'
	},
    {
		'name_one': 'john a de novo',
		'name_two': 'john a. denovo', 
		'expected': True, 
		'description': 'john a de novo comparison with article'
	},
    {
		'name_one': 'john a l saunders',
		'name_two': 'john alvah lee saunders', 
		'expected': True, 
		'description': 'john a l saunders comparison with article'
	},
    {
		'name_one': 'john a lanz',
		'name_two': 'john tollet lantz', 
		'expected': False, 
		'description': 'john a lanz comparison with article'
	},
    {
		'name_one': 'john a leavitt',
		'name_two': 'john anton leavitt', 
		'expected': True, 
		'description': 'john a leavitt comparison with article'
	},
    {
		'name_one': 'john a leiter',
		'name_two': 'hans leitner', 
		'expected': True, 
		'description': 'john a leiter comparison with article'
	},
    {
		'name_one': 'john a lester, jr',
		'name_two': 'john ashby lester', 
		'expected': True, 
		'description': 'john a lester, jr comparison with article'
	},
    {
		'name_one': 'john a spencer',
		'name_two': 'john lebaron spencer', 
		'expected': False, 
		'description': 'john a spencer comparison with article'
	},
    {
		'name_one': 'john b deluca',
		'name_two': 'georg hans bhawani luck', 
		'expected': False, 
		'description': 'john b deluca comparison with article'
	},
    {
		'name_one': 'john b fine',
		'name_two': 'john van antwerp fine', 
		'expected': False, 
		'description': 'john b fine comparison with article'
	},
    {
		'name_one': 'john b lagen',
		'name_two': 'john b. lagen', 
		'expected': True, 
		'description': 'john b lagen comparison with article'
	},
    {
		'name_one': 'john b larndry',
		'name_two': 'john b. larnen', 
		'expected': False, 
		'description': 'john b larndry comparison with article'
	},
    {
		'name_one': 'john b lentz',
		'name_two': 'john beckley lentz', 
		'expected': True, 
		'description': 'john b lentz comparison with article'
	},
    {
		'name_one': 'john b lewis',
		'name_two': 'john barkley lewis', 
		'expected': True, 
		'description': 'john b lewis comparison with article'
	},
    {
		'name_one': 'john b longstaff',
		'name_two': 'john bailey langstaff', 
		'expected': True, 
		'description': 'john b longstaff comparison with article'
	},
    {
		'name_one': 'john blair',
		'name_two': 'john dennis blair', 
		'expected': True, 
		'description': 'john blair comparison with article'
	},
    {
		'name_one': 'john c de wolfe',
		'name_two': 'john c. g. wulff', 
		'expected': True, 
		'description': 'john c de wolfe comparison with article'
	},
    {
		'name_one': 'john c lapp',
		'name_two': 'john clarke lapp', 
		'expected': True, 
		'description': 'john c lapp comparison with article'
	},
    {
		'name_one': 'john c snell',
		'name_two': 'john leslie snell', 
		'expected': False, 
		'description': 'john c snell comparison with article'
	},
    {
		'name_one': 'john c wilson',
		'name_two': 'john lacy wilson', 
		'expected': False, 
		'description': 'john c wilson comparison with article'
	},
    {
		'name_one': 'john campbell lester',
		'name_two': 'j. campbell lester', 
		'expected': True, 
		'description': 'john campbell lester comparison with article'
	},
    {
		'name_one': 'john cutler',
		'name_two': 'john levi cutler', 
		'expected': True, 
		'description': 'john cutler comparison with article'
	},
    {
		'name_one': 'john d brackett',
		'name_two': 'john denis bracket', 
		'expected': True, 
		'description': 'john d brackett comparison with article'
	},
    {
		'name_one': 'john d brackett',
		'name_two': 'john denis brackett', 
		'expected': True, 
		'description': 'john d brackett comparison with article'
	},
    {
		'name_one': 'john day larkin',
		'name_two': 'john day larkin', 
		'expected': True, 
		'description': 'john day larkin comparison with article'
	},
    {
		'name_one': 'john decarlo,jr',
		'name_two': 'john decarlo', 
		'expected': True, 
		'description': 'john decarlo,jr comparison with article'
	},
    {
		'name_one': 'john decicco',
		'name_two': 'john decicco', 
		'expected': True, 
		'description': 'john decicco comparison with article'
	},
    {
		'name_one': 'john degroot,sr',
		'name_two': 'john degroot', 
		'expected': True, 
		'description': 'john degroot,sr comparison with article'
	},
    {
		'name_one': 'john delaney',
		'name_two': 'john delaney', 
		'expected': True, 
		'description': 'john delaney comparison with article'
	},
    {
		'name_one': 'john dempson',
		'name_two': 'john dempsher', 
		'expected': False, 
		'description': 'john dempson comparison with article'
	},
    {
		'name_one': 'john e bradley',
		'name_two': 'john lewis bradley', 
		'expected': False, 
		'description': 'john e bradley comparison with article'
	},
    {
		'name_one': 'john e dees',
		'name_two': 'john essary dees', 
		'expected': True, 
		'description': 'john e dees comparison with article'
	},
    {
		'name_one': 'john e lagerstrom',
		'name_two': 'john e. lagerstrom', 
		'expected': True, 
		'description': 'john e lagerstrom comparison with article'
	},
    {
		'name_one': 'john e larsh',
		'name_two': 'john edgar larsh', 
		'expected': True, 
		'description': 'john e larsh comparison with article'
	},
    {
		'name_one': 'john e lawson',
		'name_two': 'john e. lawson', 
		'expected': True, 
		'description': 'john e lawson comparison with article'
	},
    {
		'name_one': 'john e newman',
		'name_two': 'john von neumann', 
		'expected': True, 
		'description': 'john e newman comparison with article'
	},
    {
		'name_one': 'john e vance',
		'name_two': 'john e. vance', 
		'expected': True, 
		'description': 'john e vance comparison with article'
	},
    {
		'name_one': 'john f denton',
		'name_two': 'john fletcher denton', 
		'expected': True, 
		'description': 'john f denton comparison with article'
	},
    {
		'name_one': 'john f freeman',
		'name_two': 'john leiper freeman', 
		'expected': False, 
		'description': 'john f freeman comparison with article'
	},
    {
		'name_one': 'john f mcgary',
		'name_two': 'p. f. degara', 
		'expected': False, 
		'description': 'john f mcgary comparison with article'
	},
    {
		'name_one': 'john f van vleck',
		'name_two': 'john hasbrouck van vleck', 
		'expected': False, 
		'description': 'john f van vleck comparison with article'
	},
    {
		'name_one': 'john f vanalstyne',
		'name_two': 'john pruyn van alstyne', 
		'expected': False, 
		'description': 'john f vanalstyne comparison with article'
	},
    {
		'name_one': 'john f vane',
		'name_two': 'john robert vane', 
		'expected': False, 
		'description': 'john f vane comparison with article'
	},
    {
		'name_one': 'john g denker',
		'name_two': 'p. g. denker', 
		'expected': False, 
		'description': 'john g denker comparison with article'
	},
    {
		'name_one': 'john g lewis',
		'name_two': 'john gary lewis', 
		'expected': True, 
		'description': 'john g lewis comparison with article'
	},
    {
		'name_one': 'john g moseley',
		'name_two': 'john dean moseley', 
		'expected': False, 
		'description': 'john g moseley comparison with article'
	},
    {
		'name_one': 'john h dean',
		'name_two': 'john aurie dean', 
		'expected': False, 
		'description': 'john h dean comparison with article'
	},
    {
		'name_one': 'john h dent',
		'name_two': 'john henry dent', 
		'expected': True, 
		'description': 'john h dent comparison with article'
	},
    {
		'name_one': 'john h lampe',
		'name_two': 'john harold lampe', 
		'expected': True, 
		'description': 'john h lampe comparison with article'
	},
    {
		'name_one': 'john h lawrence',
		'name_two': 'john h. lawrence', 
		'expected': True, 
		'description': 'john h lawrence comparison with article'
	},
    {
		'name_one': 'john h leek',
		'name_two': 'john halvor leek', 
		'expected': True, 
		'description': 'john h leek comparison with article'
	},
    {
		'name_one': 'john h marks',
		'name_two': 'john h. vandermark', 
		'expected': True, 
		'description': 'john h marks comparison with article'
	},
    {
		'name_one': 'john h vondell',
		'name_two': 'john henry vondell', 
		'expected': True, 
		'description': 'john h vondell comparison with article'
	},
    {
		'name_one': 'john h west',
		'name_two': 'john leslie west', 
		'expected': False, 
		'description': 'john h west comparison with article'
	},
    {
		'name_one': 'john hartley',
		'name_two': 'john leslie artley', 
		'expected': True, 
		'description': 'john hartley comparison with article'
	},
    {
		'name_one': 'john j beck',
		'name_two': 'john dengler beck', 
		'expected': False, 
		'description': 'john j beck comparison with article'
	},
    {
		'name_one': 'john j deboer',
		'name_two': 'john j. de boer', 
		'expected': True, 
		'description': 'john j deboer comparison with article'
	},
    {
		'name_one': 'john j havens',
		'name_two': 'jacobus alexander van heuven', 
		'expected': False, 
		'description': 'john j havens comparison with article'
	},
    {
		'name_one': 'john j laffey',
		'name_two': 'archille j. lafferiere', 
		'expected': False, 
		'description': 'john j laffey comparison with article'
	},
    {
		'name_one': 'john j lang',
		'name_two': 'john j. lang', 
		'expected': True, 
		'description': 'john j lang comparison with article'
	},
    {
		'name_one': 'john j lawless',
		'name_two': 'john joseph lawless', 
		'expected': True, 
		'description': 'john j lawless comparison with article'
	},
    {
		'name_one': 'john j le sage',
		'name_two': 'john lesage', 
		'expected': True, 
		'description': 'john j le sage comparison with article'
	},
    {
		'name_one': 'john j lee',
		'name_two': 'john j. lee', 
		'expected': True, 
		'description': 'john j lee comparison with article'
	},
    {
		'name_one': 'john j vannostrand',
		'name_two': 'john j. van nostrand', 
		'expected': True, 
		'description': 'john j vannostrand comparison with article'
	},
    {
		'name_one': 'john johnson',
		'name_two': 'john lars johnson', 
		'expected': True, 
		'description': 'john johnson comparison with article'
	},
    {
		'name_one': 'john k. dr lattimer, dr',
		'name_two': 'john k. lattimer', 
		'expected': True, 
		'description': 'john k. dr lattimer, dr comparison with article'
	},
    {
		'name_one': 'john l adams, jr',
		'name_two': 'john lester adams', 
		'expected': True, 
		'description': 'john l adams, jr comparison with article'
	},
    {
		'name_one': 'john l barnes',
		'name_two': 'john landes barnes', 
		'expected': True, 
		'description': 'john l barnes comparison with article'
	},
    {
		'name_one': 'john l brooks',
		'name_two': 'john langdon brooks', 
		'expected': True, 
		'description': 'john l brooks comparison with article'
	},
    {
		'name_one': 'john l champe',
		'name_two': 'john leland champe', 
		'expected': True, 
		'description': 'john l champe comparison with article'
	},
    {
		'name_one': 'john l conger',
		'name_two': 'john leonard conger', 
		'expected': True, 
		'description': 'john l conger comparison with article'
	},
    {
		'name_one': 'john l davies',
		'name_two': 'john leonard davies', 
		'expected': True, 
		'description': 'john l davies comparison with article'
	},
    {
		'name_one': 'john l doll',
		'name_two': 'john lee doll', 
		'expected': True, 
		'description': 'john l doll comparison with article'
	},
    {
		'name_one': 'john l evers',
		'name_two': 'john lawrence evers', 
		'expected': True, 
		'description': 'john l evers comparison with article'
	},
    {
		'name_one': 'john l gerig',
		'name_two': 'john lawrence gerig', 
		'expected': True, 
		'description': 'john l gerig comparison with article'
	},
    {
		'name_one': 'john l gillin',
		'name_two': 'john lewis gillin', 
		'expected': True, 
		'description': 'john l gillin comparison with article'
	},
    {
		'name_one': 'john l kelley',
		'name_two': 'john leroy kelley', 
		'expected': True, 
		'description': 'john l kelley comparison with article'
	},
    {
		'name_one': 'john l landgraf',
		'name_two': 'john leslie landgraf', 
		'expected': True, 
		'description': 'john l landgraf comparison with article'
	},
    {
		'name_one': 'john l leedy',
		'name_two': 'john lang leedy', 
		'expected': True, 
		'description': 'john l leedy comparison with article'
	},
    {
		'name_one': 'john l lievsay',
		'name_two': 'john leon lievsay', 
		'expected': True, 
		'description': 'john l lievsay comparison with article'
	},
    {
		'name_one': 'john l mothershead, sr',
		'name_two': 'john leland mothershead', 
		'expected': True, 
		'description': 'john l mothershead, sr comparison with article'
	},
    {
		'name_one': 'john l oncley',
		'name_two': 'john lawrence oncley', 
		'expected': True, 
		'description': 'john l oncley comparison with article'
	},
    {
		'name_one': 'john l plyler',
		'name_two': 'john laney plyler', 
		'expected': True, 
		'description': 'john l plyler comparison with article'
	},
    {
		'name_one': 'john l powell',
		'name_two': 'john leonard powell', 
		'expected': True, 
		'description': 'john l powell comparison with article'
	},
    {
		'name_one': 'john l reichert',
		'name_two': 'john lester reichert', 
		'expected': True, 
		'description': 'john l reichert comparison with article'
	},
    {
		'name_one': 'john l swigert, jr',
		'name_two': 'john leonard swigert', 
		'expected': True, 
		'description': 'john l swigert, jr comparison with article'
	},
    {
		'name_one': 'john l yost',
		'name_two': 'john lewis yost', 
		'expected': True, 
		'description': 'john l yost comparison with article'
	},
    {
		'name_one': 'john lamb, jr',
		'name_two': 'john lamb', 
		'expected': True, 
		'description': 'john lamb, jr comparison with article'
	},
    {
		'name_one': 'john lamb',
		'name_two': 'john henderson lamb', 
		'expected': True, 
		'description': 'john lamb comparison with article'
	},
    {
		'name_one': 'john lambert',
		'name_two': 'john ralph lambert', 
		'expected': True, 
		'description': 'john lambert comparison with article'
	},
    {
		'name_one': 'john leaser',
		'name_two': 'hans lisser', 
		'expected': True, 
		'description': 'john leaser comparison with article'
	},
    {
		'name_one': 'john lee brooks',
		'name_two': 'john lee brooks', 
		'expected': True, 
		'description': 'john lee brooks comparison with article'
	},
    {
		'name_one': 'john leibenderfer',
		'name_two': 'john edward leibenderfer', 
		'expected': True, 
		'description': 'john leibenderfer comparison with article'
	},
    {
		'name_one': 'john lester',
		'name_two': 'john l. lester', 
		'expected': True, 
		'description': 'john lester comparison with article'
	},
    {
		'name_one': 'john lewis',
		'name_two': 'john donald lewis', 
		'expected': True, 
		'description': 'john lewis comparison with article'
	},
    {
		'name_one': 'john lydon',
		'name_two': 'hans victor von leden', 
		'expected': True, 
		'description': 'john lydon comparison with article'
	},
    {
		'name_one': 'john m dennis',
		'name_two': 'john murray dennis', 
		'expected': True, 
		'description': 'john m dennis comparison with article'
	},
    {
		'name_one': 'john m lee',
		'name_two': 'john m. lee', 
		'expected': True, 
		'description': 'john m lee comparison with article'
	},
    {
		'name_one': 'john m lent',
		'name_two': 'john w. lenz', 
		'expected': False, 
		'description': 'john m lent comparison with article'
	},
    {
		'name_one': 'john m leslie',
		'name_two': 'john kenneth leslie', 
		'expected': False, 
		'description': 'john m leslie comparison with article'
	},
    {
		'name_one': 'john m lewis',
		'name_two': 'john m. lewis', 
		'expected': True, 
		'description': 'john m lewis comparison with article'
	},
    {
		'name_one': 'john n stewart',
		'name_two': 'john laurence stewart', 
		'expected': False, 
		'description': 'john n stewart comparison with article'
	},
    {
		'name_one': 'john o wood',
		'name_two': 'john lewis wood', 
		'expected': False, 
		'description': 'john o wood comparison with article'
	},
    {
		'name_one': 'john p lahey',
		'name_two': 'john p. lahey', 
		'expected': True, 
		'description': 'john p lahey comparison with article'
	},
    {
		'name_one': 'john p leagans, jr',
		'name_two': 'john paul leagans', 
		'expected': True, 
		'description': 'john p leagans, jr comparison with article'
	},
    {
		'name_one': 'john p leary',
		'name_two': 'john coleman leary', 
		'expected': False, 
		'description': 'john p leary comparison with article'
	},
    {
		'name_one': 'john p leonard',
		'name_two': 'john charles leonard', 
		'expected': False, 
		'description': 'john p leonard comparison with article'
	},
    {
		'name_one': 'john r laughnan',
		'name_two': 'john r. laughnan', 
		'expected': True, 
		'description': 'john r laughnan comparison with article'
	},
    {
		'name_one': 'john r lewis',
		'name_two': 'john prior lewis', 
		'expected': False, 
		'description': 'john r lewis comparison with article'
	},
    {
		'name_one': 'john r van de water',
		'name_two': 'john r. van de water', 
		'expected': True, 
		'description': 'john r van de water comparison with article'
	},
    {
		'name_one': 'john r vonrohr',
		'name_two': 'john robert von rohr', 
		'expected': True, 
		'description': 'john r vonrohr comparison with article'
	},
    {
		'name_one': 'john s lawrence',
		'name_two': 'john s. lawrence', 
		'expected': True, 
		'description': 'john s lawrence comparison with article'
	},
    {
		'name_one': 'john s lazzaro',
		'name_two': 'john h. lazzari', 
		'expected': False, 
		'description': 'john s lazzaro comparison with article'
	},
    {
		'name_one': 'john s leister',
		'name_two': 'john s. leister', 
		'expected': True, 
		'description': 'john s leister comparison with article'
	},
    {
		'name_one': 'john sims',
		'name_two': 'john leroy sims', 
		'expected': True, 
		'description': 'john sims comparison with article'
	},
    {
		'name_one': 'john t atwater',
		'name_two': 'thomas van valkenburgh atwater', 
		'expected': False, 
		'description': 'john t atwater comparison with article'
	},
    {
		'name_one': 'john t lanning',
		'name_two': 'john tate lanning', 
		'expected': True, 
		'description': 'john t lanning comparison with article'
	},
    {
		'name_one': 'john t lewis',
		'name_two': 'john lewis', 
		'expected': True, 
		'description': 'john t lewis comparison with article'
	},
    {
		'name_one': 'john von s maeck',
		'name_two': 'john van sicklen maeck', 
		'expected': True, 
		'description': 'john von s maeck comparison with article'
	},
    {
		'name_one': 'john w castles',
		'name_two': 'john laurence casteel', 
		'expected': False, 
		'description': 'john w castles comparison with article'
	},
    {
		'name_one': 'john w de mand,iii',
		'name_two': 'john wesley demand', 
		'expected': True, 
		'description': 'john w de mand,iii comparison with article'
	},
    {
		'name_one': 'john w dewire',
		'name_two': 'john w. dewire', 
		'expected': True, 
		'description': 'john w dewire comparison with article'
	},
    {
		'name_one': 'john w lacey',
		'name_two': 'forrest w. lacey', 
		'expected': False, 
		'description': 'john w lacey comparison with article'
	},
    {
		'name_one': 'john w lagrone',
		'name_two': 'j. w. lagrone', 
		'expected': True, 
		'description': 'john w lagrone comparison with article'
	},
    {
		'name_one': 'john w lawrence',
		'name_two': 'john william lawrence', 
		'expected': True, 
		'description': 'john w lawrence comparison with article'
	},
    {
		'name_one': 'john w lederle',
		'name_two': 'john w. lederle', 
		'expected': True, 
		'description': 'john w lederle comparison with article'
	},
    {
		'name_one': 'john w lewis',
		'name_two': 'john kent lewis', 
		'expected': False, 
		'description': 'john w lewis comparison with article'
	},
    {
		'name_one': 'john w lewis',
		'name_two': 'john w. lewis', 
		'expected': True, 
		'description': 'john w lewis comparison with article'
	},
    {
		'name_one': 'john wilt',
		'name_two': 'john w. vanderwilt', 
		'expected': True, 
		'description': 'john wilt comparison with article'
	},
    {
		'name_one': 'jordan l larson',
		'name_two': 'jordan louis larson', 
		'expected': True, 
		'description': 'jordan l larson comparison with article'
	},
    {
		'name_one': 'jose leal martel',
		'name_two': 'jose martel', 
		'expected': True, 
		'description': 'jose leal martel comparison with article'
	},
    {
		'name_one': 'jose onis',
		'name_two': 'jose de onis', 
		'expected': True, 
		'description': 'jose onis comparison with article'
	},
    {
		'name_one': 'joseh l waling',
		'name_two': 'joseph lee waling', 
		'expected': True, 
		'description': 'joseh l waling comparison with article'
	},
    {
		'name_one': 'joseh waling',
		'name_two': 'joseph lee waling', 
		'expected': True, 
		'description': 'joseh waling comparison with article'
	},
    {
		'name_one': 'joseph a leeder',
		'name_two': 'joseph a. leeder', 
		'expected': True, 
		'description': 'joseph a leeder comparison with article'
	},
    {
		'name_one': 'joseph a porter',
		'name_two': 'joseph a. del porto', 
		'expected': True, 
		'description': 'joseph a porter comparison with article'
	},
    {
		'name_one': 'joseph a vonbradish',
		'name_two': 'joseph a. von bradish', 
		'expected': True, 
		'description': 'joseph a vonbradish comparison with article'
	},
    {
		'name_one': 'joseph alfred aurele la rocque',
		'name_two': 'aurele larocque', 
		'expected': True, 
		'description': 'joseph alfred aurele la rocque comparison with article'
	},
    {
		'name_one': 'joseph b vander veer',
		'name_two': 'joseph b. vander veer', 
		'expected': True, 
		'description': 'joseph b vander veer comparison with article'
	},
    {
		'name_one': 'joseph b. leeper',
		'name_two': 'joseph b. leeper', 
		'expected': True, 
		'description': 'joseph b. leeper comparison with article'
	},
    {
		'name_one': 'joseph cleveland',
		'name_two': 'joseph lee cleveland', 
		'expected': True, 
		'description': 'joseph cleveland comparison with article'
	},
    {
		'name_one': 'joseph d clark',
		'name_two': 'joseph deadrick clark', 
		'expected': True, 
		'description': 'joseph d clark comparison with article'
	},
    {
		'name_one': 'joseph d everingham',
		'name_two': 'joseph dee everingham', 
		'expected': True, 
		'description': 'joseph d everingham comparison with article'
	},
    {
		'name_one': 'joseph davidson',
		'name_two': 'joseph leroy davidson', 
		'expected': True, 
		'description': 'joseph davidson comparison with article'
	},
    {
		'name_one': 'joseph de lauro',
		'name_two': 'joseph nicola delauro', 
		'expected': True, 
		'description': 'joseph de lauro comparison with article'
	},
    {
		'name_one': 'joseph e decamp',
		'name_two': 'joseph e. decamp', 
		'expected': True, 
		'description': 'joseph e decamp comparison with article'
	},
    {
		'name_one': 'joseph e delmonico',
		'name_two': 'e. joseph delmonico', 
		'expected': True, 
		'description': 'joseph e delmonico comparison with article'
	},
    {
		'name_one': 'joseph e devine',
		'name_two': 'joseph e. devine', 
		'expected': True, 
		'description': 'joseph e devine comparison with article'
	},
    {
		'name_one': 'joseph e viola',
		'name_two': 'forrest emanuel la violette', 
		'expected': False, 
		'description': 'joseph e viola comparison with article'
	},
    {
		'name_one': 'joseph f de luise',
		'name_two': 'frank joseph deluise', 
		'expected': True, 
		'description': 'joseph f de luise comparison with article'
	},
    {
		'name_one': 'joseph f de simone',
		'name_two': 'joseph f. desimone', 
		'expected': True, 
		'description': 'joseph f de simone comparison with article'
	},
    {
		'name_one': 'joseph g lalich',
		'name_two': 'joseph john lalich', 
		'expected': False, 
		'description': 'joseph g lalich comparison with article'
	},
    {
		'name_one': 'joseph g leeder',
		'name_two': 'joseph g. leeder', 
		'expected': True, 
		'description': 'joseph g leeder comparison with article'
	},
    {
		'name_one': 'joseph henry levi',
		'name_two': 'joseph levi', 
		'expected': True, 
		'description': 'joseph henry levi comparison with article'
	},
    {
		'name_one': 'joseph j leonard',
		'name_two': 'nelson jordan leonard', 
		'expected': False, 
		'description': 'joseph j leonard comparison with article'
	},
    {
		'name_one': 'joseph j picard',
		'name_two': 'joseph leroy picard', 
		'expected': False, 
		'description': 'joseph j picard comparison with article'
	},
    {
		'name_one': 'joseph l lennon',
		'name_two': 'joseph l. lennon', 
		'expected': True, 
		'description': 'joseph l lennon comparison with article'
	},
    {
		'name_one': 'joseph l lilienthal',
		'name_two': 'joseph leo lilienthal', 
		'expected': True, 
		'description': 'joseph l lilienthal comparison with article'
	},
    {
		'name_one': 'joseph l mc donald',
		'name_two': 'joseph lee mcdonald', 
		'expected': True, 
		'description': 'joseph l mc donald comparison with article'
	},
    {
		'name_one': 'joseph l midditon',
		'name_two': 'joseph leonard middleton', 
		'expected': True, 
		'description': 'joseph l midditon comparison with article'
	},
    {
		'name_one': 'joseph l rosenholtz',
		'name_two': 'joseph leon rosenholtz', 
		'expected': True, 
		'description': 'joseph l rosenholtz comparison with article'
	},
    {
		'name_one': 'joseph l sullivan',
		'name_two': 'joseph lewis sullivan', 
		'expected': True, 
		'description': 'joseph l sullivan comparison with article'
	},
    {
		'name_one': 'joseph l walsh',
		'name_two': 'joseph leonard walsh', 
		'expected': True, 
		'description': 'joseph l walsh comparison with article'
	},
    {
		'name_one': 'joseph landin',
		'name_two': 'joseph landin', 
		'expected': True, 
		'description': 'joseph landin comparison with article'
	},
    {
		'name_one': 'joseph latimer',
		'name_two': 'joseph marion latimer', 
		'expected': True, 
		'description': 'joseph latimer comparison with article'
	},
    {
		'name_one': 'joseph layton',
		'name_two': 'joseph alexander leighton', 
		'expected': True, 
		'description': 'joseph layton comparison with article'
	},
    {
		'name_one': 'joseph le blanc',
		'name_two': 'joseph le blanc', 
		'expected': True, 
		'description': 'joseph le blanc comparison with article'
	},
    {
		'name_one': 'joseph leavitt',
		'name_two': 'joseph m. leavitt', 
		'expected': True, 
		'description': 'joseph leavitt comparison with article'
	},
    {
		'name_one': 'joseph lennon',
		'name_two': 'joseph lennon', 
		'expected': True, 
		'description': 'joseph lennon comparison with article'
	},
    {
		'name_one': 'joseph levenson',
		'name_two': 'joseph richmond levenson', 
		'expected': True, 
		'description': 'joseph levenson comparison with article'
	},
    {
		'name_one': 'joseph melnick',
		'name_two': 'joseph lewis melnick', 
		'expected': True, 
		'description': 'joseph melnick comparison with article'
	},
    {
		'name_one': 'joseph p la master',
		'name_two': 'j. p. lamaster', 
		'expected': True, 
		'description': 'joseph p la master comparison with article'
	},
    {
		'name_one': 'joseph p lahan',
		'name_two': 'willard p. vanderlaan', 
		'expected': False, 
		'description': 'joseph p lahan comparison with article'
	},
    {
		'name_one': 'joseph p larocca',
		'name_two': 'j. p. la rocca', 
		'expected': True, 
		'description': 'joseph p larocca comparison with article'
	},
    {
		'name_one': 'joseph p mccarthy',
		'name_two': 'joseph le page mccarthy', 
		'expected': True, 
		'description': 'joseph p mccarthy comparison with article'
	},
    {
		'name_one': 'joseph p slatkavitz',
		'name_two': 'phillip leonard sirotkin', 
		'expected': False, 
		'description': 'joseph p slatkavitz comparison with article'
	},
    {
		'name_one': 'joseph t law',
		'name_two': 'joseph t. law', 
		'expected': True, 
		'description': 'joseph t law comparison with article'
	},
    {
		'name_one': 'joseph v mckelvey',
		'name_two': 'joseph vance mckelvey', 
		'expected': True, 
		'description': 'joseph v mckelvey comparison with article'
	},
    {
		'name_one': 'joshua lederberg',
		'name_two': 'joshua lederberg', 
		'expected': True, 
		'description': 'joshua lederberg comparison with article'
	},
    {
		'name_one': 'jovian lang',
		'name_two': 'jovian lang', 
		'expected': True, 
		'description': 'jovian lang comparison with article'
	},
    {
		'name_one': 'judee d paulson',
		'name_two': 'jehu dewitt paulson', 
		'expected': False, 
		'description': 'judee d paulson comparison with article'
	},
    {
		'name_one': 'jules last,dr',
		'name_two': 'jules h. last', 
		'expected': True, 
		'description': 'jules last,dr comparison with article'
	},
    {
		'name_one': 'julia g leach',
		'name_two': 'julian gilbert leach', 
		'expected': True, 
		'description': 'julia g leach comparison with article'
	},
    {
		'name_one': 'julian h degray',
		'name_two': 'julian h. degray', 
		'expected': True, 
		'description': 'julian h degray comparison with article'
	},
    {
		'name_one': 'julian l ross',
		'name_two': 'julian lenhart ross', 
		'expected': True, 
		'description': 'julian l ross comparison with article'
	},
    {
		'name_one': 'julian p barksdale',
		'name_two': 'julian devreau barksdale', 
		'expected': False, 
		'description': 'julian p barksdale comparison with article'
	},
    {
		'name_one': 'julie lee hawkins',
		'name_two': 'julia lee hawkins', 
		'expected': True, 
		'description': 'julie lee hawkins comparison with article'
	},
    {
		'name_one': 'julie r labarthe',
		'name_two': 'luther r. barth', 
		'expected': False, 
		'description': 'julie r labarthe comparison with article'
	},
    {
		'name_one': 'juliette c devin',
		'name_two': 'juliette c. devin', 
		'expected': True, 
		'description': 'juliette c devin comparison with article'
	},
    {
		'name_one': 'julius a larsen',
		'name_two': 'julius ansgar larsen', 
		'expected': True, 
		'description': 'julius a larsen comparison with article'
	},
    {
		'name_one': 'june e lewis',
		'name_two': 'june e. lewis', 
		'expected': True, 
		'description': 'june e lewis comparison with article'
	},
    {
		'name_one': 'junius larsen',
		'name_two': 'junius larsen', 
		'expected': True, 
		'description': 'junius larsen comparison with article'
	},
    {
		'name_one': 'k detkingenn',
		'name_two': 'katherine b. cettinger', 
		'expected': False, 
		'description': 'k detkingenn comparison with article'
	},
    {
		'name_one': 'karl e leib',
		'name_two': 'karl elias leib', 
		'expected': True, 
		'description': 'karl e leib comparison with article'
	},
    {
		'name_one': 'karl g larson',
		'name_two': 'karl gottfrid larson', 
		'expected': True, 
		'description': 'karl g larson comparison with article'
	},
    {
		'name_one': 'karl lark horowitz',
		'name_two': 'karl lark-horovitz', 
		'expected': True, 
		'description': 'karl lark horowitz comparison with article'
	},
    {
		'name_one': 'karl lehmann',
		'name_two': 'karl lehmann', 
		'expected': True, 
		'description': 'karl lehmann comparison with article'
	},
    {
		'name_one': 'karl o lange',
		'name_two': 'karl otto lange', 
		'expected': True, 
		'description': 'karl o lange comparison with article'
	},
    {
		'name_one': 'karl s van dyke',
		'name_two': 'karl s. van dyke', 
		'expected': True, 
		'description': 'karl s van dyke comparison with article'
	},
    {
		'name_one': 'karl w deutseh',
		'name_two': 'karl w. deutsch', 
		'expected': True, 
		'description': 'karl w deutseh comparison with article'
	},
    {
		'name_one': 'karl w deutseh',
		'name_two': 'karl wolfgang deutsch', 
		'expected': True, 
		'description': 'karl w deutseh comparison with article'
	},
    {
		'name_one': 'karol j murtz',
		'name_two': 'carel w. van der merwe', 
		'expected': False, 
		'description': 'karol j murtz comparison with article'
	},
    {
		'name_one': 'katherine densford',
		'name_two': 'katharine j. densford', 
		'expected': True, 
		'description': 'katherine densford comparison with article'
	},
    {
		'name_one': 'katherine l vankeuren',
		'name_two': 'katherine van keuren', 
		'expected': True, 
		'description': 'katherine l vankeuren comparison with article'
	},
    {
		'name_one': 'katherine lever',
		'name_two': 'katherine lever', 
		'expected': True, 
		'description': 'katherine lever comparison with article'
	},
    {
		'name_one': 'katherine ley',
		'name_two': 'katherine l. ley', 
		'expected': True, 
		'description': 'katherine ley comparison with article'
	},
    {
		'name_one': 'kathleen m lavell',
		'name_two': 'kathleen macdonald lavell', 
		'expected': True, 
		'description': 'kathleen m lavell comparison with article'
	},
    {
		'name_one': 'keith l wilson',
		'name_two': 'keith leroy wilson', 
		'expected': True, 
		'description': 'keith l wilson comparison with article'
	},
    {
		'name_one': 'kenneth b de ome',
		'name_two': 'kenneth b. deome', 
		'expected': True, 
		'description': 'kenneth b de ome comparison with article'
	},
    {
		'name_one': 'kenneth d cashin',
		'name_two': 'kenneth delbert cashin', 
		'expected': True, 
		'description': 'kenneth d cashin comparison with article'
	},
    {
		'name_one': 'kenneth e lemmer',
		'name_two': 'kenneth elery lemmer', 
		'expected': True, 
		'description': 'kenneth e lemmer comparison with article'
	},
    {
		'name_one': 'kenneth k landes',
		'name_two': 'kenneth knight landes', 
		'expected': True, 
		'description': 'kenneth k landes comparison with article'
	},
    {
		'name_one': 'kenneth l mark',
		'name_two': 'kenneth lamartine mark', 
		'expected': True, 
		'description': 'kenneth l mark comparison with article'
	},
    {
		'name_one': 'kenneth l osterud',
		'name_two': 'kenneth leland osterud', 
		'expected': True, 
		'description': 'kenneth l osterud comparison with article'
	},
    {
		'name_one': 'kenneth l pichrell',
		'name_two': 'kenneth leroy pickrell', 
		'expected': True, 
		'description': 'kenneth l pichrell comparison with article'
	},
    {
		'name_one': 'kenneth l roper',
		'name_two': 'kenneth lawrence roper', 
		'expected': True, 
		'description': 'kenneth l roper comparison with article'
	},
    {
		'name_one': 'kenneth l turk',
		'name_two': 'kenneth leroy turk', 
		'expected': True, 
		'description': 'kenneth l turk comparison with article'
	},
    {
		'name_one': 'kenneth l waters',
		'name_two': 'kenneth lee waters', 
		'expected': True, 
		'description': 'kenneth l waters comparison with article'
	},
    {
		'name_one': 'kenneth l zierler',
		'name_two': 'kenneth levie zierler', 
		'expected': True, 
		'description': 'kenneth l zierler comparison with article'
	},
    {
		'name_one': 'kenneth larowe',
		'name_two': 'kenneth davis larowe', 
		'expected': True, 
		'description': 'kenneth larowe comparison with article'
	},
    {
		'name_one': 'kerl c leeburck',
		'name_two': 'karl c. leebrick', 
		'expected': True, 
		'description': 'kerl c leeburck comparison with article'
	},
    {
		'name_one': 'kerta r leng',
		'name_two': 'herta r. leng', 
		'expected': True, 
		'description': 'kerta r leng comparison with article'
	},
    {
		'name_one': 'key l barkley',
		'name_two': 'key lee barkley', 
		'expected': True, 
		'description': 'key l barkley comparison with article'
	},
    {
		'name_one': 'kirk athow',
		'name_two': 'kirk leland athow', 
		'expected': True, 
		'description': 'kirk athow comparison with article'
	},
    {
		'name_one': 'kurt lewent',
		'name_two': 'kurt lewent', 
		'expected': True, 
		'description': 'kurt lewent comparison with article'
	},
    {
		'name_one': 'kyrl l f degravelines',
		'name_two': 'kyrl leighton-faxford degravelines', 
		'expected': True, 
		'description': 'kyrl l f degravelines comparison with article'
	},
    {
		'name_one': 'l frederick richards',
		'name_two': 'frederick leet reichert', 
		'expected': True, 
		'description': 'l frederick richards comparison with article'
	},
    {
		'name_one': 'l jackson laslett',
		'name_two': 'l. jackson laslett', 
		'expected': True, 
		'description': 'l jackson laslett comparison with article'
	},
    {
		'name_one': 'l lawton gore',
		'name_two': 'l. lawton gore', 
		'expected': True, 
		'description': 'l lawton gore comparison with article'
	},
    {
		'name_one': 'l rhodes lewis',
		'name_two': 'l. rhodes lewis', 
		'expected': True, 
		'description': 'l rhodes lewis comparison with article'
	},
    {
		'name_one': 'l walter leach',
		'name_two': 'walter barton leach', 
		'expected': False, 
		'description': 'l walter leach comparison with article'
	},
    {
		'name_one': 'l wreal lott',
		'name_two': 'wreal lester lott', 
		'expected': True, 
		'description': 'l wreal lott comparison with article'
	},
    {
		'name_one': 'la vange richardson',
		'name_two': 'la vange richardson', 
		'expected': True, 
		'description': 'la vange richardson comparison with article'
	},
    {
		'name_one': 'ladema m langdon',
		'name_two': 'ladema mary langdon', 
		'expected': True, 
		'description': 'ladema m langdon comparison with article'
	},
    {
		'name_one': 'lamar johnson',
		'name_two': 'b. lamar johnson', 
		'expected': True, 
		'description': 'lamar johnson comparison with article'
	},
    {
		'name_one': 'landis a romineck',
		'name_two': 'aaron lemonick', 
		'expected': False, 
		'description': 'landis a romineck comparison with article'
	},
    {
		'name_one': 'landis l boyd',
		'name_two': 'landis lee boyd', 
		'expected': True, 
		'description': 'landis l boyd comparison with article'
	},
    {
		'name_one': 'laraine a lebo',
		'name_two': 'averill abraham liebow', 
		'expected': False, 
		'description': 'laraine a lebo comparison with article'
	},
    {
		'name_one': 'laura c lee',
		'name_two': 'laura canfield lee', 
		'expected': True, 
		'description': 'laura c lee comparison with article'
	},
    {
		'name_one': 'laurel j lewis',
		'name_two': 'laurel jones lewis', 
		'expected': True, 
		'description': 'laurel j lewis comparison with article'
	},
    {
		'name_one': 'laurence k hawkins',
		'name_two': 'richmond laurin hawkins', 
		'expected': False, 
		'description': 'laurence k hawkins comparison with article'
	},
    {
		'name_one': 'laurence l. howe',
		'name_two': 'laurence lee howe', 
		'expected': True, 
		'description': 'laurence l. howe comparison with article'
	},
    {
		'name_one': 'laurence montgomery',
		'name_two': 'm. laurence montgomery', 
		'expected': True, 
		'description': 'laurence montgomery comparison with article'
	},
    {
		'name_one': 'laurence w de muth, jr',
		'name_two': 'laurence w. demuth', 
		'expected': True, 
		'description': 'laurence w de muth, jr comparison with article'
	},
    {
		'name_one': 'lauvery l cauperthwaite',
		'name_two': 'l. leroy cowperthwaite', 
		'expected': True, 
		'description': 'lauvery l cauperthwaite comparison with article'
	},
    {
		'name_one': 'lavar bateman',
		'name_two': 'j. lavar bateman', 
		'expected': True, 
		'description': 'lavar bateman comparison with article'
	},
    {
		'name_one': 'lawrence a larrimer',
		'name_two': 'lawrence a. larrimer', 
		'expected': True, 
		'description': 'lawrence a larrimer comparison with article'
	},
    {
		'name_one': 'lawrence anderson',
		'name_two': 'leighton lars anderson', 
		'expected': False, 
		'description': 'lawrence anderson comparison with article'
	},
    {
		'name_one': 'lawrence b lee',
		'name_two': 'lawrence h. lee', 
		'expected': False, 
		'description': 'lawrence b lee comparison with article'
	},
    {
		'name_one': 'lawrence d lafore',
		'name_two': 'laurence d. lafore', 
		'expected': True, 
		'description': 'lawrence d lafore comparison with article'
	},
    {
		'name_one': 'lawrence d stewart',
		'name_two': 'lawrence delbert stewart', 
		'expected': True, 
		'description': 'lawrence d stewart comparison with article'
	},
    {
		'name_one': 'lawrence e lawson',
		'name_two': 'lawrence james lawson', 
		'expected': False, 
		'description': 'lawrence e lawson comparison with article'
	},
    {
		'name_one': 'lawrence e lee',
		'name_two': 'lawrence lee', 
		'expected': True, 
		'description': 'lawrence e lee comparison with article'
	},
    {
		'name_one': 'lawrence key',
		'name_two': 'e. lawrence keyes', 
		'expected': True, 
		'description': 'lawrence key comparison with article'
	},
    {
		'name_one': 'lawrence l rauch',
		'name_two': 'lawrence lee rauch', 
		'expected': True, 
		'description': 'lawrence l rauch comparison with article'
	},
    {
		'name_one': 'lawrence l robbins',
		'name_two': 'laurence lamson robbins', 
		'expected': True, 
		'description': 'lawrence l robbins comparison with article'
	},
    {
		'name_one': 'lawrence l vance',
		'name_two': 'lawrence l. vance', 
		'expected': True, 
		'description': 'lawrence l vance comparison with article'
	},
    {
		'name_one': 'lawrence l waters',
		'name_two': 'lawrence leslie waters', 
		'expected': True, 
		'description': 'lawrence l waters comparison with article'
	},
    {
		'name_one': 'lawrence labree',
		'name_two': 'lawrence winthrop labree', 
		'expected': True, 
		'description': 'lawrence labree comparison with article'
	},
    {
		'name_one': 'lawrence larson',
		'name_two': 'lawrence c. larson', 
		'expected': True, 
		'description': 'lawrence larson comparison with article'
	},
    {
		'name_one': 'lawrence t lawrey',
		'name_two': 'lawrence t. lowrey', 
		'expected': True, 
		'description': 'lawrence t lawrey comparison with article'
	},
    {
		'name_one': 'lawrence w van meir',
		'name_two': 'lawrence w. van mier', 
		'expected': True, 
		'description': 'lawrence w van meir comparison with article'
	},
    {
		'name_one': 'leander j van hecke',
		'name_two': 'leander j. van hecke', 
		'expected': True, 
		'description': 'leander j van hecke comparison with article'
	},
    {
		'name_one': 'leatha j lee',
		'name_two': 'j g lee', 
		'expected': False, 
		'description': 'leatha j lee comparison with article'
	},
    {
		'name_one': 'lee a parker',
		'name_two': 'ethel lee parker', 
		'expected': False, 
		'description': 'lee a parker comparison with article'
	},
    {
		'name_one': 'lee block',
		'name_two': 'virglnia lee block', 
		'expected': True, 
		'description': 'lee block comparison with article'
	},
    {
		'name_one': 'lee e bassett',
		'name_two': 'david lee bassett', 
		'expected': False, 
		'description': 'lee e bassett comparison with article'
	},
    {
		'name_one': 'lee e deets',
		'name_two': 'lee e. deets', 
		'expected': True, 
		'description': 'lee e deets comparison with article'
	},
    {
		'name_one': 'lee krause',
		'name_two': 'herbert lee krauss', 
		'expected': True, 
		'description': 'lee krause comparison with article'
	},
    {
		'name_one': 'lee m bender',
		'name_two': 'myron lee bender', 
		'expected': True, 
		'description': 'lee m bender comparison with article'
	},
    {
		'name_one': 'lee myers',
		'name_two': 'e. lee myers', 
		'expected': True, 
		'description': 'lee myers comparison with article'
	},
    {
		'name_one': 'lee nemir',
		'name_two': 'rosa lee nemir', 
		'expected': True, 
		'description': 'lee nemir comparison with article'
	},
    {
		'name_one': 'leighton rudolph',
		'name_two': 'earle leighton rudolph', 
		'expected': True, 
		'description': 'leighton rudolph comparison with article'
	},
    {
		'name_one': 'leita e lawrence',
		'name_two': 'odie e. lawrence', 
		'expected': False, 
		'description': 'leita e lawrence comparison with article'
	},
    {
		'name_one': 'leland c. lehman',
		'name_two': 'leland c. lehman', 
		'expected': True, 
		'description': 'leland c. lehman comparison with article'
	},
    {
		'name_one': 'leland j lewis',
		'name_two': 'leland judson lewis', 
		'expected': True, 
		'description': 'leland j lewis comparison with article'
	},
    {
		'name_one': 'leland l atwood',
		'name_two': 'leland leavitt atwood', 
		'expected': True, 
		'description': 'leland l atwood comparison with article'
	},
    {
		'name_one': 'leland l briggs',
		'name_two': 'leland lawrence briggs', 
		'expected': True, 
		'description': 'leland l briggs comparison with article'
	},
    {
		'name_one': 'lena may lauer',
		'name_two': 'eleanor lauer', 
		'expected': True, 
		'description': 'lena may lauer comparison with article'
	},
    {
		'name_one': 'lennart v larson',
		'name_two': 'lennart v. larson', 
		'expected': True, 
		'description': 'lennart v larson comparison with article'
	},
    {
		'name_one': 'leo a murphy',
		'name_two': 'rex leo murphy', 
		'expected': False, 
		'description': 'leo a murphy comparison with article'
	},
    {
		'name_one': 'leo b leach',
		'name_two': 'byron elwood leach', 
		'expected': False, 
		'description': 'leo b leach comparison with article'
	},
    {
		'name_one': 'leo b smith',
		'name_two': 'richard leo smith', 
		'expected': False, 
		'description': 'leo b smith comparison with article'
	},
    {
		'name_one': 'leo clair jones',
		'name_two': 'vincent leo jones', 
		'expected': False, 
		'description': 'leo clair jones comparison with article'
	},
    {
		'name_one': 'leo fooks',
		'name_two': 'iviary leo pita volk', 
		'expected': False, 
		'description': 'leo fooks comparison with article'
	},
    {
		'name_one': 'leo l beranek',
		'name_two': 'leo leroy beranek', 
		'expected': True, 
		'description': 'leo l beranek comparison with article'
	},
    {
		'name_one': 'leo l carrick',
		'name_two': 'leo lehr carrick', 
		'expected': True, 
		'description': 'leo l carrick comparison with article'
	},
    {
		'name_one': 'leo lehrman',
		'name_two': 'leo lehrman', 
		'expected': True, 
		'description': 'leo lehrman comparison with article'
	},
    {
		'name_one': 'leo lemke',
		'name_two': 'leo lemke', 
		'expected': True, 
		'description': 'leo lemke comparison with article'
	},
    {
		'name_one': 'leo m legatski',
		'name_two': 'leo max legatski', 
		'expected': True, 
		'description': 'leo m legatski comparison with article'
	},
    {
		'name_one': 'leo sosa',
		'name_two': 'leo p. delsasso', 
		'expected': False, 
		'description': 'leo sosa comparison with article'
	},
    {
		'name_one': 'leo sosa',
		'name_two': 'leo p. delsossa', 
		'expected': True, 
		'description': 'leo sosa comparison with article'
	},
    {
		'name_one': 'leo w leary',
		'name_two': 'leo w. leary', 
		'expected': True, 
		'description': 'leo w leary comparison with article'
	},
    {
		'name_one': 'leon a hitchcock',
		'name_two': 'charles leo hitchcock', 
		'expected': False, 
		'description': 'leon a hitchcock comparison with article'
	},
    {
		'name_one': 'leon allen',
		'name_two': 'durward leon allen', 
		'expected': True, 
		'description': 'leon allen comparison with article'
	},
    {
		'name_one': 'leon c van sickle',
		'name_two': 'clyde huntus van sickle', 
		'expected': False, 
		'description': 'leon c van sickle comparison with article'
	},
    {
		'name_one': 'leon gershbein',
		'name_two': 'leon lee gershbein', 
		'expected': True, 
		'description': 'leon gershbein comparison with article'
	},
    {
		'name_one': 'leon j leahy',
		'name_two': 'leon j. leahy', 
		'expected': True, 
		'description': 'leon j leahy comparison with article'
	},
    {
		'name_one': 'leon l iltis',
		'name_two': 'leon leonard iltis', 
		'expected': True, 
		'description': 'leon l iltis comparison with article'
	},
    {
		'name_one': 'leon l stephan',
		'name_two': 'leon lemar stephan', 
		'expected': True, 
		'description': 'leon l stephan comparison with article'
	},
    {
		'name_one': 'leon lassers',
		'name_two': 'leon lassers', 
		'expected': True, 
		'description': 'leon lassers comparison with article'
	},
    {
		'name_one': 'leon singer',
		'name_two': 'ferdinand leon singer', 
		'expected': True, 
		'description': 'leon singer comparison with article'
	},
    {
		'name_one': 'leon w chaffee',
		'name_two': 'emory leon chaffee', 
		'expected': False, 
		'description': 'leon w chaffee comparison with article'
	},
    {
		'name_one': 'leon w dean',
		'name_two': 'leon w. dean', 
		'expected': True, 
		'description': 'leon w dean comparison with article'
	},
    {
		'name_one': 'leonard a lecht',
		'name_two': 'leonard a. lecht', 
		'expected': True, 
		'description': 'leonard a lecht comparison with article'
	},
    {
		'name_one': 'leonard d lee',
		'name_two': 'herbert leonard lee', 
		'expected': False, 
		'description': 'leonard d lee comparison with article'
	},
    {
		'name_one': 'leonard demorelos',
		'name_two': 'leonardo c. de morelos', 
		'expected': True, 
		'description': 'leonard demorelos comparison with article'
	},
    {
		'name_one': 'leonard f lewis',
		'name_two': 't. leonard lewis', 
		'expected': False, 
		'description': 'leonard f lewis comparison with article'
	},
    {
		'name_one': 'leonard g ryerson',
		'name_two': 'dwight leonard ryerson', 
		'expected': False, 
		'description': 'leonard g ryerson comparison with article'
	},
    {
		'name_one': 'leonard j deysach',
		'name_two': 'leonard j. deysach', 
		'expected': True, 
		'description': 'leonard j deysach comparison with article'
	},
    {
		'name_one': 'leonard leone',
		'name_two': 'leonard leone', 
		'expected': True, 
		'description': 'leonard leone comparison with article'
	},
    {
		'name_one': 'leonard levy',
		'name_two': 'leonard w. levy', 
		'expected': True, 
		'description': 'leonard levy comparison with article'
	},
    {
		'name_one': 'leonard light',
		'name_two': 'leonard leight', 
		'expected': True, 
		'description': 'leonard light comparison with article'
	},
    {
		'name_one': 'leonard marino',
		'name_two': 'leonardo santamarina', 
		'expected': True, 
		'description': 'leonard marino comparison with article'
	},
    {
		'name_one': 'leonard w laboree',
		'name_two': 'leonard woods labaree', 
		'expected': True, 
		'description': 'leonard w laboree comparison with article'
	},
    {
		'name_one': 'leroy a anderson',
		'name_two': 'stuart leroy anderson', 
		'expected': False, 
		'description': 'leroy a anderson comparison with article'
	},
    {
		'name_one': 'leroy a swanson',
		'name_two': 'adrian leroy swanson', 
		'expected': True, 
		'description': 'leroy a swanson comparison with article'
	},
    {
		'name_one': 'leroy e detling',
		'name_two': 'leroy e. detling', 
		'expected': True, 
		'description': 'leroy e detling comparison with article'
	},
    {
		'name_one': 'leroy johnson',
		'name_two': 'alfred leroy johnson', 
		'expected': True, 
		'description': 'leroy johnson comparison with article'
	},
    {
		'name_one': 'leroy koenig',
		'name_two': 'virgil leroy koenig', 
		'expected': True, 
		'description': 'leroy koenig comparison with article'
	},
    {
		'name_one': 'leroy l barnes',
		'name_two': 'leroy lesher barnes', 
		'expected': True, 
		'description': 'leroy l barnes comparison with article'
	},
    {
		'name_one': 'leroy t laase',
		'name_two': 'leeroy laase', 
		'expected': True, 
		'description': 'leroy t laase comparison with article'
	},
    {
		'name_one': 'leslie bullock',
		'name_two': 'philip leslie bullock', 
		'expected': True, 
		'description': 'leslie bullock comparison with article'
	},
    {
		'name_one': 'leslie f morrison',
		'name_two': 'paul leslie morrison', 
		'expected': False, 
		'description': 'leslie f morrison comparison with article'
	},
    {
		'name_one': 'leslie h layman',
		'name_two': 'leslie h. layman', 
		'expected': True, 
		'description': 'leslie h layman comparison with article'
	},
    {
		'name_one': 'leslie lisle lewis',
		'name_two': 'leslie l. lewis', 
		'expected': True, 
		'description': 'leslie lisle lewis comparison with article'
	},
    {
		'name_one': 'lester creaser',
		'name_two': 'william lester kraushaar', 
		'expected': True, 
		'description': 'lester creaser comparison with article'
	},
    {
		'name_one': 'lester j hayman',
		'name_two': 'joseph lester hayman', 
		'expected': True, 
		'description': 'lester j hayman comparison with article'
	},
    {
		'name_one': 'lester lee',
		'name_two': 'lester lees', 
		'expected': True, 
		'description': 'lester lee comparison with article'
	},
    {
		'name_one': 'lester s henderson',
		'name_two': 'j. lester henderson', 
		'expected': False, 
		'description': 'lester s henderson comparison with article'
	},
    {
		'name_one': 'lester w allen',
		'name_two': 'a. lester allen', 
		'expected': False, 
		'description': 'lester w allen comparison with article'
	},
    {
		'name_one': 'leston l love',
		'name_two': 'leston lewis love', 
		'expected': True, 
		'description': 'leston l love comparison with article'
	},
    {
		'name_one': 'levi dees',
		'name_two': 'levi o. dees', 
		'expected': True, 
		'description': 'levi dees comparison with article'
	},
    {
		'name_one': 'lewis l clegg',
		'name_two': 'lewis lamar clegg', 
		'expected': True, 
		'description': 'lewis l clegg comparison with article'
	},
    {
		'name_one': 'lewis larkin',
		'name_two': 'lewis b. larkin', 
		'expected': True, 
		'description': 'lewis larkin comparison with article'
	},
    {
		'name_one': 'lewis m foster',
		'name_two': 'eugene lewis foster', 
		'expected': False, 
		'description': 'lewis m foster comparison with article'
	},
    {
		'name_one': 'lewis peterson',
		'name_two': 'edwin lewis peterson', 
		'expected': True, 
		'description': 'lewis peterson comparison with article'
	},
    {
		'name_one': 'lillian c lambert',
		'name_two': 'c. n. lambert', 
		'expected': False, 
		'description': 'lillian c lambert comparison with article'
	},
    {
		'name_one': 'lillian h lanover',
		'name_two': 'hrwin wladaver', 
		'expected': False, 
		'description': 'lillian h lanover comparison with article'
	},
    {
		'name_one': 'lillian lawler',
		'name_two': 'lillian b. lawler', 
		'expected': True, 
		'description': 'lillian lawler comparison with article'
	},
    {
		'name_one': 'lillian lee vaughan',
		'name_two': 'lillian lee vaughan', 
		'expected': True, 
		'description': 'lillian lee vaughan comparison with article'
	},
    {
		'name_one': 'lincoln lapaz',
		'name_two': 'lincoln lapaz', 
		'expected': True, 
		'description': 'lincoln lapaz comparison with article'
	},
    {
		'name_one': 'linnal robinson',
		'name_two': 'selby lemley robinson', 
		'expected': False, 
		'description': 'linnal robinson comparison with article'
	},
    {
		'name_one': 'linnea c dennett',
		'name_two': 'linnea c. dennett', 
		'expected': True, 
		'description': 'linnea c dennett comparison with article'
	},
    {
		'name_one': 'lizbeth laughton',
		'name_two': 'lizbeth r. laughton', 
		'expected': True, 
		'description': 'lizbeth laughton comparison with article'
	},
    {
		'name_one': 'llewellyn l derby',
		'name_two': 'llewellyn light derby', 
		'expected': True, 
		'description': 'llewellyn l derby comparison with article'
	},
    {
		'name_one': 'lloyd a betuno',
		'name_two': 'andre j. de bethune', 
		'expected': False, 
		'description': 'lloyd a betuno comparison with article'
	},
    {
		'name_one': 'lloyd o burge',
		'name_two': 'lloyd van de berg', 
		'expected': True, 
		'description': 'lloyd o burge comparison with article'
	},
    {
		'name_one': 'lois lebar',
		'name_two': 'lois e. lebar', 
		'expected': True, 
		'description': 'lois lebar comparison with article'
	},
    {
		'name_one': 'lois schnoor',
		'name_two': 'lois laverne schnoor', 
		'expected': True, 
		'description': 'lois schnoor comparison with article'
	},
    {
		'name_one': 'lolo robinson',
		'name_two': 'lolo lemme robinson', 
		'expected': True, 
		'description': 'lolo robinson comparison with article'
	},
    {
		'name_one': 'loras t lane',
		'name_two': 'loras t. lane', 
		'expected': True, 
		'description': 'loras t lane comparison with article'
	},
    {
		'name_one': 'loren j larsen',
		'name_two': 'loren j. larsen', 
		'expected': True, 
		'description': 'loren j larsen comparison with article'
	},
    {
		'name_one': 'lorin j lucius',
		'name_two': 'joseph j. delucia', 
		'expected': False, 
		'description': 'lorin j lucius comparison with article'
	},
    {
		'name_one': 'lorna de varon',
		'name_two': 'lorna cooke devaron', 
		'expected': True, 
		'description': 'lorna de varon comparison with article'
	},
    {
		'name_one': 'lorrent le sage',
		'name_two': 'laurent lesage', 
		'expected': True, 
		'description': 'lorrent le sage comparison with article'
	},
    {
		'name_one': 'louis a derose',
		'name_two': 'louis derose', 
		'expected': True, 
		'description': 'louis a derose comparison with article'
	},
    {
		'name_one': 'louis a landa',
		'name_two': 'louis a. landa', 
		'expected': True, 
		'description': 'louis a landa comparison with article'
	},
    {
		'name_one': 'louis a sr demonbreun',
		'name_two': 'w. a. demonbreun', 
		'expected': False, 
		'description': 'louis a sr demonbreun comparison with article'
	},
    {
		'name_one': 'louis d de vries',
		'name_two': 'louis devries', 
		'expected': True, 
		'description': 'louis d de vries comparison with article'
	},
    {
		'name_one': 'louis e derryberry',
		'name_two': 'louis e. derryberry', 
		'expected': True, 
		'description': 'louis e derryberry comparison with article'
	},
    {
		'name_one': 'louis e lambert',
		'name_two': 'louis erskine lambert', 
		'expected': True, 
		'description': 'louis e lambert comparison with article'
	},
    {
		'name_one': 'louis e. vandegrift',
		'name_two': 'louis e. vandergrift', 
		'expected': True, 
		'description': 'louis e. vandegrift comparison with article'
	},
    {
		'name_one': 'louis h levin',
		'name_two': 'louis levine', 
		'expected': True, 
		'description': 'louis h levin comparison with article'
	},
    {
		'name_one': 'louis j lyell',
		'name_two': 'luis leal', 
		'expected': True, 
		'description': 'louis j lyell comparison with article'
	},
    {
		'name_one': 'louis l levy',
		'name_two': 'louis levy', 
		'expected': True, 
		'description': 'louis l levy comparison with article'
	},
    {
		'name_one': 'louis l sulya',
		'name_two': 'louis leon sulya', 
		'expected': True, 
		'description': 'louis l sulya comparison with article'
	},
    {
		'name_one': 'louis lams',
		'name_two': 'louis lams', 
		'expected': True, 
		'description': 'louis lams comparison with article'
	},
    {
		'name_one': 'louis leiter',
		'name_two': 'louis leiter', 
		'expected': True, 
		'description': 'louis leiter comparison with article'
	},
    {
		'name_one': 'louis leon thurstone',
		'name_two': 'louis leon thurstone', 
		'expected': True, 
		'description': 'louis leon thurstone comparison with article'
	},
    {
		'name_one': 'louis p lodestro',
		'name_two': 'v. p. destro', 
		'expected': False, 
		'description': 'louis p lodestro comparison with article'
	},
    {
		'name_one': 'louis r detjen',
		'name_two': 'louis reinhold detjen', 
		'expected': True, 
		'description': 'louis r detjen comparison with article'
	},
    {
		'name_one': 'louis r levin',
		'name_two': 'richard louis levin', 
		'expected': True, 
		'description': 'louis r levin comparison with article'
	},
    {
		'name_one': 'louis s le tellier',
		'name_two': 'louis shepherd letellier', 
		'expected': True, 
		'description': 'louis s le tellier comparison with article'
	},
    {
		'name_one': 'louise cassell',
		'name_two': 'wallace lewis cassell', 
		'expected': True, 
		'description': 'louise cassell comparison with article'
	},
    {
		'name_one': 'louise e leonard',
		'name_two': 'e. louise leonard', 
		'expected': True, 
		'description': 'louise e leonard comparison with article'
	},
    {
		'name_one': 'louise m leet',
		'name_two': 'lewis don leet', 
		'expected': False, 
		'description': 'louise m leet comparison with article'
	},
    {
		'name_one': 'louise van ogle',
		'name_two': 'louise van ogle', 
		'expected': True, 
		'description': 'louise van ogle comparison with article'
	},
    {
		'name_one': 'lowell d ashby',
		'name_two': 'lowell dewitt ashby', 
		'expected': True, 
		'description': 'lowell d ashby comparison with article'
	},
    {
		'name_one': 'lowell p leland',
		'name_two': 'lowell p. leland', 
		'expected': True, 
		'description': 'lowell p leland comparison with article'
	},
    {
		'name_one': 'lowell r laudon',
		'name_two': 'lowell robert laudon', 
		'expected': True, 
		'description': 'lowell r laudon comparison with article'
	},
    {
		'name_one': 'loyal l conrad',
		'name_two': 'loyal lee conrad', 
		'expected': True, 
		'description': 'loyal l conrad comparison with article'
	},
    {
		'name_one': 'lucia d hough',
		'name_two': 'lucia dearborn hough', 
		'expected': True, 
		'description': 'lucia d hough comparison with article'
	},
    {
		'name_one': 'lucie s lancaster',
		'name_two': 'dabney s. lancaster', 
		'expected': False, 
		'description': 'lucie s lancaster comparison with article'
	},
    {
		'name_one': 'lucien d. pearson',
		'name_two': 'lucien dean pearson', 
		'expected': True, 
		'description': 'lucien d. pearson comparison with article'
	},
    {
		'name_one': 'lucien desjardins',
		'name_two': 'lucien h. desjardins', 
		'expected': True, 
		'description': 'lucien desjardins comparison with article'
	},
    {
		'name_one': 'lucile delano',
		'name_two': 'lucile k. delano', 
		'expected': True, 
		'description': 'lucile delano comparison with article'
	},
    {
		'name_one': 'lucille a. lemaitre',
		'name_two': 'a. l maitre', 
		'expected': True, 
		'description': 'lucille a. lemaitre comparison with article'
	},
    {
		'name_one': 'lucille a. lemaitre',
		'name_two': 'harriette a. martire', 
		'expected': False, 
		'description': 'lucille a. lemaitre comparison with article'
	},
    {
		'name_one': 'lucille a. lemaitre',
		'name_two': 'l a. maitre', 
		'expected': True, 
		'description': 'lucille a. lemaitre comparison with article'
	},
    {
		'name_one': 'lucius j desha',
		'name_two': 'lucius junius desha', 
		'expected': True, 
		'description': 'lucius j desha comparison with article'
	},
    {
		'name_one': 'lucy a sally',
		'name_two': 'lucile c. lasalle', 
		'expected': False, 
		'description': 'lucy a sally comparison with article'
	},
    {
		'name_one': 'lucy lee call',
		'name_two': 'lucy lee call', 
		'expected': True, 
		'description': 'lucy lee call comparison with article'
	},
    {
		'name_one': 'lucy lester',
		'name_two': 'lucy lester', 
		'expected': True, 
		'description': 'lucy lester comparison with article'
	},
    {
		'name_one': 'lucy lewis',
		'name_two': 'lucy lee lewis', 
		'expected': True, 
		'description': 'lucy lewis comparison with article'
	},
    {
		'name_one': 'ludvig c larson',
		'name_two': 'ludvig conrad larson', 
		'expected': True, 
		'description': 'ludvig c larson comparison with article'
	},
    {
		'name_one': 'ludwig lewisohn',
		'name_two': 'ludwig lewisohn', 
		'expected': True, 
		'description': 'ludwig lewisohn comparison with article'
	},
    {
		'name_one': 'luis alfonso fieiro',
		'name_two': 'lonnie t. vanderveer', 
		'expected': False, 
		'description': 'luis alfonso fieiro comparison with article'
	},
    {
		'name_one': 'lula g lentz',
		'name_two': 'e. g. lentz', 
		'expected': False, 
		'description': 'lula g lentz comparison with article'
	},
    {
		'name_one': 'luther o levengood',
		'name_two': 'luther omar leavengood', 
		'expected': True, 
		'description': 'luther o levengood comparison with article'
	},
    {
		'name_one': 'lutie c leavell',
		'name_two': 'lutie c. leavell', 
		'expected': True, 
		'description': 'lutie c leavell comparison with article'
	},
    {
		'name_one': 'luz m. diaz de pachero',
		'name_two': 'luis m. diaz', 
		'expected': False, 
		'description': 'luz m. diaz de pachero comparison with article'
	},
    {
		'name_one': 'lyman langdon',
		'name_two': 'lyman albert langdon', 
		'expected': True, 
		'description': 'lyman langdon comparison with article'
	},
    {
		'name_one': 'lynn l wentworth',
		'name_two': 'lynn leota wentworth', 
		'expected': True, 
		'description': 'lynn l wentworth comparison with article'
	},
    {
		'name_one': 'lysle d leach',
		'name_two': 'lysle d. leach', 
		'expected': True, 
		'description': 'lysle d leach comparison with article'
	},
    {
		'name_one': 'm fredric landwer',
		'name_two': 'milton frederic landwer', 
		'expected': True, 
		'description': 'm fredric landwer comparison with article'
	},
    {
		'name_one': 'mabel d erwin',
		'name_two': 'mabel deane erwin', 
		'expected': True, 
		'description': 'mabel d erwin comparison with article'
	},
    {
		'name_one': 'mable lesher',
		'name_two': 'mabel lesher', 
		'expected': True, 
		'description': 'mable lesher comparison with article'
	},
    {
		'name_one': 'madeline g laberge',
		'name_two': 'g. antonio laberge', 
		'expected': False, 
		'description': 'madeline g laberge comparison with article'
	},
    {
		'name_one': 'mali g lenz',
		'name_two': 'mali goldmann lenz', 
		'expected': True, 
		'description': 'mali g lenz comparison with article'
	},
    {
		'name_one': 'mamie lee davis',
		'name_two': 'mamie myrtis davis', 
		'expected': False, 
		'description': 'mamie lee davis comparison with article'
	},
    {
		'name_one': 'manson jennings',
		'name_two': 'manson van b. jennings', 
		'expected': True, 
		'description': 'manson jennings comparison with article'
	},
    {
		'name_one': 'margaret b lagrille',
		'name_two': 'margaret b. lagrille', 
		'expected': True, 
		'description': 'margaret b lagrille comparison with article'
	},
    {
		'name_one': 'margaret c de vinny',
		'name_two': 'margaret c. devinny', 
		'expected': True, 
		'description': 'margaret c de vinny comparison with article'
	},
    {
		'name_one': 'margaret c larsen',
		'name_two': 'a. margaret larsen', 
		'expected': False, 
		'description': 'margaret c larsen comparison with article'
	},
    {
		'name_one': 'margaret de schweinitz',
		'name_two': 'margaret de schweinitz', 
		'expected': True, 
		'description': 'margaret de schweinitz comparison with article'
	},
    {
		'name_one': 'margaret dearden',
		'name_two': 'leah margaret dearden', 
		'expected': True, 
		'description': 'margaret dearden comparison with article'
	},
    {
		'name_one': 'margaret degray',
		'name_two': 'margaret patterson degray', 
		'expected': True, 
		'description': 'margaret degray comparison with article'
	},
    {
		'name_one': 'margaret l leonard',
		'name_two': 'margaret lydia leonard', 
		'expected': True, 
		'description': 'margaret l leonard comparison with article'
	},
    {
		'name_one': 'margaret lamont',
		'name_two': 'margaret lamont', 
		'expected': True, 
		'description': 'margaret lamont comparison with article'
	},
    {
		'name_one': 'margery deming',
		'name_two': 'margery van n. deming', 
		'expected': True, 
		'description': 'margery deming comparison with article'
	},
    {
		'name_one': 'marguerite richards',
		'name_two': 'marguerite lentz richards', 
		'expected': True, 
		'description': 'marguerite richards comparison with article'
	},
    {
		'name_one': 'maria d picerilli',
		'name_two': 'maria de\'negri piccirilli', 
		'expected': True, 
		'description': 'maria d picerilli comparison with article'
	},
    {
		'name_one': 'maria diez de onate',
		'name_two': 'maria d. de onate', 
		'expected': True, 
		'description': 'maria diez de onate comparison with article'
	},
    {
		'name_one': 'maria rose lowther',
		'name_two': 'maria l. de lowther', 
		'expected': False, 
		'description': 'maria rose lowther comparison with article'
	},
    {
		'name_one': 'marian v devoy',
		'name_two': 'marian v. devoy', 
		'expected': True, 
		'description': 'marian v devoy comparison with article'
	},
    {
		'name_one': 'marie b denneen',
		'name_two': 'marie b. denneen', 
		'expected': True, 
		'description': 'marie b denneen comparison with article'
	},
    {
		'name_one': 'marie l schwartz',
		'name_two': 'l. laszlo schwartz', 
		'expected': False, 
		'description': 'marie l schwartz comparison with article'
	},
    {
		'name_one': 'marie lein',
		'name_two': 'marie e. lein', 
		'expected': True, 
		'description': 'marie lein comparison with article'
	},
    {
		'name_one': 'mariette le blanc',
		'name_two': 'mariette le blanc', 
		'expected': True, 
		'description': 'mariette le blanc comparison with article'
	},
    {
		'name_one': 'marine leland',
		'name_two': 'marine leland', 
		'expected': True, 
		'description': 'marine leland comparison with article'
	},
    {
		'name_one': 'marion deronde',
		'name_two': 'marion deronde', 
		'expected': True, 
		'description': 'marion deronde comparison with article'
	},
    {
		'name_one': 'marion f deshazo',
		'name_two': 'marian frances deshazo', 
		'expected': True, 
		'description': 'marion f deshazo comparison with article'
	},
    {
		'name_one': 'marion l jackson',
		'name_two': 'marion leroy jackson', 
		'expected': True, 
		'description': 'marion l jackson comparison with article'
	},
    {
		'name_one': 'marion l mcqueen',
		'name_two': 'marion leigh macqueen', 
		'expected': True, 
		'description': 'marion l mcqueen comparison with article'
	},
    {
		'name_one': 'marion lashley',
		'name_two': 'marion m. lasley', 
		'expected': True, 
		'description': 'marion lashley comparison with article'
	},
    {
		'name_one': 'marion leahy',
		'name_two': 'marion eugene lahey', 
		'expected': True, 
		'description': 'marion leahy comparison with article'
	},
    {
		'name_one': 'marion m lawrence',
		'name_two': 'marion lawrence', 
		'expected': True, 
		'description': 'marion m lawrence comparison with article'
	},
    {
		'name_one': 'marion s lewis',
		'name_two': 'marion smith lewis', 
		'expected': True, 
		'description': 'marion s lewis comparison with article'
	},
    {
		'name_one': 'marjorie e lackey',
		'name_two': 'marjorie e. latchaw', 
		'expected': False, 
		'description': 'marjorie e lackey comparison with article'
	},
    {
		'name_one': 'marjorie leonard',
		'name_two': 'marjorie leonard', 
		'expected': True, 
		'description': 'marjorie leonard comparison with article'
	},
    {
		'name_one': 'mark d howe',
		'name_two': 'mark dewolfe howe', 
		'expected': True, 
		'description': 'mark d howe comparison with article'
	},
    {
		'name_one': 'mark de leonard',
		'name_two': 'mark f. deleonard', 
		'expected': True, 
		'description': 'mark de leonard comparison with article'
	},
    {
		'name_one': 'mark h degraff',
		'name_two': 'mark h. degraff', 
		'expected': True, 
		'description': 'mark h degraff comparison with article'
	},
    {
		'name_one': 'mark l floyde',
		'name_two': 'mark lawrence floyd', 
		'expected': True, 
		'description': 'mark l floyde comparison with article'
	},
    {
		'name_one': 'mark w delzel',
		'name_two': 'mark w. delzell', 
		'expected': True, 
		'description': 'mark w delzel comparison with article'
	},
    {
		'name_one': 'marshall l pennington',
		'name_two': 'marshall lee pennington', 
		'expected': True, 
		'description': 'marshall l pennington comparison with article'
	},
    {
		'name_one': 'marshall l schmitt',
		'name_two': 'marshall langdon schmitt', 
		'expected': True, 
		'description': 'marshall l schmitt comparison with article'
	},
    {
		'name_one': 'marston d hodgin',
		'name_two': 'marston dean hodgin', 
		'expected': True, 
		'description': 'marston d hodgin comparison with article'
	},
    {
		'name_one': 'martha d wallace',
		'name_two': 'martha dee wallace', 
		'expected': True, 
		'description': 'martha d wallace comparison with article'
	},
    {
		'name_one': 'martha e leighton',
		'name_two': 'martha emma leighton', 
		'expected': True, 
		'description': 'martha e leighton comparison with article'
	},
    {
		'name_one': 'martha lewis',
		'name_two': 'martha modena lewis', 
		'expected': True, 
		'description': 'martha lewis comparison with article'
	},
    {
		'name_one': 'martha m larsen',
		'name_two': 'r. m. larsen', 
		'expected': False, 
		'description': 'martha m larsen comparison with article'
	},
    {
		'name_one': 'martha n. lewis',
		'name_two': 'martha n. lewis', 
		'expected': True, 
		'description': 'martha n. lewis comparison with article'
	},
    {
		'name_one': 'martha taber',
		'name_two': 'martha van hoesen taber', 
		'expected': True, 
		'description': 'martha taber comparison with article'
	},
    {
		'name_one': 'martin d whitaker',
		'name_two': 'martin dewey whitaker', 
		'expected': True, 
		'description': 'martin d whitaker comparison with article'
	},
    {
		'name_one': 'martin deutsch',
		'name_two': 'martin deutsch', 
		'expected': True, 
		'description': 'martin deutsch comparison with article'
	},
    {
		'name_one': 'martin l black',
		'name_two': 'martin lee black', 
		'expected': True, 
		'description': 'martin l black comparison with article'
	},
    {
		'name_one': 'martin l. lindall',
		'name_two': 'martin leroy lindahl', 
		'expected': True, 
		'description': 'martin l. lindall comparison with article'
	},
    {
		'name_one': 'martin larrabee',
		'name_two': 'martin glover larrabee', 
		'expected': True, 
		'description': 'martin larrabee comparison with article'
	},
    {
		'name_one': 'martin leigh harrison',
		'name_two': 'leigh m. harrison', 
		'expected': True, 
		'description': 'martin leigh harrison comparison with article'
	},
    {
		'name_one': 'martin levit',
		'name_two': 'martin levit', 
		'expected': True, 
		'description': 'martin levit comparison with article'
	},
    {
		'name_one': 'martin w debenham',
		'name_two': 'martin w. debenham', 
		'expected': True, 
		'description': 'martin w debenham comparison with article'
	},
    {
		'name_one': 'marvin l granstrom',
		'name_two': 'marvin leroy granstrom', 
		'expected': True, 
		'description': 'marvin l granstrom comparison with article'
	},
    {
		'name_one': 'marvin l infinger',
		'name_two': 'marvin leslie infinger', 
		'expected': True, 
		'description': 'marvin l infinger comparison with article'
	},
    {
		'name_one': 'marvin l vest',
		'name_two': 'marvin lewis vest', 
		'expected': True, 
		'description': 'marvin l vest comparison with article'
	},
    {
		'name_one': 'marvin w de jonge',
		'name_two': 'marvin willis de jonge', 
		'expected': True, 
		'description': 'marvin w de jonge comparison with article'
	},
    {
		'name_one': 'mary a devries',
		'name_two': 'mary aid de vries', 
		'expected': True, 
		'description': 'mary a devries comparison with article'
	},
    {
		'name_one': 'mary a loginuk',
		'name_two': 'grace mead andrus de laguna', 
		'expected': False, 
		'description': 'mary a loginuk comparison with article'
	},
    {
		'name_one': 'mary a ziehl',
		'name_two': 'aldert van der ziel', 
		'expected': True, 
		'description': 'mary a ziehl comparison with article'
	},
    {
		'name_one': 'mary b laughead',
		'name_two': 'mary laughead', 
		'expected': True, 
		'description': 'mary b laughead comparison with article'
	},
    {
		'name_one': 'mary blayney',
		'name_two': 'mary dee blayney', 
		'expected': True, 
		'description': 'mary blayney comparison with article'
	},
    {
		'name_one': 'mary debow',
		'name_two': 'mary virginia debow', 
		'expected': True, 
		'description': 'mary debow comparison with article'
	},
    {
		'name_one': 'mary e lakeman',
		'name_two': 'ernest rene lacheman', 
		'expected': False, 
		'description': 'mary e lakeman comparison with article'
	},
    {
		'name_one': 'mary e lakenan',
		'name_two': 'mary e. lakenan', 
		'expected': True, 
		'description': 'mary e lakenan comparison with article'
	},
    {
		'name_one': 'mary e latimer',
		'name_two': 'mary e. latimer', 
		'expected': True, 
		'description': 'mary e latimer comparison with article'
	},
    {
		'name_one': 'mary e vance',
		'name_two': 'mary e. vance', 
		'expected': True, 
		'description': 'mary e vance comparison with article'
	},
    {
		'name_one': 'mary f lawson',
		'name_two': 'mary florence lawson', 
		'expected': True, 
		'description': 'mary f lawson comparison with article'
	},
    {
		'name_one': 'mary g decker',
		'name_two': 'mary g. decker', 
		'expected': True, 
		'description': 'mary g decker comparison with article'
	},
    {
		'name_one': 'mary h langston',
		'name_two': 'j. h. langston', 
		'expected': False, 
		'description': 'mary h langston comparison with article'
	},
    {
		'name_one': 'mary j lanier',
		'name_two': 'mary jean lanier', 
		'expected': True, 
		'description': 'mary j lanier comparison with article'
	},
    {
		'name_one': 'mary l bell',
		'name_two': 'mary laverne bell', 
		'expected': True, 
		'description': 'mary l bell comparison with article'
	},
    {
		'name_one': 'mary l caldwell',
		'name_two': 'mary letitia caldwell', 
		'expected': True, 
		'description': 'mary l caldwell comparison with article'
	},
    {
		'name_one': 'mary l lewis',
		'name_two': 'mary dearing lewis', 
		'expected': False, 
		'description': 'mary l lewis comparison with article'
	},
    {
		'name_one': 'mary l mcnair',
		'name_two': 'maryhelen vannier', 
		'expected': False, 
		'description': 'mary l mcnair comparison with article'
	},
    {
		'name_one': 'mary lahlen',
		'name_two': 'marya lilien', 
		'expected': False, 
		'description': 'mary lahlen comparison with article'
	},
    {
		'name_one': 'mary lebar',
		'name_two': 'marry e. lebar', 
		'expected': True, 
		'description': 'mary lebar comparison with article'
	},
    {
		'name_one': 'mary lee lewis',
		'name_two': 'mary teresine lewis', 
		'expected': False, 
		'description': 'mary lee lewis comparison with article'
	},
    {
		'name_one': 'mary lehn',
		'name_two': 'mary belden james lehn', 
		'expected': True, 
		'description': 'mary lehn comparison with article'
	},
    {
		'name_one': 'mary leonard',
		'name_two': 'mary katherine leonard', 
		'expected': True, 
		'description': 'mary leonard comparison with article'
	},
    {
		'name_one': 'mary m lazard',
		'name_two': 'edmond myer lazard', 
		'expected': False, 
		'description': 'mary m lazard comparison with article'
	},
    {
		'name_one': 'mary p demerse',
		'name_two': 'mary mercy', 
		'expected': False, 
		'description': 'mary p demerse comparison with article'
	},
    {
		'name_one': 'mary r austin',
		'name_two': 'mary lellah austin', 
		'expected': False, 
		'description': 'mary r austin comparison with article'
	},
    {
		'name_one': 'mary sage',
		'name_two': 'mary landon sague', 
		'expected': True, 
		'description': 'mary sage comparison with article'
	},
    {
		'name_one': 'mary t olegschlaeger',
		'name_two': 'mary depaul oligsehlaeger', 
		'expected': False, 
		'description': 'mary t olegschlaeger comparison with article'
	},
    {
		'name_one': 'mary w denny',
		'name_two': 'f. w. denny', 
		'expected': False, 
		'description': 'mary w denny comparison with article'
	},
    {
		'name_one': 'mary w ladue',
		'name_two': 'mary watson ladue', 
		'expected': True, 
		'description': 'mary w ladue comparison with article'
	},
    {
		'name_one': 'mason ladd',
		'name_two': 'mason ladd', 
		'expected': True, 
		'description': 'mason ladd comparison with article'
	},
    {
		'name_one': 'mathilda e vandenbergh',
		'name_two': 'mathilda elsie vandenbergh', 
		'expected': True, 
		'description': 'mathilda e vandenbergh comparison with article'
	},
    {
		'name_one': 'matthew vanwinkle',
		'name_two': 'matthew van winkle', 
		'expected': True, 
		'description': 'matthew vanwinkle comparison with article'
	},
    {
		'name_one': 'mattii lee williams',
		'name_two': 'mentor lee williams', 
		'expected': False, 
		'description': 'mattii lee williams comparison with article'
	},
    {
		'name_one': 'maurice a thompson',
		'name_two': 'maurice dekay thompson', 
		'expected': False, 
		'description': 'maurice a thompson comparison with article'
	},
    {
		'name_one': 'maurice b lagaard',
		'name_two': 'maurice b. lagaard', 
		'expected': True, 
		'description': 'maurice b lagaard comparison with article'
	},
    {
		'name_one': 'maurice e leonard',
		'name_two': 'maurice e. leonard', 
		'expected': True, 
		'description': 'maurice e leonard comparison with article'
	},
    {
		'name_one': 'maurice l hartung',
		'name_two': 'maurice leslie hartung', 
		'expected': True, 
		'description': 'maurice l hartung comparison with article'
	},
    {
		'name_one': 'maurice l ray',
		'name_two': 'maurice lee ray', 
		'expected': True, 
		'description': 'maurice l ray comparison with article'
	},
    {
		'name_one': 'maurice lee',
		'name_two': 'maurice w. lee', 
		'expected': True, 
		'description': 'maurice lee comparison with article'
	},
    {
		'name_one': 'maurice lenz',
		'name_two': 'maurice lenz', 
		'expected': True, 
		'description': 'maurice lenz comparison with article'
	},
    {
		'name_one': 'maurice levine',
		'name_two': 'maurice levine', 
		'expected': True, 
		'description': 'maurice levine comparison with article'
	},
    {
		'name_one': 'maurice m vance',
		'name_two': 'maurice m. vance', 
		'expected': True, 
		'description': 'maurice m vance comparison with article'
	},
    {
		'name_one': 'maurice r demers',
		'name_two': 'm. r. demers', 
		'expected': True, 
		'description': 'maurice r demers comparison with article'
	},
    {
		'name_one': 'maurice t van hecke',
		'name_two': 'maurice taylor van hecke', 
		'expected': True, 
		'description': 'maurice t van hecke comparison with article'
	},
    {
		'name_one': 'max a lauffer',
		'name_two': 'max a. lauffer', 
		'expected': True, 
		'description': 'max a lauffer comparison with article'
	},
    {
		'name_one': 'max d wheatly, jr',
		'name_two': 'max delby wheatley', 
		'expected': True, 
		'description': 'max d wheatly, jr comparison with article'
	},
    {
		'name_one': 'max delbruck',
		'name_two': 'max delbruck', 
		'expected': True, 
		'description': 'max delbruck comparison with article'
	},
    {
		'name_one': 'max l moorhead',
		'name_two': 'max leon moorhead', 
		'expected': True, 
		'description': 'max l moorhead comparison with article'
	},
    {
		'name_one': 'max lanner',
		'name_two': 'max lanner', 
		'expected': True, 
		'description': 'max lanner comparison with article'
	},
    {
		'name_one': 'max lederman',
		'name_two': 'leon max lederman', 
		'expected': True, 
		'description': 'max lederman comparison with article'
	},
    {
		'name_one': 'max lerner',
		'name_two': 'max lerner', 
		'expected': True, 
		'description': 'max lerner comparison with article'
	},
    {
		'name_one': 'maxwell e lapham',
		'name_two': 'maxwell edward lapham', 
		'expected': True, 
		'description': 'maxwell e lapham comparison with article'
	},
    {
		'name_one': 'maxwell eidenorf',
		'name_two': 'maxwell leigh eidinoff', 
		'expected': True, 
		'description': 'maxwell eidenorf comparison with article'
	},
    {
		'name_one': 'maxwell farrow',
		'name_two': 'maxwell deering farrow', 
		'expected': True, 
		'description': 'maxwell farrow comparison with article'
	},
    {
		'name_one': 'maxwell r lepper',
		'name_two': 'maxwell r. lepper', 
		'expected': True, 
		'description': 'maxwell r lepper comparison with article'
	},
    {
		'name_one': 'may b van arsdale',
		'name_two': 'may b. van arsdale', 
		'expected': True, 
		'description': 'may b van arsdale comparison with article'
	},
    {
		'name_one': 'may f lewis',
		'name_two': 'f. harlan lewis', 
		'expected': False, 
		'description': 'may f lewis comparison with article'
	},
    {
		'name_one': 'maynard l mcdowell',
		'name_two': 'maynard lee mcdowell', 
		'expected': True, 
		'description': 'maynard l mcdowell comparison with article'
	},
    {
		'name_one': 'meir degani',
		'name_two': 'meir h. degani', 
		'expected': True, 
		'description': 'meir degani comparison with article'
	},
    {
		'name_one': 'melvin c lancaster',
		'name_two': 'c. maxwell lancaster', 
		'expected': False, 
		'description': 'melvin c lancaster comparison with article'
	},
    {
		'name_one': 'melvin g de chazeau',
		'name_two': 'melvin g. dechazeau', 
		'expected': True, 
		'description': 'melvin g de chazeau comparison with article'
	},
    {
		'name_one': 'melvin o k vandenbark',
		'name_two': 'melvin van den bark', 
		'expected': True, 
		'description': 'melvin o k vandenbark comparison with article'
	},
    {
		'name_one': 'melvin s lewis',
		'name_two': 'melvin s. lewis', 
		'expected': True, 
		'description': 'melvin s lewis comparison with article'
	},
    {
		'name_one': 'mena w lamb',
		'name_two': 'mina wolf lamb', 
		'expected': True, 
		'description': 'mena w lamb comparison with article'
	},
    {
		'name_one': 'mendal e lash',
		'name_two': 'mendel elmer lash', 
		'expected': True, 
		'description': 'mendal e lash comparison with article'
	},
    {
		'name_one': 'merle l landrum',
		'name_two': 'merle l. landrum', 
		'expected': True, 
		'description': 'merle l landrum comparison with article'
	},
    {
		'name_one': 'merrill e daters',
		'name_two': 'merrill edgar deters', 
		'expected': True, 
		'description': 'merrill e daters comparison with article'
	},
    {
		'name_one': 'mervin m deems',
		'name_two': 'mervin monroe deems', 
		'expected': True, 
		'description': 'mervin m deems comparison with article'
	},
    {
		'name_one': 'meryl l burgan',
		'name_two': 'r. l. von berg', 
		'expected': False, 
		'description': 'meryl l burgan comparison with article'
	},
    {
		'name_one': 'meryl w deming',
		'name_two': 'meryl william deming', 
		'expected': True, 
		'description': 'meryl w deming comparison with article'
	},
    {
		'name_one': 'michael deangelis',
		'name_two': 'michael deangelis', 
		'expected': True, 
		'description': 'michael deangelis comparison with article'
	},
    {
		'name_one': 'michael dil balso',
		'name_two': 'michael j. del balso', 
		'expected': True, 
		'description': 'michael dil balso comparison with article'
	},
    {
		'name_one': 'michael i lerner',
		'name_two': 'i. michael lerner', 
		'expected': True, 
		'description': 'michael i lerner comparison with article'
	},
    {
		'name_one': 'michael j dempsey',
		'name_two': 'michael dempsey', 
		'expected': True, 
		'description': 'michael j dempsey comparison with article'
	},
    {
		'name_one': 'michael j litty',
		'name_two': 'michael delich', 
		'expected': False, 
		'description': 'michael j litty comparison with article'
	},
    {
		'name_one': 'michael laskowski',
		'name_two': 'michael laskowski', 
		'expected': True, 
		'description': 'michael laskowski comparison with article'
	},
    {
		'name_one': 'michael leszczynski',
		'name_two': 'mieczyslaw peszczynski', 
		'expected': False, 
		'description': 'michael leszczynski comparison with article'
	},
    {
		'name_one': 'mildred k de longchamp',
		'name_two': 'mildred k. delongchamp', 
		'expected': True, 
		'description': 'mildred k de longchamp comparison with article'
	},
    {
		'name_one': 'mildred larson',
		'name_two': 'mildred r. larson', 
		'expected': True, 
		'description': 'mildred larson comparison with article'
	},
    {
		'name_one': 'mildred s lewis',
		'name_two': 'mildred sinclair lewis', 
		'expected': True, 
		'description': 'mildred s lewis comparison with article'
	},
    {
		'name_one': 'miles l hanley',
		'name_two': 'miles lawrence hanley', 
		'expected': True, 
		'description': 'miles l hanley comparison with article'
	},
    {
		'name_one': 'milton b lennon',
		'name_two': 'milton b. lennon', 
		'expected': True, 
		'description': 'milton b lennon comparison with article'
	},
    {
		'name_one': 'milton dell',
		'name_two': 'samuel milton dell', 
		'expected': True, 
		'description': 'milton dell comparison with article'
	},
    {
		'name_one': 'milton h levy',
		'name_two': 'milton levy', 
		'expected': True, 
		'description': 'milton h levy comparison with article'
	},
    {
		'name_one': 'milton l shane',
		'name_two': 'milton lanning shane', 
		'expected': True, 
		'description': 'milton l shane comparison with article'
	},
    {
		'name_one': 'milton l sunde',
		'name_two': 'milton lester sunde', 
		'expected': True, 
		'description': 'milton l sunde comparison with article'
	},
    {
		'name_one': 'milton l wiedmann',
		'name_two': 'milton lawrence wiedmann', 
		'expected': True, 
		'description': 'milton l wiedmann comparison with article'
	},
    {
		'name_one': 'milton lebow',
		'name_two': 'milton j. lebow', 
		'expected': True, 
		'description': 'milton lebow comparison with article'
	},
    {
		'name_one': 'milton scott',
		'name_two': 'milton leonard scott', 
		'expected': True, 
		'description': 'milton scott comparison with article'
	},
    {
		'name_one': 'minnie e langwell',
		'name_two': 'alfred edwin longueil', 
		'expected': False, 
		'description': 'minnie e langwell comparison with article'
	},
    {
		'name_one': 'minor u latham',
		'name_two': 'minor white latham', 
		'expected': False, 
		'description': 'minor u latham comparison with article'
	},
    {
		'name_one': 'miriam dell',
		'name_two': 'miriam dell', 
		'expected': True, 
		'description': 'miriam dell comparison with article'
	},
    {
		'name_one': 'mitchell a lata',
		'name_two': 'mitchell a. light', 
		'expected': False, 
		'description': 'mitchell a lata comparison with article'
	},
    {
		'name_one': 'mollie k laird',
		'name_two': 'alan d. k. laird', 
		'expected': False, 
		'description': 'mollie k laird comparison with article'
	},
    {
		'name_one': 'monroe e deutsch',
		'name_two': 'monroe e. deutsch', 
		'expected': True, 
		'description': 'monroe e deutsch comparison with article'
	},
    {
		'name_one': 'monte m lemann',
		'name_two': 'monte m. lemann', 
		'expected': True, 
		'description': 'monte m lemann comparison with article'
	},
    {
		'name_one': 'morris b lambie',
		'name_two': 'morris bryan lambie', 
		'expected': True, 
		'description': 'morris b lambie comparison with article'
	},
    {
		'name_one': 'morris denerstein',
		'name_two': 'morris dinnerstein', 
		'expected': True, 
		'description': 'morris denerstein comparison with article'
	},
    {
		'name_one': 'morris lazerowitz',
		'name_two': 'morris lazerowitz', 
		'expected': True, 
		'description': 'morris lazerowitz comparison with article'
	},
    {
		'name_one': 'muriel l bishop',
		'name_two': 'merle lamont bishop', 
		'expected': False, 
		'description': 'muriel l bishop comparison with article'
	},
    {
		'name_one': 'muriel l white',
		'name_two': 'kerr lachlan white', 
		'expected': False, 
		'description': 'muriel l white comparison with article'
	},
    {
		'name_one': 'muriel s guberlet',
		'name_two': 'muriel lewin guberlet', 
		'expected': False, 
		'description': 'muriel s guberlet comparison with article'
	},
    {
		'name_one': 'myles g mace',
		'name_two': 'myles la grange mace', 
		'expected': True, 
		'description': 'myles g mace comparison with article'
	},
    {
		'name_one': 'myles mace',
		'name_two': 'myles la grange mace', 
		'expected': True, 
		'description': 'myles mace comparison with article'
	},
    {
		'name_one': 'myra l bishop',
		'name_two': 'myra leslie bishop', 
		'expected': True, 
		'description': 'myra l bishop comparison with article'
	},
    {
		'name_one': 'myron d lacy',
		'name_two': 'myron dean lacy', 
		'expected': True, 
		'description': 'myron d lacy comparison with article'
	},
    {
		'name_one': 'myron l williams',
		'name_two': 'myron lawson williams', 
		'expected': True, 
		'description': 'myron l williams comparison with article'
	},
    {
		'name_one': 'myrtle m larro',
		'name_two': 'loida m. lerew', 
		'expected': False, 
		'description': 'myrtle m larro comparison with article'
	},
    {
		'name_one': 'n lewis buck',
		'name_two': 'n. lewis buck', 
		'expected': True, 
		'description': 'n lewis buck comparison with article'
	},
    {
		'name_one': 'nancy d lewis',
		'name_two': 'nancy duke lewis', 
		'expected': True, 
		'description': 'nancy d lewis comparison with article'
	},
    {
		'name_one': 'nancy e. lewis',
		'name_two': 'nancy e. lewis', 
		'expected': True, 
		'description': 'nancy e. lewis comparison with article'
	},
    {
		'name_one': 'nancy lee lytle',
		'name_two': 'nancy lytle', 
		'expected': True, 
		'description': 'nancy lee lytle comparison with article'
	},
    {
		'name_one': 'naomi laughbaum',
		'name_two': 'naomi may laughbaum', 
		'expected': True, 
		'description': 'naomi laughbaum comparison with article'
	},
    {
		'name_one': 'natalia h latta',
		'name_two': 'harrison latta', 
		'expected': True, 
		'description': 'natalia h latta comparison with article'
	},
    {
		'name_one': 'natalie lawrence',
		'name_two': 'natalie grimes lawrence', 
		'expected': True, 
		'description': 'natalie lawrence comparison with article'
	},
    {
		'name_one': 'nathan k lazar',
		'name_two': 'nathan k. lazar', 
		'expected': True, 
		'description': 'nathan k lazar comparison with article'
	},
    {
		'name_one': 'nathaniel m lawrence',
		'name_two': 'nathaniel morris lawrence', 
		'expected': True, 
		'description': 'nathaniel m lawrence comparison with article'
	},
    {
		'name_one': 'neal b de nood',
		'name_two': 'neal breaule denood', 
		'expected': True, 
		'description': 'neal b de nood comparison with article'
	},
    {
		'name_one': 'nelda r lawrence',
		'name_two': 'nelda r. lawrence', 
		'expected': True, 
		'description': 'nelda r lawrence comparison with article'
	},
    {
		'name_one': 'nellie c white',
		'name_two': 'c. langdon white', 
		'expected': False, 
		'description': 'nellie c white comparison with article'
	},
    {
		'name_one': 'nelson l walbridge',
		'name_two': 'nelson lee walbridge', 
		'expected': True, 
		'description': 'nelson l walbridge comparison with article'
	},
    {
		'name_one': 'nelson laplante',
		'name_two': 'nelson a. la plante', 
		'expected': True, 
		'description': 'nelson laplante comparison with article'
	},
    {
		'name_one': 'neppie conner',
		'name_two': 'neppie lee conner', 
		'expected': True, 
		'description': 'neppie conner comparison with article'
	},
    {
		'name_one': 'nerris e. lenahan',
		'name_two': 'norris e. lenahan', 
		'expected': True, 
		'description': 'nerris e. lenahan comparison with article'
	},
    {
		'name_one': 'newell l sims',
		'name_two': 'newell leroy sims', 
		'expected': True, 
		'description': 'newell l sims comparison with article'
	},
    {
		'name_one': 'ney l macminn',
		'name_two': 'ney lannes macminn', 
		'expected': True, 
		'description': 'ney l macminn comparison with article'
	},
    {
		'name_one': 'nicholas m lazar',
		'name_two': 'nicholas m. lazar', 
		'expected': True, 
		'description': 'nicholas m lazar comparison with article'
	},
    {
		'name_one': 'nickolas j demerath',
		'name_two': 'nicholas jay demerath', 
		'expected': True, 
		'description': 'nickolas j demerath comparison with article'
	},
    {
		'name_one': 'nielson van de luyster',
		'name_two': 'nelson van de luyster', 
		'expected': True, 
		'description': 'nielson van de luyster comparison with article'
	},
    {
		'name_one': 'nina g dean',
		'name_two': 'nina o. dean', 
		'expected': False, 
		'description': 'nina g dean comparison with article'
	},
    {
		'name_one': 'nina l weisinger',
		'name_two': 'nina lee weisinger', 
		'expected': True, 
		'description': 'nina l weisinger comparison with article'
	},
    {
		'name_one': 'noland l van demark',
		'name_two': 'noland l. vandemark', 
		'expected': True, 
		'description': 'noland l van demark comparison with article'
	},
    {
		'name_one': 'nophtali lewis',
		'name_two': 'naphtali lewis', 
		'expected': True, 
		'description': 'nophtali lewis comparison with article'
	},
    {
		'name_one': 'norma w densmore',
		'name_two': 'warren i densmore', 
		'expected': False, 
		'description': 'norma w densmore comparison with article'
	},
    {
		'name_one': 'norman b lavers',
		'name_two': 'norman l. lavers', 
		'expected': False, 
		'description': 'norman b lavers comparison with article'
	},
    {
		'name_one': 'norman b mac lean',
		'name_two': 'norman f. maclean', 
		'expected': False, 
		'description': 'norman b mac lean comparison with article'
	},
    {
		'name_one': 'norman c laffer',
		'name_two': 'norman c. laffer', 
		'expected': True, 
		'description': 'norman c laffer comparison with article'
	},
    {
		'name_one': 'norman d levine',
		'name_two': 'norman d. levine', 
		'expected': True, 
		'description': 'norman d levine comparison with article'
	},
    {
		'name_one': 'norman e lange',
		'name_two': 'norman e. lange', 
		'expected': True, 
		'description': 'norman e lange comparison with article'
	},
    {
		'name_one': 'norman f degrasse',
		'name_two': 'norman scott brien gras', 
		'expected': False, 
		'description': 'norman f degrasse comparison with article'
	},
    {
		'name_one': 'norman l jacobson',
		'name_two': 'norman leonard jacobson', 
		'expected': True, 
		'description': 'norman l jacobson comparison with article'
	},
    {
		'name_one': 'norman lawrence',
		'name_two': 'norman lionel lawrence', 
		'expected': True, 
		'description': 'norman lawrence comparison with article'
	},
    {
		'name_one': 'norman r munn',
		'name_two': 'norman leslie munn', 
		'expected': False, 
		'description': 'norman r munn comparison with article'
	},
    {
		'name_one': 'norman torrey',
		'name_two': 'norman lewis torrey', 
		'expected': True, 
		'description': 'norman torrey comparison with article'
	},
    {
		'name_one': 'noyes leech',
		'name_two': 'noyes e. leech', 
		'expected': True, 
		'description': 'noyes leech comparison with article'
	},
    {
		'name_one': 'o lee gibson',
		'name_two': 'oscar lee gibson', 
		'expected': True, 
		'description': 'o lee gibson comparison with article'
	},
    {
		'name_one': 'obed l snowden',
		'name_two': 'obed lavelle snowden', 
		'expected': True, 
		'description': 'obed l snowden comparison with article'
	},
    {
		'name_one': 'olaf larson',
		'name_two': 'olaf frederick larson', 
		'expected': True, 
		'description': 'olaf larson comparison with article'
	},
    {
		'name_one': 'olga larson',
		'name_two': 'olga larson', 
		'expected': True, 
		'description': 'olga larson comparison with article'
	},
    {
		'name_one': 'olin d morrison',
		'name_two': 'olin dee morrison', 
		'expected': True, 
		'description': 'olin d morrison comparison with article'
	},
    {
		'name_one': 'olive deluce',
		'name_two': 'olive s. deluce', 
		'expected': True, 
		'description': 'olive deluce comparison with article'
	},
    {
		'name_one': 'olive k lawyer',
		'name_two': 'kenneth lawyer', 
		'expected': True, 
		'description': 'olive k lawyer comparison with article'
	},
    {
		'name_one': 'olive p lester',
		'name_two': 'olive p. lester', 
		'expected': True, 
		'description': 'olive p lester comparison with article'
	},
    {
		'name_one': 'oliver c lee',
		'name_two': 'oliver christopher lee', 
		'expected': True, 
		'description': 'oliver c lee comparison with article'
	},
    {
		'name_one': 'oliver l rieser',
		'name_two': 'oliver leslie reiser', 
		'expected': True, 
		'description': 'oliver l rieser comparison with article'
	},
    {
		'name_one': 'oliver l walker',
		'name_two': 'oliver lafayette walker', 
		'expected': True, 
		'description': 'oliver l walker comparison with article'
	},
    {
		'name_one': 'oliver laymon',
		'name_two': 'oliver laymon', 
		'expected': True, 
		'description': 'oliver laymon comparison with article'
	},
    {
		'name_one': 'oliver lee',
		'name_two': 'oliver justin lee', 
		'expected': True, 
		'description': 'oliver lee comparison with article'
	},
    {
		'name_one': 'oliver m langhorst',
		'name_two': 'oliver martin langhorst', 
		'expected': True, 
		'description': 'oliver m langhorst comparison with article'
	},
    {
		'name_one': 'oliver w larkin',
		'name_two': 'oliver waterman larkin', 
		'expected': True, 
		'description': 'oliver w larkin comparison with article'
	},
    {
		'name_one': 'orland lefforge',
		'name_two': 'orland s. lefforge', 
		'expected': True, 
		'description': 'orland lefforge comparison with article'
	},
    {
		'name_one': 'orlando r laurandt',
		'name_two': 'val r. lorwin', 
		'expected': False, 
		'description': 'orlando r laurandt comparison with article'
	},
    {
		'name_one': 'orlo derby',
		'name_two': 'orlo derby', 
		'expected': True, 
		'description': 'orlo derby comparison with article'
	},
    {
		'name_one': 'orvil l pence',
		'name_two': 'orville leon pence', 
		'expected': True, 
		'description': 'orvil l pence comparison with article'
	},
    {
		'name_one': 'oscar j laplante',
		'name_two': 'oscar j. laplante', 
		'expected': True, 
		'description': 'oscar j laplante comparison with article'
	},
    {
		'name_one': 'oscar lanford',
		'name_two': 'oscar e. lanford', 
		'expected': True, 
		'description': 'oscar lanford comparison with article'
	},
    {
		'name_one': 'oscar lassner',
		'name_two': 'oscar lassner', 
		'expected': True, 
		'description': 'oscar lassner comparison with article'
	},
    {
		'name_one': 'oscar lewis',
		'name_two': 'oscar lewis', 
		'expected': True, 
		'description': 'oscar lewis comparison with article'
	},
    {
		'name_one': 'oskar f l hagen',
		'name_two': 'oskar frank leonard hagen', 
		'expected': True, 
		'description': 'oskar f l hagen comparison with article'
	},
    {
		'name_one': 'otta a leistiko',
		'name_two': 'daniel a. listiak', 
		'expected': False, 
		'description': 'otta a leistiko comparison with article'
	},
    {
		'name_one': 'otto g von simson',
		'name_two': 'otto georg von simson', 
		'expected': True, 
		'description': 'otto g von simson comparison with article'
	},
    {
		'name_one': 'otto van koppenhagen',
		'name_two': 'otto van koppenhagen', 
		'expected': True, 
		'description': 'otto van koppenhagen comparison with article'
	},
    {
		'name_one': 'p eldon dennis',
		'name_two': 'philip eldon dennis', 
		'expected': True, 
		'description': 'p eldon dennis comparison with article'
	},
    {
		'name_one': 'p j leinfelder',
		'name_two': 'placidus joseph leinfelder', 
		'expected': True, 
		'description': 'p j leinfelder comparison with article'
	},
    {
		'name_one': 'paul a leidy',
		'name_two': 'paul allen leidy', 
		'expected': True, 
		'description': 'paul a leidy comparison with article'
	},
    {
		'name_one': 'paul b larson',
		'name_two': 'paul b. larson', 
		'expected': True, 
		'description': 'paul b larson comparison with article'
	},
    {
		'name_one': 'paul b lawrence',
		'name_two': 'paul roger lawrence', 
		'expected': False, 
		'description': 'paul b lawrence comparison with article'
	},
    {
		'name_one': 'paul b lawson',
		'name_two': 'paul b. lawson', 
		'expected': True, 
		'description': 'paul b lawson comparison with article'
	},
    {
		'name_one': 'paul b leonard',
		'name_two': 'paul bonar leonard', 
		'expected': True, 
		'description': 'paul b leonard comparison with article'
	},
    {
		'name_one': 'paul c lemon',
		'name_two': 'paul c. lemon', 
		'expected': True, 
		'description': 'paul c lemon comparison with article'
	},
    {
		'name_one': 'paul c munson',
		'name_two': 'paul lewis munson', 
		'expected': False, 
		'description': 'paul c munson comparison with article'
	},
    {
		'name_one': 'paul d clark',
		'name_two': 'paul dennison clark', 
		'expected': True, 
		'description': 'paul d clark comparison with article'
	},
    {
		'name_one': 'paul d evans',
		'name_two': 'paul demund evans', 
		'expected': True, 
		'description': 'paul d evans comparison with article'
	},
    {
		'name_one': 'paul d lamson',
		'name_two': 'paul dudley lamson', 
		'expected': True, 
		'description': 'paul d lamson comparison with article'
	},
    {
		'name_one': 'paul dehart hurd',
		'name_two': 'paul deh. hurd', 
		'expected': True, 
		'description': 'paul dehart hurd comparison with article'
	},
    {
		'name_one': 'paul e lewis',
		'name_two': 'paul edwin lewis', 
		'expected': True, 
		'description': 'paul e lewis comparison with article'
	},
    {
		'name_one': 'paul f de wiese',
		'name_two': 'paul f. deweese', 
		'expected': True, 
		'description': 'paul f de wiese comparison with article'
	},
    {
		'name_one': 'paul f garm, jr',
		'name_two': 'e. paul degarmo', 
		'expected': False, 
		'description': 'paul f garm, jr comparison with article'
	},
    {
		'name_one': 'paul f laubenstein',
		'name_two': 'paul fritz laubenstein', 
		'expected': True, 
		'description': 'paul f laubenstein comparison with article'
	},
    {
		'name_one': 'paul f lazarsfeld',
		'name_two': 'paul f. lazarsfeld', 
		'expected': True, 
		'description': 'paul f lazarsfeld comparison with article'
	},
    {
		'name_one': 'paul f leedy',
		'name_two': 'paul f. leedy', 
		'expected': True, 
		'description': 'paul f leedy comparison with article'
	},
    {
		'name_one': 'paul g lehman',
		'name_two': 'frederick g. lehman', 
		'expected': False, 
		'description': 'paul g lehman comparison with article'
	},
    {
		'name_one': 'paul h deeb',
		'name_two': 'paul h. deeb', 
		'expected': True, 
		'description': 'paul h deeb comparison with article'
	},
    {
		'name_one': 'paul h landis',
		'name_two': 'paul h. landis', 
		'expected': True, 
		'description': 'paul h landis comparison with article'
	},
    {
		'name_one': 'paul h lavietes',
		'name_two': 'paul harold lavietes', 
		'expected': True, 
		'description': 'paul h lavietes comparison with article'
	},
    {
		'name_one': 'paul h spencer',
		'name_two': 'paul leslie spencer', 
		'expected': False, 
		'description': 'paul h spencer comparison with article'
	},
    {
		'name_one': 'paul hartman',
		'name_two': 'paul leon hartman', 
		'expected': True, 
		'description': 'paul hartman comparison with article'
	},
    {
		'name_one': 'paul j von ebers',
		'name_two': 'paul j. von ebers', 
		'expected': True, 
		'description': 'paul j von ebers comparison with article'
	},
    {
		'name_one': 'paul k vonk',
		'name_two': 'paul k. vonk', 
		'expected': True, 
		'description': 'paul k vonk comparison with article'
	},
    {
		'name_one': 'paul l brown',
		'name_two': 'paul lawrence brown', 
		'expected': True, 
		'description': 'paul l brown comparison with article'
	},
    {
		'name_one': 'paul l davies',
		'name_two': 'paul lewis davies', 
		'expected': True, 
		'description': 'paul l davies comparison with article'
	},
    {
		'name_one': 'paul l errington',
		'name_two': 'paul lester errington', 
		'expected': True, 
		'description': 'paul l errington comparison with article'
	},
    {
		'name_one': 'paul l kelley',
		'name_two': 'paul leo kelley', 
		'expected': True, 
		'description': 'paul l kelley comparison with article'
	},
    {
		'name_one': 'paul l mackendrick',
		'name_two': 'paul lachlan niackendrick', 
		'expected': True, 
		'description': 'paul l mackendrick comparison with article'
	},
    {
		'name_one': 'paul l mclain',
		'name_two': 'paul larimer mclain', 
		'expected': True, 
		'description': 'paul l mclain comparison with article'
	},
    {
		'name_one': 'paul l mellenbruch',
		'name_two': 'parl leslie mellenbruch', 
		'expected': False, 
		'description': 'paul l mellenbruch comparison with article'
	},
    {
		'name_one': 'paul l soper',
		'name_two': 'paul leon soper', 
		'expected': True, 
		'description': 'paul l soper comparison with article'
	},
    {
		'name_one': 'paul l trump, jr',
		'name_two': 'paul leroy trump', 
		'expected': True, 
		'description': 'paul l trump, jr comparison with article'
	},
    {
		'name_one': 'paul l whitely',
		'name_two': 'paul leroy whitely', 
		'expected': True, 
		'description': 'paul l whitely comparison with article'
	},
    {
		'name_one': 'paul leberman',
		'name_two': 'paul r. leberman', 
		'expected': True, 
		'description': 'paul leberman comparison with article'
	},
    {
		'name_one': 'paul levine',
		'name_two': 'robert paul levine', 
		'expected': True, 
		'description': 'paul levine comparison with article'
	},
    {
		'name_one': 'paul m dean',
		'name_two': 'paul m. dean', 
		'expected': True, 
		'description': 'paul m dean comparison with article'
	},
    {
		'name_one': 'paul m o\' leary',
		'name_two': 'paul m. o\'leary', 
		'expected': True, 
		'description': 'paul m o\' leary comparison with article'
	},
    {
		'name_one': 'paul n landis',
		'name_two': 'paul nissley landis', 
		'expected': True, 
		'description': 'paul n landis comparison with article'
	},
    {
		'name_one': 'paul n. lehoczky',
		'name_two': 'paul n. lehoczky', 
		'expected': True, 
		'description': 'paul n. lehoczky comparison with article'
	},
    {
		'name_one': 'paul r dean',
		'name_two': 'paul r. dean', 
		'expected': True, 
		'description': 'paul r dean comparison with article'
	},
    {
		'name_one': 'paul s lavik',
		'name_two': 'paul sophus lavik', 
		'expected': True, 
		'description': 'paul s lavik comparison with article'
	},
    {
		'name_one': 'paul t de camp',
		'name_two': 'paul trumbull decamp', 
		'expected': True, 
		'description': 'paul t de camp comparison with article'
	},
    {
		'name_one': 'paul v lemkau',
		'name_two': 'paul anthony lembcke', 
		'expected': False, 
		'description': 'paul v lemkau comparison with article'
	},
    {
		'name_one': 'paul v lemkau',
		'name_two': 'paul victor lemkau', 
		'expected': True, 
		'description': 'paul v lemkau comparison with article'
	},
    {
		'name_one': 'paul v thomson',
		'name_two': 'paul van k. thomson', 
		'expected': True, 
		'description': 'paul v thomson comparison with article'
	},
    {
		'name_one': 'paul van b jones',
		'name_two': 'paul van brunt jones', 
		'expected': True, 
		'description': 'paul van b jones comparison with article'
	},
    {
		'name_one': 'paul vanarsdell',
		'name_two': 'paul m. van arsdell', 
		'expected': True, 
		'description': 'paul vanarsdell comparison with article'
	},
    {
		'name_one': 'paul vanketwick',
		'name_two': 'paul van katwijk', 
		'expected': True, 
		'description': 'paul vanketwick comparison with article'
	},
    {
		'name_one': 'paula c maynoy',
		'name_two': 'carl lamanna', 
		'expected': False, 
		'description': 'paula c maynoy comparison with article'
	},
    {
		'name_one': 'percy d wilkins',
		'name_two': 'percy desmond wilkins', 
		'expected': True, 
		'description': 'percy d wilkins comparison with article'
	},
    {
		'name_one': 'percy l gainey',
		'name_two': 'percy leigh gainey', 
		'expected': True, 
		'description': 'percy l gainey comparison with article'
	},
    {
		'name_one': 'perley l thorne',
		'name_two': 'perley lenwood thorne', 
		'expected': True, 
		'description': 'perley l thorne comparison with article'
	},
    {
		'name_one': 'perry p. denune',
		'name_two': 'perry p. denune', 
		'expected': True, 
		'description': 'perry p. denune comparison with article'
	},
    {
		'name_one': 'perry v miller',
		'name_two': 'perry van miller', 
		'expected': True, 
		'description': 'perry v miller comparison with article'
	},
    {
		'name_one': 'perry w vanwagenen',
		'name_two': 'richard whitmore van wagenen', 
		'expected': False, 
		'description': 'perry w vanwagenen comparison with article'
	},
    {
		'name_one': 'peter a corsi',
		'name_two': 'andrew delcorso', 
		'expected': False, 
		'description': 'peter a corsi comparison with article'
	},
    {
		'name_one': 'peter dennis',
		'name_two': 'peter g. danis', 
		'expected': True, 
		'description': 'peter dennis comparison with article'
	},
    {
		'name_one': 'peter p h de bruyn',
		'name_two': 'peter p. h. de bruyn', 
		'expected': True, 
		'description': 'peter p h de bruyn comparison with article'
	},
    {
		'name_one': 'peter p lawlor, jr',
		'name_two': 'peter paul lawlor', 
		'expected': True, 
		'description': 'peter p lawlor, jr comparison with article'
	},
    {
		'name_one': 'peter p lejins',
		'name_two': 'peter p. lejins', 
		'expected': True, 
		'description': 'peter p lejins comparison with article'
	},
    {
		'name_one': 'peter vandekamp',
		'name_two': 'peter van de kamp', 
		'expected': True, 
		'description': 'peter vandekamp comparison with article'
	},
    {
		'name_one': 'philip f lerner',
		'name_two': 'philip franklin lerner', 
		'expected': True, 
		'description': 'philip f lerner comparison with article'
	},
    {
		'name_one': 'philip h de lacy',
		'name_two': 'phillip h. delacy', 
		'expected': True, 
		'description': 'philip h de lacy comparison with article'
	},
    {
		'name_one': 'philip l carpenter',
		'name_two': 'philip lewis carpenter', 
		'expected': True, 
		'description': 'philip l carpenter comparison with article'
	},
    {
		'name_one': 'philip l debruyn',
		'name_two': 'philip louis de bruyn', 
		'expected': True, 
		'description': 'philip l debruyn comparison with article'
	},
    {
		'name_one': 'philip l peterson',
		'name_two': 'philip lawrence peterson', 
		'expected': True, 
		'description': 'philip l peterson comparison with article'
	},
    {
		'name_one': 'philip l shipe',
		'name_two': 'philip leister shipe', 
		'expected': True, 
		'description': 'philip l shipe comparison with article'
	},
    {
		'name_one': 'philip leighton',
		'name_two': 'philip albert leighton', 
		'expected': True, 
		'description': 'philip leighton comparison with article'
	},
    {
		'name_one': 'philip levine',
		'name_two': 'philip levine', 
		'expected': True, 
		'description': 'philip levine comparison with article'
	},
    {
		'name_one': 'philipp lecorbielle',
		'name_two': 'philippe emmanuel lecorbeiller', 
		'expected': True, 
		'description': 'philipp lecorbielle comparison with article'
	},
    {
		'name_one': 'phillip e lear',
		'name_two': 'phillip e. lear', 
		'expected': True, 
		'description': 'phillip e lear comparison with article'
	},
    {
		'name_one': 'phillippe de la mare',
		'name_two': 'philippe r. de la mare', 
		'expected': True, 
		'description': 'phillippe de la mare comparison with article'
	},
    {
		'name_one': 'phineas l windsor',
		'name_two': 'phineas lawrence windsor', 
		'expected': True, 
		'description': 'phineas l windsor comparison with article'
	},
    {
		'name_one': 'pierre van rysselberghe',
		'name_two': 'pierre j. van rysselberghe', 
		'expected': True, 
		'description': 'pierre van rysselberghe comparison with article'
	},
    {
		'name_one': 'pilar madariaga',
		'name_two': 'pilar de madariaga', 
		'expected': True, 
		'description': 'pilar madariaga comparison with article'
	},
    {
		'name_one': 'pincus p levine',
		'name_two': 'pincus philip levine', 
		'expected': True, 
		'description': 'pincus p levine comparison with article'
	},
    {
		'name_one': 'quentin (none) van winkle',
		'name_two': 'quentin van winkle', 
		'expected': True, 
		'description': 'quentin (none) van winkle comparison with article'
	},
    {
		'name_one': 'quinn b demarsh',
		'name_two': 'quin b. de marsh', 
		'expected': True, 
		'description': 'quinn b demarsh comparison with article'
	},
    {
		'name_one': 'r clark lewis',
		'name_two': 'daniel clark lewis', 
		'expected': False, 
		'description': 'r clark lewis comparison with article'
	},
    {
		'name_one': 'r ernest leffel',
		'name_two': 'r. e. leffel', 
		'expected': True, 
		'description': 'r ernest leffel comparison with article'
	},
    {
		'name_one': 'r lamar newport',
		'name_two': 'lamar newport', 
		'expected': True, 
		'description': 'r lamar newport comparison with article'
	},
    {
		'name_one': 'r lee martin',
		'name_two': 'r. lee martin', 
		'expected': True, 
		'description': 'r lee martin comparison with article'
	},
    {
		'name_one': 'rachael w deangelo',
		'name_two': 'rachael wingfield de angelo', 
		'expected': True, 
		'description': 'rachael w deangelo comparison with article'
	},
    {
		'name_one': 'raffaele lattes',
		'name_two': 'raffaele lattes', 
		'expected': True, 
		'description': 'raffaele lattes comparison with article'
	},
    {
		'name_one': 'ralph a langsam',
		'name_two': 'ralph h. langsam', 
		'expected': False, 
		'description': 'ralph a langsam comparison with article'
	},
    {
		'name_one': 'ralph a lassance',
		'name_two': 'ralph a. lassance', 
		'expected': True, 
		'description': 'ralph a lassance comparison with article'
	},
    {
		'name_one': 'ralph a van wye',
		'name_two': 'ralph a. van wye', 
		'expected': True, 
		'description': 'ralph a van wye comparison with article'
	},
    {
		'name_one': 'ralph a. deterling',
		'name_two': 'ralph a. deterling', 
		'expected': True, 
		'description': 'ralph a. deterling comparison with article'
	},
    {
		'name_one': 'ralph defalco',
		'name_two': 'ralph j. defalco', 
		'expected': True, 
		'description': 'ralph defalco comparison with article'
	},
    {
		'name_one': 'ralph e deal',
		'name_two': 'ralph elbert deal', 
		'expected': True, 
		'description': 'ralph e deal comparison with article'
	},
    {
		'name_one': 'ralph e lane',
		'name_two': 'ralph e. lane', 
		'expected': True, 
		'description': 'ralph e lane comparison with article'
	},
    {
		'name_one': 'ralph e lewis',
		'name_two': 'ralph elton lewis', 
		'expected': True, 
		'description': 'ralph e lewis comparison with article'
	},
    {
		'name_one': 'ralph e vanhorn',
		'name_two': 'ralph e. hone', 
		'expected': False, 
		'description': 'ralph e vanhorn comparison with article'
	},
    {
		'name_one': 'ralph e. lancaster',
		'name_two': 'ralph e. lancaster', 
		'expected': True, 
		'description': 'ralph e. lancaster comparison with article'
	},
    {
		'name_one': 'ralph l cope',
		'name_two': 'ralph leland cope', 
		'expected': True, 
		'description': 'ralph l cope comparison with article'
	},
    {
		'name_one': 'ralph l dannley',
		'name_two': 'ralph lawrence dannley', 
		'expected': True, 
		'description': 'ralph l dannley comparison with article'
	},
    {
		'name_one': 'ralph l davis',
		'name_two': 'ralph lanier davis', 
		'expected': True, 
		'description': 'ralph l davis comparison with article'
	},
    {
		'name_one': 'ralph l de flower',
		'name_two': 'leo gerson doefler', 
		'expected': False, 
		'description': 'ralph l de flower comparison with article'
	},
    {
		'name_one': 'ralph l eyman',
		'name_two': 'ralph lee eyman', 
		'expected': True, 
		'description': 'ralph l eyman comparison with article'
	},
    {
		'name_one': 'ralph l langenheim',
		'name_two': 'ralph l. langenheim', 
		'expected': True, 
		'description': 'ralph l langenheim comparison with article'
	},
    {
		'name_one': 'ralph l thompson',
		'name_two': 'ralph leroy thompson', 
		'expected': True, 
		'description': 'ralph l thompson comparison with article'
	},
    {
		'name_one': 'ralph l. dewey',
		'name_two': 'ralph l. dewey', 
		'expected': True, 
		'description': 'ralph l. dewey comparison with article'
	},
    {
		'name_one': 'ralph ledley',
		'name_two': 'ralph g. ledley', 
		'expected': True, 
		'description': 'ralph ledley comparison with article'
	},
    {
		'name_one': 'ralph lefler',
		'name_two': 'ralph waldo lefler', 
		'expected': True, 
		'description': 'ralph lefler comparison with article'
	},
    {
		'name_one': 'ralph m lakness',
		'name_two': 'ralph m. lakness', 
		'expected': True, 
		'description': 'ralph m lakness comparison with article'
	},
    {
		'name_one': 'ralph r lashbrook',
		'name_two': 'ralph richard lashbrook', 
		'expected': True, 
		'description': 'ralph r lashbrook comparison with article'
	},
    {
		'name_one': 'ralph r lawrence',
		'name_two': 'ralph restieaux lawrence', 
		'expected': True, 
		'description': 'ralph r lawrence comparison with article'
	},
    {
		'name_one': 'ralph v bangham',
		'name_two': 'ralph vandervort bangham', 
		'expected': True, 
		'description': 'ralph v bangham comparison with article'
	},
    {
		'name_one': 'randolph l carter',
		'name_two': 'randolph laurie carter', 
		'expected': True, 
		'description': 'randolph l carter comparison with article'
	},
    {
		'name_one': 'randy h laidlaw',
		'name_two': 'harry h. laidlaw', 
		'expected': False, 
		'description': 'randy h laidlaw comparison with article'
	},
    {
		'name_one': 'raphael demos',
		'name_two': 'raphael demos', 
		'expected': True, 
		'description': 'raphael demos comparison with article'
	},
    {
		'name_one': 'raphael levy',
		'name_two': 'raphael levy', 
		'expected': True, 
		'description': 'raphael levy comparison with article'
	},
    {
		'name_one': 'ray g langebartel',
		'name_two': 'ray g. langebartel', 
		'expected': True, 
		'description': 'ray g langebartel comparison with article'
	},
    {
		'name_one': 'ray l edwards',
		'name_two': 'ray lee edwards', 
		'expected': True, 
		'description': 'ray l edwards comparison with article'
	},
    {
		'name_one': 'ray l shappelle',
		'name_two': 'ray leon chappelle', 
		'expected': True, 
		'description': 'ray l shappelle comparison with article'
	},
    {
		'name_one': 'ray l watterson',
		'name_two': 'ray leighton watterson', 
		'expected': True, 
		'description': 'ray l watterson comparison with article'
	},
    {
		'name_one': 'raymond c dein',
		'name_two': 'r. c. dein', 
		'expected': True, 
		'description': 'raymond c dein comparison with article'
	},
    {
		'name_one': 'raymond e lanhard, jr',
		'name_two': 'raymond earl lenhard', 
		'expected': True, 
		'description': 'raymond e lanhard, jr comparison with article'
	},
    {
		'name_one': 'raymond g larson',
		'name_two': 'raymond george larson', 
		'expected': True, 
		'description': 'raymond g larson comparison with article'
	},
    {
		'name_one': 'raymond h borkenhogen',
		'name_two': 'peter h. von blanckenhagen', 
		'expected': False, 
		'description': 'raymond h borkenhogen comparison with article'
	},
    {
		'name_one': 'raymond j adams',
		'name_two': 'raymond delacy adams', 
		'expected': False, 
		'description': 'raymond j adams comparison with article'
	},
    {
		'name_one': 'raymond kendall',
		'name_two': 'raymond leon kendall', 
		'expected': True, 
		'description': 'raymond kendall comparison with article'
	},
    {
		'name_one': 'raymond l davidson',
		'name_two': 'raymond leon davidson', 
		'expected': True, 
		'description': 'raymond l davidson comparison with article'
	},
    {
		'name_one': 'raymond l hightower',
		'name_two': 'raymond lee hightower', 
		'expected': True, 
		'description': 'raymond l hightower comparison with article'
	},
    {
		'name_one': 'raymond l lind',
		'name_two': 'raymond e. vanderlinde', 
		'expected': False, 
		'description': 'raymond l lind comparison with article'
	},
    {
		'name_one': 'raymond l murdoch',
		'name_two': 'raymond lester murdoch', 
		'expected': True, 
		'description': 'raymond l murdoch comparison with article'
	},
    {
		'name_one': 'raymond l powell',
		'name_two': 'raymond leo powell', 
		'expected': True, 
		'description': 'raymond l powell comparison with article'
	},
    {
		'name_one': 'raymond l shoemaker',
		'name_two': 'raymond leroy shoemaker', 
		'expected': True, 
		'description': 'raymond l shoemaker comparison with article'
	},
    {
		'name_one': 'raymond l. hill',
		'name_two': 'raymond leroy hill', 
		'expected': True, 
		'description': 'raymond l. hill comparison with article'
	},
    {
		'name_one': 'raymond lee thompson',
		'name_two': 'raymond harris thompson', 
		'expected': False, 
		'description': 'raymond lee thompson comparison with article'
	},
    {
		'name_one': 'raymond murray',
		'name_two': 'raymond leroy murray', 
		'expected': True, 
		'description': 'raymond murray comparison with article'
	},
    {
		'name_one': 'raymond s bisplinghoff',
		'name_two': 'raymond lewis bisplinghoff', 
		'expected': False, 
		'description': 'raymond s bisplinghoff comparison with article'
	},
    {
		'name_one': 'raymond t dewitt',
		'name_two': 'r. t. dewitt', 
		'expected': True, 
		'description': 'raymond t dewitt comparison with article'
	},
    {
		'name_one': 'raymond v lesikar',
		'name_two': 'raymond v. lesikar', 
		'expected': True, 
		'description': 'raymond v lesikar comparison with article'
	},
    {
		'name_one': 'reginald h mc lean',
		'name_two': 'ross h. mclean', 
		'expected': False, 
		'description': 'reginald h mc lean comparison with article'
	},
    {
		'name_one': 'reidar l anderson',
		'name_two': 'reidar lars anderson', 
		'expected': True, 
		'description': 'reidar l anderson comparison with article'
	},
    {
		'name_one': 'reinhold f larson',
		'name_two': 'reinhold fridtjof larson', 
		'expected': True, 
		'description': 'reinhold f larson comparison with article'
	},
    {
		'name_one': 'rena m larue',
		'name_two': 'rena larue', 
		'expected': True, 
		'description': 'rena m larue comparison with article'
	},
    {
		'name_one': 'reuben law',
		'name_two': 'reuben d. law', 
		'expected': True, 
		'description': 'reuben law comparison with article'
	},
    {
		'name_one': 'rev benedict lenz',
		'name_two': 'benedict lenz', 
		'expected': True, 
		'description': 'rev benedict lenz comparison with article'
	},
    {
		'name_one': 'rev denis strittmatter',
		'name_two': 'denis strittmatter', 
		'expected': True, 
		'description': 'rev denis strittmatter comparison with article'
	},
    {
		'name_one': 'rev edmund langton',
		'name_two': 'edmund langton', 
		'expected': True, 
		'description': 'rev edmund langton comparison with article'
	},
    {
		'name_one': 'rex depew',
		'name_two': 'rex d. depew', 
		'expected': True, 
		'description': 'rex depew comparison with article'
	},
    {
		'name_one': 'richard a lang',
		'name_two': 'andrew richard lang', 
		'expected': True, 
		'description': 'richard a lang comparison with article'
	},
    {
		'name_one': 'richard a lester',
		'name_two': 'richard allen lester', 
		'expected': True, 
		'description': 'richard a lester comparison with article'
	},
    {
		'name_one': 'richard a van leer',
		'name_two': 'richard t. lyer', 
		'expected': False, 
		'description': 'richard a van leer comparison with article'
	},
    {
		'name_one': 'richard c. larkins',
		'name_two': 'richard c. larkins', 
		'expected': True, 
		'description': 'richard c. larkins comparison with article'
	},
    {
		'name_one': 'richard d challener',
		'name_two': 'richard delo challener', 
		'expected': True, 
		'description': 'richard d challener comparison with article'
	},
    {
		'name_one': 'richard de bodo',
		'name_two': 'richard c. de bodo', 
		'expected': True, 
		'description': 'richard de bodo comparison with article'
	},
    {
		'name_one': 'richard deimel',
		'name_two': 'richard francis deimel', 
		'expected': True, 
		'description': 'richard deimel comparison with article'
	},
    {
		'name_one': 'richard dewey',
		'name_two': 'richard s. dewey', 
		'expected': True, 
		'description': 'richard dewey comparison with article'
	},
    {
		'name_one': 'richard f dean',
		'name_two': 'richard dean', 
		'expected': True, 
		'description': 'richard f dean comparison with article'
	},
    {
		'name_one': 'richard h van saun',
		'name_two': 'h. richard van saun', 
		'expected': True, 
		'description': 'richard h van saun comparison with article'
	},
    {
		'name_one': 'richard j deyoung',
		'name_two': 'richard de young', 
		'expected': True, 
		'description': 'richard j deyoung comparison with article'
	},
    {
		'name_one': 'richard l clark',
		'name_two': 'richard leon clark', 
		'expected': True, 
		'description': 'richard l clark comparison with article'
	},
    {
		'name_one': 'richard l landau',
		'name_two': 'richard louis landau', 
		'expected': True, 
		'description': 'richard l landau comparison with article'
	},
    {
		'name_one': 'richard l sawyer',
		'name_two': 'richard leander sawyer', 
		'expected': True, 
		'description': 'richard l sawyer comparison with article'
	},
    {
		'name_one': 'richard l scammon',
		'name_two': 'richard lewis scammon', 
		'expected': True, 
		'description': 'richard l scammon comparison with article'
	},
    {
		'name_one': 'richard l solomon',
		'name_two': 'richard lester solomon', 
		'expected': True, 
		'description': 'richard l solomon comparison with article'
	},
    {
		'name_one': 'richard l. fulton',
		'name_two': 'richard la marr fulton', 
		'expected': True, 
		'description': 'richard l. fulton comparison with article'
	},
    {
		'name_one': 'richard l. rudy',
		'name_two': 'richard lee rudy', 
		'expected': True, 
		'description': 'richard l. rudy comparison with article'
	},
    {
		'name_one': 'richard la piere',
		'name_two': 'richard tracy lapiere', 
		'expected': True, 
		'description': 'richard la piere comparison with article'
	},
    {
		'name_one': 'richard lee huntington',
		'name_two': 'richard lee huntington', 
		'expected': True, 
		'description': 'richard lee huntington comparison with article'
	},
    {
		'name_one': 'richard lee patton',
		'name_two': 'richard patton', 
		'expected': True, 
		'description': 'richard lee patton comparison with article'
	},
    {
		'name_one': 'richard morse',
		'name_two': 'richard lawrence day morse', 
		'expected': True, 
		'description': 'richard morse comparison with article'
	},
    {
		'name_one': 'richard s lawrence',
		'name_two': 'richard s. lawrence', 
		'expected': True, 
		'description': 'richard s lawrence comparison with article'
	},
    {
		'name_one': 'richard t deters',
		'name_two': 'richard t. deters', 
		'expected': True, 
		'description': 'richard t deters comparison with article'
	},
    {
		'name_one': 'richard van cleve',
		'name_two': 'richard van cleve', 
		'expected': True, 
		'description': 'richard van cleve comparison with article'
	},
    {
		'name_one': 'richard w deeds',
		'name_two': 'richard w. deeds', 
		'expected': True, 
		'description': 'richard w deeds comparison with article'
	},
    {
		'name_one': 'richard w laird',
		'name_two': 'richard willoughby laird', 
		'expected': True, 
		'description': 'richard w laird comparison with article'
	},
    {
		'name_one': 'richard w leopold',
		'name_two': 'richard william leopold', 
		'expected': True, 
		'description': 'richard w leopold comparison with article'
	},
    {
		'name_one': 'robert a hicks',
		'name_two': 'robert lansing hicks', 
		'expected': False, 
		'description': 'robert a hicks comparison with article'
	},
    {
		'name_one': 'robert a law',
		'name_two': 'robert adger law', 
		'expected': True, 
		'description': 'robert a law comparison with article'
	},
    {
		'name_one': 'robert b berg',
		'name_two': 'robert leonard berg', 
		'expected': False, 
		'description': 'robert b berg comparison with article'
	},
    {
		'name_one': 'robert b deering',
		'name_two': 'robert b. deering', 
		'expected': True, 
		'description': 'robert b deering comparison with article'
	},
    {
		'name_one': 'robert b lane',
		'name_two': 'robert philips lane', 
		'expected': False, 
		'description': 'robert b lane comparison with article'
	},
    {
		'name_one': 'robert b leighton',
		'name_two': 'robert b. leighton', 
		'expected': True, 
		'description': 'robert b leighton comparison with article'
	},
    {
		'name_one': 'robert b lewis',
		'name_two': 'robert burns lewis', 
		'expected': True, 
		'description': 'robert b lewis comparison with article'
	},
    {
		'name_one': 'robert d lane',
		'name_two': 'robert edwin lane', 
		'expected': False, 
		'description': 'robert d lane comparison with article'
	},
    {
		'name_one': 'robert d lang',
		'name_two': 'daniel robert lang', 
		'expected': True, 
		'description': 'robert d lang comparison with article'
	},
    {
		'name_one': 'robert d leigh',
		'name_two': 'robert d. leigh', 
		'expected': True, 
		'description': 'robert d leigh comparison with article'
	},
    {
		'name_one': 'robert d leiter',
		'name_two': 'robert leiter', 
		'expected': True, 
		'description': 'robert d leiter comparison with article'
	},
    {
		'name_one': 'robert d lewis',
		'name_two': 'thomas robert lewis', 
		'expected': False, 
		'description': 'robert d lewis comparison with article'
	},
    {
		'name_one': 'robert d rhynes',
		'name_two': 'robert van reen', 
		'expected': False, 
		'description': 'robert d rhynes comparison with article'
	},
    {
		'name_one': 'robert de revere',
		'name_two': 'robert e. derevere', 
		'expected': True, 
		'description': 'robert de revere comparison with article'
	},
    {
		'name_one': 'robert denny',
		'name_two': 'robert frank denny', 
		'expected': True, 
		'description': 'robert denny comparison with article'
	},
    {
		'name_one': 'robert denton',
		'name_two': 'robert claude dentan', 
		'expected': True, 
		'description': 'robert denton comparison with article'
	},
    {
		'name_one': 'robert deupree',
		'name_two': 'robt. g. deupree', 
		'expected': True, 
		'description': 'robert deupree comparison with article'
	},
    {
		'name_one': 'robert e dengler',
		'name_two': 'robert e. dengler', 
		'expected': True, 
		'description': 'robert e dengler comparison with article'
	},
    {
		'name_one': 'robert e dewey',
		'name_two': 'robert e. dewey', 
		'expected': True, 
		'description': 'robert e dewey comparison with article'
	},
    {
		'name_one': 'robert e glass',
		'name_two': 'robert lee glass', 
		'expected': False, 
		'description': 'robert e glass comparison with article'
	},
    {
		'name_one': 'robert e l faris',
		'name_two': 'robert e. lee faris', 
		'expected': True, 
		'description': 'robert e l faris comparison with article'
	},
    {
		'name_one': 'robert e l strider',
		'name_two': 'robert edward lee strider', 
		'expected': True, 
		'description': 'robert e l strider comparison with article'
	},
    {
		'name_one': 'robert e ladd',
		'name_two': 'dwight robert ladd', 
		'expected': False, 
		'description': 'robert e ladd comparison with article'
	},
    {
		'name_one': 'robert e lake',
		'name_two': 'robert e. lake', 
		'expected': True, 
		'description': 'robert e lake comparison with article'
	},
    {
		'name_one': 'robert e lane',
		'name_two': 'robert edwards lane', 
		'expected': True, 
		'description': 'robert e lane comparison with article'
	},
    {
		'name_one': 'robert e larson',
		'name_two': 'robert earl larson', 
		'expected': True, 
		'description': 'robert e larson comparison with article'
	},
    {
		'name_one': 'robert e lee',
		'name_two': 'robert edwin lee', 
		'expected': True, 
		'description': 'robert e lee comparison with article'
	},
    {
		'name_one': 'robert f deegan',
		'name_two': 'robert f. degen', 
		'expected': True, 
		'description': 'robert f deegan comparison with article'
	},
    {
		'name_one': 'robert f lawson',
		'name_two': 'robert f. lawson', 
		'expected': True, 
		'description': 'robert f lawson comparison with article'
	},
    {
		'name_one': 'robert f lent',
		'name_two': 'robert f. lent', 
		'expected': True, 
		'description': 'robert f lent comparison with article'
	},
    {
		'name_one': 'robert faulkner',
		'name_two': 'robert lee faulkner', 
		'expected': True, 
		'description': 'robert faulkner comparison with article'
	},
    {
		'name_one': 'robert g legge',
		'name_two': 'robert t. legge', 
		'expected': False, 
		'description': 'robert g legge comparison with article'
	},
    {
		'name_one': 'robert g miller',
		'name_two': 'robert lavelle miller', 
		'expected': False, 
		'description': 'robert g miller comparison with article'
	},
    {
		'name_one': 'robert h lee, jr',
		'name_two': 'robert h. lee', 
		'expected': True, 
		'description': 'robert h lee, jr comparison with article'
	},
    {
		'name_one': 'robert haun',
		'name_two': 'robert dee haun', 
		'expected': True, 
		'description': 'robert haun comparison with article'
	},
    {
		'name_one': 'robert hay',
		'name_two': 'robert dean hay', 
		'expected': True, 
		'description': 'robert hay comparison with article'
	},
    {
		'name_one': 'robert j lampman',
		'name_two': 'robert james lampman', 
		'expected': True, 
		'description': 'robert j lampman comparison with article'
	},
    {
		'name_one': 'robert j leblanc',
		'name_two': 'robert j. leblanc', 
		'expected': True, 
		'description': 'robert j leblanc comparison with article'
	},
    {
		'name_one': 'robert l briggs',
		'name_two': 'robert leroy briggs', 
		'expected': True, 
		'description': 'robert l briggs comparison with article'
	},
    {
		'name_one': 'robert l clayton',
		'name_two': 'robert lee clayton', 
		'expected': True, 
		'description': 'robert l clayton comparison with article'
	},
    {
		'name_one': 'robert l cooper',
		'name_two': 'l. leola cooper', 
		'expected': False, 
		'description': 'robert l cooper comparison with article'
	},
    {
		'name_one': 'robert l dillon',
		'name_two': 'theodore robert van dellen', 
		'expected': False, 
		'description': 'robert l dillon comparison with article'
	},
    {
		'name_one': 'robert l easton',
		'name_two': 'robert lavern easton', 
		'expected': True, 
		'description': 'robert l easton comparison with article'
	},
    {
		'name_one': 'robert l fernald',
		'name_two': 'robert leslie fernald', 
		'expected': True, 
		'description': 'robert l fernald comparison with article'
	},
    {
		'name_one': 'robert l grilley',
		'name_two': 'robert leroy grilley', 
		'expected': True, 
		'description': 'robert l grilley comparison with article'
	},
    {
		'name_one': 'robert l jackson',
		'name_two': 'robert lawrence jackson', 
		'expected': True, 
		'description': 'robert l jackson comparison with article'
	},
    {
		'name_one': 'robert l jeske',
		'name_two': 'robert leroy jeske', 
		'expected': True, 
		'description': 'robert l jeske comparison with article'
	},
    {
		'name_one': 'robert l king',
		'name_two': 'robert leslie king', 
		'expected': True, 
		'description': 'robert l king comparison with article'
	},
    {
		'name_one': 'robert l koehl',
		'name_two': 'robert lewis koehl', 
		'expected': True, 
		'description': 'robert l koehl comparison with article'
	},
    {
		'name_one': 'robert l lam',
		'name_two': 'robert lam', 
		'expected': True, 
		'description': 'robert l lam comparison with article'
	},
    {
		'name_one': 'robert l lepper',
		'name_two': 'robert l. lepper', 
		'expected': True, 
		'description': 'robert l lepper comparison with article'
	},
    {
		'name_one': 'robert l letsinger',
		'name_two': 'robert lewis letsinger', 
		'expected': True, 
		'description': 'robert l letsinger comparison with article'
	},
    {
		'name_one': 'robert l levy',
		'name_two': 'robert l. levy', 
		'expected': True, 
		'description': 'robert l levy comparison with article'
	},
    {
		'name_one': 'robert l mckee',
		'name_two': 'robert lambert mckee', 
		'expected': True, 
		'description': 'robert l mckee comparison with article'
	},
    {
		'name_one': 'robert l meirweather',
		'name_two': 'robert lee meriwether', 
		'expected': True, 
		'description': 'robert l meirweather comparison with article'
	},
    {
		'name_one': 'robert l newell',
		'name_two': 'robert lee newell', 
		'expected': True, 
		'description': 'robert l newell comparison with article'
	},
    {
		'name_one': 'robert l noell',
		'name_two': 'robert leonard noell', 
		'expected': True, 
		'description': 'robert l noell comparison with article'
	},
    {
		'name_one': 'robert l patterson',
		'name_two': 'robert leet patterson', 
		'expected': True, 
		'description': 'robert l patterson comparison with article'
	},
    {
		'name_one': 'robert l pigford',
		'name_two': 'robert lamar pigford', 
		'expected': True, 
		'description': 'robert l pigford comparison with article'
	},
    {
		'name_one': 'robert l proffer',
		'name_two': 'robert lee proffer', 
		'expected': True, 
		'description': 'robert l proffer comparison with article'
	},
    {
		'name_one': 'robert l reynolds',
		'name_two': 'robert leonard reynolds', 
		'expected': True, 
		'description': 'robert l reynolds comparison with article'
	},
    {
		'name_one': 'robert l sharp',
		'name_two': 'robert lathrop sharp', 
		'expected': True, 
		'description': 'robert l sharp comparison with article'
	},
    {
		'name_one': 'robert l smith, sr',
		'name_two': 'robert lewis smith', 
		'expected': True, 
		'description': 'robert l smith, sr comparison with article'
	},
    {
		'name_one': 'robert l thurman',
		'name_two': 'robert lee thurman', 
		'expected': True, 
		'description': 'robert l thurman comparison with article'
	},
    {
		'name_one': 'robert l tugwell',
		'name_two': 'robert lee tugwell', 
		'expected': True, 
		'description': 'robert l tugwell comparison with article'
	},
    {
		'name_one': 'robert l vandoren',
		'name_two': 'robert lawson van doren', 
		'expected': True, 
		'description': 'robert l vandoren comparison with article'
	},
    {
		'name_one': 'robert l vanhorne',
		'name_two': 'robert loren van horne', 
		'expected': True, 
		'description': 'robert l vanhorne comparison with article'
	},
    {
		'name_one': 'robert l wiggins',
		'name_two': 'robert lemuel wiggins', 
		'expected': True, 
		'description': 'robert l wiggins comparison with article'
	},
    {
		'name_one': 'robert l wolff',
		'name_two': 'robert lee wolff', 
		'expected': True, 
		'description': 'robert l wolff comparison with article'
	},
    {
		'name_one': 'robert l. leathers',
		'name_two': 'robert l. leathers', 
		'expected': True, 
		'description': 'robert l. leathers comparison with article'
	},
    {
		'name_one': 'robert lafollette',
		'name_two': 'robert lafollette', 
		'expected': True, 
		'description': 'robert lafollette comparison with article'
	},
    {
		'name_one': 'robert lancaster',
		'name_two': 'robert samuel lancaster', 
		'expected': True, 
		'description': 'robert lancaster comparison with article'
	},
    {
		'name_one': 'robert lang',
		'name_two': 'robert lang', 
		'expected': True, 
		'description': 'robert lang comparison with article'
	},
    {
		'name_one': 'robert lanni',
		'name_two': 'robert patrick lanni', 
		'expected': True, 
		'description': 'robert lanni comparison with article'
	},
    {
		'name_one': 'robert lanzillotti',
		'name_two': 'robert lanzillotti', 
		'expected': True, 
		'description': 'robert lanzillotti comparison with article'
	},
    {
		'name_one': 'robert lee christian',
		'name_two': 'robert christian', 
		'expected': True, 
		'description': 'robert lee christian comparison with article'
	},
    {
		'name_one': 'robert lee hunter',
		'name_two': 'francis robert hunter', 
		'expected': False, 
		'description': 'robert lee hunter comparison with article'
	},
    {
		'name_one': 'robert lekachman',
		'name_two': 'robert lekachman', 
		'expected': True, 
		'description': 'robert lekachman comparison with article'
	},
    {
		'name_one': 'robert leon white',
		'name_two': 'robert leon white', 
		'expected': True, 
		'description': 'robert leon white comparison with article'
	},
    {
		'name_one': 'robert lepper',
		'name_two': 'robert lepper', 
		'expected': True, 
		'description': 'robert lepper comparison with article'
	},
    {
		'name_one': 'robert lew',
		'name_two': 'robert louise', 
		'expected': True, 
		'description': 'robert lew comparison with article'
	},
    {
		'name_one': 'robert m delaney',
		'name_two': 'robert mills delaney', 
		'expected': True, 
		'description': 'robert m delaney comparison with article'
	},
    {
		'name_one': 'robert m la forge',
		'name_two': 'robert mallory laforge', 
		'expected': True, 
		'description': 'robert m la forge comparison with article'
	},
    {
		'name_one': 'robert m lewert',
		'name_two': 'robert murdoch lewert', 
		'expected': True, 
		'description': 'robert m lewert comparison with article'
	},
    {
		'name_one': 'robert miller',
		'name_two': 'robert demorest miller', 
		'expected': True, 
		'description': 'robert miller comparison with article'
	},
    {
		'name_one': 'robert n lass',
		'name_two': 'robert n. lass', 
		'expected': True, 
		'description': 'robert n lass comparison with article'
	},
    {
		'name_one': 'robert r leidy',
		'name_two': 'raimundo lida', 
		'expected': False, 
		'description': 'robert r leidy comparison with article'
	},
    {
		'name_one': 'robert s landauer',
		'name_two': 'robert s. landauer', 
		'expected': True, 
		'description': 'robert s landauer comparison with article'
	},
    {
		'name_one': 'robert s lewis',
		'name_two': 'robert s. lewis', 
		'expected': True, 
		'description': 'robert s lewis comparison with article'
	},
    {
		'name_one': 'robert v finney',
		'name_two': 'robert vansant finney', 
		'expected': True, 
		'description': 'robert v finney comparison with article'
	},
    {
		'name_one': 'robert v longmuir',
		'name_two': 'robert v. langmuir', 
		'expected': True, 
		'description': 'robert v longmuir comparison with article'
	},
    {
		'name_one': 'robert van de graaff',
		'name_two': 'robert jemison van de graaff', 
		'expected': True, 
		'description': 'robert van de graaff comparison with article'
	},
    {
		'name_one': 'robert van horn',
		'name_two': 'robert bowman van horn', 
		'expected': True, 
		'description': 'robert van horn comparison with article'
	},
    {
		'name_one': 'robert von nardroff',
		'name_two': 'robert von nardroff', 
		'expected': True, 
		'description': 'robert von nardroff comparison with article'
	},
    {
		'name_one': 'robert w dean',
		'name_two': 'w. c. dean', 
		'expected': False, 
		'description': 'robert w dean comparison with article'
	},
    {
		'name_one': 'robert w desmond',
		'name_two': 'robert w. desmond', 
		'expected': True, 
		'description': 'robert w desmond comparison with article'
	},
    {
		'name_one': 'robert w doisher',
		'name_two': 'robert w. deisher', 
		'expected': True, 
		'description': 'robert w doisher comparison with article'
	},
    {
		'name_one': 'robert w houghton',
		'name_two': 'robert w. van houten', 
		'expected': True, 
		'description': 'robert w houghton comparison with article'
	},
    {
		'name_one': 'robert w leonard',
		'name_two': 'robert w. leonard', 
		'expected': True, 
		'description': 'robert w leonard comparison with article'
	},
    {
		'name_one': 'robert whitman',
		'name_two': 'robert van duyne whitman', 
		'expected': True, 
		'description': 'robert whitman comparison with article'
	},
    {
		'name_one': 'roberta d ortenburger',
		'name_two': 'roberta deam ortenburger', 
		'expected': True, 
		'description': 'roberta d ortenburger comparison with article'
	},
    {
		'name_one': 'roberta m law',
		'name_two': 'roberta law', 
		'expected': True, 
		'description': 'roberta m law comparison with article'
	},
    {
		'name_one': 'robt l burwell, jr',
		'name_two': 'robert lemmon burwell', 
		'expected': True, 
		'description': 'robt l burwell, jr comparison with article'
	},
    {
		'name_one': 'robt l goulding',
		'name_two': 'robert lee goulding', 
		'expected': True, 
		'description': 'robt l goulding comparison with article'
	},
    {
		'name_one': 'roderick d gordon',
		'name_two': 'roderick dean gordon', 
		'expected': True, 
		'description': 'roderick d gordon comparison with article'
	},
    {
		'name_one': 'roger c. larson',
		'name_two': 'roger c. larson', 
		'expected': True, 
		'description': 'roger c. larson comparison with article'
	},
    {
		'name_one': 'roger l lawrence',
		'name_two': 'roger l. lawrence', 
		'expected': True, 
		'description': 'roger l lawrence comparison with article'
	},
    {
		'name_one': 'roger l williams',
		'name_two': 'roger lawrence williams', 
		'expected': True, 
		'description': 'roger l williams comparison with article'
	},
    {
		'name_one': 'roland l kramer',
		'name_two': 'roland laird kramer', 
		'expected': True, 
		'description': 'roland l kramer comparison with article'
	},
    {
		'name_one': 'roland v rider',
		'name_two': 'rowland vance rider', 
		'expected': True, 
		'description': 'roland v rider comparison with article'
	},
    {
		'name_one': 'roman s ladewski',
		'name_two': 'roman s. ladewski', 
		'expected': True, 
		'description': 'roman s ladewski comparison with article'
	},
    {
		'name_one': 'ronald a lanor',
		'name_two': 'a. a. lenior', 
		'expected': False, 
		'description': 'ronald a lanor comparison with article'
	},
    {
		'name_one': 'ronald b levinson',
		'name_two': 'ronald b. levinson', 
		'expected': True, 
		'description': 'ronald b levinson comparison with article'
	},
    {
		'name_one': 'ronald k de ford',
		'name_two': 'ronald k. deford', 
		'expected': True, 
		'description': 'ronald k de ford comparison with article'
	},
    {
		'name_one': 'ronnald g le sage',
		'name_two': 'romuald g. lesage', 
		'expected': True, 
		'description': 'ronnald g le sage comparison with article'
	},
    {
		'name_one': 'rosa lee andrews',
		'name_two': 'mary lee andrews', 
		'expected': False, 
		'description': 'rosa lee andrews comparison with article'
	},
    {
		'name_one': 'rosalie wessel',
		'name_two': 'rosa lee wessel', 
		'expected': True, 
		'description': 'rosalie wessel comparison with article'
	},
    {
		'name_one': 'rosalind s langsam',
		'name_two': 'rosalind streep langsam', 
		'expected': True, 
		'description': 'rosalind s langsam comparison with article'
	},
    {
		'name_one': 'roscoe d leas',
		'name_two': 'roscoe david leas', 
		'expected': True, 
		'description': 'roscoe d leas comparison with article'
	},
    {
		'name_one': 'rose c mooney',
		'name_two': 'rose ledieu mooney', 
		'expected': False, 
		'description': 'rose c mooney comparison with article'
	},
    {
		'name_one': 'rose hum lee',
		'name_two': 'rose hum lee', 
		'expected': True, 
		'description': 'rose hum lee comparison with article'
	},
    {
		'name_one': 'rose lamme',
		'name_two': 'rose lamme', 
		'expected': True, 
		'description': 'rose lamme comparison with article'
	},
    {
		'name_one': 'rose leske',
		'name_two': 'rose katherine leske', 
		'expected': True, 
		'description': 'rose leske comparison with article'
	},
    {
		'name_one': 'rose lisenby',
		'name_two': 'rose lee lisenby', 
		'expected': True, 
		'description': 'rose lisenby comparison with article'
	},
    {
		'name_one': 'rowland w leiby',
		'name_two': 'rowland willis leiby', 
		'expected': True, 
		'description': 'rowland w leiby comparison with article'
	},
    {
		'name_one': 'roy c langford',
		'name_two': 'roy clinton langford', 
		'expected': True, 
		'description': 'roy c langford comparison with article'
	},
    {
		'name_one': 'roy d sheffield',
		'name_two': 'roy dexter sheffieid', 
		'expected': True, 
		'description': 'roy d sheffield comparison with article'
	},
    {
		'name_one': 'roy h lanphear',
		'name_two': 'roy higinbotham lanphear', 
		'expected': True, 
		'description': 'roy h lanphear comparison with article'
	},
    {
		'name_one': 'roy s dearstyne',
		'name_two': 'roy styring dearstyne', 
		'expected': True, 
		'description': 'roy s dearstyne comparison with article'
	},
    {
		'name_one': 'roy s jensen',
		'name_two': 'mead leroy jensen', 
		'expected': False, 
		'description': 'roy s jensen comparison with article'
	},
    {
		'name_one': 'roy v lalmage',
		'name_two': 'roy van neste talmage', 
		'expected': True, 
		'description': 'roy v lalmage comparison with article'
	},
    {
		'name_one': 'ruby l valz',
		'name_two': 'l. r. la valle', 
		'expected': False, 
		'description': 'ruby l valz comparison with article'
	},
    {
		'name_one': 'rudolph e langer',
		'name_two': 'rudolph ernest langer', 
		'expected': True, 
		'description': 'rudolph e langer comparison with article'
	},
    {
		'name_one': 'rudolph l biesele',
		'name_two': 'rudolph leopold biesele', 
		'expected': True, 
		'description': 'rudolph l biesele comparison with article'
	},
    {
		'name_one': 'rupert b vance',
		'name_two': 'rupert bayless vance', 
		'expected': True, 
		'description': 'rupert b vance comparison with article'
	},
    {
		'name_one': 'russel laman',
		'name_two': 'russell laman', 
		'expected': True, 
		'description': 'russel laman comparison with article'
	},
    {
		'name_one': 'russell a lecronier',
		'name_two': 'a. russell lecronier', 
		'expected': True, 
		'description': 'russell a lecronier comparison with article'
	},
    {
		'name_one': 'russell d dement',
		'name_two': 'r. d. dement', 
		'expected': True, 
		'description': 'russell d dement comparison with article'
	},
    {
		'name_one': 'russell d snyder',
		'name_two': 'russell dewey snyder', 
		'expected': True, 
		'description': 'russell d snyder comparison with article'
	},
    {
		'name_one': 'russell e kittnell',
		'name_two': 'joseph e. von kaenel', 
		'expected': False, 
		'description': 'russell e kittnell comparison with article'
	},
    {
		'name_one': 'russell e larson',
		'name_two': 'russell e. larson', 
		'expected': True, 
		'description': 'russell e larson comparison with article'
	},
    {
		'name_one': 'russell h larson',
		'name_two': 'russell harold larson', 
		'expected': True, 
		'description': 'russell h larson comparison with article'
	},
    {
		'name_one': 'russell l dicks',
		'name_two': 'russell leslie dicks', 
		'expected': True, 
		'description': 'russell l dicks comparison with article'
	},
    {
		'name_one': 'russell r de alvarez',
		'name_two': 'russell r. de alvarez', 
		'expected': True, 
		'description': 'russell r de alvarez comparison with article'
	},
    {
		'name_one': 'russell r larmon',
		'name_two': 'russell raymond larmon', 
		'expected': True, 
		'description': 'russell r larmon comparison with article'
	},
    {
		'name_one': 'ruth b langford',
		'name_two': 'ruth betty langford', 
		'expected': True, 
		'description': 'ruth b langford comparison with article'
	},
    {
		'name_one': 'ruth b leedy',
		'name_two': 'ruth berg leedy', 
		'expected': True, 
		'description': 'ruth b leedy comparison with article'
	},
    {
		'name_one': 'ruth deacon',
		'name_two': 'ruth e. deacon', 
		'expected': True, 
		'description': 'ruth deacon comparison with article'
	},
    {
		'name_one': 'ruth dean',
		'name_two': 'ruth josephine dean', 
		'expected': True, 
		'description': 'ruth dean comparison with article'
	},
    {
		'name_one': 'ruth lee kennedy',
		'name_two': 'ruth lee kennedy', 
		'expected': True, 
		'description': 'ruth lee kennedy comparison with article'
	},
    {
		'name_one': 'ruth leonard',
		'name_two': 'ruth shaw leonard', 
		'expected': True, 
		'description': 'ruth leonard comparison with article'
	},
    {
		'name_one': 'ruth m lambertus',
		'name_two': 'ruth m. lambertus', 
		'expected': True, 
		'description': 'ruth m lambertus comparison with article'
	},
    {
		'name_one': 'ruth m lampson',
		'name_two': 'ruth murdock lampson', 
		'expected': True, 
		'description': 'ruth m lampson comparison with article'
	},
    {
		'name_one': 'ruth n denny',
		'name_two': 'reuel n. denney', 
		'expected': False, 
		'description': 'ruth n denny comparison with article'
	},
    {
		'name_one': 'ruth r dismang',
		'name_two': 'winston r. de monsabert', 
		'expected': False, 
		'description': 'ruth r dismang comparison with article'
	},
    {
		'name_one': 'ruth r leitch',
		'name_two': 'ruth redding leitch', 
		'expected': True, 
		'description': 'ruth r leitch comparison with article'
	},
    {
		'name_one': 'ruth s lamb',
		'name_two': 'ruth stanton lamb', 
		'expected': True, 
		'description': 'ruth s lamb comparison with article'
	},
    {
		'name_one': 'ruth s lerner',
		'name_two': 'ruth spero lerner', 
		'expected': True, 
		'description': 'ruth s lerner comparison with article'
	},
    {
		'name_one': 'ruth t. lehman',
		'name_two': 'ruth t. lehman', 
		'expected': True, 
		'description': 'ruth t. lehman comparison with article'
	},
    {
		'name_one': 's arthur lake',
		'name_two': 'w. s. lake', 
		'expected': False, 
		'description': 's arthur lake comparison with article'
	},
    {
		'name_one': 's le roy brown',
		'name_two': 'simpson leroy brown', 
		'expected': True, 
		'description': 's le roy brown comparison with article'
	},
    {
		'name_one': 's lewis drake',
		'name_two': 'louis s. drake', 
		'expected': True, 
		'description': 's lewis drake comparison with article'
	},
    {
		'name_one': 'salvatore devita',
		'name_two': 'salvatore devita', 
		'expected': True, 
		'description': 'salvatore devita comparison with article'
	},
    {
		'name_one': 'sam c dellinger',
		'name_two': 'samuel claudius dellinger', 
		'expected': True, 
		'description': 'sam c dellinger comparison with article'
	},
    {
		'name_one': 'sam legvold',
		'name_two': 'sam legvold', 
		'expected': True, 
		'description': 'sam legvold comparison with article'
	},
    {
		'name_one': 'sam leifeste',
		'name_two': 'sam a. d. leifeste', 
		'expected': True, 
		'description': 'sam leifeste comparison with article'
	},
    {
		'name_one': 'samuel a lear',
		'name_two': 'samuel a. lear', 
		'expected': True, 
		'description': 'samuel a lear comparison with article'
	},
    {
		'name_one': 'samuel a levinson',
		'name_two': 'samuel azor levinson', 
		'expected': True, 
		'description': 'samuel a levinson comparison with article'
	},
    {
		'name_one': 'samuel d atkins',
		'name_two': 'samuel decoster atkins', 
		'expected': True, 
		'description': 'samuel d atkins comparison with article'
	},
    {
		'name_one': 'samuel d zelden',
		'name_two': 'samuel demitry zeldin', 
		'expected': True, 
		'description': 'samuel d zelden comparison with article'
	},
    {
		'name_one': 'samuel detwiler',
		'name_two': 'samuel r. detwiler', 
		'expected': True, 
		'description': 'samuel detwiler comparison with article'
	},
    {
		'name_one': 'samuel j jr lang',
		'name_two': 'samuel j. lang', 
		'expected': True, 
		'description': 'samuel j jr lang comparison with article'
	},
    {
		'name_one': 'samuel l gargill',
		'name_two': 'samuel leon gargill', 
		'expected': True, 
		'description': 'samuel l gargill comparison with article'
	},
    {
		'name_one': 'samuel l greenwood',
		'name_two': 'sam lee greenwood', 
		'expected': True, 
		'description': 'samuel l greenwood comparison with article'
	},
    {
		'name_one': 'samuel l leonard',
		'name_two': 'samuel leeson leonard', 
		'expected': True, 
		'description': 'samuel l leonard comparison with article'
	},
    {
		'name_one': 'samuel l prince',
		'name_two': 'samuel lander prince', 
		'expected': True, 
		'description': 'samuel l prince comparison with article'
	},
    {
		'name_one': 'samuel lang',
		'name_two': 'samuel lang', 
		'expected': True, 
		'description': 'samuel lang comparison with article'
	},
    {
		'name_one': 'samuel leger',
		'name_two': 'samuel h. leger', 
		'expected': True, 
		'description': 'samuel leger comparison with article'
	},
    {
		'name_one': 'samuel lehman',
		'name_two': 'samuel george lehman', 
		'expected': True, 
		'description': 'samuel lehman comparison with article'
	},
    {
		'name_one': 'samuel lerner',
		'name_two': 'samuel lerner', 
		'expected': True, 
		'description': 'samuel lerner comparison with article'
	},
    {
		'name_one': 'samuel m derrick',
		'name_two': 'samuel melanchthon derrick', 
		'expected': True, 
		'description': 'samuel m derrick comparison with article'
	},
    {
		'name_one': 'samuel m levin',
		'name_two': 'samuel m. levin', 
		'expected': True, 
		'description': 'samuel m levin comparison with article'
	},
    {
		'name_one': 'samuel van valkenburg',
		'name_two': 'samuel van valkenburg', 
		'expected': True, 
		'description': 'samuel van valkenburg comparison with article'
	},
    {
		'name_one': 'sandra lee wray',
		'name_two': 'alexius taikyue ree', 
		'expected': False, 
		'description': 'sandra lee wray comparison with article'
	},
    {
		'name_one': 'sandra lehrman',
		'name_two': 'alexander lehrman', 
		'expected': False, 
		'description': 'sandra lehrman comparison with article'
	},
    {
		'name_one': 'sanford e leeds',
		'name_two': 'sanford e. leeds', 
		'expected': True, 
		'description': 'sanford e leeds comparison with article'
	},
    {
		'name_one': 'sara a deford',
		'name_two': 'sara deford', 
		'expected': True, 
		'description': 'sara a deford comparison with article'
	},
    {
		'name_one': 'sara e burnham',
		'name_two': 'ebert van buren', 
		'expected': False, 
		'description': 'sara e burnham comparison with article'
	},
    {
		'name_one': 'sarah denett holmes',
		'name_two': 'sarah bennett holmes', 
		'expected': True, 
		'description': 'sarah denett holmes comparison with article'
	},
    {
		'name_one': 'sarah m vancil',
		'name_two': 'sarah may vancil', 
		'expected': True, 
		'description': 'sarah m vancil comparison with article'
	},
    {
		'name_one': 'saul levy',
		'name_two': 'saul levy', 
		'expected': True, 
		'description': 'saul levy comparison with article'
	},
    {
		'name_one': 'saunders mac lane',
		'name_two': 'saunders mac lane', 
		'expected': True, 
		'description': 'saunders mac lane comparison with article'
	},
    {
		'name_one': 'sergio debenedetti',
		'name_two': 'sergio de benedetti', 
		'expected': True, 
		'description': 'sergio debenedetti comparison with article'
	},
    {
		'name_one': 'sharley b demotte',
		'name_two': 'sharley b. demotte', 
		'expected': True, 
		'description': 'sharley b demotte comparison with article'
	},
    {
		'name_one': 'shelby d gerking, jr',
		'name_two': 'shelby delos gerking', 
		'expected': True, 
		'description': 'shelby d gerking, jr comparison with article'
	},
    {
		'name_one': 'sherman p lawton',
		'name_two': 'sherman paxton lawton', 
		'expected': True, 
		'description': 'sherman p lawton comparison with article'
	},
    {
		'name_one': 'sidney lees',
		'name_two': 'sidney lees', 
		'expected': True, 
		'description': 'sidney lees comparison with article'
	},
    {
		'name_one': 'sigmund w leifson',
		'name_two': 'sigmund w. leifson', 
		'expected': True, 
		'description': 'sigmund w leifson comparison with article'
	},
    {
		'name_one': 'signe larsen',
		'name_two': 'esper signius larsen', 
		'expected': True, 
		'description': 'signe larsen comparison with article'
	},
    {
		'name_one': 'silvere c. vandecaveye',
		'name_two': 's. c. vandecaveye', 
		'expected': True, 
		'description': 'silvere c. vandecaveye comparison with article'
	},
    {
		'name_one': 'simeon e leland',
		'name_two': 'simeon elbridge leland', 
		'expected': True, 
		'description': 'simeon e leland comparison with article'
	},
    {
		'name_one': 'simon leopold',
		'name_two': 'simon stein leopold', 
		'expected': True, 
		'description': 'simon leopold comparison with article'
	},
    {
		'name_one': 'sister mary john leo',
		'name_two': 'mary john', 
		'expected': True, 
		'description': 'sister mary john leo comparison with article'
	},
    {
		'name_one': 'sol levin',
		'name_two': 'saul levin', 
		'expected': True, 
		'description': 'sol levin comparison with article'
	},
    {
		'name_one': 'solomon leider',
		'name_two': 'solomon leader', 
		'expected': True, 
		'description': 'solomon leider comparison with article'
	},
    {
		'name_one': 'sophia mcdonald',
		'name_two': 'sophia levy mcdonald', 
		'expected': True, 
		'description': 'sophia mcdonald comparison with article'
	},
    {
		'name_one': 'stanley a leavy',
		'name_two': 'stanley arnold leavy', 
		'expected': True, 
		'description': 'stanley a leavy comparison with article'
	},
    {
		'name_one': 'stanley lamm',
		'name_two': 'stanley s. lamm', 
		'expected': True, 
		'description': 'stanley lamm comparison with article'
	},
    {
		'name_one': 'stanley lesser',
		'name_two': 'stanley r. lesser', 
		'expected': True, 
		'description': 'stanley lesser comparison with article'
	},
    {
		'name_one': 'stella l lamond',
		'name_two': 'stella lodge lamond', 
		'expected': True, 
		'description': 'stella l lamond comparison with article'
	},
    {
		'name_one': 'stella l lange',
		'name_two': 'stella lange', 
		'expected': True, 
		'description': 'stella l lange comparison with article'
	},
    {
		'name_one': 'stephen dean, iii',
		'name_two': 'stephen j. dean', 
		'expected': True, 
		'description': 'stephen dean, iii comparison with article'
	},
    {
		'name_one': 'stewart l garrison',
		'name_two': 'stewart lee garrison', 
		'expected': True, 
		'description': 'stewart l garrison comparison with article'
	},
    {
		'name_one': 'stewart s dallyn',
		'name_two': 'stewart lamonte dallyn', 
		'expected': False, 
		'description': 'stewart s dallyn comparison with article'
	},
    {
		'name_one': 'stuart b le compte',
		'name_two': 'stuart b. lecompte', 
		'expected': True, 
		'description': 'stuart b le compte comparison with article'
	},
    {
		'name_one': 'susan d dees',
		'name_two': 'susan coons dees', 
		'expected': False, 
		'description': 'susan d dees comparison with article'
	},
    {
		'name_one': 'suzanne lasater',
		'name_two': 'suzanne margot lasater', 
		'expected': True, 
		'description': 'suzanne lasater comparison with article'
	},
    {
		'name_one': 't l sharfman',
		'name_two': 'isaiah leo sharfman', 
		'expected': False, 
		'description': 't l sharfman comparison with article'
	},
    {
		'name_one': 't. dewitt carr',
		'name_two': 't. dewitt carr', 
		'expected': True, 
		'description': 't. dewitt carr comparison with article'
	},
    {
		'name_one': 't. lawerence foran',
		'name_two': 't. lawrence foran', 
		'expected': True, 
		'description': 't. lawerence foran comparison with article'
	},
    {
		'name_one': 'talmadge l peele',
		'name_two': 'talmadge lee peele', 
		'expected': True, 
		'description': 'talmadge l peele comparison with article'
	},
    {
		'name_one': 'tella marie debose',
		'name_two': 'tella marie debose', 
		'expected': True, 
		'description': 'tella marie debose comparison with article'
	},
    {
		'name_one': 'thelma lavine',
		'name_two': 'thelma z. lavine', 
		'expected': True, 
		'description': 'thelma lavine comparison with article'
	},
    {
		'name_one': 'theodore a lams',
		'name_two': 'theodore a. lams', 
		'expected': True, 
		'description': 'theodore a lams comparison with article'
	},
    {
		'name_one': 'theodore b ley',
		'name_two': 'theodore de lay', 
		'expected': True, 
		'description': 'theodore b ley comparison with article'
	},
    {
		'name_one': 'theodore b ley',
		'name_two': 'theodore s. de lay', 
		'expected': False, 
		'description': 'theodore b ley comparison with article'
	},
    {
		'name_one': 'theodore bakermann',
		'name_two': 'theodore von karman', 
		'expected': False, 
		'description': 'theodore bakermann comparison with article'
	},
    {
		'name_one': 'theodore harris',
		'name_two': 'theodore lester harris', 
		'expected': True, 
		'description': 'theodore harris comparison with article'
	},
    {
		'name_one': 'theodore l dehne',
		'name_two': 'theodore l. dehne', 
		'expected': True, 
		'description': 'theodore l dehne comparison with article'
	},
    {
		'name_one': 'theodore lang',
		'name_two': 'theodore lang', 
		'expected': True, 
		'description': 'theodore lang comparison with article'
	},
    {
		'name_one': 'theodore paul phillips',
		'name_two': 'theodore dewitt phillips', 
		'expected': False, 
		'description': 'theodore paul phillips comparison with article'
	},
    {
		'name_one': 'theodore storch',
		'name_two': 'theodore j. c. von storch', 
		'expected': True, 
		'description': 'theodore storch comparison with article'
	},
    {
		'name_one': 'theodore t lafferty, sr',
		'name_two': 'theodore t. lafferty', 
		'expected': True, 
		'description': 'theodore t lafferty, sr comparison with article'
	},
    {
		'name_one': 'theordore l reller',
		'name_two': 'theodore lee reller', 
		'expected': True, 
		'description': 'theordore l reller comparison with article'
	},
    {
		'name_one': 'thomas a leonard',
		'name_two': 'a. orin leonard', 
		'expected': False, 
		'description': 'thomas a leonard comparison with article'
	},
    {
		'name_one': 'thomas a. dent',
		'name_two': 'thomas johnstone dent', 
		'expected': False, 
		'description': 'thomas a. dent comparison with article'
	},
    {
		'name_one': 'thomas c deane',
		'name_two': 'c. thomas dean', 
		'expected': True, 
		'description': 'thomas c deane comparison with article'
	},
    {
		'name_one': 'thomas c laipply',
		'name_two': 'thomas charles laipply', 
		'expected': True, 
		'description': 'thomas c laipply comparison with article'
	},
    {
		'name_one': 'thomas c van cleve',
		'name_two': 'thomas curtis van cleve', 
		'expected': True, 
		'description': 'thomas c van cleve comparison with article'
	},
    {
		'name_one': 'thomas demott',
		'name_two': 'thomas demott', 
		'expected': True, 
		'description': 'thomas demott comparison with article'
	},
    {
		'name_one': 'thomas devries',
		'name_two': 'thomas de vries', 
		'expected': True, 
		'description': 'thomas devries comparison with article'
	},
    {
		'name_one': 'thomas e lasswell',
		'name_two': 'thomas e. lasswell', 
		'expected': True, 
		'description': 'thomas e lasswell comparison with article'
	},
    {
		'name_one': 'thomas f debnam',
		'name_two': 'thomas finley debnam', 
		'expected': True, 
		'description': 'thomas f debnam comparison with article'
	},
    {
		'name_one': 'thomas h lanman',
		'name_two': 'thomas hinckley lanman', 
		'expected': True, 
		'description': 'thomas h lanman comparison with article'
	},
    {
		'name_one': 'thomas h le duc',
		'name_two': 'thomas harold leduc', 
		'expected': True, 
		'description': 'thomas h le duc comparison with article'
	},
    {
		'name_one': 'thomas l leach',
		'name_two': 'thomas luther leach', 
		'expected': True, 
		'description': 'thomas l leach comparison with article'
	},
    {
		'name_one': 'thomas l quay',
		'name_two': 'thomas lavelle quay', 
		'expected': True, 
		'description': 'thomas l quay comparison with article'
	},
    {
		'name_one': 'thomas l savage',
		'name_two': 'thomas laman savage', 
		'expected': True, 
		'description': 'thomas l savage comparison with article'
	},
    {
		'name_one': 'thomas l wade, jr',
		'name_two': 'thomas leonard wade', 
		'expected': True, 
		'description': 'thomas l wade, jr comparison with article'
	},
    {
		'name_one': 'thomas l wilson',
		'name_two': 'thomas leslie wilson', 
		'expected': True, 
		'description': 'thomas l wilson comparison with article'
	},
    {
		'name_one': 'thomas l york',
		'name_two': 'thomas lenoir york', 
		'expected': True, 
		'description': 'thomas l york comparison with article'
	},
    {
		'name_one': 'thomas la saine',
		'name_two': 'thomas a. lasaine', 
		'expected': True, 
		'description': 'thomas la saine comparison with article'
	},
    {
		'name_one': 'thomas lauritsen',
		'name_two': 'thomas lauritsen', 
		'expected': True, 
		'description': 'thomas lauritsen comparison with article'
	},
    {
		'name_one': 'thomas lee bahler',
		'name_two': 'thomas l. bahler', 
		'expected': True, 
		'description': 'thomas lee bahler comparison with article'
	},
    {
		'name_one': 'thomas n lewis, n',
		'name_two': 'thomas mcdowell nelson lewis', 
		'expected': True, 
		'description': 'thomas n lewis, n comparison with article'
	},
    {
		'name_one': 'thomas o martin',
		'name_two': 'thomas leroy martin', 
		'expected': False, 
		'description': 'thomas o martin comparison with article'
	},
    {
		'name_one': 'thomas r kinney',
		'name_two': 'thomas dearman kinney', 
		'expected': False, 
		'description': 'thomas r kinney comparison with article'
	},
    {
		'name_one': 'thomas s lee',
		'name_two': 'thomas seymour lee', 
		'expected': True, 
		'description': 'thomas s lee comparison with article'
	},
    {
		'name_one': 'thomas s leith',
		'name_two': 'thomas seeter leith', 
		'expected': True, 
		'description': 'thomas s leith comparison with article'
	},
    {
		'name_one': 'thomas van voorhis',
		'name_two': 'thomas p. van voorhis', 
		'expected': True, 
		'description': 'thomas van voorhis comparison with article'
	},
    {
		'name_one': 'thomas vance',
		'name_two': 'thomas franklin vance', 
		'expected': True, 
		'description': 'thomas vance comparison with article'
	},
    {
		'name_one': 'thomas vance',
		'name_two': 'thomas hume vance', 
		'expected': True, 
		'description': 'thomas vance comparison with article'
	},
    {
		'name_one': 'thomas w lambe',
		'name_two': 'thomas william lambe', 
		'expected': True, 
		'description': 'thomas w lambe comparison with article'
	},
    {
		'name_one': 'thomas w lester',
		'name_two': 'thomas william lester', 
		'expected': True, 
		'description': 'thomas w lester comparison with article'
	},
    {
		'name_one': 'thorstin larsen',
		'name_two': 'thornstein larsen', 
		'expected': True, 
		'description': 'thorstin larsen comparison with article'
	},
    {
		'name_one': 'thurman w van meter',
		'name_two': 'thurman w. van metre', 
		'expected': True, 
		'description': 'thurman w van meter comparison with article'
	},
    {
		'name_one': 'timothy f oleary',
		'name_two': 'timothy f. leary', 
		'expected': True, 
		'description': 'timothy f oleary comparison with article'
	},
    {
		'name_one': 'tom f lewis',
		'name_two': 'tom f. lewis', 
		'expected': True, 
		'description': 'tom f lewis comparison with article'
	},
    {
		'name_one': 'tourgee debose',
		'name_two': 'tourgee a. debose', 
		'expected': True, 
		'description': 'tourgee debose comparison with article'
	},
    {
		'name_one': 'tylene e dunning',
		'name_two': 'e. leon dunning', 
		'expected': False, 
		'description': 'tylene e dunning comparison with article'
	},
    {
		'name_one': 'ulysses s vance',
		'name_two': 'ulysses vance', 
		'expected': True, 
		'description': 'ulysses s vance comparison with article'
	},
    {
		'name_one': 'una l robinson',
		'name_two': 'una lane robinson', 
		'expected': True, 
		'description': 'una l robinson comparison with article'
	},
    {
		'name_one': 'v lewis bassie',
		'name_two': 'v. lewis bassie', 
		'expected': True, 
		'description': 'v lewis bassie comparison with article'
	},
    {
		'name_one': 'valentine listard pinacoli',
		'name_two': 'valentine leotard pinacoli', 
		'expected': True, 
		'description': 'valentine listard pinacoli comparison with article'
	},
    {
		'name_one': 'van d smith',
		'name_two': 'samuel van dyke smith', 
		'expected': True, 
		'description': 'van d smith comparison with article'
	},
    {
		'name_one': 'van d thompson',
		'name_two': 'van denman thompson', 
		'expected': True, 
		'description': 'van d thompson comparison with article'
	},
    {
		'name_one': 'van derek frechette',
		'name_two': 'van derck frechette', 
		'expected': True, 
		'description': 'van derek frechette comparison with article'
	},
    {
		'name_one': 'van duyn a miller',
		'name_two': 'lea van puymbroeck miller', 
		'expected': False, 
		'description': 'van duyn a miller comparison with article'
	},
    {
		'name_one': 'van kenyon',
		'name_two': 'van leslie kenyon', 
		'expected': True, 
		'description': 'van kenyon comparison with article'
	},
    {
		'name_one': 'van l kenyon',
		'name_two': 'van leslie kenyon', 
		'expected': True, 
		'description': 'van l kenyon comparison with article'
	},
    {
		'name_one': 'van moore',
		'name_two': 'grace van dyke more', 
		'expected': True, 
		'description': 'van moore comparison with article'
	},
    {
		'name_one': 'vanue b lacour',
		'name_two': 'vanue b. lacour', 
		'expected': True, 
		'description': 'vanue b lacour comparison with article'
	},
    {
		'name_one': 'velma r lemance',
		'name_two': 'robert mayer lumiansky', 
		'expected': False, 
		'description': 'velma r lemance comparison with article'
	},
    {
		'name_one': 'vern d delaney',
		'name_two': 'verne d. delaney', 
		'expected': True, 
		'description': 'vern d delaney comparison with article'
	},
    {
		'name_one': 'vernon a demars',
		'name_two': 'vernon a. demars', 
		'expected': True, 
		'description': 'vernon a demars comparison with article'
	},
    {
		'name_one': 'vernon leroy mckenzie',
		'name_two': 'vernon mckenzie', 
		'expected': True, 
		'description': 'vernon leroy mckenzie comparison with article'
	},
    {
		'name_one': 'vernon van dyke',
		'name_two': 'vernon van dyke', 
		'expected': True, 
		'description': 'vernon van dyke comparison with article'
	},
    {
		'name_one': 'vernon w. branko',
		'name_two': 'warren van bronkhorst', 
		'expected': False, 
		'description': 'vernon w. branko comparison with article'
	},
    {
		'name_one': 'victor f lenzen',
		'name_two': 'victor f. lenzen', 
		'expected': True, 
		'description': 'victor f lenzen comparison with article'
	},
    {
		'name_one': 'victor j lemke',
		'name_two': 'victor jacob lemke', 
		'expected': True, 
		'description': 'victor j lemke comparison with article'
	},
    {
		'name_one': 'victor lange',
		'name_two': 'victor lange', 
		'expected': True, 
		'description': 'victor lange comparison with article'
	},
    {
		'name_one': 'vila a deubach',
		'name_two': 'vila deubach', 
		'expected': True, 
		'description': 'vila a deubach comparison with article'
	},
    {
		'name_one': 'vincent f. polcyn',
		'name_two': 'vincent de paul', 
		'expected': False, 
		'description': 'vincent f. polcyn comparison with article'
	},
    {
		'name_one': 'vincent g dethier',
		'name_two': 'vincent gaston dethier', 
		'expected': True, 
		'description': 'vincent g dethier comparison with article'
	},
    {
		'name_one': 'vincent j derbes',
		'name_two': 'vincent joseph depaul derbes', 
		'expected': True, 
		'description': 'vincent j derbes comparison with article'
	},
    {
		'name_one': 'vincent t lathbury',
		'name_two': 'vincent t. lathbury', 
		'expected': True, 
		'description': 'vincent t lathbury comparison with article'
	},
    {
		'name_one': 'vincent v lanfear',
		'name_two': 'vincent w. lanfear', 
		'expected': False, 
		'description': 'vincent v lanfear comparison with article'
	},
    {
		'name_one': 'vinton u dearing',
		'name_two': 'vinton adams dearing', 
		'expected': False, 
		'description': 'vinton u dearing comparison with article'
	},
    {
		'name_one': 'viola e leaf',
		'name_two': 'einar leifson', 
		'expected': False, 
		'description': 'viola e leaf comparison with article'
	},
    {
		'name_one': 'viola vanketwick',
		'name_two': 'viola beck van katwijk', 
		'expected': True, 
		'description': 'viola vanketwick comparison with article'
	},
    {
		'name_one': 'virgil collins',
		'name_two': 'virgil lee collins', 
		'expected': True, 
		'description': 'virgil collins comparison with article'
	},
    {
		'name_one': 'virgil s lequire',
		'name_two': 'virgil s. lequire', 
		'expected': True, 
		'description': 'virgil s lequire comparison with article'
	},
    {
		'name_one': 'virginia a lane',
		'name_two': 'virginia lane', 
		'expected': True, 
		'description': 'virginia a lane comparison with article'
	},
    {
		'name_one': 'virginia e denker',
		'name_two': 'erich dinkier', 
		'expected': True, 
		'description': 'virginia e denker comparison with article'
	},
    {
		'name_one': 'virginia hamilton',
		'name_two': 'virginia van der veer hamilton', 
		'expected': True, 
		'description': 'virginia hamilton comparison with article'
	},
    {
		'name_one': 'virginia harris',
		'name_two': 'virginia lee harris', 
		'expected': True, 
		'description': 'virginia harris comparison with article'
	},
    {
		'name_one': 'virginia lee guernsey',
		'name_two': 'james lee guernsey', 
		'expected': False, 
		'description': 'virginia lee guernsey comparison with article'
	},
    {
		'name_one': 'virginia lee harrison',
		'name_two': 'virginia harrison', 
		'expected': True, 
		'description': 'virginia lee harrison comparison with article'
	},
    {
		'name_one': 'vito a vanoni',
		'name_two': 'vito a. vanoni', 
		'expected': True, 
		'description': 'vito a vanoni comparison with article'
	},
    {
		'name_one': 'vivan l strickland',
		'name_two': 'vivan lewis strickland', 
		'expected': True, 
		'description': 'vivan l strickland comparison with article'
	},
    {
		'name_one': 'vladimir de\'lisovoy',
		'name_two': 'vladimir delissovoy', 
		'expected': True, 
		'description': 'vladimir de\'lisovoy comparison with article'
	},
    {
		'name_one': 'w a dence',
		'name_two': 'wilford a. dence', 
		'expected': True, 
		'description': 'w a dence comparison with article'
	},
    {
		'name_one': 'w e dennis',
		'name_two': 'wilfred sidney dennis', 
		'expected': False, 
		'description': 'w e dennis comparison with article'
	},
    {
		'name_one': 'w everett derryberry',
		'name_two': 'everett derryberry', 
		'expected': True, 
		'description': 'w everett derryberry comparison with article'
	},
    {
		'name_one': 'w lamark dodd',
		'name_two': 'lamar dodd', 
		'expected': True, 
		'description': 'w lamark dodd comparison with article'
	},
    {
		'name_one': 'w lee culp',
		'name_two': 'w. lee culp', 
		'expected': True, 
		'description': 'w lee culp comparison with article'
	},
    {
		'name_one': 'w leighton collins',
		'name_two': 'w. leighton collins', 
		'expected': True, 
		'description': 'w leighton collins comparison with article'
	},
    {
		'name_one': 'w leo batten',
		'name_two': 'w. leo batten', 
		'expected': True, 
		'description': 'w leo batten comparison with article'
	},
    {
		'name_one': 'w s laughlin',
		'name_two': 'william s. laughlin', 
		'expected': True, 
		'description': 'w s laughlin comparison with article'
	},
    {
		'name_one': 'w wayne dedman',
		'name_two': 'w. wayne dedman', 
		'expected': True, 
		'description': 'w wayne dedman comparison with article'
	},
    {
		'name_one': 'w. james leach',
		'name_two': 'w. james leach', 
		'expected': True, 
		'description': 'w. james leach comparison with article'
	},
    {
		'name_one': 'waiten l kindelsperger',
		'name_two': 'walter lewis kindelsperger', 
		'expected': False, 
		'description': 'waiten l kindelsperger comparison with article'
	},
    {
		'name_one': 'waldo e lessenger',
		'name_two': 'w. e. lessenger', 
		'expected': True, 
		'description': 'waldo e lessenger comparison with article'
	},
    {
		'name_one': 'walken l whetten',
		'name_two': 'nathan laselle whetten', 
		'expected': False, 
		'description': 'walken l whetten comparison with article'
	},
    {
		'name_one': 'wallace m lansford',
		'name_two': 'wallace monroe lansford', 
		'expected': True, 
		'description': 'wallace m lansford comparison with article'
	},
    {
		'name_one': 'walter a lawrance',
		'name_two': 'walter albert lawrance', 
		'expected': True, 
		'description': 'walter a lawrance comparison with article'
	},
    {
		'name_one': 'walter d leavitt',
		'name_two': 'walter d. leavitt', 
		'expected': True, 
		'description': 'walter d leavitt comparison with article'
	},
    {
		'name_one': 'walter d lewis',
		'name_two': 'walter richard lewis', 
		'expected': False, 
		'description': 'walter d lewis comparison with article'
	},
    {
		'name_one': 'walter daykin',
		'name_two': 'walter lesley daykin', 
		'expected': True, 
		'description': 'walter daykin comparison with article'
	},
    {
		'name_one': 'walter dewey',
		'name_two': 'walter safford dewey', 
		'expected': True, 
		'description': 'walter dewey comparison with article'
	},
    {
		'name_one': 'walter e larmie',
		'name_two': 'walter esmond larmie', 
		'expected': True, 
		'description': 'walter e larmie comparison with article'
	},
    {
		'name_one': 'walter ehrenberg',
		'name_two': 'walter j. derenberg', 
		'expected': True, 
		'description': 'walter ehrenberg comparison with article'
	},
    {
		'name_one': 'walter f clark',
		'name_two': 'walter leighton clark', 
		'expected': False, 
		'description': 'walter f clark comparison with article'
	},
    {
		'name_one': 'walter f dearborn',
		'name_two': 'walter fenno dearborn', 
		'expected': True, 
		'description': 'walter f dearborn comparison with article'
	},
    {
		'name_one': 'walter h delaplane',
		'name_two': 'walter harold delaplane', 
		'expected': True, 
		'description': 'walter h delaplane comparison with article'
	},
    {
		'name_one': 'walter j lebeau',
		'name_two': 'walter le beau', 
		'expected': True, 
		'description': 'walter j lebeau comparison with article'
	},
    {
		'name_one': 'walter j lemke',
		'name_two': 'walter john lemke', 
		'expected': True, 
		'description': 'walter j lemke comparison with article'
	},
    {
		'name_one': 'walter l coplin',
		'name_two': 'walter lee coplin', 
		'expected': True, 
		'description': 'walter l coplin comparison with article'
	},
    {
		'name_one': 'walter l moore',
		'name_two': 'walter lee moore', 
		'expected': True, 
		'description': 'walter l moore comparison with article'
	},
    {
		'name_one': 'walter l roosa',
		'name_two': 'walter laidlaw roosa', 
		'expected': True, 
		'description': 'walter l roosa comparison with article'
	},
    {
		'name_one': 'walter l simmons',
		'name_two': 'walter lee simmons', 
		'expected': True, 
		'description': 'walter l simmons comparison with article'
	},
    {
		'name_one': 'walter l thomas',
		'name_two': 'walter lee thomas', 
		'expected': True, 
		'description': 'walter l thomas comparison with article'
	},
    {
		'name_one': 'walter l van gothen',
		'name_two': 'armand l. degaetano', 
		'expected': False, 
		'description': 'walter l van gothen comparison with article'
	},
    {
		'name_one': 'walter l vandervest',
		'name_two': 'walter louis vandervest', 
		'expected': True, 
		'description': 'walter l vandervest comparison with article'
	},
    {
		'name_one': 'walter l wilson',
		'name_two': 'walter leroy wilson', 
		'expected': True, 
		'description': 'walter l wilson comparison with article'
	},
    {
		'name_one': 'walter l winkenwerder',
		'name_two': 'walter lafollette winkenwerder', 
		'expected': True, 
		'description': 'walter l winkenwerder comparison with article'
	},
    {
		'name_one': 'walter la pierre',
		'name_two': 'walter a. la pierre', 
		'expected': True, 
		'description': 'walter la pierre comparison with article'
	},
    {
		'name_one': 'walter langston',
		'name_two': 'walter stanley langston', 
		'expected': True, 
		'description': 'walter langston comparison with article'
	},
    {
		'name_one': 'walter lay',
		'name_two': 'walter edwin lay', 
		'expected': True, 
		'description': 'walter lay comparison with article'
	},
    {
		'name_one': 'walter lee green',
		'name_two': 'hampton lee green', 
		'expected': False, 
		'description': 'walter lee green comparison with article'
	},
    {
		'name_one': 'walter m denny',
		'name_two': 'walter lee denny', 
		'expected': False, 
		'description': 'walter m denny comparison with article'
	},
    {
		'name_one': 'walter m langford',
		'name_two': 'walter m. langford', 
		'expected': True, 
		'description': 'walter m langford comparison with article'
	},
    {
		'name_one': 'walter marshall',
		'name_two': 'walter vancleve marshall', 
		'expected': True, 
		'description': 'walter marshall comparison with article'
	},
    {
		'name_one': 'walter putz',
		'name_two': 'walter van de putte', 
		'expected': True, 
		'description': 'walter putz comparison with article'
	},
    {
		'name_one': 'walter s lake',
		'name_two': 'walter sidelinger lake', 
		'expected': True, 
		'description': 'walter s lake comparison with article'
	},
    {
		'name_one': 'walter summers',
		'name_two': 'walter lee summers', 
		'expected': True, 
		'description': 'walter summers comparison with article'
	},
    {
		'name_one': 'walter v price',
		'name_two': 'walter van price', 
		'expected': True, 
		'description': 'walter v price comparison with article'
	},
    {
		'name_one': 'walter v riley',
		'name_two': 'walter lee riley', 
		'expected': False, 
		'description': 'walter v riley comparison with article'
	},
    {
		'name_one': 'walter w leavitt',
		'name_two': 'harold walter leavitt', 
		'expected': False, 
		'description': 'walter w leavitt comparison with article'
	},
    {
		'name_one': 'walter wilkins',
		'name_two': 'walter laroy wilkins', 
		'expected': True, 
		'description': 'walter wilkins comparison with article'
	},
    {
		'name_one': 'ward lambert',
		'name_two': 'ward lewis lambert', 
		'expected': True, 
		'description': 'ward lambert comparison with article'
	},
    {
		'name_one': 'warren k lewis',
		'name_two': 'warren kendall lewis', 
		'expected': True, 
		'description': 'warren k lewis comparison with article'
	},
    {
		'name_one': 'warren l rosen',
		'name_two': 'warren leucht rosen', 
		'expected': True, 
		'description': 'warren l rosen comparison with article'
	},
    {
		'name_one': 'warren law',
		'name_two': 'warren aubrey law', 
		'expected': True, 
		'description': 'warren law comparison with article'
	},
    {
		'name_one': 'warren lee slagle',
		'name_two': 'warren lee slagle', 
		'expected': True, 
		'description': 'warren lee slagle comparison with article'
	},
    {
		'name_one': 'warren m deacon',
		'name_two': 'warren mcallister deacon', 
		'expected': True, 
		'description': 'warren m deacon comparison with article'
	},
    {
		'name_one': 'warren m. lee',
		'name_two': 'warren lee', 
		'expected': True, 
		'description': 'warren m. lee comparison with article'
	},
    {
		'name_one': 'warren w delapp',
		'name_two': 'warren w. delapp', 
		'expected': True, 
		'description': 'warren w delapp comparison with article'
	},
    {
		'name_one': 'warren w leigh',
		'name_two': 'warren w. leigh', 
		'expected': True, 
		'description': 'warren w leigh comparison with article'
	},
    {
		'name_one': 'washburne shipton',
		'name_two': 'washburn denning shipton', 
		'expected': True, 
		'description': 'washburne shipton comparison with article'
	},
    {
		'name_one': 'wassily w leontief',
		'name_two': 'wassily w. leontief', 
		'expected': True, 
		'description': 'wassily w leontief comparison with article'
	},
    {
		'name_one': 'wayne a lee',
		'name_two': 'wayne a. lee', 
		'expected': True, 
		'description': 'wayne a lee comparison with article'
	},
    {
		'name_one': 'wayne a r leys',
		'name_two': 'wayne a. r. leys', 
		'expected': True, 
		'description': 'wayne a r leys comparison with article'
	},
    {
		'name_one': 'wayne d sieh',
		'name_two': 'wayne delbert sieh', 
		'expected': True, 
		'description': 'wayne d sieh comparison with article'
	},
    {
		'name_one': 'wayne dennis',
		'name_two': 'wayne dennis', 
		'expected': True, 
		'description': 'wayne dennis comparison with article'
	},
    {
		'name_one': 'wayne m leitlinger',
		'name_two': 'joaquin mazdak luttinger', 
		'expected': False, 
		'description': 'wayne m leitlinger comparison with article'
	},
    {
		'name_one': 'webster w decker',
		'name_two': 'webster w. decker', 
		'expected': True, 
		'description': 'webster w decker comparison with article'
	},
    {
		'name_one': 'wendell m latimer',
		'name_two': 'wendell m. latimer', 
		'expected': True, 
		'description': 'wendell m latimer comparison with article'
	},
    {
		'name_one': 'werner f. leopold',
		'name_two': 'werner f. leopold', 
		'expected': True, 
		'description': 'werner f. leopold comparison with article'
	},
    {
		'name_one': 'werner levi',
		'name_two': 'werner levi', 
		'expected': True, 
		'description': 'werner levi comparison with article'
	},
    {
		'name_one': 'wesley e lewis',
		'name_two': 'wesley lewis', 
		'expected': True, 
		'description': 'wesley e lewis comparison with article'
	},
    {
		'name_one': 'weston l murray',
		'name_two': 'weston lafayette murray', 
		'expected': True, 
		'description': 'weston l murray comparison with article'
	},
    {
		'name_one': 'wilber l beauchamp',
		'name_two': 'wilbur lee beauchamp', 
		'expected': True, 
		'description': 'wilber l beauchamp comparison with article'
	},
    {
		'name_one': 'wilbur d johnston',
		'name_two': 'wilbur dexter johnston', 
		'expected': True, 
		'description': 'wilbur d johnston comparison with article'
	},
    {
		'name_one': 'wiley l housewright',
		'name_two': 'wiley lee housewright', 
		'expected': True, 
		'description': 'wiley l housewright comparison with article'
	},
    {
		'name_one': 'wilfid desmarais',
		'name_two': 'wilfrid desmarais', 
		'expected': True, 
		'description': 'wilfid desmarais comparison with article'
	},
    {
		'name_one': 'wilfred f langelier',
		'name_two': 'wilfred f. langelier', 
		'expected': True, 
		'description': 'wilfred f langelier comparison with article'
	},
    {
		'name_one': 'willard l rogers',
		'name_two': 'willard lewis rogers', 
		'expected': True, 
		'description': 'willard l rogers comparison with article'
	},
    {
		'name_one': 'willard oquinn',
		'name_two': 'willard van orman quine', 
		'expected': False, 
		'description': 'willard oquinn comparison with article'
	},
    {
		'name_one': 'willard t leeds',
		'name_two': 'willard l. leeds', 
		'expected': False, 
		'description': 'willard t leeds comparison with article'
	},
    {
		'name_one': 'willard van hazel',
		'name_two': 'willard van hazel', 
		'expected': True, 
		'description': 'willard van hazel comparison with article'
	},
    {
		'name_one': 'willem van wagtendonk',
		'name_two': 'willem johan van wagtendonk', 
		'expected': True, 
		'description': 'willem van wagtendonk comparison with article'
	},
    {
		'name_one': 'william a devine',
		'name_two': 'william a. devine', 
		'expected': True, 
		'description': 'william a devine comparison with article'
	},
    {
		'name_one': 'william a lewis',
		'name_two': 'william abbett lewis', 
		'expected': True, 
		'description': 'william a lewis comparison with article'
	},
    {
		'name_one': 'william a pace',
		'name_two': 'william leon pious', 
		'expected': False, 
		'description': 'william a pace comparison with article'
	},
    {
		'name_one': 'william a van heyn',
		'name_two': 'william a. venin', 
		'expected': False, 
		'description': 'william a van heyn comparison with article'
	},
    {
		'name_one': 'william a van winkle',
		'name_two': 'william alexander van winkle', 
		'expected': True, 
		'description': 'william a van winkle comparison with article'
	},
    {
		'name_one': 'william a. lamb',
		'name_two': 'c. a. lamb', 
		'expected': False, 
		'description': 'william a. lamb comparison with article'
	},
    {
		'name_one': 'william b lewis',
		'name_two': 'william benjamin lewis', 
		'expected': True, 
		'description': 'william b lewis comparison with article'
	},
    {
		'name_one': 'william c de vane',
		'name_two': 'william clyde de vane', 
		'expected': True, 
		'description': 'william c de vane comparison with article'
	},
    {
		'name_one': 'william c de vane',
		'name_two': 'william clyde devane', 
		'expected': True, 
		'description': 'william c de vane comparison with article'
	},
    {
		'name_one': 'william c deamer',
		'name_two': 'william c. deamer', 
		'expected': True, 
		'description': 'william c deamer comparison with article'
	},
    {
		'name_one': 'william c deveny',
		'name_two': 'william c. deveny', 
		'expected': True, 
		'description': 'william c deveny comparison with article'
	},
    {
		'name_one': 'william c lam',
		'name_two': 'william c. lam', 
		'expected': True, 
		'description': 'william c lam comparison with article'
	},
    {
		'name_one': 'william c. dew',
		'name_two': 'william c. dew', 
		'expected': True, 
		'description': 'william c. dew comparison with article'
	},
    {
		'name_one': 'william carmichael',
		'name_two': 'william lawson carmichael', 
		'expected': True, 
		'description': 'william carmichael comparison with article'
	},
    {
		'name_one': 'william coggshall',
		'name_two': 'william lamar coggshall', 
		'expected': True, 
		'description': 'william coggshall comparison with article'
	},
    {
		'name_one': 'william collins',
		'name_two': 'william lee collins', 
		'expected': True, 
		'description': 'william collins comparison with article'
	},
    {
		'name_one': 'william d barns',
		'name_two': 'william derrick barns', 
		'expected': True, 
		'description': 'william d barns comparison with article'
	},
    {
		'name_one': 'william d denny',
		'name_two': 'william d. denny', 
		'expected': True, 
		'description': 'william d denny comparison with article'
	},
    {
		'name_one': 'william d ladd',
		'name_two': 'william edwards ladd', 
		'expected': False, 
		'description': 'william d ladd comparison with article'
	},
    {
		'name_one': 'william d larson',
		'name_two': 'william d. larson', 
		'expected': True, 
		'description': 'william d larson comparison with article'
	},
    {
		'name_one': 'william d legg, sr',
		'name_two': 'kenneth d. legge', 
		'expected': False, 
		'description': 'william d legg, sr comparison with article'
	},
    {
		'name_one': 'william d lewis',
		'name_two': 'william ditto lewis', 
		'expected': True, 
		'description': 'william d lewis comparison with article'
	},
    {
		'name_one': 'william d metz',
		'name_two': 'william dewitt metz', 
		'expected': True, 
		'description': 'william d metz comparison with article'
	},
    {
		'name_one': 'william d perry',
		'name_two': 'william decatur perry', 
		'expected': True, 
		'description': 'william d perry comparison with article'
	},
    {
		'name_one': 'william d van vorst',
		'name_two': 'william d. van vorst', 
		'expected': True, 
		'description': 'william d van vorst comparison with article'
	},
    {
		'name_one': 'william daniel lee',
		'name_two': 'william daniel lee', 
		'expected': True, 
		'description': 'william daniel lee comparison with article'
	},
    {
		'name_one': 'william de feo',
		'name_two': 'william f. macfee', 
		'expected': True, 
		'description': 'william de feo comparison with article'
	},
    {
		'name_one': 'william dehorn',
		'name_two': 'william dehorn', 
		'expected': True, 
		'description': 'william dehorn comparison with article'
	},
    {
		'name_one': 'william dickerman',
		'name_two': 'william b. deichmann', 
		'expected': False, 
		'description': 'william dickerman comparison with article'
	},
    {
		'name_one': 'william e de turk',
		'name_two': 'william ernest deturk', 
		'expected': True, 
		'description': 'william e de turk comparison with article'
	},
    {
		'name_one': 'william e decker',
		'name_two': 'william decker', 
		'expected': True, 
		'description': 'william e decker comparison with article'
	},
    {
		'name_one': 'william e lawrence',
		'name_two': 'william ewart lawrence', 
		'expected': True, 
		'description': 'william e lawrence comparison with article'
	},
    {
		'name_one': 'william e merritt',
		'name_two': 'william wellesley demeritt', 
		'expected': False, 
		'description': 'william e merritt comparison with article'
	},
    {
		'name_one': 'william e p clark',
		'name_two': 'william e. de clark', 
		'expected': True, 
		'description': 'william e p clark comparison with article'
	},
    {
		'name_one': 'william f lahey',
		'name_two': 'william f. lahey', 
		'expected': True, 
		'description': 'william f lahey comparison with article'
	},
    {
		'name_one': 'william f lamb',
		'name_two': 'william f. lamb', 
		'expected': True, 
		'description': 'william f lamb comparison with article'
	},
    {
		'name_one': 'william g dent',
		'name_two': 'robert william dent', 
		'expected': False, 
		'description': 'william g dent comparison with article'
	},
    {
		'name_one': 'william g lennox',
		'name_two': 'william gordon lennox', 
		'expected': True, 
		'description': 'william g lennox comparison with article'
	},
    {
		'name_one': 'william g leonard',
		'name_two': 'guy william leonard', 
		'expected': True, 
		'description': 'william g leonard comparison with article'
	},
    {
		'name_one': 'william g robertson',
		'name_two': 'william van bogaert robertson', 
		'expected': False, 
		'description': 'william g robertson comparison with article'
	},
    {
		'name_one': 'william h crum',
		'name_two': 'william leonard crum', 
		'expected': False, 
		'description': 'william h crum comparison with article'
	},
    {
		'name_one': 'william h garrett',
		'name_two': 'william lawrence garrott', 
		'expected': False, 
		'description': 'william h garrett comparison with article'
	},
    {
		'name_one': 'william h lavell',
		'name_two': 'hugh rodman leavell', 
		'expected': False, 
		'description': 'william h lavell comparison with article'
	},
    {
		'name_one': 'william h lawrence',
		'name_two': 'william henry lawrence', 
		'expected': True, 
		'description': 'william h lawrence comparison with article'
	},
    {
		'name_one': 'william h leary',
		'name_two': 'wllliam h. leary', 
		'expected': True, 
		'description': 'william h leary comparison with article'
	},
    {
		'name_one': 'william h meyer',
		'name_two': 'william h. lewis meyer', 
		'expected': True, 
		'description': 'william h meyer comparison with article'
	},
    {
		'name_one': 'william h seward',
		'name_two': 'herbert lee seward', 
		'expected': False, 
		'description': 'william h seward comparison with article'
	},
    {
		'name_one': 'william j dean',
		'name_two': 'william j. dean', 
		'expected': True, 
		'description': 'william j dean comparison with article'
	},
    {
		'name_one': 'william j dehaas',
		'name_two': 'j. anton de haas', 
		'expected': False, 
		'description': 'william j dehaas comparison with article'
	},
    {
		'name_one': 'william j dempsey',
		'name_two': 'william j. dempsey', 
		'expected': True, 
		'description': 'william j dempsey comparison with article'
	},
    {
		'name_one': 'william j lee',
		'name_two': 'william j. lee', 
		'expected': True, 
		'description': 'william j lee comparison with article'
	},
    {
		'name_one': 'william j leipertz',
		'name_two': 'vernon william lippard', 
		'expected': False, 
		'description': 'william j leipertz comparison with article'
	},
    {
		'name_one': 'william j leonard',
		'name_two': 'william j. leonard', 
		'expected': True, 
		'description': 'william j leonard comparison with article'
	},
    {
		'name_one': 'william johnston',
		'name_two': 'william denis johnston', 
		'expected': True, 
		'description': 'william johnston comparison with article'
	},
    {
		'name_one': 'william l burlison',
		'name_two': 'william leonidas burlison', 
		'expected': True, 
		'description': 'william l burlison comparison with article'
	},
    {
		'name_one': 'william l cory',
		'name_two': 'william leonard cory', 
		'expected': True, 
		'description': 'william l cory comparison with article'
	},
    {
		'name_one': 'william l doyle',
		'name_two': 'william lewis doyle', 
		'expected': True, 
		'description': 'william l doyle comparison with article'
	},
    {
		'name_one': 'william l duren',
		'name_two': 'william larkin duren', 
		'expected': True, 
		'description': 'william l duren comparison with article'
	},
    {
		'name_one': 'william l gardner',
		'name_two': 'william lawrence gardner', 
		'expected': True, 
		'description': 'william l gardner comparison with article'
	},
    {
		'name_one': 'william l king',
		'name_two': 'william lewis king', 
		'expected': True, 
		'description': 'william l king comparison with article'
	},
    {
		'name_one': 'william l lane',
		'name_two': 'laurence william lane', 
		'expected': True, 
		'description': 'william l lane comparison with article'
	},
    {
		'name_one': 'william l langer',
		'name_two': 'william leonard langer', 
		'expected': True, 
		'description': 'william l langer comparison with article'
	},
    {
		'name_one': 'william l lester',
		'name_two': 'william l. lester', 
		'expected': True, 
		'description': 'william l lester comparison with article'
	},
    {
		'name_one': 'william l lomey',
		'name_two': 'william l. lamey', 
		'expected': True, 
		'description': 'william l lomey comparison with article'
	},
    {
		'name_one': 'william l sachse',
		'name_two': 'william lewis sachse', 
		'expected': True, 
		'description': 'william l sachse comparison with article'
	},
    {
		'name_one': 'william l schwartz',
		'name_two': 'william leonard schwartz', 
		'expected': True, 
		'description': 'william l schwartz comparison with article'
	},
    {
		'name_one': 'william l wheeler',
		'name_two': 'william lawrence wheeler', 
		'expected': True, 
		'description': 'william l wheeler comparison with article'
	},
    {
		'name_one': 'william l wiley',
		'name_two': 'william leon wiley', 
		'expected': True, 
		'description': 'william l wiley comparison with article'
	},
    {
		'name_one': 'william l wylie',
		'name_two': 'william leroy wylie', 
		'expected': True, 
		'description': 'william l wylie comparison with article'
	},
    {
		'name_one': 'william lafferty',
		'name_two': 'william a. lafferty', 
		'expected': True, 
		'description': 'william lafferty comparison with article'
	},
    {
		'name_one': 'william lagrange',
		'name_two': 'william f. lagrange', 
		'expected': True, 
		'description': 'william lagrange comparison with article'
	},
    {
		'name_one': 'william lamont',
		'name_two': 'william hayes fogg lamont', 
		'expected': True, 
		'description': 'william lamont comparison with article'
	},
    {
		'name_one': 'william land',
		'name_two': 'william m. landau', 
		'expected': True, 
		'description': 'william land comparison with article'
	},
    {
		'name_one': 'william landeen',
		'name_two': 'william m. landeen', 
		'expected': True, 
		'description': 'william landeen comparison with article'
	},
    {
		'name_one': 'william langford',
		'name_two': 'william s. langford', 
		'expected': True, 
		'description': 'william langford comparison with article'
	},
    {
		'name_one': 'william lee',
		'name_two': 'james william lee', 
		'expected': True, 
		'description': 'william lee comparison with article'
	},
    {
		'name_one': 'william leo lucey',
		'name_two': 'william l. lucey', 
		'expected': True, 
		'description': 'william leo lucey comparison with article'
	},
    {
		'name_one': 'william lewis',
		'name_two': 'ben william lewis', 
		'expected': True, 
		'description': 'william lewis comparison with article'
	},
    {
		'name_one': 'william m dey',
		'name_two': 'william morton dey', 
		'expected': True, 
		'description': 'william m dey comparison with article'
	},
    {
		'name_one': 'william m laub',
		'name_two': 'william t. laube', 
		'expected': False, 
		'description': 'william m laub comparison with article'
	},
    {
		'name_one': 'william miller',
		'name_two': 'william lee miller', 
		'expected': True, 
		'description': 'william miller comparison with article'
	},
    {
		'name_one': 'william n lacey',
		'name_two': 'william n. lacey', 
		'expected': True, 
		'description': 'william n lacey comparison with article'
	},
    {
		'name_one': 'william n leonard',
		'name_two': 'william n. leonard', 
		'expected': True, 
		'description': 'william n leonard comparison with article'
	},
    {
		'name_one': 'william o. dewey',
		'name_two': 'osee hughes dewey', 
		'expected': False, 
		'description': 'william o. dewey comparison with article'
	},
    {
		'name_one': 'william p delaney',
		'name_two': 'william p. delaney', 
		'expected': True, 
		'description': 'william p delaney comparison with article'
	},
    {
		'name_one': 'william p lehrer',
		'name_two': 'william p. lehrer', 
		'expected': True, 
		'description': 'william p lehrer comparison with article'
	},
    {
		'name_one': 'william r de valdez',
		'name_two': 'william belcher ballis', 
		'expected': False, 
		'description': 'william r de valdez comparison with article'
	},
    {
		'name_one': 'william r dennes',
		'name_two': 'william r. dennes', 
		'expected': True, 
		'description': 'william r dennes comparison with article'
	},
    {
		'name_one': 'william r devine',
		'name_two': 'william r. divine', 
		'expected': True, 
		'description': 'william r devine comparison with article'
	},
    {
		'name_one': 'william roberts',
		'name_two': 'william lewis roberts', 
		'expected': True, 
		'description': 'william roberts comparison with article'
	},
    {
		'name_one': 'william s la sor, jr',
		'name_two': 'w. s. lasor', 
		'expected': True, 
		'description': 'william s la sor, jr comparison with article'
	},
    {
		'name_one': 'william s levings',
		'name_two': 'william s. levings', 
		'expected': True, 
		'description': 'william s levings comparison with article'
	},
    {
		'name_one': 'william s root',
		'name_two': 'william dean rutz', 
		'expected': False, 
		'description': 'william s root comparison with article'
	},
    {
		'name_one': 'william stephen walker',
		'name_two': 'stephen leonard walker', 
		'expected': False, 
		'description': 'william stephen walker comparison with article'
	},
    {
		'name_one': 'william sullivan',
		'name_two': 'william lawrence sullivan', 
		'expected': True, 
		'description': 'william sullivan comparison with article'
	},
    {
		'name_one': 'william t kolb',
		'name_two': 'william lester kolb', 
		'expected': False, 
		'description': 'william t kolb comparison with article'
	},
    {
		'name_one': 'william t laprade',
		'name_two': 'william thomas laprade', 
		'expected': True, 
		'description': 'william t laprade comparison with article'
	},
    {
		'name_one': 'william t lentz',
		'name_two': 'william jacoby lentz', 
		'expected': False, 
		'description': 'william t lentz comparison with article'
	},
    {
		'name_one': 'william v chandler',
		'name_two': 'william von chandler', 
		'expected': True, 
		'description': 'william v chandler comparison with article'
	},
    {
		'name_one': 'william v lambert',
		'name_two': 'william v. lambert', 
		'expected': True, 
		'description': 'william v lambert comparison with article'
	},
    {
		'name_one': 'william van camp',
		'name_two': 'william morris van camp', 
		'expected': True, 
		'description': 'william van camp comparison with article'
	},
    {
		'name_one': 'william van parker',
		'name_two': 'william vann parker', 
		'expected': True, 
		'description': 'william van parker comparison with article'
	},
    {
		'name_one': 'william van tassel',
		'name_two': 'william van tassel', 
		'expected': True, 
		'description': 'william van tassel comparison with article'
	},
    {
		'name_one': 'willie lee bonner',
		'name_two': 'lee bonar', 
		'expected': True, 
		'description': 'willie lee bonner comparison with article'
	},
    {
		'name_one': 'wilmer l sibbet',
		'name_two': 'wilmer lawrence sibbitt', 
		'expected': True, 
		'description': 'wilmer l sibbet comparison with article'
	},
    {
		'name_one': 'wilson c ladue',
		'name_two': 'wilson c. ladue', 
		'expected': True, 
		'description': 'wilson c ladue comparison with article'
	},
    {
		'name_one': 'wilson e langley',
		'name_two': 'wilson d. langley', 
		'expected': False, 
		'description': 'wilson e langley comparison with article'
	},
    {
		'name_one': 'wilson l miser',
		'name_two': 'wilson lee miser', 
		'expected': True, 
		'description': 'wilson l miser comparison with article'
	},
    {
		'name_one': 'winford l sharp',
		'name_two': 'winford lee sharp', 
		'expected': True, 
		'description': 'winford l sharp comparison with article'
	},
    {
		'name_one': 'winfred p lehmann',
		'name_two': 'winfred p. lehmann', 
		'expected': True, 
		'description': 'winfred p lehmann comparison with article'
	},
    {
		'name_one': 'winiferd m leiby',
		'name_two': 'lester m. libo', 
		'expected': False, 
		'description': 'winiferd m leiby comparison with article'
	},
    {
		'name_one': 'winifred v shields',
		'name_two': 'currin vance shields', 
		'expected': False, 
		'description': 'winifred v shields comparison with article'
	},
    {
		'name_one': 'winston l brembeck',
		'name_two': 'winston lamont brembeck', 
		'expected': True, 
		'description': 'winston l brembeck comparison with article'
	},
    {
		'name_one': 'wm a lessa',
		'name_two': 'william a. lessa', 
		'expected': True, 
		'description': 'wm a lessa comparison with article'
	},
    {
		'name_one': 'wm van a jr clark, jr',
		'name_two': 'william van alan clark', 
		'expected': True, 
		'description': 'wm van a jr clark, jr comparison with article'
	},
    {
		'name_one': 'wm w sanderson',
		'name_two': 'wiley devere sanderson', 
		'expected': False, 
		'description': 'wm w sanderson comparison with article'
	},
    {
		'name_one': 'wm. lester jordan',
		'name_two': 'lester jordan', 
		'expected': True, 
		'description': 'wm. lester jordan comparison with article'
	},
    {
		'name_one': 'yvonne m cam',
		'name_two': 'lucien m. lecam', 
		'expected': False, 
		'description': 'yvonne m cam comparison with article'
	},
    {
		'name_one': 'zebulon b vance',
		'name_two': 'zeb vance', 
		'expected': True, 
		'description': 'zebulon b vance comparison with article'
	},
    {
		'name_one': 'zelma b leonhard',
		'name_two': 'zelma b. leonhard', 
		'expected': True, 
		'description': 'zelma b leonhard comparison with article'
	},
    {
		'name_one': 'zens l smith',
		'name_two': 'zens lawrence smith', 
		'expected': True, 
		'description': 'zens l smith comparison with article'
	},
    {
		'name_one': 'a john vounie',
		'name_two': 'john j. a. devenny', 
		'expected': True, 
		'description': 'a john vounie comparison with article'
	},
    {
		'name_one': 'albert renzi',
		'name_two': 'albert bernhardi van rennes', 
		'expected': True, 
		'description': 'albert renzi comparison with article'
	},
    {
		'name_one': 'alfred von geldern',
		'name_two': 'alfred gellhorn', 
		'expected': True, 
		'description': 'alfred von geldern comparison with article'
	},
    {
		'name_one': 'clifford mays',
		'name_two': 'clifford j. lemay', 
		'expected': True, 
		'description': 'clifford mays comparison with article'
	},
    {
		'name_one': 'helan francest lauterer',
		'name_two': 'helen forrest lauterer', 
		'expected': True, 
		'description': 'helan francest lauterer comparison with article'
	},
    {
		'name_one': 'henry p lane, jr',
		'name_two': 'henry p. lange', 
		'expected': False, 
		'description': 'henry p lane, jr comparison with article'
	},
    {
		'name_one': 'irving large',
		'name_two': 'irving d. lorge', 
		'expected': True, 
		'description': 'irving large comparison with article'
	},
    {
		'name_one': 'john w leslie',
		'name_two': 'wolf leslau', 
		'expected': False, 
		'description': 'john w leslie comparison with article'
	},
    {
		'name_one': 'joseph panta',
		'name_two': 'joseph della penta', 
		'expected': True, 
		'description': 'joseph panta comparison with article'
	},
    {
		'name_one': 'joseph w beck',
		'name_two': 'joseph van derbeek', 
		'expected': True, 
		'description': 'joseph w beck comparison with article'
	},
    {
		'name_one': 'louis depolito',
		'name_two': 'robert louis politzer', 
		'expected': False, 
		'description': 'louis depolito comparison with article'
	},
    {
		'name_one': 'martin lisan',
		'name_two': 'martin lessen', 
		'expected': True, 
		'description': 'martin lisan comparison with article'
	},
    {
		'name_one': 'morton levy',
		'name_two': 'martin j. levy', 
		'expected': False, 
		'description': 'morton levy comparison with article'
	},
    {
		'name_one': 'theodore b ley',
		'name_two': 'theodore delay', 
		'expected': True, 
		'description': 'theodore b ley comparison with article'
	},
    {
		'name_one': 'victor j cassidy',
		'name_two': 'julian victor langmead casserley', 
		'expected': True, 
		'description': 'victor j cassidy comparison with article'
	},
]
