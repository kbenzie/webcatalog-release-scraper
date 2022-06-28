# WebCatalog release scraper

Grabs the HTML https://webcatalog.io/webcatalog/changelog/ and scrapes the
release version and changelog into the `op-releases.json` file. This is intended
to facilitate automatic installation and upgrade of the WebCatalog application
on platforms where package manager support is not already provided.

## Usage

Grab the latest list of WebCatalog releases:

```console
$ curl -s https://raw.githubusercontent.com/kbenzie/webcatalog-release-scraper/main/webcatalog-releases.json
```
