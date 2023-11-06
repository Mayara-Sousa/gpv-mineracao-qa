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

@pytest.mark.OM03
def test_validar_campo_data_não_permita_inserir_data_menor_que_inicio(page: Page):
    with allure.step("acessar tela OM03"):
        OM03Page.page_OM03(page)
    with allure.step("Validar que campo data não permita inserir data fim menor do que data início"):
        OM03Page.validar_campo_data_não_permita_inserir_data_menor_que_inicio(page)

@pytest.mark.OM03
def test_validar_componentes_e_botoes_ao_clicar_em_adicionar(page: Page):
    with allure.step("acessar tela OM03"):
        OM03Page.page_OM03(page)
    with allure.step("Validar componentes e botões ao clicar em Adicionar na tela"):
        OM03Page.validar_componentes_e_botoes_ao_clicar_em_adicionar(page)

@pytest.mark.OM03
def test_validar_campo_equipamento_habilitado(page: Page):
     with allure.step("acessar tela OM03"):
        OM03Page.page_OM03(page)
     with allure.step("Validar campo equipamento sendo habilitado após selecionar uma Unidade Operacional"):
        OM03Page.validar_campo_equipamento_habilitado(page)

@pytest.mark.OM03
def test_validar_segundo_botao_adicionar(page: Page):
     with allure.step("acessar tela OM03"):
        OM03Page.page_OM03(page)
     with allure.step("Validar segundo botao adicionar"):
        OM03Page.validar_segundo_botao_adicionar(page)

@pytest.mark.OM03
def test_validar_clicar_confirmar_no_grid_sem_inserir_informações(page: Page):
     with allure.step("acessar tela OM03"):
        OM03Page.page_OM03(page)
     with allure.step("Validar clicar em confirmar dentro da linha do Grid sem inserir informações"):
        OM03Page.validar_clicar_confirmar_no_grid_sem_inserir_informações(page)

@pytest.mark.OM03
def test_validar_clicar_confirmar_no_grid_com_informações(page: Page):
     with allure.step("acessar tela OM03"):
        OM03Page.page_OM03(page)
     with allure.step("Validar clicar em confirmar dentro da linha do Grid inserindo informações"):
        OM03Page.validar_clicar_confirmar_no_grid_com_informações(page)