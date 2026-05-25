---
title: For Frontend and Wallet Engineers
description: A Web3 security path for protecting wallet-facing pages, signing flows, account abstraction, browser code, and frontend supply chains.
---

# For Frontend and Wallet Engineers

Protect users where transactions are composed, displayed, simulated, approved,
and submitted. Browser-shipped code is part of the trust boundary.

## 30 / 60 / 90-day path

| Window | What to do | Evidence to keep |
| --- | --- | --- |
| 30 days | Inventory scripts, wallet connectors, RPC keys, signing flows, public env vars, and privileged routes. | Runtime script list, key inventory, signing-flow diagram. |
| 60 days | Create signing-path, frontend, supply-chain, and account-abstraction evidence gates. | Route baseline, transaction previews, dependency approvals. |
| 90 days | Add recurring drift monitoring and rehearse wallet-drainer response. | Drift alerts, rollback drill, takedown packet, user comms draft. |

## Must-read pages

- [Frontend security](../checklists/frontend.md)
- [Wallet security](../checklists/wallet.md)
- [Account abstraction and smart wallets](../topics/account-abstraction-smart-wallets.md)
- [Frontend and supply chain resources](../resources/frontend-supply-chain.md)

## Checklists to use first

- [Frontend security](../checklists/frontend.md)
- [Wallet security](../checklists/wallet.md)
- [Account abstraction readiness](../checklists/account-abstraction.md)

## First 10 resources

1. [ERC-4337 resources](https://docs.erc4337.io/resources/)
2. [ERC-4337 simulation requirements](https://docs.erc4337.io/bundlers/simulation-requirements/)
3. [OpenZeppelin EIP-4337 audit](https://www.openzeppelin.com/news/eth-foundation-account-abstraction-audit)
4. [Tenderly docs](https://docs.tenderly.co/)
5. [BlockSec Phalcon simulator](https://docs.blocksec.com/phalcon/phalcon-explorer/simulator)
6. [MetaMask eth-phishing-detect](https://github.com/MetaMask/eth-phishing-detect)
7. [Safe Help Center](https://help.safe.global/)
8. [GoPlus Security](https://gopluslabs.io/)
9. [Blockaid](https://www.blockaid.io/)
10. [VANTAGE by DigiBastion](https://vantage.digibastion.com/)

## Common failure

Teams review source code but not the browser-observed runtime. Wallet-facing
pages need evidence for domains, scripts, modals, RPCs, transaction previews,
dependencies, and rollback paths.
