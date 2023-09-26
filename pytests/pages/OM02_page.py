from pytests.support.screenshot_service import ScreenshotService
import time
import os

class OM02Page:

    # **
    # * Mapeamento de elementos
    # **

    # elementos tela inicial OM02
    
    # campo instancia de seleção livre
    @staticmethod
    def campo_instancia(page):
        return page.get_by_role("textbox")
    
    @staticmethod
    def botao_adicionar_instancia(page):
        return page.get_by_role("button", name="Adicionar")
    
    @staticmethod
    def opcao_acoes_visualizar(page):
        return page.get_by_role("menuitem", name="Visualizar").locator("a")
    
    @staticmethod
    def opcao_acoes_editar(page):
        return page.get_by_role("menuitem", name="Editar").locator("a")
    
    @staticmethod
    def opcao_acoes_excluir(page):
        return page.get_by_role("menuitem", name="Excluir").locator("a")
    
    @staticmethod
    def botao_pesquisar_0M02(page):
        return page.get_by_role("button", name="Pesquisar")
    
    @staticmethod
    def botao_limpar_pesquisa_OM02(page):
        return page.get_by_role("button", name="Limpar")
    
    @staticmethod
    def coluna_codigo_grid(page):
        return page.get_by_role("cell", name="Código")
    
    @staticmethod
    def coluna_sistema_de_coordenada_grid(page):
        return page.get_by_role("cell", name="Sistema de Coordenada")
    
    @staticmethod
    def loading_page_0M02(page):
        return page.get_by_role("heading", name="Por favor aguarde. Processando...")
    
    @staticmethod
    def item_MMCKS_grid(page):
        return page.get_by_role("cell", name="MMCKS")
    
    @staticmethod
    def item_MMITB_grid(page):
        return page.get_by_role("cell", name="MMITB")
    
    @staticmethod
    def flag_clique_item(page):
        return page.get_by_role("row", name="MMCKS UTM (metros)").locator("p-tablecheckbox span")
    
    @staticmethod
    def flag_clique_item_MMITB(page):
        return page.get_by_role("row", name="MMITB UTM (metros)").locator("p-tablecheckbox span")
    
    @staticmethod
    def check_box_acoes(page):
        return page.get_by_role("button", name="Ações")
    
    @staticmethod
    def loading_page_visualizacao(page):
        return page.locator("#spinner div")
    
    @staticmethod
    def botao_de_exclusao_nao(page):
        return page.get_by_role("button", name="Não")
    
    @staticmethod
    def modal_sim_não(page):
        return page.get_by_text("SimNão")
    
    @staticmethod
    def botao_de_exclusao_sim(page):
        return page.get_by_role("button", name="Sim")
    
    
    #Campos apresentados ao clicar para 'Adicionar' na tela OM02
    @staticmethod
    def campo_sistema_de_despacho(page):
        return page.get_by_role("textbox").first
    
    @staticmethod
    def campo_id_gpvm(page):
        return page.locator("xpath=//div[@class='ui-grid-col-7']//input[@formcontrolname='idGPVM']")

    @staticmethod
    def campo_sistema_de_coordenada(page):
        return page.locator("xpath=//div[@class='ui-grid-col-7']//vale-dropdown[@formcontrolname='codigoSistemaCoordenada']")
    
    @staticmethod
    def item_geografica(page):
        return page.get_by_text("GEOGRÁFICA (Grau Decimal)")
    
    @staticmethod
    def item_utm_metros(page):
        return page.get_by_text("UTM (metros)", exact=True)
    
    @staticmethod
    def item_carajas_utm(page):
        return page.get_by_text("Carajás UTM (metros)")
    
    @staticmethod
    def campo_datum(page):
        return page.locator("xpath=//div[@class='ui-grid-col-7']//vale-dropdown[@formcontrolname='datum']")
    
    @staticmethod
    def item_WGS8_datum(page):
        return page.get_by_role("option", name="WGS84")

    @staticmethod
    def item_SAD69_datum(page):
        return page.get_by_text("SAD 69")

    @staticmethod
    def item_corrego_alegre_datum(page):
        return page.get_by_text("Córrego Alegre")
    
    @staticmethod
    def item_astro_chua_datum_datum(page):
        return page.get_by_text("Astro-Chuá")
    
    @staticmethod
    def item_SIRGAS2000_datum(page):
        return page.get_by_text("SIRGAS2000")  
    
    @staticmethod
    def campo_zona_UTM(page):
        return page.get_by_text("Zona UTM*:")

    @staticmethod
    def campo_hemisferio(page):
        return page.get_by_text("Hemisfério*:")
    
    @staticmethod
    def campo_offset_x(page):
        return page.get_by_text("Offset X*:")
    
    @staticmethod
    def campo_offset_y(page):
        return page.get_by_text("Offset Y*:")
    
    @staticmethod
    def botao_salvar_ao_adicionar(page):
        return page.get_by_role("button", name="Salvar")
    
    @staticmethod
    def campo_obrigatório_sistema_de_despacho(page):
        return page.get_by_text("Sistema de Despacho é obrigatório")

    @staticmethod
    def campo_obrigatório_id_gpvm(page):
        return page.get_by_text("Id GPVM é obrigatório")

    @staticmethod
    def campo_obrigatório_sistema_de_coordenada(page):
        return page.get_by_text("Sistema de Coordenada é obrigatório")

    @staticmethod
    def campo_obrigatório_datum(page):
        return page.get_by_text("Datum é obrigatório")
    
    @staticmethod
    def mensagem_de_erro_campos(page):
        return page.locator("p-messages div")
    
    @staticmethod
    def botao_cancelar(page):
        return page.get_by_role("button", name="Cancelar")
    
    @staticmethod
    def mensagem_de_salvo_com_sucesso(page):
        return page.get_by_text("Salvo com sucesso")

    @staticmethod
    def botao_voltar_excessao_tela(page):
        return page.get_by_role("button", name="Voltar")

                                
 # Abre a página inicial da OM02
    @staticmethod
    def page_OM02(page):
        page.goto(f"{os.environ['URL_OM02']}")

        # aguardando em loop 1 segundo enquanto o campo instancia não estiver visivel na tela
        while not OM02Page.campo_instancia(page).is_visible():
          time.sleep(1)

        # aguardando em loop 1 segundo enquando o popup de loading page estiver visivel na tela
        while OM02Page.loading_page_0M02(page).is_visible():
           time.sleep(1)

        # ao apresentar erro de excessão não tratada na tela esse elemento foi mapeado para clicar no botão voltar 
        if OM02Page.botao_voltar_excessao_tela(page).is_visible() == True:
            OM02Page.botao_voltar_excessao_tela(page).click()
        ScreenshotService.take_screenshot(page)

    # Validar componentes e botões da tela OM02
    @staticmethod
    def validar_campos_visiveis_0M02(page):
        assert OM02Page.campo_instancia(page).is_visible() == True
        assert OM02Page.botao_pesquisar_0M02(page).is_visible() == True
        assert OM02Page.campo_instancia(page).is_visible() == True
        assert OM02Page.botao_pesquisar_0M02(page).is_visible() == True
        assert OM02Page.botao_limpar_pesquisa_OM02(page).is_visible() == True
        assert OM02Page.botao_adicionar_instancia(page).is_visible() == True
        assert OM02Page.check_box_acoes(page).is_visible() == True
        ScreenshotService.take_screenshot(page)

    
