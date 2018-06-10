
import json


from pprint import pprint
from datetime import datetime as dt

import pprint



########################################################################
# Script para limpar ou obter a 'estrutura' de um ficheiro JSON
#
# FUNÇÕES DE ALTO NÍVEL
#
# listaparcial(caminho_entrada, caminho_saida, limitcount, 
#		maxlevel) - função de amostragem que transforma 'limitcount' 
#		linhas do ficheiro JSON de entrada numa saida de texto indentado, 
# 		sem filtrar, e sem preocupação em construir objectos JSON
#		completos na saída.
#
#		O objectivo desta função é o de conseguir ler com facilidade n
#		linhas ou o JSON original apenas até uma certa profundidade. 
#		Depois de efectuar uma amostragem por esta via, é mais fácil
#		produzir a configuração final de extracção a usar com 'unique'.
#
#		parâmetros:
#	
#			caminho_entrada - caminho completo para o ficheiro de 
#			entrada;
#
#			caminho_saida - caminho completo para o ficheiro JSON de 
#			saida;
#
#			limitcount - limite de número máximo de linhas a ler do 
#			ficheiro de entrada;
#
#			maxlevel - limite máximo à profunidade da árvore a ler.
#
# full(caminho_entrada, caminho_saida, configobj) - após filtrar o 
#		conteúdo, é gerado um novo ficheiro JSON indentado, contendo a 
#		totalidade do ficheiro de entrada.
#		O nome de saída pode levar uma entrada de formato {} que receberá
#		a data e hora no formato ISO
#
#		parâmetros:
#	
#			caminho_entrada - caminho completo para o ficheiro JSON de 
#			entrada;
#
#			caminho_saida - caminho completo para o ficheiro JSON de 
#			saida;
#
#			configobj - dicionário contendo os parâmetros de configuração
#			do processo de leitura;
#
# unique(caminho_entrada, caminho_saida, configobj) - após filtrar o 
#		conteúdo, é gerado um novo ficheiro JSON de "estrutura", 
#		indentado, no qual cada lista é substituída por uma lista idêntica 
#		contendo apenas o último elemento.
#		O nome de saída pode levar uma entrada de formato {} que receberá
#		a data e hora no formato ISO
#
#		parâmetros:
#	
#			caminho_entrada - caminho completo para o ficheiro JSON de 
#			entrada;
#
#			caminho_saida - caminho completo para o ficheiro JSON de 
#			saida;
#
#			configobj - dicionário contendo os parâmetros de configuração
#			do processo de leitura;
#
#
# OUTRAS FUNÇÕES
#
# ler(caminho_entrada, dicionário_saida, configobj, 
#		listaumelemento, maxlevel) - extractor propriamente dito, 
#		transforma o ficheiro de entrada numa árvore dentro do dicionário
#		que deverá estar vazio.
#
#		parâmetros:
#	
#			caminho_entrada - caminho completo para o ficheiro de 
#			entrada;
#
#			dicionário_saida - dicionário que irá receber a árvore produzida;
#
#			configobj - dicionário contendo os parâmetros de configuração
#			do processo de leitura;
#
#			listaumelemento - booleano, se verdadeiro apenas o primeiro
#			elemento de cada lista é transcrito;
#
#			maxlevel - limite máximo à profunidade da árvore a ler.
#
# listar(caminho_entrada, lista_saida, 
#		limitcount, maxlevel) - extractor de texto  transforma o ficheiro 
#		de entrada numa lista de linhas de text de saída que deverá 
#		estar vazia.
#
#		parâmetros:
#	
#			caminho_entrada - caminho completo para o ficheiro de 
#			entrada;
#
#			lista_saida - lista que irá receber as linhas de texto 
#			produzidas;
#
#			limitcount - limite de número máximo de linhas a ler do 
#			ficheiro de entrada;
#
#			maxlevel - limite máximo à profunidade da árvore a ler.
#
#
#			


