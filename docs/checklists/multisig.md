---
title: Multisig and Governance
description: Multisig and Governance page in the Web3 Security Resources 2026 hub.
---

# Multisig and Governance

- Signers are independent and reachable.
- Threshold is appropriate for value at risk and response time.
- Hardware wallets are used for production signing.
- Transaction simulation and human-readable review are required.
- Emergency procedures define who signs, where, and under what evidence.
- Timelocks apply to non-emergency changes.
- Admin roles are inventoried and monitored.
- Governance proposals include security impact and rollback notes.
- Signer rotation and compromise response are rehearsed.


## Evidence gates

| Gate | Evidence | Owner | Pass condition | Common failure |
| --- | --- | --- | --- | --- |
| Signer set is appropriate | Signer list, hardware policy, geography, role, quorum, backup, and replacement plan. | Protocol founder | Signer model fits asset value, response needs, and compromise risk. | Quorum is copied from another project without matching risk. |
| Transactions are simulated | Pre-sign trace, decoded calldata, target verification, value transfer, and expected state diff. | Operations lead | Signers understand what they approve before signing. | Signers rely on a human summary instead of decoded and simulated evidence. |
| Signer compromise has a runbook | Replacement steps, freeze actions, communication templates, device guidance, and case owner. | Incident commander | A lost or compromised signer can be handled without halting indefinitely. | Signer recovery is treated as an informal founder chat. |
