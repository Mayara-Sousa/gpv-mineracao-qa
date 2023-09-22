from pytests.support.screenshot_service import ScreenshotService
from pytests.pages.OM02_page import OM02Page
import time
import os

class OM01Page:

    # **
    # * Mapeamento de elementos
    # **

    # elementos unidade operacional

    @staticmethod
    def campo_unidade_operacional(page):
        return page.locator("vale-dropdown label")
    
    @staticmethod
    def item_alegria(page):
        return page.get_by_role("option", name="Alegria")
    
    @staticmethod
    def item_capao_xavier(page):
        return page.get_by_role("option", name="Capão Xavier")
    
    @staticmethod
    def item_caue(page):
        return page.get_by_role("option", name="Cauê")
    
    @staticmethod
    def item_conceicao_1(page):
        return page.get_by_text("Conceição I", exact=True)
    
    @staticmethod
    def item_conceicao_2(page):
        return page.get_by_text("Conceição II")
    
    @staticmethod
    def item_fabrica_nova(page):
        #return page.get_by_text("Fábrica Nova")
        return page.get_by_role("option", name="Fábrica Nova").get_by_text("Fábrica Nova")
    
    @staticmethod
    def item_fazendao(page):
        return  page.get_by_role("option", name="Fazendão")
    
    @staticmethod
    def item_mutuca(page):
        return page.get_by_role("option", name="Mutuca")
    
    @staticmethod
    def item_salobo(page):
        return page.get_by_role("option", name="Salobo")
    
    @staticmethod
    def item_serra_norte(page):
        return page.get_by_text("Serra Norte")
    
    @staticmethod
    def item_serra_sul(page):
        return page.get_by_role("option", name="Serra Sul")
    
    @staticmethod
    def item_timbopeba(page):
        return page.get_by_role("option", name="Timbopeba")
    
    @staticmethod
    def item_viga(page):
        return page.get_by_role("option", name="Viga")
    

    # elementos gerais da tela 
    
    @staticmethod
    def botao_acoes(page):
        return page.get_by_role("button", name="Ações")
    
    # botão de Ação na tela principal que apresenta os submenus abaixo
    @staticmethod
    def check_box_acoes(page):
        return page.locator("p-tablecheckbox span")
    
    # submenu apresentado ao clicar no botão ações 
    @staticmethod
    def campo_adicionar_destino_referencia(page):
        return page.get_by_role("menuitem", name=" Adicionar Destino de Referência")
    
    
    #botão apresentado na tela inicial para realizar a pesquisa
    @staticmethod
    def botao_pesquisar(page):
        return page.get_by_role("button", name="Pesquisar")
    
    #botao apresentado na tela inicial para limpar a pesquisa
    @staticmethod
    def botao_limpar(page):
        return page.get_by_role("button", name="Limpar")
    
    # quando a tela está carregando
    @staticmethod
    def loading_page(page):
        return page.get_by_role("heading", name="Por favor aguarde. Processando...")
    
   
    # elementos grid
    # Unidades Operacionais apresentadas conforme escolhida
    @staticmethod
    def grid_alegria(page):
        return page.get_by_role("cell", name="Alegria").get_by_text("Alegria")
    
    @staticmethod
    def grid_capao_xavier(page):
        return page.get_by_role("cell", name="Capão Xavier").get_by_text("Capão Xavier")
    
    @staticmethod
    def grid_caue(page):
        return page.get_by_role("cell", name="Cauê").get_by_text("Cauê")
    
    @staticmethod
    def grid_conceicao_1(page):
        return page.get_by_role("cell", name="Conceição I").get_by_text("Conceição I")
    
    @staticmethod
    def grid_conceicao_2(page):
        return page.get_by_role("cell", name="Conceição II").get_by_text("Conceição II")
    
    @staticmethod
    def grid_fabrica_nova(page):
        return page.get_by_role("cell", name="Fábrica Nova").get_by_text("Fábrica Nova")

    @staticmethod
    def grid_fazendao(page):
        return page.get_by_role("cell", name="Fazendão")
    
    @staticmethod
    def grid_mutuca(page):
        return page.get_by_role("row", name="Mutuca").get_by_text("Mutuca")
    
    @staticmethod
    def grid_salobo(page):
        return page.get_by_role("row", name="Salobo").get_by_text("Salobo")
    
    @staticmethod
    def grid_serra_norte(page):
        return page.get_by_role("cell", name="Serra Norte").get_by_text("Serra Norte")
    
    @staticmethod
    def grid_serra_sul(page):
        return page.get_by_role("cell", name="Serra Sul").get_by_text("Serra Sul")
    
    @staticmethod
    def grid_timbopeba(page):
        return page.get_by_role("cell", name="Timbopeba").get_by_text("Timbopeba")
    
    @staticmethod
    def grid_viga(page):
        return page.get_by_role("cell", name="Viga").get_by_text("Viga")
    
    
    # Elementos apresentados ao escolher a opção 'Adicionar Destino de Referência' no submenu

    # primeira coluna apresentada TIPO DE DESTINO 
    @staticmethod
    def visualização_coluna_tipo_destino(page):
        return page.get_by_role("cell", name="Tipo de destino")

     # segunda coluna apresentada DESTINO 
    @staticmethod
    def visualização_coluna_destino(page):
        return page.locator("xpath=//div[@class='ui-table-scrollable-header-box']//th[contains(text(),' Destino ')]")

    # terceira coluna apresentada NOME
    @staticmethod
    def visualização_coluna_nome(page):
        return page.get_by_role("cell", name="Nome")
    
    # botão cancelar para retornar a tela principal 
    @staticmethod
    def botao_cancelar_tela(page):
        return page.get_by_role("button", name="Cancelar")
    
    # botão salvar a operação realizada 
    @staticmethod
    def botao_salvar_tela(page):
        return page.get_by_role("button", name="Salvar")
    
    #botão dentro da grid para editar um registro existente 
    @staticmethod
    def botao_editar(page, item):
        return page.locator(f"xpath=//div[@class='ui-table-scrollable-view']//span[contains(text(),'SNP170029')]//i[@title='editar']")
    
    #botão dentro da grid para excluir um registro existente 
    @staticmethod
    def botao_excluir(page, item):
        return page.get_by_role("row", name=item).get_by_role("cell", name="").locator("a")
                                                                                                                   
    # opção apresentada após clicar no botão excluir - não exclui o registro
    @staticmethod
    def excluir_nao(page):
        return page.get_by_role("button", name="Não")
    
    # opção apresentada após clicar no botão excluir - exclui o registro 
    @staticmethod
    def excluir_sim(page):
        return page.get_by_role("button", name="Sim")

    # elementos apresentados ao clicar no botão Adicionar na opção 'Adicionar Destino de Referência' no submenu 

    # botão para clicar '+Adicionar'
    @staticmethod
    def botao_adicionar(page):
        return page.get_by_role("button", name="Adicionar")
    
    # linha vazia apresentada na coluna TIPO DE DESTINO 
    @staticmethod
    def linha_coluna_tipo_destino(page):
        return page.locator("label").nth(2)
    
    # opções apresentada para preencher na coluna TIPO DE DESTINO
    @staticmethod
    def item_frente_de_lavra(page):
        return page.get_by_role("cell", name="Frente de lavra Frente de lavra ").locator("span")
    
    @staticmethod
    def item_pilha(page):
        return page.get_by_role("option", name="Pilha")
    
    @staticmethod
    def item_lote(page):
        return page.get_by_role("cell", name="Lote Lote ").locator("span")
    
    @staticmethod
    def item_sub_processo(page):
        return page.get_by_role("cell", name="Sub processo Sub processo ").locator("span")
    
    @staticmethod
    def item_area_de_patio(page):
        return page.get_by_role("option", name="Área de pátio")
    
    # linha apresentada na coluna DESTINO 
    @staticmethod
    def linha_coluna_destino(page):
        return page.get_by_role("cell", name="", exact=True).locator("label")
    
    # opção apresentada para preencher na coluna DESTINO
    @staticmethod
    def item_coluna_destino(page, item):
        return page.get_by_role("option", name=item)
    
    # linha apresentada na coluna NOME 
    @staticmethod
    def linha_coluna_nome(page):
        return page.get_by_role("textbox").nth(2)
    
    # botão apresentado somente quando a linha de adicionar/editar estiver habilitada 
    @staticmethod
    def botao_cancelar_edicao_linha_grid(page):
        return page.get_by_role("cell", name=" ").locator("a").nth(1)
    
    # botão apresentado somente quando a linha de adicionar/editar estiver habilitada 
    @staticmethod
    def botao_salvar_edicao_linha_grid(page):
        return page.locator("xpath=//div[@class='ui-table-scrollable-wrapper ng-star-inserted']//i[@title='salvar']")
    
    # mensagem apresentada ao salvar a edição/adição do item na grid
    @staticmethod
    def mensagem_de_salvo_com_sucesso(page):
        return page.get_by_text("Salvo com sucesso")
    
    @staticmethod
    def mensagem_nome_registro_duplicado(page, nome):
        return page.get_by_text(f"O nome {nome} já é utilizado em outra Unidade Operacional")
    
    # elementos modal de exclusão 

    @staticmethod
    def modal_sim_nao(page):
        return page.get_by_text("SimNão")
    
    # elementos apresentados ao clicar em Ações>Adicionar Equipamento 
    
    # submenu apresentado ao clicar no botão ações 
    @staticmethod
    def campo_adicionar_equipamentos(page):
        return page.get_by_role("menuitem", name=" Adicionar Equipamentos")
    
    #colunas apresentadas ao entrar na tela 
    @staticmethod
    def visualizacao_coluna_equipamento(page):
        return page.get_by_role("cell", name="Equipamento")
    
    @staticmethod
    def visualizacao_coluna_associacao(page):
        return page.get_by_role("cell", name="Associação")
    
    @staticmethod
    def botao_editar_equipamento_precisao(page, item):
        return page.get_by_role("row", name=item).locator("a")
    
    @staticmethod
    def associacao_manual(page):
        return page.get_by_role("option", name="Manual")
    
    @staticmethod
    def associacao_alta_precisao(page):
        return page.get_by_role("option", name="Alta precisão")
    
    @staticmethod
    def associacao_baixa_precisao(page):
        return page.get_by_role("option", name="Baixa precisão").get_by_text("Baixa precisão")

    @staticmethod
    def botao_selecao_equipamentos(page, nome_associacao):
        return page.get_by_role("option", name=nome_associacao)
    
    # elementos ao clicar no botão pesquisar sem preencher o campo 
    
    @staticmethod
    def grid_inicial_aboboras(page):
        return page.get_by_text("Abóboras")
    
    @staticmethod
    def grid_inicial_agua_limpa(page):
        return page.get_by_text("Água Limpa")
    
    @staticmethod
    def grid_inicial_alegria(page):
        return page.get_by_text("Alegria")
    
    @staticmethod
    def grid_inicial_brucutu(page):
        return page.get_by_text("Brucutu")
    
    @staticmethod
    def grid_inicial_capao_xavier(page):
        return page.get_by_text("Capão Xavier")
    
    @staticmethod
    def grid_inicial_capitao_do_mato(page):
        return page.get_by_text("Capitão do Mato")
    
    @staticmethod
    def grid_inicial_caue(page):
        return page.get_by_text("Cauê")
    
    @staticmethod
    def grid_inicial_conceicao_1(page):
        return page.get_by_text("Conceição I", exact=True)
    
    @staticmethod
    def grid_inicial_conceicao_2(page):
        return page.get_by_text("Conceição II")
    
    @staticmethod
    def grid_inicial_corrego_do_feijao(page):
        return page.get_by_text("Córrego do Feijão")
    
    @staticmethod
    def grid_inicial_fabrica(page):
        return page.get_by_text("Fábrica", exact=True)
    
    @staticmethod
    def grid_inicial_fabrica_nova(page):
        return page.get_by_text("Fábrica Nova")
    
    @staticmethod
    def grid_inicial_fazendao(page):
        return page.get_by_text("Fazendão")
        
    @staticmethod
    def grid_inicial_jangada(page):
        return page.get_by_text("Jangada")
     
    @staticmethod
    def grid_inicial_mar_azul(page):
        return page.get_by_text("Mar Azul")

    @staticmethod
    def table_header_check_box(page):
        return page.locator("p-tableheadercheckbox span")
    
    @staticmethod
    def botao_abrir_selecao_equipamento(page, select_name):
        return page.get_by_role("cell", name=select_name).locator("label")
    
    # **
    # * Métodos e Funções
    # **

    # abre a página inicial da OM01
    @staticmethod
    def page_OM01(page):
        page.goto(f"{os.environ['URL_OM01']}")

        # aguardando em loop 1 segundo enquanto o campo UO não estiver visivel na tela
        while not OM01Page.campo_unidade_operacional(page).is_visible():
            time.sleep(1)

        # aguardando em loop 1 segundo enquando o popup de loading page estiver visivel na tela
        while OM01Page.loading_page(page).is_visible():
            time.sleep(1)
        
        # ao apresentar erro de excessão não tratada na tela esse elemento foi mapeado para clicar no botão voltar 
        if OM02Page.botao_voltar_excessao_tela(page).is_visible() == True:
            OM02Page.botao_voltar_excessao_tela(page).click()
        ScreenshotService.take_screenshot(page)
        
    # unico campo unidade operacional aparece visivel na tela 
    @staticmethod
    def validar_campos_visiveis(page):
        OM01Page.campo_unidade_operacional(page).click()
        ScreenshotService.take_screenshot(page)
        assert OM01Page.item_alegria(page).is_visible() == True
        assert OM01Page.item_capao_xavier(page).is_visible() == True
        assert OM01Page.item_caue(page).is_visible() == True
        assert OM01Page.item_conceicao_1(page).is_visible() == True
        assert OM01Page.item_conceicao_2(page).is_visible() == True
        assert OM01Page.item_fabrica_nova(page).is_visible() == True
        assert OM01Page.item_fazendao(page).is_visible() == True
        assert OM01Page.item_mutuca(page).is_visible() == True
        assert OM01Page.item_salobo(page).is_visible() == True
        assert OM01Page.item_serra_norte(page).is_visible() == True
        assert OM01Page.item_serra_sul(page).is_visible() == True
        assert OM01Page.item_timbopeba(page).is_visible() == True
        assert OM01Page.item_viga(page).is_visible() == True
        assert OM01Page.botao_pesquisar(page).is_visible() == True
        assert OM01Page.botao_limpar(page).is_visible() == True
        assert OM01Page.botao_acoes(page).is_visible() == True        

    # quando selecionado uma UO a mesma deve ser apresentada no grid para seleção 
    @staticmethod
    def validar_campos_grid(page):
        OM01Page.campo_unidade_operacional(page).click()
        OM01Page.item_alegria(page).click()
        OM01Page.botao_pesquisar(page).click()

        # aguardando em loop 1 segundo enquanto a grid alegria não estiver visivel na tela
        while not OM01Page.grid_alegria(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM01Page.grid_alegria(page).is_visible() == True

        OM01Page.botao_limpar
        OM01Page.campo_unidade_operacional(page).click()
        OM01Page.item_capao_xavier(page).click()
        OM01Page.botao_pesquisar(page).click()
        while not OM01Page.grid_capao_xavier(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM01Page.grid_capao_xavier(page).is_visible() == True

        OM01Page.botao_limpar
        OM01Page.campo_unidade_operacional(page).click()
        OM01Page.item_caue(page).click()
        OM01Page.botao_pesquisar(page).click()
        while not OM01Page.grid_caue(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM01Page.grid_caue(page).is_visible() == True

        OM01Page.botao_limpar
        OM01Page.campo_unidade_operacional(page).click()
        OM01Page.item_conceicao_1(page).click()
        OM01Page.botao_pesquisar(page).click()
        while not OM01Page.grid_conceicao_1(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM01Page.grid_conceicao_1(page).is_visible() == True

        OM01Page.botao_limpar
        OM01Page.campo_unidade_operacional(page).click()
        OM01Page.item_conceicao_2(page).click()
        OM01Page.botao_pesquisar(page).click()
        while not OM01Page.grid_conceicao_2(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM01Page.grid_conceicao_2(page).is_visible() == True  

        OM01Page.botao_limpar
        OM01Page.campo_unidade_operacional(page).click()
        OM01Page.item_fabrica_nova(page).click()
        OM01Page.botao_pesquisar(page).click()
        while not OM01Page.grid_fabrica_nova(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM01Page.grid_fabrica_nova(page).is_visible() == True

        OM01Page.botao_limpar
        OM01Page.campo_unidade_operacional(page).click()
        OM01Page.item_fazendao(page).click()
        OM01Page.botao_pesquisar(page).click()
        while not OM01Page.grid_fazendao(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM01Page.grid_fazendao(page).is_visible() == True

        OM01Page.botao_limpar
        OM01Page.campo_unidade_operacional(page).click()
        OM01Page.item_mutuca(page).click()
        OM01Page.botao_pesquisar(page).click()
        while not OM01Page.grid_mutuca(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM01Page.grid_mutuca(page).is_visible() == True

        OM01Page.botao_limpar
        OM01Page.campo_unidade_operacional(page).click()
        OM01Page.item_salobo(page).click()
        OM01Page.botao_pesquisar(page).click()
        while not OM01Page.grid_salobo(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM01Page.grid_salobo(page).is_visible() == True

        OM01Page.botao_limpar
        OM01Page.campo_unidade_operacional(page).click()
        OM01Page.item_serra_norte(page).click()
        OM01Page.botao_pesquisar(page).click()
        while not OM01Page.grid_serra_norte(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM01Page.grid_serra_norte(page).is_visible() == True

        OM01Page.botao_limpar
        OM01Page.campo_unidade_operacional(page).click()
        OM01Page.item_serra_sul(page).click()
        OM01Page.botao_pesquisar(page).click()
        while not OM01Page.grid_serra_sul(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM01Page.grid_serra_sul(page).is_visible() == True

        OM01Page.botao_limpar
        OM01Page.campo_unidade_operacional(page).click()
        OM01Page.item_timbopeba(page).click()
        OM01Page.botao_pesquisar(page).click()
        while not OM01Page.grid_timbopeba(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM01Page.grid_timbopeba(page).is_visible() == True

        OM01Page.botao_limpar
        OM01Page.campo_unidade_operacional(page).click()
        OM01Page.item_viga(page).click()
        OM01Page.botao_pesquisar(page).click()
        while not OM01Page.grid_viga(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM01Page.grid_viga(page).is_visible() == True

    @staticmethod
    def inserir_unidade_operacional(page):
        OM01Page.campo_unidade_operacional(page).click()
        OM01Page.item_serra_norte(page).click()
        ScreenshotService.take_screenshot(page)
        OM01Page.botao_pesquisar(page).click()
        while not OM01Page.grid_serra_norte(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
    
    @staticmethod
    def validar_botao_limpar(page):
        OM01Page.campo_unidade_operacional(page).click()
        OM01Page.item_alegria(page).click()
        ScreenshotService.take_screenshot(page)
        OM01Page.botao_limpar(page).click()
        while OM01Page.item_alegria(page).is_visible():
            time.sleep(1)
        assert OM01Page.item_alegria(page).is_visible() == False
        ScreenshotService.take_screenshot(page)
    
    @staticmethod
    def validar_botao_limpar_depois_pesquisa(page):
        OM01Page.campo_unidade_operacional(page).click()
        OM01Page.item_capao_xavier(page).click()
        ScreenshotService.take_screenshot(page)
        OM01Page.botao_pesquisar(page).click()
        while not OM01Page.grid_capao_xavier(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        OM01Page.botao_limpar(page).click()
        while OM01Page.item_capao_xavier(page).is_visible():
            time.sleep(1)
        assert OM01Page.item_capao_xavier(page).is_visible() == False
        assert OM01Page.grid_capao_xavier(page).is_visible() == False
        ScreenshotService.take_screenshot(page)
    
    @staticmethod
    def validar_conteudo_acoes_adicionar_destino_referencia(page):
        OM01Page.check_box_acoes(page).click()
        ScreenshotService.take_screenshot(page)
        OM01Page.botao_acoes(page).click()
        ScreenshotService.take_screenshot(page)
        OM01Page.campo_adicionar_destino_referencia(page).click()
        while OM01Page.loading_page(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM01Page.botao_adicionar(page).is_visible() == True
        assert OM01Page.visualização_coluna_tipo_destino(page).is_visible() == True
        assert OM01Page.visualização_coluna_destino(page).is_visible() == True
        assert OM01Page.visualização_coluna_nome(page).is_visible() == True
        assert OM01Page.botao_cancelar_tela(page).is_visible() == True
        assert OM01Page.botao_salvar_tela(page).is_visible() == True

    @staticmethod
    def adicionar_destino_referencia(page, item):
        OM01Page.check_box_acoes(page).click()
        OM01Page.botao_acoes(page).click()
        ScreenshotService.take_screenshot(page)
        OM01Page.campo_adicionar_destino_referencia(page).click()
        while OM01Page.loading_page(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)

        assert OM01Page.botao_adicionar(page).is_visible() == True
        OM01Page.botao_adicionar(page).click()
        assert OM01Page.visualização_coluna_tipo_destino(page).is_visible() == True
        assert OM01Page.visualização_coluna_destino(page).is_visible() == True
        assert OM01Page.visualização_coluna_nome(page).is_visible() == True
        ScreenshotService.take_screenshot(page)

        OM01Page.linha_coluna_tipo_destino(page).click()
        OM01Page.item_pilha(page).click()
        OM01Page.linha_coluna_destino(page).click()
        OM01Page.item_coluna_destino(page, item).click()
        OM01Page.linha_coluna_nome(page).fill("teste automacao")
        ScreenshotService.take_screenshot(page)
        OM01Page.botao_salvar_edicao_linha_grid(page).click()
        OM01Page.botao_salvar_tela(page).click()

    @staticmethod
    def remover_destino_referencia(page, item):
        OM01Page.check_box_acoes(page).click()
        OM01Page.botao_acoes(page).click()
        ScreenshotService.take_screenshot(page)
        OM01Page.campo_adicionar_destino_referencia(page).click()
        while OM01Page.loading_page(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        OM01Page.botao_excluir(page, item).click()
        ScreenshotService.take_screenshot(page)
        OM01Page.excluir_sim(page).click()
        OM01Page.botao_salvar_tela(page).click()
        
    @staticmethod
    def validar_destino_salvo(page):
        while not OM01Page.mensagem_de_salvo_com_sucesso(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM01Page.mensagem_de_salvo_com_sucesso(page).text_content() == "Salvo com sucesso"


    # @staticmethod
    # def validar_editar_destino_existente(page, item, nome):
    #     OM01Page.check_box_acoes(page).click()
    #     ScreenshotService.take_screenshot(page)
    #     OM01Page.botao_acoes(page).click()
    #     ScreenshotService.take_screenshot(page)
    #     OM01Page.campo_adicionar_destino_referencia(page).click()
    #     while OM01Page.loading_page(page).is_visible():
    #         time.sleep(1)
    #     ScreenshotService.take_screenshot(page)
    #     assert OM01Page.botao_adicionar(page).is_visible() == True
    #     OM01Page.botao_editar(page, item).click()
    #     ScreenshotService.take_screenshot(page)
    #     assert OM01Page.visualização_coluna_nome(page).is_visible() == True
    #     assert OM01Page.linha_coluna_nome(page).fill(nome)
    #     ScreenshotService.take_screenshot(page)
    #     OM01Page.botao_salvar_edicao_linha_grid(page).click()
    #     OM01Page.botao_salvar_tela(page).click()

    # @staticmethod
    # def validar_destino_editado_com_sucesso(page):
    #     while not OM01Page.mensagem_de_salvo_com_sucesso(page).is_visible():
    #         time.sleep(1)
    #     ScreenshotService.take_screenshot(page)
    #     assert OM01Page.mensagem_de_salvo_com_sucesso(page).text_content() == "Salvo com sucesso"

        # testes novos

    @staticmethod
    def validar_clicar_nao_para_excluir(page, item):
        OM01Page.check_box_acoes(page).click()
        OM01Page.botao_acoes(page).click()
        ScreenshotService.take_screenshot(page)
        OM01Page.campo_adicionar_destino_referencia(page).click()
        while OM01Page.loading_page(page).is_visible():
            time.sleep(1)
        assert OM01Page.botao_adicionar(page).is_visible() == True
        OM01Page.botao_excluir(page, item).click()
        ScreenshotService.take_screenshot(page)
        assert OM01Page.modal_sim_nao(page).is_visible() == True
        OM01Page.excluir_nao(page).click()
        ScreenshotService.take_screenshot(page)


    @staticmethod
    def validar_cancelar_cadastro_destino_referencia(page, item, nome):
        OM01Page.campo_unidade_operacional(page).click()
        OM01Page.item_capao_xavier(page).click()
        OM01Page.botao_pesquisar(page).click()
        while not OM01Page.grid_capao_xavier(page).is_visible():
            time.sleep(1)
            ScreenshotService.take_screenshot(page)
        OM01Page.check_box_acoes(page).click()
        OM01Page.botao_acoes(page).click()
        ScreenshotService.take_screenshot(page)
        OM01Page.campo_adicionar_destino_referencia(page).click()
        while OM01Page.loading_page(page).is_visible():
            time.sleep(1)
        assert OM01Page.botao_adicionar(page).is_visible() == True
        OM01Page.botao_adicionar(page).click()
        assert OM01Page.visualização_coluna_tipo_destino(page).is_visible() == True
        assert OM01Page.visualização_coluna_destino(page).is_visible() == True
        assert OM01Page.visualização_coluna_nome(page).is_visible() == True
        ScreenshotService.take_screenshot(page)
        OM01Page.linha_coluna_tipo_destino(page).click()
        OM01Page.item_pilha(page).click()
        OM01Page.linha_coluna_destino(page).click()
        OM01Page.item_coluna_destino(page, item).click()
        OM01Page.linha_coluna_nome(page).fill(nome)
        ScreenshotService.take_screenshot(page)
        OM01Page.botao_cancelar_edicao_linha_grid(page).click()
        ScreenshotService.take_screenshot(page)


    @staticmethod
    def validar_conteudo_acoes_adicionar_equipamento(page, item):
        OM01Page.campo_unidade_operacional(page).click()
        OM01Page.item_capao_xavier(page).click()
        OM01Page.botao_pesquisar(page).click()
        while not OM01Page.grid_capao_xavier(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        OM01Page.check_box_acoes(page).click()
        OM01Page.botao_acoes(page).click()
        ScreenshotService.take_screenshot(page)
        OM01Page.campo_adicionar_equipamentos(page).click()
        while OM01Page.loading_page(page).is_visible():
            time.sleep(1)
        assert OM01Page.visualizacao_coluna_equipamento(page).is_visible() == True
        assert OM01Page.visualizacao_coluna_associacao(page).is_visible() == True
        assert OM01Page.botao_cancelar_tela(page).is_visible() == True
        assert OM01Page.botao_salvar_tela(page).is_visible() == True
        assert OM01Page.botao_editar_equipamento_precisao(page, item).is_visible() == True
        ScreenshotService.take_screenshot(page)
 
    @staticmethod
    def validar_editar_equipamento_cadastrado(page, item, nome_associacao, item_selecao):
        OM01Page.campo_unidade_operacional(page).click()
        OM01Page.item_fabrica_nova(page).click()
        OM01Page.botao_pesquisar(page).click()
        while not OM01Page.grid_fabrica_nova(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        OM01Page.check_box_acoes(page).click()
        OM01Page.botao_acoes(page).click()
        ScreenshotService.take_screenshot(page)
        OM01Page.campo_adicionar_equipamentos(page).click()
        while OM01Page.loading_page(page).is_visible():
            time.sleep(1)
        assert OM01Page.visualizacao_coluna_associacao(page).is_visible() == True
        OM01Page.botao_editar_equipamento_precisao(page, item).click()
        OM01Page.botao_abrir_selecao_equipamento(page, item_selecao).click()
        OM01Page.botao_selecao_equipamentos(page, nome_associacao).click()
        ScreenshotService.take_screenshot(page)
        OM01Page.botao_salvar_edicao_linha_grid(page).click()
        OM01Page.botao_salvar_tela(page).click()
        ScreenshotService.take_screenshot(page)

    @staticmethod
    def validar_realizar_pesquisa_filtro_em_branco(page):
        assert OM01Page.campo_unidade_operacional(page).is_visible() == True
        OM01Page.botao_pesquisar(page).click()
        while OM01Page.loading_page(page).is_visible():
            time.sleep(1)
        assert OM01Page.grid_inicial_aboboras(page).is_visible() == True
        assert OM01Page.grid_inicial_agua_limpa(page).is_visible() == True
        assert OM01Page.grid_inicial_alegria(page).is_visible() == True
        assert OM01Page.grid_inicial_brucutu(page).is_visible() == True
        assert OM01Page.grid_inicial_capao_xavier(page).is_visible() == True
        assert OM01Page.grid_inicial_capitao_do_mato(page).is_visible() == True
        assert OM01Page.grid_inicial_caue(page).is_visible() == True
        assert OM01Page.grid_inicial_conceicao_1(page).is_visible() == True
        assert OM01Page.grid_inicial_conceicao_2(page).is_visible() == True
        assert OM01Page.grid_inicial_corrego_do_feijao(page).is_visible() == True
        assert OM01Page.grid_inicial_fabrica(page).is_visible() == True
        assert OM01Page.grid_inicial_fabrica_nova(page).is_visible() == True
        assert OM01Page.grid_inicial_fazendao(page).is_visible() == True
        assert OM01Page.grid_inicial_jangada(page).is_visible() == True
        assert OM01Page.grid_inicial_mar_azul(page).is_visible() == True
        assert OM01Page.table_header_check_box(page).is_visible() == True
        ScreenshotService.take_screenshot(page)
    
    
    @staticmethod
    def validar_cancelar_edicao_equipamento_cadastrado(page, item, nome_associacao):
        OM01Page.campo_unidade_operacional(page).click()
        OM01Page.item_alegria(page).click()
        OM01Page.botao_pesquisar(page).click()
        while not OM01Page.item_alegria(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        OM01Page.check_box_acoes(page).click()
        OM01Page.botao_acoes(page).click()
        ScreenshotService.take_screenshot(page)
        OM01Page.campo_adicionar_equipamentos(page).click()
        while OM01Page.loading_page(page).is_visible():
            time.sleep(1)
        assert OM01Page.visualizacao_coluna_associacao(page).is_visible() == True
        OM01Page.botao_editar_equipamento_precisao(page, item).click()
        OM01Page.botao_abrir_selecao_equipamento(page, nome_associacao).click()
        ScreenshotService.take_screenshot(page)
        OM01Page.associacao_alta_precisao(page).click()
        ScreenshotService.take_screenshot(page)
        OM01Page.botao_cancelar_edicao_linha_grid(page).click()
        ScreenshotService.take_screenshot(page)


    @staticmethod
    def validar_utilizar_nome_para_outra_unidade_operacional(page, item, nome):
        OM01Page.campo_unidade_operacional(page).click()
        OM01Page.item_alegria(page).click()
        OM01Page.botao_pesquisar(page).click()
        while not OM01Page.grid_alegria(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        OM01Page.check_box_acoes(page).click()
        OM01Page.botao_acoes(page).click()
        ScreenshotService.take_screenshot(page)
        OM01Page.campo_adicionar_destino_referencia(page).click()
        while OM01Page.loading_page(page).is_visible():
            time.sleep(1)
        assert OM01Page.visualização_coluna_tipo_destino(page).is_visible() == True
        assert OM01Page.visualização_coluna_destino(page).is_visible() == True
        assert OM01Page.visualização_coluna_nome(page).is_visible() == True
        ScreenshotService.take_screenshot(page)
        assert OM01Page.botao_adicionar(page).is_visible() == True
        OM01Page.botao_adicionar(page).click()
        OM01Page.linha_coluna_tipo_destino(page).click()
        OM01Page.item_pilha(page).click()
        OM01Page.linha_coluna_destino(page).click()
        OM01Page.item_coluna_destino(page, item).click()
        OM01Page.linha_coluna_nome(page).fill(nome)
        ScreenshotService.take_screenshot(page)
        OM01Page.botao_salvar_edicao_linha_grid(page).click()
        while not OM01Page.mensagem_nome_registro_duplicado(page, nome).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM01Page.mensagem_nome_registro_duplicado(page, nome).text_content() == f"O nome {nome} já é utilizado em outra Unidade Operacional"



