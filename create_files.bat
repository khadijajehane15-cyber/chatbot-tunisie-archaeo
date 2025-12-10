@echo off
echo Création de 50 fichiers pour le projet...
echo.

cd data

:: Sites principaux (10 sites)
set SITES=carthage dougga el_jem kerkouane bulla_regia sbeitla utique thuburbo_majus makthar chemtou

:: Pour chaque site
for %%s in (%SITES%) do (
    echo Création des fichiers pour %%s...
    
    :: 1. Fichier général
    echo Source : Wikipédia > "%%s_general.txt"
    echo Site : %%s >> "%%s_general.txt"
    echo Type : Description générale >> "%%s_general.txt"
    echo. >> "%%s_general.txt"
    
    :: 2. Fichier histoire
    echo Source : Wikipédia > "%%s_histoire.txt"
    echo Site : %%s >> "%%s_histoire.txt"
    echo Type : Histoire >> "%%s_histoire.txt"
    echo. >> "%%s_histoire.txt"
    
    :: 3. Fichier architecture
    echo Source : Wikipédia > "%%s_architecture.txt"
    echo Site : %%s >> "%%s_architecture.txt"
    echo Type : Architecture >> "%%s_architecture.txt"
    echo. >> "%%s_architecture.txt"
    
    :: 4. Fichier fouilles
    echo Source : Wikipédia > "%%s_fouilles.txt"
    echo Site : %%s >> "%%s_fouilles.txt"
    echo Type : Fouilles archéologiques >> "%%s_fouilles.txt"
    echo. >> "%%s_fouilles.txt"
    
    :: 5. Fichier UNESCO
    echo Source : UNESCO > "%%s_unesco.txt"
    echo Site : %%s >> "%%s_unesco.txt"
    echo Type : Patrimoine mondial >> "%%s_unesco.txt"
    echo. >> "%%s_unesco.txt"
)

echo.
echo ✅ 50 fichiers créés avec en-têtes !
echo Il reste à remplir le contenu.
pause