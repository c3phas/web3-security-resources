---
title: Oracle, Liquidation, and MEV Readiness Checklist
description: Evidence-based readiness gates for price feeds, liquidation economics, MEV-sensitive flows, perps, AMMs, vaults, and circuit breakers.
---

# Oracle, Liquidation, and MEV Readiness

| Gate | Evidence | Owner | Pass condition | Common failure |
| --- | --- | --- | --- | --- |
| Feed assumptions are encoded | Feed source, decimals, heartbeat, deviation, stale threshold, sequencer status, and fallback. | Protocol engineer | Bad, stale, missing, or delayed oracle data cannot create unsafe accounting. | Tests use perfect oracle values and miss stale or decimal mismatch paths. |
| Liquidation incentives are tested | Edge-case simulations across volatility, liquidity, oracle delay, gas, and keeper failure. | Protocol engineer | Liquidations remain economically viable and bounded during stress. | The protocol is solvent only under normal liquidity. |
| Ordering risk is reviewed | MEV analysis for sandwiching, backrunning, stale updates, auction behavior, and privileged sequencing. | Security lead | Known ordering attacks are mitigated or explicitly accepted. | MEV is dismissed as market risk even when contract logic amplifies it. |
| Circuit breakers are operable | Pause thresholds, admin path, monitoring, public comms, and safe recovery steps. | Operations lead | The team can stop unsafe operation and restart without corrupting state. | Circuit breakers exist but were never tested with real failure scenarios. |

## References

- [Chainlink feed selection docs](https://docs.chain.link/data-feeds/selecting-data-feeds)
- [Tenderly docs](https://docs.tenderly.co/)
- [BlockSec Phalcon simulator](https://docs.blocksec.com/phalcon/phalcon-explorer/simulator)
