# Performance_dashboard

Projet Sorbonne pour la création d'un dashboard sur l'application Flask pour visualiser les données des perfromances sur les rameurs 
La compétition se déroule comme suit : chaque série comporte 4 rameurs qui vont parcourir 2000m virtuels sur leurs machines. Le but est évidemment d'être le plus rapide possible sur ces 2000m. Les données de chaque série sont enregistrées par les machines et recueillies. Les courses ont été paramétrées pour que chaque parcours de 2000m soit divisé en quatre parties de 500m, c'est-à-dire que les statistiques données par les ergomètres sont calculées et restituées tous les 500m. Chaque fichier du zip correspond à une série. 

## Installations à faire 
- Version Python 3.11.7
Importer le lien du projet et puis créez votre environnement virtuel
Importer le lien du projet et puis créez votre environnement virtuel
```
https://github.com/vincent-tran-94/Performance_dashboard.git
python3 -m venv env
source env/Scripts/activate
```
Diriger-vous vers le dossier
```
cd application_dashboard/
```
Installer les dépendances 
```
pip install -r requirements.txt 
```
## Analyse des données et import des fichiers CSV
Ce fichier est un fichier notebook qui permet d'analyser les données sur les performances du rameur 
Vous devez impérativement installer Python sur votre machine ainsi que les dépendances 
```
Select Kernel <Nom de l'environnement virtuel>
```
## Lanchement de l'pplication web sur Flask
Lancer votre application Flask pour démarrer votre serveur 
```
python app.py 
```