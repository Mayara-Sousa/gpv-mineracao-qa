from pytests.support.screenshot_service import ScreenshotService
import time
import os

class OM04Page:

    # **
    # * Mapeamento de elementos
    # **

# elementos tela inicial OM04

# Campos apresentados na tela inicial
    
    @staticmethod
    def loading_page_OM04(page):
        return page.get_by_role("heading", name="Por favor aguarde. Processando...")
  
    @staticmethod
    def campo_modelo_de_bloco(page):
        return page.get_by_text("Modelo de Bloco*:")

    @staticmethod
    def campo_inicio_de_vigencia(page):
        return page.get_by_text("Início de Vigência*:")

    @staticmethod
    def campo_fim_de_vigencia(page):
        return page.get_by_text("Fim de Vigência:")

    @staticmethod
    def campo_bloco(page):
        return page.get_by_role("textbox").nth(3)

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
    def opcao_editar_acoes(page):
        return page.get_by_role("menuitem", name=" Editar").locator("a")

    @staticmethod
    def opcao_excluir_acoes(page):
        return page.get_by_role("menuitem", name=" Excluir").locator("a")


# Campos apresentados ao clicar no botão Adicionar 

    @staticmethod
    def campo_modelo_de_bloco_adic(page):
        return page.locator(".ui-dropdown-label-container > .ng-tns-c24-40")

    @staticmethod
    def campo_bloco_adic(page):
        return page.get_by_text("Bloco*:", exact=True)

    @staticmethod
    def campo_inicio_de_vigencia_adic(page):
        return page.locator("div").filter(has_text=re.compile(r"^Início de Vigência\*: ui-btnui-btn$")).get_by_role("textbox")

    @staticmethod
    def campo_fim_de_vigencia_adic(page):
        return page.locator("div").filter(has_text=re.compile(r"^Fim de Vigência: ui-btnui-btn$")).get_by_role("textbox")

    @staticmethod
    def campo_latitude_adic(page):
        return page.get_by_role("spinbutton").first

    @staticmethod
    def campo_longitude_adic(page):
        return page.get_by_role("spinbutton").nth(1)

    @staticmethod
    def campo_altitude_adic(page):
        return page.get_by_role("spinbutton").nth(2)

    @staticmethod
    def campo_material_adic(page):
        return page.get_by_text("empty")

    @staticmethod
    def botao_salvar_adic(page):
        return page.get_by_role("button", name="Salvar")

    @staticmethod
    def botao_cancelar_adic(page):
        return page.get_by_role("button", name="Cancelar")


# Mensagens e erros na tela

    @staticmethod
    def msg_modelo_de_bloco_obrigatório(page):
        return page.get_by_text("Modelo de Bloco é obrigatório")

    @staticmethod
    def msg_inicio_de_vigencia_obrigatorio(page):
        return page.get_by_text("Início de Vigência é obrigatório")
    
    @staticmethod
    def botao_voltar_excessao_tela(page):
        return page.get_by_role("button", name="Voltar")


  # Abre a página inicial da OM04
    @staticmethod
    def page_OM04(page):
        page.goto(f"{os.environ['URL_OM04']}")

    # aguardando em loop 1 segundo enquanto o campo Modelo de Bloco não estiver visivel na tela
        while not OM04Page.campo_modelo_de_bloco(page).is_visible():
          time.sleep(1)

    # aguardando em loop 1 segundo enquando o popup de loading page estiver visivel na tela
        while OM04Page.loading_page_OM04(page).is_visible():
           time.sleep(1)

    # ao apresentar erro de excessão não tratada na tela esse elemento foi mapeado para clicar no botão voltar 
        if OM04Page.botao_voltar_excessao_tela(page).is_visible() == True:
            OM04Page.botao_voltar_excessao_tela(page).click()
        ScreenshotService.take_screenshot(page)


    # casos de testes
    # Validar componentes e botões da tela OM04
    @staticmethod
    def validar_campos_visiveis_0M04(page):
        assert OM04Page.campo_modelo_de_bloco(page).is_visible() == True
        assert OM04Page.campo_inicio_de_vigencia(page).is_visible() == True
        assert OM04Page.campo_fim_de_vigencia(page).is_visible() == True
        assert OM04Page.campo_bloco(page).is_visible() == True
        assert OM04Page.botao_pesquisar(page).is_visible() == True
        assert OM04Page.botao_limpar(page).is_visible() == True
        assert OM04Page.botao_adicionar(page).is_visible() == True
        assert OM04Page.checkbox_acoes(page).is_visible() == True
        ScreenshotService.take_screenshot(page)

    # Validar campo Modelo de Bloco 
    @staticmethod
    def validar_campo_modelo_de_bloco(page):
        assert OM04Page.campo_modelo_de_bloco(page).is_visible() == True
        OM04Page.campo_modelo_de_bloco(page).click()
        ScreenshotService.take_screenshot(page)



