from pytests.support.screenshot_service import ScreenshotService
import time
import os

class OM03Page:

    # **
    # * Mapeamento de elementos
    # **

# elementos tela inicial OM03

# Campos apresentados na tela inicial 

    @staticmethod
    def loading_page_OM03(page):
        return page.get_by_role("heading", name="Por favor aguarde. Processando...")

    @staticmethod
    def campo_unidade_operacional(page):
        return page.locator(".ui-dropdown-label-container > .ng-tns-c24-9")
    
    @staticmethod
    def campo_equipamento(page):
        return page.locator(".ui-dropdown-label-container > .ng-tns-c24-10")
    
    @staticmethod
    def campo_inicio_da_associacao(page):
        return page.locator("div").filter(has_text=re.compile(r"^Início da associação:ui-btnui-btn$")).get_by_role("textbox")
    
    @staticmethod
    def campo_fim_da_associacao(page):
        return page.locator("div").filter(has_text=re.compile(r"^Fim da associação:ui-btnui-btn$")).get_by_role("textbox")
    
    @staticmethod
    def botao_pesquisar(page):
        return page.get_by_role("button", name="Pesquisar")
    
    @staticmethod
    def botao_limpar(page):
        return page.get_by_role("button", name="Limpar")
    
    @staticmethod
    def botao_adicionar(page):
        return page.get_by_role("button", name="Adicionar")
    
    @staticmethod
    def checkbox_acoes(page):
        return page.get_by_role("button", name="Ações")
    
    @staticmethod
    def acoes_editar(page):
        return page.get_by_role("menuitem", name="Editar").locator("a")
    
    @staticmethod
    def acoes_excluir(page):
        return page.get_by_role("menuitem", name="Excluir").locator("a")
    
    @staticmethod
    def coluna_equipamento_tela_inicial(page):
        return page.get_by_role("cell", name="Equipamento")
    
    @staticmethod
    def coluna_inicio_associacao_tela_inicial(page):
        return  page.get_by_role("cell", name="Início da associação")
    
    @staticmethod
    def coluna_fim_associacao_tela_inicial(page):
        return page.get_by_role("cell", name="Fim da associação")
    
    @staticmethod
    def coluna_bloco_tela_inicial(page):
        return page.get_by_role("cell", name="Bloco")
    
    # elementos mapeados ao clicar no botão de 'Adicionar'
    @staticmethod
    def campo_unidade_op_adicionar(page):
        return page.locator("label").first
    
    @staticmethod
    def campo_equipamento_adicionar(page):
        return page.locator("label").nth(1)
    
    @staticmethod
    def linha_coluna_inicio_da_associacao(page):
        return page.get_by_role("textbox").nth(2)
    
    @staticmethod
    def linha_coluna_fim_da_associacao(page):
        return page.get_by_role("textbox").nth(3)
    
    @staticmethod
    def linha_coluna_bloco(page):
        return page.get_by_role("cell", name="").locator("label")
    
    @staticmethod
    def botao_salvar_edicao_grid(page):
        return page.get_by_role("cell", name=" ").locator("a").first
    
    @staticmethod
    def botao_cancelar_edicao_grid(page):
        return page.get_by_role("cell", name=" ").locator("a").nth(1)
    
    @staticmethod
    def botao_salvar(page):
        return page.get_by_role("button", name="Salvar")
    
    @staticmethod
    def botao_cancelar(page):
        return page.get_by_role("button", name="Cancelar")
    
    @staticmethod
    def mensagem_de_erro_campo_unidade_obrigatório(page):
        return page.get_by_text("Unidade Operacional é obrigatório")
    
    @staticmethod
    def mensagem_de_erro_campo_inicio_da_associação(page):
        return page.get_by_text("Início da associação é obrigatório")
    
    @staticmethod
    def mensagem_de_erro_bloco_obrigatório(page):
        return page.get_by_text("Bloco é obrigatório")
    
    @staticmethod
    def serra_norte_unidade_operacional(page):
        return page.get_by_text("Serra Norte")
    
    @staticmethod
    def equipamento_0902(page):
        return page.get_by_role("option", name="0902")
    
    @staticmethod
    def item_bloco_grid(page):
        return page.get_by_text("595157.097000-9325037.283000-563.271000")
    
    @staticmethod
    def bota_voltar_excessao_tela(page):
        return page.get_by_role("button", name="Voltar")
    

    # Abre a página inicial da OM03
    @staticmethod
    def page_OM03(page):
        page.goto(f"{os.environ['URL_OM03']}")

        # aguardando em loop 1 segundo enquanto o campo Unidade Operacional não estiver visivel na tela
        while not OM03Page.campo_unidade_operacional(page).is_visible():
          time.sleep(1)

        # aguardando em loop 1 segundo enquando o popup de loading page estiver visivel na tela
        while OM03Page.loading_page_OM03(page).is_visible():
           time.sleep(1)

        # ao apresentar erro de excessão não tratada na tela esse elemento foi mapeado para clicar no botão voltar 
        if OM03Page.bota_voltar_excessao_tela(page).is_visible() == True:
            OM03Page.bota_voltar_excessao_tela(page).click()
        ScreenshotService.take_screenshot(page)


    # casos de testes
