---
title: Move Auditor
description: Move Auditor page in the Web3 Security Resources 2026 hub.
---

# Move Auditor

Audience: auditors reviewing Aptos, Sui, and Move-based protocols.

## Outcomes

- Understand resources, abilities, capabilities, modules, objects, and package upgrades.
- Review object ownership, capability leakage, signer assumptions, and resource conservation.
- Use Move Prover and local test frameworks for specification-backed review.

## Roadmap

| Stage | Focus | Proof of work |
| --- | --- | --- |
| Move language | Resources, abilities, generics, modules, visibility | Explain why resources cannot be copied or dropped accidentally. |
| Chain model | Aptos accounts or Sui objects, packages, upgrades | Map ownership and authority for a sample protocol. |
| Security review | Capabilities, object access, coin/resource flows | Find an authorization or conservation bug in a toy app. |
| Verification | Move Prover, specs, abort conditions, invariants | Write one useful spec for a critical function. |
| Operations | Upgrade governance, admin controls, monitoring | Produce a launch checklist for a Move package. |

## Must Learn

| Resource | Why |
| --- | --- |
| [Move Book](https://move-book.com/) | Practical language introduction and examples. |
| [Aptos Move Docs](https://aptos.dev/en/build/smart-contracts) | Aptos-specific module, account, and tooling reference. |
| [Sui Move Docs](https://docs.sui.io/concepts/sui-move-concepts) | Sui object model and Move concepts. |
| [Move Prover](https://aptos.dev/en/build/smart-contracts/prover) | Formal specification and verification workflow. |
| [Move Security Guidelines](https://aptos.dev/en/build/smart-contracts/move-security-guidelines) | Common Move-specific security practices. |

## Use in Real Audits

- Track object/resource ownership from entry function to final state.
- Identify which capabilities can mint, burn, pause, upgrade, withdraw, or transfer.
- Check whether friend modules and package visibility expand trusted code unexpectedly.
- Confirm upgrade paths cannot bypass invariants or governance.
- Verify abort behavior and error paths do not lock funds or strand objects.
