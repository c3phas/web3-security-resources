---
title: Incident War Room Checklist
description: First-hour evidence and containment gates for exploits, frontend compromise, wallet drainers, signer compromise, and bridge or oracle incidents.
---

# Incident War Room

| Gate | Evidence | Owner | Pass condition | Common failure |
| --- | --- | --- | --- | --- |
| Command is assigned | Incident commander, engineering lead, comms lead, legal owner, scribe, and executive contact. | Security lead | The team knows who decides, who executes, and who communicates. | Everyone investigates but no one owns containment. |
| Containment options are ranked | Pause, upgrade, DNS/CDN action, frontend rollback, signer replacement, rate limits, and partner notification. | Incident commander | Actions are ordered by user harm reduction and reversibility. | Teams patch or post publicly before preserving evidence. |
| Evidence is snapshotted | Transactions, traces, contracts, signatures, DNS, frontend assets, screenshots, logs, reports, and timestamps. | Scribe | A later reviewer can reconstruct what happened and when. | Emergency fixes destroy root-cause evidence. |
| Public updates are controlled | Holding statement, affected assets, user action guidance, uncertainty labels, and next update time. | Comms lead | Users receive useful instructions without unsupported attribution or speculation. | Silence, overconfidence, or conflicting social posts worsen harm. |

## References

- [SEAL 911](https://securityalliance.org/seal-911)
- [Chainabuse](https://www.chainabuse.com/)
- [MetaMask eth-phishing-detect](https://github.com/MetaMask/eth-phishing-detect)
