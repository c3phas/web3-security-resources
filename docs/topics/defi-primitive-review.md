---
title: DeFi Primitive Review
description: Review AMMs, lending markets, vaults, perps, restaking, RWAs, and stablecoins by invariants, accounting, liquidity, and control boundaries.
---

# DeFi Primitive Review

Use shared gates for ownership, invariants, and monitoring, then add
primitive-specific tests for accounting, liquidity, ordering, or compliance
assumptions.

## Review questions

- What assets can be minted, burned, borrowed, withdrawn, restaked, bridged, or liquidated?
- Which accounting invariant must hold across every state transition?
- Which admin, oracle, bridge, or frontend path can change user solvency?

## Review workflow

1. Write primitive-specific invariants before reading implementation details.
2. Map external dependencies and privileged controls.
3. Stress test accounting under fees, rounding, liquidity cliffs, oracle delays, and pause states.
4. Connect launch gates to monitoring and accepted-risk expiry dates.

## Primitive prompts

| Primitive | Review focus |
| --- | --- |
| AMM | Reserves, fees, rounding, oracle use, sandwich resistance, pool initialization. |
| Lending | Collateral factors, liquidation, interest accrual, bad debt, oracle delay. |
| Vault | Share accounting, deposit/withdraw ordering, strategy loss, fee extraction. |
| Perps | Funding, liquidations, oracle freshness, keeper incentives, insurance fund. |
| Restaking | Slashing, operator delegation, withdrawal delay, cross-protocol contagion. |
| RWA/stablecoin | Mint authority, redemption, blacklist/freeze, reserves, compliance oracle. |

## Linked checklists

- [Pre-audit readiness](../checklists/pre-audit.md)
- [Oracle, liquidation, and MEV readiness](../checklists/oracle-mev.md)
- [Launch readiness](../checklists/launch.md)

## FAQ

**What is the first artifact to ask for?**
Ask for a concise invariant document that states what must never be false, even
during stress, pause, or admin action.

**Should every primitive use the same checklist?**
No. Use shared readiness gates and add primitive-specific invariants and stress
tests.

## Starting resources

- [OWASP SCSVS](https://scs.owasp.org/SCSVS/)
- [OpenZeppelin Contracts docs](https://docs.openzeppelin.com/contracts/)
- [DeFiHackLabs](https://github.com/SunWeb3Sec/DeFiHackLabs)
