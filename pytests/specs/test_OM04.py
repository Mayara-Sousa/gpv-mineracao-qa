from pytests.support.hooks import *
from pytests.pages.OM04_page import OM04Page
from pytests.support.sql_server_service import SqlServeService
from playwright.sync_api import Page
import allure


# Descrição dos testes com pytest
@pytest.mark.OM04
def test_validar_campos_visiveis_0M04(page: Page):
    with allure.step("acessar tela OM04"):
        OM04Page.page_OM04(page)
    with allure.step("Validar campos e botões"):
        OM04Page.validar_campos_visiveis_0M04(page)

@pytest.mark.OM04
def test_validar_campo_modelo_de_bloco(page: Page):
    with allure.step("acessar tela OM04"):
        OM04Page.page_OM04(page)
    with allure.step("Validar campo modelo de bloco"):
        OM04Page.validar_campo_modelo_de_bloco(page)


