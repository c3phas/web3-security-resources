---
title: Checklists
description: Checklists page in the Web3 Security Resources 2026 hub.
---

# Checklists

These checklists are starting points for real review work. Adapt them to the
protocol, chain, custody model, and threat profile.

| Checklist | Use before |
| --- | --- |
| [Pre-Audit Readiness](pre-audit.md) | Sending code to external auditors or contests. |
| [Launch Readiness](launch.md) | Deploying or upgrading production systems. |
| [Post-Launch Operations](post-launch.md) | Running a live protocol. |
| [Frontend Security](frontend.md) | Shipping user-facing dapps. |
| [Supply Chain Security](supply-chain.md) | Trusting dependencies, CI/CD, and build artifacts. |
| [Multisig and Governance](multisig.md) | Assigning privileged authority. |
| [Wallet Security](wallet.md) | Protecting users and signers. |
| [SOC and Incident Response](soc-ir.md) | Monitoring and responding to incidents. |
| [Bug Bounty Readiness](bug-bounty.md) | Opening public vulnerability disclosure. |
| [Account Abstraction Readiness](account-abstraction.md) | Shipping ERC-4337 smart accounts, paymasters, bundlers, or session keys. |
| [Bridge and Cross-Chain Readiness](bridge-cross-chain.md) | Adding cross-chain messaging, bridges, relayers, or canonical asset flows. |
| [Oracle, Liquidation, and MEV Readiness](oracle-mev.md) | Depending on feeds, keepers, liquidations, auctions, perps, or ordering-sensitive flows. |
| [Incident War Room](incident-war-room.md) | Running the first hour of exploit, frontend, signer, bridge, or oracle response. |
| [Solana Program Readiness](solana-program.md) | Reviewing Anchor/native Rust programs, PDAs, CPIs, and account lifecycle. |

## Checklist Rule

Every checked item should have evidence: a PR, test, script output, transaction,
dashboard, policy, runbook, or owner.
