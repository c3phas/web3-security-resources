# Web3 Security Resources 2026

This guide is a curated, opinionated map for Web3 security work in 2026. It is
designed for beginners, smart contract auditors, protocol engineers, frontend
security teams, incident responders, and researchers working across EVM, Solana,
Move, Cairo/Starknet, and ZK systems.

![Protocol security lifecycle](assets/diagrams/protocol-security-lifecycle.svg)

## Choose Your Track

| Track | Use it when |
| --- | --- |
| [Start From Zero](roadmaps/start-from-zero.md) | You need blockchain, Solidity, tools, and security mindset from first principles. |
| [Solidity/EVM Auditor](roadmaps/solidity-evm-auditor.md) | You want to review Solidity systems, DeFi protocols, upgradeable contracts, and contest scopes. |
| [Rust/Solana Auditor](roadmaps/solana-rust-auditor.md) | You review Solana programs, Anchor projects, Token-2022 integrations, and CPI/account-model risks. |
| [Move Auditor](roadmaps/move-auditor.md) | You work on Aptos, Sui, Move resources, capabilities, and upgrade safety. |
| [Cairo/Starknet Auditor](roadmaps/cairo-starknet-auditor.md) | You audit Cairo contracts, Starknet account abstraction, messaging, and bridge flows. |
| [ZK Security](roadmaps/zk-security.md) | You review circuits, proof systems, constraint systems, and verifier integrations. |
| [Protocol Security Engineer](roadmaps/protocol-security-engineer.md) | You own security from design through monitoring and incident response. |
| [Full-Stack Web3 Security](roadmaps/full-stack-web3-security.md) | You secure DNS, web apps, wallets, APIs, package supply chain, and transaction UX. |
| [AI-Assisted Auditor](roadmaps/ai-assisted-auditor.md) | You want practical LLM workflows without outsourcing judgment to the model. |

## The Operating Model

```mermaid
flowchart LR
  A[Design] --> B[Build]
  B --> C[Test]
  C --> D[Internal review]
  D --> E[External audit]
  E --> F[Fix verification]
  F --> G[Launch]
  G --> H[Monitor]
  H --> I[Incident response]
  I --> A
```

## Curated Resource Tiers

| Tier | Meaning |
| --- | --- |
| Must learn | Foundational resources worth reading carefully and revisiting. |
| Use in real audits | Tools, standards, and references that help during live review work. |
| Situational / advanced | Specialized material for bridges, ZK, governance, infra, or chain-specific risks. |
| Paid / certification | Useful structured training or products with a cost or restricted access model. |
| Watchlist | Promising or rapidly changing resources that should be verified before critical use. |

## High-Signal First Links

- [OWASP Smart Contract Top 10 2026](https://owasp.org/www-project-smart-contract-top-10/) for shared risk language.
- [OWASP Smart Contract Security Verification Standard](https://scs.owasp.org/SCSVS/) for assessment structure.
- [OpenZeppelin Audit Readiness](https://www.openzeppelin.com/readiness-guide) for preparing a codebase and team for review.
- [Solodit](https://solodit.cyfrin.io/) for searching public findings and contests.
- [SEAL Frameworks](https://frameworks.securityalliance.org/) for security operations and incident readiness.
- [DeFiHackLabs](https://github.com/SunWeb3Sec/DeFiHackLabs) for exploit reproduction and incident study.

## How to Use This Site

Start with one roadmap, build the matching toolchain, then use the checklists on
real or toy systems. Do not try to consume every link. Good Web3 security work is
iterative: learn a class of bug, reproduce it, write tests for it, review real
reports, and then apply it to a scope with a clear threat model.