# Validar componentes e botões da tela OM03
    @staticmethod
    def validar_campos_visiveis_0M03(page):
        assert OM03Page.campo_unidade_operacional(page).is_visible() == True
        assert OM03Page.campo_equipamento(page).is_visible() == True
        assert OM03Page.campo_inicio_da_associacao(page).is_visible() == True
        assert OM03Page.campo_fim_da_associacao(page).is_visible() == True
        assert OM03Page.botao_pesquisar(page).is_visible() == True
        assert OM03Page.botao_limpar(page).is_visible() == True
        assert OM03Page.botao_adicionar(page).is_visible() == True
        assert OM03Page.checkbox_acoes(page).is_visible() == True
        ScreenshotService.take_screenshot(page)

# Validar realizar pesquisa com filtro em branco 
    @staticmethod
    def validar_realizar_pesquisa_com_filtro_em_branco(page):
        assert OM03Page.botao_pesquisar(page).is_visible() == True
        OM03Page.botao_pesquisar(page).click()
        while not OM03Page.mensagem_de_erro_campo_unidade_obrigatório(page).is_visible():
            time.sleep(1)
        ScreenshotService.take_screenshot(page)

# Validar realizar pesquisa com filtros preenchidos
    @staticmethod
    def validar_realizar_pesquisa_com_filtro_preenchido(page):
        assert OM03Page.campo_unidade_operacional(page).is_visible() == True
        OM03Page.campo_unidade_operacional(page).click()
        assert OM03Page.serra_norte_unidade_operacional(page).is_visible() == True
        OM03Page.serra_norte_unidade_operacional(page).click()
        assert OM03Page.botao_pesquisar(page).is_visible() == True
        OM03Page.botao_pesquisar(page).click()
        ScreenshotService.take_screenshot(page)
        #precisa validar no banco de dados 


# Validar colunas apresentadas no Grid após realizar a pesquisa 
    @staticmethod
    def validar_colunas_no_grid_ao_realizar_pesquisa(page):
        assert OM03Page.campo_unidade_operacional(page).is_visible() == True
        OM03Page.campo_unidade_operacional(page).click()
        assert OM03Page.serra_norte_unidade_operacional(page).is_visible() == True
        OM03Page.serra_norte_unidade_operacional(page).click()
        assert OM03Page.botao_pesquisar(page).is_visible() == True
        OM03Page.botao_pesquisar(page).click()
        ScreenshotService.take_screenshot(page)
        assert OM03Page.coluna_equipamento_tela_inicial(page).is_visible() == True
        assert OM03Page.coluna_inicio_associacao_tela_inicial(page).is_visible() == True
        assert OM03Page.coluna_fim_associacao_tela_inicial(page).is_visible() == True
        assert OM03Page.coluna_bloco_tela_inicial(page).is_visible() == True

