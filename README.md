# lab_system
Sistema de controle de equipamentos de laboratório na área da saúde. 

# 🧪 Sistema de Controle de Equipamentos de Laboratório

Sistema web desenvolvido em **Django** para controle de equipamentos de laboratório, permitindo:
- Registro de uso
- Devolução
- Manutenção
- Dashboard gerencial
- Relatórios em CSV e Excel

---

## 🚀 Funcionalidades

### 📋 Equipamentos
- Listagem completa
- Status normalizados:
  - `disponivel`
  - `em_uso`
  - `manutencao`
- Histórico de uso por equipamento
- Controle de empréstimo e devolução

### 👤 Usuários
- Autenticação (Login/logout)
- Exibição do usuário logado em todas páginas
- Visualização de equipamentos em uso pelo próprio usuário
- Controle de devolução

### 🛠 Manutenção
- Enviar equipamento para manutenção
- Finalizar manutenção
- Página dedicada de relatório de equipamentos em manutenção
- Exportação do relatório de eqipamentos em manutenção
- Exportação do relatório em CSV  Exel

### 📊 Dashboard
- Total de equipamentos
- Disponíveis
- Em uso
- Em manutenção
- Em uso pelo usuário logado
- Menu centralizado de acesso aos relatórios

### 📄 Relatórios
- Página de relatório de manutenção
- Página de relatório de equipamentos em uso
- Página de usuários para seleção
- Página com equipamentos em uso por usuário selecionado
- Exportação em:
  - CSV
  - Excel (.xlsx)

---

## 🧱 Tecnologias Utilizadas

- Python 3.12
- Django 6.x
- HTML5
- CSS3
- SQLite (padrão, pode ser trocado)
- openpyxl (para Excel)

---

## 📁 Estrutura do Projeto

```text
lab_system/
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── equipamentos/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── equipamentos/
│   │       ├── dashboard.html
│   │       ├── lista.html
│   │       ├── meus_equipamentos.html
│   │       └── relatorio_manutencao.html
│   └── static/
│       └── css/style.css
├── manage.py
└── README.md
```
---

## Importação de usuários

O sistema possui um comando para importar usuários via CSV.

### Exemplo de uso

```bash
python manage.py importar_usuarios data/usuarios_lab.csv

```


## Importação de equipamentos

O sistema possui um comando para importar equipamentos via CSV.

### Exemplo de uso

```bash
python manage.py importar_equipamentos data/importar_equipamentos.csv

```




