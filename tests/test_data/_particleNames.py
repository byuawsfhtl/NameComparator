"""This file has a list of name comparisons that involve particles (e.g. 'de', 'do', 'van')
and the expected outcome. A pair of two different particles must not count as a matching
word, since it already lowers the number of word matches required."""

particleNames = [
    {
		'name_one': 'Marques de Barros',
		'name_two': 'do Valle',
		'expected': False,
		'description': 'only the particles de and do pair up'
	},
    {
		'name_one': 'Silva de Souza',
		'name_two': 'do Valle',
		'expected': False,
		'description': 'only the particles de and do pair up (silva de souza)'
	},
    {
		'name_one': 'Ana de Jesus',
		'name_two': 'do Valle',
		'expected': False,
		'description': 'only the particles de and do pair up (ana de jesus)'
	},
    {
		'name_one': 'Marques de Barros',
		'name_two': 'du Valle',
		'expected': False,
		'description': 'only the particles de and du pair up'
	},
    {
		'name_one': 'Maria do Valle',
		'name_two': 'do Valle',
		'expected': True,
		'description': 'surname contained in the longer name'
	},
    {
		'name_one': 'Ribeiro Paes',
		'name_two': 'Paes',
		'expected': True,
		'description': 'one word surname contained in the longer name'
	},
    {
		'name_one': 'de Souza',
		'name_two': 'da Souza',
		'expected': True,
		'description': 'same surname with a different particle'
	},
    {
		'name_one': 'dela cruz',
		'name_two': 'd rosa',
		'expected': False,
		'description': 'an initial paired with a particle is not a match'
	},
    {
		'name_one': 'anna v berg',
		'name_two': 'anna van berg',
		'expected': True,
		'description': 'an initial can stand in for a particle'
	},
]