# Validar botão 'limpar' antes da pesquisa
    @staticmethod
    def validar_botao_limpar_antes_pesquisa(page):
        assert OM03Page.campo_unidade_operacional(page).is_visible() == True
        OM03Page.campo_unidade_operacional(page).click()
        assert OM03Page.serra_norte_unidade_operacional(page).is_visible() == True
        OM03Page.serra_norte_unidade_operacional(page).click()
        ScreenshotService.take_screenshot(page)
        assert OM03Page.botao_limpar(page).is_visible() == True
        OM03Page.botao_limpar(page).click()
        ScreenshotService.take_screenshot(page)

# Validar botão 'limpar' depois da pesquisa
    @staticmethod
    def validar_botao_limpar_depois_da_pesquisa(page):
        assert OM03Page.campo_unidade_operacional(page).is_visible() == True
        OM03Page.campo_unidade_operacional(page).click()
        assert OM03Page.serra_norte_unidade_operacional(page).is_visible() == True
        OM03Page.serra_norte_unidade_operacional(page).click()
        ScreenshotService.take_screenshot(page)
        assert OM03Page.botao_pesquisar(page).is_visible() == True
        OM03Page.botao_pesquisar(page).click()
        ScreenshotService.take_screenshot(page)
        assert OM03Page.botao_limpar(page).is_visible() == True
        OM03Page.botao_limpar(page).click()
        ScreenshotService.take_screenshot(page)

# Validar que campo data não permita inserir data fim menor do que data início 
    @staticmethod
    def validar_campo_data_não_permita_inserir_data_menor_que_inicio(page):
        assert OM03Page.campo_unidade_operacional(page).is_visible() == True
        OM03Page.campo_unidade_operacional(page).click()
        assert OM03Page.serra_norte_unidade_operacional(page).is_visible() == True
        OM03Page.serra_norte_unidade_operacional(page).click()
        assert OM03Page.campo_inicio_da_associacao(page).is_visible() == True
        OM03Page.campo_inicio_da_associacao(page).click()
        OM03Page.campo_inicio_da_associacao(page).fill("01/10/2023")
        assert OM03Page.campo_fim_da_associacao(page).is_visible() == True
        OM03Page.campo_fim_da_associacao(page).fill("01/09/2023")
        ScreenshotService.take_screenshot(page)

# Validar componentes e botões ao clicar em Adicionar na tela 
    @staticmethod
    def validar_componentes_e_botoes_ao_clicar_em_adicionar(page):
        assert OM03Page.botao_adicionar(page).is_visible() == True
        OM03Page.botao_adicionar(page).click()
        assert OM03Page.campo_unidade_op_adicionar(page).is_visible() == True
        assert OM03Page.campo_equipamento_adicionar(page).is_visible() == True
        ScreenshotService.take_screenshot(page)

# Validar campo equipamento sendo habilitado após selecionar uma Unidade Operacional 
    @staticmethod
    def validar_campo_equipamento_habilitado(page):
        assert OM03Page.botao_adicionar(page).is_visible() == True
        OM03Page.botao_adicionar(page).click()
        assert OM03Page.campo_unidade_op_adicionar(page).is_visible() == True
        assert OM03Page.serra_norte_unidade_operacional(page).is_visible() == True
        OM03Page.serra_norte_unidade_operacional(page).click()
        assert OM03Page.campo_equipamento_adicionar(page).is_visible() == True
        OM03Page.campo_equipamento_adicionar(page).click()
        ScreenshotService.take_screenshot(page)

