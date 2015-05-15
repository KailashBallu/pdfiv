pdfiv
====================

Friendly indexer and viewer of PDF files by web application.

## Manual

### Requirements
- Python
- Windows

### External tools

- Xpdf http://www.foolabs.com/xpdf/
- https://code.google.com/p/tesseract-ocr/

### Executing

Converting PDF:

Default way: PDF > PNG + HTML + Text from PDF

```bash
$: python.exe -u scripts/convertpdf.py files/pdf files/target default
```

OCR way: PDF > PNG > Text from OCR

```bash
$: python.exe -u scripts/convertpdf.py files/pdf files/target default
```

Other tools

```bash
$: python.exe -u scripts/createmetadata.py files/target
$: python.exe -u scripts/updatesearchindex.py files/target
$: python.exe -u scripts/download.py urlist.txt files/pdf
```

## Author

Adrian Pietka

* [http://adrian.pietka.me](http://adrian.pietka.me)
* [adrian@pietka.me](mailto:adrian@pietka.me)

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0) &copy; Adrian Pietka

## Release History

* 0.1.0 Concept of application