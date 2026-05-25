# Web3 Security Resources 2026

An opinionated, maintained learning hub for Web3 security in 2026.

This repository is no longer a giant bookmark dump. It is a GitHub Pages
knowledge base with curated roadmaps, resource tiers, and readiness checklists
for people who want to learn, audit, build, launch, and operate Web3 systems
safely.

## Start Here

| Goal | Best entry point |
| --- | --- |
| I am new to Web3 security | [Start From Zero](docs/roadmaps/start-from-zero.md) |
| I want to become an EVM auditor | [Solidity/EVM Auditor](docs/roadmaps/solidity-evm-auditor.md) |
| I audit Solana programs | [Rust/Solana Auditor](docs/roadmaps/solana-rust-auditor.md) |
| I work on Move, Cairo, or ZK systems | [Move](docs/roadmaps/move-auditor.md), [Cairo/Starknet](docs/roadmaps/cairo-starknet-auditor.md), [ZK Security](docs/roadmaps/zk-security.md) |
| I run security for a protocol | [Protocol Security Engineer](docs/roadmaps/protocol-security-engineer.md) |
| I secure a Web3 frontend or app stack | [Full-Stack Web3 Security](docs/roadmaps/full-stack-web3-security.md) |
| I want checklists before launch | [Security Checklists](docs/checklists/index.md) |

## What Changed

- Added a MkDocs Material site for GitHub Pages.
- Reorganized resources by audience, maturity, and audit usefulness.
- Added roadmaps for EVM, Solana, Move, Cairo/Starknet, ZK, protocol security,
  full-stack Web3 security, and AI-assisted auditing.
- Added checklists for audit readiness, launch, post-launch operations,
  frontend security, supply chain, multisigs, wallets, SOC/IR, and bug bounties.
- Added curated resource metadata with verification dates and tier labels.
- Added GitHub Actions for Pages deployment and weekly link checking.

## Resource Tiers

- **Must learn**: Foundational resources worth studying deeply.
- **Use in real audits**: Tools and references that repeatedly help on live work.
- **Situational / advanced**: Specialized material for specific systems or risks.
- **Paid / certification**: Useful but not required; cost or access may limit use.
- **Watchlist**: Promising, niche, or changing quickly; verify before relying on it.

## Local Development

```bash
pip install -r requirements.txt
mkdocs serve
mkdocs build --strict
```

The deployed site is configured for:

```text
https://raiders0786.github.io/web3-security-resources/
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md). New resources must include a
title, URL, category, why it matters, free/paid status, and last verified date.
This project favors high-signal curation over exhaustive indexing.
