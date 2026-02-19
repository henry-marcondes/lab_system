# Changelog

Todas as mudanças relevantes deste projeto serão documentadas neste arquivo.

O formato segue o padrão [Keep a Changelog](https://keepachangelog.com/)
e o projeto utiliza [Versionamento Semântico](https://semver.org/).

---

## [Unreleased]
### Added
- Página central de relatórios com seleção de tipo e formato
- Relatórios de equipamentos em uso
- Relatórios por usuário (histórico completo de manuseio)
- Exportação de relatórios em CSV
- Exportação de relatórios em Excel (.xlsx)
- Menu de relatórios acessível a partir do dashboard

### Changed
- Refatoração do dashboard para uso de status normalizados
- Navegação global via `base.html`
- Organização dos relatórios por rotas (`/relatorios/`)

### Fixed
- Correção de carregamento de arquivos estáticos
- Ajustes em rotas e reverses de URLs
- Correções de dependências para geração de relatórios

---

## [0.1.0] - 2026-02-19
### Added
- Sistema de autenticação (login/logout)
- Cadastro e listagem de equipamentos
- Controle de uso e devolução de equipamentos
- Controle de manutenção de equipamentos
- Histórico de uso por equipamento
- Dashboard gerencial
- Comandos de importação via CSV:
  - Importação de usuários
  - Importação de equipamentos
- Estilização base com CSS próprio
