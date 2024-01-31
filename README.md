# orderline-dw

## Configuratie

Zorg voor twee databases:
- Een oltp (test) database. Je kunt een test database op Azure SQL of SQL Server opzetten
met het sql script `orderline-oltp-test-create-insert.sql`.
- Een database voor het data warehouse met daarin een schema `staging`.

Maak een bestand `config_dev.ini` met daarin ingevuld de parameters die 
je kunt vinden in `config.ini`.

## Huidige functionaliteit

Het python script `oltp2staging` kopieert de tabellen van oltp naar 
staging in het data warehouse. 

## Package management met poetry

Dit project gebruikt poetry voor package management. Zorg ervoor dat je
poetry geinstalleerd hebt en dat je werkt met een environment. Dan kun je
`poetry install` gebruiken om alle packages te installeren.
Zie https://python-poetry.org/



