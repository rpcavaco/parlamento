
from lib_estrutura_json import unique, listaparcial, full


CONFIGOBJ_ACTIV_DEPUTADOS = {
	'prefixos_a_truncar': [
		'pt_gov_ar_wsar_objectos_', 
		'pt_ar_wsgode_objectos_'
	],
	'prefixos_de_atributo_a_ignorar': [
		'@', '?', 'ArrayOf'
	],
	'sufixos_de_atributo_a_ignorar': [
		'List'
	],
	'atributos_a_ignorar': [
		"ini","req","sgt", "scgt", "intev", "actP", "gpa", "rel", "eventos",
		"deslocacoes","cms","dadosLegisDeputado","audiencias","audicoes", "depGP", "depCargo",
		"parlamentoJovens", "videos", "depSituacao", "dlP", "dlE", "relatoresIniciativas",
		"relatoresPeticoes", "relatoresContasPublicas", "relatoresIniEuropeias"		
	]
}

			
if __name__ == "__main__":
	
	#unique('Originais/AtividadesXIII.json', 'Atividade013_Struct_{}.json', CONFIGOBJ_ACTIVS)
	
	#unique('Originais/AtividadeDeputadoXIII.json', 'AtividadeDeputado013_{}.json', CONFIGOBJ_ACTIV_DEPUTADOS)
	
	#listaparcial('Originais/AtividadesXIII.json', 'AtividadesXIII_amostra.txt', limitcount=1000, maxlevel=6)


	#full('Originais/AtividadesXIII.json', 'Atividade013_{}.json', CONFIGOBJ_ACTIVS)

	#full('Originais/AtividadeDeputadoXIII.json', 'AtividadeDeputado013_{}.json', CONFIGOBJ_ACTIV_DEPUTADOS)
	
	# 20180509 
	#listaparcial('Originais/20180609/AtividadesXIII.json', 'saidas/20180609/AtividadesXIII_amostra.txt', limitcount=1000, maxlevel=6)
	#extractvalues = set([])
	full('Originais/20180609/AtividadesXIII.json', 'saidas/20180609/Atividade013_Struct_{}.json', CONFIGOBJ_ACTIVS, maxlevel=-1)
	
	#print(extractvalues)
