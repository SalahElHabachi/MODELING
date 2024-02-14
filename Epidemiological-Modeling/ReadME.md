
##  C'est quoi une maladie épidémiologique ?  🙄 
Les maladies épidémiologiques sont des affections qui affectent un grand nombre de personnes dans une population donnée.

L'épidémiologie est la branche de la science de la santé qui étudie la distribution et les déterminants des maladies au sein des populations. Les chercheurs en épidémiologie analysent les schémas de propagation des maladies, identifient les facteurs de risque et développent des stratégies de prévention et de contrôle.

les maladies epidémiologiques peuvent etre decrits par des modèles de type SIR, SIRI,SIRS ...

## Objectif du projet ?
Dans le cadre de ce projet académique, j'ai examiné plusieurs modèles décrivant la propagation d'une maladie épidémiologique au sein d'une population supposée stable (en considérant le nombre de naissances égal au nombre de décès). J'ai débuté par une approche mathématique, rétablissant les systèmes différentiels régissant les trois modèles SIR, SIRI et SIRS.

Par la suite, j'ai développé une application Python à partir de zéro, avant l'avènement de ChatGPT, qui offre plusieurs fonctionnalités, notamment :
- La résolution des systèmes différentiels.
- Le tracé des courbes caractéristiques des modèles.
- Les deux états d'équilibre ( libre, infectueux ).
- La représentation graphique des schémas des modèles SIR, SIRI et SIRS.
- La possibilité de sauvegarder les figures avec les différents paramètres du modèle.

Cette application a donc été conçue pour faciliter l'analyse, la visualisation et la compréhension des dynamiques de propagation de la maladie en fonction des divers paramètres du modèle.

## Comment faire marcher l'application ?
### Préprer le terrain : 😉
1. Cloner le projet en local :
```bash
git clone ...............
```
2. Créer & Activer un environnement conda :
```bash
conda create --name nom_de_votre_environnement python=3.10

```
 - Sur Windows :
```bash
activate nom_de_votre_environnement
```
 - Sur Linux/macOS :
```bash
source activate nom_de_votre_environnement
```
3. Installer les package nécessaires :
> Dans ce projet on a utilisé la bibiothèque Tkinter de python :

```bash
conda install pillow

```
```bash
conda install matplotlib

```
```bash
conda install numpy

```
```bash
conda install scipy

```
### Exécuter le code : 😉
> Si vous utiliser un IDE, il faut ouvrir le fichier ``code source.py`` et l'exécuter.
> Si vous voulez pas passer par un IDE, utilisez la ligne de commande ( ou bash ). Il faut tapper : ``python code source.py``
> Si tout ce passe bien, vous aurez une interface graphique (genêtre Tkinter) qui vous demande de choisir le modèle et d'introduire les valeurs des différents paramètres.
> Et pour lancer les calculs + le tracer ==> il faut cliquer sur le bouton ***Tracer***.