# Validar segundo botão Adicionar 
    @staticmethod
    def validar_segundo_botao_adicionar(page):
        assert OM03Page.botao_adicionar(page).is_visible() == True
        OM03Page.botao_adicionar(page).click()
        assert OM03Page.campo_unidade_op_adicionar(page).is_visible() == True
        assert OM03Page.serra_norte_unidade_operacional(page).is_visible() == True
        OM03Page.serra_norte_unidade_operacional(page).click()
        assert OM03Page.campo_equipamento_adicionar(page).is_visible() == True
        OM03Page.campo_equipamento_adicionar(page).click()
        OM03Page.equipamento_0902(page).click()
        assert OM03Page.botao_adicionar(page).is_visible() == True
        OM03Page.botao_adicionar(page).click()
        assert OM03Page.linha_coluna_inicio_da_associacao(page).is_visible() == True
        assert OM03Page.linha_coluna_fim_da_associacao(page).is_visible() == True
        assert OM03Page.linha_coluna_bloco(page).is_visible() == True
        ScreenshotService.take_screenshot(page)

# Validar clicar em confirmar dentro da linha do Grid sem inserir informações 
    @staticmethod
    def validar_clicar_confirmar_no_grid_sem_inserir_informações(page):
        assert OM03Page.botao_adicionar(page).is_visible() == True
        OM03Page.botao_adicionar(page).click()
        assert OM03Page.campo_unidade_op_adicionar(page).is_visible() == True
        assert OM03Page.serra_norte_unidade_operacional(page).is_visible() == True
        OM03Page.serra_norte_unidade_operacional(page).click()
        assert OM03Page.campo_equipamento_adicionar(page).is_visible() == True
        OM03Page.campo_equipamento_adicionar(page).click()
        OM03Page.equipamento_0902(page).click()
        assert OM03Page.botao_adicionar(page).is_visible() == True
        OM03Page.botao_adicionar(page).click()
        assert OM03Page.linha_coluna_inicio_da_associacao(page).is_visible() == True
        assert OM03Page.linha_coluna_fim_da_associacao(page).is_visible() == True
        assert OM03Page.linha_coluna_bloco(page).is_visible() == True
        assert OM03Page.botao_salvar_edicao_grid(page).is_visible() == True
        OM03Page.botao_salvar_edicao_grid(page).click()
        assert OM03Page.mensagem_de_erro_campo_inicio_da_associação(page).is_visible() == True
        assert OM03Page.mensagem_de_erro_bloco_obrigatório(page).is_visible() == True
        ScreenshotService.take_screenshot(page)

# Validar clicar em confirmar dentro da linha do Grid inserindo informações
    @staticmethod
    def validar_clicar_confirmar_no_grid_com_informações(page):
        assert OM03Page.botao_adicionar(page).is_visible() == True
        OM03Page.botao_adicionar(page).click()
        assert OM03Page.campo_unidade_op_adicionar(page).is_visible() == True
        assert OM03Page.serra_norte_unidade_operacional(page).is_visible() == True
        OM03Page.serra_norte_unidade_operacional(page).click()
        assert OM03Page.campo_equipamento_adicionar(page).is_visible() == True
        OM03Page.campo_equipamento_adicionar(page).click()
        OM03Page.equipamento_0902(page).click()
        assert OM03Page.botao_adicionar(page).is_visible() == True
        OM03Page.botao_adicionar(page).click()
        assert OM03Page.linha_coluna_inicio_da_associacao(page).is_visible() == True
        OM03Page.linha_coluna_inicio_da_associacao(page).click()
        OM03Page.linha_coluna_inicio_da_associacao(page).fill("01/11/2023")
        assert OM03Page.linha_coluna_fim_da_associacao(page).is_visible() == True
        OM03Page.linha_coluna_fim_da_associacao(page).click()
        OM03Page.linha_coluna_fim_da_associacao(page).fill("01/12/2023")
        assert OM03Page.linha_coluna_bloco(page).is_visible() == True 
        OM03Page.linha_coluna_bloco(page).click() 
        assert OM03Page.item_bloco_grid(page).is_visible() == True 
        OM03Page.item_bloco_grid(page).click()
        ScreenshotService.take_screenshot(page)


