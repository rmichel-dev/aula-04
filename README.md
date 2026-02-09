# Projeto Django – Aula 4

Este projeto foi desenvolvido em aula com o objetivo de ensinar os primeiros passos com **Python + Django**, incluindo ambiente virtual, criação de projeto, apps e execução do servidor local.

---

## Sistema Operacional

Este projeto **roda em Windows**:

---

## Pré-requisitos

Antes de começar, verifique se o Python está instalado:

```powershell
python --version
```

Pode ser necessário rodar
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Observação: O Windows Defender também pode bloquear a execução dos comandos caso o "Controle Inteligente de Aplicativos" esteja ativado.

---

## 1. Criar o Ambiente Virtual

No PowerShell, execute:

```powershell
python -m venv venv
```

Isso criará a pasta `venv` com o ambiente virtual do projeto.

---

## 2. Ativar o Ambiente Virtual

No **PowerShell**:

```powershell
.\venv\Scripts\activate
```

Se tudo estiver correto, o terminal exibirá:

```
(venv)
```

### Possível erro no PowerShell

Se aparecer erro de **script desativado**, você pode:

- Abrir o **Prompt de Comando (CMD)** e executar:
  ```cmd
  venv\Scripts\activate.bat
  ```
- Ou apenas confirmar que o `(venv)` apareceu no terminal

---

## 3. Instalar o Django

Com o ambiente virtual ativado:

```powershell
pip install django
```

Verifique a instalação:

```powershell
django-admin --version
```

---

## 4. Criar o Projeto Django

Crie o projeto na pasta atual:

```powershell
django-admin startproject setup .
```

> O ponto (`.`) evita a criação de pastas extras.

---

## 5. Criar o App Principal

Crie o app chamado `core`:

```powershell
python manage.py startapp core
```

---

## 6. Executar o Servidor

Inicie o servidor de desenvolvimento:

```powershell
python manage.py runserver
```

Abra o navegador e acesse:

```
http://127.0.0.1:8000/
```

---

## Encerrar o Servidor

Para parar o servidor:

```
Ctrl + C
```

---

## Sair do Ambiente Virtual

```powershell
deactivate
```

---

# Aula 10

### preparar as migrações
```powershell
python .\manage.py makemigrations
```

### Aplicar as migrações
```powershell
python .\manage.py migrate
```

### Aplicar as migrações
```powershell
python .\manage.py migrate
```

### Criar um superusuário
```powershell
python .\manage.py createsuperuser
```