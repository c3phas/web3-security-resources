---
title: Bridge and Cross-Chain Security
description: Review cross-chain messaging, finality, relayers, guardians, liquidity accounting, governance, and emergency controls.
---

# Bridge and Cross-Chain Security

Bridge and messaging failures cross technical, governance, liquidity, and
operations boundaries. A normal contract checklist is not enough.

## Review questions

- What actors can approve, relay, reorder, censor, replay, or upgrade messages?
- How does the system detect supply mismatch, stuck transfers, and finality confusion?
- Which route can be paused without unnecessary global damage?

## Review workflow

1. Draw source chain, destination chain, message, finality, governance, and liquidity boundaries.
2. Test forged, replayed, delayed, reordered, and partially executed messages.
3. Monitor supply reconciliation, relay health, queue delays, and unexpected route volume.
4. Rehearse route-specific pause and recovery.

## Common risks

| Risk | What to verify |
| --- | --- |
| Finality mismatch | Confirmation assumptions per chain and rollback behavior. |
| Replay | Source chain, destination chain, nonce, payload, and domain separators. |
| Guardian or relayer compromise | Quorum, key management, monitoring, and emergency replacement. |
| Pause blast radius | Per-chain, per-route, or per-asset containment. |

## Linked checklists

- [Bridge and cross-chain readiness](../checklists/bridge-cross-chain.md)
- [Incident war room](../checklists/incident-war-room.md)
- [Multisig and governance](../checklists/multisig.md)

## FAQ

**Why do bridges need separate gates?**
Bridge failures often involve message validation, finality, privileged relayers,
liquidity accounting, governance, and emergency response at the same time.

**What evidence matters most?**
Message validation tests, finality assumptions, reconciliation dashboards, pause
procedures, and privileged role ownership.

## Starting resources

- [Wormhole security](https://wormhole.com/security/)
- [DefiLlama hacks](https://defillama.com/hacks)
- [SEAL Frameworks](https://frameworks.securityalliance.org/)
