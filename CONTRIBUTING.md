# Contributing

This project favors curated, useful resources over exhaustive link collection.

## Resource Requirements

Every new resource must include:

- title
- URL
- category
- target track or audience
- why it matters
- free, paid, freemium, or certification status
- last verified date in `YYYY-MM-DD` format
- suggested tier: `Must learn`, `Use in real audits`, `Situational / advanced`,
  `Paid / certification`, or `Watchlist`

If you add a resource to a Markdown page, also add or update the matching entry
in `docs/data/resources.yml` when it is intended to be part of the maintained
catalog.

## Quality Bar

Good additions usually have at least one of these properties:

- primary documentation for a language, chain, tool, or standard
- public audit reports or security research
- runnable exploit reproduction or practice material
- maintained tool used by real auditors or security teams
- incident response, monitoring, OPSEC, or launch-readiness value

Avoid adding:

- stale listicles
- unsourced rankings
- affiliate-only pages
- thin marketing pages with no practical security content
- tools that require sending sensitive protocol data without clear disclosure

## Local Checks

```bash
pip install -r requirements.txt
mkdocs build --strict
```

Link checking runs in GitHub Actions with Lychee. If a real link blocks
automated checkers, add it to `.lycheeignore` with a short comment.
