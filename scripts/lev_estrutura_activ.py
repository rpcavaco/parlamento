
from lib_estrutura_json import unique, listaparcial, full

CONFIGOBJ_ACTIVS= {
	'prefixos_a_truncar': [
		'pt_gov_ar_objectos_actividades_',
		'pt_gov_ar_objectos_',
		'ArrayOfPt_gov_ar_objectos_'
	],
	'prefixos_de_atributo_a_ignorar': [
		'@', '?', 'ArrayOf'
	],
	'sufixos_de_atributo_a_ignorar': [
		'List', 'Out'
	],
	'atributos_a_ignorar': [
		"Atividades"
	]
}

DATA = "20180609"
				
if __name__ == "__main__":
	
	full('Originais/20180609/AtividadesXIII.json', 'saidas/20180609/Atividade013_Struct_{}.json', CONFIGOBJ_ACTIVS, maxlevel=-1)
	
	frompath = "Originais/{}/AtividadesXIII.json".format(DATA) 
	topath = "Originais/{}/".format(DATA) + "Atividade013_Struct_{}.json"
	
	full(frompath, topath, CONFIGOBJ_ACTIVS, maxlevel=-1)
