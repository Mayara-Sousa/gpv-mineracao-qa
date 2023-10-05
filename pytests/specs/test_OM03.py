from pytests.support.hooks import *
from pytests.pages.OM03_page import OM03Page
from pytests.support.sql_server_service import SqlServeService
from playwright.sync_api import Page
import allure


# Descrição dos testes com pytest
@pytest.mark.OM03
def test_validar_campos_visiveis_0M03(page: Page):
    with allure.step("acessar tela OM03"):
        OM03Page.page_OM03(page)
    with allure.step("Validar campos e botões"):
        OM03Page.validar_campos_visiveis_0M03(page)

@pytest.mark.OM03
def test_validar_realizar_pesquisa_com_filtro_em_branco(page: Page):
    with allure.step("acessar tela OM03"):
        OM03Page.page_OM03(page)
    with allure.step("Validar realizar pesquisa com filtro em branco"):
        OM03Page.validar_realizar_pesquisa_com_filtro_em_branco(page)

@pytest.mark.OM03
def test_validar_realizar_pesquisa_com_filtro_preenchido(page: Page):
    with allure.step("acessar tela OM03"):
        OM03Page.page_OM03(page)
    with allure.step("Validar realizar pesquisa com filtro preenchido"):
        OM03Page.validar_realizar_pesquisa_com_filtro_preenchido(page)
        SqlServeService.connection_sql()

@pytest.mark.OM03
def test_validar_colunas_apresentadas_no_grid_ao_realizar_pesquisa(page: Page):
    with allure.step("acessar tela OM03"):
        OM03Page.page_OM03(page)
    with allure.step("Validar colunas apresentadas no grid ao realizar pesquisa"):
        OM03Page.validar_colunas_no_grid_ao_realizar_pesquisa(page)

@pytest.mark.OM03
def test_validar_botao_limpar_antes_da_pesquisa(page: Page):
    with allure.step("acessar tela OM03"):
        OM03Page.page_OM03(page)
    with allure.step("Validar botao limpar antes da pesquisa"):
        OM03Page.validar_botao_limpar_antes_pesquisa(page)

@pytest.mark.OM03
def test_validar_botao_limpar_depois_da_pesquisa(page: Page):
    with allure.step("acessar tela OM03"):
        OM03Page.page_OM03(page)
    with allure.step("Validar botao limpar depois da pesquisa"):
        OM03Page.validar_botao_limpar_depois_da_pesquisa(page)

