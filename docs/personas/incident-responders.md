---
title: For Incident Responders
description: A Web3 incident response path for containment, evidence preservation, transaction reproduction, signer safety, and user communications.
---

# For Incident Responders

Focus on containment, evidence preservation, transaction reproduction, signer
safety, user communications, and post-incident control fixes.

## 30 / 60 / 90-day path

| Window | What to do | Evidence to keep |
| --- | --- | --- |
| 30 days | Define severity triggers, war-room roles, public comms owners, legal escalation, and evidence templates. | Severity matrix, role card, case template, comms draft. |
| 60 days | Add simulation and trace tools, signer replacement steps, and wallet-drainer reporting paths. | Trace examples, transaction review checklist, takedown packet. |
| 90 days | Run a full tabletop with executives, engineers, comms, legal, support, and partners. | Exercise notes, remediation tracker, monitoring updates. |

## Must-read pages

- [Incident war room](../checklists/incident-war-room.md)
- [SOC and incident response](../checklists/soc-ir.md)
- [Incident response resources](../resources/incident-response.md)
- [Wallet security](../checklists/wallet.md)

## Checklists to use first

- [Incident war room](../checklists/incident-war-room.md)
- [SOC and incident response](../checklists/soc-ir.md)
- [Post-launch operations](../checklists/post-launch.md)

## First 10 resources

1. [SEAL 911](https://securityalliance.org/seal-911)
2. [SEAL Frameworks](https://frameworks.securityalliance.org/)
3. [BlockSec Phalcon simulator](https://docs.blocksec.com/phalcon/phalcon-explorer/simulator)
4. [Tenderly docs](https://docs.tenderly.co/)
5. [Chainabuse](https://www.chainabuse.com/)
6. [MetaMask eth-phishing-detect](https://github.com/MetaMask/eth-phishing-detect)
7. [DefiLlama hacks](https://defillama.com/hacks)
8. [Safe Transaction Service](https://docs.safe.global/core-api/transaction-service-overview)
9. [Wormhole security](https://wormhole.com/security/)
10. [DigiBastion Threat Intel](https://www.digibastion.com/threat-intel)

## Common failure

Incident teams often patch before preserving evidence. Snapshot transactions,
traces, DNS, frontend assets, logs, screenshots, public reports, and timestamps
before emergency fixes erase root-cause material.
