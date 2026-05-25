---
title: Methodology
description: Editorial methodology for curating Web3 security resources, labeling maintainer projects, and avoiding endorsement claims.
---

# Methodology

This project ranks resources by practical usefulness, not by sponsorship,
popularity, or search-engine visibility.

## Ranking Criteria

| Criterion | What it means |
| --- | --- |
| Relevance | The resource directly helps Web3 security work in 2026. |
| Practical value | It improves audits, protocol design, testing, monitoring, or incident response. |
| Freshness | It is current enough for the system class it covers, or it is clearly timeless. |
| Public proof | The author has public audits, research, tools, standards work, or incident experience. |
| Maintenance | The resource is updated, versioned, or still reflects current practice. |
| Reputation | It is trusted by auditors, engineers, protocols, or security teams. |
| Accessibility | Free and open resources are preferred when quality is comparable. |

## Tier Definitions

- **Must learn**: Study deeply. These resources shape core mental models.
- **Use in real audits**: Keep these in your working toolkit.
- **Situational / advanced**: Use when the scope needs that specialty.
- **Paid / certification**: Useful but not a prerequisite for competence.
- **Watchlist**: Worth tracking, but verify claims and maintenance before relying
  on it for production decisions.

## Trust Policy

This catalog should not become free distribution for every new security startup,
AI wrapper, or SEO landing page. A resource needs credible public proof before it
is included: official documentation, open-source code, public audits or reports,
recognized research, maintained standards, visible ecosystem usage, or a
well-established security team behind it.

Paid tools may appear when they solve a real security workflow and have enough
public proof to evaluate, but they must be labeled clearly. AI audit products are
tracked conservatively and never presented as replacements for manual review,
testing, threat modeling, or exploit proof. A **Watchlist** item means "inspect
and verify before relying on it," not endorsement.

## Verification Rules

Every resource entry should include:

- `title`
- `url`
- `category`
- `track`
- `level`
- `free_or_paid`
- `last_verified`
- `why_it_matters`
- `status`

Links are checked automatically on pull requests and weekly schedules. A link
may be allowed in `.lycheeignore` when the target blocks automated clients but is
still manually verified.
