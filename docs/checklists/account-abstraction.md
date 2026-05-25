---
title: Account Abstraction Readiness Checklist
description: Evidence-based readiness gates for ERC-4337 wallets, paymasters, bundlers, session keys, and smart account integrations.
---

# Account Abstraction Readiness

| Gate | Evidence | Owner | Pass condition | Common failure |
| --- | --- | --- | --- | --- |
| UserOperation lifecycle is modeled | Diagram for client, account, paymaster, bundler, mempool, EntryPoint, and execution. | Wallet lead | The team can explain validation, simulation, inclusion, payment, failure, and replay behavior. | Only on-chain contracts are reviewed while bundler and paymaster assumptions remain implicit. |
| Paymaster griefing is bounded | Stake/deposit policy, `postOp` behavior, sponsorship limits, throttling, and abuse monitoring. | Security lead | A malicious user cannot cheaply drain or disable sponsorship. | Paymaster business rules live off-chain without testable failure modes. |
| Replay and delegation are explicit | Nonce policy, chain binding, session key scope, expiry, revocation, and signature domain. | Wallet lead | A signed operation cannot be reused beyond intended account, chain, time, or permission. | Session keys accumulate broad authority for convenience. |
| Bundler assumptions are monitored | Simulation requirements, mempool policy, reputation behavior, fallback bundlers, and metrics. | Infrastructure lead | Bundler behavior is observable and failure does not silently strand users. | Any bundler endpoint is treated as interchangeable infrastructure. |

## References

- [ERC-4337 resources](https://docs.erc4337.io/resources/)
- [ERC-4337 simulation requirements](https://docs.erc4337.io/bundlers/simulation-requirements/)
- [OpenZeppelin EIP-4337 audit](https://www.openzeppelin.com/news/eth-foundation-account-abstraction-audit)