def listar(p_path, out_list, limitcount=-1, maxlevel=-1):
	
	stack = []
	level = 0
	tree = json.load(open(p_path))
	del out_list[:]
	
	stack.append([level, '--raiz--', tree])
	
	count = 0
	
	while len(stack) > 0:
		
		currlevel, currid, currnode = stack.pop()
			
		if currnode is None:
			continue
		
		newlevel = currlevel + 1	
		
		if maxlevel >= 0 and newlevel > maxlevel:
			dostack = False
		else:
			dostack = True
		
		if isinstance(currnode, list):	
			
			out_list.append("{}{}:".format(' '*(newlevel-2), currid))
			if dostack:
				#currnode.reverse()
				for ei, el in reversed(list(enumerate(currnode))):
					stack.append([newlevel, str(ei), el])
			
		elif isinstance(currnode, dict):

			if currid != '--raiz--' \
					and not currid.startswith('@') \
					and not currid.startswith('?'):
				out_list.append("{}{}:".format(' '*(newlevel-2), currid))
			
			if dostack:
				kl = list(currnode.keys())
				kl.reverse()
				for key in kl:				
					stack.append([newlevel, key, currnode[key]])

		else:	
			
			if not str(currid).strip().startswith('@'):
				out_list.append("{}{}: {}".format(' '*(newlevel-2), currid, str(currnode)[:40]))
		
		if limitcount >= 0 and len(out_list) >= limitcount:	
			break	
	
	
def listaparcial(p_in_path, p_out_path, limitcount=10000, maxlevel=-1):
	out = []
	listar(p_in_path, out, limitcount=limitcount, maxlevel=maxlevel)
	with open(p_out_path, 'w') as f:
		for item in out:
			f.write("%s\n" % item)


def lerstruct(p_path, out_dict, configobj, listaumelemento=True, maxlevel=-1, extractkey=None, extractvalues=None):
	
	stack = []
	level = 0
	tree = json.load(open(p_path))
	
	keys_set = set([])
	
	pp = pprint.PrettyPrinter(indent=4)
	
	# A stack é uma lista que contém os nós da árvore que foram 'tocados' 
	# mas ainda não 'visitados'. Em cada nova 'visita' a um nó da árvore, 
	# os nós que lhe são adjacentes são 'tocados' e colocados na stack para 
	# serem 'visitados' em ciclos seguintes
	# No início, a stack contém apenas o nó raiz da árvore.
	
	stack.append([level, '--raiz--', tree, out_dict, []])
	
	count = 0
	
	while len(stack) > 0:

		# Retirar da stack um nó 'tocado'.  
		currlevel, currid, currnode, outobj_node, tree_path_list = stack.pop()
		
		
		# if 'Eventos' in tree_path_list:
			# print(tree_path_list)
		# break
		
		# Chegámos ao final de um ramo da árvore
		if currnode is None:
			continue
		
		# Cada nova visita, a 'profundidade' aumenta
		newlevel = currlevel + 1	
		
		# Se tiver sido imposto um limite de 'profundidade' às visitas,
		# e esse limite tiver sido ultrapassado, vamos parar de 'tocar'
		# nós, impedindo novas colocações na stack
		if maxlevel >= 0 and newlevel > maxlevel:
			dostack = False
		else:
			dostack = True

		# Truncar prefixos de acordo com as configurações
		for prefx in configobj['prefixos_a_truncar']:			
			currid = currid.replace(prefx, '')
		
		# Se o nó seguinte for um dicionário de uma só chave que contém
		#  uma lista, vamos resumi-lo 'a lista nele contida
		if isinstance(currnode, dict) and len(currnode.keys()) == 1:
			keysl = list(currnode.keys())
			singlekey = keysl[0]
			if isinstance(currnode[singlekey], list):
				currnode = currnode[singlekey]
				
		# if isinstance(currnode, dict):
			# keysl = list(currnode.keys())
			# firstkey = keysl[0]
			# print(f"currid: {currid}, fkey:{firstkey}")
		
		# Se o nó seguinte for uma lista, riar e preencher uma lista
		# no objecto de saída
		if isinstance(currnode, list):	
			
			# if len(currnode) == 1:
				# if isinstance(currnode[0], dict):	
					# if len(currnode[0].keys()) == 1:
						# testobj = currnode[0][currnode[0].keys()[0]]
						# if isinstance(testobj, list) and len(testobj) > 1:
							# currnode = testobj
		
			try:
				currid = int(currid)
			except ValueError:
				pass
				
			try:
				
				if not isinstance(outobj_node, list):
					# outobj_node.append([])
					# outobj_node = outobj_node[-1]
				# else:					
					outobj_node[currid] = []
					outobj_node = outobj_node[currid]

			except:
				print(f"currid: {currid} type: {type(currid)}, len:{len(outobj_node)}")
				pp.pprint(currnode)
				pp.pprint(outobj_node)
				raise

			if dostack:
				for ei, el in reversed(list(enumerate(currnode))):
					tree_path_list.append(ei)
					stack.append([newlevel, str(ei), el, outobj_node, tree_path_list])
					if listaumelemento:
						break
			
		elif isinstance(currnode, dict):

			oktogo = False
			if currid != '--raiz--' \
					and not currid in configobj['atributos_a_ignorar']:
						
				okprefix_suffix = True
				
				for attrprf in configobj['prefixos_de_atributo_a_ignorar']:
					if currid.startswith(attrprf):
						okprefix_suffix = False
						break

				if okprefix_suffix:
					for attrsfx in configobj['sufixos_de_atributo_a_ignorar']:
						if currid.endswith(attrsfx):
							okprefix_suffix = False
							break
						
				if okprefix_suffix:
					oktogo = True
						
			if oktogo:
										
				if isinstance(outobj_node, list):
					outobj_node.append({})
					outobj_node = outobj_node[-1]
				else:	
					outobj_node[currid] = {}
					outobj_node = outobj_node[currid]
					
			if dostack:
				kl = list(currnode.keys())
				kl.reverse()
				for key in kl:	
					if len(kl) == 1 and isinstance(currnode[key], list):
						for ei, el in reversed(list(enumerate(currnode[key]))):
							tree_path_list.append(ei)
							stack.append([newlevel, str(ei), el, outobj_node, tree_path_list])
							if listaumelemento:
								break
					else:
						tree_path_list.append(key)		
						stack.append([newlevel, key, currnode[key], outobj_node, tree_path_list])

		else:	

			if extractkey == currid and not extractvalues is None:
				extractvalues.add(currnode)
			
			if not str(currid).strip().startswith('@'):
				if isinstance(outobj_node, list):
					outobj_node.append(currnode)
				elif isinstance(outobj_node, dict):
					outobj_node[currid] = currnode
					