### Résultat (exemple) : 
---
![Exemple](https://github.com/SalahElHabachi/MODELING/tree/main/Epidemiological-Modeling/image/exemple.PNG)

>**Explication de la sortie de l'interface :**
---
> **Le taux initial d'infection (I0) :** Correspond au pourcentage de personnes infectées au début de la simulation, à l'instant t=0.

> **Le taux d'incidence :** Indique le taux auquel de nouvelles infections se produisent, c'est-à-dire le pourcentage de personnes qui passent de l'état Susceptible (S) à l'état Infecté (I).

> **Le taux d'immunité :** Indique la proportion de personnes qui, après avoir été infectées et guéries, restent susceptibles de contracter la maladie à nouveau. Dans le modèle SIRS, ce taux est non nul, ce qui signifie que l'immunité n'est pas éternelle.

> **Le bouton État d'équilibre :** Montre l'état de stabilité de la maladie lorsque le temps t devient très grand. Il existe deux types d'équilibre en fonction du nombre de base de reproduction R0, qui dépend des trois paramètres mentionnés précédemment :
  1. Un état libre, où la maladie ne se propage pas de manière épidémique.
  2. Un état épidémique, où la maladie se propage de manière épidémique, c'est-à-dire qu'une épidémie est en cours.

> **Le bouton Schéma du modèle :** Permet d'afficher un schéma illustrant le flux des cas selon le modèle sélectionné, mettant en évidence les transitions entre les états Susceptible (S), Infecté (I) et Rétabli (R).

> **Le bouton Enregistrer :** Permet de sauvegarder la figure localement, avec éventuellement la date et les paramètres inclus dans le nom de fichier. Cela offre la possibilité de conserver une trace visuelle des résultats de la simulation.

> **Voici un exemple de deux figures enregistrées une avec params et l'autre sans params :**
---
>![Exemple](https://github.com/SalahElHabachi/MODELING/tree/main/Epidemiological-Modeling/image/exemple2.PNG)
---

## Ressources  : 📻


---
Pour les gens qui seront intéressé par le sujet, et veulent aller un peu dans les détails mathématiques je veux laisse les ressources que j'avais trouvées : 


**1. Livres :**
>   - [Mathematical Models in Population Biology and Epidemiology](https://www.academia.edu/42818669/Mathematical_Models_in_Population_Biology_and_Epidemiology20200422_114276_1hkkd3b) par Fred Brauer et Carlos Castillo-Chávez : Ce livre offre une introduction complète à la modélisation mathématique en biologie des populations et en épidémiologie, avec une discussion détaillée sur les modèles épidémiologiques.
>   - [Mathematical Epidemiology](https://link.springer.com/book/10.1007/978-3-540-78911-6)" par Odo Diekmann, Hans Heesterbeek et Tom Britton : Ce livre fournit une introduction détaillée à >la modélisation mathématique des maladies infectieuses, couvrant un large éventail de sujets, des bases mathématiques aux applications pratiques.

**2. Cours en ligne :**
>   - [Epidemics - the Dynamics of Infectious Diseases](https://www.coursera.org/learn/epidemics) sur Coursera : Ce cours de l'Université de Pennsylvanie offre une introduction aux modèles épidémiologiques, avec un accent particulier sur les épidémies et les pandémies.
>   - "[Modeling Infectious Diseases](lien_vers_le_cours)" sur edX : Ce cours de l'Université de Washington explore les concepts clés de la modélisation des maladies infectieuses, y compris les modèles déterministes et stochastiques.

**3. Articles et revues :**
>   - "[Modeling infectious diseases in humans and animals](https://www.jstor.org/stable/j.ctvcm4gk0)" par Matt J. Keeling et Pejman Rohani, dans "Science" : Cet article offre une vue d'ensemble de la modélisation des maladies infectieuses, en mettant l'accent sur les techniques mathématiques utilisées et les défis rencontrés.
>   - "[Mathematical models to characterize early epidemic growth: A review](https://www.sciencedirect.com/science/article/abs/pii/S1571064516300641)" par Daniel B. Larremore et al., dans "Physics Reports" : Cette revue examine les modèles mathématiques utilisés pour caractériser la croissance épidémique précoce et fournit des informations sur leur utilisation dans la prévision des épidémies.

**4. Ressources en ligne :**
>   - Le [site web du Centre de Contrôle et de Prévention des Maladies (CDC)](https://www.cdc.gov/index.htm) propose une section sur la modélisation mathématique des maladies infectieuses, avec des ressources et des outils pour les chercheurs et les professionnels de la santé.
   - Le [site web du Réseau d'Analyse de Risques Infectieux en Europe (ERINHA)](https://erinha.eu/) offre des informations sur la modélisation mathématique des maladies infectieuses, ainsi que des liens vers des outils et des ressources supplémentaires.


---
>![Thanks](https://github.com/SalahElHabachi/MODELING/tree/main/Epidemiological-Modeling/image/thanks.PNG)
---
