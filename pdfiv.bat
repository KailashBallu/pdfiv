python.exe -u scripts/convertpdf.py files/pdf files/target
python.exe -u src/createstructureindex.py target/ target/structureindex.json
python.exe -u src/updatesearchindex.py target/ target/structureindex.json