# Validar realizar pesquisa com filtro em branco 
    @staticmethod
    def validar_realizar_pesquisa_com_filtro_em_branco(page):
        assert OM02Page.botao_pesquisar_0M02(page).is_visible() == True
        OM02Page.botao_pesquisar_0M02(page).click()
        while not OM02Page.item_MMCKS_grid(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)


# Validar realizar pesquisa inserindo parte do nome de uma instância já cadastrada
    @staticmethod
    def validar_realizar_pesquisa_preenchido_filtro_instancia(page):
        assert OM02Page.campo_instancia(page).is_visible() == True
        OM02Page.campo_instancia(page).click()
        OM02Page.campo_instancia(page).fill("MMC")
        OM02Page.botao_pesquisar_0M02(page).click()
        while not OM02Page.item_MMCKS_grid(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)

    
# Validar botão 'limpar' antes da pesquisa 
    @staticmethod
    def validar_limpar_filtro_antes_pesquisa(page):
        assert OM02Page.campo_instancia(page).is_visible() == True
        OM02Page.campo_instancia(page).click()
        OM02Page.campo_instancia(page).fill("MMC")
        ScreenshotService.take_screenshot(page)
        assert OM02Page.botao_limpar_pesquisa_OM02(page).is_visible() == True
        OM02Page.botao_limpar_pesquisa_OM02(page).click()
        ScreenshotService.take_screenshot(page)

    
