from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status

class CursosTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT1', descricao='Curso teste 1',
            nivel='B'
        )
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT2', descricao='Curso teste 2',
            nivel='A'
        )

    # def test_falhador(self):
    #     self.fail('Teste falhou de propósito')
    def test_requisicao_get_para_listar_cursos(self):
        """Teste para verificar a requisição GET para listar os cursos"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code,status.HTTP_200_OK)

    def test_requisicao_post_para_criar_curso(self):
        """Teste para verificar a requisição POST para incluir um curso"""
        data ={
            'codigo_curso': 'CTT3',
            'descricao': 'Curso teste 3',
            'nivel': 'A'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
