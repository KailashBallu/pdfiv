pdfiv
====================

Friendly indexer and viewer of PDF files by web application.

## Manual

### Requirements
- Python
- Windows

### Executing

```bash
python.exe -u scripts/convertpdf.py files/pdf files/target
python.exe -u scripts/createstructureindex.py files/target
python.exe -u scripts/updatesearchindex.py files/target files/target/structureindex.json
```

## Author

Adrian Pietka

* [http://adrian.pietka.me](http://adrian.pietka.me)
* [adrian@pietka.me](mailto:adrian@pietka.me)

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0) &copy; Adrian Pietka

## Release History

* 0.1.0 Concept of application