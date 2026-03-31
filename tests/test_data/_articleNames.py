"""This file has a list of article name comparisons and the expected outcome.
These have been individually looked at by a real person to determine the 
expected outcome of each. The current version of NameComparator has a high 
level of accuracy at predicting the expected outcome, though it is not 
perfect."""

articleNames = [
    {
		'input': 'a bertram lemon;a. bertram lemon', 
		'expected': True, 
		'description': 'a bertram lemon comparison with article'
	},
    {
		'input': 'a c la follette;arthur c. la follette', 
		'expected': True, 
		'description': 'a c la follette comparison with article'
	},
    {
		'input': 'a harold lancour;harold lancour', 
		'expected': True, 
		'description': 'a harold lancour comparison with article'
	},
    {
		'input': 'a henry detweiler;albert henry detweiler', 
		'expected': True, 
		'description': 'a henry detweiler comparison with article'
	},
    {
		'input': 'a laurence mortensen;alfred laurence mortensen', 
		'expected': True, 
		'description': 'a laurence mortensen comparison with article'
	},
    {
		'input': 'a lee dunlap;archibald lee dunlap', 
		'expected': True, 
		'description': 'a lee dunlap comparison with article'
	},
    {
		'input': 'a leland beam;a. leland beam', 
		'expected': True, 
		'description': 'a leland beam comparison with article'
	},
    {
		'input': 'a leo oppenheim;adolf leo oppenheim', 
		'expected': True, 
		'description': 'a leo oppenheim comparison with article'
	},
    {
		'input': 'a m de la torre;antonio marcial de la torre', 
		'expected': True, 
		'description': 'a m de la torre comparison with article'
	},
    {
		'input': 'a michael deluca;a. michael de luca', 
		'expected': True, 
		'description': 'a michael deluca comparison with article'
	},
    {
		'input': 'a willis dearing;a. willis dearing', 
		'expected': True, 
		'description': 'a willis dearing comparison with article'
	},
    {
		'input': 'aaron donnelly;aaron van donnelly', 
		'expected': True, 
		'description': 'aaron donnelly comparison with article'
	},
    {
		'input': 'abba p lerner;abba p. lerner', 
		'expected': True, 
		'description': 'abba p lerner comparison with article'
	},
    {
		'input': 'able levitt;abel levitt', 
		'expected': True, 
		'description': 'able levitt comparison with article'
	},
    {
		'input': 'abraham h levy;abraham h. levy', 
		'expected': True, 
		'description': 'abraham h levy comparison with article'
	},
    {
		'input': 'abraham levinson;abraham levinson', 
		'expected': True, 
		'description': 'abraham levinson comparison with article'
	},
    {
		'input': 'abram l sachar;abram leon sachar', 
		'expected': True, 
		'description': 'abram l sachar comparison with article'
	},
    {
		'input': 'abram william vander meer;abram w. vandermeer', 
		'expected': True, 
		'description': 'abram william vander meer comparison with article'
	},
    {
		'input': 'ada lee hawkins;ada hawkins', 
		'expected': True, 
		'description': 'ada lee hawkins comparison with article'
	},
    {
		'input': 'adah lewis;adah lewis', 
		'expected': True, 
		'description': 'adah lewis comparison with article'
	},
    {
		'input': 'addison e lee;addison e. lee', 
		'expected': True, 
		'description': 'addison e lee comparison with article'
	},
    {
		'input': 'adelaide e deters;emma e. deters', 
		'expected': False, 
		'description': 'adelaide e deters comparison with article'
	},
    {
		'input': 'adelle h land;adelle h. land', 
		'expected': True, 
		'description': 'adelle h land comparison with article'
	},
    {
		'input': 'adolph desanctis;adolph g. desanctis', 
		'expected': True, 
		'description': 'adolph desanctis comparison with article'
	},
    {
		'input': 'adolph dettloff;adolph mansen dettloff', 
		'expected': True, 
		'description': 'adolph dettloff comparison with article'
	},
    {
		'input': 'adolph ladru jensen;adolph ladru jensen', 
		'expected': True, 
		'description': 'adolph ladru jensen comparison with article'
	},
    {
		'input': 'adolph leschnitzer;adolf f. leschnitzer', 
		'expected': True, 
		'description': 'adolph leschnitzer comparison with article'
	},
    {
		'input': 'adrian r legault;adrian r. legault', 
		'expected': True, 
		'description': 'adrian r legault comparison with article'
	},
    {
		'input': 'agnes gregory;agnes lee gregory', 
		'expected': True, 
		'description': 'agnes gregory comparison with article'
	},
    {
		'input': 'agnes k michels;agnes kirsopp lake michels', 
		'expected': True, 
		'description': 'agnes k michels comparison with article'
	},
    {
		'input': 'agnes m. larson;agnes m. larson', 
		'expected': True, 
		'description': 'agnes m. larson comparison with article'
	},
    {
		'input': 'agnes o leindorff;agnes olson leindorff', 
		'expected': True, 
		'description': 'agnes o leindorff comparison with article'
	},
    {
		'input': 'alan v mcgee;alan van keuren mcgee', 
		'expected': True, 
		'description': 'alan v mcgee comparison with article'
	},
    {
		'input': 'albert a la plante, a. jr;albert aurel la plante', 
		'expected': True, 
		'description': 'albert a la plante, a. jr comparison with article'
	},
    {
		'input': 'albert b m lewis;albert dale milton lewis', 
		'expected': True, 
		'description': 'albert b m lewis comparison with article'
	},
    {
		'input': 'albert c vandusen;albert clarence van dusen', 
		'expected': True, 
		'description': 'albert c vandusen comparison with article'
	},
    {
		'input': 'albert d kirwan;albert dennis kirwan', 
		'expected': True, 
		'description': 'albert d kirwan comparison with article'
	},
    {
		'input': 'albert d lebau;albert c. baugh', 
		'expected': False, 
		'description': 'albert d lebau comparison with article'
	},
    {
		'input': 'albert degroat;albert degroat', 
		'expected': True, 
		'description': 'albert degroat comparison with article'
	},
    {
		'input': 'albert delisle;albert l. delisle', 
		'expected': True, 
		'description': 'albert delisle comparison with article'
	},
    {
		'input': 'albert e babb;albert leslie babb', 
		'expected': False, 
		'description': 'albert e babb comparison with article'
	},
    {
		'input': 'albert fritz;karl albert kurt von fritz', 
		'expected': True, 
		'description': 'albert fritz comparison with article'
	},
    {
		'input': 'albert hyler;albert leroy hilliard', 
		'expected': False, 
		'description': 'albert hyler comparison with article'
	},
    {
		'input': 'albert j latham;albert j. latham', 
		'expected': True, 
		'description': 'albert j latham comparison with article'
	},
    {
		'input': 'albert l demaree;albert lowther demaree', 
		'expected': True, 
		'description': 'albert l demaree comparison with article'
	},
    {
		'input': 'albert l franzke;albert leonard franzke', 
		'expected': True, 
		'description': 'albert l franzke comparison with article'
	},
    {
		'input': 'albert l hoffman;elbert lee hoffman', 
		'expected': True, 
		'description': 'albert l hoffman comparison with article'
	},
    {
		'input': 'albert l leduc, jr;albert l. leduc', 
		'expected': True, 
		'description': 'albert l leduc, jr comparison with article'
	},
    {
		'input': 'albert l sturm;albert lee sturm', 
		'expected': True, 
		'description': 'albert l sturm comparison with article'
	},
    {
		'input': 'albert laubengayer;albert w. laubengayer', 
		'expected': True, 
		'description': 'albert laubengayer comparison with article'
	},
    {
		'input': 'albert lazan;albert lazan', 
		'expected': True, 
		'description': 'albert lazan comparison with article'
	},
    {
		'input': 'albert le mieux;albert a lemieux', 
		'expected': True, 
		'description': 'albert le mieux comparison with article'
	},
    {
		'input': 'albert le roy taylor;albert leroy taylor', 
		'expected': True, 
		'description': 'albert le roy taylor comparison with article'
	},
    {
		'input': 'albert levine;samuel albert levine', 
		'expected': True, 
		'description': 'albert levine comparison with article'
	},
    {
		'input': 'albert levy;albert w. levi', 
		'expected': True, 
		'description': 'albert levy comparison with article'
	},
    {
		'input': 'albert r lamb;albert r. lamb', 
		'expected': True, 
		'description': 'albert r lamb comparison with article'
	},
    {
		'input': 'albert r lang;albert ray lang', 
		'expected': True, 
		'description': 'albert r lang comparison with article'
	},
    {
		'input': 'albert s dealaman, jr;gellert s. alleman', 
		'expected': True, 
		'description': 'albert s dealaman, jr comparison with article'
	},
    {
		'input': 'albert s lada;milan s. la du', 
		'expected': False, 
		'description': 'albert s lada comparison with article'
	},
    {
		'input': 'albert w van ness;albert w. van ness', 
		'expected': True, 
		'description': 'albert w van ness comparison with article'
	},
    {
		'input': 'alberta k levine;albert k. levine', 
		'expected': True, 
		'description': 'alberta k levine comparison with article'
	},
    {
		'input': 'alberta m price;m. lawrence price', 
		'expected': False, 
		'description': 'alberta m price comparison with article'
	},
    {
		'input': 'alden crittenden;alden larue crittenden', 
		'expected': True, 
		'description': 'alden crittenden comparison with article'
	},
    {
		'input': 'aldon s lang;aldon s. lang', 
		'expected': True, 
		'description': 'aldon s lang comparison with article'
	},
    {
		'input': 'alex lawrie;alex laurie', 
		'expected': True, 
		'description': 'alex lawrie comparison with article'
	},
    {
		'input': 'alex s levens;alexander s. levens', 
		'expected': True, 
		'description': 'alex s levens comparison with article'
	},
    {
		'input': 'alexander a rowell, sr;gillie a. larew', 
		'expected': False, 
		'description': 'alexander a rowell, sr comparison with article'
	},
    {
		'input': 'alexander h lighton;alexander h. leighton', 
		'expected': True, 
		'description': 'alexander h lighton comparison with article'
	},
    {
		'input': 'alexander kreisler;alexander von kreisler', 
		'expected': True, 
		'description': 'alexander kreisler comparison with article'
	},
    {
		'input': 'alexander l geisenheimer;alexander leopold geisenheimer', 
		'expected': True, 
		'description': 'alexander l geisenheimer comparison with article'
	},
    {
		'input': 'alexander leitch;alexander leitch', 
		'expected': True, 
		'description': 'alexander leitch comparison with article'
	},
    {
		'input': 'alexander levine;alexander levine', 
		'expected': True, 
		'description': 'alexander levine comparison with article'
	},
    {
		'input': 'alexander popov;alexander van popov', 
		'expected': True, 
		'description': 'alexander popov comparison with article'
	},
    {
		'input': 'alfa c latzke;alpha corinne latzke', 
		'expected': True, 
		'description': 'alfa c latzke comparison with article'
	},
    {
		'input': 'alfred a devellio;claude alvin villee', 
		'expected': False, 
		'description': 'alfred a devellio comparison with article'
	},
    {
		'input': 'alfred biggs;alfred debard biggs', 
		'expected': True, 
		'description': 'alfred biggs comparison with article'
	},
    {
		'input': 'alfred d longhouse;alfred delbert longhouse', 
		'expected': True, 
		'description': 'alfred d longhouse comparison with article'
	},
    {
		'input': 'alfred d simpson;alfred dexter simpson', 
		'expected': True, 
		'description': 'alfred d simpson comparison with article'
	},
    {
		'input': 'alfred l burt;alfred leroy burt', 
		'expected': True, 
		'description': 'alfred l burt comparison with article'
	},
    {
		'input': 'alfred l clapp;alfred lester clapp', 
		'expected': True, 
		'description': 'alfred l clapp comparison with article'
	},
    {
		'input': 'alfred l edwards;alfred leroy edwards', 
		'expected': True, 
		'description': 'alfred l edwards comparison with article'
	},
    {
		'input': 'alfred l gausewitz;alfred leroy gausewitz', 
		'expected': True, 
		'description': 'alfred l gausewitz comparison with article'
	},
    {
		'input': 'alfred l lomax;alfred lewis lomax', 
		'expected': True, 
		'description': 'alfred l lomax comparison with article'
	},
    {
		'input': 'alfred l miller;alfred lawrence miller', 
		'expected': True, 
		'description': 'alfred l miller comparison with article'
	},
    {
		'input': 'alfred l wilds;alfred lawrence wilds', 
		'expected': True, 
		'description': 'alfred l wilds comparison with article'
	},
    {
		'input': 'alfred lande;alfred lande', 
		'expected': True, 
		'description': 'alfred lande comparison with article'
	},
    {
		'input': 'alfred leimdorfer;alfred leimdorfer', 
		'expected': True, 
		'description': 'alfred leimdorfer comparison with article'
	},
    {
		'input': 'alfred m lee;alfred mcclung lee', 
		'expected': True, 
		'description': 'alfred m lee comparison with article'
	},
    {
		'input': 'alfred s lazarus;alfred s. lazarus', 
		'expected': True, 
		'description': 'alfred s lazarus comparison with article'
	},
    {
		'input': 'alfred schmied;alfred leo schmied', 
		'expected': True, 
		'description': 'alfred schmied comparison with article'
	},
    {
		'input': 'alfred vacchio;alfred del vecchio', 
		'expected': True, 
		'description': 'alfred vacchio comparison with article'
	},
    {
		'input': 'alice j vandermeulen;alice john vandermeulen', 
		'expected': True, 
		'description': 'alice j vandermeulen comparison with article'
	},
    {
		'input': 'alice l hodgson;linwood lamb hodgdon', 
		'expected': False, 
		'description': 'alice l hodgson comparison with article'
	},
    {
		'input': 'alice lazerowitz;alice loman ambrose lazerowitz', 
		'expected': True, 
		'description': 'alice lazerowitz comparison with article'
	},
    {
		'input': 'alice m demeritt;m. mauritia', 
		'expected': True, 
		'description': 'alice m demeritt comparison with article'
	},
    {
		'input': 'alice m vau de voort;alice van de voort', 
		'expected': True, 
		'description': 'alice m vau de voort comparison with article'
	},
    {
		'input': 'alice w leland;thomas w. leland', 
		'expected': False, 
		'description': 'alice w leland comparison with article'
	},
    {
		'input': 'allan c de lacy;allan clark delacy', 
		'expected': True, 
		'description': 'allan c de lacy comparison with article'
	},
    {
		'input': 'allan l strout;alan lang strout', 
		'expected': True, 
		'description': 'allan l strout comparison with article'
	},
    {
		'input': 'allen a lasko;alvin a. lasko', 
		'expected': True, 
		'description': 'allen a lasko comparison with article'
	},
    {
		'input': 'allen b lambdin;allen b. lambdin', 
		'expected': True, 
		'description': 'allen b lambdin comparison with article'
	},
    {
		'input': 'allen d cooper;allen lamar cooper', 
		'expected': False, 
		'description': 'allen d cooper comparison with article'
	},
    {
		'input': 'allen l king;allen lewis king', 
		'expected': True, 
		'description': 'allen l king comparison with article'
	},
    {
		'input': 'allen l lorincz;allan levente lorincz', 
		'expected': True, 
		'description': 'allen l lorincz comparison with article'
	},
    {
		'input': 'allen lein;allen lein', 
		'expected': True, 
		'description': 'allen lein comparison with article'
	},
    {
		'input': 'alonzo a leifeste;a. a. liefeste', 
		'expected': True, 
		'description': 'alonzo a leifeste comparison with article'
	},
    {
		'input': 'alva l kerbow;alva lee kerbow', 
		'expected': True, 
		'description': 'alva l kerbow comparison with article'
	},
    {
		'input': 'alva leroy prickett;alva leroy prickett', 
		'expected': True, 
		'description': 'alva leroy prickett comparison with article'
	},
    {
		'input': 'alvah l newcomb;alvah lay newcomb', 
		'expected': True, 
		'description': 'alvah l newcomb comparison with article'
	},
    {
		'input': 'alvan l barach;alvan leroy barach', 
		'expected': True, 
		'description': 'alvan l barach comparison with article'
	},
    {
		'input': 'alvin d etlers;alvin derald etler', 
		'expected': True, 
		'description': 'alvin d etlers comparison with article'
	},
    {
		'input': 'alvin g law;alvin g. law', 
		'expected': True, 
		'description': 'alvin g law comparison with article'
	},
    {
		'input': 'alvin l lang;alvin l. lang', 
		'expected': True, 
		'description': 'alvin l lang comparison with article'
	},
    {
		'input': 'amance a desautels;agnes de st louis', 
		'expected': False, 
		'description': 'amance a desautels comparison with article'
	},
    {
		'input': 'amanda l forkner;hamden landon forkner', 
		'expected': False, 
		'description': 'amanda l forkner comparison with article'
	},
    {
		'input': 'amelia delrio;amelia a. de del rio', 
		'expected': True, 
		'description': 'amelia delrio comparison with article'
	},
    {
		'input': 'amos p leib;amos p. leib', 
		'expected': True, 
		'description': 'amos p leib comparison with article'
	},
    {
		'input': 'amy l turner;amy lee turner', 
		'expected': True, 
		'description': 'amy l turner comparison with article'
	},
    {
		'input': 'anastasia vanbebber;anastasia van bebber', 
		'expected': True, 
		'description': 'anastasia vanbebber comparison with article'
	},
    {
		'input': 'anastasia vanburkalow;anastasia van burkalow', 
		'expected': True, 
		'description': 'anastasia vanburkalow comparison with article'
	},
    {
		'input': 'andre c leveque;andre camille leveque', 
		'expected': True, 
		'description': 'andre c leveque comparison with article'
	},
    {
		'input': 'andre von gronicka;andre von gronicka', 
		'expected': True, 
		'description': 'andre von gronicka comparison with article'
	},
    {
		'input': 'andree de c heller;andree heller', 
		'expected': True, 
		'description': 'andree de c heller comparison with article'
	},
    {
		'input': 'andrew l papailion;laura van pappelendam', 
		'expected': False, 
		'description': 'andrew l papailion comparison with article'
	},
    {
		'input': 'andrew malon;peter andrew van der meulen', 
		'expected': True, 
		'description': 'andrew malon comparison with article'
	},
    {
		'input': 'andrew p van hook;andrew p. van hook', 
		'expected': True, 
		'description': 'andrew p van hook comparison with article'
	},
    {
		'input': 'andrew p vanderpoel;priscilla paine van der poel', 
		'expected': False, 
		'description': 'andrew p vanderpoel comparison with article'
	},
    {
		'input': 'andrew w lawson, jr;andrew werner lawson', 
		'expected': True, 
		'description': 'andrew w lawson, jr comparison with article'
	},
    {
		'input': 'angel delrio;angel del rio', 
		'expected': True, 
		'description': 'angel delrio comparison with article'
	},
    {
		'input': 'angela d oglesby;dwayne la vergne oglesby', 
		'expected': False, 
		'description': 'angela d oglesby comparison with article'
	},
    {
		'input': 'angela g lardner;gerhart ladner', 
		'expected': True, 
		'description': 'angela g lardner comparison with article'
	},
    {
		'input': 'angelina la piana;angeline la piana', 
		'expected': True, 
		'description': 'angelina la piana comparison with article'
	},
    {
		'input': 'angelo degennaro;angelo a. de gennaro', 
		'expected': True, 
		'description': 'angelo degennaro comparison with article'
	},
    {
		'input': 'angie t king;angie lena turner king', 
		'expected': True, 
		'description': 'angie t king comparison with article'
	},
    {
		'input': 'ann deeds;ann catherine deeds', 
		'expected': True, 
		'description': 'ann deeds comparison with article'
	},
    {
		'input': 'ann k ann k,;nancy van anne', 
		'expected': False, 
		'description': 'ann k ann k, comparison with article'
	},
    {
		'input': 'ann l diem;william l. deam', 
		'expected': False, 
		'description': 'ann l diem comparison with article'
	},
    {
		'input': 'ann lankford;ann elizabeth lankford', 
		'expected': True, 
		'description': 'ann lankford comparison with article'
	},
    {
		'input': 'ann s lettle;elizabeth ann liddle', 
		'expected': False, 
		'description': 'ann s lettle comparison with article'
	},
    {
		'input': 'anna c lageragen;anna constantia lagergren', 
		'expected': True, 
		'description': 'anna c lageragen comparison with article'
	},
    {
		'input': 'anna e. lange;e. o. lange', 
		'expected': False, 
		'description': 'anna e. lange comparison with article'
	},
    {
		'input': 'anna j de armond;anna janney dearmond', 
		'expected': True, 
		'description': 'anna j de armond comparison with article'
	},
    {
		'input': 'anna l cochran;elmer lendell cockrum', 
		'expected': False, 
		'description': 'anna l cochran comparison with article'
	},
    {
		'input': 'anna p lauterbur;anna p. lauterbur', 
		'expected': True, 
		'description': 'anna p lauterbur comparison with article'
	},
    {
		'input': 'anne b lay;anne brownlee lay', 
		'expected': True, 
		'description': 'anne b lay comparison with article'
	},
    {
		'input': 'anne l lewis;anne louise lewis', 
		'expected': True, 
		'description': 'anne l lewis comparison with article'
	},
    {
		'input': 'annita delano;annita delano', 
		'expected': True, 
		'description': 'annita delano comparison with article'
	},
    {
		'input': 'anthonie van harreveld, jr;anthonie van harreveld', 
		'expected': True, 
		'description': 'anthonie van harreveld, jr comparison with article'
	},
    {
		'input': 'anthony de michele;laurence anthony michel', 
		'expected': True, 
		'description': 'anthony de michele comparison with article'
	},
    {
		'input': 'anthony de oreo;gerard anthony de oreo', 
		'expected': True, 
		'description': 'anthony de oreo comparison with article'
	},
    {
		'input': 'anthony j defilipps;a. j. defilipps', 
		'expected': True, 
		'description': 'anthony j defilipps comparison with article'
	},
    {
		'input': 'anthony j del mastro;anthony j. del mastro', 
		'expected': True, 
		'description': 'anthony j del mastro comparison with article'
	},
    {
		'input': 'anthony l turkevich;anthony leonid turkevich', 
		'expected': True, 
		'description': 'anthony l turkevich comparison with article'
	},
    {
		'input': 'anton lang;anton lang', 
		'expected': True, 
		'description': 'anton lang comparison with article'
	},
    {
		'input': 'arch lauterer;arch lauterer', 
		'expected': True, 
		'description': 'arch lauterer comparison with article'
	},
    {
		'input': 'archbald laforte;archibald smith foord', 
		'expected': False, 
		'description': 'archbald laforte comparison with article'
	},
    {
		'input': 'archibald s dean;archibald s. dean', 
		'expected': True, 
		'description': 'archibald s dean comparison with article'
	},
    {
		'input': 'archie l leonard;archie leroy leonard', 
		'expected': True, 
		'description': 'archie l leonard comparison with article'
	},
    {
		'input': 'ariel f lausche;luverne frederick lausche', 
		'expected': False, 
		'description': 'ariel f lausche comparison with article'
	},
    {
		'input': 'arman j lawrence;armon jay lawrence', 
		'expected': True, 
		'description': 'arman j lawrence comparison with article'
	},
    {
		'input': 'armand desautel;armand h. desautels', 
		'expected': True, 
		'description': 'armand desautel comparison with article'
	},
    {
		'input': 'arnand b leavelle;arnaud b. leavelle', 
		'expected': True, 
		'description': 'arnand b leavelle comparison with article'
	},
    {
		'input': 'arno t lenz;arno thomas lenz', 
		'expected': True, 
		'description': 'arno t lenz comparison with article'
	},
    {
		'input': 'arnold lazerow;arnold lazarow', 
		'expected': True, 
		'description': 'arnold lazerow comparison with article'
	},
    {
		'input': 'arnold w lapp;arnold w. lapp', 
		'expected': True, 
		'description': 'arnold w lapp comparison with article'
	},
    {
		'input': 'arthur a lewis;arthur o. lewis', 
		'expected': False, 
		'description': 'arthur a lewis comparison with article'
	},
    {
		'input': 'arthur b leible;arthur blank leible', 
		'expected': True, 
		'description': 'arthur b leible comparison with article'
	},
    {
		'input': 'arthur b lewis;arthur beverly lewis', 
		'expected': True, 
		'description': 'arthur b lewis comparison with article'
	},
    {
		'input': 'arthur brandon;arthur leon brandon', 
		'expected': True, 
		'description': 'arthur brandon comparison with article'
	},
    {
		'input': 'arthur d butterfield;arthur dexter butterfield', 
		'expected': True, 
		'description': 'arthur d butterfield comparison with article'
	},
    {
		'input': 'arthur d les?eut;arthur m. lassek', 
		'expected': False, 
		'description': 'arthur d les?eut comparison with article'
	},
    {
		'input': 'arthur d moore;arthur dearth moore', 
		'expected': True, 
		'description': 'arthur d moore comparison with article'
	},
    {
		'input': 'arthur delez;arthur louis delez', 
		'expected': True, 
		'description': 'arthur delez comparison with article'
	},
    {
		'input': 'arthur denney;arthur c. denney', 
		'expected': True, 
		'description': 'arthur denney comparison with article'
	},
    {
		'input': 'arthur e lamb;arthur e. lamb', 
		'expected': True, 
		'description': 'arthur e lamb comparison with article'
	},
    {
		'input': 'arthur f deam;arthur f. deam', 
		'expected': True, 
		'description': 'arthur f deam comparison with article'
	},
    {
		'input': 'arthur f watkins;arthur lancaster watkins', 
		'expected': False, 
		'description': 'arthur f watkins comparison with article'
	},
    {
		'input': 'arthur h leavitt;arthur h. leavitt', 
		'expected': True, 
		'description': 'arthur h leavitt comparison with article'
	},
    {
		'input': 'arthur herbert levy, jr;arthur herbert levy', 
		'expected': True, 
		'description': 'arthur herbert levy, jr comparison with article'
	},
    {
		'input': 'arthur j lopovsky;arthur j. lapovsky', 
		'expected': True, 
		'description': 'arthur j lopovsky comparison with article'
	},
    {
		'input': 'arthur l albert;arthur lemuel albert', 
		'expected': True, 
		'description': 'arthur l albert comparison with article'
	},
    {
		'input': 'arthur l anderson;arthur lawrence anderson', 
		'expected': True, 
		'description': 'arthur l anderson comparison with article'
	},
    {
		'input': 'arthur l benton;arthur lester benton', 
		'expected': True, 
		'description': 'arthur l benton comparison with article'
	},
    {
		'input': 'arthur l derring;arthur l. deering', 
		'expected': True, 
		'description': 'arthur l derring comparison with article'
	},
    {
		'input': 'arthur l goodrich;arthur leonard goodrich', 
		'expected': True, 
		'description': 'arthur l goodrich comparison with article'
	},
    {
		'input': 'arthur l neal;arthur leslie neal', 
		'expected': True, 
		'description': 'arthur l neal comparison with article'
	},
    {
		'input': 'arthur l searles;arthur langley searles', 
		'expected': True, 
		'description': 'arthur l searles comparison with article'
	},
    {
		'input': 'arthur l svenson;arthur lee svenson', 
		'expected': True, 
		'description': 'arthur l svenson comparison with article'
	},
    {
		'input': 'arthur l tatum;arthur lawrie tatum', 
		'expected': True, 
		'description': 'arthur l tatum comparison with article'
	},
    {
		'input': 'arthur l townsend;arthur lawrence townsend', 
		'expected': True, 
		'description': 'arthur l townsend comparison with article'
	},
    {
		'input': 'arthur l vollman;ludwig von sallmann', 
		'expected': False, 
		'description': 'arthur l vollman comparison with article'
	},
    {
		'input': 'arthur l young;arthur leighton young', 
		'expected': True, 
		'description': 'arthur l young comparison with article'
	},
    {
		'input': 'arthur lamay;mark arthur may', 
		'expected': True, 
		'description': 'arthur lamay comparison with article'
	},
    {
		'input': 'arthur larson;arthur larson', 
		'expected': True, 
		'description': 'arthur larson comparison with article'
	},
    {
		'input': 'arthur lawrence bakke;arthur lawrence bakke', 
		'expected': True, 
		'description': 'arthur lawrence bakke comparison with article'
	},
    {
		'input': 'arthur lenhoff;arthur lenhoff', 
		'expected': True, 
		'description': 'arthur lenhoff comparison with article'
	},
    {
		'input': 'arthur lesser;arthur lesser', 
		'expected': True, 
		'description': 'arthur lesser comparison with article'
	},
    {
		'input': 'arthur lewis;arthur lewis', 
		'expected': True, 
		'description': 'arthur lewis comparison with article'
	},
    {
		'input': 'arthur prince;arthur leslie prince', 
		'expected': True, 
		'description': 'arthur prince comparison with article'
	},
    {
		'input': 'arthur r fisher;arthur lawrence fisher', 
		'expected': False, 
		'description': 'arthur r fisher comparison with article'
	},
    {
		'input': 'arthur s levine;arthur sidney levine', 
		'expected': True, 
		'description': 'arthur s levine comparison with article'
	},
    {
		'input': 'arthur van mehren;arthur taylor von mehren', 
		'expected': True, 
		'description': 'arthur van mehren comparison with article'
	},
    {
		'input': 'arthur w leighton;arthur w. leighton', 
		'expected': True, 
		'description': 'arthur w leighton comparison with article'
	},
    {
		'input': 'arvo vanalstyne;arvo van alstyne', 
		'expected': True, 
		'description': 'arvo vanalstyne comparison with article'
	},
    {
		'input': 'ashton welsh;ashton leroy welsh', 
		'expected': True, 
		'description': 'ashton welsh comparison with article'
	},
    {
		'input': 'aubrey landers;aubrey w. landers', 
		'expected': True, 
		'description': 'aubrey landers comparison with article'
	},
    {
		'input': 'august d lang;arch d. lang', 
		'expected': False, 
		'description': 'august d lang comparison with article'
	},
    {
		'input': 'august r leisner;a. roberts leisner', 
		'expected': True, 
		'description': 'august r leisner comparison with article'
	},
    {
		'input': 'augustin cosgrove;augustin lawrence cosgrove', 
		'expected': True, 
		'description': 'augustin cosgrove comparison with article'
	},
    {
		'input': 'austin lamont;austin lamont', 
		'expected': True, 
		'description': 'austin lamont comparison with article'
	},
    {
		'input': 'avis graham;avis exalee lair graham', 
		'expected': True, 
		'description': 'avis graham comparison with article'
	},
    {
		'input': 'babette levy;babette m. levy', 
		'expected': True, 
		'description': 'babette levy comparison with article'
	},
    {
		'input': 'barbara lee;barbara lee', 
		'expected': True, 
		'description': 'barbara lee comparison with article'
	},
    {
		'input': 'barboar l herrington;barbour lawson herrington', 
		'expected': True, 
		'description': 'barboar l herrington comparison with article'
	},
    {
		'input': 'barclay leathem;barclay s. leathem', 
		'expected': True, 
		'description': 'barclay leathem comparison with article'
	},
    {
		'input': 'barnes f lathrop;barnes f. lathrop', 
		'expected': True, 
		'description': 'barnes f lathrop comparison with article'
	},
    {
		'input': 'barnet m levy;barnet m. levy', 
		'expected': True, 
		'description': 'barnet m levy comparison with article'
	},
    {
		'input': 'basil l sherrill;basil lamar sherrill', 
		'expected': True, 
		'description': 'basil l sherrill comparison with article'
	},
    {
		'input': 'beatrice m la vigne;beatrice lavigne', 
		'expected': True, 
		'description': 'beatrice m la vigne comparison with article'
	},
    {
		'input': 'beatrice von keller;beatrice von keller', 
		'expected': True, 
		'description': 'beatrice von keller comparison with article'
	},
    {
		'input': 'beautine h de costa;beautine h. decosta', 
		'expected': True, 
		'description': 'beautine h de costa comparison with article'
	},
    {
		'input': 'ben f lemert;benjamin franklin lemert', 
		'expected': True, 
		'description': 'ben f lemert comparison with article'
	},
    {
		'input': 'ben l. love;ben del love', 
		'expected': True, 
		'description': 'ben l. love comparison with article'
	},
    {
		'input': 'benjamin averbook;benjamin lewis averbach', 
		'expected': False, 
		'description': 'benjamin averbook comparison with article'
	},
    {
		'input': 'benjamin d leith;benjamin donald leith', 
		'expected': True, 
		'description': 'benjamin d leith comparison with article'
	},
    {
		'input': 'benjamin h lehman;benjamin h. lehman', 
		'expected': True, 
		'description': 'benjamin h lehman comparison with article'
	},
    {
		'input': 'benjamin l smits;benjamin levi smits', 
		'expected': True, 
		'description': 'benjamin l smits comparison with article'
	},
    {
		'input': 'benjamin lease;benjamin lease', 
		'expected': True, 
		'description': 'benjamin lease comparison with article'
	},
    {
		'input': 'benjimine r lacy;benjamin rice lacy', 
		'expected': True, 
		'description': 'benjimine r lacy comparison with article'
	},
    {
		'input': 'benno landsberger;benno landsberger', 
		'expected': True, 
		'description': 'benno landsberger comparison with article'
	},
    {
		'input': 'benson j. lamp;benson j. lamp', 
		'expected': True, 
		'description': 'benson j. lamp comparison with article'
	},
    {
		'input': 'bernard h larsen, jr;bernard boysen larsen', 
		'expected': False, 
		'description': 'bernard h larsen, jr comparison with article'
	},
    {
		'input': 'bernard karten;bernard leon kartin', 
		'expected': True, 
		'description': 'bernard karten comparison with article'
	},
    {
		'input': 'bernard lander;bernard lander', 
		'expected': True, 
		'description': 'bernard lander comparison with article'
	},
    {
		'input': 'bernard lemann;bernard lemann', 
		'expected': True, 
		'description': 'bernard lemann comparison with article'
	},
    {
		'input': 'bernard levy;bernard levy', 
		'expected': True, 
		'description': 'bernard levy comparison with article'
	},
    {
		'input': 'bernard liebman;o. bernard leibman', 
		'expected': True, 
		'description': 'bernard liebman comparison with article'
	},
    {
		'input': 'bernhardt lemmel;bernhardt lemmel', 
		'expected': True, 
		'description': 'bernhardt lemmel comparison with article'
	},
    {
		'input': 'bernt o larson;bernt o. larson', 
		'expected': True, 
		'description': 'bernt o larson comparison with article'
	},
    {
		'input': 'bertha m levy;bertha marion levy', 
		'expected': True, 
		'description': 'bertha m levy comparison with article'
	},
    {
		'input': 'bertha v lederar;bertha v. lederer', 
		'expected': True, 
		'description': 'bertha v lederar comparison with article'
	},
    {
		'input': 'bertina laborde;bertina anne laborde', 
		'expected': True, 
		'description': 'bertina laborde comparison with article'
	},
    {
		'input': 'bertram levinson;bertram levinson', 
		'expected': True, 
		'description': 'bertram levinson comparison with article'
	},
    {
		'input': 'bessie g campbell;bessie lee gambrill', 
		'expected': False, 
		'description': 'bessie g campbell comparison with article'
	},
    {
		'input': 'betty a land;betty aiken land', 
		'expected': True, 
		'description': 'betty a land comparison with article'
	},
    {
		'input': 'betty c delavan;betty c. delavan', 
		'expected': True, 
		'description': 'betty c delavan comparison with article'
	},
    {
		'input': 'bevin lewis;bevan blau lewis', 
		'expected': True, 
		'description': 'bevin lewis comparison with article'
	},
    {
		'input': 'bianca del vecchio;bianca del vecchio', 
		'expected': True, 
		'description': 'bianca del vecchio comparison with article'
	},
    {
		'input': 'billy j van gundy;justine van gundy', 
		'expected': True, 
		'description': 'billy j van gundy comparison with article'
	},
    {
		'input': 'blaine de lancey;blaine delancey', 
		'expected': True, 
		'description': 'blaine de lancey comparison with article'
	},
    {
		'input': 'blake ragsdale von leer;blake ragsdale van leer', 
		'expected': True, 
		'description': 'blake ragsdale von leer comparison with article'
	},
    {
		'input': 'boni j delaureal;boni james delaureal', 
		'expected': True, 
		'description': 'boni j delaureal comparison with article'
	},
    {
		'input': 'boris leaf;boris leaf', 
		'expected': True, 
		'description': 'boris leaf comparison with article'
	},
    {
		'input': 'boris levinson;boris m. levinson', 
		'expected': True, 
		'description': 'boris levinson comparison with article'
	},
    {
		'input': 'borisz deballa;borisz de balla', 
		'expected': True, 
		'description': 'borisz deballa comparison with article'
	},
    {
		'input': 'boyd l o\'dell;boyd lee o\'dell', 
		'expected': True, 
		'description': 'boyd l o\'dell comparison with article'
	},
    {
		'input': 'bradley d thompson;bradley deforrest thompson', 
		'expected': True, 
		'description': 'bradley d thompson comparison with article'
	},
    {
		'input': 'bror l grondal;bror leonard grondal', 
		'expected': True, 
		'description': 'bror l grondal comparison with article'
	},
    {
		'input': 'bruce despelder;bruce e. despelder', 
		'expected': True, 
		'description': 'bruce despelder comparison with article'
	},
    {
		'input': 'bruce g dearing;bruce dearing', 
		'expected': True, 
		'description': 'bruce g dearing comparison with article'
	},
    {
		'input': 'bruce l cartter;bruce lanpher cartter', 
		'expected': True, 
		'description': 'bruce l cartter comparison with article'
	},
    {
		'input': 'bruce weidner;bruce van scoyoc weidner', 
		'expected': True, 
		'description': 'bruce weidner comparison with article'
	},
    {
		'input': 'brunell d faris;brunel debost faris', 
		'expected': True, 
		'description': 'brunell d faris comparison with article'
	},
    {
		'input': 'bryan c landreth;catherine landreth', 
		'expected': True, 
		'description': 'bryan c landreth comparison with article'
	},
    {
		'input': 'burtis lawson;burtis carl lawson', 
		'expected': True, 
		'description': 'burtis lawson comparison with article'
	},
    {
		'input': 'byron e lauer;bryon elmer lauer', 
		'expected': True, 
		'description': 'byron e lauer comparison with article'
	},
    {
		'input': 'byron l jr burford;bryon leslie burford', 
		'expected': True, 
		'description': 'byron l jr burford comparison with article'
	},
    {
		'input': 'c lee harwell;c. lee harwell', 
		'expected': True, 
		'description': 'c lee harwell comparison with article'
	},
    {
		'input': 'c leonard huskins;charles leonard huskins', 
		'expected': True, 
		'description': 'c leonard huskins comparison with article'
	},
    {
		'input': 'c lewis hafermekl;charles louis hafermehl', 
		'expected': True, 
		'description': 'c lewis hafermekl comparison with article'
	},
    {
		'input': 'c lowell lees;c. lowell lees', 
		'expected': True, 
		'description': 'c lowell lees comparison with article'
	},
    {
		'input': 'c marshall lee;c. marshall lee', 
		'expected': True, 
		'description': 'c marshall lee comparison with article'
	},
    {
		'input': 'c theodore larson;c. theodore larson', 
		'expected': True, 
		'description': 'c theodore larson comparison with article'
	},
    {
		'input': 'camile j le vois;camille joseph le vois', 
		'expected': True, 
		'description': 'camile j le vois comparison with article'
	},
    {
		'input': 'carl a leopold;aldo carl leopold', 
		'expected': True, 
		'description': 'carl a leopold comparison with article'
	},
    {
		'input': 'carl a. lamey;carl a. lamey', 
		'expected': True, 
		'description': 'carl a. lamey comparison with article'
	},
    {
		'input': 'carl de zeeuw;carl h. dezeeuw', 
		'expected': True, 
		'description': 'carl de zeeuw comparison with article'
	},
    {
		'input': 'carl e liangenhop;carl e. langenhop', 
		'expected': True, 
		'description': 'carl e liangenhop comparison with article'
	},
    {
		'input': 'carl frank lagler;karl f. lagler', 
		'expected': True, 
		'description': 'carl frank lagler comparison with article'
	},
    {
		'input': 'carl g debono;gabriel bonno', 
		'expected': True, 
		'description': 'carl g debono comparison with article'
	},
    {
		'input': 'carl g van buskirk;carl george van buskirk', 
		'expected': True, 
		'description': 'carl g van buskirk comparison with article'
	},
    {
		'input': 'carl h lenhart;carl h. lenhart', 
		'expected': True, 
		'description': 'carl h lenhart comparison with article'
	},
    {
		'input': 'carl l de graff;edwin charles greif', 
		'expected': False, 
		'description': 'carl l de graff comparison with article'
	},
    {
		'input': 'carl l gillies;carl lewis gillies', 
		'expected': True, 
		'description': 'carl l gillies comparison with article'
	},
    {
		'input': 'carl l heyerdahl;carl lewis heyerdahl', 
		'expected': True, 
		'description': 'carl l heyerdahl comparison with article'
	},
    {
		'input': 'carl l huffaker;carl leo huffaker', 
		'expected': True, 
		'description': 'carl l huffaker comparison with article'
	},
    {
		'input': 'carl landauer;carl landauer', 
		'expected': True, 
		'description': 'carl landauer comparison with article'
	},
    {
		'input': 'carl w lawton;carl william lawton', 
		'expected': True, 
		'description': 'carl w lawton comparison with article'
	},
    {
		'input': 'carl w schwette;karl de schweinitz', 
		'expected': False, 
		'description': 'carl w schwette comparison with article'
	},
    {
		'input': 'carlo l lastrucci;carlo l. lastrucci', 
		'expected': True, 
		'description': 'carlo l lastrucci comparison with article'
	},
    {
		'input': 'carlton h larrabee, male;carlton h. larrabee', 
		'expected': True, 
		'description': 'carlton h larrabee, male comparison with article'
	},
    {
		'input': 'carlyn c delavan;carlyn c. delavan', 
		'expected': True, 
		'description': 'carlyn c delavan comparison with article'
	},
    {
		'input': 'carmela d laskin;d. s. laskin', 
		'expected': False, 
		'description': 'carmela d laskin comparison with article'
	},
    {
		'input': 'carney landis;carney landis', 
		'expected': True, 
		'description': 'carney landis comparison with article'
	},
    {
		'input': 'caroline a lester;caroline a. lester', 
		'expected': True, 
		'description': 'caroline a lester comparison with article'
	},
    {
		'input': 'caroll meeks;carroll louis vanderslice meeks', 
		'expected': True, 
		'description': 'caroll meeks comparison with article'
	},
    {
		'input': 'carolyn l widmer;carolyn ladd widmer', 
		'expected': True, 
		'description': 'carolyn l widmer comparison with article'
	},
    {
		'input': 'carrol l. birch;carroll la fleur birch', 
		'expected': True, 
		'description': 'carrol l. birch comparison with article'
	},
    {
		'input': 'carroll l christenson;carroll lawrence christenson', 
		'expected': True, 
		'description': 'carroll l christenson comparison with article'
	},
    {
		'input': 'carroll l. mann;carroll lamb mann', 
		'expected': True, 
		'description': 'carroll l. mann comparison with article'
	},
    {
		'input': 'carroll v glines;carroll vane glines', 
		'expected': True, 
		'description': 'carroll v glines comparison with article'
	},
    {
		'input': 'carroll. l. shartle;carroll leonard shartle', 
		'expected': True, 
		'description': 'carroll. l. shartle comparison with article'
	},
    {
		'input': 'carter marshall, jr;carter lee marshall', 
		'expected': True, 
		'description': 'carter marshall, jr comparison with article'
	},
    {
		'input': 'catherine j phelps;catherine denny phelps', 
		'expected': False, 
		'description': 'catherine j phelps comparison with article'
	},
    {
		'input': 'catherine l lipscomb;winifred lawrence lipscomb', 
		'expected': False, 
		'description': 'catherine l lipscomb comparison with article'
	},
    {
		'input': 'catherine lawlor;anna catherine lawlor', 
		'expected': True, 
		'description': 'catherine lawlor comparison with article'
	},
    {
		'input': 'cecil y lang;cecil tavener lane', 
		'expected': False, 
		'description': 'cecil y lang comparison with article'
	},
    {
		'input': 'cecil y lang;cecil yelverton lang', 
		'expected': True, 
		'description': 'cecil y lang comparison with article'
	},
    {
		'input': 'cecile debanke;cecile de banke', 
		'expected': True, 
		'description': 'cecile debanke comparison with article'
	},
    {
		'input': 'cecilie leuchtenberger;cecilie leuchtenberger', 
		'expected': True, 
		'description': 'cecilie leuchtenberger comparison with article'
	},
    {
		'input': 'charle leonard lundin;charles leonard lundin', 
		'expected': True, 
		'description': 'charle leonard lundin comparison with article'
	},
    {
		'input': 'charles a lee;charles a. lee', 
		'expected': True, 
		'description': 'charles a lee comparison with article'
	},
    {
		'input': 'charles a nelson;charles leblanc nelson', 
		'expected': False, 
		'description': 'charles a nelson comparison with article'
	},
    {
		'input': 'charles a roover;raymond a. de roover', 
		'expected': False, 
		'description': 'charles a roover comparison with article'
	},
    {
		'input': 'charles b deibel;wallace b. diboll', 
		'expected': False, 
		'description': 'charles b deibel comparison with article'
	},
    {
		'input': 'charles c flick;charles lewis fluke', 
		'expected': False, 
		'description': 'charles c flick comparison with article'
	},
    {
		'input': 'charles c lasater;chas. crawford lasater', 
		'expected': True, 
		'description': 'charles c lasater comparison with article'
	},
    {
		'input': 'charles c lauritsen;charles christian lauritsen', 
		'expected': True, 
		'description': 'charles c lauritsen comparison with article'
	},
    {
		'input': 'charles c lawrence;charles e. lawrence', 
		'expected': False, 
		'description': 'charles c lawrence comparison with article'
	},
    {
		'input': 'charles c leib;charles c. lieb', 
		'expected': True, 
		'description': 'charles c leib comparison with article'
	},
    {
		'input': 'charles d de long;charles clifton delong', 
		'expected': False, 
		'description': 'charles d de long comparison with article'
	},
    {
		'input': 'charles d lamond;charles lamond', 
		'expected': True, 
		'description': 'charles d lamond comparison with article'
	},
    {
		'input': 'charles d spotts;charles dewey spotts', 
		'expected': True, 
		'description': 'charles d spotts comparison with article'
	},
    {
		'input': 'charles d van cleave;charles durward van cleave', 
		'expected': True, 
		'description': 'charles d van cleave comparison with article'
	},
    {
		'input': 'charles d. davis;charles deforest davis', 
		'expected': True, 
		'description': 'charles d. davis comparison with article'
	},
    {
		'input': 'charles debartolo;karl t. barthelmess', 
		'expected': False, 
		'description': 'charles debartolo comparison with article'
	},
    {
		'input': 'charles debruler;charles debruler', 
		'expected': True, 
		'description': 'charles debruler comparison with article'
	},
    {
		'input': 'charles derleth, jr;charles derleth', 
		'expected': True, 
		'description': 'charles derleth, jr comparison with article'
	},
    {
		'input': 'charles e deckbar;p. e. dicker', 
		'expected': False, 
		'description': 'charles e deckbar comparison with article'
	},
    {
		'input': 'charles e decker;charles elijah decker', 
		'expected': True, 
		'description': 'charles e decker comparison with article'
	},
    {
		'input': 'charles e dewey;charles s. dewey', 
		'expected': False, 
		'description': 'charles e dewey comparison with article'
	},
    {
		'input': 'charles e hubbs;carl leavitt hubbs', 
		'expected': False, 
		'description': 'charles e hubbs comparison with article'
	},
    {
		'input': 'charles e hurd;charles dewitt hurd', 
		'expected': False, 
		'description': 'charles e hurd comparison with article'
	},
    {
		'input': 'charles e landon;charles earl landon', 
		'expected': True, 
		'description': 'charles e landon comparison with article'
	},
    {
		'input': 'charles e lane;charles e. lane', 
		'expected': True, 
		'description': 'charles e lane comparison with article'
	},
    {
		'input': 'charles e lauer;charles e. lauer', 
		'expected': True, 
		'description': 'charles e lauer comparison with article'
	},
    {
		'input': 'charles e leach;charles edward leach', 
		'expected': True, 
		'description': 'charles e leach comparison with article'
	},
    {
		'input': 'charles f dean;robert charles dean', 
		'expected': False, 
		'description': 'charles f dean comparison with article'
	},
    {
		'input': 'charles f deiss;charles frederick deiss', 
		'expected': True, 
		'description': 'charles f deiss comparison with article'
	},
    {
		'input': 'charles f lewis;charles frederick lewis', 
		'expected': True, 
		'description': 'charles f lewis comparison with article'
	},
    {
		'input': 'charles f van cleve;charles f. van cleve', 
		'expected': True, 
		'description': 'charles f van cleve comparison with article'
	},
    {
		'input': 'charles g decker;charles garfield decker', 
		'expected': True, 
		'description': 'charles g decker comparison with article'
	},
    {
		'input': 'charles g lencaln;charles g. lincoln', 
		'expected': True, 
		'description': 'charles g lencaln comparison with article'
	},
    {
		'input': 'charles h desgrey;arthur h. desgrey', 
		'expected': False, 
		'description': 'charles h desgrey comparison with article'
	},
    {
		'input': 'charles h lange;charles h. lange', 
		'expected': True, 
		'description': 'charles h lange comparison with article'
	},
    {
		'input': 'charles h lawshe;charles hubert lawshe', 
		'expected': True, 
		'description': 'charles h lawshe comparison with article'
	},
    {
		'input': 'charles h lehman;charles h lehman', 
		'expected': True, 
		'description': 'charles h lehman comparison with article'
	},
    {
		'input': 'charles h lesesne, jr;charles haynesworth lesesne', 
		'expected': True, 
		'description': 'charles h lesesne, jr comparison with article'
	},
    {
		'input': 'charles h vanduzer;charles h. van duzer', 
		'expected': True, 
		'description': 'charles h vanduzer comparison with article'
	},
    {
		'input': 'charles j fawcett;charles dev. fawcett', 
		'expected': False, 
		'description': 'charles j fawcett comparison with article'
	},
    {
		'input': 'charles j lakofsky;charles j. lakofsky', 
		'expected': True, 
		'description': 'charles j lakofsky comparison with article'
	},
    {
		'input': 'charles l allen;charles laurel allen', 
		'expected': True, 
		'description': 'charles l allen comparison with article'
	},
    {
		'input': 'charles l brown;charles lafayette brown', 
		'expected': True, 
		'description': 'charles l brown comparison with article'
	},
    {
		'input': 'charles l carroll;charles lemuel carroll', 
		'expected': True, 
		'description': 'charles l carroll comparison with article'
	},
    {
		'input': 'charles l jamison;charles laselle jamison', 
		'expected': True, 
		'description': 'charles l jamison comparison with article'
	},
    {
		'input': 'charles l latimer;charles trowbridge latimer', 
		'expected': False, 
		'description': 'charles l latimer comparison with article'
	},
    {
		'input': 'charles l ozer;charles leonard ozer', 
		'expected': True, 
		'description': 'charles l ozer comparison with article'
	},
    {
		'input': 'charles l parmenter;charles leroy parmenter', 
		'expected': True, 
		'description': 'charles l parmenter comparison with article'
	},
    {
		'input': 'charles l peacock, sr;charles leroy peacock', 
		'expected': True, 
		'description': 'charles l peacock, sr comparison with article'
	},
    {
		'input': 'charles l remington;charles lee remington', 
		'expected': True, 
		'description': 'charles l remington comparison with article'
	},
    {
		'input': 'charles l sherman;charles lawton sherman', 
		'expected': True, 
		'description': 'charles l sherman comparison with article'
	},
    {
		'input': 'charles l stewart;charles leslie stewart', 
		'expected': True, 
		'description': 'charles l stewart comparison with article'
	},
    {
		'input': 'charles larocco;charles gerald la rocco', 
		'expected': True, 
		'description': 'charles larocco comparison with article'
	},
    {
		'input': 'charles lassiter;charles albert lassiter', 
		'expected': True, 
		'description': 'charles lassiter comparison with article'
	},
    {
		'input': 'charles leroy atkinson;charles l. atkinson', 
		'expected': True, 
		'description': 'charles leroy atkinson comparison with article'
	},
    {
		'input': 'charles lewis rasor;charles lewis rasor', 
		'expected': True, 
		'description': 'charles lewis rasor comparison with article'
	},
    {
		'input': 'charles m wildes;karl leland wildes', 
		'expected': False, 
		'description': 'charles m wildes comparison with article'
	},
    {
		'input': 'charles n lanier, jr;charles n. lanier', 
		'expected': True, 
		'description': 'charles n lanier, jr comparison with article'
	},
    {
		'input': 'charles n lebeaux;charles n. lebeaux', 
		'expected': True, 
		'description': 'charles n lebeaux comparison with article'
	},
    {
		'input': 'charles r deprima;charles r. deprima', 
		'expected': True, 
		'description': 'charles r deprima comparison with article'
	},
    {
		'input': 'charles r masters;charles a. lemaistre', 
		'expected': False, 
		'description': 'charles r masters comparison with article'
	},
    {
		'input': 'charles s lane;cecelia s. lane', 
		'expected': False, 
		'description': 'charles s lane comparison with article'
	},
    {
		'input': 'charles schalwitz;karl de schweinitz', 
		'expected': False, 
		'description': 'charles schalwitz comparison with article'
	},
    {
		'input': 'charles stone;charles leonard stone', 
		'expected': True, 
		'description': 'charles stone comparison with article'
	},
    {
		'input': 'charles t lester;charles t. lester', 
		'expected': True, 
		'description': 'charles t lester comparison with article'
	},
    {
		'input': 'charles vanbuskirk;chas. van buskirk', 
		'expected': True, 
		'description': 'charles vanbuskirk comparison with article'
	},
    {
		'input': 'charles vanderkar;charles william cares', 
		'expected': False, 
		'description': 'charles vanderkar comparison with article'
	},
    {
		'input': 'charles w devier;charles w. devier', 
		'expected': True, 
		'description': 'charles w devier comparison with article'
	},
    {
		'input': 'charles w lawrence;charles wilson lawrence', 
		'expected': True, 
		'description': 'charles w lawrence comparison with article'
	},
    {
		'input': 'charles z lesher;charles zaner lesher', 
		'expected': True, 
		'description': 'charles z lesher comparison with article'
	},
    {
		'input': 'charlotte i lee;charlotte i. lee', 
		'expected': True, 
		'description': 'charlotte i lee comparison with article'
	},
    {
		'input': 'chas a. larwood;charles h. larwood', 
		'expected': False, 
		'description': 'chas a. larwood comparison with article'
	},
    {
		'input': 'chase kearl;chase delmar kearl', 
		'expected': True, 
		'description': 'chase kearl comparison with article'
	},
    {
		'input': 'chauncey d harris;chauncy dennison harris', 
		'expected': True, 
		'description': 'chauncey d harris comparison with article'
	},
    {
		'input': 'chauncey d holmes;chauncey deppew holmes', 
		'expected': True, 
		'description': 'chauncey d holmes comparison with article'
	},
    {
		'input': 'chester a dow;chester laurens dawes', 
		'expected': False, 
		'description': 'chester a dow comparison with article'
	},
    {
		'input': 'chester a palmer;chester leroy palmer', 
		'expected': False, 
		'description': 'chester a palmer comparison with article'
	},
    {
		'input': 'chester d lee;chester daniel lee', 
		'expected': True, 
		'description': 'chester d lee comparison with article'
	},
    {
		'input': 'chester f lay;chester f. lay', 
		'expected': True, 
		'description': 'chester f lay comparison with article'
	},
    {
		'input': 'chester m destler;chester mcarthur destler', 
		'expected': True, 
		'description': 'chester m destler comparison with article'
	},
    {
		'input': 'chet h lamoure;chet harmon lamore', 
		'expected': True, 
		'description': 'chet h lamoure comparison with article'
	},
    {
		'input': 'chiles b van antwerp;chiles van antwerp', 
		'expected': True, 
		'description': 'chiles b van antwerp comparison with article'
	},
    {
		'input': 'christian j lambertien;christian j. lambertsen', 
		'expected': True, 
		'description': 'christian j lambertien comparison with article'
	},
    {
		'input': 'churchill p lathrop;churchill pierce lathrop', 
		'expected': True, 
		'description': 'churchill p lathrop comparison with article'
	},
    {
		'input': 'clair v langton;c. v. langton', 
		'expected': True, 
		'description': 'clair v langton comparison with article'
	},
    {
		'input': 'clair v langton;c. v. n. langton', 
		'expected': True, 
		'description': 'clair v langton comparison with article'
	},
    {
		'input': 'claire m van leeuven;myron james van leeuwen', 
		'expected': False, 
		'description': 'claire m van leeuven comparison with article'
	},
    {
		'input': 'clara l de land;clara hockridge de land', 
		'expected': False, 
		'description': 'clara l de land comparison with article'
	},
    {
		'input': 'clara l van nins;l. nanni', 
		'expected': False, 
		'description': 'clara l van nins comparison with article'
	},
    {
		'input': 'clara lee tanner;clara lee tanner', 
		'expected': True, 
		'description': 'clara lee tanner comparison with article'
	},
    {
		'input': 'clarance vanepps;clarence van epps', 
		'expected': True, 
		'description': 'clarance vanepps comparison with article'
	},
    {
		'input': 'clare l marquette;clare leslie marquette', 
		'expected': True, 
		'description': 'clare l marquette comparison with article'
	},
    {
		'input': 'clare russell;clare dewitt russell', 
		'expected': True, 
		'description': 'clare russell comparison with article'
	},
    {
		'input': 'clarence b hogan;clarence lester hogan', 
		'expected': False, 
		'description': 'clarence b hogan comparison with article'
	},
    {
		'input': 'clarence b lafromboise;clarence brown lafromboise', 
		'expected': True, 
		'description': 'clarence b lafromboise comparison with article'
	},
    {
		'input': 'clarence c lee;clarence pendleton lee', 
		'expected': False, 
		'description': 'clarence c lee comparison with article'
	},
    {
		'input': 'clarence d dieter;clarence dewey dieter', 
		'expected': True, 
		'description': 'clarence d dieter comparison with article'
	},
    {
		'input': 'clarence d thorpe;clarence dewitt thorpe', 
		'expected': True, 
		'description': 'clarence d thorpe comparison with article'
	},
    {
		'input': 'clarence e deakins;clarence earl deakins', 
		'expected': True, 
		'description': 'clarence e deakins comparison with article'
	},
    {
		'input': 'clarence f lewis;clarence flavius lewis', 
		'expected': True, 
		'description': 'clarence f lewis comparison with article'
	},
    {
		'input': 'clarence i lewis;clarence irving lewis', 
		'expected': True, 
		'description': 'clarence i lewis comparison with article'
	},
    {
		'input': 'clarence l miller;clarence lee miller', 
		'expected': True, 
		'description': 'clarence l miller comparison with article'
	},
    {
		'input': 'clarence l nystrom;clarence leroy nystrom', 
		'expected': True, 
		'description': 'clarence l nystrom comparison with article'
	},
    {
		'input': 'clarence l turner;clarence lester turner', 
		'expected': True, 
		'description': 'clarence l turner comparison with article'
	},
    {
		'input': 'clarence l van sickle;clarence l. vansickle', 
		'expected': True, 
		'description': 'clarence l van sickle comparison with article'
	},
    {
		'input': 'clarence lee furrow;clarence lee furrow', 
		'expected': True, 
		'description': 'clarence lee furrow comparison with article'
	},
    {
		'input': 'clarence n oliver;clarence leslie oliver', 
		'expected': False, 
		'description': 'clarence n oliver comparison with article'
	},
    {
		'input': 'clark j laus;clark john laus', 
		'expected': True, 
		'description': 'clark j laus comparison with article'
	},
    {
		'input': 'clark l allen;clark lee allen', 
		'expected': True, 
		'description': 'clark l allen comparison with article'
	},
    {
		'input': 'clark l thayer;clark leonard thayer', 
		'expected': True, 
		'description': 'clark l thayer comparison with article'
	},
    {
		'input': 'clark o lamberton;clark d. lamberton', 
		'expected': False, 
		'description': 'clark o lamberton comparison with article'
	},
    {
		'input': 'claude e lett, jr;martin e. lichte', 
		'expected': False, 
		'description': 'claude e lett, jr comparison with article'
	},
    {
		'input': 'claude k deischer;claude knauss deischer', 
		'expected': True, 
		'description': 'claude k deischer comparison with article'
	},
    {
		'input': 'claude l finney;claude lee finney', 
		'expected': True, 
		'description': 'claude l finney comparison with article'
	},
    {
		'input': 'claude s la dow;claude s. ladow', 
		'expected': True, 
		'description': 'claude s la dow comparison with article'
	},
    {
		'input': 'claudine mason;claudine van cleave mason', 
		'expected': True, 
		'description': 'claudine mason comparison with article'
	},
    {
		'input': 'clayton l farrar;clayton leon farrar', 
		'expected': True, 
		'description': 'clayton l farrar comparison with article'
	},
    {
		'input': 'clem a. leonard;a. byron leonard', 
		'expected': False, 
		'description': 'clem a. leonard comparison with article'
	},
    {
		'input': 'clifford barrett;clifford leslie barrett', 
		'expected': True, 
		'description': 'clifford barrett comparison with article'
	},
    {
		'input': 'clifford e lampman;clifford e. lampman', 
		'expected': True, 
		'description': 'clifford e lampman comparison with article'
	},
    {
		'input': 'clifford l whitman;clifford ler. whitman', 
		'expected': True, 
		'description': 'clifford l whitman comparison with article'
	},
    {
		'input': 'clifford l. brownell;clifford lee brownell', 
		'expected': True, 
		'description': 'clifford l. brownell comparison with article'
	},
    {
		'input': 'clifton e. van sickle;c. e. vansickle', 
		'expected': True, 
		'description': 'clifton e. van sickle comparison with article'
	},
    {
		'input': 'clinton f larson;clinton f. larson', 
		'expected': True, 
		'description': 'clinton f larson comparison with article'
	},
    {
		'input': 'clinton l compere;clinton lee compere', 
		'expected': True, 
		'description': 'clinton l compere comparison with article'
	},
    {
		'input': 'clyde d mueller;clyde dewey mueller', 
		'expected': True, 
		'description': 'clyde d mueller comparison with article'
	},
    {
		'input': 'clyde deming, jr;clyde leroy deming', 
		'expected': True, 
		'description': 'clyde deming, jr comparison with article'
	},
    {
		'input': 'clyde l colson;clyde lemuel colson', 
		'expected': True, 
		'description': 'clyde l colson comparison with article'
	},
    {
		'input': 'clyde l farrar;clyde leo farrar', 
		'expected': True, 
		'description': 'clyde l farrar comparison with article'
	},
    {
		'input': 'clyde v lee;clyde v. lee', 
		'expected': True, 
		'description': 'clyde v lee comparison with article'
	},
    {
		'input': 'constant van de wall;constant van de wall', 
		'expected': True, 
		'description': 'constant van de wall comparison with article'
	},
    {
		'input': 'cora lee coleman;amoss lee coleman', 
		'expected': False, 
		'description': 'cora lee coleman comparison with article'
	},
    {
		'input': 'cristo g coutsibos;r. g. lacount', 
		'expected': False, 
		'description': 'cristo g coutsibos comparison with article'
	},
    {
		'input': 'curt leben;curt charles leben', 
		'expected': True, 
		'description': 'curt leben comparison with article'
	},
    {
		'input': 'curtis l farrington;curtis leon farrington', 
		'expected': True, 
		'description': 'curtis l farrington comparison with article'
	},
    {
		'input': 'cyril l vance;cyril vance', 
		'expected': True, 
		'description': 'cyril l vance comparison with article'
	},
    {
		'input': 'cyril r delaney;cyril r. delaney', 
		'expected': True, 
		'description': 'cyril r delaney comparison with article'
	},
    {
		'input': 'cyrus l day;cyrus lawrence day', 
		'expected': True, 
		'description': 'cyrus l day comparison with article'
	},
    {
		'input': 'd leo hayes;daniel leo hayes', 
		'expected': True, 
		'description': 'd leo hayes comparison with article'
	},
    {
		'input': 'd, jack rogers,;jack dean rogers', 
		'expected': True, 
		'description': 'd, jack rogers, comparison with article'
	},
    {
		'input': 'dagobert de levie;dagobert de levie', 
		'expected': True, 
		'description': 'dagobert de levie comparison with article'
	},
    {
		'input': 'dallas m lancaster;dallas m. lancaster', 
		'expected': True, 
		'description': 'dallas m lancaster comparison with article'
	},
    {
		'input': 'dana j. demorest;dana j. demorest', 
		'expected': True, 
		'description': 'dana j. demorest comparison with article'
	},
    {
		'input': 'danial m laskin;d. m. laskin', 
		'expected': True, 
		'description': 'danial m laskin comparison with article'
	},
    {
		'input': 'daniel d linglebach;daniel dee linglebach', 
		'expected': True, 
		'description': 'daniel d linglebach comparison with article'
	},
    {
		'input': 'daniel e vandraegan;daniel vandraegen', 
		'expected': True, 
		'description': 'daniel e vandraegan comparison with article'
	},
    {
		'input': 'daniel h levan;daniel jacob levinson', 
		'expected': False, 
		'description': 'daniel h levan comparison with article'
	},
    {
		'input': 'daniel l delakas;daniel lindviko delakes', 
		'expected': True, 
		'description': 'daniel l delakas comparison with article'
	},
    {
		'input': 'daniel v hageman;daniel vanbrunt hegeman', 
		'expected': True, 
		'description': 'daniel v hageman comparison with article'
	},
    {
		'input': 'daris g lafferty;daris grover lafferty', 
		'expected': True, 
		'description': 'daris g lafferty comparison with article'
	},
    {
		'input': 'darrell l spriggs;darrell leonard spriggs', 
		'expected': True, 
		'description': 'darrell l spriggs comparison with article'
	},
    {
		'input': 'david a ledet;david a. ledet', 
		'expected': True, 
		'description': 'david a ledet comparison with article'
	},
    {
		'input': 'david a mac lennan;david alexander maclennan', 
		'expected': True, 
		'description': 'david a mac lennan comparison with article'
	},
    {
		'input': 'david b dekker;david bliss dekker', 
		'expected': True, 
		'description': 'david b dekker comparison with article'
	},
    {
		'input': 'david d law;david barclay law', 
		'expected': False, 
		'description': 'david d law comparison with article'
	},
    {
		'input': 'david f farley;david la bauve farley', 
		'expected': False, 
		'description': 'david f farley comparison with article'
	},
    {
		'input': 'david f strain;david o. van strien', 
		'expected': False, 
		'description': 'david f strain comparison with article'
	},
    {
		'input': 'david j lamotte;david joseph lamothe', 
		'expected': True, 
		'description': 'david j lamotte comparison with article'
	},
    {
		'input': 'david k detweiler;david k. detweiler', 
		'expected': True, 
		'description': 'david k detweiler comparison with article'
	},
    {
		'input': 'david l anderson;david leonard anderson', 
		'expected': True, 
		'description': 'david l anderson comparison with article'
	},
    {
		'input': 'david l arm;david lehr arm', 
		'expected': True, 
		'description': 'david l arm comparison with article'
	},
    {
		'input': 'david l clark;david lee clark', 
		'expected': True, 
		'description': 'david l clark comparison with article'
	},
    {
		'input': 'david l dodd;david le fevre dodd', 
		'expected': True, 
		'description': 'david l dodd comparison with article'
	},
    {
		'input': 'david l farley;david la bauve farley', 
		'expected': True, 
		'description': 'david l farley comparison with article'
	},
    {
		'input': 'david l lawson;edwin david lawson', 
		'expected': False, 
		'description': 'david l lawson comparison with article'
	},
    {
		'input': 'david l mackintosh;david leslie mackintosh', 
		'expected': True, 
		'description': 'david l mackintosh comparison with article'
	},
    {
		'input': 'david lewis;david lewis', 
		'expected': True, 
		'description': 'david lewis comparison with article'
	},
    {
		'input': 'david m deforest;david m. deforest', 
		'expected': True, 
		'description': 'david m deforest comparison with article'
	},
    {
		'input': 'david m dennison;david mathias dennison', 
		'expected': True, 
		'description': 'david m dennison comparison with article'
	},
    {
		'input': 'david t lapkin;david t. lapkin', 
		'expected': True, 
		'description': 'david t lapkin comparison with article'
	},
    {
		'input': 'david v lawrence;david lawrence', 
		'expected': True, 
		'description': 'david v lawrence comparison with article'
	},
    {
		'input': 'david van meter;david van meter', 
		'expected': True, 
		'description': 'david van meter comparison with article'
	},
    {
		'input': 'david van vactor;david g. vanvactor', 
		'expected': True, 
		'description': 'david van vactor comparison with article'
	},
    {
		'input': 'dean d pearl;herbert dean pearl', 
		'expected': False, 
		'description': 'dean d pearl comparison with article'
	},
    {
		'input': 'dean e babbage;e. dean babbage', 
		'expected': True, 
		'description': 'dean e babbage comparison with article'
	},
    {
		'input': 'deane l lawrence;laszlo lorand', 
		'expected': False, 
		'description': 'deane l lawrence comparison with article'
	},
    {
		'input': 'deane lent;deane lent', 
		'expected': True, 
		'description': 'deane lent comparison with article'
	},
    {
		'input': 'delbert l rutledge;delbert leroy rutledge', 
		'expected': True, 
		'description': 'delbert l rutledge comparison with article'
	},
    {
		'input': 'delight m maughan;h. delight maughan', 
		'expected': False, 
		'description': 'delight m maughan comparison with article'
	},
    {
		'input': 'della lehman;della lehman', 
		'expected': True, 
		'description': 'della lehman comparison with article'
	},
    {
		'input': 'delmar leighton, jr;delmar leighton', 
		'expected': True, 
		'description': 'delmar leighton, jr comparison with article'
	},
    {
		'input': 'dennis anderson;ira dennis anderson', 
		'expected': True, 
		'description': 'dennis anderson comparison with article'
	},
    {
		'input': 'denoe leedy;charles denoe leedy', 
		'expected': True, 
		'description': 'denoe leedy comparison with article'
	},
    {
		'input': 'dexter j hill;j. levan hill', 
		'expected': False, 
		'description': 'dexter j hill comparison with article'
	},
    {
		'input': 'dexter levy;dexter s. levy', 
		'expected': True, 
		'description': 'dexter levy comparison with article'
	},
    {
		'input': 'diane j de lotto;marcel j. de lotto', 
		'expected': False, 
		'description': 'diane j de lotto comparison with article'
	},
    {
		'input': 'dick s vanfleet;dick scott van fleet', 
		'expected': True, 
		'description': 'dick s vanfleet comparison with article'
	},
    {
		'input': 'dietrich hildebrand;dietrich von hildebrand', 
		'expected': True, 
		'description': 'dietrich hildebrand comparison with article'
	},
    {
		'input': 'dinna p lipkin;peter p. lapiken', 
		'expected': False, 
		'description': 'dinna p lipkin comparison with article'
	},
    {
		'input': 'dixy lee ray;dixy lee ray', 
		'expected': True, 
		'description': 'dixy lee ray comparison with article'
	},
    {
		'input': 'don d lescohier;don divance lescohier', 
		'expected': True, 
		'description': 'don d lescohier comparison with article'
	},
    {
		'input': 'don l good;don ladoyt good', 
		'expected': True, 
		'description': 'don l good comparison with article'
	},
    {
		'input': 'don l. demorest;don l. demorest', 
		'expected': True, 
		'description': 'don l. demorest comparison with article'
	},
    {
		'input': 'don lewis;don lewis', 
		'expected': True, 
		'description': 'don lewis comparison with article'
	},
    {
		'input': 'donald a lentz;donald a. lentz', 
		'expected': True, 
		'description': 'donald a lentz comparison with article'
	},
    {
		'input': 'donald b lawrence;donald b. lawrence', 
		'expected': True, 
		'description': 'donald b lawrence comparison with article'
	},
    {
		'input': 'donald darickson;donald derickson', 
		'expected': True, 
		'description': 'donald darickson comparison with article'
	},
    {
		'input': 'donald deford;donald dale deford', 
		'expected': True, 
		'description': 'donald deford comparison with article'
	},
    {
		'input': 'donald devault;don devault', 
		'expected': True, 
		'description': 'donald devault comparison with article'
	},
    {
		'input': 'donald e stewart;donald dean stewart', 
		'expected': False, 
		'description': 'donald e stewart comparison with article'
	},
    {
		'input': 'donald e. lowell;edgar lafayette lowell', 
		'expected': False, 
		'description': 'donald e. lowell comparison with article'
	},
    {
		'input': 'donald f lake;donald frederick lach', 
		'expected': True, 
		'description': 'donald f lake comparison with article'
	},
    {
		'input': 'donald fabian;donald leroy fabian', 
		'expected': True, 
		'description': 'donald fabian comparison with article'
	},
    {
		'input': 'donald g lee;donald g. lee', 
		'expected': True, 
		'description': 'donald g lee comparison with article'
	},
    {
		'input': 'donald g. decker;donald gilmore decker', 
		'expected': True, 
		'description': 'donald g. decker comparison with article'
	},
    {
		'input': 'donald i augustine;donald leslie augustine', 
		'expected': False, 
		'description': 'donald i augustine comparison with article'
	},
    {
		'input': 'donald j dettinger;donald j. dettinger', 
		'expected': True, 
		'description': 'donald j dettinger comparison with article'
	},
    {
		'input': 'donald j lewis;donald joseph lewis', 
		'expected': True, 
		'description': 'donald j lewis comparison with article'
	},
    {
		'input': 'donald l heinemeyer;donald leroy heinemeyer', 
		'expected': True, 
		'description': 'donald l heinemeyer comparison with article'
	},
    {
		'input': 'donald l katz;donald laverne katz', 
		'expected': True, 
		'description': 'donald l katz comparison with article'
	},
    {
		'input': 'donald lake;donald l. lake', 
		'expected': True, 
		'description': 'donald lake comparison with article'
	},
    {
		'input': 'donald le tendre;donald henry letendre', 
		'expected': True, 
		'description': 'donald le tendre comparison with article'
	},
    {
		'input': 'donald murphy;donald van dale murphy', 
		'expected': True, 
		'description': 'donald murphy comparison with article'
	},
    {
		'input': 'donald r larsen;donald r. larson', 
		'expected': True, 
		'description': 'donald r larsen comparison with article'
	},
    {
		'input': 'donald w del carlo;donald w. de carle', 
		'expected': True, 
		'description': 'donald w del carlo comparison with article'
	},
    {
		'input': 'doris e lees;doris estabrook lees', 
		'expected': True, 
		'description': 'doris e lees comparison with article'
	},
    {
		'input': 'doris f larsen;bent f. larsen', 
		'expected': False, 
		'description': 'doris f larsen comparison with article'
	},
    {
		'input': 'dorothy c lee;shu-ching lee', 
		'expected': False, 
		'description': 'dorothy c lee comparison with article'
	},
    {
		'input': 'dorothy dean;dorothy dean', 
		'expected': True, 
		'description': 'dorothy dean comparison with article'
	},
    {
		'input': 'dorothy delany;dorothy celia delany', 
		'expected': True, 
		'description': 'dorothy delany comparison with article'
	},
    {
		'input': 'dorothy f deach;dorothy f. deach', 
		'expected': True, 
		'description': 'dorothy f deach comparison with article'
	},
    {
		'input': 'dorothy jean laubacher;dorothy laubacher', 
		'expected': True, 
		'description': 'dorothy jean laubacher comparison with article'
	},
    {
		'input': 'dorothy l fuller;dorothy langford fuller', 
		'expected': True, 
		'description': 'dorothy l fuller comparison with article'
	},
    {
		'input': 'dorothy l large;dorothy large', 
		'expected': True, 
		'description': 'dorothy l large comparison with article'
	},
    {
		'input': 'dorothy leahy;dorothy leahy', 
		'expected': True, 
		'description': 'dorothy leahy comparison with article'
	},
    {
		'input': 'dorothy lee hayes;dorothy hayes', 
		'expected': True, 
		'description': 'dorothy lee hayes comparison with article'
	},
    {
		'input': 'dorothy levine;dorothy levens', 
		'expected': False, 
		'description': 'dorothy levine comparison with article'
	},
    {
		'input': 'dorothy m lasalle;dorothy m. lasalle', 
		'expected': True, 
		'description': 'dorothy m lasalle comparison with article'
	},
    {
		'input': 'dorothy mac lean;dorothy g. maclean', 
		'expected': True, 
		'description': 'dorothy mac lean comparison with article'
	},
    {
		'input': 'dorothy v a fuller;dorothy van arsdale fuller', 
		'expected': True, 
		'description': 'dorothy v a fuller comparison with article'
	},
    {
		'input': 'dorothy w dennis;dorothy warner dennis', 
		'expected': True, 
		'description': 'dorothy w dennis comparison with article'
	},
    {
		'input': 'dorsey d jones;dorsey dee jones', 
		'expected': True, 
		'description': 'dorsey d jones comparison with article'
	},
    {
		'input': 'dorsey e lane;dorsey e. lane', 
		'expected': True, 
		'description': 'dorsey e lane comparison with article'
	},
    {
		'input': 'dorval d despres;solveig d. preus', 
		'expected': False, 
		'description': 'dorval d despres comparison with article'
	},
    {
		'input': 'douglas d martin;douglas deveny martin', 
		'expected': True, 
		'description': 'douglas d martin comparison with article'
	},
    {
		'input': 'douglas e lawson;douglas e. lawson', 
		'expected': True, 
		'description': 'douglas e lawson comparison with article'
	},
    {
		'input': 'douglas h lawrence;douglas howard lawrence', 
		'expected': True, 
		'description': 'douglas h lawrence comparison with article'
	},
    {
		'input': 'douglas l kraus;douglas lawrence kraus', 
		'expected': True, 
		'description': 'douglas l kraus comparison with article'
	},
    {
		'input': 'douglass lathwell;douglas j. lathwell', 
		'expected': True, 
		'description': 'douglass lathwell comparison with article'
	},
    {
		'input': 'dr alphonse vonderahe;alphonse r. vonderahe', 
		'expected': True, 
		'description': 'dr alphonse vonderahe comparison with article'
	},
    {
		'input': 'dr howard l alt;howard lang alt', 
		'expected': True, 
		'description': 'dr howard l alt comparison with article'
	},
    {
		'input': 'dr leonard aguilino;leonard m. aquilino', 
		'expected': True, 
		'description': 'dr leonard aguilino comparison with article'
	},
    {
		'input': 'dr. lester r cahn;lester r. cahn', 
		'expected': True, 
		'description': 'dr. lester r cahn comparison with article'
	},
    {
		'input': 'dudley d carroll;dudley dewitt carroll', 
		'expected': True, 
		'description': 'dudley d carroll comparison with article'
	},
    {
		'input': 'dwight e lee;dwight erwin lee', 
		'expected': True, 
		'description': 'dwight e lee comparison with article'
	},
    {
		'input': 'dwight l ling;dwight leroy ling', 
		'expected': True, 
		'description': 'dwight l ling comparison with article'
	},
    {
		'input': 'dwight l spencer, jr;guilford lawson spencer', 
		'expected': False, 
		'description': 'dwight l spencer, jr comparison with article'
	},
    {
		'input': 'dwight m delong;dwight m. delong', 
		'expected': True, 
		'description': 'dwight m delong comparison with article'
	},
    {
		'input': 'e donald lawrence;e. donald lawrence', 
		'expected': True, 
		'description': 'e donald lawrence comparison with article'
	},
    {
		'input': 'e harold laws;e. harold laws', 
		'expected': True, 
		'description': 'e harold laws comparison with article'
	},
    {
		'input': 'e lane davis;edward lane davis', 
		'expected': True, 
		'description': 'e lane davis comparison with article'
	},
    {
		'input': 'e lee goldsborough;e. lee goldsborough', 
		'expected': True, 
		'description': 'e lee goldsborough comparison with article'
	},
    {
		'input': 'e lee kinsey;e. lee kinsey', 
		'expected': True, 
		'description': 'e lee kinsey comparison with article'
	},
    {
		'input': 'e lewis morris;lewis r. morris', 
		'expected': False, 
		'description': 'e lewis morris comparison with article'
	},
    {
		'input': 'e richard larson;e. richard larson', 
		'expected': True, 
		'description': 'e richard larson comparison with article'
	},
    {
		'input': 'e virginia lewis;virginia e. lewis', 
		'expected': True, 
		'description': 'e virginia lewis comparison with article'
	},
    {
		'input': 'earl l butz;earl lauer butz', 
		'expected': True, 
		'description': 'earl l butz comparison with article'
	},
    {
		'input': 'earl l core;earl lemley core', 
		'expected': True, 
		'description': 'earl l core comparison with article'
	},
    {
		'input': 'earl l farmer;earl leroy farmer', 
		'expected': True, 
		'description': 'earl l farmer comparison with article'
	},
    {
		'input': 'earl l griggs;earl leslie griggs', 
		'expected': True, 
		'description': 'earl l griggs comparison with article'
	},
    {
		'input': 'earl l martin;earl leslie martin', 
		'expected': True, 
		'description': 'earl l martin comparison with article'
	},
    {
		'input': 'earl l stone, jr;earl lewis stone', 
		'expected': True, 
		'description': 'earl l stone, jr comparison with article'
	},
    {
		'input': 'earl l vance;earl lynn vance', 
		'expected': True, 
		'description': 'earl l vance comparison with article'
	},
    {
		'input': 'earl latham;earl latham', 
		'expected': True, 
		'description': 'earl latham comparison with article'
	},
    {
		'input': 'earl p lasher, jr;earl parsons lasher', 
		'expected': True, 
		'description': 'earl p lasher, jr comparison with article'
	},
    {
		'input': 'earl r leng;earl r. leng', 
		'expected': True, 
		'description': 'earl r leng comparison with article'
	},
    {
		'input': 'earl s howard;earl dean howard', 
		'expected': False, 
		'description': 'earl s howard comparison with article'
	},
    {
		'input': 'earnest langley;ernest felix langley', 
		'expected': True, 
		'description': 'earnest langley comparison with article'
	},
    {
		'input': 'edgar l lazier;edgar l. lazier', 
		'expected': True, 
		'description': 'edgar l lazier comparison with article'
	},
    {
		'input': 'edgar l mcgowan;edgar leon mcgowan', 
		'expected': True, 
		'description': 'edgar l mcgowan comparison with article'
	},
    {
		'input': 'edgar lewis winfrey;lewis edgar winfrey', 
		'expected': True, 
		'description': 'edgar lewis winfrey comparison with article'
	},
    {
		'input': 'edgar w lacy;edgar wilson lacy', 
		'expected': True, 
		'description': 'edgar w lacy comparison with article'
	},
    {
		'input': 'edith a laue;edith a. laue', 
		'expected': True, 
		'description': 'edith a laue comparison with article'
	},
    {
		'input': 'edith layer;edith e. layer', 
		'expected': True, 
		'description': 'edith layer comparison with article'
	},
    {
		'input': 'edith m branin;m. lelyn branin', 
		'expected': False, 
		'description': 'edith m branin comparison with article'
	},
    {
		'input': 'edith m derrick;lawrence m. derickier', 
		'expected': False, 
		'description': 'edith m derrick comparison with article'
	},
    {
		'input': 'edmund d lewandowski;edmund d. lewandowski', 
		'expected': True, 
		'description': 'edmund d lewandowski comparison with article'
	},
    {
		'input': 'edmund h campbell;edmund lee gamble', 
		'expected': False, 
		'description': 'edmund h campbell comparison with article'
	},
    {
		'input': 'edmund p learned;edmund philip learned', 
		'expected': True, 
		'description': 'edmund p learned comparison with article'
	},
    {
		'input': 'edmund v laitone;edmund v. laitone', 
		'expected': True, 
		'description': 'edmund v laitone comparison with article'
	},
    {
		'input': 'edna landros;edna landros', 
		'expected': True, 
		'description': 'edna landros comparison with article'
	},
    {
		'input': 'edna m lawrence;edna w. lawrence', 
		'expected': False, 
		'description': 'edna m lawrence comparison with article'
	},
    {
		'input': 'edna w lewis;edna lewis', 
		'expected': True, 
		'description': 'edna w lewis comparison with article'
	},
    {
		'input': 'edward a gibbs;edward delmar gibbs', 
		'expected': False, 
		'description': 'edward a gibbs comparison with article'
	},
    {
		'input': 'edward a lavin;edward a. levin', 
		'expected': True, 
		'description': 'edward a lavin comparison with article'
	},
    {
		'input': 'edward b lawton, jr;edward b. lawton', 
		'expected': True, 
		'description': 'edward b lawton, jr comparison with article'
	},
    {
		'input': 'edward b lewis;edward b. lewis', 
		'expected': True, 
		'description': 'edward b lewis comparison with article'
	},
    {
		'input': 'edward bassett;edward lewis bassett', 
		'expected': True, 
		'description': 'edward bassett comparison with article'
	},
    {
		'input': 'edward c lambert;edward c. lambert', 
		'expected': True, 
		'description': 'edward c lambert comparison with article'
	},
    {
		'input': 'edward c lambert;edward charles lambert', 
		'expected': True, 
		'description': 'edward c lambert comparison with article'
	},
    {
		'input': 'edward c lesch;edward c. a. lesch', 
		'expected': True, 
		'description': 'edward c lesch comparison with article'
	},
    {
		'input': 'edward d lafferty;d. lafferty', 
		'expected': True, 
		'description': 'edward d lafferty comparison with article'
	},
    {
		'input': 'edward d myers;edward delos myers', 
		'expected': True, 
		'description': 'edward d myers comparison with article'
	},
    {
		'input': 'edward d seeber;edward derbyshire seeber', 
		'expected': True, 
		'description': 'edward d seeber comparison with article'
	},
    {
		'input': 'edward de s matthews,s;edward desaunhac matthews', 
		'expected': True, 
		'description': 'edward de s matthews,s comparison with article'
	},
    {
		'input': 'edward dean christensen;edward l. christensen', 
		'expected': False, 
		'description': 'edward dean christensen comparison with article'
	},
    {
		'input': 'edward e landis;edward everett landis', 
		'expected': True, 
		'description': 'edward e landis comparison with article'
	},
    {
		'input': 'edward erikson;edward leerdrup eriksen', 
		'expected': True, 
		'description': 'edward erikson comparison with article'
	},
    {
		'input': 'edward g lewis;edward g. lewis', 
		'expected': True, 
		'description': 'edward g lewis comparison with article'
	},
    {
		'input': 'edward g van bibber;george van bibber', 
		'expected': True, 
		'description': 'edward g van bibber comparison with article'
	},
    {
		'input': 'edward h davis;edward smith deevey', 
		'expected': False, 
		'description': 'edward h davis comparison with article'
	},
    {
		'input': 'edward h la forge;edward h. lafarge', 
		'expected': True, 
		'description': 'edward h la forge comparison with article'
	},
    {
		'input': 'edward h leach;mac edward leach', 
		'expected': False, 
		'description': 'edward h leach comparison with article'
	},
    {
		'input': 'edward h lepper;m. h. lepper', 
		'expected': False, 
		'description': 'edward h lepper comparison with article'
	},
    {
		'input': 'edward j larkin;edward j larkin', 
		'expected': True, 
		'description': 'edward j larkin comparison with article'
	},
    {
		'input': 'edward j lawrence;edward j. lorenze', 
		'expected': False, 
		'description': 'edward j lawrence comparison with article'
	},
    {
		'input': 'edward j lazear, jr;edward j. lazear', 
		'expected': True, 
		'description': 'edward j lazear, jr comparison with article'
	},
    {
		'input': 'edward j van liere;edward gerald van liere', 
		'expected': False, 
		'description': 'edward j van liere comparison with article'
	},
    {
		'input': 'edward j vanloon;edward j. van loon', 
		'expected': True, 
		'description': 'edward j vanloon comparison with article'
	},
    {
		'input': 'edward k lebohner;edward k. lebohner', 
		'expected': True, 
		'description': 'edward k lebohner comparison with article'
	},
    {
		'input': 'edward l clark;edward lester clark', 
		'expected': True, 
		'description': 'edward l clark comparison with article'
	},
    {
		'input': 'edward l emling;edward langhoff emling', 
		'expected': True, 
		'description': 'edward l emling comparison with article'
	},
    {
		'input': 'edward l howes;edward lee howes', 
		'expected': True, 
		'description': 'edward l howes comparison with article'
	},
    {
		'input': 'edward l jenkins;edward lealand jenkinson', 
		'expected': True, 
		'description': 'edward l jenkins comparison with article'
	},
    {
		'input': 'edward l king;edward lacy king', 
		'expected': True, 
		'description': 'edward l king comparison with article'
	},
    {
		'input': 'edward l tatum;edward lawrie tatum', 
		'expected': True, 
		'description': 'edward l tatum comparison with article'
	},
    {
		'input': 'edward lathrop;edward flint lathrop', 
		'expected': True, 
		'description': 'edward lathrop comparison with article'
	},
    {
		'input': 'edward lecomte;edward s. le comte', 
		'expected': True, 
		'description': 'edward lecomte comparison with article'
	},
    {
		'input': 'edward lee dorsett;edward lee dorsett', 
		'expected': True, 
		'description': 'edward lee dorsett comparison with article'
	},
    {
		'input': 'edward leonard, jr;edward leonard', 
		'expected': True, 
		'description': 'edward leonard, jr comparison with article'
	},
    {
		'input': 'edward lowson;edward f. lewison', 
		'expected': False, 
		'description': 'edward lowson comparison with article'
	},
    {
		'input': 'edward p lana;edward p. lana', 
		'expected': True, 
		'description': 'edward p lana comparison with article'
	},
    {
		'input': 'edward r dezurko;e. r. dezurko', 
		'expected': True, 
		'description': 'edward r dezurko comparison with article'
	},
    {
		'input': 'edward t ladd;edward taylor ladd', 
		'expected': True, 
		'description': 'edward t ladd comparison with article'
	},
    {
		'input': 'edward van ormer;edward b. van ormer', 
		'expected': True, 
		'description': 'edward van ormer comparison with article'
	},
    {
		'input': 'edward van winkle;edward hasbrouck van winkle', 
		'expected': True, 
		'description': 'edward van winkle comparison with article'
	},
    {
		'input': 'edward wallace;edward leon wallace', 
		'expected': True, 
		'description': 'edward wallace comparison with article'
	},
    {
		'input': 'edwin a lee;edwin a. lee', 
		'expected': True, 
		'description': 'edwin a lee comparison with article'
	},
    {
		'input': 'edwin b langston;beach langston', 
		'expected': True, 
		'description': 'edwin b langston comparison with article'
	},
    {
		'input': 'edwin h lewis;edwin h lewis', 
		'expected': True, 
		'description': 'edwin h lewis comparison with article'
	},
    {
		'input': 'edwin j lamont;edwin i. lamont', 
		'expected': False, 
		'description': 'edwin j lamont comparison with article'
	},
    {
		'input': 'edwin j lanwerth;edwin j lanwerth', 
		'expected': True, 
		'description': 'edwin j lanwerth comparison with article'
	},
    {
		'input': 'edwin l lame;edwin l. lame', 
		'expected': True, 
		'description': 'edwin l lame comparison with article'
	},
    {
		'input': 'edwin l levy;edwin l. levy', 
		'expected': True, 
		'description': 'edwin l levy comparison with article'
	},
    {
		'input': 'edwin l miller;edwin lawrence miller', 
		'expected': True, 
		'description': 'edwin l miller comparison with article'
	},
    {
		'input': 'edwin l theiss;edwin leodgar theiss', 
		'expected': True, 
		'description': 'edwin l theiss comparison with article'
	},
    {
		'input': 'edwin l williams;edwin lea williams', 
		'expected': True, 
		'description': 'edwin l williams comparison with article'
	},
    {
		'input': 'edwin m larsen;edwin merritt larsen', 
		'expected': True, 
		'description': 'edwin m larsen comparison with article'
	},
    {
		'input': 'edwin mclean;martin edwin lean', 
		'expected': False, 
		'description': 'edwin mclean comparison with article'
	},
    {
		'input': 'edwin n. lassettre;edwin n. lassettre', 
		'expected': True, 
		'description': 'edwin n. lassettre comparison with article'
	},
    {
		'input': 'elbert persons;elbert lapsley persons', 
		'expected': True, 
		'description': 'elbert persons comparison with article'
	},
    {
		'input': 'elbridge p vance;elbridge putnam vance', 
		'expected': True, 
		'description': 'elbridge p vance comparison with article'
	},
    {
		'input': 'elden e leasure, 2nd;elden emanuel leasure', 
		'expected': True, 
		'description': 'elden e leasure, 2nd comparison with article'
	},
    {
		'input': 'eleanor a rhodes;arnold densmore rhodes', 
		'expected': False, 
		'description': 'eleanor a rhodes comparison with article'
	},
    {
		'input': 'eleanor delfs;eleanor delfs', 
		'expected': True, 
		'description': 'eleanor delfs comparison with article'
	},
    {
		'input': 'eleanor leek;eleanor leek', 
		'expected': True, 
		'description': 'eleanor leek comparison with article'
	},
    {
		'input': 'eleanor lewis;eleanor lewis', 
		'expected': True, 
		'description': 'eleanor lewis comparison with article'
	},
    {
		'input': 'eli m levine;eli m. levine', 
		'expected': True, 
		'description': 'eli m levine comparison with article'
	},
    {
		'input': 'eline m von borries;eline von borries', 
		'expected': True, 
		'description': 'eline m von borries comparison with article'
	},
    {
		'input': 'elizabeth h leduc;elizabeth h. leduc', 
		'expected': True, 
		'description': 'elizabeth h leduc comparison with article'
	},
    {
		'input': 'elizabeth hanscom;elizabeth deering hanscom', 
		'expected': True, 
		'description': 'elizabeth hanscom comparison with article'
	},
    {
		'input': 'elizabeth lanham;elizabeth lanham', 
		'expected': True, 
		'description': 'elizabeth lanham comparison with article'
	},
    {
		'input': 'elizabeth lawrence;elizabeth lawrence', 
		'expected': True, 
		'description': 'elizabeth lawrence comparison with article'
	},
    {
		'input': 'elizabeth m lasley;mary elizabeth lasley', 
		'expected': True, 
		'description': 'elizabeth m lasley comparison with article'
	},
    {
		'input': 'elizabeth n barkett;nasry fayad vander barkett', 
		'expected': False, 
		'description': 'elizabeth n barkett comparison with article'
	},
    {
		'input': 'elizabeth s moths;miltiades s. demos', 
		'expected': False, 
		'description': 'elizabeth s moths comparison with article'
	},
    {
		'input': 'ella a ray;ella de los reyes', 
		'expected': True, 
		'description': 'ella a ray comparison with article'
	},
    {
		'input': 'ella ray;ella de los reyes', 
		'expected': True, 
		'description': 'ella ray comparison with article'
	},
    {
		'input': 'ellen dearing;ellen l deering', 
		'expected': True, 
		'description': 'ellen dearing comparison with article'
	},
    {
		'input': 'elliott diller;elliot van nostrand diller', 
		'expected': True, 
		'description': 'elliott diller comparison with article'
	},
    {
		'input': 'ellis a lasky;mortimer a. lasky', 
		'expected': False, 
		'description': 'ellis a lasky comparison with article'
	},
    {
		'input': 'ellis p leonard;ellis pierson leonard', 
		'expected': True, 
		'description': 'ellis p leonard comparison with article'
	},
    {
		'input': 'ellis t. demars;e. theodore demars', 
		'expected': True, 
		'description': 'ellis t. demars comparison with article'
	},
    {
		'input': 'ellwood d rushworth;ellwood derrick rushworth', 
		'expected': True, 
		'description': 'ellwood d rushworth comparison with article'
	},
    {
		'input': 'elmer a leslie;elmer archibald leslie', 
		'expected': True, 
		'description': 'elmer a leslie comparison with article'
	},
    {
		'input': 'elmer de gowin;elmer louis degowin', 
		'expected': True, 
		'description': 'elmer de gowin comparison with article'
	},
    {
		'input': 'elmer l lucas;elmer lawrence lucas', 
		'expected': True, 
		'description': 'elmer l lucas comparison with article'
	},
    {
		'input': 'elmer l mcbride;elmer leon mcbride', 
		'expected': True, 
		'description': 'elmer l mcbride comparison with article'
	},
    {
		'input': 'elmer l whitman;elmer leroy whitman', 
		'expected': True, 
		'description': 'elmer l whitman comparison with article'
	},
    {
		'input': 'elsa dehaas;elsa de haas', 
		'expected': True, 
		'description': 'elsa dehaas comparison with article'
	},
    {
		'input': 'elsie h leicester;katherine h. leicester', 
		'expected': False, 
		'description': 'elsie h leicester comparison with article'
	},
    {
		'input': 'elta vannorman;c. elta van norman', 
		'expected': True, 
		'description': 'elta vannorman comparison with article'
	},
    {
		'input': 'elton l quinn;elton leroy quinn', 
		'expected': True, 
		'description': 'elton l quinn comparison with article'
	},
    {
		'input': 'elva leawton;elva lawton', 
		'expected': True, 
		'description': 'elva leawton comparison with article'
	},
    {
		'input': 'elvin r latty;elvin remus latty', 
		'expected': True, 
		'description': 'elvin r latty comparison with article'
	},
    {
		'input': 'emanual delgado;jose manuel rodriguez delgado', 
		'expected': True, 
		'description': 'emanual delgado comparison with article'
	},
    {
		'input': 'emanuel levin;emanuel jack levin', 
		'expected': True, 
		'description': 'emanuel levin comparison with article'
	},
    {
		'input': 'emeric a lawrence;emeric a. lawrence', 
		'expected': True, 
		'description': 'emeric a lawrence comparison with article'
	},
    {
		'input': 'emery leffel;emory c. leffel', 
		'expected': True, 
		'description': 'emery leffel comparison with article'
	},
    {
		'input': 'emil jordan;emil leopold jordan', 
		'expected': True, 
		'description': 'emil jordan comparison with article'
	},
    {
		'input': 'emil lengyel;emil lengyel', 
		'expected': True, 
		'description': 'emil lengyel comparison with article'
	},
    {
		'input': 'emil r wesa;pierre emile deguise', 
		'expected': False, 
		'description': 'emil r wesa comparison with article'
	},
    {
		'input': 'emil w lehmann;emil wilhelm lehmann', 
		'expected': True, 
		'description': 'emil w lehmann comparison with article'
	},
    {
		'input': 'emilia larson;henrietta melia larson', 
		'expected': True, 
		'description': 'emilia larson comparison with article'
	},
    {
		'input': 'emily k landrum;emily k. landrum', 
		'expected': True, 
		'description': 'emily k landrum comparison with article'
	},
    {
		'input': 'emily l. stogdill;emily leatherman stogdill', 
		'expected': True, 
		'description': 'emily l. stogdill comparison with article'
	},
    {
		'input': 'emmerich von haam;emmerich von haam', 
		'expected': True, 
		'description': 'emmerich von haam comparison with article'
	},
    {
		'input': 'emmett l bennett;emmett leslie bennett', 
		'expected': True, 
		'description': 'emmett l bennett comparison with article'
	},
    {
		'input': 'emmy l wolff;emmy land wolff', 
		'expected': True, 
		'description': 'emmy l wolff comparison with article'
	},
    {
		'input': 'erastus h lee;erastus h. lee', 
		'expected': True, 
		'description': 'erastus h lee comparison with article'
	},
    {
		'input': 'eric b degroat;eric brooks degroat', 
		'expected': True, 
		'description': 'eric b degroat comparison with article'
	},
    {
		'input': 'erich l lehmann;erich leo lehmann', 
		'expected': True, 
		'description': 'erich l lehmann comparison with article'
	},
    {
		'input': 'ernest a dean;marshall a. dean', 
		'expected': False, 
		'description': 'ernest a dean comparison with article'
	},
    {
		'input': 'ernest e leisy;ernest erwin leisy', 
		'expected': True, 
		'description': 'ernest e leisy comparison with article'
	},
    {
		'input': 'ernest g gardner;ernest dean gardner', 
		'expected': False, 
		'description': 'ernest g gardner comparison with article'
	},
    {
		'input': 'ernest j. monica;j. ernest delmonico', 
		'expected': True, 
		'description': 'ernest j. monica comparison with article'
	},
    {
		'input': 'ernest l highbarger;ernest leslie highbarger', 
		'expected': True, 
		'description': 'ernest l highbarger comparison with article'
	},
    {
		'input': 'ernest l luther;ernest leonard luther', 
		'expected': True, 
		'description': 'ernest l luther comparison with article'
	},
    {
		'input': 'ernest leavitt;ernest e. leavitt', 
		'expected': True, 
		'description': 'ernest leavitt comparison with article'
	},
    {
		'input': 'ernest leveque;ernest j. leveque', 
		'expected': True, 
		'description': 'ernest leveque comparison with article'
	},
    {
		'input': 'ernest mader;ernest lee mader', 
		'expected': True, 
		'description': 'ernest mader comparison with article'
	},
    {
		'input': 'ernest o lawrence;ernest o. lawrence', 
		'expected': True, 
		'description': 'ernest o lawrence comparison with article'
	},
    {
		'input': 'ernest p lane;ernest preston lane', 
		'expected': True, 
		'description': 'ernest p lane comparison with article'
	},
    {
		'input': 'ernest s larson;ernest s. larson', 
		'expected': True, 
		'description': 'ernest s larson comparison with article'
	},
    {
		'input': 'ernest t de wald;ernest theodore dewald', 
		'expected': True, 
		'description': 'ernest t de wald comparison with article'
	},
    {
		'input': 'ernestine d guelich;ernestine dewes guelich', 
		'expected': True, 
		'description': 'ernestine d guelich comparison with article'
	},
    {
		'input': 'ernst levy;ernst levy', 
		'expected': True, 
		'description': 'ernst levy comparison with article'
	},
    {
		'input': 'erskine morse;erskine vance morse', 
		'expected': True, 
		'description': 'erskine morse comparison with article'
	},
    {
		'input': 'ervin denisen;ervin loren denisen', 
		'expected': True, 
		'description': 'ervin denisen comparison with article'
	},
    {
		'input': 'erving a leonard;irving a. leonard', 
		'expected': True, 
		'description': 'erving a leonard comparison with article'
	},
    {
		'input': 'estelle lacy;estelle allen delacy', 
		'expected': True, 
		'description': 'estelle lacy comparison with article'
	},
    {
		'input': 'esther d carlson;esther dewitz carlson', 
		'expected': True, 
		'description': 'esther d carlson comparison with article'
	},
    {
		'input': 'esther lee;esther lee', 
		'expected': True, 
		'description': 'esther lee comparison with article'
	},
    {
		'input': 'esther leigeber;esther marie leihgeber', 
		'expected': True, 
		'description': 'esther leigeber comparison with article'
	},
    {
		'input': 'ethel b lamore;ethel b. lamore', 
		'expected': True, 
		'description': 'ethel b lamore comparison with article'
	},
    {
		'input': 'eugene delwiche;eugene albert delwiche', 
		'expected': True, 
		'description': 'eugene delwiche comparison with article'
	},
    {
		'input': 'eugene f vanepps;eugene francis van epps', 
		'expected': True, 
		'description': 'eugene f vanepps comparison with article'
	},
    {
		'input': 'eugene j landry;eugene markley landis', 
		'expected': False, 
		'description': 'eugene j landry comparison with article'
	},
    {
		'input': 'eugene l shrader;eugene lee shrader', 
		'expected': True, 
		'description': 'eugene l shrader comparison with article'
	},
    {
		'input': 'eugene m lewis;floyd eugene lewis', 
		'expected': False, 
		'description': 'eugene m lewis comparison with article'
	},
    {
		'input': 'eugene w lepeschkin;eugene lepeschkin', 
		'expected': True, 
		'description': 'eugene w lepeschkin comparison with article'
	},
    {
		'input': 'eugene walsh;eugene lawrence walsh', 
		'expected': True, 
		'description': 'eugene walsh comparison with article'
	},
    {
		'input': 'eva l goble;eva lenora goble', 
		'expected': True, 
		'description': 'eva l goble comparison with article'
	},
    {
		'input': 'evald b lawson;evald b. lawson', 
		'expected': True, 
		'description': 'evald b lawson comparison with article'
	},
    {
		'input': 'evan l lewis;evan l. lewis', 
		'expected': True, 
		'description': 'evan l lewis comparison with article'
	},
    {
		'input': 'evans a. laroche;e. a. laroche', 
		'expected': True, 
		'description': 'evans a. laroche comparison with article'
	},
    {
		'input': 'evelyn h lewis;evelyn hodges lewis', 
		'expected': True, 
		'description': 'evelyn h lewis comparison with article'
	},
    {
		'input': 'evelyn l way;evelyn lee way', 
		'expected': True, 
		'description': 'evelyn l way comparison with article'
	},
    {
		'input': 'evelyn r landon;r. d. landon', 
		'expected': False, 
		'description': 'evelyn r landon comparison with article'
	},
    {
		'input': 'everett l keener;everett lee keener', 
		'expected': True, 
		'description': 'everett l keener comparison with article'
	},
    {
		'input': 'everett lee;everett s. lee', 
		'expected': True, 
		'description': 'everett lee comparison with article'
	},
    {
		'input': 'everett lewis;everett vernon lewis', 
		'expected': True, 
		'description': 'everett lewis comparison with article'
	},
    {
		'input': 'evert f van maanen;e. f. van maanen', 
		'expected': True, 
		'description': 'evert f van maanen comparison with article'
	},
    {
		'input': 'ewell j lytton;j. leon lichtin', 
		'expected': False, 
		'description': 'ewell j lytton comparison with article'
	},
    {
		'input': 'ezra l howell;ezra lewis howell', 
		'expected': True, 
		'description': 'ezra l howell comparison with article'
	},
    {
		'input': 'f dean mcclusky;f. dean mcclusky', 
		'expected': True, 
		'description': 'f dean mcclusky comparison with article'
	},
    {
		'input': 'f devere smith;fenelon devere smith', 
		'expected': True, 
		'description': 'f devere smith comparison with article'
	},
    {
		'input': 'f lee benns;f. lee benns', 
		'expected': True, 
		'description': 'f lee benns comparison with article'
	},
    {
		'input': 'faith l. gorrell;faith lanman gorrell', 
		'expected': True, 
		'description': 'faith l. gorrell comparison with article'
	},
    {
		'input': 'fanny a lahti;aarre kotivalo lahti', 
		'expected': False, 
		'description': 'fanny a lahti comparison with article'
	},
    {
		'input': 'faust c dewalsh;faust charles dewalsh', 
		'expected': True, 
		'description': 'faust c dewalsh comparison with article'
	},
    {
		'input': 'ferdinand lessing;ferdinand d. lessing', 
		'expected': True, 
		'description': 'ferdinand lessing comparison with article'
	},
    {
		'input': 'fitzhugh l carmichael;fitzhugh lee carmichael', 
		'expected': True, 
		'description': 'fitzhugh l carmichael comparison with article'
	},
    {
		'input': 'fitzhugh l mcree, jr;fitzhugh lee mcree', 
		'expected': True, 
		'description': 'fitzhugh l mcree, jr comparison with article'
	},
    {
		'input': 'flaria h frain;h. larue frain', 
		'expected': False, 
		'description': 'flaria h frain comparison with article'
	},
    {
		'input': 'florence alden;florence delia alden', 
		'expected': True, 
		'description': 'florence alden comparison with article'
	},
    {
		'input': 'florence b leaver;florence b. leaver', 
		'expected': True, 
		'description': 'florence b leaver comparison with article'
	},
    {
		'input': 'florence p lewis;florence parthenia lewis', 
		'expected': True, 
		'description': 'florence p lewis comparison with article'
	},
    {
		'input': 'flornece leiser;florine j. leiser', 
		'expected': True, 
		'description': 'flornece leiser comparison with article'
	},
    {
		'input': 'floy de lancey;floy w. delancey', 
		'expected': True, 
		'description': 'floy de lancey comparison with article'
	},
    {
		'input': 'floyd j. leblanc;floyd j. leblanc', 
		'expected': True, 
		'description': 'floyd j. leblanc comparison with article'
	},
    {
		'input': 'floyd l mcelroy;floyd lester mcelroy', 
		'expected': True, 
		'description': 'floyd l mcelroy comparison with article'
	},
    {
		'input': 'floyd lamb james;floyd lamb james', 
		'expected': True, 
		'description': 'floyd lamb james comparison with article'
	},
    {
		'input': 'floyd lear;floyd s. lear', 
		'expected': True, 
		'description': 'floyd lear comparison with article'
	},
    {
		'input': 'floyd s de lashmutt;floyd delashmutt', 
		'expected': True, 
		'description': 'floyd s de lashmutt comparison with article'
	},
    {
		'input': 'ford louis battles;ford lewis battles', 
		'expected': True, 
		'description': 'ford louis battles comparison with article'
	},
    {
		'input': 'forest l shoemaker;forest leroy shoemaker', 
		'expected': True, 
		'description': 'forest l shoemaker comparison with article'
	},
    {
		'input': 'forrest n lake;forrest unna lake', 
		'expected': False, 
		'description': 'forrest n lake comparison with article'
	},
    {
		'input': 'forrest w lancaster;forrest wesley lancaster', 
		'expected': True, 
		'description': 'forrest w lancaster comparison with article'
	},
    {
		'input': 'france g fell;germaine lafeuille', 
		'expected': False, 
		'description': 'france g fell comparison with article'
	},
    {
		'input': 'frances d scott;frances dean scott', 
		'expected': True, 
		'description': 'frances d scott comparison with article'
	},
    {
		'input': 'frances e craft;frances de graaff', 
		'expected': False, 
		'description': 'frances e craft comparison with article'
	},
    {
		'input': 'frances j dieg;francis j. deig', 
		'expected': False, 
		'description': 'frances j dieg comparison with article'
	},
    {
		'input': 'frances l cox;cyrus lafayette cox', 
		'expected': False, 
		'description': 'frances l cox comparison with article'
	},
    {
		'input': 'frances l tyler;frances landrum tyler', 
		'expected': True, 
		'description': 'frances l tyler comparison with article'
	},
    {
		'input': 'frances m graef;frances de graaff', 
		'expected': True, 
		'description': 'frances m graef comparison with article'
	},
    {
		'input': 'frances v holton;frances virginia lee holton', 
		'expected': True, 
		'description': 'frances v holton comparison with article'
	},
    {
		'input': 'frances van duyne;frances o. van duyne', 
		'expected': True, 
		'description': 'frances van duyne comparison with article'
	},
    {
		'input': 'frances vanvoorhis;frances van voorhis', 
		'expected': True, 
		'description': 'frances vanvoorhis comparison with article'
	},
    {
		'input': 'francis a laine;francis anthony laine', 
		'expected': True, 
		'description': 'francis a laine comparison with article'
	},
    {
		'input': 'francis c lanning;francis chowing lanning', 
		'expected': True, 
		'description': 'francis c lanning comparison with article'
	},
    {
		'input': 'francis c lathrop;francis child lathrop', 
		'expected': True, 
		'description': 'francis c lathrop comparison with article'
	},
    {
		'input': 'francis d lazanby;francis d. lazenby', 
		'expected': True, 
		'description': 'francis d lazanby comparison with article'
	},
    {
		'input': 'francis deleo;francis x. dileo', 
		'expected': True, 
		'description': 'francis deleo comparison with article'
	},
    {
		'input': 'francis e lejeune, jr;francis ernest le jeune', 
		'expected': True, 
		'description': 'francis e lejeune, jr comparison with article'
	},
    {
		'input': 'francis g lee;francis g. lee', 
		'expected': True, 
		'description': 'francis g lee comparison with article'
	},
    {
		'input': 'francis h friedman;francis lee friedman', 
		'expected': False, 
		'description': 'francis h friedman comparison with article'
	},
    {
		'input': 'francis l castleman;francis lee castleman', 
		'expected': True, 
		'description': 'francis l castleman comparison with article'
	},
    {
		'input': 'francis l harmon;francis lelande harmon', 
		'expected': True, 
		'description': 'francis l harmon comparison with article'
	},
    {
		'input': 'francis l k hsu;francis lang-kwang hsu', 
		'expected': True, 
		'description': 'francis l k hsu comparison with article'
	},
    {
		'input': 'francis l lederer;francis loeffler lederer', 
		'expected': True, 
		'description': 'francis l lederer comparison with article'
	},
    {
		'input': 'francis l. childs;francis lane childs', 
		'expected': True, 
		'description': 'francis l. childs comparison with article'
	},
    {
		'input': 'francis l. utley;francis lee utley', 
		'expected': True, 
		'description': 'francis l. utley comparison with article'
	},
    {
		'input': 'francis lee;leon francis lee', 
		'expected': True, 
		'description': 'francis lee comparison with article'
	},
    {
		'input': 'francis m la fleur;francis m. la fleur', 
		'expected': True, 
		'description': 'francis m la fleur comparison with article'
	},
    {
		'input': 'francis m lamb;francis lamb', 
		'expected': True, 
		'description': 'francis m lamb comparison with article'
	},
    {
		'input': 'francis r delfeld;francis delfeld', 
		'expected': True, 
		'description': 'francis r delfeld comparison with article'
	},
    {
		'input': 'francis weille;francis lee weille', 
		'expected': True, 
		'description': 'francis weille comparison with article'
	},
    {
		'input': 'francis x lake;francis x. lake', 
		'expected': True, 
		'description': 'francis x lake comparison with article'
	},
    {
		'input': 'francisco dela sala;francesco della-sala', 
		'expected': True, 
		'description': 'francisco dela sala comparison with article'
	},
    {
		'input': 'frank a de costa,jr;frank a. decosta', 
		'expected': True, 
		'description': 'frank a de costa,jr comparison with article'
	},
    {
		'input': 'frank a demars;frank addison demars', 
		'expected': True, 
		'description': 'frank a demars comparison with article'
	},
    {
		'input': 'frank a evger;frank e. vandiver', 
		'expected': False, 
		'description': 'frank a evger comparison with article'
	},
    {
		'input': 'frank a laurie;frank a. laurie', 
		'expected': True, 
		'description': 'frank a laurie comparison with article'
	},
    {
		'input': 'frank b mcclelland;frank deloss mcclelland', 
		'expected': False, 
		'description': 'frank b mcclelland comparison with article'
	},
    {
		'input': 'frank c larson;frank clark larson', 
		'expected': True, 
		'description': 'frank c larson comparison with article'
	},
    {
		'input': 'frank d watson;frank dekker watson', 
		'expected': True, 
		'description': 'frank d watson comparison with article'
	},
    {
		'input': 'frank delano, jr;frank lanni', 
		'expected': True, 
		'description': 'frank delano, jr comparison with article'
	},
    {
		'input': 'frank e legg;frank evariste legg', 
		'expected': True, 
		'description': 'frank e legg comparison with article'
	},
    {
		'input': 'frank e lentz;frank edwin lentz', 
		'expected': True, 
		'description': 'frank e lentz comparison with article'
	},
    {
		'input': 'frank g lankard;frank g. lankard', 
		'expected': True, 
		'description': 'frank g lankard comparison with article'
	},
    {
		'input': 'frank h lee;frank h. lee', 
		'expected': True, 
		'description': 'frank h lee comparison with article'
	},
    {
		'input': 'frank j roberts;frank lester roberts', 
		'expected': False, 
		'description': 'frank j roberts comparison with article'
	},
    {
		'input': 'frank l day;frank leighton day', 
		'expected': True, 
		'description': 'frank l day comparison with article'
	},
    {
		'input': 'frank l guest;dominic l. degiusti', 
		'expected': False, 
		'description': 'frank l guest comparison with article'
	},
    {
		'input': 'frank l howard;frank leslie howard', 
		'expected': True, 
		'description': 'frank l howard comparison with article'
	},
    {
		'input': 'frank l jennings;frank lamont jennings', 
		'expected': True, 
		'description': 'frank l jennings comparison with article'
	},
    {
		'input': 'frank l meleney;frank lamont meleney', 
		'expected': True, 
		'description': 'frank l meleney comparison with article'
	},
    {
		'input': 'frank l myers;frank lewis myers', 
		'expected': True, 
		'description': 'frank l myers comparison with article'
	},
    {
		'input': 'frank l weston;frank laurance weston', 
		'expected': True, 
		'description': 'frank l weston comparison with article'
	},
    {
		'input': 'frank laguori;frank e. liguori', 
		'expected': True, 
		'description': 'frank laguori comparison with article'
	},
    {
		'input': 'frank m de giacomo;frank degiacomo', 
		'expected': True, 
		'description': 'frank m de giacomo comparison with article'
	},
    {
		'input': 'frank m lescher;frank mills lescher', 
		'expected': True, 
		'description': 'frank m lescher comparison with article'
	},
    {
		'input': 'frank n van buren;frank newman van buren', 
		'expected': True, 
		'description': 'frank n van buren comparison with article'
	},
    {
		'input': 'frank r lacy;frank r. lacy', 
		'expected': True, 
		'description': 'frank r lacy comparison with article'
	},
    {
		'input': 'frank s schwartz;frank leroy schwartz', 
		'expected': False, 
		'description': 'frank s schwartz comparison with article'
	},
    {
		'input': 'frank t hitchcock;frank lauren hitchcock', 
		'expected': False, 
		'description': 'frank t hitchcock comparison with article'
	},
    {
		'input': 'frank t lane;frank lane', 
		'expected': True, 
		'description': 'frank t lane comparison with article'
	},
    {
		'input': 'frank w dewolf;frank w. dewolf', 
		'expected': True, 
		'description': 'frank w dewolf comparison with article'
	},
    {
		'input': 'frank w lewis;frank mendell lewis', 
		'expected': False, 
		'description': 'frank w lewis comparison with article'
	},
    {
		'input': 'frank walter clark;walter van tilburg clark', 
		'expected': False, 
		'description': 'frank walter clark comparison with article'
	},
    {
		'input': 'frank x keller;frank leuer keller', 
		'expected': False, 
		'description': 'frank x keller comparison with article'
	},
    {
		'input': 'franklin c latcham;franklin chester latcham', 
		'expected': True, 
		'description': 'franklin c latcham comparison with article'
	},
    {
		'input': 'franklin l baumer;franklin levan baumer', 
		'expected': True, 
		'description': 'franklin l baumer comparison with article'
	},
    {
		'input': 'franklyn vanhouten;franklyn bosworth van houten', 
		'expected': True, 
		'description': 'franklyn vanhouten comparison with article'
	},
    {
		'input': 'franz landsderbel;franz landsbsrger', 
		'expected': False, 
		'description': 'franz landsderbel comparison with article'
	},
    {
		'input': 'fred b deknatel;frederick brockway deknatel', 
		'expected': True, 
		'description': 'fred b deknatel comparison with article'
	},
    {
		'input': 'fred d cochran;fred derward cochran', 
		'expected': True, 
		'description': 'fred d cochran comparison with article'
	},
    {
		'input': 'fred e. deatherage;fred e. deatherage', 
		'expected': True, 
		'description': 'fred e. deatherage comparison with article'
	},
    {
		'input': 'fred fontes;fred e. lafon', 
		'expected': False, 
		'description': 'fred fontes comparison with article'
	},
    {
		'input': 'fred j lewis;fred j. lewis', 
		'expected': True, 
		'description': 'fred j lewis comparison with article'
	},
    {
		'input': 'fred l humphrey;fred lasalle humphrey', 
		'expected': True, 
		'description': 'fred l humphrey comparison with article'
	},
    {
		'input': 'fred l kerr;frederick laird kerr', 
		'expected': True, 
		'description': 'fred l kerr comparison with article'
	},
    {
		'input': 'fred l stetson;fred lea stetson', 
		'expected': True, 
		'description': 'fred l stetson comparison with article'
	},
    {
		'input': 'fred l walkey;fred leslie walkey', 
		'expected': True, 
		'description': 'fred l walkey comparison with article'
	},
    {
		'input': 'fred m moreau;fred l. lamoreau', 
		'expected': False, 
		'description': 'fred m moreau comparison with article'
	},
    {
		'input': 'fred m moreau;fred lamoreau', 
		'expected': True, 
		'description': 'fred m moreau comparison with article'
	},
    {
		'input': 'frederic h leavitt;frederic headley leavitt', 
		'expected': True, 
		'description': 'frederic h leavitt comparison with article'
	},
    {
		'input': 'frederich deibler;frederick shipp deibler', 
		'expected': True, 
		'description': 'frederich deibler comparison with article'
	},
    {
		'input': 'frederick c lane;frederic chapin lane', 
		'expected': True, 
		'description': 'frederick c lane comparison with article'
	},
    {
		'input': 'frederick c leonard;frederick c. leonard', 
		'expected': True, 
		'description': 'frederick c leonard comparison with article'
	},
    {
		'input': 'frederick c. landsittel;frederick c. landsittel', 
		'expected': True, 
		'description': 'frederick c. landsittel comparison with article'
	},
    {
		'input': 'frederick d geist;frederick denkmar geist', 
		'expected': True, 
		'description': 'frederick d geist comparison with article'
	},
    {
		'input': 'frederick d heald;frederick deforest heald', 
		'expected': True, 
		'description': 'frederick d heald comparison with article'
	},
    {
		'input': 'frederick d miller;frederick dewolfe miller', 
		'expected': True, 
		'description': 'frederick d miller comparison with article'
	},
    {
		'input': 'frederick d tootell;frederic delmont tootell', 
		'expected': True, 
		'description': 'frederick d tootell comparison with article'
	},
    {
		'input': 'frederick deuschle;frederick m. deuschle', 
		'expected': True, 
		'description': 'frederick deuschle comparison with article'
	},
    {
		'input': 'frederick l hovde;frederick lawson hovde', 
		'expected': True, 
		'description': 'frederick l hovde comparison with article'
	},
    {
		'input': 'frederick l test;frederick laurent test', 
		'expected': True, 
		'description': 'frederick l test comparison with article'
	},
    {
		'input': 'frederick lehner;frederick lehner', 
		'expected': True, 
		'description': 'frederick lehner comparison with article'
	},
    {
		'input': 'frederick lewis;frederick d. lewis', 
		'expected': True, 
		'description': 'frederick lewis comparison with article'
	},
    {
		'input': 'frederick w edwards;frederick lee edwards', 
		'expected': False, 
		'description': 'frederick w edwards comparison with article'
	},
    {
		'input': 'frederick w lenz;frederick walter lenz', 
		'expected': True, 
		'description': 'frederick w lenz comparison with article'
	},
    {
		'input': 'frederick w vanname;frederick w. van name', 
		'expected': True, 
		'description': 'frederick w vanname comparison with article'
	},
    {
		'input': 'fredrica shattuck;fredrica van trice shattuck', 
		'expected': True, 
		'description': 'fredrica shattuck comparison with article'
	},
    {
		'input': 'fredrick l rodkey;frederick lee rodkey', 
		'expected': True, 
		'description': 'fredrick l rodkey comparison with article'
	},
    {
		'input': 'fredrick lacy;frederic j. lacy', 
		'expected': True, 
		'description': 'fredrick lacy comparison with article'
	},
    {
		'input': 'fredrick w vanbuskirk;frederick william van buskirk', 
		'expected': True, 
		'description': 'fredrick w vanbuskirk comparison with article'
	},
    {
		'input': 'friderico deonis;federico de onis', 
		'expected': True, 
		'description': 'friderico deonis comparison with article'
	},
    {
		'input': 'fritz h laves;fritz laves', 
		'expected': True, 
		'description': 'fritz h laves comparison with article'
	},
    {
		'input': 'fritz l hoffmann;fritz leo hoffmann', 
		'expected': True, 
		'description': 'fritz l hoffmann comparison with article'
	},
    {
		'input': 'fritz v lenel;fritz v. lenel', 
		'expected': True, 
		'description': 'fritz v lenel comparison with article'
	},
    {
		'input': 'g alvin le page;gerald alvin lepage', 
		'expected': True, 
		'description': 'g alvin le page comparison with article'
	},
    {
		'input': 'g geoffrey langsam;gert geoffrey langsam', 
		'expected': True, 
		'description': 'g geoffrey langsam comparison with article'
	},
    {
		'input': 'g leslie miller;g. leslie miller', 
		'expected': True, 
		'description': 'g leslie miller comparison with article'
	},
    {
		'input': 'g v lantzeff;george v. lantzeff', 
		'expected': True, 
		'description': 'g v lantzeff comparison with article'
	},
    {
		'input': 'g. joseph delor;c. joseph delor', 
		'expected': False, 
		'description': 'g. joseph delor comparison with article'
	},
    {
		'input': 'gabriel lasker;gabriel w. lasker', 
		'expected': True, 
		'description': 'gabriel lasker comparison with article'
	},
    {
		'input': 'gail e densmore;gail ernest densmore', 
		'expected': True, 
		'description': 'gail e densmore comparison with article'
	},
    {
		'input': 'gardner leslie warner;c. gardner warner', 
		'expected': False, 
		'description': 'gardner leslie warner comparison with article'
	},
    {
		'input': 'garnette l fittro;garnette leona fittro', 
		'expected': True, 
		'description': 'garnette l fittro comparison with article'
	},
    {
		'input': 'garth l lee;garth l. lee', 
		'expected': True, 
		'description': 'garth l lee comparison with article'
	},
    {
		'input': 'garvin l. von eschen;garvin l. von eschen', 
		'expected': True, 
		'description': 'garvin l. von eschen comparison with article'
	},
    {
		'input': 'gendolynde m demchuk;esther m. dimchevsky', 
		'expected': False, 
		'description': 'gendolynde m demchuk comparison with article'
	},
    {
		'input': 'gene l hemmle;gene leclair hemmle', 
		'expected': True, 
		'description': 'gene l hemmle comparison with article'
	},
    {
		'input': 'genieve a w lamson;genieve lamson', 
		'expected': True, 
		'description': 'genieve a w lamson comparison with article'
	},
    {
		'input': 'george a adsit;george depue hadzsits', 
		'expected': False, 
		'description': 'george a adsit comparison with article'
	},
    {
		'input': 'george a dean;george a. dean', 
		'expected': True, 
		'description': 'george a dean comparison with article'
	},
    {
		'input': 'george a laisner;george a. laisner', 
		'expected': True, 
		'description': 'george a laisner comparison with article'
	},
    {
		'input': 'george b denton;george bion denton', 
		'expected': True, 
		'description': 'george b denton comparison with article'
	},
    {
		'input': 'george b lacey, jr;jorgen laessoe', 
		'expected': False, 
		'description': 'george b lacey, jr comparison with article'
	},
    {
		'input': 'george b van schaack;george b. van schaack', 
		'expected': True, 
		'description': 'george b van schaack comparison with article'
	},
    {
		'input': 'george deaver;george g. deaver', 
		'expected': True, 
		'description': 'george deaver comparison with article'
	},
    {
		'input': 'george deckey;george deckey', 
		'expected': True, 
		'description': 'george deckey comparison with article'
	},
    {
		'input': 'george e beick;george e. vander beke', 
		'expected': True, 
		'description': 'george e beick comparison with article'
	},
    {
		'input': 'george e lamaitre;georges eduoard lemaitre', 
		'expected': True, 
		'description': 'george e lamaitre comparison with article'
	},
    {
		'input': 'george e leedham;george edwin leedham', 
		'expected': True, 
		'description': 'george e leedham comparison with article'
	},
    {
		'input': 'george e. large;george e. large', 
		'expected': True, 
		'description': 'george e. large comparison with article'
	},
    {
		'input': 'george f deasy;george f. deasy', 
		'expected': True, 
		'description': 'george f deasy comparison with article'
	},
    {
		'input': 'george f depuy;george f. depuy', 
		'expected': True, 
		'description': 'george f depuy comparison with article'
	},
    {
		'input': 'george f smith;george van siclen smith', 
		'expected': False, 
		'description': 'george f smith comparison with article'
	},
    {
		'input': 'george f taylor;george vanderbeck taylor', 
		'expected': False, 
		'description': 'george f taylor comparison with article'
	},
    {
		'input': 'george f. lawlor;george f. lawlor', 
		'expected': True, 
		'description': 'george f. lawlor comparison with article'
	},
    {
		'input': 'george g lamb;george goodrich lamb', 
		'expected': True, 
		'description': 'george g lamb comparison with article'
	},
    {
		'input': 'george h dell;geo h. dell', 
		'expected': True, 
		'description': 'george h dell comparison with article'
	},
    {
		'input': 'george h dession;george hathaway dession', 
		'expected': True, 
		'description': 'george h dession comparison with article'
	},
    {
		'input': 'george h larson;george herbert larson', 
		'expected': True, 
		'description': 'george h larson comparison with article'
	},
    {
		'input': 'george j la lande;george albert lanyi', 
		'expected': False, 
		'description': 'george j la lande comparison with article'
	},
    {
		'input': 'george l abernethy;george lawrence abernethy', 
		'expected': True, 
		'description': 'george l abernethy comparison with article'
	},
    {
		'input': 'george l barnett;george leonard barnett', 
		'expected': True, 
		'description': 'george l barnett comparison with article'
	},
    {
		'input': 'george l clarke;george leonard clarke', 
		'expected': True, 
		'description': 'george l clarke comparison with article'
	},
    {
		'input': 'george l horner;george lewis horner', 
		'expected': True, 
		'description': 'george l horner comparison with article'
	},
    {
		'input': 'george l leffler;george l. leffler', 
		'expected': True, 
		'description': 'george l leffler comparison with article'
	},
    {
		'input': 'george l matuschka;george leslie matuschka', 
		'expected': True, 
		'description': 'george l matuschka comparison with article'
	},
    {
		'input': 'george l shuster;george lee schuster', 
		'expected': True, 
		'description': 'george l shuster comparison with article'
	},
    {
		'input': 'george l sullivan;george leonard sullivan', 
		'expected': True, 
		'description': 'george l sullivan comparison with article'
	},
    {
		'input': 'george lefevre, jr;george lefevre', 
		'expected': True, 
		'description': 'george lefevre, jr comparison with article'
	},
    {
		'input': 'george lehner;george f. j. lehner', 
		'expected': True, 
		'description': 'george lehner comparison with article'
	},
    {
		'input': 'george lensen;george alexander lensen', 
		'expected': True, 
		'description': 'george lensen comparison with article'
	},
    {
		'input': 'george leuca;george leuca', 
		'expected': True, 
		'description': 'george leuca comparison with article'
	},
    {
		'input': 'george m landrock;george m. landrock', 
		'expected': True, 
		'description': 'george m landrock comparison with article'
	},
    {
		'input': 'george n lauer;george n. lauer', 
		'expected': True, 
		'description': 'george n lauer comparison with article'
	},
    {
		'input': 'george p deyoe;george p. deyoe', 
		'expected': True, 
		'description': 'george p deyoe comparison with article'
	},
    {
		'input': 'george r lacy;george rufus lacy', 
		'expected': True, 
		'description': 'george r lacy comparison with article'
	},
    {
		'input': 'george r santillo;giorgio diaz de santillana', 
		'expected': False, 
		'description': 'george r santillo comparison with article'
	},
    {
		'input': 'george s lane;george sherman lane', 
		'expected': True, 
		'description': 'george s lane comparison with article'
	},
    {
		'input': 'george s lasher;george starr lasher', 
		'expected': True, 
		'description': 'george s lasher comparison with article'
	},
    {
		'input': 'george s lewis;george s. lewis', 
		'expected': True, 
		'description': 'george s lewis comparison with article'
	},
    {
		'input': 'george t lewis;george t. lewis', 
		'expected': True, 
		'description': 'george t lewis comparison with article'
	},
    {
		'input': 'george t pynne;george la piana', 
		'expected': False, 
		'description': 'george t pynne comparison with article'
	},
    {
		'input': 'george t vane;george thomas vane', 
		'expected': True, 
		'description': 'george t vane comparison with article'
	},
    {
		'input': 'george v leroy;george v. leroy', 
		'expected': True, 
		'description': 'george v leroy comparison with article'
	},
    {
		'input': 'george vander noot;george w. vander noot', 
		'expected': True, 
		'description': 'george vander noot comparison with article'
	},
    {
		'input': 'george vandyke;george d. van dyke', 
		'expected': True, 
		'description': 'george vandyke comparison with article'
	},
    {
		'input': 'george vanhorn;george a. van horn', 
		'expected': True, 
		'description': 'george vanhorn comparison with article'
	},
    {
		'input': 'george vlahabis;willis george labes', 
		'expected': False, 
		'description': 'george vlahabis comparison with article'
	},
    {
		'input': 'george w ladd;george e. ladd', 
		'expected': False, 
		'description': 'george w ladd comparison with article'
	},
    {
		'input': 'george w le maire;george w. lemaire', 
		'expected': True, 
		'description': 'george w le maire comparison with article'
	},
    {
		'input': 'george w lees;george winchester lees', 
		'expected': True, 
		'description': 'george w lees comparison with article'
	},
    {
		'input': 'george w vien;george levene', 
		'expected': False, 
		'description': 'george w vien comparison with article'
	},
    {
		'input': 'georgia b leach;georgia belle leach', 
		'expected': True, 
		'description': 'georgia b leach comparison with article'
	},
    {
		'input': 'georgia bell;georgia laxson bell', 
		'expected': True, 
		'description': 'georgia bell comparison with article'
	},
    {
		'input': 'georgia k del franco;georgia del franco', 
		'expected': True, 
		'description': 'georgia k del franco comparison with article'
	},
    {
		'input': 'georgia l shaffer;george lewis shaffer', 
		'expected': True, 
		'description': 'georgia l shaffer comparison with article'
	},
    {
		'input': 'gerald a leonards;gerald allen leonards', 
		'expected': True, 
		'description': 'gerald a leonards comparison with article'
	},
    {
		'input': 'gerald d meyer;gerald dennis meyer', 
		'expected': True, 
		'description': 'gerald d meyer comparison with article'
	},
    {
		'input': 'gerald desmond;gerald desmond', 
		'expected': True, 
		'description': 'gerald desmond comparison with article'
	},
    {
		'input': 'gerald langford;gerald langford', 
		'expected': True, 
		'description': 'gerald langford comparison with article'
	},
    {
		'input': 'gerald w lawlor;gerald w. lawlor', 
		'expected': True, 
		'description': 'gerald w lawlor comparison with article'
	},
    {
		'input': 'gerhard e von glahn;gerhard e. von glahn', 
		'expected': True, 
		'description': 'gerhard e von glahn comparison with article'
	},
    {
		'input': 'gerrit de jong,jr;gerrit de jong', 
		'expected': True, 
		'description': 'gerrit de jong,jr comparison with article'
	},
    {
		'input': 'gertrude a ncdounough;agnes crawford leaycraft donohugh', 
		'expected': False, 
		'description': 'gertrude a ncdounough comparison with article'
	},
    {
		'input': 'gertrude e leich;gertrude leich', 
		'expected': True, 
		'description': 'gertrude e leich comparison with article'
	},
    {
		'input': 'gertrude e way;e. leong way', 
		'expected': False, 
		'description': 'gertrude e way comparison with article'
	},
    {
		'input': 'gertrude leighton;gertrude c. k. leighton', 
		'expected': True, 
		'description': 'gertrude leighton comparison with article'
	},
    {
		'input': 'gertrude m levy;nissim m. levy', 
		'expected': False, 
		'description': 'gertrude m levy comparison with article'
	},
    {
		'input': 'gertrude van zandt;gertrude van zandt', 
		'expected': True, 
		'description': 'gertrude van zandt comparison with article'
	},
    {
		'input': 'geza de takats;geza de takats', 
		'expected': True, 
		'description': 'geza de takats comparison with article'
	},
    {
		'input': 'gilbert levine;gilbert levine', 
		'expected': True, 
		'description': 'gilbert levine comparison with article'
	},
    {
		'input': 'gilbert w lambert;gilbert w. lambert', 
		'expected': True, 
		'description': 'gilbert w lambert comparison with article'
	},
    {
		'input': 'gilman d. kirk;gilman deering kirk', 
		'expected': True, 
		'description': 'gilman d. kirk comparison with article'
	},
    {
		'input': 'gladys e leonard;gladys leonard', 
		'expected': True, 
		'description': 'gladys e leonard comparison with article'
	},
    {
		'input': 'gladys m leahy;kathleen m. leahy', 
		'expected': False, 
		'description': 'gladys m leahy comparison with article'
	},
    {
		'input': 'gladys vanarsdale;gladys van arsdale', 
		'expected': True, 
		'description': 'gladys vanarsdale comparison with article'
	},
    {
		'input': 'glen a lagrange;glen a. lagrange', 
		'expected': True, 
		'description': 'glen a lagrange comparison with article'
	},
    {
		'input': 'glend vanwormer;glenn i. van wormer', 
		'expected': True, 
		'description': 'glend vanwormer comparison with article'
	},
    {
		'input': 'glenn devine;glenn daniel devine', 
		'expected': True, 
		'description': 'glenn devine comparison with article'
	},
    {
		'input': 'glenn j lawlor, sr;glenn j. lawlor', 
		'expected': True, 
		'description': 'glenn j lawlor, sr comparison with article'
	},
    {
		'input': 'glenn l alt;glenn leslie alt', 
		'expected': True, 
		'description': 'glenn l alt comparison with article'
	},
    {
		'input': 'gloria dela vega;gloria de la vega', 
		'expected': True, 
		'description': 'gloria dela vega comparison with article'
	},
    {
		'input': 'gordon f lee;gordon canfield lee', 
		'expected': False, 
		'description': 'gordon f lee comparison with article'
	},
    {
		'input': 'gordon r dewart;gordon r. dewart', 
		'expected': True, 
		'description': 'gordon r dewart comparison with article'
	},
    {
		'input': 'gottfried delatour;gottfried delatour', 
		'expected': True, 
		'description': 'gottfried delatour comparison with article'
	},
    {
		'input': 'grace e lampe;e. w. lampe', 
		'expected': False, 
		'description': 'grace e lampe comparison with article'
	},
    {
		'input': 'grace j lawrence;bertram j. lawrence', 
		'expected': False, 
		'description': 'grace j lawrence comparison with article'
	},
    {
		'input': 'grace langford;grace langford', 
		'expected': True, 
		'description': 'grace langford comparison with article'
	},
    {
		'input': 'grace leathurby;grace c. leathurby', 
		'expected': True, 
		'description': 'grace leathurby comparison with article'
	},
    {
		'input': 'grant h laing;grant harrison laing', 
		'expected': True, 
		'description': 'grant h laing comparison with article'
	},
    {
		'input': 'gray l hunter;guy leroy hunner', 
		'expected': False, 
		'description': 'gray l hunter comparison with article'
	},
    {
		'input': 'graydon s deland, jr;graydon skerritt deland', 
		'expected': True, 
		'description': 'graydon s deland, jr comparison with article'
	},
    {
		'input': 'graydon s deland,jr;graydon skerritt deland', 
		'expected': True, 
		'description': 'graydon s deland,jr comparison with article'
	},
    {
		'input': 'gregory g la grone;gregory g. lagrone', 
		'expected': True, 
		'description': 'gregory g la grone comparison with article'
	},
    {
		'input': 'gregory j derschug;gregory j. derschug', 
		'expected': True, 
		'description': 'gregory j derschug comparison with article'
	},
    {
		'input': 'greta a lash;greta alecia lash', 
		'expected': True, 
		'description': 'greta a lash comparison with article'
	},
    {
		'input': 'gussie l teague;gussie lee teague', 
		'expected': True, 
		'description': 'gussie l teague comparison with article'
	},
    {
		'input': 'gustav a lehman;gustav adolf lehman', 
		'expected': True, 
		'description': 'gustav a lehman comparison with article'
	},
    {
		'input': 'gustave e von grunebaum;gustave e. von grunebaum', 
		'expected': True, 
		'description': 'gustave e von grunebaum comparison with article'
	},
    {
		'input': 'gustave w larson;philip gustave laurson', 
		'expected': False, 
		'description': 'gustave w larson comparison with article'
	},
    {
		'input': 'guy j desimone;guy j. de simone', 
		'expected': True, 
		'description': 'guy j desimone comparison with article'
	},
    {
		'input': 'guy j lemieux;guy j. lemieux', 
		'expected': True, 
		'description': 'guy j lemieux comparison with article'
	},
    {
		'input': 'guy l bryan;guy lee bryan', 
		'expected': True, 
		'description': 'guy l bryan comparison with article'
	},
    {
		'input': 'guy l jones;guy langston jones', 
		'expected': True, 
		'description': 'guy l jones comparison with article'
	},
    {
		'input': 'guy l odom;guy leary odom', 
		'expected': True, 
		'description': 'guy l odom comparison with article'
	},
    {
		'input': 'gwendolyn tinklin;gwendolyn laverne tinklin', 
		'expected': True, 
		'description': 'gwendolyn tinklin comparison with article'
	},
    {
		'input': 'h dean burdick;h. dean burdick', 
		'expected': True, 
		'description': 'h dean burdick comparison with article'
	},
    {
		'input': 'h jerry lavender;h. jerry lavender', 
		'expected': True, 
		'description': 'h jerry lavender comparison with article'
	},
    {
		'input': 'h leland vaughan;h. leland vaughan', 
		'expected': True, 
		'description': 'h leland vaughan comparison with article'
	},
    {
		'input': 'h leroy baumgartner;h. leroy baumgartner', 
		'expected': True, 
		'description': 'h leroy baumgartner comparison with article'
	},
    {
		'input': 'h lewis batts;lewis batts', 
		'expected': True, 
		'description': 'h lewis batts comparison with article'
	},
    {
		'input': 'h p lankelma;herman p. lankelma', 
		'expected': True, 
		'description': 'h p lankelma comparison with article'
	},
    {
		'input': 'h roger baker;roger denio baker', 
		'expected': False, 
		'description': 'h roger baker comparison with article'
	},
    {
		'input': 'haley d worthy;haley dewey worthy', 
		'expected': True, 
		'description': 'haley d worthy comparison with article'
	},
    {
		'input': 'hampden lawson;hampden c. lawson', 
		'expected': True, 
		'description': 'hampden lawson comparison with article'
	},
    {
		'input': 'hanpt g bower;holle g. deboer', 
		'expected': False, 
		'description': 'hanpt g bower comparison with article'
	},
    {
		'input': 'hans lewy;hans lewy', 
		'expected': True, 
		'description': 'hans lewy comparison with article'
	},
    {
		'input': 'hardin c van duerson;hardin van deursen', 
		'expected': True, 
		'description': 'hardin c van duerson comparison with article'
	},
    {
		'input': 'harlen l hagman;harlan lawrence hagman', 
		'expected': True, 
		'description': 'harlen l hagman comparison with article'
	},
    {
		'input': 'harold a decker;harold a. decker', 
		'expected': True, 
		'description': 'harold a decker comparison with article'
	},
    {
		'input': 'harold c davis;harold leicester davis', 
		'expected': False, 
		'description': 'harold c davis comparison with article'
	},
    {
		'input': 'harold c deutsch;harold c. deutsch', 
		'expected': True, 
		'description': 'harold c deutsch comparison with article'
	},
    {
		'input': 'harold c van horne;harold cornelius van horne', 
		'expected': True, 
		'description': 'harold c van horne comparison with article'
	},
    {
		'input': 'harold de mott hughes;harold demott hughes', 
		'expected': True, 
		'description': 'harold de mott hughes comparison with article'
	},
    {
		'input': 'harold f deutsch;harold francis deutsch', 
		'expected': True, 
		'description': 'harold f deutsch comparison with article'
	},
    {
		'input': 'harold f laroe;harold f. laroe', 
		'expected': True, 
		'description': 'harold f laroe comparison with article'
	},
    {
		'input': 'harold f lenz;harold lenz', 
		'expected': True, 
		'description': 'harold f lenz comparison with article'
	},
    {
		'input': 'harold j lang;harold locke lang', 
		'expected': False, 
		'description': 'harold j lang comparison with article'
	},
    {
		'input': 'harold j lewis;harold merrills lewis', 
		'expected': False, 
		'description': 'harold j lewis comparison with article'
	},
    {
		'input': 'harold l bond;harold lewis bond', 
		'expected': True, 
		'description': 'harold l bond comparison with article'
	},
    {
		'input': 'harold l cohen;harold larry cohen', 
		'expected': True, 
		'description': 'harold l cohen comparison with article'
	},
    {
		'input': 'harold l haley;harold leroy haley', 
		'expected': True, 
		'description': 'harold l haley comparison with article'
	},
    {
		'input': 'harold l harris;harold leo harris', 
		'expected': True, 
		'description': 'harold l harris comparison with article'
	},
    {
		'input': 'harold l. yochum;harold leland yochum', 
		'expected': True, 
		'description': 'harold l. yochum comparison with article'
	},
    {
		'input': 'harold laufman;harold laufman', 
		'expected': True, 
		'description': 'harold laufman comparison with article'
	},
    {
		'input': 'harold lewis;harold gregg lewis', 
		'expected': True, 
		'description': 'harold lewis comparison with article'
	},
    {
		'input': 'harold m devolt;harold m. devolt', 
		'expected': True, 
		'description': 'harold m devolt comparison with article'
	},
    {
		'input': 'harold n lee;harold newton lee', 
		'expected': True, 
		'description': 'harold n lee comparison with article'
	},
    {
		'input': 'harold r kugler;harold leroy kugler', 
		'expected': False, 
		'description': 'harold r kugler comparison with article'
	},
    {
		'input': 'harold r laycock;harold r. laycock', 
		'expected': True, 
		'description': 'harold r laycock comparison with article'
	},
    {
		'input': 'harold r laycock;ralph g. laycock', 
		'expected': False, 
		'description': 'harold r laycock comparison with article'
	},
    {
		'input': 'harold r leith;harold r. leith', 
		'expected': True, 
		'description': 'harold r leith comparison with article'
	},
    {
		'input': 'harold w dean;w. t. dean', 
		'expected': False, 
		'description': 'harold w dean comparison with article'
	},
    {
		'input': 'harold w lee;harold w. lee', 
		'expected': True, 
		'description': 'harold w lee comparison with article'
	},
    {
		'input': 'harold w levin;harold levin', 
		'expected': True, 
		'description': 'harold w levin comparison with article'
	},
    {
		'input': 'harold w lewis;harold walter lewis', 
		'expected': True, 
		'description': 'harold w lewis comparison with article'
	},
    {
		'input': 'harold wolf;l. harold dewolf', 
		'expected': True, 
		'description': 'harold wolf comparison with article'
	},
    {
		'input': 'harriet b denham;wallace brett donham', 
		'expected': False, 
		'description': 'harriet b denham comparison with article'
	},
    {
		'input': 'harriet c woodward;c. vann woodward', 
		'expected': False, 
		'description': 'harriet c woodward comparison with article'
	},
    {
		'input': 'harriet herring;harriet laura herring', 
		'expected': True, 
		'description': 'harriet herring comparison with article'
	},
    {
		'input': 'harriet m lewis;g. m. lewis', 
		'expected': False, 
		'description': 'harriet m lewis comparison with article'
	},
    {
		'input': 'harris s langeler;georg harris langeler', 
		'expected': False, 
		'description': 'harris s langeler comparison with article'
	},
    {
		'input': 'harris w dean;harris william dean', 
		'expected': True, 
		'description': 'harris w dean comparison with article'
	},
    {
		'input': 'harrison d le baron;h. d. lebaron', 
		'expected': True, 
		'description': 'harrison d le baron comparison with article'
	},
    {
		'input': 'harrison l chance;harrison levi chance', 
		'expected': True, 
		'description': 'harrison l chance comparison with article'
	},
    {
		'input': 'harrison l harley;harrison leroy harley', 
		'expected': True, 
		'description': 'harrison l harley comparison with article'
	},
    {
		'input': 'harry b decook;harry b. decook', 
		'expected': True, 
		'description': 'harry b decook comparison with article'
	},
    {
		'input': 'harry b van dyke;harry b. van dyke', 
		'expected': True, 
		'description': 'harry b van dyke comparison with article'
	},
    {
		'input': 'harry d taft;harry derward taft', 
		'expected': True, 
		'description': 'harry d taft comparison with article'
	},
    {
		'input': 'harry d wolf;harry demerle wolf', 
		'expected': True, 
		'description': 'harry d wolf comparison with article'
	},
    {
		'input': 'harry e dassau;walter edward dessauer', 
		'expected': False, 
		'description': 'harry e dassau comparison with article'
	},
    {
		'input': 'harry e. le fever;harry lefever', 
		'expected': True, 
		'description': 'harry e. le fever comparison with article'
	},
    {
		'input': 'harry g laforge;harry g. laforge', 
		'expected': True, 
		'description': 'harry g laforge comparison with article'
	},
    {
		'input': 'harry h leonard;harry wesley leonard', 
		'expected': False, 
		'description': 'harry h leonard comparison with article'
	},
    {
		'input': 'harry i leddel;harry edwall', 
		'expected': False, 
		'description': 'harry i leddel comparison with article'
	},
    {
		'input': 'harry j deuel;harry j. deuel', 
		'expected': True, 
		'description': 'harry j deuel comparison with article'
	},
    {
		'input': 'harry j digirolamo,sr;harry j. de girolamo', 
		'expected': True, 
		'description': 'harry j digirolamo,sr comparison with article'
	},
    {
		'input': 'harry l chant;harry leddy chant', 
		'expected': True, 
		'description': 'harry l chant comparison with article'
	},
    {
		'input': 'harry l hoffee;harry lee hoffee', 
		'expected': True, 
		'description': 'harry l hoffee comparison with article'
	},
    {
		'input': 'harry l lantz;harry lantz', 
		'expected': True, 
		'description': 'harry l lantz comparison with article'
	},
    {
		'input': 'harry l solberg;harry leland solberg', 
		'expected': True, 
		'description': 'harry l solberg comparison with article'
	},
    {
		'input': 'harry l taylor;harry leroy taylor', 
		'expected': True, 
		'description': 'harry l taylor comparison with article'
	},
    {
		'input': 'harry landis;harry m. landis', 
		'expected': True, 
		'description': 'harry landis comparison with article'
	},
    {
		'input': 'harry lee;douglas harry kedgwin lee', 
		'expected': True, 
		'description': 'harry lee comparison with article'
	},
    {
		'input': 'harry levy;harry levy', 
		'expected': True, 
		'description': 'harry levy comparison with article'
	},
    {
		'input': 'harry m jr langsford;harry langsford', 
		'expected': True, 
		'description': 'harry m jr langsford comparison with article'
	},
    {
		'input': 'harry r larson;r. a. larson', 
		'expected': False, 
		'description': 'harry r larson comparison with article'
	},
    {
		'input': 'harry s bowman;harry lake bowman', 
		'expected': False, 
		'description': 'harry s bowman comparison with article'
	},
    {
		'input': 'harry s duerow;harry aaron derow', 
		'expected': False, 
		'description': 'harry s duerow comparison with article'
	},
    {
		'input': 'harry s legum;samuel legum', 
		'expected': True, 
		'description': 'harry s legum comparison with article'
	},
    {
		'input': 'harry s vandiver;harry schultz vandiver', 
		'expected': True, 
		'description': 'harry s vandiver comparison with article'
	},
    {
		'input': 'harry t levin;harry tuchman levin', 
		'expected': True, 
		'description': 'harry t levin comparison with article'
	},
    {
		'input': 'harry v langeluttig;h. v. langeluttig', 
		'expected': True, 
		'description': 'harry v langeluttig comparison with article'
	},
    {
		'input': 'harry w le fevre, iii;harry wilson lefevre', 
		'expected': True, 
		'description': 'harry w le fevre, iii comparison with article'
	},
    {
		'input': 'harry w leacock;emory w. luccock', 
		'expected': False, 
		'description': 'harry w leacock comparison with article'
	},
    {
		'input': 'harry w. vanneman;harry walter vanneman', 
		'expected': True, 
		'description': 'harry w. vanneman comparison with article'
	},
    {
		'input': 'harvey b densmore;harvey bruce densmore', 
		'expected': True, 
		'description': 'harvey b densmore comparison with article'
	},
    {
		'input': 'harvey b vanderford;harvey birch vanderford', 
		'expected': True, 
		'description': 'harvey b vanderford comparison with article'
	},
    {
		'input': 'harvey c lehman;harvey christian lehman', 
		'expected': True, 
		'description': 'harvey c lehman comparison with article'
	},
    {
		'input': 'harvey e lehman;harvey eugene lehman', 
		'expected': True, 
		'description': 'harvey e lehman comparison with article'
	},
    {
		'input': 'harvey j brown;harvey de bruine', 
		'expected': True, 
		'description': 'harvey j brown comparison with article'
	},
    {
		'input': 'harvey l carter;harvey lewis carter', 
		'expected': True, 
		'description': 'harvey l carter comparison with article'
	},
    {
		'input': 'harvey l sweetman;harvey leroy sweetman', 
		'expected': True, 
		'description': 'harvey l sweetman comparison with article'
	},
    {
		'input': 'harvey lee lantz;harvey lee lantz', 
		'expected': True, 
		'description': 'harvey lee lantz comparison with article'
	},
    {
		'input': 'harwood l childs;harwood lawrence childs', 
		'expected': True, 
		'description': 'harwood l childs comparison with article'
	},
    {
		'input': 'hazel b shands;hazel lee shands', 
		'expected': False, 
		'description': 'hazel b shands comparison with article'
	},
    {
		'input': 'hazel d howe;hazel dell howe', 
		'expected': True, 
		'description': 'hazel d howe comparison with article'
	},
    {
		'input': 'hazel g vance;g. a. vance', 
		'expected': False, 
		'description': 'hazel g vance comparison with article'
	},
    {
		'input': 'hazel l morrison;l. leotus morrison', 
		'expected': False, 
		'description': 'hazel l morrison comparison with article'
	},
    {
		'input': 'hazel m. lewis;hazel m. lewis', 
		'expected': True, 
		'description': 'hazel m. lewis comparison with article'
	},
    {
		'input': 'hazel van ness;hazel van ness', 
		'expected': True, 
		'description': 'hazel van ness comparison with article'
	},
    {
		'input': 'hector h lee;hector lee', 
		'expected': True, 
		'description': 'hector h lee comparison with article'
	},
    {
		'input': 'heinz m vonfoerster;heinz vonfoerster', 
		'expected': True, 
		'description': 'heinz m vonfoerster comparison with article'
	},
    {
		'input': 'helen a denyes;helen arliss denyes', 
		'expected': True, 
		'description': 'helen a denyes comparison with article'
	},
    {
		'input': 'helen c deibert;franklin c. daiber', 
		'expected': False, 
		'description': 'helen c deibert comparison with article'
	},
    {
		'input': 'helen g harris;gould leach harris', 
		'expected': False, 
		'description': 'helen g harris comparison with article'
	},
    {
		'input': 'helen h law;helen hull law', 
		'expected': True, 
		'description': 'helen h law comparison with article'
	},
    {
		'input': 'helen l richey;helen lenore richey', 
		'expected': True, 
		'description': 'helen l richey comparison with article'
	},
    {
		'input': 'helen l smith;helen leonore smith', 
		'expected': True, 
		'description': 'helen l smith comparison with article'
	},
    {
		'input': 'helen l stevens;helen larson stevens', 
		'expected': True, 
		'description': 'helen l stevens comparison with article'
	},
    {
		'input': 'helen l van gilder;helen louise van gilder', 
		'expected': True, 
		'description': 'helen l van gilder comparison with article'
	},
    {
		'input': 'helen l wikoff;helen landman wikoff', 
		'expected': True, 
		'description': 'helen l wikoff comparison with article'
	},
    {
		'input': 'helen lamprechet;helen lamprecht', 
		'expected': True, 
		'description': 'helen lamprechet comparison with article'
	},
    {
		'input': 'helen loskiewicz;helen r. washkovich', 
		'expected': False, 
		'description': 'helen loskiewicz comparison with article'
	},
    {
		'input': 'helen ward;helen lavina ward', 
		'expected': True, 
		'description': 'helen ward comparison with article'
	},
    {
		'input': 'helmit h vonerfe;helmut h. von erffa', 
		'expected': True, 
		'description': 'helmit h vonerfe comparison with article'
	},
    {
		'input': 'helmit h vonerfer;helmut h. von erffa', 
		'expected': True, 
		'description': 'helmit h vonerfer comparison with article'
	},
    {
		'input': 'heman l ibsen;heman lauritz ibsen', 
		'expected': True, 
		'description': 'heman l ibsen comparison with article'
	},
    {
		'input': 'henning larson;henning larsen', 
		'expected': True, 
		'description': 'henning larson comparison with article'
	},
    {
		'input': 'henry a lardy;henry arnold lardy', 
		'expected': True, 
		'description': 'henry a lardy comparison with article'
	},
    {
		'input': 'henry a lasch;henry lasch', 
		'expected': True, 
		'description': 'henry a lasch comparison with article'
	},
    {
		'input': 'henry a lepper;henry albert lepper', 
		'expected': True, 
		'description': 'henry a lepper comparison with article'
	},
    {
		'input': 'henry a melander;axel leonard melander', 
		'expected': False, 
		'description': 'henry a melander comparison with article'
	},
    {
		'input': 'henry a vandiest;alice e. van diest', 
		'expected': False, 
		'description': 'henry a vandiest comparison with article'
	},
    {
		'input': 'henry b. lacey;henry b. lacey', 
		'expected': True, 
		'description': 'henry b. lacey comparison with article'
	},
    {
		'input': 'henry d bockus, sr;henry leroy bockus', 
		'expected': False, 
		'description': 'henry d bockus, sr comparison with article'
	},
    {
		'input': 'henry d cay;henry george dekay', 
		'expected': False, 
		'description': 'henry d cay comparison with article'
	},
    {
		'input': 'henry d lederer;henry david lederer', 
		'expected': True, 
		'description': 'henry d lederer comparison with article'
	},
    {
		'input': 'henry d smyth;henry dewolf smyth', 
		'expected': True, 
		'description': 'henry d smyth comparison with article'
	},
    {
		'input': 'henry de vries,jr;henry p. de vries', 
		'expected': True, 
		'description': 'henry de vries,jr comparison with article'
	},
    {
		'input': 'henry g lew;henry g. lew', 
		'expected': True, 
		'description': 'henry g lew comparison with article'
	},
    {
		'input': 'henry h bergmann;henry leonard birge', 
		'expected': False, 
		'description': 'henry h bergmann comparison with article'
	},
    {
		'input': 'henry k metcalf;keyes dewitt metcalf', 
		'expected': False, 
		'description': 'henry k metcalf comparison with article'
	},
    {
		'input': 'henry l clarke;henry leland clarke', 
		'expected': True, 
		'description': 'henry l clarke comparison with article'
	},
    {
		'input': 'henry l dean;henry lee dean', 
		'expected': True, 
		'description': 'henry l dean comparison with article'
	},
    {
		'input': 'henry l kragbill;henry lawrence kraybill', 
		'expected': True, 
		'description': 'henry l kragbill comparison with article'
	},
    {
		'input': 'henry l langhaar;henry l. langhaar', 
		'expected': True, 
		'description': 'henry l langhaar comparison with article'
	},
    {
		'input': 'henry l lucas, jr;henry lawrence lucas', 
		'expected': True, 
		'description': 'henry l lucas, jr comparison with article'
	},
    {
		'input': 'henry l marlowe;l. dennis marlowe', 
		'expected': False, 
		'description': 'henry l marlowe comparison with article'
	},
    {
		'input': 'henry l miller;henry laurence miller', 
		'expected': True, 
		'description': 'henry l miller comparison with article'
	},
    {
		'input': 'henry l robinson;henry leon robinson', 
		'expected': True, 
		'description': 'henry l robinson comparison with article'
	},
    {
		'input': 'henry l seaver;henry latimer seaver', 
		'expected': True, 
		'description': 'henry l seaver comparison with article'
	},
    {
		'input': 'henry l smith;henry ladd smith', 
		'expected': True, 
		'description': 'henry l smith comparison with article'
	},
    {
		'input': 'henry l swint;henry lee swint', 
		'expected': True, 
		'description': 'henry l swint comparison with article'
	},
    {
		'input': 'henry l van mater;henry lear van mater', 
		'expected': True, 
		'description': 'henry l van mater comparison with article'
	},
    {
		'input': 'henry l warfres;l. s. vander werf', 
		'expected': False, 
		'description': 'henry l warfres comparison with article'
	},
    {
		'input': 'henry leffert;henry leffert', 
		'expected': True, 
		'description': 'henry leffert comparison with article'
	},
    {
		'input': 'henry negro;enrico de negri', 
		'expected': True, 
		'description': 'henry negro comparison with article'
	},
    {
		'input': 'henry p lang;paul henry lang', 
		'expected': True, 
		'description': 'henry p lang comparison with article'
	},
    {
		'input': 'henry r lefevre;reginald r. lefebvre', 
		'expected': False, 
		'description': 'henry r lefevre comparison with article'
	},
    {
		'input': 'henry t van lith;thomas henry leith', 
		'expected': True, 
		'description': 'henry t van lith comparison with article'
	},
    {
		'input': 'henry t van lith;thomas henry lith', 
		'expected': True, 
		'description': 'henry t van lith comparison with article'
	},
    {
		'input': 'henry w vonholt;henry w. von holt', 
		'expected': True, 
		'description': 'henry w vonholt comparison with article'
	},
    {
		'input': 'henry wilkins lewis;henry wilkins lewis', 
		'expected': True, 
		'description': 'henry wilkins lewis comparison with article'
	},
    {
		'input': 'herbert a deane;herbert a. deane', 
		'expected': True, 
		'description': 'herbert a deane comparison with article'
	},
    {
		'input': 'herbert a laitinen;herbert a. laitinen', 
		'expected': True, 
		'description': 'herbert a laitinen comparison with article'
	},
    {
		'input': 'herbert c vandeventer;herbert c. van deventer', 
		'expected': True, 
		'description': 'herbert c vandeventer comparison with article'
	},
    {
		'input': 'herbert d landahl;herbert daniel landahl', 
		'expected': True, 
		'description': 'herbert d landahl comparison with article'
	},
    {
		'input': 'herbert denny orth;herbert denny orth', 
		'expected': True, 
		'description': 'herbert denny orth comparison with article'
	},
    {
		'input': 'herbert deresiewicz;herbert deresiewicz', 
		'expected': True, 
		'description': 'herbert deresiewicz comparison with article'
	},
    {
		'input': 'herbert f langdon;herbert f. langdon', 
		'expected': True, 
		'description': 'herbert f langdon comparison with article'
	},
    {
		'input': 'herbert i bon haden;herbert ira von haden', 
		'expected': True, 
		'description': 'herbert i bon haden comparison with article'
	},
    {
		'input': 'herbert j langen;herbert j. langen', 
		'expected': True, 
		'description': 'herbert j langen comparison with article'
	},
    {
		'input': 'herbert l anderson;herbert lawrence anderson', 
		'expected': True, 
		'description': 'herbert l anderson comparison with article'
	},
    {
		'input': 'herbert l bridges;herbert lee bridges', 
		'expected': True, 
		'description': 'herbert l bridges comparison with article'
	},
    {
		'input': 'herbert l creek;herbert le sourd creek', 
		'expected': True, 
		'description': 'herbert l creek comparison with article'
	},
    {
		'input': 'herbert l gilman;herbert lester gilman', 
		'expected': True, 
		'description': 'herbert l gilman comparison with article'
	},
    {
		'input': 'herbert l sherman;herbert leroy sherman', 
		'expected': True, 
		'description': 'herbert l sherman comparison with article'
	},
    {
		'input': 'herbert lattig;herbert e lattig', 
		'expected': True, 
		'description': 'herbert lattig comparison with article'
	},
    {
		'input': 'herbert ler steele;herbert l. steele', 
		'expected': True, 
		'description': 'herbert ler steele comparison with article'
	},
    {
		'input': 'herbert meritt;herbert dean meritt', 
		'expected': True, 
		'description': 'herbert meritt comparison with article'
	},
    {
		'input': 'herbert w beckerath;herbert von beckerath', 
		'expected': True, 
		'description': 'herbert w beckerath comparison with article'
	},
    {
		'input': 'herman donovan;herman lee donovan', 
		'expected': True, 
		'description': 'herman donovan comparison with article'
	},
    {
		'input': 'herman g laughlin;herman gleyn laughlin', 
		'expected': True, 
		'description': 'herman g laughlin comparison with article'
	},
    {
		'input': 'herman w larson;curtis w. r. larson', 
		'expected': False, 
		'description': 'herman w larson comparison with article'
	},
    {
		'input': 'herman w larson;herman w. larson', 
		'expected': True, 
		'description': 'herman w larson comparison with article'
	},
    {
		'input': 'herold l kooser;herold lang kooser', 
		'expected': True, 
		'description': 'herold l kooser comparison with article'
	},
    {
		'input': 'herrell degraff;herrell franklin degraff', 
		'expected': True, 
		'description': 'herrell degraff comparison with article'
	},
    {
		'input': 'herschel l roman;herschel lewis roman', 
		'expected': True, 
		'description': 'herschel l roman comparison with article'
	},
    {
		'input': 'hilmer h laude;hilmer henry laude', 
		'expected': True, 
		'description': 'hilmer h laude comparison with article'
	},
    {
		'input': 'homer r dehoney;r. w. dehoney', 
		'expected': False, 
		'description': 'homer r dehoney comparison with article'
	},
    {
		'input': 'homer r lewis;homer collier lewis', 
		'expected': False, 
		'description': 'homer r lewis comparison with article'
	},
    {
		'input': 'horace b vanvalkenburgh;horace b. van valkenburgh', 
		'expected': True, 
		'description': 'horace b vanvalkenburgh comparison with article'
	},
    {
		'input': 'horace l barnett;horace leslie barnett', 
		'expected': True, 
		'description': 'horace l barnett comparison with article'
	},
    {
		'input': 'horace l friess;horace leland friess', 
		'expected': True, 
		'description': 'horace l friess comparison with article'
	},
    {
		'input': 'horace w leet;horace w. leet', 
		'expected': True, 
		'description': 'horace w leet comparison with article'
	},
    {
		'input': 'horton laude;horton m. laude', 
		'expected': True, 
		'description': 'horton laude comparison with article'
	},
    {
		'input': 'howard a lane;howard a. lane', 
		'expected': True, 
		'description': 'howard a lane comparison with article'
	},
    {
		'input': 'howard boatwright;howard leake boatwright', 
		'expected': True, 
		'description': 'howard boatwright comparison with article'
	},
    {
		'input': 'howard d smethers;howard dewight smethers', 
		'expected': True, 
		'description': 'howard d smethers comparison with article'
	},
    {
		'input': 'howard l dunlap;howard leroy dunlap', 
		'expected': True, 
		'description': 'howard l dunlap comparison with article'
	},
    {
		'input': 'howard l hall;howard lewis hall', 
		'expected': True, 
		'description': 'howard l hall comparison with article'
	},
    {
		'input': 'howard l hamilton;howard laverne hamilton', 
		'expected': True, 
		'description': 'howard l hamilton comparison with article'
	},
    {
		'input': 'howard l lange;howard l. lange', 
		'expected': True, 
		'description': 'howard l lange comparison with article'
	},
    {
		'input': 'howard l nostrand;howard lee nostrand', 
		'expected': True, 
		'description': 'howard l nostrand comparison with article'
	},
    {
		'input': 'howard levene;howard levene', 
		'expected': True, 
		'description': 'howard levene comparison with article'
	},
    {
		'input': 'howard levi;howard levi', 
		'expected': True, 
		'description': 'howard levi comparison with article'
	},
    {
		'input': 'howard mckinney;howard decker mckinney', 
		'expected': True, 
		'description': 'howard mckinney comparison with article'
	},
    {
		'input': 'howard o deming;howard o. deming', 
		'expected': True, 
		'description': 'howard o deming comparison with article'
	},
    {
		'input': 'howard o. deay;howard owen deay', 
		'expected': True, 
		'description': 'howard o. deay comparison with article'
	},
    {
		'input': 'howard r lamar;howard roberts lamar', 
		'expected': True, 
		'description': 'howard r lamar comparison with article'
	},
    {
		'input': 'howard r mitchell;howard lee mitchell', 
		'expected': False, 
		'description': 'howard r mitchell comparison with article'
	},
    {
		'input': 'howard w larsh;howard william larsh', 
		'expected': True, 
		'description': 'howard w larsh comparison with article'
	},
    {
		'input': 'howard w lattin;gerald w. lattin', 
		'expected': False, 
		'description': 'howard w lattin comparison with article'
	},
    {
		'input': 'howard w lewis;howard thompson lewis', 
		'expected': False, 
		'description': 'howard w lewis comparison with article'
	},
    {
		'input': 'hubert g dearicks;hubert g. derrick', 
		'expected': True, 
		'description': 'hubert g dearicks comparison with article'
	},
    {
		'input': 'hubert olin;hubert leonard olin', 
		'expected': True, 
		'description': 'hubert olin comparison with article'
	},
    {
		'input': 'hubert w lamb;hubert weldon lamb', 
		'expected': True, 
		'description': 'hubert w lamb comparison with article'
	},
    {
		'input': 'huey kesing ay lee;kwan hua lee', 
		'expected': False, 
		'description': 'huey kesing ay lee comparison with article'
	},
    {
		'input': 'hugh d. laughlin;hugh donald laughlin', 
		'expected': True, 
		'description': 'hugh d. laughlin comparison with article'
	},
    {
		'input': 'hugh hodgson;hugh leslie hodgson', 
		'expected': True, 
		'description': 'hugh hodgson comparison with article'
	},
    {
		'input': 'hugh t lefler;hugh talmage lefler', 
		'expected': True, 
		'description': 'hugh t lefler comparison with article'
	},
    {
		'input': 'hugo l blownquist;hugo leander blomquist', 
		'expected': True, 
		'description': 'hugo l blownquist comparison with article'
	},
    {
		'input': 'hulda garrett;hulda van steeter garrett', 
		'expected': True, 
		'description': 'hulda garrett comparison with article'
	},
    {
		'input': 'ida o haigh;ida deck haigh', 
		'expected': False, 
		'description': 'ida o haigh comparison with article'
	},
    {
		'input': 'ike f. deeter;ike deeter', 
		'expected': True, 
		'description': 'ike f. deeter comparison with article'
	},
    {
		'input': 'ina leone strom;ina l. strom', 
		'expected': True, 
		'description': 'ina leone strom comparison with article'
	},
    {
		'input': 'ina van stan;ina vanstan', 
		'expected': True, 
		'description': 'ina van stan comparison with article'
	},
    {
		'input': 'ira d porterfield;ira deward porterfield', 
		'expected': True, 
		'description': 'ira d porterfield comparison with article'
	},
    {
		'input': 'ira l collier;ira leonard collier', 
		'expected': True, 
		'description': 'ira l collier comparison with article'
	},
    {
		'input': 'ira la rivers;ira larivers', 
		'expected': True, 
		'description': 'ira la rivers comparison with article'
	},
    {
		'input': 'ira v lee;ira d. lee', 
		'expected': False, 
		'description': 'ira v lee comparison with article'
	},
    {
		'input': 'ira williams;ira lawson williams', 
		'expected': True, 
		'description': 'ira williams comparison with article'
	},
    {
		'input': 'irene e van osdel;edgar bates van osdel', 
		'expected': False, 
		'description': 'irene e van osdel comparison with article'
	},
    {
		'input': 'irene s lashey;karl spencer lashley', 
		'expected': False, 
		'description': 'irene s lashey comparison with article'
	},
    {
		'input': 'irene s lavant;leopoldo santiago lavandero', 
		'expected': False, 
		'description': 'irene s lavant comparison with article'
	},
    {
		'input': 'irving h lepow;irwin howard lepow', 
		'expected': False, 
		'description': 'irving h lepow comparison with article'
	},
    {
		'input': 'irving j lee;irving j. lee', 
		'expected': True, 
		'description': 'irving j lee comparison with article'
	},
    {
		'input': 'irving l janis;irving lester janis', 
		'expected': True, 
		'description': 'irving l janis comparison with article'
	},
    {
		'input': 'irving o dein;irving o. dein', 
		'expected': True, 
		'description': 'irving o dein comparison with article'
	},
    {
		'input': 'irving peterson;irving leonard peterson', 
		'expected': True, 
		'description': 'irving peterson comparison with article'
	},
    {
		'input': 'irwin i levine;l. i. levine', 
		'expected': False, 
		'description': 'irwin i levine comparison with article'
	},
    {
		'input': 'isaac leroy domingus;isaac leroy domingos', 
		'expected': True, 
		'description': 'isaac leroy domingus comparison with article'
	},
    {
		'input': 'isaac lewin;isaac lewin', 
		'expected': True, 
		'description': 'isaac lewin comparison with article'
	},
    {
		'input': 'isabel lewis;isabel boyd lewis', 
		'expected': True, 
		'description': 'isabel lewis comparison with article'
	},
    {
		'input': 'isabelle r lebreton;dagmar renshaw lebreton', 
		'expected': False, 
		'description': 'isabelle r lebreton comparison with article'
	},
    {
		'input': 'isidore l robbins;isidore leon robbins', 
		'expected': True, 
		'description': 'isidore l robbins comparison with article'
	},
    {
		'input': 'ivan l hill;ivan leroy hill', 
		'expected': True, 
		'description': 'ivan l hill comparison with article'
	},
    {
		'input': 'ivan l little;ivan lee little', 
		'expected': True, 
		'description': 'ivan l little comparison with article'
	},
    {
		'input': 'ivan m lee;ivan m. lee', 
		'expected': True, 
		'description': 'ivan m lee comparison with article'
	},
    {
		'input': 'ivor d spencer;ivor debenham spencer', 
		'expected': True, 
		'description': 'ivor d spencer comparison with article'
	},
    {
		'input': 'j andreas (joseph andreas) de marco;rene j. marcou', 
		'expected': False, 
		'description': 'j andreas (joseph andreas) de marco comparison with article'
	},
    {
		'input': 'j dean swift;j. dean swift', 
		'expected': True, 
		'description': 'j dean swift comparison with article'
	},
    {
		'input': 'j deryl hart;julian deryl hart', 
		'expected': True, 
		'description': 'j deryl hart comparison with article'
	},
    {
		'input': 'j howard demar;howard h. lamar', 
		'expected': False, 
		'description': 'j howard demar comparison with article'
	},
    {
		'input': 'j lawton ellis;j. lawton ellis', 
		'expected': True, 
		'description': 'j lawton ellis comparison with article'
	},
    {
		'input': 'j layton fraser;thomas layton fraser', 
		'expected': False, 
		'description': 'j layton fraser comparison with article'
	},
    {
		'input': 'j leonard brandt;j. leonard brandt', 
		'expected': True, 
		'description': 'j leonard brandt comparison with article'
	},
    {
		'input': 'j leonard goldner;joseph leonard goldner', 
		'expected': True, 
		'description': 'j leonard goldner comparison with article'
	},
    {
		'input': 'j leroy anderson;leray j. anderson', 
		'expected': True, 
		'description': 'j leroy anderson comparison with article'
	},
    {
		'input': 'j lewis allison;joseph lewis allison', 
		'expected': True, 
		'description': 'j lewis allison comparison with article'
	},
    {
		'input': 'j lewis maynard;j. lewis maynard', 
		'expected': True, 
		'description': 'j lewis maynard comparison with article'
	},
    {
		'input': 'j paul leonard;j paul leonard', 
		'expected': True, 
		'description': 'j paul leonard comparison with article'
	},
    {
		'input': 'j s ladd thomas;j. s. ladd thomas', 
		'expected': True, 
		'description': 'j s ladd thomas comparison with article'
	},
    {
		'input': 'j warren lee;james warren lee', 
		'expected': True, 
		'description': 'j warren lee comparison with article'
	},
    {
		'input': 'j. murray lee;j. murray lee', 
		'expected': True, 
		'description': 'j. murray lee comparison with article'
	},
    {
		'input': 'j. raymond derby;j. raymond derby', 
		'expected': True, 
		'description': 'j. raymond derby comparison with article'
	},
    {
		'input': 'j. wayne ley;j. wayne ley', 
		'expected': True, 
		'description': 'j. wayne ley comparison with article'
	},
    {
		'input': 'jack a denison;jack a. denison', 
		'expected': True, 
		'description': 'jack a denison comparison with article'
	},
    {
		'input': 'jack j detzler;jack j. detzler', 
		'expected': True, 
		'description': 'jack j detzler comparison with article'
	},
    {
		'input': 'jack layton;jack malcolm layton', 
		'expected': True, 
		'description': 'jack layton comparison with article'
	},
    {
		'input': 'jack lenhart;jack lenhart', 
		'expected': True, 
		'description': 'jack lenhart comparison with article'
	},
    {
		'input': 'jack levine;jack levine', 
		'expected': True, 
		'description': 'jack levine comparison with article'
	},
    {
		'input': 'jack r leonards;jack ralph leonards', 
		'expected': True, 
		'description': 'jack r leonards comparison with article'
	},
    {
		'input': 'jacob a o larsen;jakob aall ottesen larsen', 
		'expected': True, 
		'description': 'jacob a o larsen comparison with article'
	},
    {
		'input': 'jacob f leibald;f. l. liebolt', 
		'expected': False, 
		'description': 'jacob f leibald comparison with article'
	},
    {
		'input': 'jacob haas;jacob anton de haas', 
		'expected': True, 
		'description': 'jacob haas comparison with article'
	},
    {
		'input': 'jacob levine;jacob levine', 
		'expected': True, 
		'description': 'jacob levine comparison with article'
	},
    {
		'input': 'jacob levitt;jacob levitt', 
		'expected': True, 
		'description': 'jacob levitt comparison with article'
	},
    {
		'input': 'jacob van ek;jacob van ek', 
		'expected': True, 
		'description': 'jacob van ek comparison with article'
	},
    {
		'input': 'jacob vanderzee;jacob van der zee', 
		'expected': True, 
		'description': 'jacob vanderzee comparison with article'
	},
    {
		'input': 'jacqueline a rochelle;augustine larochelle', 
		'expected': True, 
		'description': 'jacqueline a rochelle comparison with article'
	},
    {
		'input': 'jacqueline e delaharp;jacqueline de la harpe', 
		'expected': True, 
		'description': 'jacqueline e delaharp comparison with article'
	},
    {
		'input': 'jadan g jr lee;jordan g. lee', 
		'expected': False, 
		'description': 'jadan g jr lee comparison with article'
	},
    {
		'input': 'james b lewis;b. roland lewis', 
		'expected': False, 
		'description': 'james b lewis comparison with article'
	},
    {
		'input': 'james b ley;b. james ley', 
		'expected': True, 
		'description': 'james b ley comparison with article'
	},
    {
		'input': 'james c landon;f. c. lendrum', 
		'expected': False, 
		'description': 'james c landon comparison with article'
	},
    {
		'input': 'james c mc leod;james currie mcleod', 
		'expected': True, 
		'description': 'james c mc leod comparison with article'
	},
    {
		'input': 'james d decker;james d. decker', 
		'expected': True, 
		'description': 'james d decker comparison with article'
	},
    {
		'input': 'james d heard;james delaven heard', 
		'expected': True, 
		'description': 'james d heard comparison with article'
	},
    {
		'input': 'james d. wilson;james dean wilson', 
		'expected': True, 
		'description': 'james d. wilson comparison with article'
	},
    {
		'input': 'james derr;james g. derr', 
		'expected': True, 
		'description': 'james derr comparison with article'
	},
    {
		'input': 'james dewey;james edwin dewey', 
		'expected': True, 
		'description': 'james dewey comparison with article'
	},
    {
		'input': 'james e deese;james earle deese', 
		'expected': True, 
		'description': 'james e deese comparison with article'
	},
    {
		'input': 'james e dew;james e. dew', 
		'expected': True, 
		'description': 'james e dew comparison with article'
	},
    {
		'input': 'james e lebensohn;james elzer lebensohn', 
		'expected': True, 
		'description': 'james e lebensohn comparison with article'
	},
    {
		'input': 'james e legates;james edward legates', 
		'expected': True, 
		'description': 'james e legates comparison with article'
	},
    {
		'input': 'james e lewis;james e. lewis', 
		'expected': True, 
		'description': 'james e lewis comparison with article'
	},
    {
		'input': 'james f campbell;james lawder gamble', 
		'expected': False, 
		'description': 'james f campbell comparison with article'
	},
    {
		'input': 'james g vanderpool;james g. vanderpool', 
		'expected': True, 
		'description': 'james g vanderpool comparison with article'
	},
    {
		'input': 'james h decker;james h. decker', 
		'expected': True, 
		'description': 'james h decker comparison with article'
	},
    {
		'input': 'james h leathem;james h. leathem', 
		'expected': True, 
		'description': 'james h leathem comparison with article'
	},
    {
		'input': 'james j de costa;edwin j. decosta', 
		'expected': False, 
		'description': 'james j de costa comparison with article'
	},
    {
		'input': 'james j devine;james j. devine', 
		'expected': True, 
		'description': 'james j devine comparison with article'
	},
    {
		'input': 'james j devlin;james j. devlin', 
		'expected': True, 
		'description': 'james j devlin comparison with article'
	},
    {
		'input': 'james j lawlor;james joseph lawlor', 
		'expected': True, 
		'description': 'james j lawlor comparison with article'
	},
    {
		'input': 'james j leahy;james j. leahy', 
		'expected': True, 
		'description': 'james j leahy comparison with article'
	},
    {
		'input': 'james l botsford;james lawrence botsford', 
		'expected': True, 
		'description': 'james l botsford comparison with article'
	},
    {
		'input': 'james l carrico;james leon carrico', 
		'expected': True, 
		'description': 'james l carrico comparison with article'
	},
    {
		'input': 'james l cate;james lea cate', 
		'expected': True, 
		'description': 'james l cate comparison with article'
	},
    {
		'input': 'james l cronin;james lawrence cronin', 
		'expected': True, 
		'description': 'james l cronin comparison with article'
	},
    {
		'input': 'james l deegan;james wayne deegan', 
		'expected': False, 
		'description': 'james l deegan comparison with article'
	},
    {
		'input': 'james l guenveur;james lapenne guenveur', 
		'expected': True, 
		'description': 'james l guenveur comparison with article'
	},
    {
		'input': 'james l hall;james lester hall', 
		'expected': True, 
		'description': 'james l hall comparison with article'
	},
    {
		'input': 'james l leach;james l. leach', 
		'expected': True, 
		'description': 'james l leach comparison with article'
	},
    {
		'input': 'james l lee;luther james lee', 
		'expected': True, 
		'description': 'james l lee comparison with article'
	},
    {
		'input': 'james l leggett;james llewellyn leggett', 
		'expected': True, 
		'description': 'james l leggett comparison with article'
	},
    {
		'input': 'james l leroy;l. w. leroy', 
		'expected': False, 
		'description': 'james l leroy comparison with article'
	},
    {
		'input': 'james l meriam;james lathrop meriam', 
		'expected': True, 
		'description': 'james l meriam comparison with article'
	},
    {
		'input': 'james l moore;james legrand moore', 
		'expected': True, 
		'description': 'james l moore comparison with article'
	},
    {
		'input': 'james l morrill;james lewis morrill', 
		'expected': True, 
		'description': 'james l morrill comparison with article'
	},
    {
		'input': 'james l reycroft, jr;james leonard reycraft', 
		'expected': True, 
		'description': 'james l reycroft, jr comparison with article'
	},
    {
		'input': 'james l sellers;james lee sellers', 
		'expected': True, 
		'description': 'james l sellers comparison with article'
	},
    {
		'input': 'james l whittenberger;james laverre whittenberger', 
		'expected': True, 
		'description': 'james l whittenberger comparison with article'
	},
    {
		'input': 'james lape;james l lapoe', 
		'expected': True, 
		'description': 'james lape comparison with article'
	},
    {
		'input': 'james lawrence;james vantine lawrence', 
		'expected': True, 
		'description': 'james lawrence comparison with article'
	},
    {
		'input': 'james lechay;james lechay', 
		'expected': True, 
		'description': 'james lechay comparison with article'
	},
    {
		'input': 'james levitt;james d. levitt', 
		'expected': True, 
		'description': 'james levitt comparison with article'
	},
    {
		'input': 'james m lamb;marion m. lamb', 
		'expected': False, 
		'description': 'james m lamb comparison with article'
	},
    {
		'input': 'james m lavin;james m. lavin', 
		'expected': True, 
		'description': 'james m lavin comparison with article'
	},
    {
		'input': 'james m leavey;james m. leavey', 
		'expected': True, 
		'description': 'james m leavey comparison with article'
	},
    {
		'input': 'james m ledanard;james lawrence lardner', 
		'expected': False, 
		'description': 'james m ledanard comparison with article'
	},
    {
		'input': 'james mahler;james lewis mahler', 
		'expected': True, 
		'description': 'james mahler comparison with article'
	},
    {
		'input': 'james r degroat;james r. degroat', 
		'expected': True, 
		'description': 'james r degroat comparison with article'
	},
    {
		'input': 'james r latimer;richmond lattimore', 
		'expected': True, 
		'description': 'james r latimer comparison with article'
	},
    {
		'input': 'james r van dyke;james r. van dyke', 
		'expected': True, 
		'description': 'james r van dyke comparison with article'
	},
    {
		'input': 'james robert hall;robert leon hall', 
		'expected': False, 
		'description': 'james robert hall comparison with article'
	},
    {
		'input': 'james s howe;james lewis howe', 
		'expected': False, 
		'description': 'james s howe comparison with article'
	},
    {
		'input': 'james s lemen;janice speer lemen', 
		'expected': False, 
		'description': 'james s lemen comparison with article'
	},
    {
		'input': 'james t lapsley, jr;james t. lapsley', 
		'expected': True, 
		'description': 'james t lapsley, jr comparison with article'
	},
    {
		'input': 'james v delgiudace;valentine l. telegdi', 
		'expected': False, 
		'description': 'james v delgiudace comparison with article'
	},
    {
		'input': 'james v newman;james leet valentine newman', 
		'expected': True, 
		'description': 'james v newman comparison with article'
	},
    {
		'input': 'james v rice;james van nostran rice', 
		'expected': True, 
		'description': 'james v rice comparison with article'
	},
    {
		'input': 'james van ness;james edward van ness', 
		'expected': True, 
		'description': 'james van ness comparison with article'
	},
    {
		'input': 'james w haun;james r. dehaan', 
		'expected': False, 
		'description': 'james w haun comparison with article'
	},
    {
		'input': 'james w. lesley;james w. lesley', 
		'expected': True, 
		'description': 'james w. lesley comparison with article'
	},
    {
		'input': 'jan a vanden brook;jan abram van den broek', 
		'expected': True, 
		'description': 'jan a vanden brook comparison with article'
	},
    {
		'input': 'jane a lawson;jane sorrie lawson', 
		'expected': False, 
		'description': 'jane a lawson comparison with article'
	},
    {
		'input': 'jane b van deusen;jayne c. van deusen', 
		'expected': False, 
		'description': 'jane b van deusen comparison with article'
	},
    {
		'input': 'jane f desforges;jane f. desforges', 
		'expected': True, 
		'description': 'jane f desforges comparison with article'
	},
    {
		'input': 'jane g demarest;g. stuart demarest', 
		'expected': False, 
		'description': 'jane g demarest comparison with article'
	},
    {
		'input': 'jane l gardner;jane lester gardner', 
		'expected': True, 
		'description': 'jane l gardner comparison with article'
	},
    {
		'input': 'janice a lazarre;arnold lazarow', 
		'expected': False, 
		'description': 'janice a lazarre comparison with article'
	},
    {
		'input': 'janice vanderwater;janice o. van de water', 
		'expected': True, 
		'description': 'janice vanderwater comparison with article'
	},
    {
		'input': 'jasper l callaway;jasper lamar callaway', 
		'expected': True, 
		'description': 'jasper l callaway comparison with article'
	},
    {
		'input': 'jasper stuckey;jasper leonidas stuckey', 
		'expected': True, 
		'description': 'jasper stuckey comparison with article'
	},
    {
		'input': 'jay c vankirk;jay calvin van kirk', 
		'expected': True, 
		'description': 'jay c vankirk comparison with article'
	},
    {
		'input': 'jay laurence lush;jay laurence lush', 
		'expected': True, 
		'description': 'jay laurence lush comparison with article'
	},
    {
		'input': 'jean blattel;jean van bladel', 
		'expected': True, 
		'description': 'jean blattel comparison with article'
	},
    {
		'input': 'jean c gallaher;clark van galder', 
		'expected': False, 
		'description': 'jean c gallaher comparison with article'
	},
    {
		'input': 'jean hansen;jean lee hansen', 
		'expected': True, 
		'description': 'jean hansen comparison with article'
	},
    {
		'input': 'jean j demorest;jean-jacques demorest', 
		'expected': True, 
		'description': 'jean j demorest comparison with article'
	},
    {
		'input': 'jean johnston;jean vance johnston', 
		'expected': True, 
		'description': 'jean johnston comparison with article'
	},
    {
		'input': 'jean labatut;jean labatut', 
		'expected': True, 
		'description': 'jean labatut comparison with article'
	},
    {
		'input': 'jean m demos;jean m. demos', 
		'expected': True, 
		'description': 'jean m demos comparison with article'
	},
    {
		'input': 'jean p lesperance;jean paul lesperance', 
		'expected': True, 
		'description': 'jean p lesperance comparison with article'
	},
    {
		'input': 'jeanette o laflamme;floyd o. flom', 
		'expected': False, 
		'description': 'jeanette o laflamme comparison with article'
	},
    {
		'input': 'jeannette laguaite;jeannette katherine laguaite', 
		'expected': True, 
		'description': 'jeannette laguaite comparison with article'
	},
    {
		'input': 'jennie l epps;jennie lee epps', 
		'expected': True, 
		'description': 'jennie l epps comparison with article'
	},
    {
		'input': 'jeremiah d ford;jeremiah denis matthias ford', 
		'expected': True, 
		'description': 'jeremiah d ford comparison with article'
	},
    {
		'input': 'jeremonah c lehane;jeremiah lehane', 
		'expected': True, 
		'description': 'jeremonah c lehane comparison with article'
	},
    {
		'input': 'jerome j. dee;jerome j. dee', 
		'expected': True, 
		'description': 'jerome j. dee comparison with article'
	},
    {
		'input': 'jerome l le master;jerome lloyd lemaster', 
		'expected': True, 
		'description': 'jerome l le master comparison with article'
	},
    {
		'input': 'jesse deboer;jesse deboer', 
		'expected': True, 
		'description': 'jesse deboer comparison with article'
	},
    {
		'input': 'jesse l charlton;jesse laurence charlton', 
		'expected': True, 
		'description': 'jesse l charlton comparison with article'
	},
    {
		'input': 'jesse l rader;jesse lee rader', 
		'expected': True, 
		'description': 'jesse l rader comparison with article'
	},
    {
		'input': 'jesse l rose;jesse lee rose', 
		'expected': True, 
		'description': 'jesse l rose comparison with article'
	},
    {
		'input': 'jesse lefforge;jess h. lefforge', 
		'expected': True, 
		'description': 'jesse lefforge comparison with article'
	},
    {
		'input': 'jessie l p delprat;jessie l. p. delprat', 
		'expected': True, 
		'description': 'jessie l p delprat comparison with article'
	},
    {
		'input': 'jessie l paul;jessie leonore paul', 
		'expected': True, 
		'description': 'jessie l paul comparison with article'
	},
    {
		'input': 'jessie larson;jessie larsen', 
		'expected': True, 
		'description': 'jessie larson comparison with article'
	},
    {
		'input': 'jimmy lee larue;jimmae larue', 
		'expected': True, 
		'description': 'jimmy lee larue comparison with article'
	},
    {
		'input': 'joe dennis;joe dennis', 
		'expected': True, 
		'description': 'joe dennis comparison with article'
	},
    {
		'input': 'joe l haddon;joe leon haddon', 
		'expected': True, 
		'description': 'joe l haddon comparison with article'
	},
    {
		'input': 'joe l lawson, jr;joe l. lawson', 
		'expected': True, 
		'description': 'joe l lawson, jr comparison with article'
	},
    {
		'input': 'joel p dean;joel dean', 
		'expected': True, 
		'description': 'joel p dean comparison with article'
	},
    {
		'input': 'joesph p lasalle;joseph p. lasalle', 
		'expected': True, 
		'description': 'joesph p lasalle comparison with article'
	},
    {
		'input': 'joffre l coe;joffre lanning coe', 
		'expected': True, 
		'description': 'joffre l coe comparison with article'
	},
    {
		'input': 'johannis l boysen;joh. lassen boysen', 
		'expected': True, 
		'description': 'johannis l boysen comparison with article'
	},
    {
		'input': 'john a de novo;john a. denovo', 
		'expected': True, 
		'description': 'john a de novo comparison with article'
	},
    {
		'input': 'john a l saunders;john alvah lee saunders', 
		'expected': True, 
		'description': 'john a l saunders comparison with article'
	},
    {
		'input': 'john a lanz;john tollet lantz', 
		'expected': False, 
		'description': 'john a lanz comparison with article'
	},
    {
		'input': 'john a leavitt;john anton leavitt', 
		'expected': True, 
		'description': 'john a leavitt comparison with article'
	},
    {
		'input': 'john a leiter;hans leitner', 
		'expected': True, 
		'description': 'john a leiter comparison with article'
	},
    {
		'input': 'john a lester, jr;john ashby lester', 
		'expected': True, 
		'description': 'john a lester, jr comparison with article'
	},
    {
		'input': 'john a spencer;john lebaron spencer', 
		'expected': False, 
		'description': 'john a spencer comparison with article'
	},
    {
		'input': 'john b deluca;georg hans bhawani luck', 
		'expected': False, 
		'description': 'john b deluca comparison with article'
	},
    {
		'input': 'john b fine;john van antwerp fine', 
		'expected': False, 
		'description': 'john b fine comparison with article'
	},
    {
		'input': 'john b lagen;john b. lagen', 
		'expected': True, 
		'description': 'john b lagen comparison with article'
	},
    {
		'input': 'john b larndry;john b. larnen', 
		'expected': False, 
		'description': 'john b larndry comparison with article'
	},
    {
		'input': 'john b lentz;john beckley lentz', 
		'expected': True, 
		'description': 'john b lentz comparison with article'
	},
    {
		'input': 'john b lewis;john barkley lewis', 
		'expected': True, 
		'description': 'john b lewis comparison with article'
	},
    {
		'input': 'john b longstaff;john bailey langstaff', 
		'expected': True, 
		'description': 'john b longstaff comparison with article'
	},
    {
		'input': 'john blair;john dennis blair', 
		'expected': True, 
		'description': 'john blair comparison with article'
	},
    {
		'input': 'john c de wolfe;john c. g. wulff', 
		'expected': True, 
		'description': 'john c de wolfe comparison with article'
	},
    {
		'input': 'john c lapp;john clarke lapp', 
		'expected': True, 
		'description': 'john c lapp comparison with article'
	},
    {
		'input': 'john c snell;john leslie snell', 
		'expected': False, 
		'description': 'john c snell comparison with article'
	},
    {
		'input': 'john c wilson;john lacy wilson', 
		'expected': False, 
		'description': 'john c wilson comparison with article'
	},
    {
		'input': 'john campbell lester;j. campbell lester', 
		'expected': True, 
		'description': 'john campbell lester comparison with article'
	},
    {
		'input': 'john cutler;john levi cutler', 
		'expected': True, 
		'description': 'john cutler comparison with article'
	},
    {
		'input': 'john d brackett;john denis bracket', 
		'expected': True, 
		'description': 'john d brackett comparison with article'
	},
    {
		'input': 'john d brackett;john denis brackett', 
		'expected': True, 
		'description': 'john d brackett comparison with article'
	},
    {
		'input': 'john day larkin;john day larkin', 
		'expected': True, 
		'description': 'john day larkin comparison with article'
	},
    {
		'input': 'john decarlo,jr;john decarlo', 
		'expected': True, 
		'description': 'john decarlo,jr comparison with article'
	},
    {
		'input': 'john decicco;john decicco', 
		'expected': True, 
		'description': 'john decicco comparison with article'
	},
    {
		'input': 'john degroot,sr;john degroot', 
		'expected': True, 
		'description': 'john degroot,sr comparison with article'
	},
    {
		'input': 'john delaney;john delaney', 
		'expected': True, 
		'description': 'john delaney comparison with article'
	},
    {
		'input': 'john dempson;john dempsher', 
		'expected': False, 
		'description': 'john dempson comparison with article'
	},
    {
		'input': 'john e bradley;john lewis bradley', 
		'expected': False, 
		'description': 'john e bradley comparison with article'
	},
    {
		'input': 'john e dees;john essary dees', 
		'expected': True, 
		'description': 'john e dees comparison with article'
	},
    {
		'input': 'john e lagerstrom;john e. lagerstrom', 
		'expected': True, 
		'description': 'john e lagerstrom comparison with article'
	},
    {
		'input': 'john e larsh;john edgar larsh', 
		'expected': True, 
		'description': 'john e larsh comparison with article'
	},
    {
		'input': 'john e lawson;john e. lawson', 
		'expected': True, 
		'description': 'john e lawson comparison with article'
	},
    {
		'input': 'john e newman;john von neumann', 
		'expected': True, 
		'description': 'john e newman comparison with article'
	},
    {
		'input': 'john e vance;john e. vance', 
		'expected': True, 
		'description': 'john e vance comparison with article'
	},
    {
		'input': 'john f denton;john fletcher denton', 
		'expected': True, 
		'description': 'john f denton comparison with article'
	},
    {
		'input': 'john f freeman;john leiper freeman', 
		'expected': False, 
		'description': 'john f freeman comparison with article'
	},
    {
		'input': 'john f mcgary;p. f. degara', 
		'expected': False, 
		'description': 'john f mcgary comparison with article'
	},
    {
		'input': 'john f van vleck;john hasbrouck van vleck', 
		'expected': False, 
		'description': 'john f van vleck comparison with article'
	},
    {
		'input': 'john f vanalstyne;john pruyn van alstyne', 
		'expected': False, 
		'description': 'john f vanalstyne comparison with article'
	},
    {
		'input': 'john f vane;john robert vane', 
		'expected': False, 
		'description': 'john f vane comparison with article'
	},
    {
		'input': 'john g denker;p. g. denker', 
		'expected': False, 
		'description': 'john g denker comparison with article'
	},
    {
		'input': 'john g lewis;john gary lewis', 
		'expected': True, 
		'description': 'john g lewis comparison with article'
	},
    {
		'input': 'john g moseley;john dean moseley', 
		'expected': False, 
		'description': 'john g moseley comparison with article'
	},
    {
		'input': 'john h dean;john aurie dean', 
		'expected': False, 
		'description': 'john h dean comparison with article'
	},
    {
		'input': 'john h dent;john henry dent', 
		'expected': True, 
		'description': 'john h dent comparison with article'
	},
    {
		'input': 'john h lampe;john harold lampe', 
		'expected': True, 
		'description': 'john h lampe comparison with article'
	},
    {
		'input': 'john h lawrence;john h. lawrence', 
		'expected': True, 
		'description': 'john h lawrence comparison with article'
	},
    {
		'input': 'john h leek;john halvor leek', 
		'expected': True, 
		'description': 'john h leek comparison with article'
	},
    {
		'input': 'john h marks;john h. vandermark', 
		'expected': True, 
		'description': 'john h marks comparison with article'
	},
    {
		'input': 'john h vondell;john henry vondell', 
		'expected': True, 
		'description': 'john h vondell comparison with article'
	},
    {
		'input': 'john h west;john leslie west', 
		'expected': False, 
		'description': 'john h west comparison with article'
	},
    {
		'input': 'john hartley;john leslie artley', 
		'expected': True, 
		'description': 'john hartley comparison with article'
	},
    {
		'input': 'john j beck;john dengler beck', 
		'expected': False, 
		'description': 'john j beck comparison with article'
	},
    {
		'input': 'john j deboer;john j. de boer', 
		'expected': True, 
		'description': 'john j deboer comparison with article'
	},
    {
		'input': 'john j havens;jacobus alexander van heuven', 
		'expected': False, 
		'description': 'john j havens comparison with article'
	},
    {
		'input': 'john j laffey;archille j. lafferiere', 
		'expected': False, 
		'description': 'john j laffey comparison with article'
	},
    {
		'input': 'john j lang;john j. lang', 
		'expected': True, 
		'description': 'john j lang comparison with article'
	},
    {
		'input': 'john j lawless;john joseph lawless', 
		'expected': True, 
		'description': 'john j lawless comparison with article'
	},
    {
		'input': 'john j le sage;john lesage', 
		'expected': True, 
		'description': 'john j le sage comparison with article'
	},
    {
		'input': 'john j lee;john j. lee', 
		'expected': True, 
		'description': 'john j lee comparison with article'
	},
    {
		'input': 'john j vannostrand;john j. van nostrand', 
		'expected': True, 
		'description': 'john j vannostrand comparison with article'
	},
    {
		'input': 'john johnson;john lars johnson', 
		'expected': True, 
		'description': 'john johnson comparison with article'
	},
    {
		'input': 'john k. dr lattimer, dr;john k. lattimer', 
		'expected': True, 
		'description': 'john k. dr lattimer, dr comparison with article'
	},
    {
		'input': 'john l adams, jr;john lester adams', 
		'expected': True, 
		'description': 'john l adams, jr comparison with article'
	},
    {
		'input': 'john l barnes;john landes barnes', 
		'expected': True, 
		'description': 'john l barnes comparison with article'
	},
    {
		'input': 'john l brooks;john langdon brooks', 
		'expected': True, 
		'description': 'john l brooks comparison with article'
	},
    {
		'input': 'john l champe;john leland champe', 
		'expected': True, 
		'description': 'john l champe comparison with article'
	},
    {
		'input': 'john l conger;john leonard conger', 
		'expected': True, 
		'description': 'john l conger comparison with article'
	},
    {
		'input': 'john l davies;john leonard davies', 
		'expected': True, 
		'description': 'john l davies comparison with article'
	},
    {
		'input': 'john l doll;john lee doll', 
		'expected': True, 
		'description': 'john l doll comparison with article'
	},
    {
		'input': 'john l evers;john lawrence evers', 
		'expected': True, 
		'description': 'john l evers comparison with article'
	},
    {
		'input': 'john l gerig;john lawrence gerig', 
		'expected': True, 
		'description': 'john l gerig comparison with article'
	},
    {
		'input': 'john l gillin;john lewis gillin', 
		'expected': True, 
		'description': 'john l gillin comparison with article'
	},
    {
		'input': 'john l kelley;john leroy kelley', 
		'expected': True, 
		'description': 'john l kelley comparison with article'
	},
    {
		'input': 'john l landgraf;john leslie landgraf', 
		'expected': True, 
		'description': 'john l landgraf comparison with article'
	},
    {
		'input': 'john l leedy;john lang leedy', 
		'expected': True, 
		'description': 'john l leedy comparison with article'
	},
    {
		'input': 'john l lievsay;john leon lievsay', 
		'expected': True, 
		'description': 'john l lievsay comparison with article'
	},
    {
		'input': 'john l mothershead, sr;john leland mothershead', 
		'expected': True, 
		'description': 'john l mothershead, sr comparison with article'
	},
    {
		'input': 'john l oncley;john lawrence oncley', 
		'expected': True, 
		'description': 'john l oncley comparison with article'
	},
    {
		'input': 'john l plyler;john laney plyler', 
		'expected': True, 
		'description': 'john l plyler comparison with article'
	},
    {
		'input': 'john l powell;john leonard powell', 
		'expected': True, 
		'description': 'john l powell comparison with article'
	},
    {
		'input': 'john l reichert;john lester reichert', 
		'expected': True, 
		'description': 'john l reichert comparison with article'
	},
    {
		'input': 'john l swigert, jr;john leonard swigert', 
		'expected': True, 
		'description': 'john l swigert, jr comparison with article'
	},
    {
		'input': 'john l yost;john lewis yost', 
		'expected': True, 
		'description': 'john l yost comparison with article'
	},
    {
		'input': 'john lamb, jr;john lamb', 
		'expected': True, 
		'description': 'john lamb, jr comparison with article'
	},
    {
		'input': 'john lamb;john henderson lamb', 
		'expected': True, 
		'description': 'john lamb comparison with article'
	},
    {
		'input': 'john lambert;john ralph lambert', 
		'expected': True, 
		'description': 'john lambert comparison with article'
	},
    {
		'input': 'john leaser;hans lisser', 
		'expected': True, 
		'description': 'john leaser comparison with article'
	},
    {
		'input': 'john lee brooks;john lee brooks', 
		'expected': True, 
		'description': 'john lee brooks comparison with article'
	},
    {
		'input': 'john leibenderfer;john edward leibenderfer', 
		'expected': True, 
		'description': 'john leibenderfer comparison with article'
	},
    {
		'input': 'john lester;john l. lester', 
		'expected': True, 
		'description': 'john lester comparison with article'
	},
    {
		'input': 'john lewis;john donald lewis', 
		'expected': True, 
		'description': 'john lewis comparison with article'
	},
    {
		'input': 'john lydon;hans victor von leden', 
		'expected': True, 
		'description': 'john lydon comparison with article'
	},
    {
		'input': 'john m dennis;john murray dennis', 
		'expected': True, 
		'description': 'john m dennis comparison with article'
	},
    {
		'input': 'john m lee;john m. lee', 
		'expected': True, 
		'description': 'john m lee comparison with article'
	},
    {
		'input': 'john m lent;john w. lenz', 
		'expected': False, 
		'description': 'john m lent comparison with article'
	},
    {
		'input': 'john m leslie;john kenneth leslie', 
		'expected': False, 
		'description': 'john m leslie comparison with article'
	},
    {
		'input': 'john m lewis;john m. lewis', 
		'expected': True, 
		'description': 'john m lewis comparison with article'
	},
    {
		'input': 'john n stewart;john laurence stewart', 
		'expected': False, 
		'description': 'john n stewart comparison with article'
	},
    {
		'input': 'john o wood;john lewis wood', 
		'expected': False, 
		'description': 'john o wood comparison with article'
	},
    {
		'input': 'john p lahey;john p. lahey', 
		'expected': True, 
		'description': 'john p lahey comparison with article'
	},
    {
		'input': 'john p leagans, jr;john paul leagans', 
		'expected': True, 
		'description': 'john p leagans, jr comparison with article'
	},
    {
		'input': 'john p leary;john coleman leary', 
		'expected': False, 
		'description': 'john p leary comparison with article'
	},
    {
		'input': 'john p leonard;john charles leonard', 
		'expected': False, 
		'description': 'john p leonard comparison with article'
	},
    {
		'input': 'john r laughnan;john r. laughnan', 
		'expected': True, 
		'description': 'john r laughnan comparison with article'
	},
    {
		'input': 'john r lewis;john prior lewis', 
		'expected': False, 
		'description': 'john r lewis comparison with article'
	},
    {
		'input': 'john r van de water;john r. van de water', 
		'expected': True, 
		'description': 'john r van de water comparison with article'
	},
    {
		'input': 'john r vonrohr;john robert von rohr', 
		'expected': True, 
		'description': 'john r vonrohr comparison with article'
	},
    {
		'input': 'john s lawrence;john s. lawrence', 
		'expected': True, 
		'description': 'john s lawrence comparison with article'
	},
    {
		'input': 'john s lazzaro;john h. lazzari', 
		'expected': False, 
		'description': 'john s lazzaro comparison with article'
	},
    {
		'input': 'john s leister;john s. leister', 
		'expected': True, 
		'description': 'john s leister comparison with article'
	},
    {
		'input': 'john sims;john leroy sims', 
		'expected': True, 
		'description': 'john sims comparison with article'
	},
    {
		'input': 'john t atwater;thomas van valkenburgh atwater', 
		'expected': False, 
		'description': 'john t atwater comparison with article'
	},
    {
		'input': 'john t lanning;john tate lanning', 
		'expected': True, 
		'description': 'john t lanning comparison with article'
	},
    {
		'input': 'john t lewis;john lewis', 
		'expected': True, 
		'description': 'john t lewis comparison with article'
	},
    {
		'input': 'john von s maeck;john van sicklen maeck', 
		'expected': True, 
		'description': 'john von s maeck comparison with article'
	},
    {
		'input': 'john w castles;john laurence casteel', 
		'expected': False, 
		'description': 'john w castles comparison with article'
	},
    {
		'input': 'john w de mand,iii;john wesley demand', 
		'expected': True, 
		'description': 'john w de mand,iii comparison with article'
	},
    {
		'input': 'john w dewire;john w. dewire', 
		'expected': True, 
		'description': 'john w dewire comparison with article'
	},
    {
		'input': 'john w lacey;forrest w. lacey', 
		'expected': False, 
		'description': 'john w lacey comparison with article'
	},
    {
		'input': 'john w lagrone;j. w. lagrone', 
		'expected': True, 
		'description': 'john w lagrone comparison with article'
	},
    {
		'input': 'john w lawrence;john william lawrence', 
		'expected': True, 
		'description': 'john w lawrence comparison with article'
	},
    {
		'input': 'john w lederle;john w. lederle', 
		'expected': True, 
		'description': 'john w lederle comparison with article'
	},
    {
		'input': 'john w lewis;john kent lewis', 
		'expected': False, 
		'description': 'john w lewis comparison with article'
	},
    {
		'input': 'john w lewis;john w. lewis', 
		'expected': True, 
		'description': 'john w lewis comparison with article'
	},
    {
		'input': 'john wilt;john w. vanderwilt', 
		'expected': True, 
		'description': 'john wilt comparison with article'
	},
    {
		'input': 'jordan l larson;jordan louis larson', 
		'expected': True, 
		'description': 'jordan l larson comparison with article'
	},
    {
		'input': 'jose leal martel;jose martel', 
		'expected': True, 
		'description': 'jose leal martel comparison with article'
	},
    {
		'input': 'jose onis;jose de onis', 
		'expected': True, 
		'description': 'jose onis comparison with article'
	},
    {
		'input': 'joseh l waling;joseph lee waling', 
		'expected': True, 
		'description': 'joseh l waling comparison with article'
	},
    {
		'input': 'joseh waling;joseph lee waling', 
		'expected': True, 
		'description': 'joseh waling comparison with article'
	},
    {
		'input': 'joseph a leeder;joseph a. leeder', 
		'expected': True, 
		'description': 'joseph a leeder comparison with article'
	},
    {
		'input': 'joseph a porter;joseph a. del porto', 
		'expected': True, 
		'description': 'joseph a porter comparison with article'
	},
    {
		'input': 'joseph a vonbradish;joseph a. von bradish', 
		'expected': True, 
		'description': 'joseph a vonbradish comparison with article'
	},
    {
		'input': 'joseph alfred aurele la rocque;aurele larocque', 
		'expected': True, 
		'description': 'joseph alfred aurele la rocque comparison with article'
	},
    {
		'input': 'joseph b vander veer;joseph b. vander veer', 
		'expected': True, 
		'description': 'joseph b vander veer comparison with article'
	},
    {
		'input': 'joseph b. leeper;joseph b. leeper', 
		'expected': True, 
		'description': 'joseph b. leeper comparison with article'
	},
    {
		'input': 'joseph cleveland;joseph lee cleveland', 
		'expected': True, 
		'description': 'joseph cleveland comparison with article'
	},
    {
		'input': 'joseph d clark;joseph deadrick clark', 
		'expected': True, 
		'description': 'joseph d clark comparison with article'
	},
    {
		'input': 'joseph d everingham;joseph dee everingham', 
		'expected': True, 
		'description': 'joseph d everingham comparison with article'
	},
    {
		'input': 'joseph davidson;joseph leroy davidson', 
		'expected': True, 
		'description': 'joseph davidson comparison with article'
	},
    {
		'input': 'joseph de lauro;joseph nicola delauro', 
		'expected': True, 
		'description': 'joseph de lauro comparison with article'
	},
    {
		'input': 'joseph e decamp;joseph e. decamp', 
		'expected': True, 
		'description': 'joseph e decamp comparison with article'
	},
    {
		'input': 'joseph e delmonico;e. joseph delmonico', 
		'expected': True, 
		'description': 'joseph e delmonico comparison with article'
	},
    {
		'input': 'joseph e devine;joseph e. devine', 
		'expected': True, 
		'description': 'joseph e devine comparison with article'
	},
    {
		'input': 'joseph e viola;forrest emanuel la violette', 
		'expected': False, 
		'description': 'joseph e viola comparison with article'
	},
    {
		'input': 'joseph f de luise;frank joseph deluise', 
		'expected': True, 
		'description': 'joseph f de luise comparison with article'
	},
    {
		'input': 'joseph f de simone;joseph f. desimone', 
		'expected': True, 
		'description': 'joseph f de simone comparison with article'
	},
    {
		'input': 'joseph g lalich;joseph john lalich', 
		'expected': False, 
		'description': 'joseph g lalich comparison with article'
	},
    {
		'input': 'joseph g leeder;joseph g. leeder', 
		'expected': True, 
		'description': 'joseph g leeder comparison with article'
	},
    {
		'input': 'joseph henry levi;joseph levi', 
		'expected': True, 
		'description': 'joseph henry levi comparison with article'
	},
    {
		'input': 'joseph j leonard;nelson jordan leonard', 
		'expected': False, 
		'description': 'joseph j leonard comparison with article'
	},
    {
		'input': 'joseph j picard;joseph leroy picard', 
		'expected': False, 
		'description': 'joseph j picard comparison with article'
	},
    {
		'input': 'joseph l lennon;joseph l. lennon', 
		'expected': True, 
		'description': 'joseph l lennon comparison with article'
	},
    {
		'input': 'joseph l lilienthal;joseph leo lilienthal', 
		'expected': True, 
		'description': 'joseph l lilienthal comparison with article'
	},
    {
		'input': 'joseph l mc donald;joseph lee mcdonald', 
		'expected': True, 
		'description': 'joseph l mc donald comparison with article'
	},
    {
		'input': 'joseph l midditon;joseph leonard middleton', 
		'expected': True, 
		'description': 'joseph l midditon comparison with article'
	},
    {
		'input': 'joseph l rosenholtz;joseph leon rosenholtz', 
		'expected': True, 
		'description': 'joseph l rosenholtz comparison with article'
	},
    {
		'input': 'joseph l sullivan;joseph lewis sullivan', 
		'expected': True, 
		'description': 'joseph l sullivan comparison with article'
	},
    {
		'input': 'joseph l walsh;joseph leonard walsh', 
		'expected': True, 
		'description': 'joseph l walsh comparison with article'
	},
    {
		'input': 'joseph landin;joseph landin', 
		'expected': True, 
		'description': 'joseph landin comparison with article'
	},
    {
		'input': 'joseph latimer;joseph marion latimer', 
		'expected': True, 
		'description': 'joseph latimer comparison with article'
	},
    {
		'input': 'joseph layton;joseph alexander leighton', 
		'expected': True, 
		'description': 'joseph layton comparison with article'
	},
    {
		'input': 'joseph le blanc;joseph le blanc', 
		'expected': True, 
		'description': 'joseph le blanc comparison with article'
	},
    {
		'input': 'joseph leavitt;joseph m. leavitt', 
		'expected': True, 
		'description': 'joseph leavitt comparison with article'
	},
    {
		'input': 'joseph lennon;joseph lennon', 
		'expected': True, 
		'description': 'joseph lennon comparison with article'
	},
    {
		'input': 'joseph levenson;joseph richmond levenson', 
		'expected': True, 
		'description': 'joseph levenson comparison with article'
	},
    {
		'input': 'joseph melnick;joseph lewis melnick', 
		'expected': True, 
		'description': 'joseph melnick comparison with article'
	},
    {
		'input': 'joseph p la master;j. p. lamaster', 
		'expected': True, 
		'description': 'joseph p la master comparison with article'
	},
    {
		'input': 'joseph p lahan;willard p. vanderlaan', 
		'expected': False, 
		'description': 'joseph p lahan comparison with article'
	},
    {
		'input': 'joseph p larocca;j. p. la rocca', 
		'expected': True, 
		'description': 'joseph p larocca comparison with article'
	},
    {
		'input': 'joseph p mccarthy;joseph le page mccarthy', 
		'expected': True, 
		'description': 'joseph p mccarthy comparison with article'
	},
    {
		'input': 'joseph p slatkavitz;phillip leonard sirotkin', 
		'expected': False, 
		'description': 'joseph p slatkavitz comparison with article'
	},
    {
		'input': 'joseph t law;joseph t. law', 
		'expected': True, 
		'description': 'joseph t law comparison with article'
	},
    {
		'input': 'joseph v mckelvey;joseph vance mckelvey', 
		'expected': True, 
		'description': 'joseph v mckelvey comparison with article'
	},
    {
		'input': 'joshua lederberg;joshua lederberg', 
		'expected': True, 
		'description': 'joshua lederberg comparison with article'
	},
    {
		'input': 'jovian lang;jovian lang', 
		'expected': True, 
		'description': 'jovian lang comparison with article'
	},
    {
		'input': 'judee d paulson;jehu dewitt paulson', 
		'expected': False, 
		'description': 'judee d paulson comparison with article'
	},
    {
		'input': 'jules last,dr;jules h. last', 
		'expected': True, 
		'description': 'jules last,dr comparison with article'
	},
    {
		'input': 'julia g leach;julian gilbert leach', 
		'expected': True, 
		'description': 'julia g leach comparison with article'
	},
    {
		'input': 'julian h degray;julian h. degray', 
		'expected': True, 
		'description': 'julian h degray comparison with article'
	},
    {
		'input': 'julian l ross;julian lenhart ross', 
		'expected': True, 
		'description': 'julian l ross comparison with article'
	},
    {
		'input': 'julian p barksdale;julian devreau barksdale', 
		'expected': False, 
		'description': 'julian p barksdale comparison with article'
	},
    {
		'input': 'julie lee hawkins;julia lee hawkins', 
		'expected': True, 
		'description': 'julie lee hawkins comparison with article'
	},
    {
		'input': 'julie r labarthe;luther r. barth', 
		'expected': False, 
		'description': 'julie r labarthe comparison with article'
	},
    {
		'input': 'juliette c devin;juliette c. devin', 
		'expected': True, 
		'description': 'juliette c devin comparison with article'
	},
    {
		'input': 'julius a larsen;julius ansgar larsen', 
		'expected': True, 
		'description': 'julius a larsen comparison with article'
	},
    {
		'input': 'june e lewis;june e. lewis', 
		'expected': True, 
		'description': 'june e lewis comparison with article'
	},
    {
		'input': 'junius larsen;junius larsen', 
		'expected': True, 
		'description': 'junius larsen comparison with article'
	},
    {
		'input': 'k detkingenn;katherine b. cettinger', 
		'expected': False, 
		'description': 'k detkingenn comparison with article'
	},
    {
		'input': 'karl e leib;karl elias leib', 
		'expected': True, 
		'description': 'karl e leib comparison with article'
	},
    {
		'input': 'karl g larson;karl gottfrid larson', 
		'expected': True, 
		'description': 'karl g larson comparison with article'
	},
    {
		'input': 'karl lark horowitz;karl lark-horovitz', 
		'expected': True, 
		'description': 'karl lark horowitz comparison with article'
	},
    {
		'input': 'karl lehmann;karl lehmann', 
		'expected': True, 
		'description': 'karl lehmann comparison with article'
	},
    {
		'input': 'karl o lange;karl otto lange', 
		'expected': True, 
		'description': 'karl o lange comparison with article'
	},
    {
		'input': 'karl s van dyke;karl s. van dyke', 
		'expected': True, 
		'description': 'karl s van dyke comparison with article'
	},
    {
		'input': 'karl w deutseh;karl w. deutsch', 
		'expected': True, 
		'description': 'karl w deutseh comparison with article'
	},
    {
		'input': 'karl w deutseh;karl wolfgang deutsch', 
		'expected': True, 
		'description': 'karl w deutseh comparison with article'
	},
    {
		'input': 'karol j murtz;carel w. van der merwe', 
		'expected': False, 
		'description': 'karol j murtz comparison with article'
	},
    {
		'input': 'katherine densford;katharine j. densford', 
		'expected': True, 
		'description': 'katherine densford comparison with article'
	},
    {
		'input': 'katherine l vankeuren;katherine van keuren', 
		'expected': True, 
		'description': 'katherine l vankeuren comparison with article'
	},
    {
		'input': 'katherine lever;katherine lever', 
		'expected': True, 
		'description': 'katherine lever comparison with article'
	},
    {
		'input': 'katherine ley;katherine l. ley', 
		'expected': True, 
		'description': 'katherine ley comparison with article'
	},
    {
		'input': 'kathleen m lavell;kathleen macdonald lavell', 
		'expected': True, 
		'description': 'kathleen m lavell comparison with article'
	},
    {
		'input': 'keith l wilson;keith leroy wilson', 
		'expected': True, 
		'description': 'keith l wilson comparison with article'
	},
    {
		'input': 'kenneth b de ome;kenneth b. deome', 
		'expected': True, 
		'description': 'kenneth b de ome comparison with article'
	},
    {
		'input': 'kenneth d cashin;kenneth delbert cashin', 
		'expected': True, 
		'description': 'kenneth d cashin comparison with article'
	},
    {
		'input': 'kenneth e lemmer;kenneth elery lemmer', 
		'expected': True, 
		'description': 'kenneth e lemmer comparison with article'
	},
    {
		'input': 'kenneth k landes;kenneth knight landes', 
		'expected': True, 
		'description': 'kenneth k landes comparison with article'
	},
    {
		'input': 'kenneth l mark;kenneth lamartine mark', 
		'expected': True, 
		'description': 'kenneth l mark comparison with article'
	},
    {
		'input': 'kenneth l osterud;kenneth leland osterud', 
		'expected': True, 
		'description': 'kenneth l osterud comparison with article'
	},
    {
		'input': 'kenneth l pichrell;kenneth leroy pickrell', 
		'expected': True, 
		'description': 'kenneth l pichrell comparison with article'
	},
    {
		'input': 'kenneth l roper;kenneth lawrence roper', 
		'expected': True, 
		'description': 'kenneth l roper comparison with article'
	},
    {
		'input': 'kenneth l turk;kenneth leroy turk', 
		'expected': True, 
		'description': 'kenneth l turk comparison with article'
	},
    {
		'input': 'kenneth l waters;kenneth lee waters', 
		'expected': True, 
		'description': 'kenneth l waters comparison with article'
	},
    {
		'input': 'kenneth l zierler;kenneth levie zierler', 
		'expected': True, 
		'description': 'kenneth l zierler comparison with article'
	},
    {
		'input': 'kenneth larowe;kenneth davis larowe', 
		'expected': True, 
		'description': 'kenneth larowe comparison with article'
	},
    {
		'input': 'kerl c leeburck;karl c. leebrick', 
		'expected': True, 
		'description': 'kerl c leeburck comparison with article'
	},
    {
		'input': 'kerta r leng;herta r. leng', 
		'expected': True, 
		'description': 'kerta r leng comparison with article'
	},
    {
		'input': 'key l barkley;key lee barkley', 
		'expected': True, 
		'description': 'key l barkley comparison with article'
	},
    {
		'input': 'kirk athow;kirk leland athow', 
		'expected': True, 
		'description': 'kirk athow comparison with article'
	},
    {
		'input': 'kurt lewent;kurt lewent', 
		'expected': True, 
		'description': 'kurt lewent comparison with article'
	},
    {
		'input': 'kyrl l f degravelines;kyrl leighton-faxford degravelines', 
		'expected': True, 
		'description': 'kyrl l f degravelines comparison with article'
	},
    {
		'input': 'l frederick richards;frederick leet reichert', 
		'expected': True, 
		'description': 'l frederick richards comparison with article'
	},
    {
		'input': 'l jackson laslett;l. jackson laslett', 
		'expected': True, 
		'description': 'l jackson laslett comparison with article'
	},
    {
		'input': 'l lawton gore;l. lawton gore', 
		'expected': True, 
		'description': 'l lawton gore comparison with article'
	},
    {
		'input': 'l rhodes lewis;l. rhodes lewis', 
		'expected': True, 
		'description': 'l rhodes lewis comparison with article'
	},
    {
		'input': 'l walter leach;walter barton leach', 
		'expected': False, 
		'description': 'l walter leach comparison with article'
	},
    {
		'input': 'l wreal lott;wreal lester lott', 
		'expected': True, 
		'description': 'l wreal lott comparison with article'
	},
    {
		'input': 'la vange richardson;la vange richardson', 
		'expected': True, 
		'description': 'la vange richardson comparison with article'
	},
    {
		'input': 'ladema m langdon;ladema mary langdon', 
		'expected': True, 
		'description': 'ladema m langdon comparison with article'
	},
    {
		'input': 'lamar johnson;b. lamar johnson', 
		'expected': True, 
		'description': 'lamar johnson comparison with article'
	},
    {
		'input': 'landis a romineck;aaron lemonick', 
		'expected': False, 
		'description': 'landis a romineck comparison with article'
	},
    {
		'input': 'landis l boyd;landis lee boyd', 
		'expected': True, 
		'description': 'landis l boyd comparison with article'
	},
    {
		'input': 'laraine a lebo;averill abraham liebow', 
		'expected': False, 
		'description': 'laraine a lebo comparison with article'
	},
    {
		'input': 'laura c lee;laura canfield lee', 
		'expected': True, 
		'description': 'laura c lee comparison with article'
	},
    {
		'input': 'laurel j lewis;laurel jones lewis', 
		'expected': True, 
		'description': 'laurel j lewis comparison with article'
	},
    {
		'input': 'laurence k hawkins;richmond laurin hawkins', 
		'expected': False, 
		'description': 'laurence k hawkins comparison with article'
	},
    {
		'input': 'laurence l. howe;laurence lee howe', 
		'expected': True, 
		'description': 'laurence l. howe comparison with article'
	},
    {
		'input': 'laurence montgomery;m. laurence montgomery', 
		'expected': True, 
		'description': 'laurence montgomery comparison with article'
	},
    {
		'input': 'laurence w de muth, jr;laurence w. demuth', 
		'expected': True, 
		'description': 'laurence w de muth, jr comparison with article'
	},
    {
		'input': 'lauvery l cauperthwaite;l. leroy cowperthwaite', 
		'expected': True, 
		'description': 'lauvery l cauperthwaite comparison with article'
	},
    {
		'input': 'lavar bateman;j. lavar bateman', 
		'expected': True, 
		'description': 'lavar bateman comparison with article'
	},
    {
		'input': 'lawrence a larrimer;lawrence a. larrimer', 
		'expected': True, 
		'description': 'lawrence a larrimer comparison with article'
	},
    {
		'input': 'lawrence anderson;leighton lars anderson', 
		'expected': False, 
		'description': 'lawrence anderson comparison with article'
	},
    {
		'input': 'lawrence b lee;lawrence h. lee', 
		'expected': False, 
		'description': 'lawrence b lee comparison with article'
	},
    {
		'input': 'lawrence d lafore;laurence d. lafore', 
		'expected': True, 
		'description': 'lawrence d lafore comparison with article'
	},
    {
		'input': 'lawrence d stewart;lawrence delbert stewart', 
		'expected': True, 
		'description': 'lawrence d stewart comparison with article'
	},
    {
		'input': 'lawrence e lawson;lawrence james lawson', 
		'expected': False, 
		'description': 'lawrence e lawson comparison with article'
	},
    {
		'input': 'lawrence e lee;lawrence lee', 
		'expected': True, 
		'description': 'lawrence e lee comparison with article'
	},
    {
		'input': 'lawrence key;e. lawrence keyes', 
		'expected': True, 
		'description': 'lawrence key comparison with article'
	},
    {
		'input': 'lawrence l rauch;lawrence lee rauch', 
		'expected': True, 
		'description': 'lawrence l rauch comparison with article'
	},
    {
		'input': 'lawrence l robbins;laurence lamson robbins', 
		'expected': True, 
		'description': 'lawrence l robbins comparison with article'
	},
    {
		'input': 'lawrence l vance;lawrence l. vance', 
		'expected': True, 
		'description': 'lawrence l vance comparison with article'
	},
    {
		'input': 'lawrence l waters;lawrence leslie waters', 
		'expected': True, 
		'description': 'lawrence l waters comparison with article'
	},
    {
		'input': 'lawrence labree;lawrence winthrop labree', 
		'expected': True, 
		'description': 'lawrence labree comparison with article'
	},
    {
		'input': 'lawrence larson;lawrence c. larson', 
		'expected': True, 
		'description': 'lawrence larson comparison with article'
	},
    {
		'input': 'lawrence t lawrey;lawrence t. lowrey', 
		'expected': True, 
		'description': 'lawrence t lawrey comparison with article'
	},
    {
		'input': 'lawrence w van meir;lawrence w. van mier', 
		'expected': True, 
		'description': 'lawrence w van meir comparison with article'
	},
    {
		'input': 'leander j van hecke;leander j. van hecke', 
		'expected': True, 
		'description': 'leander j van hecke comparison with article'
	},
    {
		'input': 'leatha j lee;j g lee', 
		'expected': False, 
		'description': 'leatha j lee comparison with article'
	},
    {
		'input': 'lee a parker;ethel lee parker', 
		'expected': False, 
		'description': 'lee a parker comparison with article'
	},
    {
		'input': 'lee block;virglnia lee block', 
		'expected': True, 
		'description': 'lee block comparison with article'
	},
    {
		'input': 'lee e bassett;david lee bassett', 
		'expected': False, 
		'description': 'lee e bassett comparison with article'
	},
    {
		'input': 'lee e deets;lee e. deets', 
		'expected': True, 
		'description': 'lee e deets comparison with article'
	},
    {
		'input': 'lee krause;herbert lee krauss', 
		'expected': True, 
		'description': 'lee krause comparison with article'
	},
    {
		'input': 'lee m bender;myron lee bender', 
		'expected': True, 
		'description': 'lee m bender comparison with article'
	},
    {
		'input': 'lee myers;e. lee myers', 
		'expected': True, 
		'description': 'lee myers comparison with article'
	},
    {
		'input': 'lee nemir;rosa lee nemir', 
		'expected': True, 
		'description': 'lee nemir comparison with article'
	},
    {
		'input': 'leighton rudolph;earle leighton rudolph', 
		'expected': True, 
		'description': 'leighton rudolph comparison with article'
	},
    {
		'input': 'leita e lawrence;odie e. lawrence', 
		'expected': False, 
		'description': 'leita e lawrence comparison with article'
	},
    {
		'input': 'leland c. lehman;leland c. lehman', 
		'expected': True, 
		'description': 'leland c. lehman comparison with article'
	},
    {
		'input': 'leland j lewis;leland judson lewis', 
		'expected': True, 
		'description': 'leland j lewis comparison with article'
	},
    {
		'input': 'leland l atwood;leland leavitt atwood', 
		'expected': True, 
		'description': 'leland l atwood comparison with article'
	},
    {
		'input': 'leland l briggs;leland lawrence briggs', 
		'expected': True, 
		'description': 'leland l briggs comparison with article'
	},
    {
		'input': 'lena may lauer;eleanor lauer', 
		'expected': True, 
		'description': 'lena may lauer comparison with article'
	},
    {
		'input': 'lennart v larson;lennart v. larson', 
		'expected': True, 
		'description': 'lennart v larson comparison with article'
	},
    {
		'input': 'leo a murphy;rex leo murphy', 
		'expected': False, 
		'description': 'leo a murphy comparison with article'
	},
    {
		'input': 'leo b leach;byron elwood leach', 
		'expected': False, 
		'description': 'leo b leach comparison with article'
	},
    {
		'input': 'leo b smith;richard leo smith', 
		'expected': False, 
		'description': 'leo b smith comparison with article'
	},
    {
		'input': 'leo clair jones;vincent leo jones', 
		'expected': False, 
		'description': 'leo clair jones comparison with article'
	},
    {
		'input': 'leo fooks;iviary leo pita volk', 
		'expected': False, 
		'description': 'leo fooks comparison with article'
	},
    {
		'input': 'leo l beranek;leo leroy beranek', 
		'expected': True, 
		'description': 'leo l beranek comparison with article'
	},
    {
		'input': 'leo l carrick;leo lehr carrick', 
		'expected': True, 
		'description': 'leo l carrick comparison with article'
	},
    {
		'input': 'leo lehrman;leo lehrman', 
		'expected': True, 
		'description': 'leo lehrman comparison with article'
	},
    {
		'input': 'leo lemke;leo lemke', 
		'expected': True, 
		'description': 'leo lemke comparison with article'
	},
    {
		'input': 'leo m legatski;leo max legatski', 
		'expected': True, 
		'description': 'leo m legatski comparison with article'
	},
    {
		'input': 'leo sosa;leo p. delsasso', 
		'expected': False, 
		'description': 'leo sosa comparison with article'
	},
    {
		'input': 'leo sosa;leo p. delsossa', 
		'expected': True, 
		'description': 'leo sosa comparison with article'
	},
    {
		'input': 'leo w leary;leo w. leary', 
		'expected': True, 
		'description': 'leo w leary comparison with article'
	},
    {
		'input': 'leon a hitchcock;charles leo hitchcock', 
		'expected': False, 
		'description': 'leon a hitchcock comparison with article'
	},
    {
		'input': 'leon allen;durward leon allen', 
		'expected': True, 
		'description': 'leon allen comparison with article'
	},
    {
		'input': 'leon c van sickle;clyde huntus van sickle', 
		'expected': False, 
		'description': 'leon c van sickle comparison with article'
	},
    {
		'input': 'leon gershbein;leon lee gershbein', 
		'expected': True, 
		'description': 'leon gershbein comparison with article'
	},
    {
		'input': 'leon j leahy;leon j. leahy', 
		'expected': True, 
		'description': 'leon j leahy comparison with article'
	},
    {
		'input': 'leon l iltis;leon leonard iltis', 
		'expected': True, 
		'description': 'leon l iltis comparison with article'
	},
    {
		'input': 'leon l stephan;leon lemar stephan', 
		'expected': True, 
		'description': 'leon l stephan comparison with article'
	},
    {
		'input': 'leon lassers;leon lassers', 
		'expected': True, 
		'description': 'leon lassers comparison with article'
	},
    {
		'input': 'leon singer;ferdinand leon singer', 
		'expected': True, 
		'description': 'leon singer comparison with article'
	},
    {
		'input': 'leon w chaffee;emory leon chaffee', 
		'expected': False, 
		'description': 'leon w chaffee comparison with article'
	},
    {
		'input': 'leon w dean;leon w. dean', 
		'expected': True, 
		'description': 'leon w dean comparison with article'
	},
    {
		'input': 'leonard a lecht;leonard a. lecht', 
		'expected': True, 
		'description': 'leonard a lecht comparison with article'
	},
    {
		'input': 'leonard d lee;herbert leonard lee', 
		'expected': False, 
		'description': 'leonard d lee comparison with article'
	},
    {
		'input': 'leonard demorelos;leonardo c. de morelos', 
		'expected': True, 
		'description': 'leonard demorelos comparison with article'
	},
    {
		'input': 'leonard f lewis;t. leonard lewis', 
		'expected': False, 
		'description': 'leonard f lewis comparison with article'
	},
    {
		'input': 'leonard g ryerson;dwight leonard ryerson', 
		'expected': False, 
		'description': 'leonard g ryerson comparison with article'
	},
    {
		'input': 'leonard j deysach;leonard j. deysach', 
		'expected': True, 
		'description': 'leonard j deysach comparison with article'
	},
    {
		'input': 'leonard leone;leonard leone', 
		'expected': True, 
		'description': 'leonard leone comparison with article'
	},
    {
		'input': 'leonard levy;leonard w. levy', 
		'expected': True, 
		'description': 'leonard levy comparison with article'
	},
    {
		'input': 'leonard light;leonard leight', 
		'expected': True, 
		'description': 'leonard light comparison with article'
	},
    {
		'input': 'leonard marino;leonardo santamarina', 
		'expected': True, 
		'description': 'leonard marino comparison with article'
	},
    {
		'input': 'leonard w laboree;leonard woods labaree', 
		'expected': True, 
		'description': 'leonard w laboree comparison with article'
	},
    {
		'input': 'leroy a anderson;stuart leroy anderson', 
		'expected': False, 
		'description': 'leroy a anderson comparison with article'
	},
    {
		'input': 'leroy a swanson;adrian leroy swanson', 
		'expected': True, 
		'description': 'leroy a swanson comparison with article'
	},
    {
		'input': 'leroy e detling;leroy e. detling', 
		'expected': True, 
		'description': 'leroy e detling comparison with article'
	},
    {
		'input': 'leroy johnson;alfred leroy johnson', 
		'expected': True, 
		'description': 'leroy johnson comparison with article'
	},
    {
		'input': 'leroy koenig;virgil leroy koenig', 
		'expected': True, 
		'description': 'leroy koenig comparison with article'
	},
    {
		'input': 'leroy l barnes;leroy lesher barnes', 
		'expected': True, 
		'description': 'leroy l barnes comparison with article'
	},
    {
		'input': 'leroy t laase;leeroy laase', 
		'expected': True, 
		'description': 'leroy t laase comparison with article'
	},
    {
		'input': 'leslie bullock;philip leslie bullock', 
		'expected': True, 
		'description': 'leslie bullock comparison with article'
	},
    {
		'input': 'leslie f morrison;paul leslie morrison', 
		'expected': False, 
		'description': 'leslie f morrison comparison with article'
	},
    {
		'input': 'leslie h layman;leslie h. layman', 
		'expected': True, 
		'description': 'leslie h layman comparison with article'
	},
    {
		'input': 'leslie lisle lewis;leslie l. lewis', 
		'expected': True, 
		'description': 'leslie lisle lewis comparison with article'
	},
    {
		'input': 'lester creaser;william lester kraushaar', 
		'expected': True, 
		'description': 'lester creaser comparison with article'
	},
    {
		'input': 'lester j hayman;joseph lester hayman', 
		'expected': True, 
		'description': 'lester j hayman comparison with article'
	},
    {
		'input': 'lester lee;lester lees', 
		'expected': True, 
		'description': 'lester lee comparison with article'
	},
    {
		'input': 'lester s henderson;j. lester henderson', 
		'expected': False, 
		'description': 'lester s henderson comparison with article'
	},
    {
		'input': 'lester w allen;a. lester allen', 
		'expected': False, 
		'description': 'lester w allen comparison with article'
	},
    {
		'input': 'leston l love;leston lewis love', 
		'expected': True, 
		'description': 'leston l love comparison with article'
	},
    {
		'input': 'levi dees;levi o. dees', 
		'expected': True, 
		'description': 'levi dees comparison with article'
	},
    {
		'input': 'lewis l clegg;lewis lamar clegg', 
		'expected': True, 
		'description': 'lewis l clegg comparison with article'
	},
    {
		'input': 'lewis larkin;lewis b. larkin', 
		'expected': True, 
		'description': 'lewis larkin comparison with article'
	},
    {
		'input': 'lewis m foster;eugene lewis foster', 
		'expected': False, 
		'description': 'lewis m foster comparison with article'
	},
    {
		'input': 'lewis peterson;edwin lewis peterson', 
		'expected': True, 
		'description': 'lewis peterson comparison with article'
	},
    {
		'input': 'lillian c lambert;c. n. lambert', 
		'expected': False, 
		'description': 'lillian c lambert comparison with article'
	},
    {
		'input': 'lillian h lanover;hrwin wladaver', 
		'expected': False, 
		'description': 'lillian h lanover comparison with article'
	},
    {
		'input': 'lillian lawler;lillian b. lawler', 
		'expected': True, 
		'description': 'lillian lawler comparison with article'
	},
    {
		'input': 'lillian lee vaughan;lillian lee vaughan', 
		'expected': True, 
		'description': 'lillian lee vaughan comparison with article'
	},
    {
		'input': 'lincoln lapaz;lincoln lapaz', 
		'expected': True, 
		'description': 'lincoln lapaz comparison with article'
	},
    {
		'input': 'linnal robinson;selby lemley robinson', 
		'expected': False, 
		'description': 'linnal robinson comparison with article'
	},
    {
		'input': 'linnea c dennett;linnea c. dennett', 
		'expected': True, 
		'description': 'linnea c dennett comparison with article'
	},
    {
		'input': 'lizbeth laughton;lizbeth r. laughton', 
		'expected': True, 
		'description': 'lizbeth laughton comparison with article'
	},
    {
		'input': 'llewellyn l derby;llewellyn light derby', 
		'expected': True, 
		'description': 'llewellyn l derby comparison with article'
	},
    {
		'input': 'lloyd a betuno;andre j. de bethune', 
		'expected': False, 
		'description': 'lloyd a betuno comparison with article'
	},
    {
		'input': 'lloyd o burge;lloyd van de berg', 
		'expected': True, 
		'description': 'lloyd o burge comparison with article'
	},
    {
		'input': 'lois lebar;lois e. lebar', 
		'expected': True, 
		'description': 'lois lebar comparison with article'
	},
    {
		'input': 'lois schnoor;lois laverne schnoor', 
		'expected': True, 
		'description': 'lois schnoor comparison with article'
	},
    {
		'input': 'lolo robinson;lolo lemme robinson', 
		'expected': True, 
		'description': 'lolo robinson comparison with article'
	},
    {
		'input': 'loras t lane;loras t. lane', 
		'expected': True, 
		'description': 'loras t lane comparison with article'
	},
    {
		'input': 'loren j larsen;loren j. larsen', 
		'expected': True, 
		'description': 'loren j larsen comparison with article'
	},
    {
		'input': 'lorin j lucius;joseph j. delucia', 
		'expected': False, 
		'description': 'lorin j lucius comparison with article'
	},
    {
		'input': 'lorna de varon;lorna cooke devaron', 
		'expected': True, 
		'description': 'lorna de varon comparison with article'
	},
    {
		'input': 'lorrent le sage;laurent lesage', 
		'expected': True, 
		'description': 'lorrent le sage comparison with article'
	},
    {
		'input': 'louis a derose;louis derose', 
		'expected': True, 
		'description': 'louis a derose comparison with article'
	},
    {
		'input': 'louis a landa;louis a. landa', 
		'expected': True, 
		'description': 'louis a landa comparison with article'
	},
    {
		'input': 'louis a sr demonbreun;w. a. demonbreun', 
		'expected': False, 
		'description': 'louis a sr demonbreun comparison with article'
	},
    {
		'input': 'louis d de vries;louis devries', 
		'expected': True, 
		'description': 'louis d de vries comparison with article'
	},
    {
		'input': 'louis e derryberry;louis e. derryberry', 
		'expected': True, 
		'description': 'louis e derryberry comparison with article'
	},
    {
		'input': 'louis e lambert;louis erskine lambert', 
		'expected': True, 
		'description': 'louis e lambert comparison with article'
	},
    {
		'input': 'louis e. vandegrift;louis e. vandergrift', 
		'expected': True, 
		'description': 'louis e. vandegrift comparison with article'
	},
    {
		'input': 'louis h levin;louis levine', 
		'expected': True, 
		'description': 'louis h levin comparison with article'
	},
    {
		'input': 'louis j lyell;luis leal', 
		'expected': True, 
		'description': 'louis j lyell comparison with article'
	},
    {
		'input': 'louis l levy;louis levy', 
		'expected': True, 
		'description': 'louis l levy comparison with article'
	},
    {
		'input': 'louis l sulya;louis leon sulya', 
		'expected': True, 
		'description': 'louis l sulya comparison with article'
	},
    {
		'input': 'louis lams;louis lams', 
		'expected': True, 
		'description': 'louis lams comparison with article'
	},
    {
		'input': 'louis leiter;louis leiter', 
		'expected': True, 
		'description': 'louis leiter comparison with article'
	},
    {
		'input': 'louis leon thurstone;louis leon thurstone', 
		'expected': True, 
		'description': 'louis leon thurstone comparison with article'
	},
    {
		'input': 'louis p lodestro;v. p. destro', 
		'expected': False, 
		'description': 'louis p lodestro comparison with article'
	},
    {
		'input': 'louis r detjen;louis reinhold detjen', 
		'expected': True, 
		'description': 'louis r detjen comparison with article'
	},
    {
		'input': 'louis r levin;richard louis levin', 
		'expected': True, 
		'description': 'louis r levin comparison with article'
	},
    {
		'input': 'louis s le tellier;louis shepherd letellier', 
		'expected': True, 
		'description': 'louis s le tellier comparison with article'
	},
    {
		'input': 'louise cassell;wallace lewis cassell', 
		'expected': True, 
		'description': 'louise cassell comparison with article'
	},
    {
		'input': 'louise e leonard;e. louise leonard', 
		'expected': True, 
		'description': 'louise e leonard comparison with article'
	},
    {
		'input': 'louise m leet;lewis don leet', 
		'expected': False, 
		'description': 'louise m leet comparison with article'
	},
    {
		'input': 'louise van ogle;louise van ogle', 
		'expected': True, 
		'description': 'louise van ogle comparison with article'
	},
    {
		'input': 'lowell d ashby;lowell dewitt ashby', 
		'expected': True, 
		'description': 'lowell d ashby comparison with article'
	},
    {
		'input': 'lowell p leland;lowell p. leland', 
		'expected': True, 
		'description': 'lowell p leland comparison with article'
	},
    {
		'input': 'lowell r laudon;lowell robert laudon', 
		'expected': True, 
		'description': 'lowell r laudon comparison with article'
	},
    {
		'input': 'loyal l conrad;loyal lee conrad', 
		'expected': True, 
		'description': 'loyal l conrad comparison with article'
	},
    {
		'input': 'lucia d hough;lucia dearborn hough', 
		'expected': True, 
		'description': 'lucia d hough comparison with article'
	},
    {
		'input': 'lucie s lancaster;dabney s. lancaster', 
		'expected': False, 
		'description': 'lucie s lancaster comparison with article'
	},
    {
		'input': 'lucien d. pearson;lucien dean pearson', 
		'expected': True, 
		'description': 'lucien d. pearson comparison with article'
	},
    {
		'input': 'lucien desjardins;lucien h. desjardins', 
		'expected': True, 
		'description': 'lucien desjardins comparison with article'
	},
    {
		'input': 'lucile delano;lucile k. delano', 
		'expected': True, 
		'description': 'lucile delano comparison with article'
	},
    {
		'input': 'lucille a. lemaitre;a. l maitre', 
		'expected': True, 
		'description': 'lucille a. lemaitre comparison with article'
	},
    {
		'input': 'lucille a. lemaitre;harriette a. martire', 
		'expected': False, 
		'description': 'lucille a. lemaitre comparison with article'
	},
    {
		'input': 'lucille a. lemaitre;l a. maitre', 
		'expected': True, 
		'description': 'lucille a. lemaitre comparison with article'
	},
    {
		'input': 'lucius j desha;lucius junius desha', 
		'expected': True, 
		'description': 'lucius j desha comparison with article'
	},
    {
		'input': 'lucy a sally;lucile c. lasalle', 
		'expected': False, 
		'description': 'lucy a sally comparison with article'
	},
    {
		'input': 'lucy lee call;lucy lee call', 
		'expected': True, 
		'description': 'lucy lee call comparison with article'
	},
    {
		'input': 'lucy lester;lucy lester', 
		'expected': True, 
		'description': 'lucy lester comparison with article'
	},
    {
		'input': 'lucy lewis;lucy lee lewis', 
		'expected': True, 
		'description': 'lucy lewis comparison with article'
	},
    {
		'input': 'ludvig c larson;ludvig conrad larson', 
		'expected': True, 
		'description': 'ludvig c larson comparison with article'
	},
    {
		'input': 'ludwig lewisohn;ludwig lewisohn', 
		'expected': True, 
		'description': 'ludwig lewisohn comparison with article'
	},
    {
		'input': 'luis alfonso fieiro;lonnie t. vanderveer', 
		'expected': False, 
		'description': 'luis alfonso fieiro comparison with article'
	},
    {
		'input': 'lula g lentz;e. g. lentz', 
		'expected': False, 
		'description': 'lula g lentz comparison with article'
	},
    {
		'input': 'luther o levengood;luther omar leavengood', 
		'expected': True, 
		'description': 'luther o levengood comparison with article'
	},
    {
		'input': 'lutie c leavell;lutie c. leavell', 
		'expected': True, 
		'description': 'lutie c leavell comparison with article'
	},
    {
		'input': 'luz m. diaz de pachero;luis m. diaz', 
		'expected': False, 
		'description': 'luz m. diaz de pachero comparison with article'
	},
    {
		'input': 'lyman langdon;lyman albert langdon', 
		'expected': True, 
		'description': 'lyman langdon comparison with article'
	},
    {
		'input': 'lynn l wentworth;lynn leota wentworth', 
		'expected': True, 
		'description': 'lynn l wentworth comparison with article'
	},
    {
		'input': 'lysle d leach;lysle d. leach', 
		'expected': True, 
		'description': 'lysle d leach comparison with article'
	},
    {
		'input': 'm fredric landwer;milton frederic landwer', 
		'expected': True, 
		'description': 'm fredric landwer comparison with article'
	},
    {
		'input': 'mabel d erwin;mabel deane erwin', 
		'expected': True, 
		'description': 'mabel d erwin comparison with article'
	},
    {
		'input': 'mable lesher;mabel lesher', 
		'expected': True, 
		'description': 'mable lesher comparison with article'
	},
    {
		'input': 'madeline g laberge;g. antonio laberge', 
		'expected': False, 
		'description': 'madeline g laberge comparison with article'
	},
    {
		'input': 'mali g lenz;mali goldmann lenz', 
		'expected': True, 
		'description': 'mali g lenz comparison with article'
	},
    {
		'input': 'mamie lee davis;mamie myrtis davis', 
		'expected': False, 
		'description': 'mamie lee davis comparison with article'
	},
    {
		'input': 'manson jennings;manson van b. jennings', 
		'expected': True, 
		'description': 'manson jennings comparison with article'
	},
    {
		'input': 'margaret b lagrille;margaret b. lagrille', 
		'expected': True, 
		'description': 'margaret b lagrille comparison with article'
	},
    {
		'input': 'margaret c de vinny;margaret c. devinny', 
		'expected': True, 
		'description': 'margaret c de vinny comparison with article'
	},
    {
		'input': 'margaret c larsen;a. margaret larsen', 
		'expected': False, 
		'description': 'margaret c larsen comparison with article'
	},
    {
		'input': 'margaret de schweinitz;margaret de schweinitz', 
		'expected': True, 
		'description': 'margaret de schweinitz comparison with article'
	},
    {
		'input': 'margaret dearden;leah margaret dearden', 
		'expected': True, 
		'description': 'margaret dearden comparison with article'
	},
    {
		'input': 'margaret degray;margaret patterson degray', 
		'expected': True, 
		'description': 'margaret degray comparison with article'
	},
    {
		'input': 'margaret l leonard;margaret lydia leonard', 
		'expected': True, 
		'description': 'margaret l leonard comparison with article'
	},
    {
		'input': 'margaret lamont;margaret lamont', 
		'expected': True, 
		'description': 'margaret lamont comparison with article'
	},
    {
		'input': 'margery deming;margery van n. deming', 
		'expected': True, 
		'description': 'margery deming comparison with article'
	},
    {
		'input': 'marguerite richards;marguerite lentz richards', 
		'expected': True, 
		'description': 'marguerite richards comparison with article'
	},
    {
		'input': 'maria d picerilli;maria de\'negri piccirilli', 
		'expected': True, 
		'description': 'maria d picerilli comparison with article'
	},
    {
		'input': 'maria diez de onate;maria d. de onate', 
		'expected': True, 
		'description': 'maria diez de onate comparison with article'
	},
    {
		'input': 'maria rose lowther;maria l. de lowther', 
		'expected': False, 
		'description': 'maria rose lowther comparison with article'
	},
    {
		'input': 'marian v devoy;marian v. devoy', 
		'expected': True, 
		'description': 'marian v devoy comparison with article'
	},
    {
		'input': 'marie b denneen;marie b. denneen', 
		'expected': True, 
		'description': 'marie b denneen comparison with article'
	},
    {
		'input': 'marie l schwartz;l. laszlo schwartz', 
		'expected': False, 
		'description': 'marie l schwartz comparison with article'
	},
    {
		'input': 'marie lein;marie e. lein', 
		'expected': True, 
		'description': 'marie lein comparison with article'
	},
    {
		'input': 'mariette le blanc;mariette le blanc', 
		'expected': True, 
		'description': 'mariette le blanc comparison with article'
	},
    {
		'input': 'marine leland;marine leland', 
		'expected': True, 
		'description': 'marine leland comparison with article'
	},
    {
		'input': 'marion deronde;marion deronde', 
		'expected': True, 
		'description': 'marion deronde comparison with article'
	},
    {
		'input': 'marion f deshazo;marian frances deshazo', 
		'expected': True, 
		'description': 'marion f deshazo comparison with article'
	},
    {
		'input': 'marion l jackson;marion leroy jackson', 
		'expected': True, 
		'description': 'marion l jackson comparison with article'
	},
    {
		'input': 'marion l mcqueen;marion leigh macqueen', 
		'expected': True, 
		'description': 'marion l mcqueen comparison with article'
	},
    {
		'input': 'marion lashley;marion m. lasley', 
		'expected': True, 
		'description': 'marion lashley comparison with article'
	},
    {
		'input': 'marion leahy;marion eugene lahey', 
		'expected': True, 
		'description': 'marion leahy comparison with article'
	},
    {
		'input': 'marion m lawrence;marion lawrence', 
		'expected': True, 
		'description': 'marion m lawrence comparison with article'
	},
    {
		'input': 'marion s lewis;marion smith lewis', 
		'expected': True, 
		'description': 'marion s lewis comparison with article'
	},
    {
		'input': 'marjorie e lackey;marjorie e. latchaw', 
		'expected': False, 
		'description': 'marjorie e lackey comparison with article'
	},
    {
		'input': 'marjorie leonard;marjorie leonard', 
		'expected': True, 
		'description': 'marjorie leonard comparison with article'
	},
    {
		'input': 'mark d howe;mark dewolfe howe', 
		'expected': True, 
		'description': 'mark d howe comparison with article'
	},
    {
		'input': 'mark de leonard;mark f. deleonard', 
		'expected': True, 
		'description': 'mark de leonard comparison with article'
	},
    {
		'input': 'mark h degraff;mark h. degraff', 
		'expected': True, 
		'description': 'mark h degraff comparison with article'
	},
    {
		'input': 'mark l floyde;mark lawrence floyd', 
		'expected': True, 
		'description': 'mark l floyde comparison with article'
	},
    {
		'input': 'mark w delzel;mark w. delzell', 
		'expected': True, 
		'description': 'mark w delzel comparison with article'
	},
    {
		'input': 'marshall l pennington;marshall lee pennington', 
		'expected': True, 
		'description': 'marshall l pennington comparison with article'
	},
    {
		'input': 'marshall l schmitt;marshall langdon schmitt', 
		'expected': True, 
		'description': 'marshall l schmitt comparison with article'
	},
    {
		'input': 'marston d hodgin;marston dean hodgin', 
		'expected': True, 
		'description': 'marston d hodgin comparison with article'
	},
    {
		'input': 'martha d wallace;martha dee wallace', 
		'expected': True, 
		'description': 'martha d wallace comparison with article'
	},
    {
		'input': 'martha e leighton;martha emma leighton', 
		'expected': True, 
		'description': 'martha e leighton comparison with article'
	},
    {
		'input': 'martha lewis;martha modena lewis', 
		'expected': True, 
		'description': 'martha lewis comparison with article'
	},
    {
		'input': 'martha m larsen;r. m. larsen', 
		'expected': False, 
		'description': 'martha m larsen comparison with article'
	},
    {
		'input': 'martha n. lewis;martha n. lewis', 
		'expected': True, 
		'description': 'martha n. lewis comparison with article'
	},
    {
		'input': 'martha taber;martha van hoesen taber', 
		'expected': True, 
		'description': 'martha taber comparison with article'
	},
    {
		'input': 'martin d whitaker;martin dewey whitaker', 
		'expected': True, 
		'description': 'martin d whitaker comparison with article'
	},
    {
		'input': 'martin deutsch;martin deutsch', 
		'expected': True, 
		'description': 'martin deutsch comparison with article'
	},
    {
		'input': 'martin l black;martin lee black', 
		'expected': True, 
		'description': 'martin l black comparison with article'
	},
    {
		'input': 'martin l. lindall;martin leroy lindahl', 
		'expected': True, 
		'description': 'martin l. lindall comparison with article'
	},
    {
		'input': 'martin larrabee;martin glover larrabee', 
		'expected': True, 
		'description': 'martin larrabee comparison with article'
	},
    {
		'input': 'martin leigh harrison;leigh m. harrison', 
		'expected': True, 
		'description': 'martin leigh harrison comparison with article'
	},
    {
		'input': 'martin levit;martin levit', 
		'expected': True, 
		'description': 'martin levit comparison with article'
	},
    {
		'input': 'martin w debenham;martin w. debenham', 
		'expected': True, 
		'description': 'martin w debenham comparison with article'
	},
    {
		'input': 'marvin l granstrom;marvin leroy granstrom', 
		'expected': True, 
		'description': 'marvin l granstrom comparison with article'
	},
    {
		'input': 'marvin l infinger;marvin leslie infinger', 
		'expected': True, 
		'description': 'marvin l infinger comparison with article'
	},
    {
		'input': 'marvin l vest;marvin lewis vest', 
		'expected': True, 
		'description': 'marvin l vest comparison with article'
	},
    {
		'input': 'marvin w de jonge;marvin willis de jonge', 
		'expected': True, 
		'description': 'marvin w de jonge comparison with article'
	},
    {
		'input': 'mary a devries;mary aid de vries', 
		'expected': True, 
		'description': 'mary a devries comparison with article'
	},
    {
		'input': 'mary a loginuk;grace mead andrus de laguna', 
		'expected': False, 
		'description': 'mary a loginuk comparison with article'
	},
    {
		'input': 'mary a ziehl;aldert van der ziel', 
		'expected': True, 
		'description': 'mary a ziehl comparison with article'
	},
    {
		'input': 'mary b laughead;mary laughead', 
		'expected': True, 
		'description': 'mary b laughead comparison with article'
	},
    {
		'input': 'mary blayney;mary dee blayney', 
		'expected': True, 
		'description': 'mary blayney comparison with article'
	},
    {
		'input': 'mary debow;mary virginia debow', 
		'expected': True, 
		'description': 'mary debow comparison with article'
	},
    {
		'input': 'mary e lakeman;ernest rene lacheman', 
		'expected': False, 
		'description': 'mary e lakeman comparison with article'
	},
    {
		'input': 'mary e lakenan;mary e. lakenan', 
		'expected': True, 
		'description': 'mary e lakenan comparison with article'
	},
    {
		'input': 'mary e latimer;mary e. latimer', 
		'expected': True, 
		'description': 'mary e latimer comparison with article'
	},
    {
		'input': 'mary e vance;mary e. vance', 
		'expected': True, 
		'description': 'mary e vance comparison with article'
	},
    {
		'input': 'mary f lawson;mary florence lawson', 
		'expected': True, 
		'description': 'mary f lawson comparison with article'
	},
    {
		'input': 'mary g decker;mary g. decker', 
		'expected': True, 
		'description': 'mary g decker comparison with article'
	},
    {
		'input': 'mary h langston;j. h. langston', 
		'expected': False, 
		'description': 'mary h langston comparison with article'
	},
    {
		'input': 'mary j lanier;mary jean lanier', 
		'expected': True, 
		'description': 'mary j lanier comparison with article'
	},
    {
		'input': 'mary l bell;mary laverne bell', 
		'expected': True, 
		'description': 'mary l bell comparison with article'
	},
    {
		'input': 'mary l caldwell;mary letitia caldwell', 
		'expected': True, 
		'description': 'mary l caldwell comparison with article'
	},
    {
		'input': 'mary l lewis;mary dearing lewis', 
		'expected': False, 
		'description': 'mary l lewis comparison with article'
	},
    {
		'input': 'mary l mcnair;maryhelen vannier', 
		'expected': False, 
		'description': 'mary l mcnair comparison with article'
	},
    {
		'input': 'mary lahlen;marya lilien', 
		'expected': False, 
		'description': 'mary lahlen comparison with article'
	},
    {
		'input': 'mary lebar;marry e. lebar', 
		'expected': True, 
		'description': 'mary lebar comparison with article'
	},
    {
		'input': 'mary lee lewis;mary teresine lewis', 
		'expected': False, 
		'description': 'mary lee lewis comparison with article'
	},
    {
		'input': 'mary lehn;mary belden james lehn', 
		'expected': True, 
		'description': 'mary lehn comparison with article'
	},
    {
		'input': 'mary leonard;mary katherine leonard', 
		'expected': True, 
		'description': 'mary leonard comparison with article'
	},
    {
		'input': 'mary m lazard;edmond myer lazard', 
		'expected': False, 
		'description': 'mary m lazard comparison with article'
	},
    {
		'input': 'mary p demerse;mary mercy', 
		'expected': False, 
		'description': 'mary p demerse comparison with article'
	},
    {
		'input': 'mary r austin;mary lellah austin', 
		'expected': False, 
		'description': 'mary r austin comparison with article'
	},
    {
		'input': 'mary sage;mary landon sague', 
		'expected': True, 
		'description': 'mary sage comparison with article'
	},
    {
		'input': 'mary t olegschlaeger;mary depaul oligsehlaeger', 
		'expected': False, 
		'description': 'mary t olegschlaeger comparison with article'
	},
    {
		'input': 'mary w denny;f. w. denny', 
		'expected': False, 
		'description': 'mary w denny comparison with article'
	},
    {
		'input': 'mary w ladue;mary watson ladue', 
		'expected': True, 
		'description': 'mary w ladue comparison with article'
	},
    {
		'input': 'mason ladd;mason ladd', 
		'expected': True, 
		'description': 'mason ladd comparison with article'
	},
    {
		'input': 'mathilda e vandenbergh;mathilda elsie vandenbergh', 
		'expected': True, 
		'description': 'mathilda e vandenbergh comparison with article'
	},
    {
		'input': 'matthew vanwinkle;matthew van winkle', 
		'expected': True, 
		'description': 'matthew vanwinkle comparison with article'
	},
    {
		'input': 'mattii lee williams;mentor lee williams', 
		'expected': False, 
		'description': 'mattii lee williams comparison with article'
	},
    {
		'input': 'maurice a thompson;maurice dekay thompson', 
		'expected': False, 
		'description': 'maurice a thompson comparison with article'
	},
    {
		'input': 'maurice b lagaard;maurice b. lagaard', 
		'expected': True, 
		'description': 'maurice b lagaard comparison with article'
	},
    {
		'input': 'maurice e leonard;maurice e. leonard', 
		'expected': True, 
		'description': 'maurice e leonard comparison with article'
	},
    {
		'input': 'maurice l hartung;maurice leslie hartung', 
		'expected': True, 
		'description': 'maurice l hartung comparison with article'
	},
    {
		'input': 'maurice l ray;maurice lee ray', 
		'expected': True, 
		'description': 'maurice l ray comparison with article'
	},
    {
		'input': 'maurice lee;maurice w. lee', 
		'expected': True, 
		'description': 'maurice lee comparison with article'
	},
    {
		'input': 'maurice lenz;maurice lenz', 
		'expected': True, 
		'description': 'maurice lenz comparison with article'
	},
    {
		'input': 'maurice levine;maurice levine', 
		'expected': True, 
		'description': 'maurice levine comparison with article'
	},
    {
		'input': 'maurice m vance;maurice m. vance', 
		'expected': True, 
		'description': 'maurice m vance comparison with article'
	},
    {
		'input': 'maurice r demers;m. r. demers', 
		'expected': True, 
		'description': 'maurice r demers comparison with article'
	},
    {
		'input': 'maurice t van hecke;maurice taylor van hecke', 
		'expected': True, 
		'description': 'maurice t van hecke comparison with article'
	},
    {
		'input': 'max a lauffer;max a. lauffer', 
		'expected': True, 
		'description': 'max a lauffer comparison with article'
	},
    {
		'input': 'max d wheatly, jr;max delby wheatley', 
		'expected': True, 
		'description': 'max d wheatly, jr comparison with article'
	},
    {
		'input': 'max delbruck;max delbruck', 
		'expected': True, 
		'description': 'max delbruck comparison with article'
	},
    {
		'input': 'max l moorhead;max leon moorhead', 
		'expected': True, 
		'description': 'max l moorhead comparison with article'
	},
    {
		'input': 'max lanner;max lanner', 
		'expected': True, 
		'description': 'max lanner comparison with article'
	},
    {
		'input': 'max lederman;leon max lederman', 
		'expected': True, 
		'description': 'max lederman comparison with article'
	},
    {
		'input': 'max lerner;max lerner', 
		'expected': True, 
		'description': 'max lerner comparison with article'
	},
    {
		'input': 'maxwell e lapham;maxwell edward lapham', 
		'expected': True, 
		'description': 'maxwell e lapham comparison with article'
	},
    {
		'input': 'maxwell eidenorf;maxwell leigh eidinoff', 
		'expected': True, 
		'description': 'maxwell eidenorf comparison with article'
	},
    {
		'input': 'maxwell farrow;maxwell deering farrow', 
		'expected': True, 
		'description': 'maxwell farrow comparison with article'
	},
    {
		'input': 'maxwell r lepper;maxwell r. lepper', 
		'expected': True, 
		'description': 'maxwell r lepper comparison with article'
	},
    {
		'input': 'may b van arsdale;may b. van arsdale', 
		'expected': True, 
		'description': 'may b van arsdale comparison with article'
	},
    {
		'input': 'may f lewis;f. harlan lewis', 
		'expected': False, 
		'description': 'may f lewis comparison with article'
	},
    {
		'input': 'maynard l mcdowell;maynard lee mcdowell', 
		'expected': True, 
		'description': 'maynard l mcdowell comparison with article'
	},
    {
		'input': 'meir degani;meir h. degani', 
		'expected': True, 
		'description': 'meir degani comparison with article'
	},
    {
		'input': 'melvin c lancaster;c. maxwell lancaster', 
		'expected': False, 
		'description': 'melvin c lancaster comparison with article'
	},
    {
		'input': 'melvin g de chazeau;melvin g. dechazeau', 
		'expected': True, 
		'description': 'melvin g de chazeau comparison with article'
	},
    {
		'input': 'melvin o k vandenbark;melvin van den bark', 
		'expected': True, 
		'description': 'melvin o k vandenbark comparison with article'
	},
    {
		'input': 'melvin s lewis;melvin s. lewis', 
		'expected': True, 
		'description': 'melvin s lewis comparison with article'
	},
    {
		'input': 'mena w lamb;mina wolf lamb', 
		'expected': True, 
		'description': 'mena w lamb comparison with article'
	},
    {
		'input': 'mendal e lash;mendel elmer lash', 
		'expected': True, 
		'description': 'mendal e lash comparison with article'
	},
    {
		'input': 'merle l landrum;merle l. landrum', 
		'expected': True, 
		'description': 'merle l landrum comparison with article'
	},
    {
		'input': 'merrill e daters;merrill edgar deters', 
		'expected': True, 
		'description': 'merrill e daters comparison with article'
	},
    {
		'input': 'mervin m deems;mervin monroe deems', 
		'expected': True, 
		'description': 'mervin m deems comparison with article'
	},
    {
		'input': 'meryl l burgan;r. l. von berg', 
		'expected': False, 
		'description': 'meryl l burgan comparison with article'
	},
    {
		'input': 'meryl w deming;meryl william deming', 
		'expected': True, 
		'description': 'meryl w deming comparison with article'
	},
    {
		'input': 'michael deangelis;michael deangelis', 
		'expected': True, 
		'description': 'michael deangelis comparison with article'
	},
    {
		'input': 'michael dil balso;michael j. del balso', 
		'expected': True, 
		'description': 'michael dil balso comparison with article'
	},
    {
		'input': 'michael i lerner;i. michael lerner', 
		'expected': True, 
		'description': 'michael i lerner comparison with article'
	},
    {
		'input': 'michael j dempsey;michael dempsey', 
		'expected': True, 
		'description': 'michael j dempsey comparison with article'
	},
    {
		'input': 'michael j litty;michael delich', 
		'expected': False, 
		'description': 'michael j litty comparison with article'
	},
    {
		'input': 'michael laskowski;michael laskowski', 
		'expected': True, 
		'description': 'michael laskowski comparison with article'
	},
    {
		'input': 'michael leszczynski;mieczyslaw peszczynski', 
		'expected': False, 
		'description': 'michael leszczynski comparison with article'
	},
    {
		'input': 'mildred k de longchamp;mildred k. delongchamp', 
		'expected': True, 
		'description': 'mildred k de longchamp comparison with article'
	},
    {
		'input': 'mildred larson;mildred r. larson', 
		'expected': True, 
		'description': 'mildred larson comparison with article'
	},
    {
		'input': 'mildred s lewis;mildred sinclair lewis', 
		'expected': True, 
		'description': 'mildred s lewis comparison with article'
	},
    {
		'input': 'miles l hanley;miles lawrence hanley', 
		'expected': True, 
		'description': 'miles l hanley comparison with article'
	},
    {
		'input': 'milton b lennon;milton b. lennon', 
		'expected': True, 
		'description': 'milton b lennon comparison with article'
	},
    {
		'input': 'milton dell;samuel milton dell', 
		'expected': True, 
		'description': 'milton dell comparison with article'
	},
    {
		'input': 'milton h levy;milton levy', 
		'expected': True, 
		'description': 'milton h levy comparison with article'
	},
    {
		'input': 'milton l shane;milton lanning shane', 
		'expected': True, 
		'description': 'milton l shane comparison with article'
	},
    {
		'input': 'milton l sunde;milton lester sunde', 
		'expected': True, 
		'description': 'milton l sunde comparison with article'
	},
    {
		'input': 'milton l wiedmann;milton lawrence wiedmann', 
		'expected': True, 
		'description': 'milton l wiedmann comparison with article'
	},
    {
		'input': 'milton lebow;milton j. lebow', 
		'expected': True, 
		'description': 'milton lebow comparison with article'
	},
    {
		'input': 'milton scott;milton leonard scott', 
		'expected': True, 
		'description': 'milton scott comparison with article'
	},
    {
		'input': 'minnie e langwell;alfred edwin longueil', 
		'expected': False, 
		'description': 'minnie e langwell comparison with article'
	},
    {
		'input': 'minor u latham;minor white latham', 
		'expected': False, 
		'description': 'minor u latham comparison with article'
	},
    {
		'input': 'miriam dell;miriam dell', 
		'expected': True, 
		'description': 'miriam dell comparison with article'
	},
    {
		'input': 'mitchell a lata;mitchell a. light', 
		'expected': False, 
		'description': 'mitchell a lata comparison with article'
	},
    {
		'input': 'mollie k laird;alan d. k. laird', 
		'expected': False, 
		'description': 'mollie k laird comparison with article'
	},
    {
		'input': 'monroe e deutsch;monroe e. deutsch', 
		'expected': True, 
		'description': 'monroe e deutsch comparison with article'
	},
    {
		'input': 'monte m lemann;monte m. lemann', 
		'expected': True, 
		'description': 'monte m lemann comparison with article'
	},
    {
		'input': 'morris b lambie;morris bryan lambie', 
		'expected': True, 
		'description': 'morris b lambie comparison with article'
	},
    {
		'input': 'morris denerstein;morris dinnerstein', 
		'expected': True, 
		'description': 'morris denerstein comparison with article'
	},
    {
		'input': 'morris lazerowitz;morris lazerowitz', 
		'expected': True, 
		'description': 'morris lazerowitz comparison with article'
	},
    {
		'input': 'muriel l bishop;merle lamont bishop', 
		'expected': False, 
		'description': 'muriel l bishop comparison with article'
	},
    {
		'input': 'muriel l white;kerr lachlan white', 
		'expected': False, 
		'description': 'muriel l white comparison with article'
	},
    {
		'input': 'muriel s guberlet;muriel lewin guberlet', 
		'expected': False, 
		'description': 'muriel s guberlet comparison with article'
	},
    {
		'input': 'myles g mace;myles la grange mace', 
		'expected': True, 
		'description': 'myles g mace comparison with article'
	},
    {
		'input': 'myles mace;myles la grange mace', 
		'expected': True, 
		'description': 'myles mace comparison with article'
	},
    {
		'input': 'myra l bishop;myra leslie bishop', 
		'expected': True, 
		'description': 'myra l bishop comparison with article'
	},
    {
		'input': 'myron d lacy;myron dean lacy', 
		'expected': True, 
		'description': 'myron d lacy comparison with article'
	},
    {
		'input': 'myron l williams;myron lawson williams', 
		'expected': True, 
		'description': 'myron l williams comparison with article'
	},
    {
		'input': 'myrtle m larro;loida m. lerew', 
		'expected': False, 
		'description': 'myrtle m larro comparison with article'
	},
    {
		'input': 'n lewis buck;n. lewis buck', 
		'expected': True, 
		'description': 'n lewis buck comparison with article'
	},
    {
		'input': 'nancy d lewis;nancy duke lewis', 
		'expected': True, 
		'description': 'nancy d lewis comparison with article'
	},
    {
		'input': 'nancy e. lewis;nancy e. lewis', 
		'expected': True, 
		'description': 'nancy e. lewis comparison with article'
	},
    {
		'input': 'nancy lee lytle;nancy lytle', 
		'expected': True, 
		'description': 'nancy lee lytle comparison with article'
	},
    {
		'input': 'naomi laughbaum;naomi may laughbaum', 
		'expected': True, 
		'description': 'naomi laughbaum comparison with article'
	},
    {
		'input': 'natalia h latta;harrison latta', 
		'expected': True, 
		'description': 'natalia h latta comparison with article'
	},
    {
		'input': 'natalie lawrence;natalie grimes lawrence', 
		'expected': True, 
		'description': 'natalie lawrence comparison with article'
	},
    {
		'input': 'nathan k lazar;nathan k. lazar', 
		'expected': True, 
		'description': 'nathan k lazar comparison with article'
	},
    {
		'input': 'nathaniel m lawrence;nathaniel morris lawrence', 
		'expected': True, 
		'description': 'nathaniel m lawrence comparison with article'
	},
    {
		'input': 'neal b de nood;neal breaule denood', 
		'expected': True, 
		'description': 'neal b de nood comparison with article'
	},
    {
		'input': 'nelda r lawrence;nelda r. lawrence', 
		'expected': True, 
		'description': 'nelda r lawrence comparison with article'
	},
    {
		'input': 'nellie c white;c. langdon white', 
		'expected': False, 
		'description': 'nellie c white comparison with article'
	},
    {
		'input': 'nelson l walbridge;nelson lee walbridge', 
		'expected': True, 
		'description': 'nelson l walbridge comparison with article'
	},
    {
		'input': 'nelson laplante;nelson a. la plante', 
		'expected': True, 
		'description': 'nelson laplante comparison with article'
	},
    {
		'input': 'neppie conner;neppie lee conner', 
		'expected': True, 
		'description': 'neppie conner comparison with article'
	},
    {
		'input': 'nerris e. lenahan;norris e. lenahan', 
		'expected': True, 
		'description': 'nerris e. lenahan comparison with article'
	},
    {
		'input': 'newell l sims;newell leroy sims', 
		'expected': True, 
		'description': 'newell l sims comparison with article'
	},
    {
		'input': 'ney l macminn;ney lannes macminn', 
		'expected': True, 
		'description': 'ney l macminn comparison with article'
	},
    {
		'input': 'nicholas m lazar;nicholas m. lazar', 
		'expected': True, 
		'description': 'nicholas m lazar comparison with article'
	},
    {
		'input': 'nickolas j demerath;nicholas jay demerath', 
		'expected': True, 
		'description': 'nickolas j demerath comparison with article'
	},
    {
		'input': 'nielson van de luyster;nelson van de luyster', 
		'expected': True, 
		'description': 'nielson van de luyster comparison with article'
	},
    {
		'input': 'nina g dean;nina o. dean', 
		'expected': False, 
		'description': 'nina g dean comparison with article'
	},
    {
		'input': 'nina l weisinger;nina lee weisinger', 
		'expected': True, 
		'description': 'nina l weisinger comparison with article'
	},
    {
		'input': 'noland l van demark;noland l. vandemark', 
		'expected': True, 
		'description': 'noland l van demark comparison with article'
	},
    {
		'input': 'nophtali lewis;naphtali lewis', 
		'expected': True, 
		'description': 'nophtali lewis comparison with article'
	},
    {
		'input': 'norma w densmore;warren i densmore', 
		'expected': False, 
		'description': 'norma w densmore comparison with article'
	},
    {
		'input': 'norman b lavers;norman l. lavers', 
		'expected': False, 
		'description': 'norman b lavers comparison with article'
	},
    {
		'input': 'norman b mac lean;norman f. maclean', 
		'expected': False, 
		'description': 'norman b mac lean comparison with article'
	},
    {
		'input': 'norman c laffer;norman c. laffer', 
		'expected': True, 
		'description': 'norman c laffer comparison with article'
	},
    {
		'input': 'norman d levine;norman d. levine', 
		'expected': True, 
		'description': 'norman d levine comparison with article'
	},
    {
		'input': 'norman e lange;norman e. lange', 
		'expected': True, 
		'description': 'norman e lange comparison with article'
	},
    {
		'input': 'norman f degrasse;norman scott brien gras', 
		'expected': False, 
		'description': 'norman f degrasse comparison with article'
	},
    {
		'input': 'norman l jacobson;norman leonard jacobson', 
		'expected': True, 
		'description': 'norman l jacobson comparison with article'
	},
    {
		'input': 'norman lawrence;norman lionel lawrence', 
		'expected': True, 
		'description': 'norman lawrence comparison with article'
	},
    {
		'input': 'norman r munn;norman leslie munn', 
		'expected': False, 
		'description': 'norman r munn comparison with article'
	},
    {
		'input': 'norman torrey;norman lewis torrey', 
		'expected': True, 
		'description': 'norman torrey comparison with article'
	},
    {
		'input': 'noyes leech;noyes e. leech', 
		'expected': True, 
		'description': 'noyes leech comparison with article'
	},
    {
		'input': 'o lee gibson;oscar lee gibson', 
		'expected': True, 
		'description': 'o lee gibson comparison with article'
	},
    {
		'input': 'obed l snowden;obed lavelle snowden', 
		'expected': True, 
		'description': 'obed l snowden comparison with article'
	},
    {
		'input': 'olaf larson;olaf frederick larson', 
		'expected': True, 
		'description': 'olaf larson comparison with article'
	},
    {
		'input': 'olga larson;olga larson', 
		'expected': True, 
		'description': 'olga larson comparison with article'
	},
    {
		'input': 'olin d morrison;olin dee morrison', 
		'expected': True, 
		'description': 'olin d morrison comparison with article'
	},
    {
		'input': 'olive deluce;olive s. deluce', 
		'expected': True, 
		'description': 'olive deluce comparison with article'
	},
    {
		'input': 'olive k lawyer;kenneth lawyer', 
		'expected': True, 
		'description': 'olive k lawyer comparison with article'
	},
    {
		'input': 'olive p lester;olive p. lester', 
		'expected': True, 
		'description': 'olive p lester comparison with article'
	},
    {
		'input': 'oliver c lee;oliver christopher lee', 
		'expected': True, 
		'description': 'oliver c lee comparison with article'
	},
    {
		'input': 'oliver l rieser;oliver leslie reiser', 
		'expected': True, 
		'description': 'oliver l rieser comparison with article'
	},
    {
		'input': 'oliver l walker;oliver lafayette walker', 
		'expected': True, 
		'description': 'oliver l walker comparison with article'
	},
    {
		'input': 'oliver laymon;oliver laymon', 
		'expected': True, 
		'description': 'oliver laymon comparison with article'
	},
    {
		'input': 'oliver lee;oliver justin lee', 
		'expected': True, 
		'description': 'oliver lee comparison with article'
	},
    {
		'input': 'oliver m langhorst;oliver martin langhorst', 
		'expected': True, 
		'description': 'oliver m langhorst comparison with article'
	},
    {
		'input': 'oliver w larkin;oliver waterman larkin', 
		'expected': True, 
		'description': 'oliver w larkin comparison with article'
	},
    {
		'input': 'orland lefforge;orland s. lefforge', 
		'expected': True, 
		'description': 'orland lefforge comparison with article'
	},
    {
		'input': 'orlando r laurandt;val r. lorwin', 
		'expected': False, 
		'description': 'orlando r laurandt comparison with article'
	},
    {
		'input': 'orlo derby;orlo derby', 
		'expected': True, 
		'description': 'orlo derby comparison with article'
	},
    {
		'input': 'orvil l pence;orville leon pence', 
		'expected': True, 
		'description': 'orvil l pence comparison with article'
	},
    {
		'input': 'oscar j laplante;oscar j. laplante', 
		'expected': True, 
		'description': 'oscar j laplante comparison with article'
	},
    {
		'input': 'oscar lanford;oscar e. lanford', 
		'expected': True, 
		'description': 'oscar lanford comparison with article'
	},
    {
		'input': 'oscar lassner;oscar lassner', 
		'expected': True, 
		'description': 'oscar lassner comparison with article'
	},
    {
		'input': 'oscar lewis;oscar lewis', 
		'expected': True, 
		'description': 'oscar lewis comparison with article'
	},
    {
		'input': 'oskar f l hagen;oskar frank leonard hagen', 
		'expected': True, 
		'description': 'oskar f l hagen comparison with article'
	},
    {
		'input': 'otta a leistiko;daniel a. listiak', 
		'expected': False, 
		'description': 'otta a leistiko comparison with article'
	},
    {
		'input': 'otto g von simson;otto georg von simson', 
		'expected': True, 
		'description': 'otto g von simson comparison with article'
	},
    {
		'input': 'otto van koppenhagen;otto van koppenhagen', 
		'expected': True, 
		'description': 'otto van koppenhagen comparison with article'
	},
    {
		'input': 'p eldon dennis;philip eldon dennis', 
		'expected': True, 
		'description': 'p eldon dennis comparison with article'
	},
    {
		'input': 'p j leinfelder;placidus joseph leinfelder', 
		'expected': True, 
		'description': 'p j leinfelder comparison with article'
	},
    {
		'input': 'paul a leidy;paul allen leidy', 
		'expected': True, 
		'description': 'paul a leidy comparison with article'
	},
    {
		'input': 'paul b larson;paul b. larson', 
		'expected': True, 
		'description': 'paul b larson comparison with article'
	},
    {
		'input': 'paul b lawrence;paul roger lawrence', 
		'expected': False, 
		'description': 'paul b lawrence comparison with article'
	},
    {
		'input': 'paul b lawson;paul b. lawson', 
		'expected': True, 
		'description': 'paul b lawson comparison with article'
	},
    {
		'input': 'paul b leonard;paul bonar leonard', 
		'expected': True, 
		'description': 'paul b leonard comparison with article'
	},
    {
		'input': 'paul c lemon;paul c. lemon', 
		'expected': True, 
		'description': 'paul c lemon comparison with article'
	},
    {
		'input': 'paul c munson;paul lewis munson', 
		'expected': False, 
		'description': 'paul c munson comparison with article'
	},
    {
		'input': 'paul d clark;paul dennison clark', 
		'expected': True, 
		'description': 'paul d clark comparison with article'
	},
    {
		'input': 'paul d evans;paul demund evans', 
		'expected': True, 
		'description': 'paul d evans comparison with article'
	},
    {
		'input': 'paul d lamson;paul dudley lamson', 
		'expected': True, 
		'description': 'paul d lamson comparison with article'
	},
    {
		'input': 'paul dehart hurd;paul deh. hurd', 
		'expected': True, 
		'description': 'paul dehart hurd comparison with article'
	},
    {
		'input': 'paul e lewis;paul edwin lewis', 
		'expected': True, 
		'description': 'paul e lewis comparison with article'
	},
    {
		'input': 'paul f de wiese;paul f. deweese', 
		'expected': True, 
		'description': 'paul f de wiese comparison with article'
	},
    {
		'input': 'paul f garm, jr;e. paul degarmo', 
		'expected': False, 
		'description': 'paul f garm, jr comparison with article'
	},
    {
		'input': 'paul f laubenstein;paul fritz laubenstein', 
		'expected': True, 
		'description': 'paul f laubenstein comparison with article'
	},
    {
		'input': 'paul f lazarsfeld;paul f. lazarsfeld', 
		'expected': True, 
		'description': 'paul f lazarsfeld comparison with article'
	},
    {
		'input': 'paul f leedy;paul f. leedy', 
		'expected': True, 
		'description': 'paul f leedy comparison with article'
	},
    {
		'input': 'paul g lehman;frederick g. lehman', 
		'expected': False, 
		'description': 'paul g lehman comparison with article'
	},
    {
		'input': 'paul h deeb;paul h. deeb', 
		'expected': True, 
		'description': 'paul h deeb comparison with article'
	},
    {
		'input': 'paul h landis;paul h. landis', 
		'expected': True, 
		'description': 'paul h landis comparison with article'
	},
    {
		'input': 'paul h lavietes;paul harold lavietes', 
		'expected': True, 
		'description': 'paul h lavietes comparison with article'
	},
    {
		'input': 'paul h spencer;paul leslie spencer', 
		'expected': False, 
		'description': 'paul h spencer comparison with article'
	},
    {
		'input': 'paul hartman;paul leon hartman', 
		'expected': True, 
		'description': 'paul hartman comparison with article'
	},
    {
		'input': 'paul j von ebers;paul j. von ebers', 
		'expected': True, 
		'description': 'paul j von ebers comparison with article'
	},
    {
		'input': 'paul k vonk;paul k. vonk', 
		'expected': True, 
		'description': 'paul k vonk comparison with article'
	},
    {
		'input': 'paul l brown;paul lawrence brown', 
		'expected': True, 
		'description': 'paul l brown comparison with article'
	},
    {
		'input': 'paul l davies;paul lewis davies', 
		'expected': True, 
		'description': 'paul l davies comparison with article'
	},
    {
		'input': 'paul l errington;paul lester errington', 
		'expected': True, 
		'description': 'paul l errington comparison with article'
	},
    {
		'input': 'paul l kelley;paul leo kelley', 
		'expected': True, 
		'description': 'paul l kelley comparison with article'
	},
    {
		'input': 'paul l mackendrick;paul lachlan niackendrick', 
		'expected': True, 
		'description': 'paul l mackendrick comparison with article'
	},
    {
		'input': 'paul l mclain;paul larimer mclain', 
		'expected': True, 
		'description': 'paul l mclain comparison with article'
	},
    {
		'input': 'paul l mellenbruch;parl leslie mellenbruch', 
		'expected': False, 
		'description': 'paul l mellenbruch comparison with article'
	},
    {
		'input': 'paul l soper;paul leon soper', 
		'expected': True, 
		'description': 'paul l soper comparison with article'
	},
    {
		'input': 'paul l trump, jr;paul leroy trump', 
		'expected': True, 
		'description': 'paul l trump, jr comparison with article'
	},
    {
		'input': 'paul l whitely;paul leroy whitely', 
		'expected': True, 
		'description': 'paul l whitely comparison with article'
	},
    {
		'input': 'paul leberman;paul r. leberman', 
		'expected': True, 
		'description': 'paul leberman comparison with article'
	},
    {
		'input': 'paul levine;robert paul levine', 
		'expected': True, 
		'description': 'paul levine comparison with article'
	},
    {
		'input': 'paul m dean;paul m. dean', 
		'expected': True, 
		'description': 'paul m dean comparison with article'
	},
    {
		'input': 'paul m o\' leary;paul m. o\'leary', 
		'expected': True, 
		'description': 'paul m o\' leary comparison with article'
	},
    {
		'input': 'paul n landis;paul nissley landis', 
		'expected': True, 
		'description': 'paul n landis comparison with article'
	},
    {
		'input': 'paul n. lehoczky;paul n. lehoczky', 
		'expected': True, 
		'description': 'paul n. lehoczky comparison with article'
	},
    {
		'input': 'paul r dean;paul r. dean', 
		'expected': True, 
		'description': 'paul r dean comparison with article'
	},
    {
		'input': 'paul s lavik;paul sophus lavik', 
		'expected': True, 
		'description': 'paul s lavik comparison with article'
	},
    {
		'input': 'paul t de camp;paul trumbull decamp', 
		'expected': True, 
		'description': 'paul t de camp comparison with article'
	},
    {
		'input': 'paul v lemkau;paul anthony lembcke', 
		'expected': False, 
		'description': 'paul v lemkau comparison with article'
	},
    {
		'input': 'paul v lemkau;paul victor lemkau', 
		'expected': True, 
		'description': 'paul v lemkau comparison with article'
	},
    {
		'input': 'paul v thomson;paul van k. thomson', 
		'expected': True, 
		'description': 'paul v thomson comparison with article'
	},
    {
		'input': 'paul van b jones;paul van brunt jones', 
		'expected': True, 
		'description': 'paul van b jones comparison with article'
	},
    {
		'input': 'paul vanarsdell;paul m. van arsdell', 
		'expected': True, 
		'description': 'paul vanarsdell comparison with article'
	},
    {
		'input': 'paul vanketwick;paul van katwijk', 
		'expected': True, 
		'description': 'paul vanketwick comparison with article'
	},
    {
		'input': 'paula c maynoy;carl lamanna', 
		'expected': False, 
		'description': 'paula c maynoy comparison with article'
	},
    {
		'input': 'percy d wilkins;percy desmond wilkins', 
		'expected': True, 
		'description': 'percy d wilkins comparison with article'
	},
    {
		'input': 'percy l gainey;percy leigh gainey', 
		'expected': True, 
		'description': 'percy l gainey comparison with article'
	},
    {
		'input': 'perley l thorne;perley lenwood thorne', 
		'expected': True, 
		'description': 'perley l thorne comparison with article'
	},
    {
		'input': 'perry p. denune;perry p. denune', 
		'expected': True, 
		'description': 'perry p. denune comparison with article'
	},
    {
		'input': 'perry v miller;perry van miller', 
		'expected': True, 
		'description': 'perry v miller comparison with article'
	},
    {
		'input': 'perry w vanwagenen;richard whitmore van wagenen', 
		'expected': False, 
		'description': 'perry w vanwagenen comparison with article'
	},
    {
		'input': 'peter a corsi;andrew delcorso', 
		'expected': False, 
		'description': 'peter a corsi comparison with article'
	},
    {
		'input': 'peter dennis;peter g. danis', 
		'expected': True, 
		'description': 'peter dennis comparison with article'
	},
    {
		'input': 'peter p h de bruyn;peter p. h. de bruyn', 
		'expected': True, 
		'description': 'peter p h de bruyn comparison with article'
	},
    {
		'input': 'peter p lawlor, jr;peter paul lawlor', 
		'expected': True, 
		'description': 'peter p lawlor, jr comparison with article'
	},
    {
		'input': 'peter p lejins;peter p. lejins', 
		'expected': True, 
		'description': 'peter p lejins comparison with article'
	},
    {
		'input': 'peter vandekamp;peter van de kamp', 
		'expected': True, 
		'description': 'peter vandekamp comparison with article'
	},
    {
		'input': 'philip f lerner;philip franklin lerner', 
		'expected': True, 
		'description': 'philip f lerner comparison with article'
	},
    {
		'input': 'philip h de lacy;phillip h. delacy', 
		'expected': True, 
		'description': 'philip h de lacy comparison with article'
	},
    {
		'input': 'philip l carpenter;philip lewis carpenter', 
		'expected': True, 
		'description': 'philip l carpenter comparison with article'
	},
    {
		'input': 'philip l debruyn;philip louis de bruyn', 
		'expected': True, 
		'description': 'philip l debruyn comparison with article'
	},
    {
		'input': 'philip l peterson;philip lawrence peterson', 
		'expected': True, 
		'description': 'philip l peterson comparison with article'
	},
    {
		'input': 'philip l shipe;philip leister shipe', 
		'expected': True, 
		'description': 'philip l shipe comparison with article'
	},
    {
		'input': 'philip leighton;philip albert leighton', 
		'expected': True, 
		'description': 'philip leighton comparison with article'
	},
    {
		'input': 'philip levine;philip levine', 
		'expected': True, 
		'description': 'philip levine comparison with article'
	},
    {
		'input': 'philipp lecorbielle;philippe emmanuel lecorbeiller', 
		'expected': True, 
		'description': 'philipp lecorbielle comparison with article'
	},
    {
		'input': 'phillip e lear;phillip e. lear', 
		'expected': True, 
		'description': 'phillip e lear comparison with article'
	},
    {
		'input': 'phillippe de la mare;philippe r. de la mare', 
		'expected': True, 
		'description': 'phillippe de la mare comparison with article'
	},
    {
		'input': 'phineas l windsor;phineas lawrence windsor', 
		'expected': True, 
		'description': 'phineas l windsor comparison with article'
	},
    {
		'input': 'pierre van rysselberghe;pierre j. van rysselberghe', 
		'expected': True, 
		'description': 'pierre van rysselberghe comparison with article'
	},
    {
		'input': 'pilar madariaga;pilar de madariaga', 
		'expected': True, 
		'description': 'pilar madariaga comparison with article'
	},
    {
		'input': 'pincus p levine;pincus philip levine', 
		'expected': True, 
		'description': 'pincus p levine comparison with article'
	},
    {
		'input': 'quentin (none) van winkle;quentin van winkle', 
		'expected': True, 
		'description': 'quentin (none) van winkle comparison with article'
	},
    {
		'input': 'quinn b demarsh;quin b. de marsh', 
		'expected': True, 
		'description': 'quinn b demarsh comparison with article'
	},
    {
		'input': 'r clark lewis;daniel clark lewis', 
		'expected': False, 
		'description': 'r clark lewis comparison with article'
	},
    {
		'input': 'r ernest leffel;r. e. leffel', 
		'expected': True, 
		'description': 'r ernest leffel comparison with article'
	},
    {
		'input': 'r lamar newport;lamar newport', 
		'expected': True, 
		'description': 'r lamar newport comparison with article'
	},
    {
		'input': 'r lee martin;r. lee martin', 
		'expected': True, 
		'description': 'r lee martin comparison with article'
	},
    {
		'input': 'rachael w deangelo;rachael wingfield de angelo', 
		'expected': True, 
		'description': 'rachael w deangelo comparison with article'
	},
    {
		'input': 'raffaele lattes;raffaele lattes', 
		'expected': True, 
		'description': 'raffaele lattes comparison with article'
	},
    {
		'input': 'ralph a langsam;ralph h. langsam', 
		'expected': False, 
		'description': 'ralph a langsam comparison with article'
	},
    {
		'input': 'ralph a lassance;ralph a. lassance', 
		'expected': True, 
		'description': 'ralph a lassance comparison with article'
	},
    {
		'input': 'ralph a van wye;ralph a. van wye', 
		'expected': True, 
		'description': 'ralph a van wye comparison with article'
	},
    {
		'input': 'ralph a. deterling;ralph a. deterling', 
		'expected': True, 
		'description': 'ralph a. deterling comparison with article'
	},
    {
		'input': 'ralph defalco;ralph j. defalco', 
		'expected': True, 
		'description': 'ralph defalco comparison with article'
	},
    {
		'input': 'ralph e deal;ralph elbert deal', 
		'expected': True, 
		'description': 'ralph e deal comparison with article'
	},
    {
		'input': 'ralph e lane;ralph e. lane', 
		'expected': True, 
		'description': 'ralph e lane comparison with article'
	},
    {
		'input': 'ralph e lewis;ralph elton lewis', 
		'expected': True, 
		'description': 'ralph e lewis comparison with article'
	},
    {
		'input': 'ralph e vanhorn;ralph e. hone', 
		'expected': False, 
		'description': 'ralph e vanhorn comparison with article'
	},
    {
		'input': 'ralph e. lancaster;ralph e. lancaster', 
		'expected': True, 
		'description': 'ralph e. lancaster comparison with article'
	},
    {
		'input': 'ralph l cope;ralph leland cope', 
		'expected': True, 
		'description': 'ralph l cope comparison with article'
	},
    {
		'input': 'ralph l dannley;ralph lawrence dannley', 
		'expected': True, 
		'description': 'ralph l dannley comparison with article'
	},
    {
		'input': 'ralph l davis;ralph lanier davis', 
		'expected': True, 
		'description': 'ralph l davis comparison with article'
	},
    {
		'input': 'ralph l de flower;leo gerson doefler', 
		'expected': False, 
		'description': 'ralph l de flower comparison with article'
	},
    {
		'input': 'ralph l eyman;ralph lee eyman', 
		'expected': True, 
		'description': 'ralph l eyman comparison with article'
	},
    {
		'input': 'ralph l langenheim;ralph l. langenheim', 
		'expected': True, 
		'description': 'ralph l langenheim comparison with article'
	},
    {
		'input': 'ralph l thompson;ralph leroy thompson', 
		'expected': True, 
		'description': 'ralph l thompson comparison with article'
	},
    {
		'input': 'ralph l. dewey;ralph l. dewey', 
		'expected': True, 
		'description': 'ralph l. dewey comparison with article'
	},
    {
		'input': 'ralph ledley;ralph g. ledley', 
		'expected': True, 
		'description': 'ralph ledley comparison with article'
	},
    {
		'input': 'ralph lefler;ralph waldo lefler', 
		'expected': True, 
		'description': 'ralph lefler comparison with article'
	},
    {
		'input': 'ralph m lakness;ralph m. lakness', 
		'expected': True, 
		'description': 'ralph m lakness comparison with article'
	},
    {
		'input': 'ralph r lashbrook;ralph richard lashbrook', 
		'expected': True, 
		'description': 'ralph r lashbrook comparison with article'
	},
    {
		'input': 'ralph r lawrence;ralph restieaux lawrence', 
		'expected': True, 
		'description': 'ralph r lawrence comparison with article'
	},
    {
		'input': 'ralph v bangham;ralph vandervort bangham', 
		'expected': True, 
		'description': 'ralph v bangham comparison with article'
	},
    {
		'input': 'randolph l carter;randolph laurie carter', 
		'expected': True, 
		'description': 'randolph l carter comparison with article'
	},
    {
		'input': 'randy h laidlaw;harry h. laidlaw', 
		'expected': False, 
		'description': 'randy h laidlaw comparison with article'
	},
    {
		'input': 'raphael demos;raphael demos', 
		'expected': True, 
		'description': 'raphael demos comparison with article'
	},
    {
		'input': 'raphael levy;raphael levy', 
		'expected': True, 
		'description': 'raphael levy comparison with article'
	},
    {
		'input': 'ray g langebartel;ray g. langebartel', 
		'expected': True, 
		'description': 'ray g langebartel comparison with article'
	},
    {
		'input': 'ray l edwards;ray lee edwards', 
		'expected': True, 
		'description': 'ray l edwards comparison with article'
	},
    {
		'input': 'ray l shappelle;ray leon chappelle', 
		'expected': True, 
		'description': 'ray l shappelle comparison with article'
	},
    {
		'input': 'ray l watterson;ray leighton watterson', 
		'expected': True, 
		'description': 'ray l watterson comparison with article'
	},
    {
		'input': 'raymond c dein;r. c. dein', 
		'expected': True, 
		'description': 'raymond c dein comparison with article'
	},
    {
		'input': 'raymond e lanhard, jr;raymond earl lenhard', 
		'expected': True, 
		'description': 'raymond e lanhard, jr comparison with article'
	},
    {
		'input': 'raymond g larson;raymond george larson', 
		'expected': True, 
		'description': 'raymond g larson comparison with article'
	},
    {
		'input': 'raymond h borkenhogen;peter h. von blanckenhagen', 
		'expected': False, 
		'description': 'raymond h borkenhogen comparison with article'
	},
    {
		'input': 'raymond j adams;raymond delacy adams', 
		'expected': False, 
		'description': 'raymond j adams comparison with article'
	},
    {
		'input': 'raymond kendall;raymond leon kendall', 
		'expected': True, 
		'description': 'raymond kendall comparison with article'
	},
    {
		'input': 'raymond l davidson;raymond leon davidson', 
		'expected': True, 
		'description': 'raymond l davidson comparison with article'
	},
    {
		'input': 'raymond l hightower;raymond lee hightower', 
		'expected': True, 
		'description': 'raymond l hightower comparison with article'
	},
    {
		'input': 'raymond l lind;raymond e. vanderlinde', 
		'expected': False, 
		'description': 'raymond l lind comparison with article'
	},
    {
		'input': 'raymond l murdoch;raymond lester murdoch', 
		'expected': True, 
		'description': 'raymond l murdoch comparison with article'
	},
    {
		'input': 'raymond l powell;raymond leo powell', 
		'expected': True, 
		'description': 'raymond l powell comparison with article'
	},
    {
		'input': 'raymond l shoemaker;raymond leroy shoemaker', 
		'expected': True, 
		'description': 'raymond l shoemaker comparison with article'
	},
    {
		'input': 'raymond l. hill;raymond leroy hill', 
		'expected': True, 
		'description': 'raymond l. hill comparison with article'
	},
    {
		'input': 'raymond lee thompson;raymond harris thompson', 
		'expected': False, 
		'description': 'raymond lee thompson comparison with article'
	},
    {
		'input': 'raymond murray;raymond leroy murray', 
		'expected': True, 
		'description': 'raymond murray comparison with article'
	},
    {
		'input': 'raymond s bisplinghoff;raymond lewis bisplinghoff', 
		'expected': False, 
		'description': 'raymond s bisplinghoff comparison with article'
	},
    {
		'input': 'raymond t dewitt;r. t. dewitt', 
		'expected': True, 
		'description': 'raymond t dewitt comparison with article'
	},
    {
		'input': 'raymond v lesikar;raymond v. lesikar', 
		'expected': True, 
		'description': 'raymond v lesikar comparison with article'
	},
    {
		'input': 'reginald h mc lean;ross h. mclean', 
		'expected': False, 
		'description': 'reginald h mc lean comparison with article'
	},
    {
		'input': 'reidar l anderson;reidar lars anderson', 
		'expected': True, 
		'description': 'reidar l anderson comparison with article'
	},
    {
		'input': 'reinhold f larson;reinhold fridtjof larson', 
		'expected': True, 
		'description': 'reinhold f larson comparison with article'
	},
    {
		'input': 'rena m larue;rena larue', 
		'expected': True, 
		'description': 'rena m larue comparison with article'
	},
    {
		'input': 'reuben law;reuben d. law', 
		'expected': True, 
		'description': 'reuben law comparison with article'
	},
    {
		'input': 'rev benedict lenz;benedict lenz', 
		'expected': True, 
		'description': 'rev benedict lenz comparison with article'
	},
    {
		'input': 'rev denis strittmatter;denis strittmatter', 
		'expected': True, 
		'description': 'rev denis strittmatter comparison with article'
	},
    {
		'input': 'rev edmund langton;edmund langton', 
		'expected': True, 
		'description': 'rev edmund langton comparison with article'
	},
    {
		'input': 'rex depew;rex d. depew', 
		'expected': True, 
		'description': 'rex depew comparison with article'
	},
    {
		'input': 'richard a lang;andrew richard lang', 
		'expected': True, 
		'description': 'richard a lang comparison with article'
	},
    {
		'input': 'richard a lester;richard allen lester', 
		'expected': True, 
		'description': 'richard a lester comparison with article'
	},
    {
		'input': 'richard a van leer;richard t. lyer', 
		'expected': False, 
		'description': 'richard a van leer comparison with article'
	},
    {
		'input': 'richard c. larkins;richard c. larkins', 
		'expected': True, 
		'description': 'richard c. larkins comparison with article'
	},
    {
		'input': 'richard d challener;richard delo challener', 
		'expected': True, 
		'description': 'richard d challener comparison with article'
	},
    {
		'input': 'richard de bodo;richard c. de bodo', 
		'expected': True, 
		'description': 'richard de bodo comparison with article'
	},
    {
		'input': 'richard deimel;richard francis deimel', 
		'expected': True, 
		'description': 'richard deimel comparison with article'
	},
    {
		'input': 'richard dewey;richard s. dewey', 
		'expected': True, 
		'description': 'richard dewey comparison with article'
	},
    {
		'input': 'richard f dean;richard dean', 
		'expected': True, 
		'description': 'richard f dean comparison with article'
	},
    {
		'input': 'richard h van saun;h. richard van saun', 
		'expected': True, 
		'description': 'richard h van saun comparison with article'
	},
    {
		'input': 'richard j deyoung;richard de young', 
		'expected': True, 
		'description': 'richard j deyoung comparison with article'
	},
    {
		'input': 'richard l clark;richard leon clark', 
		'expected': True, 
		'description': 'richard l clark comparison with article'
	},
    {
		'input': 'richard l landau;richard louis landau', 
		'expected': True, 
		'description': 'richard l landau comparison with article'
	},
    {
		'input': 'richard l sawyer;richard leander sawyer', 
		'expected': True, 
		'description': 'richard l sawyer comparison with article'
	},
    {
		'input': 'richard l scammon;richard lewis scammon', 
		'expected': True, 
		'description': 'richard l scammon comparison with article'
	},
    {
		'input': 'richard l solomon;richard lester solomon', 
		'expected': True, 
		'description': 'richard l solomon comparison with article'
	},
    {
		'input': 'richard l. fulton;richard la marr fulton', 
		'expected': True, 
		'description': 'richard l. fulton comparison with article'
	},
    {
		'input': 'richard l. rudy;richard lee rudy', 
		'expected': True, 
		'description': 'richard l. rudy comparison with article'
	},
    {
		'input': 'richard la piere;richard tracy lapiere', 
		'expected': True, 
		'description': 'richard la piere comparison with article'
	},
    {
		'input': 'richard lee huntington;richard lee huntington', 
		'expected': True, 
		'description': 'richard lee huntington comparison with article'
	},
    {
		'input': 'richard lee patton;richard patton', 
		'expected': True, 
		'description': 'richard lee patton comparison with article'
	},
    {
		'input': 'richard morse;richard lawrence day morse', 
		'expected': True, 
		'description': 'richard morse comparison with article'
	},
    {
		'input': 'richard s lawrence;richard s. lawrence', 
		'expected': True, 
		'description': 'richard s lawrence comparison with article'
	},
    {
		'input': 'richard t deters;richard t. deters', 
		'expected': True, 
		'description': 'richard t deters comparison with article'
	},
    {
		'input': 'richard van cleve;richard van cleve', 
		'expected': True, 
		'description': 'richard van cleve comparison with article'
	},
    {
		'input': 'richard w deeds;richard w. deeds', 
		'expected': True, 
		'description': 'richard w deeds comparison with article'
	},
    {
		'input': 'richard w laird;richard willoughby laird', 
		'expected': True, 
		'description': 'richard w laird comparison with article'
	},
    {
		'input': 'richard w leopold;richard william leopold', 
		'expected': True, 
		'description': 'richard w leopold comparison with article'
	},
    {
		'input': 'robert a hicks;robert lansing hicks', 
		'expected': False, 
		'description': 'robert a hicks comparison with article'
	},
    {
		'input': 'robert a law;robert adger law', 
		'expected': True, 
		'description': 'robert a law comparison with article'
	},
    {
		'input': 'robert b berg;robert leonard berg', 
		'expected': False, 
		'description': 'robert b berg comparison with article'
	},
    {
		'input': 'robert b deering;robert b. deering', 
		'expected': True, 
		'description': 'robert b deering comparison with article'
	},
    {
		'input': 'robert b lane;robert philips lane', 
		'expected': False, 
		'description': 'robert b lane comparison with article'
	},
    {
		'input': 'robert b leighton;robert b. leighton', 
		'expected': True, 
		'description': 'robert b leighton comparison with article'
	},
    {
		'input': 'robert b lewis;robert burns lewis', 
		'expected': True, 
		'description': 'robert b lewis comparison with article'
	},
    {
		'input': 'robert d lane;robert edwin lane', 
		'expected': False, 
		'description': 'robert d lane comparison with article'
	},
    {
		'input': 'robert d lang;daniel robert lang', 
		'expected': True, 
		'description': 'robert d lang comparison with article'
	},
    {
		'input': 'robert d leigh;robert d. leigh', 
		'expected': True, 
		'description': 'robert d leigh comparison with article'
	},
    {
		'input': 'robert d leiter;robert leiter', 
		'expected': True, 
		'description': 'robert d leiter comparison with article'
	},
    {
		'input': 'robert d lewis;thomas robert lewis', 
		'expected': False, 
		'description': 'robert d lewis comparison with article'
	},
    {
		'input': 'robert d rhynes;robert van reen', 
		'expected': False, 
		'description': 'robert d rhynes comparison with article'
	},
    {
		'input': 'robert de revere;robert e. derevere', 
		'expected': True, 
		'description': 'robert de revere comparison with article'
	},
    {
		'input': 'robert denny;robert frank denny', 
		'expected': True, 
		'description': 'robert denny comparison with article'
	},
    {
		'input': 'robert denton;robert claude dentan', 
		'expected': True, 
		'description': 'robert denton comparison with article'
	},
    {
		'input': 'robert deupree;robt. g. deupree', 
		'expected': True, 
		'description': 'robert deupree comparison with article'
	},
    {
		'input': 'robert e dengler;robert e. dengler', 
		'expected': True, 
		'description': 'robert e dengler comparison with article'
	},
    {
		'input': 'robert e dewey;robert e. dewey', 
		'expected': True, 
		'description': 'robert e dewey comparison with article'
	},
    {
		'input': 'robert e glass;robert lee glass', 
		'expected': False, 
		'description': 'robert e glass comparison with article'
	},
    {
		'input': 'robert e l faris;robert e. lee faris', 
		'expected': True, 
		'description': 'robert e l faris comparison with article'
	},
    {
		'input': 'robert e l strider;robert edward lee strider', 
		'expected': True, 
		'description': 'robert e l strider comparison with article'
	},
    {
		'input': 'robert e ladd;dwight robert ladd', 
		'expected': False, 
		'description': 'robert e ladd comparison with article'
	},
    {
		'input': 'robert e lake;robert e. lake', 
		'expected': True, 
		'description': 'robert e lake comparison with article'
	},
    {
		'input': 'robert e lane;robert edwards lane', 
		'expected': True, 
		'description': 'robert e lane comparison with article'
	},
    {
		'input': 'robert e larson;robert earl larson', 
		'expected': True, 
		'description': 'robert e larson comparison with article'
	},
    {
		'input': 'robert e lee;robert edwin lee', 
		'expected': True, 
		'description': 'robert e lee comparison with article'
	},
    {
		'input': 'robert f deegan;robert f. degen', 
		'expected': True, 
		'description': 'robert f deegan comparison with article'
	},
    {
		'input': 'robert f lawson;robert f. lawson', 
		'expected': True, 
		'description': 'robert f lawson comparison with article'
	},
    {
		'input': 'robert f lent;robert f. lent', 
		'expected': True, 
		'description': 'robert f lent comparison with article'
	},
    {
		'input': 'robert faulkner;robert lee faulkner', 
		'expected': True, 
		'description': 'robert faulkner comparison with article'
	},
    {
		'input': 'robert g legge;robert t. legge', 
		'expected': False, 
		'description': 'robert g legge comparison with article'
	},
    {
		'input': 'robert g miller;robert lavelle miller', 
		'expected': False, 
		'description': 'robert g miller comparison with article'
	},
    {
		'input': 'robert h lee, jr;robert h. lee', 
		'expected': True, 
		'description': 'robert h lee, jr comparison with article'
	},
    {
		'input': 'robert haun;robert dee haun', 
		'expected': True, 
		'description': 'robert haun comparison with article'
	},
    {
		'input': 'robert hay;robert dean hay', 
		'expected': True, 
		'description': 'robert hay comparison with article'
	},
    {
		'input': 'robert j lampman;robert james lampman', 
		'expected': True, 
		'description': 'robert j lampman comparison with article'
	},
    {
		'input': 'robert j leblanc;robert j. leblanc', 
		'expected': True, 
		'description': 'robert j leblanc comparison with article'
	},
    {
		'input': 'robert l briggs;robert leroy briggs', 
		'expected': True, 
		'description': 'robert l briggs comparison with article'
	},
    {
		'input': 'robert l clayton;robert lee clayton', 
		'expected': True, 
		'description': 'robert l clayton comparison with article'
	},
    {
		'input': 'robert l cooper;l. leola cooper', 
		'expected': False, 
		'description': 'robert l cooper comparison with article'
	},
    {
		'input': 'robert l dillon;theodore robert van dellen', 
		'expected': False, 
		'description': 'robert l dillon comparison with article'
	},
    {
		'input': 'robert l easton;robert lavern easton', 
		'expected': True, 
		'description': 'robert l easton comparison with article'
	},
    {
		'input': 'robert l fernald;robert leslie fernald', 
		'expected': True, 
		'description': 'robert l fernald comparison with article'
	},
    {
		'input': 'robert l grilley;robert leroy grilley', 
		'expected': True, 
		'description': 'robert l grilley comparison with article'
	},
    {
		'input': 'robert l jackson;robert lawrence jackson', 
		'expected': True, 
		'description': 'robert l jackson comparison with article'
	},
    {
		'input': 'robert l jeske;robert leroy jeske', 
		'expected': True, 
		'description': 'robert l jeske comparison with article'
	},
    {
		'input': 'robert l king;robert leslie king', 
		'expected': True, 
		'description': 'robert l king comparison with article'
	},
    {
		'input': 'robert l koehl;robert lewis koehl', 
		'expected': True, 
		'description': 'robert l koehl comparison with article'
	},
    {
		'input': 'robert l lam;robert lam', 
		'expected': True, 
		'description': 'robert l lam comparison with article'
	},
    {
		'input': 'robert l lepper;robert l. lepper', 
		'expected': True, 
		'description': 'robert l lepper comparison with article'
	},
    {
		'input': 'robert l letsinger;robert lewis letsinger', 
		'expected': True, 
		'description': 'robert l letsinger comparison with article'
	},
    {
		'input': 'robert l levy;robert l. levy', 
		'expected': True, 
		'description': 'robert l levy comparison with article'
	},
    {
		'input': 'robert l mckee;robert lambert mckee', 
		'expected': True, 
		'description': 'robert l mckee comparison with article'
	},
    {
		'input': 'robert l meirweather;robert lee meriwether', 
		'expected': True, 
		'description': 'robert l meirweather comparison with article'
	},
    {
		'input': 'robert l newell;robert lee newell', 
		'expected': True, 
		'description': 'robert l newell comparison with article'
	},
    {
		'input': 'robert l noell;robert leonard noell', 
		'expected': True, 
		'description': 'robert l noell comparison with article'
	},
    {
		'input': 'robert l patterson;robert leet patterson', 
		'expected': True, 
		'description': 'robert l patterson comparison with article'
	},
    {
		'input': 'robert l pigford;robert lamar pigford', 
		'expected': True, 
		'description': 'robert l pigford comparison with article'
	},
    {
		'input': 'robert l proffer;robert lee proffer', 
		'expected': True, 
		'description': 'robert l proffer comparison with article'
	},
    {
		'input': 'robert l reynolds;robert leonard reynolds', 
		'expected': True, 
		'description': 'robert l reynolds comparison with article'
	},
    {
		'input': 'robert l sharp;robert lathrop sharp', 
		'expected': True, 
		'description': 'robert l sharp comparison with article'
	},
    {
		'input': 'robert l smith, sr;robert lewis smith', 
		'expected': True, 
		'description': 'robert l smith, sr comparison with article'
	},
    {
		'input': 'robert l thurman;robert lee thurman', 
		'expected': True, 
		'description': 'robert l thurman comparison with article'
	},
    {
		'input': 'robert l tugwell;robert lee tugwell', 
		'expected': True, 
		'description': 'robert l tugwell comparison with article'
	},
    {
		'input': 'robert l vandoren;robert lawson van doren', 
		'expected': True, 
		'description': 'robert l vandoren comparison with article'
	},
    {
		'input': 'robert l vanhorne;robert loren van horne', 
		'expected': True, 
		'description': 'robert l vanhorne comparison with article'
	},
    {
		'input': 'robert l wiggins;robert lemuel wiggins', 
		'expected': True, 
		'description': 'robert l wiggins comparison with article'
	},
    {
		'input': 'robert l wolff;robert lee wolff', 
		'expected': True, 
		'description': 'robert l wolff comparison with article'
	},
    {
		'input': 'robert l. leathers;robert l. leathers', 
		'expected': True, 
		'description': 'robert l. leathers comparison with article'
	},
    {
		'input': 'robert lafollette;robert lafollette', 
		'expected': True, 
		'description': 'robert lafollette comparison with article'
	},
    {
		'input': 'robert lancaster;robert samuel lancaster', 
		'expected': True, 
		'description': 'robert lancaster comparison with article'
	},
    {
		'input': 'robert lang;robert lang', 
		'expected': True, 
		'description': 'robert lang comparison with article'
	},
    {
		'input': 'robert lanni;robert patrick lanni', 
		'expected': True, 
		'description': 'robert lanni comparison with article'
	},
    {
		'input': 'robert lanzillotti;robert lanzillotti', 
		'expected': True, 
		'description': 'robert lanzillotti comparison with article'
	},
    {
		'input': 'robert lee christian;robert christian', 
		'expected': True, 
		'description': 'robert lee christian comparison with article'
	},
    {
		'input': 'robert lee hunter;francis robert hunter', 
		'expected': False, 
		'description': 'robert lee hunter comparison with article'
	},
    {
		'input': 'robert lekachman;robert lekachman', 
		'expected': True, 
		'description': 'robert lekachman comparison with article'
	},
    {
		'input': 'robert leon white;robert leon white', 
		'expected': True, 
		'description': 'robert leon white comparison with article'
	},
    {
		'input': 'robert lepper;robert lepper', 
		'expected': True, 
		'description': 'robert lepper comparison with article'
	},
    {
		'input': 'robert lew;robert louise', 
		'expected': True, 
		'description': 'robert lew comparison with article'
	},
    {
		'input': 'robert m delaney;robert mills delaney', 
		'expected': True, 
		'description': 'robert m delaney comparison with article'
	},
    {
		'input': 'robert m la forge;robert mallory laforge', 
		'expected': True, 
		'description': 'robert m la forge comparison with article'
	},
    {
		'input': 'robert m lewert;robert murdoch lewert', 
		'expected': True, 
		'description': 'robert m lewert comparison with article'
	},
    {
		'input': 'robert miller;robert demorest miller', 
		'expected': True, 
		'description': 'robert miller comparison with article'
	},
    {
		'input': 'robert n lass;robert n. lass', 
		'expected': True, 
		'description': 'robert n lass comparison with article'
	},
    {
		'input': 'robert r leidy;raimundo lida', 
		'expected': False, 
		'description': 'robert r leidy comparison with article'
	},
    {
		'input': 'robert s landauer;robert s. landauer', 
		'expected': True, 
		'description': 'robert s landauer comparison with article'
	},
    {
		'input': 'robert s lewis;robert s. lewis', 
		'expected': True, 
		'description': 'robert s lewis comparison with article'
	},
    {
		'input': 'robert v finney;robert vansant finney', 
		'expected': True, 
		'description': 'robert v finney comparison with article'
	},
    {
		'input': 'robert v longmuir;robert v. langmuir', 
		'expected': True, 
		'description': 'robert v longmuir comparison with article'
	},
    {
		'input': 'robert van de graaff;robert jemison van de graaff', 
		'expected': True, 
		'description': 'robert van de graaff comparison with article'
	},
    {
		'input': 'robert van horn;robert bowman van horn', 
		'expected': True, 
		'description': 'robert van horn comparison with article'
	},
    {
		'input': 'robert von nardroff;robert von nardroff', 
		'expected': True, 
		'description': 'robert von nardroff comparison with article'
	},
    {
		'input': 'robert w dean;w. c. dean', 
		'expected': False, 
		'description': 'robert w dean comparison with article'
	},
    {
		'input': 'robert w desmond;robert w. desmond', 
		'expected': True, 
		'description': 'robert w desmond comparison with article'
	},
    {
		'input': 'robert w doisher;robert w. deisher', 
		'expected': True, 
		'description': 'robert w doisher comparison with article'
	},
    {
		'input': 'robert w houghton;robert w. van houten', 
		'expected': True, 
		'description': 'robert w houghton comparison with article'
	},
    {
		'input': 'robert w leonard;robert w. leonard', 
		'expected': True, 
		'description': 'robert w leonard comparison with article'
	},
    {
		'input': 'robert whitman;robert van duyne whitman', 
		'expected': True, 
		'description': 'robert whitman comparison with article'
	},
    {
		'input': 'roberta d ortenburger;roberta deam ortenburger', 
		'expected': True, 
		'description': 'roberta d ortenburger comparison with article'
	},
    {
		'input': 'roberta m law;roberta law', 
		'expected': True, 
		'description': 'roberta m law comparison with article'
	},
    {
		'input': 'robt l burwell, jr;robert lemmon burwell', 
		'expected': True, 
		'description': 'robt l burwell, jr comparison with article'
	},
    {
		'input': 'robt l goulding;robert lee goulding', 
		'expected': True, 
		'description': 'robt l goulding comparison with article'
	},
    {
		'input': 'roderick d gordon;roderick dean gordon', 
		'expected': True, 
		'description': 'roderick d gordon comparison with article'
	},
    {
		'input': 'roger c. larson;roger c. larson', 
		'expected': True, 
		'description': 'roger c. larson comparison with article'
	},
    {
		'input': 'roger l lawrence;roger l. lawrence', 
		'expected': True, 
		'description': 'roger l lawrence comparison with article'
	},
    {
		'input': 'roger l williams;roger lawrence williams', 
		'expected': True, 
		'description': 'roger l williams comparison with article'
	},
    {
		'input': 'roland l kramer;roland laird kramer', 
		'expected': True, 
		'description': 'roland l kramer comparison with article'
	},
    {
		'input': 'roland v rider;rowland vance rider', 
		'expected': True, 
		'description': 'roland v rider comparison with article'
	},
    {
		'input': 'roman s ladewski;roman s. ladewski', 
		'expected': True, 
		'description': 'roman s ladewski comparison with article'
	},
    {
		'input': 'ronald a lanor;a. a. lenior', 
		'expected': False, 
		'description': 'ronald a lanor comparison with article'
	},
    {
		'input': 'ronald b levinson;ronald b. levinson', 
		'expected': True, 
		'description': 'ronald b levinson comparison with article'
	},
    {
		'input': 'ronald k de ford;ronald k. deford', 
		'expected': True, 
		'description': 'ronald k de ford comparison with article'
	},
    {
		'input': 'ronnald g le sage;romuald g. lesage', 
		'expected': True, 
		'description': 'ronnald g le sage comparison with article'
	},
    {
		'input': 'rosa lee andrews;mary lee andrews', 
		'expected': False, 
		'description': 'rosa lee andrews comparison with article'
	},
    {
		'input': 'rosalie wessel;rosa lee wessel', 
		'expected': True, 
		'description': 'rosalie wessel comparison with article'
	},
    {
		'input': 'rosalind s langsam;rosalind streep langsam', 
		'expected': True, 
		'description': 'rosalind s langsam comparison with article'
	},
    {
		'input': 'roscoe d leas;roscoe david leas', 
		'expected': True, 
		'description': 'roscoe d leas comparison with article'
	},
    {
		'input': 'rose c mooney;rose ledieu mooney', 
		'expected': False, 
		'description': 'rose c mooney comparison with article'
	},
    {
		'input': 'rose hum lee;rose hum lee', 
		'expected': True, 
		'description': 'rose hum lee comparison with article'
	},
    {
		'input': 'rose lamme;rose lamme', 
		'expected': True, 
		'description': 'rose lamme comparison with article'
	},
    {
		'input': 'rose leske;rose katherine leske', 
		'expected': True, 
		'description': 'rose leske comparison with article'
	},
    {
		'input': 'rose lisenby;rose lee lisenby', 
		'expected': True, 
		'description': 'rose lisenby comparison with article'
	},
    {
		'input': 'rowland w leiby;rowland willis leiby', 
		'expected': True, 
		'description': 'rowland w leiby comparison with article'
	},
    {
		'input': 'roy c langford;roy clinton langford', 
		'expected': True, 
		'description': 'roy c langford comparison with article'
	},
    {
		'input': 'roy d sheffield;roy dexter sheffieid', 
		'expected': True, 
		'description': 'roy d sheffield comparison with article'
	},
    {
		'input': 'roy h lanphear;roy higinbotham lanphear', 
		'expected': True, 
		'description': 'roy h lanphear comparison with article'
	},
    {
		'input': 'roy s dearstyne;roy styring dearstyne', 
		'expected': True, 
		'description': 'roy s dearstyne comparison with article'
	},
    {
		'input': 'roy s jensen;mead leroy jensen', 
		'expected': False, 
		'description': 'roy s jensen comparison with article'
	},
    {
		'input': 'roy v lalmage;roy van neste talmage', 
		'expected': True, 
		'description': 'roy v lalmage comparison with article'
	},
    {
		'input': 'ruby l valz;l. r. la valle', 
		'expected': False, 
		'description': 'ruby l valz comparison with article'
	},
    {
		'input': 'rudolph e langer;rudolph ernest langer', 
		'expected': True, 
		'description': 'rudolph e langer comparison with article'
	},
    {
		'input': 'rudolph l biesele;rudolph leopold biesele', 
		'expected': True, 
		'description': 'rudolph l biesele comparison with article'
	},
    {
		'input': 'rupert b vance;rupert bayless vance', 
		'expected': True, 
		'description': 'rupert b vance comparison with article'
	},
    {
		'input': 'russel laman;russell laman', 
		'expected': True, 
		'description': 'russel laman comparison with article'
	},
    {
		'input': 'russell a lecronier;a. russell lecronier', 
		'expected': True, 
		'description': 'russell a lecronier comparison with article'
	},
    {
		'input': 'russell d dement;r. d. dement', 
		'expected': True, 
		'description': 'russell d dement comparison with article'
	},
    {
		'input': 'russell d snyder;russell dewey snyder', 
		'expected': True, 
		'description': 'russell d snyder comparison with article'
	},
    {
		'input': 'russell e kittnell;joseph e. von kaenel', 
		'expected': False, 
		'description': 'russell e kittnell comparison with article'
	},
    {
		'input': 'russell e larson;russell e. larson', 
		'expected': True, 
		'description': 'russell e larson comparison with article'
	},
    {
		'input': 'russell h larson;russell harold larson', 
		'expected': True, 
		'description': 'russell h larson comparison with article'
	},
    {
		'input': 'russell l dicks;russell leslie dicks', 
		'expected': True, 
		'description': 'russell l dicks comparison with article'
	},
    {
		'input': 'russell r de alvarez;russell r. de alvarez', 
		'expected': True, 
		'description': 'russell r de alvarez comparison with article'
	},
    {
		'input': 'russell r larmon;russell raymond larmon', 
		'expected': True, 
		'description': 'russell r larmon comparison with article'
	},
    {
		'input': 'ruth b langford;ruth betty langford', 
		'expected': True, 
		'description': 'ruth b langford comparison with article'
	},
    {
		'input': 'ruth b leedy;ruth berg leedy', 
		'expected': True, 
		'description': 'ruth b leedy comparison with article'
	},
    {
		'input': 'ruth deacon;ruth e. deacon', 
		'expected': True, 
		'description': 'ruth deacon comparison with article'
	},
    {
		'input': 'ruth dean;ruth josephine dean', 
		'expected': True, 
		'description': 'ruth dean comparison with article'
	},
    {
		'input': 'ruth lee kennedy;ruth lee kennedy', 
		'expected': True, 
		'description': 'ruth lee kennedy comparison with article'
	},
    {
		'input': 'ruth leonard;ruth shaw leonard', 
		'expected': True, 
		'description': 'ruth leonard comparison with article'
	},
    {
		'input': 'ruth m lambertus;ruth m. lambertus', 
		'expected': True, 
		'description': 'ruth m lambertus comparison with article'
	},
    {
		'input': 'ruth m lampson;ruth murdock lampson', 
		'expected': True, 
		'description': 'ruth m lampson comparison with article'
	},
    {
		'input': 'ruth n denny;reuel n. denney', 
		'expected': False, 
		'description': 'ruth n denny comparison with article'
	},
    {
		'input': 'ruth r dismang;winston r. de monsabert', 
		'expected': False, 
		'description': 'ruth r dismang comparison with article'
	},
    {
		'input': 'ruth r leitch;ruth redding leitch', 
		'expected': True, 
		'description': 'ruth r leitch comparison with article'
	},
    {
		'input': 'ruth s lamb;ruth stanton lamb', 
		'expected': True, 
		'description': 'ruth s lamb comparison with article'
	},
    {
		'input': 'ruth s lerner;ruth spero lerner', 
		'expected': True, 
		'description': 'ruth s lerner comparison with article'
	},
    {
		'input': 'ruth t. lehman;ruth t. lehman', 
		'expected': True, 
		'description': 'ruth t. lehman comparison with article'
	},
    {
		'input': 's arthur lake;w. s. lake', 
		'expected': False, 
		'description': 's arthur lake comparison with article'
	},
    {
		'input': 's le roy brown;simpson leroy brown', 
		'expected': True, 
		'description': 's le roy brown comparison with article'
	},
    {
		'input': 's lewis drake;louis s. drake', 
		'expected': True, 
		'description': 's lewis drake comparison with article'
	},
    {
		'input': 'salvatore devita;salvatore devita', 
		'expected': True, 
		'description': 'salvatore devita comparison with article'
	},
    {
		'input': 'sam c dellinger;samuel claudius dellinger', 
		'expected': True, 
		'description': 'sam c dellinger comparison with article'
	},
    {
		'input': 'sam legvold;sam legvold', 
		'expected': True, 
		'description': 'sam legvold comparison with article'
	},
    {
		'input': 'sam leifeste;sam a. d. leifeste', 
		'expected': True, 
		'description': 'sam leifeste comparison with article'
	},
    {
		'input': 'samuel a lear;samuel a. lear', 
		'expected': True, 
		'description': 'samuel a lear comparison with article'
	},
    {
		'input': 'samuel a levinson;samuel azor levinson', 
		'expected': True, 
		'description': 'samuel a levinson comparison with article'
	},
    {
		'input': 'samuel d atkins;samuel decoster atkins', 
		'expected': True, 
		'description': 'samuel d atkins comparison with article'
	},
    {
		'input': 'samuel d zelden;samuel demitry zeldin', 
		'expected': True, 
		'description': 'samuel d zelden comparison with article'
	},
    {
		'input': 'samuel detwiler;samuel r. detwiler', 
		'expected': True, 
		'description': 'samuel detwiler comparison with article'
	},
    {
		'input': 'samuel j jr lang;samuel j. lang', 
		'expected': True, 
		'description': 'samuel j jr lang comparison with article'
	},
    {
		'input': 'samuel l gargill;samuel leon gargill', 
		'expected': True, 
		'description': 'samuel l gargill comparison with article'
	},
    {
		'input': 'samuel l greenwood;sam lee greenwood', 
		'expected': True, 
		'description': 'samuel l greenwood comparison with article'
	},
    {
		'input': 'samuel l leonard;samuel leeson leonard', 
		'expected': True, 
		'description': 'samuel l leonard comparison with article'
	},
    {
		'input': 'samuel l prince;samuel lander prince', 
		'expected': True, 
		'description': 'samuel l prince comparison with article'
	},
    {
		'input': 'samuel lang;samuel lang', 
		'expected': True, 
		'description': 'samuel lang comparison with article'
	},
    {
		'input': 'samuel leger;samuel h. leger', 
		'expected': True, 
		'description': 'samuel leger comparison with article'
	},
    {
		'input': 'samuel lehman;samuel george lehman', 
		'expected': True, 
		'description': 'samuel lehman comparison with article'
	},
    {
		'input': 'samuel lerner;samuel lerner', 
		'expected': True, 
		'description': 'samuel lerner comparison with article'
	},
    {
		'input': 'samuel m derrick;samuel melanchthon derrick', 
		'expected': True, 
		'description': 'samuel m derrick comparison with article'
	},
    {
		'input': 'samuel m levin;samuel m. levin', 
		'expected': True, 
		'description': 'samuel m levin comparison with article'
	},
    {
		'input': 'samuel van valkenburg;samuel van valkenburg', 
		'expected': True, 
		'description': 'samuel van valkenburg comparison with article'
	},
    {
		'input': 'sandra lee wray;alexius taikyue ree', 
		'expected': False, 
		'description': 'sandra lee wray comparison with article'
	},
    {
		'input': 'sandra lehrman;alexander lehrman', 
		'expected': False, 
		'description': 'sandra lehrman comparison with article'
	},
    {
		'input': 'sanford e leeds;sanford e. leeds', 
		'expected': True, 
		'description': 'sanford e leeds comparison with article'
	},
    {
		'input': 'sara a deford;sara deford', 
		'expected': True, 
		'description': 'sara a deford comparison with article'
	},
    {
		'input': 'sara e burnham;ebert van buren', 
		'expected': False, 
		'description': 'sara e burnham comparison with article'
	},
    {
		'input': 'sarah denett holmes;sarah bennett holmes', 
		'expected': True, 
		'description': 'sarah denett holmes comparison with article'
	},
    {
		'input': 'sarah m vancil;sarah may vancil', 
		'expected': True, 
		'description': 'sarah m vancil comparison with article'
	},
    {
		'input': 'saul levy;saul levy', 
		'expected': True, 
		'description': 'saul levy comparison with article'
	},
    {
		'input': 'saunders mac lane;saunders mac lane', 
		'expected': True, 
		'description': 'saunders mac lane comparison with article'
	},
    {
		'input': 'sergio debenedetti;sergio de benedetti', 
		'expected': True, 
		'description': 'sergio debenedetti comparison with article'
	},
    {
		'input': 'sharley b demotte;sharley b. demotte', 
		'expected': True, 
		'description': 'sharley b demotte comparison with article'
	},
    {
		'input': 'shelby d gerking, jr;shelby delos gerking', 
		'expected': True, 
		'description': 'shelby d gerking, jr comparison with article'
	},
    {
		'input': 'sherman p lawton;sherman paxton lawton', 
		'expected': True, 
		'description': 'sherman p lawton comparison with article'
	},
    {
		'input': 'sidney lees;sidney lees', 
		'expected': True, 
		'description': 'sidney lees comparison with article'
	},
    {
		'input': 'sigmund w leifson;sigmund w. leifson', 
		'expected': True, 
		'description': 'sigmund w leifson comparison with article'
	},
    {
		'input': 'signe larsen;esper signius larsen', 
		'expected': True, 
		'description': 'signe larsen comparison with article'
	},
    {
		'input': 'silvere c. vandecaveye;s. c. vandecaveye', 
		'expected': True, 
		'description': 'silvere c. vandecaveye comparison with article'
	},
    {
		'input': 'simeon e leland;simeon elbridge leland', 
		'expected': True, 
		'description': 'simeon e leland comparison with article'
	},
    {
		'input': 'simon leopold;simon stein leopold', 
		'expected': True, 
		'description': 'simon leopold comparison with article'
	},
    {
		'input': 'sister mary john leo;mary john', 
		'expected': True, 
		'description': 'sister mary john leo comparison with article'
	},
    {
		'input': 'sol levin;saul levin', 
		'expected': True, 
		'description': 'sol levin comparison with article'
	},
    {
		'input': 'solomon leider;solomon leader', 
		'expected': True, 
		'description': 'solomon leider comparison with article'
	},
    {
		'input': 'sophia mcdonald;sophia levy mcdonald', 
		'expected': True, 
		'description': 'sophia mcdonald comparison with article'
	},
    {
		'input': 'stanley a leavy;stanley arnold leavy', 
		'expected': True, 
		'description': 'stanley a leavy comparison with article'
	},
    {
		'input': 'stanley lamm;stanley s. lamm', 
		'expected': True, 
		'description': 'stanley lamm comparison with article'
	},
    {
		'input': 'stanley lesser;stanley r. lesser', 
		'expected': True, 
		'description': 'stanley lesser comparison with article'
	},
    {
		'input': 'stella l lamond;stella lodge lamond', 
		'expected': True, 
		'description': 'stella l lamond comparison with article'
	},
    {
		'input': 'stella l lange;stella lange', 
		'expected': True, 
		'description': 'stella l lange comparison with article'
	},
    {
		'input': 'stephen dean, iii;stephen j. dean', 
		'expected': True, 
		'description': 'stephen dean, iii comparison with article'
	},
    {
		'input': 'stewart l garrison;stewart lee garrison', 
		'expected': True, 
		'description': 'stewart l garrison comparison with article'
	},
    {
		'input': 'stewart s dallyn;stewart lamonte dallyn', 
		'expected': False, 
		'description': 'stewart s dallyn comparison with article'
	},
    {
		'input': 'stuart b le compte;stuart b. lecompte', 
		'expected': True, 
		'description': 'stuart b le compte comparison with article'
	},
    {
		'input': 'susan d dees;susan coons dees', 
		'expected': False, 
		'description': 'susan d dees comparison with article'
	},
    {
		'input': 'suzanne lasater;suzanne margot lasater', 
		'expected': True, 
		'description': 'suzanne lasater comparison with article'
	},
    {
		'input': 't l sharfman;isaiah leo sharfman', 
		'expected': False, 
		'description': 't l sharfman comparison with article'
	},
    {
		'input': 't. dewitt carr;t. dewitt carr', 
		'expected': True, 
		'description': 't. dewitt carr comparison with article'
	},
    {
		'input': 't. lawerence foran;t. lawrence foran', 
		'expected': True, 
		'description': 't. lawerence foran comparison with article'
	},
    {
		'input': 'talmadge l peele;talmadge lee peele', 
		'expected': True, 
		'description': 'talmadge l peele comparison with article'
	},
    {
		'input': 'tella marie debose;tella marie debose', 
		'expected': True, 
		'description': 'tella marie debose comparison with article'
	},
    {
		'input': 'thelma lavine;thelma z. lavine', 
		'expected': True, 
		'description': 'thelma lavine comparison with article'
	},
    {
		'input': 'theodore a lams;theodore a. lams', 
		'expected': True, 
		'description': 'theodore a lams comparison with article'
	},
    {
		'input': 'theodore b ley;theodore de lay', 
		'expected': True, 
		'description': 'theodore b ley comparison with article'
	},
    {
		'input': 'theodore b ley;theodore s. de lay', 
		'expected': False, 
		'description': 'theodore b ley comparison with article'
	},
    {
		'input': 'theodore bakermann;theodore von karman', 
		'expected': False, 
		'description': 'theodore bakermann comparison with article'
	},
    {
		'input': 'theodore harris;theodore lester harris', 
		'expected': True, 
		'description': 'theodore harris comparison with article'
	},
    {
		'input': 'theodore l dehne;theodore l. dehne', 
		'expected': True, 
		'description': 'theodore l dehne comparison with article'
	},
    {
		'input': 'theodore lang;theodore lang', 
		'expected': True, 
		'description': 'theodore lang comparison with article'
	},
    {
		'input': 'theodore paul phillips;theodore dewitt phillips', 
		'expected': False, 
		'description': 'theodore paul phillips comparison with article'
	},
    {
		'input': 'theodore storch;theodore j. c. von storch', 
		'expected': True, 
		'description': 'theodore storch comparison with article'
	},
    {
		'input': 'theodore t lafferty, sr;theodore t. lafferty', 
		'expected': True, 
		'description': 'theodore t lafferty, sr comparison with article'
	},
    {
		'input': 'theordore l reller;theodore lee reller', 
		'expected': True, 
		'description': 'theordore l reller comparison with article'
	},
    {
		'input': 'thomas a leonard;a. orin leonard', 
		'expected': False, 
		'description': 'thomas a leonard comparison with article'
	},
    {
		'input': 'thomas a. dent;thomas johnstone dent', 
		'expected': False, 
		'description': 'thomas a. dent comparison with article'
	},
    {
		'input': 'thomas c deane;c. thomas dean', 
		'expected': True, 
		'description': 'thomas c deane comparison with article'
	},
    {
		'input': 'thomas c laipply;thomas charles laipply', 
		'expected': True, 
		'description': 'thomas c laipply comparison with article'
	},
    {
		'input': 'thomas c van cleve;thomas curtis van cleve', 
		'expected': True, 
		'description': 'thomas c van cleve comparison with article'
	},
    {
		'input': 'thomas demott;thomas demott', 
		'expected': True, 
		'description': 'thomas demott comparison with article'
	},
    {
		'input': 'thomas devries;thomas de vries', 
		'expected': True, 
		'description': 'thomas devries comparison with article'
	},
    {
		'input': 'thomas e lasswell;thomas e. lasswell', 
		'expected': True, 
		'description': 'thomas e lasswell comparison with article'
	},
    {
		'input': 'thomas f debnam;thomas finley debnam', 
		'expected': True, 
		'description': 'thomas f debnam comparison with article'
	},
    {
		'input': 'thomas h lanman;thomas hinckley lanman', 
		'expected': True, 
		'description': 'thomas h lanman comparison with article'
	},
    {
		'input': 'thomas h le duc;thomas harold leduc', 
		'expected': True, 
		'description': 'thomas h le duc comparison with article'
	},
    {
		'input': 'thomas l leach;thomas luther leach', 
		'expected': True, 
		'description': 'thomas l leach comparison with article'
	},
    {
		'input': 'thomas l quay;thomas lavelle quay', 
		'expected': True, 
		'description': 'thomas l quay comparison with article'
	},
    {
		'input': 'thomas l savage;thomas laman savage', 
		'expected': True, 
		'description': 'thomas l savage comparison with article'
	},
    {
		'input': 'thomas l wade, jr;thomas leonard wade', 
		'expected': True, 
		'description': 'thomas l wade, jr comparison with article'
	},
    {
		'input': 'thomas l wilson;thomas leslie wilson', 
		'expected': True, 
		'description': 'thomas l wilson comparison with article'
	},
    {
		'input': 'thomas l york;thomas lenoir york', 
		'expected': True, 
		'description': 'thomas l york comparison with article'
	},
    {
		'input': 'thomas la saine;thomas a. lasaine', 
		'expected': True, 
		'description': 'thomas la saine comparison with article'
	},
    {
		'input': 'thomas lauritsen;thomas lauritsen', 
		'expected': True, 
		'description': 'thomas lauritsen comparison with article'
	},
    {
		'input': 'thomas lee bahler;thomas l. bahler', 
		'expected': True, 
		'description': 'thomas lee bahler comparison with article'
	},
    {
		'input': 'thomas n lewis, n;thomas mcdowell nelson lewis', 
		'expected': True, 
		'description': 'thomas n lewis, n comparison with article'
	},
    {
		'input': 'thomas o martin;thomas leroy martin', 
		'expected': False, 
		'description': 'thomas o martin comparison with article'
	},
    {
		'input': 'thomas r kinney;thomas dearman kinney', 
		'expected': False, 
		'description': 'thomas r kinney comparison with article'
	},
    {
		'input': 'thomas s lee;thomas seymour lee', 
		'expected': True, 
		'description': 'thomas s lee comparison with article'
	},
    {
		'input': 'thomas s leith;thomas seeter leith', 
		'expected': True, 
		'description': 'thomas s leith comparison with article'
	},
    {
		'input': 'thomas van voorhis;thomas p. van voorhis', 
		'expected': True, 
		'description': 'thomas van voorhis comparison with article'
	},
    {
		'input': 'thomas vance;thomas franklin vance', 
		'expected': True, 
		'description': 'thomas vance comparison with article'
	},
    {
		'input': 'thomas vance;thomas hume vance', 
		'expected': True, 
		'description': 'thomas vance comparison with article'
	},
    {
		'input': 'thomas w lambe;thomas william lambe', 
		'expected': True, 
		'description': 'thomas w lambe comparison with article'
	},
    {
		'input': 'thomas w lester;thomas william lester', 
		'expected': True, 
		'description': 'thomas w lester comparison with article'
	},
    {
		'input': 'thorstin larsen;thornstein larsen', 
		'expected': True, 
		'description': 'thorstin larsen comparison with article'
	},
    {
		'input': 'thurman w van meter;thurman w. van metre', 
		'expected': True, 
		'description': 'thurman w van meter comparison with article'
	},
    {
		'input': 'timothy f oleary;timothy f. leary', 
		'expected': True, 
		'description': 'timothy f oleary comparison with article'
	},
    {
		'input': 'tom f lewis;tom f. lewis', 
		'expected': True, 
		'description': 'tom f lewis comparison with article'
	},
    {
		'input': 'tourgee debose;tourgee a. debose', 
		'expected': True, 
		'description': 'tourgee debose comparison with article'
	},
    {
		'input': 'tylene e dunning;e. leon dunning', 
		'expected': False, 
		'description': 'tylene e dunning comparison with article'
	},
    {
		'input': 'ulysses s vance;ulysses vance', 
		'expected': True, 
		'description': 'ulysses s vance comparison with article'
	},
    {
		'input': 'una l robinson;una lane robinson', 
		'expected': True, 
		'description': 'una l robinson comparison with article'
	},
    {
		'input': 'v lewis bassie;v. lewis bassie', 
		'expected': True, 
		'description': 'v lewis bassie comparison with article'
	},
    {
		'input': 'valentine listard pinacoli;valentine leotard pinacoli', 
		'expected': True, 
		'description': 'valentine listard pinacoli comparison with article'
	},
    {
		'input': 'van d smith;samuel van dyke smith', 
		'expected': True, 
		'description': 'van d smith comparison with article'
	},
    {
		'input': 'van d thompson;van denman thompson', 
		'expected': True, 
		'description': 'van d thompson comparison with article'
	},
    {
		'input': 'van derek frechette;van derck frechette', 
		'expected': True, 
		'description': 'van derek frechette comparison with article'
	},
    {
		'input': 'van duyn a miller;lea van puymbroeck miller', 
		'expected': False, 
		'description': 'van duyn a miller comparison with article'
	},
    {
		'input': 'van kenyon;van leslie kenyon', 
		'expected': True, 
		'description': 'van kenyon comparison with article'
	},
    {
		'input': 'van l kenyon;van leslie kenyon', 
		'expected': True, 
		'description': 'van l kenyon comparison with article'
	},
    {
		'input': 'van moore;grace van dyke more', 
		'expected': True, 
		'description': 'van moore comparison with article'
	},
    {
		'input': 'vanue b lacour;vanue b. lacour', 
		'expected': True, 
		'description': 'vanue b lacour comparison with article'
	},
    {
		'input': 'velma r lemance;robert mayer lumiansky', 
		'expected': False, 
		'description': 'velma r lemance comparison with article'
	},
    {
		'input': 'vern d delaney;verne d. delaney', 
		'expected': True, 
		'description': 'vern d delaney comparison with article'
	},
    {
		'input': 'vernon a demars;vernon a. demars', 
		'expected': True, 
		'description': 'vernon a demars comparison with article'
	},
    {
		'input': 'vernon leroy mckenzie;vernon mckenzie', 
		'expected': True, 
		'description': 'vernon leroy mckenzie comparison with article'
	},
    {
		'input': 'vernon van dyke;vernon van dyke', 
		'expected': True, 
		'description': 'vernon van dyke comparison with article'
	},
    {
		'input': 'vernon w. branko;warren van bronkhorst', 
		'expected': False, 
		'description': 'vernon w. branko comparison with article'
	},
    {
		'input': 'victor f lenzen;victor f. lenzen', 
		'expected': True, 
		'description': 'victor f lenzen comparison with article'
	},
    {
		'input': 'victor j lemke;victor jacob lemke', 
		'expected': True, 
		'description': 'victor j lemke comparison with article'
	},
    {
		'input': 'victor lange;victor lange', 
		'expected': True, 
		'description': 'victor lange comparison with article'
	},
    {
		'input': 'vila a deubach;vila deubach', 
		'expected': True, 
		'description': 'vila a deubach comparison with article'
	},
    {
		'input': 'vincent f. polcyn;vincent de paul', 
		'expected': False, 
		'description': 'vincent f. polcyn comparison with article'
	},
    {
		'input': 'vincent g dethier;vincent gaston dethier', 
		'expected': True, 
		'description': 'vincent g dethier comparison with article'
	},
    {
		'input': 'vincent j derbes;vincent joseph depaul derbes', 
		'expected': True, 
		'description': 'vincent j derbes comparison with article'
	},
    {
		'input': 'vincent t lathbury;vincent t. lathbury', 
		'expected': True, 
		'description': 'vincent t lathbury comparison with article'
	},
    {
		'input': 'vincent v lanfear;vincent w. lanfear', 
		'expected': False, 
		'description': 'vincent v lanfear comparison with article'
	},
    {
		'input': 'vinton u dearing;vinton adams dearing', 
		'expected': False, 
		'description': 'vinton u dearing comparison with article'
	},
    {
		'input': 'viola e leaf;einar leifson', 
		'expected': False, 
		'description': 'viola e leaf comparison with article'
	},
    {
		'input': 'viola vanketwick;viola beck van katwijk', 
		'expected': True, 
		'description': 'viola vanketwick comparison with article'
	},
    {
		'input': 'virgil collins;virgil lee collins', 
		'expected': True, 
		'description': 'virgil collins comparison with article'
	},
    {
		'input': 'virgil s lequire;virgil s. lequire', 
		'expected': True, 
		'description': 'virgil s lequire comparison with article'
	},
    {
		'input': 'virginia a lane;virginia lane', 
		'expected': True, 
		'description': 'virginia a lane comparison with article'
	},
    {
		'input': 'virginia e denker;erich dinkier', 
		'expected': True, 
		'description': 'virginia e denker comparison with article'
	},
    {
		'input': 'virginia hamilton;virginia van der veer hamilton', 
		'expected': True, 
		'description': 'virginia hamilton comparison with article'
	},
    {
		'input': 'virginia harris;virginia lee harris', 
		'expected': True, 
		'description': 'virginia harris comparison with article'
	},
    {
		'input': 'virginia lee guernsey;james lee guernsey', 
		'expected': False, 
		'description': 'virginia lee guernsey comparison with article'
	},
    {
		'input': 'virginia lee harrison;virginia harrison', 
		'expected': True, 
		'description': 'virginia lee harrison comparison with article'
	},
    {
		'input': 'vito a vanoni;vito a. vanoni', 
		'expected': True, 
		'description': 'vito a vanoni comparison with article'
	},
    {
		'input': 'vivan l strickland;vivan lewis strickland', 
		'expected': True, 
		'description': 'vivan l strickland comparison with article'
	},
    {
		'input': 'vladimir de\'lisovoy;vladimir delissovoy', 
		'expected': True, 
		'description': 'vladimir de\'lisovoy comparison with article'
	},
    {
		'input': 'w a dence;wilford a. dence', 
		'expected': True, 
		'description': 'w a dence comparison with article'
	},
    {
		'input': 'w e dennis;wilfred sidney dennis', 
		'expected': False, 
		'description': 'w e dennis comparison with article'
	},
    {
		'input': 'w everett derryberry;everett derryberry', 
		'expected': True, 
		'description': 'w everett derryberry comparison with article'
	},
    {
		'input': 'w lamark dodd;lamar dodd', 
		'expected': True, 
		'description': 'w lamark dodd comparison with article'
	},
    {
		'input': 'w lee culp;w. lee culp', 
		'expected': True, 
		'description': 'w lee culp comparison with article'
	},
    {
		'input': 'w leighton collins;w. leighton collins', 
		'expected': True, 
		'description': 'w leighton collins comparison with article'
	},
    {
		'input': 'w leo batten;w. leo batten', 
		'expected': True, 
		'description': 'w leo batten comparison with article'
	},
    {
		'input': 'w s laughlin;william s. laughlin', 
		'expected': True, 
		'description': 'w s laughlin comparison with article'
	},
    {
		'input': 'w wayne dedman;w. wayne dedman', 
		'expected': True, 
		'description': 'w wayne dedman comparison with article'
	},
    {
		'input': 'w. james leach;w. james leach', 
		'expected': True, 
		'description': 'w. james leach comparison with article'
	},
    {
		'input': 'waiten l kindelsperger;walter lewis kindelsperger', 
		'expected': False, 
		'description': 'waiten l kindelsperger comparison with article'
	},
    {
		'input': 'waldo e lessenger;w. e. lessenger', 
		'expected': True, 
		'description': 'waldo e lessenger comparison with article'
	},
    {
		'input': 'walken l whetten;nathan laselle whetten', 
		'expected': False, 
		'description': 'walken l whetten comparison with article'
	},
    {
		'input': 'wallace m lansford;wallace monroe lansford', 
		'expected': True, 
		'description': 'wallace m lansford comparison with article'
	},
    {
		'input': 'walter a lawrance;walter albert lawrance', 
		'expected': True, 
		'description': 'walter a lawrance comparison with article'
	},
    {
		'input': 'walter d leavitt;walter d. leavitt', 
		'expected': True, 
		'description': 'walter d leavitt comparison with article'
	},
    {
		'input': 'walter d lewis;walter richard lewis', 
		'expected': False, 
		'description': 'walter d lewis comparison with article'
	},
    {
		'input': 'walter daykin;walter lesley daykin', 
		'expected': True, 
		'description': 'walter daykin comparison with article'
	},
    {
		'input': 'walter dewey;walter safford dewey', 
		'expected': True, 
		'description': 'walter dewey comparison with article'
	},
    {
		'input': 'walter e larmie;walter esmond larmie', 
		'expected': True, 
		'description': 'walter e larmie comparison with article'
	},
    {
		'input': 'walter ehrenberg;walter j. derenberg', 
		'expected': True, 
		'description': 'walter ehrenberg comparison with article'
	},
    {
		'input': 'walter f clark;walter leighton clark', 
		'expected': False, 
		'description': 'walter f clark comparison with article'
	},
    {
		'input': 'walter f dearborn;walter fenno dearborn', 
		'expected': True, 
		'description': 'walter f dearborn comparison with article'
	},
    {
		'input': 'walter h delaplane;walter harold delaplane', 
		'expected': True, 
		'description': 'walter h delaplane comparison with article'
	},
    {
		'input': 'walter j lebeau;walter le beau', 
		'expected': True, 
		'description': 'walter j lebeau comparison with article'
	},
    {
		'input': 'walter j lemke;walter john lemke', 
		'expected': True, 
		'description': 'walter j lemke comparison with article'
	},
    {
		'input': 'walter l coplin;walter lee coplin', 
		'expected': True, 
		'description': 'walter l coplin comparison with article'
	},
    {
		'input': 'walter l moore;walter lee moore', 
		'expected': True, 
		'description': 'walter l moore comparison with article'
	},
    {
		'input': 'walter l roosa;walter laidlaw roosa', 
		'expected': True, 
		'description': 'walter l roosa comparison with article'
	},
    {
		'input': 'walter l simmons;walter lee simmons', 
		'expected': True, 
		'description': 'walter l simmons comparison with article'
	},
    {
		'input': 'walter l thomas;walter lee thomas', 
		'expected': True, 
		'description': 'walter l thomas comparison with article'
	},
    {
		'input': 'walter l van gothen;armand l. degaetano', 
		'expected': False, 
		'description': 'walter l van gothen comparison with article'
	},
    {
		'input': 'walter l vandervest;walter louis vandervest', 
		'expected': True, 
		'description': 'walter l vandervest comparison with article'
	},
    {
		'input': 'walter l wilson;walter leroy wilson', 
		'expected': True, 
		'description': 'walter l wilson comparison with article'
	},
    {
		'input': 'walter l winkenwerder;walter lafollette winkenwerder', 
		'expected': True, 
		'description': 'walter l winkenwerder comparison with article'
	},
    {
		'input': 'walter la pierre;walter a. la pierre', 
		'expected': True, 
		'description': 'walter la pierre comparison with article'
	},
    {
		'input': 'walter langston;walter stanley langston', 
		'expected': True, 
		'description': 'walter langston comparison with article'
	},
    {
		'input': 'walter lay;walter edwin lay', 
		'expected': True, 
		'description': 'walter lay comparison with article'
	},
    {
		'input': 'walter lee green;hampton lee green', 
		'expected': False, 
		'description': 'walter lee green comparison with article'
	},
    {
		'input': 'walter m denny;walter lee denny', 
		'expected': False, 
		'description': 'walter m denny comparison with article'
	},
    {
		'input': 'walter m langford;walter m. langford', 
		'expected': True, 
		'description': 'walter m langford comparison with article'
	},
    {
		'input': 'walter marshall;walter vancleve marshall', 
		'expected': True, 
		'description': 'walter marshall comparison with article'
	},
    {
		'input': 'walter putz;walter van de putte', 
		'expected': True, 
		'description': 'walter putz comparison with article'
	},
    {
		'input': 'walter s lake;walter sidelinger lake', 
		'expected': True, 
		'description': 'walter s lake comparison with article'
	},
    {
		'input': 'walter summers;walter lee summers', 
		'expected': True, 
		'description': 'walter summers comparison with article'
	},
    {
		'input': 'walter v price;walter van price', 
		'expected': True, 
		'description': 'walter v price comparison with article'
	},
    {
		'input': 'walter v riley;walter lee riley', 
		'expected': False, 
		'description': 'walter v riley comparison with article'
	},
    {
		'input': 'walter w leavitt;harold walter leavitt', 
		'expected': False, 
		'description': 'walter w leavitt comparison with article'
	},
    {
		'input': 'walter wilkins;walter laroy wilkins', 
		'expected': True, 
		'description': 'walter wilkins comparison with article'
	},
    {
		'input': 'ward lambert;ward lewis lambert', 
		'expected': True, 
		'description': 'ward lambert comparison with article'
	},
    {
		'input': 'warren k lewis;warren kendall lewis', 
		'expected': True, 
		'description': 'warren k lewis comparison with article'
	},
    {
		'input': 'warren l rosen;warren leucht rosen', 
		'expected': True, 
		'description': 'warren l rosen comparison with article'
	},
    {
		'input': 'warren law;warren aubrey law', 
		'expected': True, 
		'description': 'warren law comparison with article'
	},
    {
		'input': 'warren lee slagle;warren lee slagle', 
		'expected': True, 
		'description': 'warren lee slagle comparison with article'
	},
    {
		'input': 'warren m deacon;warren mcallister deacon', 
		'expected': True, 
		'description': 'warren m deacon comparison with article'
	},
    {
		'input': 'warren m. lee;warren lee', 
		'expected': True, 
		'description': 'warren m. lee comparison with article'
	},
    {
		'input': 'warren w delapp;warren w. delapp', 
		'expected': True, 
		'description': 'warren w delapp comparison with article'
	},
    {
		'input': 'warren w leigh;warren w. leigh', 
		'expected': True, 
		'description': 'warren w leigh comparison with article'
	},
    {
		'input': 'washburne shipton;washburn denning shipton', 
		'expected': True, 
		'description': 'washburne shipton comparison with article'
	},
    {
		'input': 'wassily w leontief;wassily w. leontief', 
		'expected': True, 
		'description': 'wassily w leontief comparison with article'
	},
    {
		'input': 'wayne a lee;wayne a. lee', 
		'expected': True, 
		'description': 'wayne a lee comparison with article'
	},
    {
		'input': 'wayne a r leys;wayne a. r. leys', 
		'expected': True, 
		'description': 'wayne a r leys comparison with article'
	},
    {
		'input': 'wayne d sieh;wayne delbert sieh', 
		'expected': True, 
		'description': 'wayne d sieh comparison with article'
	},
    {
		'input': 'wayne dennis;wayne dennis', 
		'expected': True, 
		'description': 'wayne dennis comparison with article'
	},
    {
		'input': 'wayne m leitlinger;joaquin mazdak luttinger', 
		'expected': False, 
		'description': 'wayne m leitlinger comparison with article'
	},
    {
		'input': 'webster w decker;webster w. decker', 
		'expected': True, 
		'description': 'webster w decker comparison with article'
	},
    {
		'input': 'wendell m latimer;wendell m. latimer', 
		'expected': True, 
		'description': 'wendell m latimer comparison with article'
	},
    {
		'input': 'werner f. leopold;werner f. leopold', 
		'expected': True, 
		'description': 'werner f. leopold comparison with article'
	},
    {
		'input': 'werner levi;werner levi', 
		'expected': True, 
		'description': 'werner levi comparison with article'
	},
    {
		'input': 'wesley e lewis;wesley lewis', 
		'expected': True, 
		'description': 'wesley e lewis comparison with article'
	},
    {
		'input': 'weston l murray;weston lafayette murray', 
		'expected': True, 
		'description': 'weston l murray comparison with article'
	},
    {
		'input': 'wilber l beauchamp;wilbur lee beauchamp', 
		'expected': True, 
		'description': 'wilber l beauchamp comparison with article'
	},
    {
		'input': 'wilbur d johnston;wilbur dexter johnston', 
		'expected': True, 
		'description': 'wilbur d johnston comparison with article'
	},
    {
		'input': 'wiley l housewright;wiley lee housewright', 
		'expected': True, 
		'description': 'wiley l housewright comparison with article'
	},
    {
		'input': 'wilfid desmarais;wilfrid desmarais', 
		'expected': True, 
		'description': 'wilfid desmarais comparison with article'
	},
    {
		'input': 'wilfred f langelier;wilfred f. langelier', 
		'expected': True, 
		'description': 'wilfred f langelier comparison with article'
	},
    {
		'input': 'willard l rogers;willard lewis rogers', 
		'expected': True, 
		'description': 'willard l rogers comparison with article'
	},
    {
		'input': 'willard oquinn;willard van orman quine', 
		'expected': False, 
		'description': 'willard oquinn comparison with article'
	},
    {
		'input': 'willard t leeds;willard l. leeds', 
		'expected': False, 
		'description': 'willard t leeds comparison with article'
	},
    {
		'input': 'willard van hazel;willard van hazel', 
		'expected': True, 
		'description': 'willard van hazel comparison with article'
	},
    {
		'input': 'willem van wagtendonk;willem johan van wagtendonk', 
		'expected': True, 
		'description': 'willem van wagtendonk comparison with article'
	},
    {
		'input': 'william a devine;william a. devine', 
		'expected': True, 
		'description': 'william a devine comparison with article'
	},
    {
		'input': 'william a lewis;william abbett lewis', 
		'expected': True, 
		'description': 'william a lewis comparison with article'
	},
    {
		'input': 'william a pace;william leon pious', 
		'expected': False, 
		'description': 'william a pace comparison with article'
	},
    {
		'input': 'william a van heyn;william a. venin', 
		'expected': False, 
		'description': 'william a van heyn comparison with article'
	},
    {
		'input': 'william a van winkle;william alexander van winkle', 
		'expected': True, 
		'description': 'william a van winkle comparison with article'
	},
    {
		'input': 'william a. lamb;c. a. lamb', 
		'expected': False, 
		'description': 'william a. lamb comparison with article'
	},
    {
		'input': 'william b lewis;william benjamin lewis', 
		'expected': True, 
		'description': 'william b lewis comparison with article'
	},
    {
		'input': 'william c de vane;william clyde de vane', 
		'expected': True, 
		'description': 'william c de vane comparison with article'
	},
    {
		'input': 'william c de vane;william clyde devane', 
		'expected': True, 
		'description': 'william c de vane comparison with article'
	},
    {
		'input': 'william c deamer;william c. deamer', 
		'expected': True, 
		'description': 'william c deamer comparison with article'
	},
    {
		'input': 'william c deveny;william c. deveny', 
		'expected': True, 
		'description': 'william c deveny comparison with article'
	},
    {
		'input': 'william c lam;william c. lam', 
		'expected': True, 
		'description': 'william c lam comparison with article'
	},
    {
		'input': 'william c. dew;william c. dew', 
		'expected': True, 
		'description': 'william c. dew comparison with article'
	},
    {
		'input': 'william carmichael;william lawson carmichael', 
		'expected': True, 
		'description': 'william carmichael comparison with article'
	},
    {
		'input': 'william coggshall;william lamar coggshall', 
		'expected': True, 
		'description': 'william coggshall comparison with article'
	},
    {
		'input': 'william collins;william lee collins', 
		'expected': True, 
		'description': 'william collins comparison with article'
	},
    {
		'input': 'william d barns;william derrick barns', 
		'expected': True, 
		'description': 'william d barns comparison with article'
	},
    {
		'input': 'william d denny;william d. denny', 
		'expected': True, 
		'description': 'william d denny comparison with article'
	},
    {
		'input': 'william d ladd;william edwards ladd', 
		'expected': False, 
		'description': 'william d ladd comparison with article'
	},
    {
		'input': 'william d larson;william d. larson', 
		'expected': True, 
		'description': 'william d larson comparison with article'
	},
    {
		'input': 'william d legg, sr;kenneth d. legge', 
		'expected': False, 
		'description': 'william d legg, sr comparison with article'
	},
    {
		'input': 'william d lewis;william ditto lewis', 
		'expected': True, 
		'description': 'william d lewis comparison with article'
	},
    {
		'input': 'william d metz;william dewitt metz', 
		'expected': True, 
		'description': 'william d metz comparison with article'
	},
    {
		'input': 'william d perry;william decatur perry', 
		'expected': True, 
		'description': 'william d perry comparison with article'
	},
    {
		'input': 'william d van vorst;william d. van vorst', 
		'expected': True, 
		'description': 'william d van vorst comparison with article'
	},
    {
		'input': 'william daniel lee;william daniel lee', 
		'expected': True, 
		'description': 'william daniel lee comparison with article'
	},
    {
		'input': 'william de feo;william f. macfee', 
		'expected': True, 
		'description': 'william de feo comparison with article'
	},
    {
		'input': 'william dehorn;william dehorn', 
		'expected': True, 
		'description': 'william dehorn comparison with article'
	},
    {
		'input': 'william dickerman;william b. deichmann', 
		'expected': False, 
		'description': 'william dickerman comparison with article'
	},
    {
		'input': 'william e de turk;william ernest deturk', 
		'expected': True, 
		'description': 'william e de turk comparison with article'
	},
    {
		'input': 'william e decker;william decker', 
		'expected': True, 
		'description': 'william e decker comparison with article'
	},
    {
		'input': 'william e lawrence;william ewart lawrence', 
		'expected': True, 
		'description': 'william e lawrence comparison with article'
	},
    {
		'input': 'william e merritt;william wellesley demeritt', 
		'expected': False, 
		'description': 'william e merritt comparison with article'
	},
    {
		'input': 'william e p clark;william e. de clark', 
		'expected': True, 
		'description': 'william e p clark comparison with article'
	},
    {
		'input': 'william f lahey;william f. lahey', 
		'expected': True, 
		'description': 'william f lahey comparison with article'
	},
    {
		'input': 'william f lamb;william f. lamb', 
		'expected': True, 
		'description': 'william f lamb comparison with article'
	},
    {
		'input': 'william g dent;robert william dent', 
		'expected': False, 
		'description': 'william g dent comparison with article'
	},
    {
		'input': 'william g lennox;william gordon lennox', 
		'expected': True, 
		'description': 'william g lennox comparison with article'
	},
    {
		'input': 'william g leonard;guy william leonard', 
		'expected': True, 
		'description': 'william g leonard comparison with article'
	},
    {
		'input': 'william g robertson;william van bogaert robertson', 
		'expected': False, 
		'description': 'william g robertson comparison with article'
	},
    {
		'input': 'william h crum;william leonard crum', 
		'expected': False, 
		'description': 'william h crum comparison with article'
	},
    {
		'input': 'william h garrett;william lawrence garrott', 
		'expected': False, 
		'description': 'william h garrett comparison with article'
	},
    {
		'input': 'william h lavell;hugh rodman leavell', 
		'expected': False, 
		'description': 'william h lavell comparison with article'
	},
    {
		'input': 'william h lawrence;william henry lawrence', 
		'expected': True, 
		'description': 'william h lawrence comparison with article'
	},
    {
		'input': 'william h leary;wllliam h. leary', 
		'expected': True, 
		'description': 'william h leary comparison with article'
	},
    {
		'input': 'william h meyer;william h. lewis meyer', 
		'expected': True, 
		'description': 'william h meyer comparison with article'
	},
    {
		'input': 'william h seward;herbert lee seward', 
		'expected': False, 
		'description': 'william h seward comparison with article'
	},
    {
		'input': 'william j dean;william j. dean', 
		'expected': True, 
		'description': 'william j dean comparison with article'
	},
    {
		'input': 'william j dehaas;j. anton de haas', 
		'expected': False, 
		'description': 'william j dehaas comparison with article'
	},
    {
		'input': 'william j dempsey;william j. dempsey', 
		'expected': True, 
		'description': 'william j dempsey comparison with article'
	},
    {
		'input': 'william j lee;william j. lee', 
		'expected': True, 
		'description': 'william j lee comparison with article'
	},
    {
		'input': 'william j leipertz;vernon william lippard', 
		'expected': False, 
		'description': 'william j leipertz comparison with article'
	},
    {
		'input': 'william j leonard;william j. leonard', 
		'expected': True, 
		'description': 'william j leonard comparison with article'
	},
    {
		'input': 'william johnston;william denis johnston', 
		'expected': True, 
		'description': 'william johnston comparison with article'
	},
    {
		'input': 'william l burlison;william leonidas burlison', 
		'expected': True, 
		'description': 'william l burlison comparison with article'
	},
    {
		'input': 'william l cory;william leonard cory', 
		'expected': True, 
		'description': 'william l cory comparison with article'
	},
    {
		'input': 'william l doyle;william lewis doyle', 
		'expected': True, 
		'description': 'william l doyle comparison with article'
	},
    {
		'input': 'william l duren;william larkin duren', 
		'expected': True, 
		'description': 'william l duren comparison with article'
	},
    {
		'input': 'william l gardner;william lawrence gardner', 
		'expected': True, 
		'description': 'william l gardner comparison with article'
	},
    {
		'input': 'william l king;william lewis king', 
		'expected': True, 
		'description': 'william l king comparison with article'
	},
    {
		'input': 'william l lane;laurence william lane', 
		'expected': True, 
		'description': 'william l lane comparison with article'
	},
    {
		'input': 'william l langer;william leonard langer', 
		'expected': True, 
		'description': 'william l langer comparison with article'
	},
    {
		'input': 'william l lester;william l. lester', 
		'expected': True, 
		'description': 'william l lester comparison with article'
	},
    {
		'input': 'william l lomey;william l. lamey', 
		'expected': True, 
		'description': 'william l lomey comparison with article'
	},
    {
		'input': 'william l sachse;william lewis sachse', 
		'expected': True, 
		'description': 'william l sachse comparison with article'
	},
    {
		'input': 'william l schwartz;william leonard schwartz', 
		'expected': True, 
		'description': 'william l schwartz comparison with article'
	},
    {
		'input': 'william l wheeler;william lawrence wheeler', 
		'expected': True, 
		'description': 'william l wheeler comparison with article'
	},
    {
		'input': 'william l wiley;william leon wiley', 
		'expected': True, 
		'description': 'william l wiley comparison with article'
	},
    {
		'input': 'william l wylie;william leroy wylie', 
		'expected': True, 
		'description': 'william l wylie comparison with article'
	},
    {
		'input': 'william lafferty;william a. lafferty', 
		'expected': True, 
		'description': 'william lafferty comparison with article'
	},
    {
		'input': 'william lagrange;william f. lagrange', 
		'expected': True, 
		'description': 'william lagrange comparison with article'
	},
    {
		'input': 'william lamont;william hayes fogg lamont', 
		'expected': True, 
		'description': 'william lamont comparison with article'
	},
    {
		'input': 'william land;william m. landau', 
		'expected': True, 
		'description': 'william land comparison with article'
	},
    {
		'input': 'william landeen;william m. landeen', 
		'expected': True, 
		'description': 'william landeen comparison with article'
	},
    {
		'input': 'william langford;william s. langford', 
		'expected': True, 
		'description': 'william langford comparison with article'
	},
    {
		'input': 'william lee;james william lee', 
		'expected': True, 
		'description': 'william lee comparison with article'
	},
    {
		'input': 'william leo lucey;william l. lucey', 
		'expected': True, 
		'description': 'william leo lucey comparison with article'
	},
    {
		'input': 'william lewis;ben william lewis', 
		'expected': True, 
		'description': 'william lewis comparison with article'
	},
    {
		'input': 'william m dey;william morton dey', 
		'expected': True, 
		'description': 'william m dey comparison with article'
	},
    {
		'input': 'william m laub;william t. laube', 
		'expected': False, 
		'description': 'william m laub comparison with article'
	},
    {
		'input': 'william miller;william lee miller', 
		'expected': True, 
		'description': 'william miller comparison with article'
	},
    {
		'input': 'william n lacey;william n. lacey', 
		'expected': True, 
		'description': 'william n lacey comparison with article'
	},
    {
		'input': 'william n leonard;william n. leonard', 
		'expected': True, 
		'description': 'william n leonard comparison with article'
	},
    {
		'input': 'william o. dewey;osee hughes dewey', 
		'expected': False, 
		'description': 'william o. dewey comparison with article'
	},
    {
		'input': 'william p delaney;william p. delaney', 
		'expected': True, 
		'description': 'william p delaney comparison with article'
	},
    {
		'input': 'william p lehrer;william p. lehrer', 
		'expected': True, 
		'description': 'william p lehrer comparison with article'
	},
    {
		'input': 'william r de valdez;william belcher ballis', 
		'expected': False, 
		'description': 'william r de valdez comparison with article'
	},
    {
		'input': 'william r dennes;william r. dennes', 
		'expected': True, 
		'description': 'william r dennes comparison with article'
	},
    {
		'input': 'william r devine;william r. divine', 
		'expected': True, 
		'description': 'william r devine comparison with article'
	},
    {
		'input': 'william roberts;william lewis roberts', 
		'expected': True, 
		'description': 'william roberts comparison with article'
	},
    {
		'input': 'william s la sor, jr;w. s. lasor', 
		'expected': True, 
		'description': 'william s la sor, jr comparison with article'
	},
    {
		'input': 'william s levings;william s. levings', 
		'expected': True, 
		'description': 'william s levings comparison with article'
	},
    {
		'input': 'william s root;william dean rutz', 
		'expected': False, 
		'description': 'william s root comparison with article'
	},
    {
		'input': 'william stephen walker;stephen leonard walker', 
		'expected': False, 
		'description': 'william stephen walker comparison with article'
	},
    {
		'input': 'william sullivan;william lawrence sullivan', 
		'expected': True, 
		'description': 'william sullivan comparison with article'
	},
    {
		'input': 'william t kolb;william lester kolb', 
		'expected': False, 
		'description': 'william t kolb comparison with article'
	},
    {
		'input': 'william t laprade;william thomas laprade', 
		'expected': True, 
		'description': 'william t laprade comparison with article'
	},
    {
		'input': 'william t lentz;william jacoby lentz', 
		'expected': False, 
		'description': 'william t lentz comparison with article'
	},
    {
		'input': 'william v chandler;william von chandler', 
		'expected': True, 
		'description': 'william v chandler comparison with article'
	},
    {
		'input': 'william v lambert;william v. lambert', 
		'expected': True, 
		'description': 'william v lambert comparison with article'
	},
    {
		'input': 'william van camp;william morris van camp', 
		'expected': True, 
		'description': 'william van camp comparison with article'
	},
    {
		'input': 'william van parker;william vann parker', 
		'expected': True, 
		'description': 'william van parker comparison with article'
	},
    {
		'input': 'william van tassel;william van tassel', 
		'expected': True, 
		'description': 'william van tassel comparison with article'
	},
    {
		'input': 'willie lee bonner;lee bonar', 
		'expected': True, 
		'description': 'willie lee bonner comparison with article'
	},
    {
		'input': 'wilmer l sibbet;wilmer lawrence sibbitt', 
		'expected': True, 
		'description': 'wilmer l sibbet comparison with article'
	},
    {
		'input': 'wilson c ladue;wilson c. ladue', 
		'expected': True, 
		'description': 'wilson c ladue comparison with article'
	},
    {
		'input': 'wilson e langley;wilson d. langley', 
		'expected': False, 
		'description': 'wilson e langley comparison with article'
	},
    {
		'input': 'wilson l miser;wilson lee miser', 
		'expected': True, 
		'description': 'wilson l miser comparison with article'
	},
    {
		'input': 'winford l sharp;winford lee sharp', 
		'expected': True, 
		'description': 'winford l sharp comparison with article'
	},
    {
		'input': 'winfred p lehmann;winfred p. lehmann', 
		'expected': True, 
		'description': 'winfred p lehmann comparison with article'
	},
    {
		'input': 'winiferd m leiby;lester m. libo', 
		'expected': False, 
		'description': 'winiferd m leiby comparison with article'
	},
    {
		'input': 'winifred v shields;currin vance shields', 
		'expected': False, 
		'description': 'winifred v shields comparison with article'
	},
    {
		'input': 'winston l brembeck;winston lamont brembeck', 
		'expected': True, 
		'description': 'winston l brembeck comparison with article'
	},
    {
		'input': 'wm a lessa;william a. lessa', 
		'expected': True, 
		'description': 'wm a lessa comparison with article'
	},
    {
		'input': 'wm van a jr clark, jr;william van alan clark', 
		'expected': True, 
		'description': 'wm van a jr clark, jr comparison with article'
	},
    {
		'input': 'wm w sanderson;wiley devere sanderson', 
		'expected': False, 
		'description': 'wm w sanderson comparison with article'
	},
    {
		'input': 'wm. lester jordan;lester jordan', 
		'expected': True, 
		'description': 'wm. lester jordan comparison with article'
	},
    {
		'input': 'yvonne m cam;lucien m. lecam', 
		'expected': False, 
		'description': 'yvonne m cam comparison with article'
	},
    {
		'input': 'zebulon b vance;zeb vance', 
		'expected': True, 
		'description': 'zebulon b vance comparison with article'
	},
    {
		'input': 'zelma b leonhard;zelma b. leonhard', 
		'expected': True, 
		'description': 'zelma b leonhard comparison with article'
	},
    {
		'input': 'zens l smith;zens lawrence smith', 
		'expected': True, 
		'description': 'zens l smith comparison with article'
	},
    {
		'input': 'a john vounie;john j. a. devenny', 
		'expected': True, 
		'description': 'a john vounie comparison with article'
	},
    {
		'input': 'albert renzi;albert bernhardi van rennes', 
		'expected': True, 
		'description': 'albert renzi comparison with article'
	},
    {
		'input': 'alfred von geldern;alfred gellhorn', 
		'expected': True, 
		'description': 'alfred von geldern comparison with article'
	},
    {
		'input': 'clifford mays;clifford j. lemay', 
		'expected': True, 
		'description': 'clifford mays comparison with article'
	},
    {
		'input': 'helan francest lauterer;helen forrest lauterer', 
		'expected': True, 
		'description': 'helan francest lauterer comparison with article'
	},
    {
		'input': 'henry p lane, jr;henry p. lange', 
		'expected': False, 
		'description': 'henry p lane, jr comparison with article'
	},
    {
		'input': 'irving large;irving d. lorge', 
		'expected': True, 
		'description': 'irving large comparison with article'
	},
    {
		'input': 'john w leslie;wolf leslau', 
		'expected': False, 
		'description': 'john w leslie comparison with article'
	},
    {
		'input': 'joseph panta;joseph della penta', 
		'expected': True, 
		'description': 'joseph panta comparison with article'
	},
    {
		'input': 'joseph w beck;joseph van derbeek', 
		'expected': True, 
		'description': 'joseph w beck comparison with article'
	},
    {
		'input': 'louis depolito;robert louis politzer', 
		'expected': False, 
		'description': 'louis depolito comparison with article'
	},
    {
		'input': 'martin lisan;martin lessen', 
		'expected': True, 
		'description': 'martin lisan comparison with article'
	},
    {
		'input': 'morton levy;martin j. levy', 
		'expected': False, 
		'description': 'morton levy comparison with article'
	},
    {
		'input': 'theodore b ley;theodore delay', 
		'expected': True, 
		'description': 'theodore b ley comparison with article'
	},
    {
		'input': 'victor j cassidy;julian victor langmead casserley', 
		'expected': True, 
		'description': 'victor j cassidy comparison with article'
	},
]
