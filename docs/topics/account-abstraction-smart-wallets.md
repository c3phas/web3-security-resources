---
title: Account Abstraction and Smart Wallets
description: Review ERC-4337, smart accounts, paymasters, bundlers, session keys, and wallet UX as one security system.
---

# Account Abstraction and Smart Wallets

ERC-4337 reviews span contracts, clients, bundlers, paymasters, simulation,
mempool policy, wallet UX, and monitoring. Treat the system as a distributed
security boundary, not just a contract scope.

## Review questions

- Can a `UserOperation` be replayed, invalidated, censored, or executed outside the assumed lifecycle?
- Can a paymaster be griefed, drained, throttled, or forced into unsafe `postOp` behavior?
- Does wallet UX represent delegated authority, gas sponsorship, and failure modes clearly?

## Review workflow

1. Map client, account, paymaster, bundler, EntryPoint, mempool, and execution.
2. Review off-chain simulation requirements alongside contract validation.
3. Test replay, nonce, chain binding, session key scope, revocation, and failure handling.
4. Monitor bundler health, paymaster balances, rejection patterns, and sponsorship limits.

## Common risks

| Risk | What to verify |
| --- | --- |
| Implicit off-chain assumptions | Simulation, reputation, mempool policy, bundler fallback, and metrics. |
| Broad session keys | Scope, expiry, spending limits, chain binding, and revocation. |
| Paymaster griefing | Stake, deposit, sponsorship policy, `postOp`, throttling, and abuse monitoring. |
| Weak user intent display | Clear transaction preview and delegated authority language. |

## Linked checklists

- [Account abstraction readiness](../checklists/account-abstraction.md)
- [Wallet security](../checklists/wallet.md)
- [Pre-audit readiness](../checklists/pre-audit.md)

## FAQ

**Is account abstraction only a contract audit problem?**
No. ERC-4337 security spans contracts, bundlers, paymasters, client UX, mempool
policy, simulation, and monitoring.

**What should teams review first?**
Start with the `UserOperation` lifecycle, replay protection, paymaster economics,
session-key scope, and what the wallet shows before signing.

## Starting resources

- [ERC-4337 resources](https://docs.erc4337.io/resources/)
- [ERC-4337 simulation requirements](https://docs.erc4337.io/bundlers/simulation-requirements/)
- [OpenZeppelin EIP-4337 audit](https://www.openzeppelin.com/news/eth-foundation-account-abstraction-audit)
