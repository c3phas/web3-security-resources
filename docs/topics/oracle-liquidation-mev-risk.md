---
title: Oracle, Liquidation, and MEV Risk
description: Review price feeds, stale data, liquidation incentives, transaction ordering, perps, AMMs, vaults, and circuit breakers.
---

# Oracle, Liquidation, and MEV Risk

Oracle integrations are not safe just because the provider is reputable. Teams
still need feed selection, stale-value handling, decimals, sequencer status,
fallbacks, liquidation stress tests, and circuit breakers.

## Review questions

- What happens when the feed is stale, delayed, wrong, missing, or unavailable?
- Are liquidations economically viable during volatile markets and gas spikes?
- Can transaction ordering, sandwiching, backrunning, or stale updates move value?

## Review workflow

1. List feed sources, decimals, heartbeat, deviation, sequencer status, and fallback behavior.
2. Stress test solvency, liquidation, and keeper incentives under volatility.
3. Simulate MEV-sensitive paths before launch.
4. Add circuit breakers that operators can actually execute and restart safely.

## Common risks

| Risk | What to verify |
| --- | --- |
| Stale values | Heartbeat, age checks, fallback, and sequencer status. |
| Decimal mismatch | Unit tests for every feed and asset path. |
| Keeper failure | Incentive, gas, liquidity, and backlog stress tests. |
| Unsafe restart | Pause, resume, recovery, and accounting reconciliation. |

## Linked checklists

- [Oracle, liquidation, and MEV readiness](../checklists/oracle-mev.md)
- [Launch readiness](../checklists/launch.md)
- [Post-launch operations](../checklists/post-launch.md)

## FAQ

**Where does MEV enter the review?**
Review swaps, liquidations, oracle updates, auctions, withdrawals, perps funding,
and privileged operations that depend on ordering.

**What should a launch gate require?**
Feed assumptions, stale-data tests, stress simulations, keeper failure handling,
and operable circuit breakers.

## Starting resources

- [Chainlink feed selection docs](https://docs.chain.link/data-feeds/selecting-data-feeds)
- [Tenderly docs](https://docs.tenderly.co/)
- [BlockSec Phalcon simulator](https://docs.blocksec.com/phalcon/phalcon-explorer/simulator)