# Validar botão 'limpar' depois da pesquisa
    @staticmethod
    def validar_limpar_filtro_depois_pesquisa(page):
        assert OM02Page.campo_instancia(page).is_visible() == True
        OM02Page.campo_instancia(page).click()
        OM02Page.campo_instancia(page).fill("MMI")
        OM02Page.botao_pesquisar_0M02(page).click()
        while not OM02Page.item_MMITB_grid(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM02Page.botao_limpar_pesquisa_OM02(page).is_visible() == True
        OM02Page.botao_limpar_pesquisa_OM02(page).click()
        ScreenshotService.take_screenshot(page)


# Validar campos apresentados ao clicar em Adicionar na tela 
    @staticmethod
    def validar_clicar_adicionar_tela(page):
        assert OM02Page.botao_adicionar_instancia(page).is_visible() == True
        OM02Page.botao_adicionar_instancia(page).click()
        while OM02Page.loading_page_visualizacao(page).is_visible():
           time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM02Page.campo_sistema_de_despacho(page).is_visible() == True
        assert OM02Page.campo_id_gpvm(page).is_visible() == True
        assert OM02Page.campo_sistema_de_coordenada(page).is_visible() == True
        assert OM02Page.campo_datum(page).is_visible() == True


# Validar campo Sistema de Despacho 
    @staticmethod
    def validar_campo_sistema_de_despacho(page):
        assert OM02Page.botao_adicionar_instancia(page).is_visible() == True
        OM02Page.botao_adicionar_instancia(page).click()
        while not OM02Page.campo_sistema_de_despacho(page).is_visible():
            time.sleep(1)
        assert OM02Page.campo_sistema_de_despacho(page).is_visible() == True
        OM02Page.campo_sistema_de_despacho(page).click()
        OM02Page.campo_sistema_de_despacho(page).fill("TESTE AUT")
        ScreenshotService.take_screenshot(page)


# Validar campo ID GPVM
    @staticmethod
    def validar_campo_id_gpvm(page):
        assert OM02Page.botao_adicionar_instancia(page).is_visible() == True
        OM02Page.botao_adicionar_instancia(page).click()
        while not OM02Page.campo_id_gpvm(page).is_visible():
            time.sleep(1)
        assert OM02Page.campo_id_gpvm(page).is_visible() == True
        OM02Page.campo_id_gpvm(page).click()
        OM02Page.campo_id_gpvm(page).fill("123456")
        ScreenshotService.take_screenshot(page)


# Validar clicar em Salvar sem preencher nenhum campo 
    @staticmethod
    def validar_clicar_para_salvar_sem_preencher_campo(page):
        assert OM02Page.botao_adicionar_instancia(page).is_visible() == True
        OM02Page.botao_adicionar_instancia(page).click()
        while not OM02Page.campo_sistema_de_despacho(page).is_visible():
            time.sleep(1)
        assert OM02Page.botao_salvar_ao_adicionar(page).is_visible() == True
        OM02Page.botao_salvar_ao_adicionar(page).click()
        while not OM02Page.mensagem_de_erro_campos(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)    
        assert OM02Page.mensagem_de_erro_campos(page).is_visible() == True
        assert OM02Page.mensagem_de_erro_campos(page).text_content() == "Sistema de Despacho é obrigatórioId GPVM é obrigatórioSistema de Coordenada é obrigatórioDatum é obrigatório"

   
# Validar clicar no botão cancelar sem preencher nenhum campo 
    @staticmethod
    def validar_clicar_para_cancelar_sem_preencher_campos(page):
        assert OM02Page.botao_adicionar_instancia(page).is_visible() == True
        OM02Page.botao_adicionar_instancia(page).click()
        while not OM02Page.campo_sistema_de_despacho(page).is_visible():
            time.sleep(1)   
        ScreenshotService.take_screenshot(page) 
        assert OM02Page.botao_cancelar(page).is_visible() == True
        OM02Page.botao_cancelar(page).click()
        ScreenshotService.take_screenshot(page)    


# Validar botão Ação- Visualizar
    @staticmethod
    def validar_sub_menu_visualizar(page):
        assert OM02Page.campo_instancia(page).is_visible() == True
        assert OM02Page.botao_pesquisar_0M02(page).is_visible() == True
        OM02Page.botao_pesquisar_0M02(page).click()
        while not OM02Page.item_MMCKS_grid(page).is_visible():
           time.sleep(1)
        assert OM02Page.item_MMCKS_grid(page).is_visible() == True
        OM02Page.flag_clique_item(page).click()
        ScreenshotService.take_screenshot(page)  
        assert OM02Page.check_box_acoes(page).is_visible() == True
        OM02Page.check_box_acoes(page).click()
        assert OM02Page.opcao_acoes_visualizar(page).is_visible() == True
        ScreenshotService.take_screenshot(page)
        OM02Page.opcao_acoes_visualizar(page).click()
        while OM02Page.loading_page_visualizacao(page).is_visible():
           time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM02Page.campo_sistema_de_despacho(page).is_visible() == True
        assert OM02Page.campo_sistema_de_despacho(page).is_visible() == True
        assert OM02Page.campo_id_gpvm(page).is_visible() == True
        assert OM02Page.campo_sistema_de_coordenada(page).is_visible() == True
        assert OM02Page.campo_datum(page).is_visible() == True
        assert OM02Page.campo_zona_UTM(page).is_visible() == True
        assert OM02Page.campo_hemisferio(page).is_visible() == True
        assert OM02Page.campo_offset_x(page).is_visible() == True
        assert OM02Page.campo_offset_y(page).is_visible() == True
        assert OM02Page.botao_cancelar(page).is_visible() == True


# Validar botão Ação- Editar
    @staticmethod
    def validar_sub_menu_editar(page):
        assert OM02Page.campo_instancia(page).is_visible() == True
        assert OM02Page.botao_pesquisar_0M02(page).is_visible() == True
        OM02Page.botao_pesquisar_0M02(page).click()
        while not OM02Page.item_MMCKS_grid(page).is_visible():
           time.sleep(1)
        assert OM02Page.item_MMCKS_grid(page).is_visible() == True
        OM02Page.flag_clique_item(page).click()
        ScreenshotService.take_screenshot(page)  
        assert OM02Page.check_box_acoes(page).is_visible() == True
        OM02Page.check_box_acoes(page).click()
        assert OM02Page.opcao_acoes_editar(page).is_visible() == True
        ScreenshotService.take_screenshot(page)
        OM02Page.opcao_acoes_editar(page).click()
        while OM02Page.loading_page_visualizacao(page).is_visible():
           time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM02Page.campo_sistema_de_despacho(page).is_visible() == True
        assert OM02Page.campo_id_gpvm(page).is_visible() == True
        assert OM02Page.campo_sistema_de_coordenada(page).is_visible() == True
        assert OM02Page.campo_datum(page).is_visible() == True
        assert OM02Page.campo_zona_UTM(page).is_visible() == True
        assert OM02Page.campo_hemisferio(page).is_visible() == True
        assert OM02Page.campo_offset_x(page).is_visible() == True
        assert OM02Page.campo_offset_y(page).is_visible() == True
        assert OM02Page.botao_cancelar(page).is_visible() == True


# Validar realizar uma edição e salvar 
    @staticmethod
    def validar_realizar_edicao_e_salvar(page):
        assert OM02Page.campo_instancia(page).is_visible() == True
        assert OM02Page.botao_pesquisar_0M02(page).is_visible() == True
        OM02Page.botao_pesquisar_0M02(page).click()
        while not OM02Page.item_MMCKS_grid(page).is_visible():
           time.sleep(1)
        assert OM02Page.item_MMCKS_grid(page).is_visible() == True
        OM02Page.flag_clique_item(page).click()
        ScreenshotService.take_screenshot(page)  
        assert OM02Page.check_box_acoes(page).is_visible() == True
        OM02Page.check_box_acoes(page).click()
        assert OM02Page.opcao_acoes_editar(page).is_visible() == True
        ScreenshotService.take_screenshot(page)
        OM02Page.opcao_acoes_editar(page).click()
        while OM02Page.loading_page_visualizacao(page).is_visible():
           time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM02Page.campo_id_gpvm(page).is_visible() == True
        OM02Page.campo_id_gpvm(page).click()
        OM02Page.campo_id_gpvm(page).fill("200")
        ScreenshotService.take_screenshot(page)
        assert OM02Page.botao_salvar_ao_adicionar(page).is_visible() == True
        OM02Page.botao_salvar_ao_adicionar(page).click()

    @staticmethod
    def validar_edicao_salva(page):
        while not OM02Page.mensagem_de_salvo_com_sucesso(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM02Page.mensagem_de_salvo_com_sucesso(page).text_content() == "Salvo com sucesso"

# Validar realizar uma edição e clicar em cancelar
    @staticmethod
    def validar_realizar_edicao_e_cancelar(page):
        assert OM02Page.campo_instancia(page).is_visible() == True
        assert OM02Page.botao_pesquisar_0M02(page).is_visible() == True
        OM02Page.botao_pesquisar_0M02(page).click()
        while not OM02Page.item_MMCKS_grid(page).is_visible():
           time.sleep(1)
        assert OM02Page.item_MMCKS_grid(page).is_visible() == True
        OM02Page.flag_clique_item(page).click()
        ScreenshotService.take_screenshot(page)  
        assert OM02Page.check_box_acoes(page).is_visible() == True
        OM02Page.check_box_acoes(page).click()
        assert OM02Page.opcao_acoes_editar(page).is_visible() == True
        ScreenshotService.take_screenshot(page)
        OM02Page.opcao_acoes_editar(page).click()
        while OM02Page.loading_page_visualizacao(page).is_visible():
           time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM02Page.campo_id_gpvm(page).is_visible() == True
        OM02Page.campo_id_gpvm(page).click()
        OM02Page.campo_id_gpvm(page).fill("456")
        ScreenshotService.take_screenshot(page)
        assert OM02Page.botao_cancelar(page).is_visible() == True
        OM02Page.botao_cancelar(page).click()
        ScreenshotService.take_screenshot(page)


# Validar botão Ação- Excluir clicando em NÃO 
    @staticmethod
    def validar_clicar_nao_para_excluir(page):
        assert OM02Page.campo_instancia(page).is_visible() == True
        assert OM02Page.botao_pesquisar_0M02(page).is_visible() == True
        OM02Page.botao_pesquisar_0M02(page).click()
        while not OM02Page.item_MMITB_grid(page).is_visible():
           time.sleep(1)
        assert OM02Page.item_MMITB_grid(page).is_visible() == True
        OM02Page.flag_clique_item_MMITB(page).click()
        ScreenshotService.take_screenshot(page)  
        assert OM02Page.check_box_acoes(page).is_visible() == True
        OM02Page.check_box_acoes(page).click()
        OM02Page.opcao_acoes_excluir(page).click()
        ScreenshotService.take_screenshot(page)
        assert OM02Page.modal_sim_não(page).is_visible() == True
        OM02Page.botao_de_exclusao_nao(page).click()
        ScreenshotService.take_screenshot(page)


# Validar clicar no botão cancelar preenchendo todos os campos obrigatórios
    @staticmethod
    def validar_clicar_para_cancelar_com_todos_os_campos_preenchidos(page):
        assert OM02Page.campo_instancia(page).is_visible() == True
        assert OM02Page.botao_adicionar_instancia(page).is_visible() == True
        OM02Page.botao_adicionar_instancia(page).click()
        while not OM02Page.campo_sistema_de_despacho(page).is_visible():
            time.sleep(1)   
        ScreenshotService.take_screenshot(page) 
        OM02Page.campo_sistema_de_despacho(page).click()
        OM02Page.campo_sistema_de_despacho(page).fill("TESTE AUT 2")
        assert OM02Page.campo_id_gpvm(page).is_visible() == True
        OM02Page.campo_id_gpvm(page).click()
        OM02Page.campo_id_gpvm(page).fill("2000")
        assert OM02Page.campo_sistema_de_coordenada(page).is_visible() == True
        OM02Page.campo_sistema_de_coordenada(page).click()
        assert OM02Page.item_geografica(page).is_visible() == True
        OM02Page.item_geografica(page).click()
        assert OM02Page.campo_datum(page).is_visible() == True
        OM02Page.campo_datum(page).click()
        assert OM02Page.item_SIRGAS2000_datum(page).is_visible() == True
        OM02Page.item_SIRGAS2000_datum(page).click()
        ScreenshotService.take_screenshot(page)
        assert OM02Page.botao_cancelar(page).is_visible() == True
        OM02Page.botao_cancelar(page).click()
        ScreenshotService.take_screenshot(page)

# Validar campo Sistema de Coordenada
    @staticmethod
    def validar_campo_sistema_de_coordenada(page):
        assert OM02Page.botao_adicionar_instancia(page).is_visible() == True
        OM02Page.botao_adicionar_instancia(page).click()
        while not OM02Page.campo_sistema_de_coordenada(page).is_visible():
            time.sleep(1)
        OM02Page.campo_sistema_de_coordenada(page).click()
        OM02Page.item_geografica(page).click()
        ScreenshotService.take_screenshot(page)

# Validar campo Datum 
    @staticmethod
    def validar_campo_datum(page):
        assert OM02Page.botao_adicionar_instancia(page).is_visible() == True
        OM02Page.botao_adicionar_instancia(page).click()
        while not OM02Page.campo_datum(page).is_visible():
            time.sleep(1)
        assert OM02Page.campo_datum(page).is_visible() == True
        OM02Page.campo_datum(page).click()
        assert OM02Page.item_SIRGAS2000_datum(page).is_visible() == True
        OM02Page.item_SIRGAS2000_datum(page).click()
        ScreenshotService.take_screenshot(page)
        
# Validar clicar em salvar preenchendo todos os campos obrigatórios
    @staticmethod
    def validar_clicar_para_salvar_com_todos_os_campos_preenchidos(page):
        assert OM02Page.campo_instancia(page).is_visible() == True
        assert OM02Page.botao_adicionar_instancia(page).is_visible() == True
        OM02Page.botao_adicionar_instancia(page).click()
        while not OM02Page.campo_sistema_de_despacho(page).is_visible():
            time.sleep(1)   
        ScreenshotService.take_screenshot(page) 
        OM02Page.campo_sistema_de_despacho(page).click()
        OM02Page.campo_sistema_de_despacho(page).fill("TESTE AUT 3")
        assert OM02Page.campo_id_gpvm(page).is_visible() == True
        OM02Page.campo_id_gpvm(page).click()
        OM02Page.campo_id_gpvm(page).fill("3000")
        assert OM02Page.campo_sistema_de_coordenada(page).is_visible() == True
        OM02Page.campo_sistema_de_coordenada(page).click()
        assert OM02Page.item_geografica(page).is_visible() == True
        OM02Page.item_geografica(page).click()
        assert OM02Page.campo_datum(page).is_visible() == True
        OM02Page.campo_datum(page).click()
        assert OM02Page.item_SAD69_datum(page).is_visible() == True
        OM02Page.item_SAD69_datum(page).click()
        ScreenshotService.take_screenshot(page)
        assert OM02Page.botao_salvar_ao_adicionar(page).is_visible() == True
        OM02Page.botao_salvar_ao_adicionar(page).click()

    @staticmethod
    def validar_salvo_com_sucesso(page):
        while not OM02Page.mensagem_de_salvo_com_sucesso(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM02Page.mensagem_de_salvo_com_sucesso(page).text_content() == "Salvo com sucesso"
        ScreenshotService.take_screenshot(page)


# Validar opções apresentadas ao selecionar no campo Sistema de Coordenada as opções UTM (metros) ou Carajás UTM (metros)
    @staticmethod
    def validar_mais_campos_apresentados_ao_selecionar_outro_sistema_coordenada(page):
        assert OM02Page.campo_instancia(page).is_visible() == True
        assert OM02Page.botao_adicionar_instancia(page).is_visible() == True
        OM02Page.botao_adicionar_instancia(page).click()
        while not OM02Page.campo_sistema_de_despacho(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)
        assert OM02Page.campo_sistema_de_coordenada(page).is_visible() == True
        OM02Page.campo_sistema_de_coordenada(page).click()
        assert OM02Page.item_utm_metros(page).is_visible() == True
        OM02Page.item_utm_metros(page).click()
        ScreenshotService.take_screenshot(page)
        assert OM02Page.campo_zona_UTM(page).is_visible() == True
        assert OM02Page.campo_hemisferio(page).is_visible() == True
        assert OM02Page.campo_offset_x(page).is_visible() == True
        assert OM02Page.campo_offset_y(page).is_visible() == True


# Validar botão Ação- Excluir clicando em SIM 
    @staticmethod
    def validar_clicar_sim_para_excluir(page):
        assert OM02Page.campo_instancia(page).is_visible() == True
        assert OM02Page.botao_pesquisar_0M02(page).is_visible() == True
        OM02Page.botao_pesquisar_0M02(page).click()
        while not OM02Page.item_MMITB_grid(page).is_visible():
           time.sleep(1)
        assert OM02Page.item_MMITB_grid(page).is_visible() == True
        OM02Page.flag_clique_item_MMITB(page).click()
        ScreenshotService.take_screenshot(page)  
        assert OM02Page.check_box_acoes(page).is_visible() == True
        OM02Page.check_box_acoes(page).click()
        OM02Page.opcao_acoes_excluir(page).click()
        ScreenshotService.take_screenshot(page)
        assert OM02Page.modal_sim_não(page).is_visible() == True
        OM02Page.botao_de_exclusao_sim(page).click()
        ScreenshotService.take_screenshot(page)

    @staticmethod
    def validar_adicionar_item_MMITB(page):
        assert OM02Page.campo_instancia(page).is_visible() == True
        assert OM02Page.botao_adicionar_instancia(page).is_visible() == True
        OM02Page.botao_adicionar_instancia(page).click()
        while not OM02Page.campo_sistema_de_despacho(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page) 
        OM02Page.campo_sistema_de_despacho(page).click()
        OM02Page.campo_sistema_de_despacho(page).fill("MMITB")
        assert OM02Page.campo_id_gpvm(page).is_visible() == True
        OM02Page.campo_id_gpvm(page).click()
        OM02Page.campo_id_gpvm(page).fill("95")
        assert OM02Page.campo_sistema_de_coordenada(page).is_visible() == True
        OM02Page.campo_sistema_de_coordenada(page).click()
        assert OM02Page.item_geografica(page).is_visible() == True
        OM02Page.item_geografica(page).click()
        assert OM02Page.campo_datum(page).is_visible() == True
        OM02Page.campo_datum(page).click()
        assert OM02Page.item_SAD69_datum(page).is_visible() == True
        OM02Page.item_SAD69_datum(page).click()
        ScreenshotService.take_screenshot(page)
        assert OM02Page.botao_salvar_ao_adicionar(page).is_visible() == True
        OM02Page.botao_salvar_ao_adicionar(page).click()

         
    