def unique(p_in_path, p_out_path, p_configobj):
	out = {}
	lerstruct(p_in_path, out, p_configobj)
	with open(p_out_path.format(dt.now().isoformat()), 'w') as outfile:
		json.dump(out, outfile, indent=2, ensure_ascii=False)

def full(p_in_path, p_out_path, p_configobj, listaumelemento=False, maxlevel=-1, extractkey=None, extractvalues=None):
	out = {}
	lerstruct(p_in_path, out, p_configobj, listaumelemento=False, maxlevel=maxlevel,  extractkey=extractkey, extractvalues=extractvalues)
	with open(p_out_path.format(dt.now().isoformat()), 'w') as outfile:
		json.dump(out, outfile, indent=2, ensure_ascii=False)
				
# if __name__ == "__main__":
	
	# #unique('Originais/AtividadesXIII.json', 'Atividade013_Struct_{}.json', CONFIGOBJ_ACTIVS)
	
	# #unique('Originais/AtividadeDeputadoXIII.json', 'AtividadeDeputado013_{}.json', CONFIGOBJ_ACTIV_DEPUTADOS)
	
	# #listaparcial('Originais/AtividadesXIII.json', 'AtividadesXIII_amostra.txt', limitcount=1000, maxlevel=6)


	# #full('Originais/AtividadesXIII.json', 'Atividade013_{}.json', CONFIGOBJ_ACTIVS)

	# #full('Originais/AtividadeDeputadoXIII.json', 'AtividadeDeputado013_{}.json', CONFIGOBJ_ACTIV_DEPUTADOS)
	
	# # 20180509 
	# #listaparcial('Originais/20180609/AtividadesXIII.json', 'saidas/20180609/AtividadesXIII_amostra.txt', limitcount=1000, maxlevel=6)
	# #extractvalues = set([])
	# full('Originais/20180609/AtividadesXIII.json', 'saidas/20180609/Atividade013_Struct_{}.json', CONFIGOBJ_ACTIVS, maxlevel=-1)
