# Modelo de Predição de Partidas CBLOL2024

* Modelo criado exclusivamente para fim educativos.
* As bases de treino utilizadas para a predição estão na pasta data.

### Atributos e Modelo

O modelo utilizado no APP é um modelo de RandomForest treinado utilizando a média  
dos seguintes atributos individuais de cada jogador na temporada:

* Kills
* Deaths
* Assists
* CS
* CS/M (CS per minute)
* Gold
* G/M (Gold per minute)
* DMG
* DMG/M (Damage per minute)
* KPAR (Kill Participation (K+A/Team K))
* KS (Kill Share (K/Team K))
* GS (Gold Share)

O DataFrame de treino foi criado utilizando a função treino() descrita no notebook na pasta model.  
Foi gerado dentro do dataset matches, que contém as partidas finalizadas até o fim de semana 09/03 até  
10/03, todos os atributos afim de classificar o atributo target "blue_venceu".

Para que a predição possa ser feita sem a necessidade do preenchimento de todos os atributos por consulta, foi criada a  
função criar_dados() que recebe o dataset de times, o time azul e vermelho fornecidos pelo usuário e retorna um  
dataframe de linha única com as características a serem utilizadas na predição.




