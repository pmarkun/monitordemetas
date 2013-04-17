# Monitor de Metas :: Specs

Especificação do sistema do Monitor de Metas.

## Funcionalidades

* Plano de Metas
	* Área de abrangência
	* Data Início
	* Data Fim
	* Responsável
		* Nome
		* Email
* Meta
	* Número
	* Descrição
	* Tipo
		* Quantitativa
		* Qualitativa
		* Espacial ?
	* Métrica
		* Bool (true or false) (versionado)
		* Quantitativa (quantidade / unidade / item)  (versionado)
	* Espacial (opcional)
		* Lat/Lng (ponto)
		* GeoJSON

* Cadastro de usuários-monitores para cada meta
	* Nome
	* Bio
	* Email
	* Metas monitoradas
	* Configuração de alertas
* Sistema de upload de arquivos relativos as metas
	* Título
	* Arquivo
	* Descrição
	* Categoria: Notícia, Legislação, Biblioteca
	* Somente os usuário-monitores podem fazer upload
	* É possível editar (atualizar) ou deletar uploads feitos
* Sistema de inclusão de links relativos as metas
	* Título
	* Url
	* Descrição
	* Categoria: Notícia, Legislação, Biblioteca
	* Somente os usuário-monitores podem incluir links
	* É possível editar (atualizar) ou deletar links
* Sistema de comentários
	* Autor
	* Email (não fica vísivel)
	* Comentário
	* reCaptcha (não necessario para monitores-usuários)
	* Resposta ao comentário->id (threaded)
	* Os comentários funcionam em thread
	* Os comentários podem incluir sintaxe simplificada markdown, incluindo urls.
	* Qualquer pessoa pode incluir comentário
* Sistema de alertas para metas
	* Envia um reminder de x em x dias (configurável por usuário) lembrando de atualizar informação sobre as metas