
# TP Youtube Scrapping

Permet de récuperer les informations importantes d'une vidéos au format json

Le scrapping ne récupère pas les commentaires car il faudrait utiliser une librairie du type Selenium afin de charger le JS hors ce n'est pas autorisé.




## Details

Details sur le programme

### Execution :
python3 scrapper.py --input <input_file>.json --output <output_file>.json

### Input_file
Fichier au format json contenant les **id** des vidéos à parser (youtube.com/watch?v=**3cIObgePakE**)

### Output_file
Fichier au format json contenant les données parsées

### Tests
python3 -m pytest tests

## Author

- [@rlecuppe](https://www.github.com/rlecuppe)

