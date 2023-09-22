from pytests.support.hooks import *
from pytests.pages.OM01_page import OM01Page
from playwright.sync_api import Page
import allure


# Descrição dos testes com pytest
@pytest.mark.OM01
def test_validar_tela(page: Page):
    with allure.step("acessar tela OM01"):
        OM01Page.page_OM01(page)
    with allure.step("Validar campos visiveis"):
        OM01Page.validar_campos_visiveis(page)

@pytest.mark.OM01
def test_validar_campo_unidade_preenchido(page: Page):
    with allure.step("acessar tela OM01"):
        OM01Page.page_OM01(page) 
    with allure.step("Validar campo sendo apresentado no grid"):
        OM01Page.validar_campos_grid(page)

@pytest.mark.OM01
def test_validar_botão_limpar_antes_pesquisa(page: Page):
    with allure.step("acessar tela OM01"):
        OM01Page.page_OM01(page)
    with allure.step("Validar botão limpar antes da pesquisa"):
        OM01Page.validar_botao_limpar(page)

@pytest.mark.OM01
def test_validar_botão_limpar_depois_pesquisa(page: Page):
    with allure.step("acessar tela OM01"):
        OM01Page.page_OM01(page)
    with allure.step("Validar botão limpar depois da pesquisa"):
        OM01Page.validar_botao_limpar_depois_pesquisa(page)

@pytest.mark.OM01
def test_validar_conteudo_destino_referencia(page: Page):
    with allure.step("acessar tela OM01"):
        OM01Page.page_OM01(page)
    with allure.step("selecionar unidade operacional e adicionar destino"):
        OM01Page.inserir_unidade_operacional(page)
    with allure.step("validar campos apresentados na tela de destino"):
        OM01Page.validar_conteudo_acoes_adicionar_destino_referencia(page)

@pytest.mark.OM01
def test_validar_adicionar_destino_referencia(page: Page):
    with allure.step("acessar tela OM01"):
        OM01Page.page_OM01(page)
    with allure.step("selecionar unidade operacional e adicionar destino"):
        OM01Page.inserir_unidade_operacional(page)
    with allure.step("adicionar um destino referencia"):
        OM01Page.adicionar_destino_referencia(page, "SNP170030")
    with allure.step("validar destino adicionado com sucesso"):
        OM01Page.validar_destino_salvo(page)
        OM01Page.remover_destino_referencia(page, "SNP170030")
        OM01Page.validar_destino_salvo(page)

    
# @pytest.mark.validar_editar_destino_existente
# def test_validar_editar_destino_existente(page :Page):
#     with allure.step("acessar tela OM01"):
#         OM01Page.page_OM01(page)
#     with allure.step("selecionar unidade operacional"):
#         OM01Page.inserir_unidade_operacional(page)
#     with allure.step("validar editar destino existente"):
#         OM01Page.validar_editar_destino_existente(page, "Pilha SNP170029 teste automacao  ", "teste automacao 1")
#         OM01Page.validar_destino_editado_com_sucesso(page)
#         OM01Page.validar_editar_destino_existente(page, "Pilha SNP170029 teste automacao 1  ", "teste automacao")
#         OM01Page.validar_destino_editado_com_sucesso(page)

@pytest.mark.OM01
def test_validar_clicar_nao_para_excluir(page :Page):
    with allure.step("acessar tela OM01"):
        OM01Page.page_OM01(page)
    with allure.step("selecionar unidade operacional"):
        OM01Page.inserir_unidade_operacional(page)
    with allure.step("validar clicar no botao exclur"):
        OM01Page.validar_clicar_nao_para_excluir(page, "Pilha SNR170002 BRIT  ")
 

@pytest.mark.OM01
def test_validar_cancelar_cadastro_destino_referencia(page :Page):
     with allure.step("acessar tela OM01"):
        OM01Page.page_OM01(page)
     with allure.step("validar cancelar o cadastro do destino referencia"):
        OM01Page.validar_cancelar_cadastro_destino_referencia(page, "CXE170002", "Teste automação")


@pytest.mark.OM01
def test_validar_conteudo_acoes_adicionar_equipamento(page :Page):
     with allure.step("acessar tela OM01"):
        OM01Page.page_OM01(page)
     with allure.step("validar conteudo tela adicionar equipamento"):
         OM01Page.validar_conteudo_acoes_adicionar_equipamento(page, "EM2501 Baixa precisão ")


@pytest.mark.OM01
def test_validar_editar_equipamento_cadastrado(page :Page):
    with allure.step("acessar tela OM01"):
        OM01Page.page_OM01(page)
    with allure.step("editar equipamento cadastrado"):
        OM01Page.validar_editar_equipamento_cadastrado(page, "EM4001 Baixa precisão ", "Manual", "Baixa precisão Baixa precisão ")
        OM01Page.validar_destino_salvo(page)
        OM01Page.validar_editar_equipamento_cadastrado(page, "EM4001 Manual ", "Baixa precisão", "Manual Manual ") 


@pytest.mark.OM01
def test_validar_realizar_pesquisa_filtro_em_branco(page :Page):
    with allure.step("acessar tela OM01"):
        OM01Page.page_OM01(page)
    with allure.step("validar realizar pesquisa com o filtro em branco"):
        OM01Page.validar_realizar_pesquisa_filtro_em_branco(page)


@pytest.mark.OM01
def test_validar_cancelar_edicao_equipamento_cadastrado(page :Page):
    with allure.step("acessar tela OM01"):
        OM01Page.page_OM01(page)
    with allure.step("editar equipamento cadastrado"):
        OM01Page.validar_cancelar_edicao_equipamento_cadastrado(page, "EM2001 Baixa precisão ", "Baixa precisão Baixa precisão ")


@pytest.mark.OM01
def test_validar_utilizar_nome_para_outra_unidade_operacional(page :Page):
    with allure.step("acessar tela OM01"):
        OM01Page.page_OM01(page)
    with allure.step("validar adicionar um nome de registro já utilizado em outra Unidade Operacional"):
        OM01Page.validar_utilizar_nome_para_outra_unidade_operacional(page, "ALI190002", "teste_123")
    
