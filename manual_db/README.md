# Local Manual Library

`sources.json` is the library registry. A source entry has one vendor/platform/version and a list of official HTML URLs. The file can contain one source entry directly, or a `manuals` array when it contains multiple versions.

Example source entry:

```json
{
  "vendor": "Cisco",
  "platform": "IOS XR",
  "version": "7.7.1",
  "sources": [
    "https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/routing/command/reference/b-routing-cr-asr9000.html",
    "https://www.cisco.com/c/en/us/td/docs/routers/asr9000/software/asr9k-r7-8/routing/configuration/guide/b-routing-cg-asr9000-79x.html"
  ]
}
```

Run the audit with `--manual-library` to select the matching vendor/version entry. Each URL is downloaded only when its cache entry is absent, then reused from `manual_db/cache/` by later audits. Reports retain the original source URL as evidence.
