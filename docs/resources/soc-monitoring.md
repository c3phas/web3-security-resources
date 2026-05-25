# SOC and Monitoring

Protocol monitoring should cover contracts, privileged actions, frontend drift,
DNS, dependencies, wallets, APIs, and governance.

## Monitoring Resources

| Resource | Tier | Use |
| --- | --- | --- |
| [Forta](https://forta.org/) | Use in real audits | On-chain detection bots and alerting. |
| [OpenZeppelin Defender Monitor](https://www.openzeppelin.com/defender) | Use in real audits | Contract event and admin monitoring. |
| [Hypernative](https://www.hypernative.io/) | Paid / certification | Real-time exploit and anomaly detection. |
| [Tenderly Alerts](https://tenderly.co/) | Use in real audits | Transaction and contract monitoring. |
| [Dune](https://dune.com/) | Situational / advanced | Custom dashboards and queries. |
| [EigenPhi](https://eigenphi.io/) | Situational / advanced | MEV and transaction behavior analysis. |
| [DigiBastion](https://digibastion.com/) | Watchlist | Maintainer-labeled DNS/domain posture resource. |
| [VANTAGE](https://vantage.security/) | Watchlist | Maintainer-labeled protocol intelligence and risk analytics resource. |

## Alert Categories

- privileged role changes
- proxy upgrades and implementation changes
- pause/unpause and emergency action calls
- oracle deviation and stale feeds
- TVL and reserve anomalies
- bridge mint/burn mismatches
- abnormal approvals, drains, or token movements
- frontend asset hash drift
- DNS, TLS, registrar, and nameserver changes
- governance proposal creation and execution
