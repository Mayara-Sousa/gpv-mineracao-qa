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
def 