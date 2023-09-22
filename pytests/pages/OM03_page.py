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
    def botao_salvar(page):
        return page.get_by_role("button", name="Salvar")
    
    @staticmethod
    def botao_cancelar(page):
        return page.get_by_role("button", name="Cancelar")