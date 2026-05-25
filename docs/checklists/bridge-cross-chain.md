---
title: Bridge and Cross-Chain Readiness Checklist
description: Evidence-based readiness gates for bridges, cross-chain messages, relayers, guardians, liquidity accounting, and emergency pause controls.
---

# Bridge and Cross-Chain Readiness

| Gate | Evidence | Owner | Pass condition | Common failure |
| --- | --- | --- | --- | --- |
| Trust boundaries are explicit | Guardian/validator set, relayers, finality assumptions, message format, replay rules, and governance path. | Protocol architect | Every chain and actor boundary has a failure-mode owner. | The bridge is described as infrastructure instead of a security-critical subsystem. |
| Message validation is complete | Source chain, destination chain, nonce, payload, replay protection, finality, and authorization tests. | Engineering lead | Forged, replayed, delayed, or reordered messages fail safely. | Happy-path relay tests pass but adversarial message tests are missing. |
| Liquidity and accounting reconcile | Mint/burn/lock/unlock invariant tests, rate limits, pause policy, and reconciliation dashboards. | Security lead | Supply mismatches and stuck transfers are detected quickly. | Accounting assumes all relayed events are final and correct. |
| Incident pause is scoped | Per-chain pause, asset pause, rate-limit controls, signer rules, and user communications. | Incident commander | The team can contain one route without unnecessary global damage. | Emergency controls are too broad to use or too narrow to stop loss. |

## References

- [Wormhole security](https://docs.wormhole.com/protocol/security/)
- [SEAL Frameworks](https://frameworks.securityalliance.org/)
- [DefiLlama hacks](https://defillama.com/hacks)
