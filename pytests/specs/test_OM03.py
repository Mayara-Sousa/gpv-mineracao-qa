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

@pytest.mark.OM03
def test_validar_clicar_salvar_sem_adicionar_informacoes(page: Page):
     with allure.step("acessar tela OM03"):
        OM03Page.page_OM03(page)
     with allure.step("Validar clicar em salvar sem adicionar informações"):
         OM03Page.validar_clicar_salvar_sem_adicionar_informacoes(page)

@pytest.mark.OM03
def test_validar_clicar_em_cancelar_dentro_da_linha_do_grid(page: Page):
     with allure.step("acessar tela OM03"):
        OM03Page.page_OM03(page)
     with allure.step("Validar clicar em cancelar dentro da linha do grid"):
         OM03Page.validar_clicar_em_cancelar_dentro_da_linha_do_grid(page)

@pytest.mark.OM03
def test_validar_clicar_em_editar_dentro_da_linha_do_grid(page: Page):
     with allure.step("acessar tela OM03"):
        OM03Page.page_OM03(page)
     with allure.step("Validar clicar em editar dentro da linha do grid"):
         OM03Page.validar_clicar_em_editar_dentro_da_linha_do_grid(page)

# Validar registro inserido salvo no banco de dados 
         
@pytest.mark.OM03
def test_validar_clicar_não_para_excluir_registro(page: Page):
     with allure.step("acessar tela OM03"):
        OM03Page.page_OM03(page)
     with allure.step("Validar clicar não ao clicar para excluir registro"):
         OM03Page.validar_clicar_não_ao_clicar_para_excluir_registro(page)


@pytest.mark.OM03
def test_validar_clicar_sim_para_excluir_registro(page: Page):
     with allure.step("acessar tela OM03"):
        OM03Page.page_OM03(page)
     with allure.step("Validar clicar em editar dentro da linha do grid"):
         OM03Page.validar_clicar_em_editar_dentro_da_linha_do_grid(page)


# Validar registro excluído do banco
         
@pytest.mark.OM03
def test_validar_erro_ao_tentar_salvar_registro_com_data_vigencia_no_passado(page: Page):
     with allure.step("acessar tela OM03"):
        OM03Page.page_OM03(page)
     with allure.step("Validar erro ao tentar salvar registro com data de vigencia no passado"):
         OM03Page.validar_erro_ao_tentar_salvar_registro_com_data_vigencia_no_passado(page)

@pytest.mark.OM03
def test_validar_mensagem_ao_adicionar_registro_com_associação_equipamento_já_existente(page: Page):
     with allure.step("acessar tela OM03"):
        OM03Page.page_OM03(page)
     with allure.step("Validar mensagem de erro ao adicionar registro com data de associação já existente para o equipamento/bloco"):
         OM03Page.validar_mensagem_ao_adicionar_registro_com_associação_equipamento_já_existente(page)

@pytest.mark.OM03
def test_validar_mensagem_erro_quando_não_preencher_campo_fim_associacao(page: Page):
     with allure.step("acessar tela OM03"):
        OM03Page.page_OM03(page)
     with allure.step("Validar mensagem de erro quando não preencher o registro com data de fim de associação se já existir um sem"):
         OM03Page.validar_mensagem_erro_quando_não_preencher_campo_fim_associacao(page)