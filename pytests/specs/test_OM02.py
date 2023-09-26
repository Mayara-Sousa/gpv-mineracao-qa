from pytests.support.hooks import *
from pytests.pages.OM02_page import OM02Page
from playwright.sync_api import Page
import allure


# Descrição dos testes com pytest
@pytest.mark.OM02
def test_validar_campos_visiveis_0M02(page: Page):
    with allure.step("acessar tela OM02"):
        OM02Page.page_OM02(page)
    with allure.step("Validar campos e botões"):
        OM02Page.validar_campos_visiveis_0M02(page)

@pytest.mark.OM02
def test_validar_realizar_pesquisa_com_filtro_em_branco(page: Page):
    with allure.step("acessar tela OM02"):
        OM02Page.page_OM02(page)
    with allure.step("Validar clicar no botão pesquisar com filtro em branco"):
        OM02Page.validar_realizar_pesquisa_com_filtro_em_branco(page)

@pytest.mark.OM02
def test_validar_realizar_pesquisa_preenchido_filtro_instancia(page: Page):
    with allure.step("acessar tela OM02"):
        OM02Page.page_OM02(page)
    with allure.step("Validar clicar no botão pesquisar com filtro preenchido"):
        OM02Page.validar_realizar_pesquisa_preenchido_filtro_instancia(page)

@pytest.mark.OM02
def test_validar_limpar_filtro_antes_pesquisa(page: Page):
    with allure.step("acessar tela OM02"):
        OM02Page.page_OM02(page)
    with allure.step("Validar limpar filtro antes de realizar pesquisa"):
        OM02Page.validar_limpar_filtro_antes_pesquisa(page)

@pytest.mark.OM02
def test_validar_limpar_filtro_depois_pesquisa(page: Page):
    with allure.step("acessar tela OM02"):
        OM02Page.page_OM02(page)
    with allure.step("Validar limpar filtro depois de realizar pesquisa"):
        OM02Page.validar_limpar_filtro_depois_pesquisa(page)

#cenário com erro
@pytest.mark.OM02
def test_validar_clicar_adicionar_tela(page: Page):
    with allure.step("acessar tela OM02"):
        OM02Page.page_OM02(page)
    with allure.step("Validar campos apresentados ao clicar no botão adicionar"):
        OM02Page.validar_clicar_adicionar_tela(page)

@pytest.mark.OM02
def test_validar_campo_sistema_de_despacho(page: Page):
    with allure.step("acessar tela OM02"):
        OM02Page.page_OM02(page)
    with allure.step("Validar campo sistema de despacho"):
        OM02Page.validar_campo_sistema_de_despacho(page)

@pytest.mark.OM02
def test_validar_campo_id_gpvm(page: Page):
    with allure.step("acessar tela OM02"):
        OM02Page.page_OM02(page)
    with allure.step("Validar campo ID GPVM"):
        OM02Page.validar_campo_id_gpvm(page)

@pytest.mark.OM02
def test_validar_clicar_para_salvar_sem_preencher_campo(page: Page):
    with allure.step("acessar tela OM02"):
        OM02Page.page_OM02(page)
    with allure.step("Validar clicar em salvar sem preencher os campos"):
        OM02Page.validar_clicar_para_salvar_sem_preencher_campo(page)

@pytest.mark.OM02
def test_validar_clicar_para_cancelar_sem_preencher_campos(page: Page):
    with allure.step("acessar tela OM02"):
        OM02Page.page_OM02(page)
    with allure.step("Validar clicar em cancelar sem preencher os campos"):
        OM02Page.validar_clicar_para_cancelar_sem_preencher_campos(page)

@pytest.mark.OM02
def test_validar_sub_menu_visualizar(page: Page):
    with allure.step("acessar tela OM02"):
        OM02Page.page_OM02(page)
    with allure.step("Validar botão de visualização do item"):
        OM02Page.validar_sub_menu_visualizar(page)

@pytest.mark.OM02
def test_validar_sub_menu_editar(page: Page):
    with allure.step("acessar tela OM02"):
        OM02Page.page_OM02(page)
    with allure.step("Validar botão de edição do item"):
        OM02Page.validar_sub_menu_editar(page)

@pytest.mark.OM02
def test_validar_realizar_edicao_e_salvar(page: Page):
    with allure.step("acessar tela OM02"):
        OM02Page.page_OM02(page)
    with allure.step("Validar realizar edição e salvar"):
        OM02Page.validar_realizar_edicao_e_salvar(page)
    
@pytest.mark.OM02
def test_validar_realizar_edicao_e_cancelar(page: Page):
    with allure.step("acessar tela OM02"):
        OM02Page.page_OM02(page)
    with allure.step("Validar realizar edição e cancelar"):
        OM02Page.validar_realizar_edicao_e_cancelar(page)

@pytest.mark.OM02
def test_validar_clicar_nao_para_excluir(page: Page):
    with allure.step("acessar tela OM02"):
        OM02Page.page_OM02(page)
    with allure.step("Validar clicar em não na mensagem de excluir"):
        OM02Page.validar_clicar_nao_para_excluir(page)

@pytest.mark.OM02
def test_validar_clicar_para_cancelar_com_todos_os_campos_preenchidos(page: Page):
    with allure.step("acessar tela OM02"):
        OM02Page.page_OM02(page)
    with allure.step("Validar clicar para cancelar com todos os campos preenchidos"):
        OM02Page.validar_clicar_para_cancelar_com_todos_os_campos_preenchidos(page)

@pytest.mark.OM02
def test_validar_campo_sistema_de_coordenada(page: Page):
    with allure.step("acessar tela OM02"):
        OM02Page.page_OM02(page)
    with allure.step("Validar campo sistema de coordenada"):
        OM02Page.validar_campo_sistema_de_coordenada(page)

@pytest.mark.OM02
def test_validar_campo_datum(page: Page):
    with allure.step("acessar tela OM02"):
        OM02Page.page_OM02(page)
    with allure.step("Validar campo datum"):
        OM02Page.validar_campo_datum(page)

@pytest.mark.OM02
def test_validar_clicar_para_salvar_com_todos_os_campos_preenchidos(page: Page):
    with allure.step("acessar tela OM02"):
        OM02Page.page_OM02(page)
    with allure.step("Validar clicar para salvar com todos os campos preenchidos"):
        OM02Page.validar_clicar_para_salvar_com_todos_os_campos_preenchidos(page)
        OM02Page.validar_salvo_com_sucesso(page)

@pytest.mark.OM02
def test_validar_mais_campos_apresentados_ao_selecionar_outro_sistema_coordenada(page: Page):
    with allure.step("acessar tela OM02"):
        OM02Page.page_OM02(page)
    with allure.step("Validar mais campos apresentados ao selecionar outra opção no campo de Coordenada"):
        OM02Page.validar_mais_campos_apresentados_ao_selecionar_outro_sistema_coordenada(page)
     
@staticmethod
def test_validar_clicar_sim_para_excluir(page: Page):
    with allure.step("acessar tela OM02"):
        OM02Page.page_OM02(page)
    with allure.step("Validar clicar em sim para excluir o registro"):
        OM02Page.validar_clicar_sim_para_excluir(page)
        OM02Page.validar_adicionar_item_MMITB(page)






