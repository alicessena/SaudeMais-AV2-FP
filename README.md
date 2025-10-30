# 🏥 Sistema de Agendamento de Consultas em UBS (Desafio 3)

![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-blue)
![Framework](https://img.shields.io/badge/Framework-Django-0C4B33?logo=django)
![Language](https://img.shields.io/badge/Language-Python-3776AB?logo=python)
![React](https://img.shields.io/badge/React-61DAFB?logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white)

Este projeto é um sistema para gerenciamento e agendamento de consultas em uma Unidade Básica de Saúde (UBS), desenvolvido para a disciplina de **Fundamentos da Programação**.

## 🎯 Objetivo

O objetivo principal é otimizar o agendamento de consultas, visando melhorar o fluxo de pacientes e profissionais, proporcionar um atendimento mais eficiente e reduzir as filas de espera.

A iniciativa está alinhada diretamente ao **Objetivo de Desenvolvimento Sustentável (ODS) 3: Saúde e Bem-Estar** da ONU.

---
## ✨ Funcionalidades Essenciais

O sistema implementa as seguintes operações (CRUD) e relatórios:

* **Gestão de Pacientes:**
    * [ ] Cadastrar Paciente (Create)
    * [ ] Listar/Buscar Pacientes (Read)
    * [ ] Atualizar dados do Paciente (Update)
    * [ ] Excluir Paciente (Delete)
* **Gestão de Profissionais:**
    * [ ] Cadastrar Profissional (Create)
    * [ ] Listar/Buscar Profissionais (Read)
    * [ ] Atualizar dados do Profissional (Update)
    * [ ] Excluir Profissional (Delete)
* **Gestão de Consultas:**
    * [ ] Agendar Consulta (Create)
    * [ ] Visualizar Consultas (Read)
    * [ ] Reagendar/Editar Consulta (Update)
    * [ ] Cancelar Consulta (Delete)
* **Gestão de Exames:**
    * [ ] Solicitar Exame (Create)
    * [ ] Consultar Exames (Read)
    * [ ] Registrar/Atualizar Resultado (Update)
* **Gestão de Farmácia:**
    * [ ] Consultar Estoque de Remédio (Read)
    * [ ] Solicitar Remédio (Create)
    * [ ] Registrar Retirada de Remédio (Update)
* **Relatórios Essenciais:**
    * [ ] Gerar relatório de consultas por profissional.
    * [ ] Gerar relatório de consultas por data.
---

## 💻 Tecnologias Utilizadas

* **Backend:** Python
* **Framework Web:** Django
* **Frontend (Base):** React com Typescript

---

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para executar o projeto localmente.

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/alicessena/SaudeMais-AV2-FP.git
    cd nome-do-repositorio
    ```

2.  **Crie e ative um ambiente virtual (venv):**
    ```bash
    # No Windows
    python -m venv venv
    .\venv\Scripts\activate

    # No macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    (É uma boa prática criar um arquivo `requirements.txt` com `pip freeze > requirements.txt` e adicionar as dependências, como o Django)
    ```bash
    pip install -r requirements.txt
    # Ou instale o Django manualmente se for o início
    # pip install django
    ```

4.  **Aplique as migrações (migrations) do banco de dados:**
    ```bash
    python manage.py migrate
    ```

5.  **(Opcional) Crie um superusuário para acessar o Admin do Django:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

7.  Acesse `http://127.0.0.1:8000/` no seu navegador.

---

## 👥 Equipe

Este projeto está sendo desenvolvido pelos seguintes integrantes:

* Alice Maria Sena Pereira (**Leader**)
* Aquiles Pereira dos Santos
* Eloi de Lima Sousa
* Leticia Gomes da Silva
* Lucas Filipe de Lima Segundo 
* Luan Ventura Ferreira de Moura (**Tech Leader**)

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT.
