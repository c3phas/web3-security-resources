# Reports and Vulnerability Intelligence

## Finding Search and Public Reports

| Resource | Tier | Use |
| --- | --- | --- |
| [Solodit](https://solodit.cyfrin.io/) | Must learn | Search public contest and audit findings. |
| [Code4rena Reports](https://code4rena.com/reports) | Use in real audits | Public competitive audit findings. |
| [Sherlock Audits](https://audits.sherlock.xyz/) | Use in real audits | Reports from Sherlock contests and audits. |
| [Cantina Competitions](https://cantina.xyz/competitions) | Use in real audits | Contest scopes and findings. |
| [Spearbit Portfolio](https://github.com/spearbit/portfolio) | Use in real audits | Public reports and specialty checklists. |
| [OpenZeppelin Audit Reports](https://www.openzeppelin.com/security-audits) | Use in real audits | Mature report format and remediation style. |
| [Trail of Bits Publications](https://github.com/trailofbits/publications) | Use in real audits | Public reports and research. |
| [ConsenSys Diligence Audits](https://consensys.io/diligence/audits/) | Use in real audits | EVM audit reports and tooling references. |

## Incident and Exploit Study

| Resource | Tier | Use |
| --- | --- | --- |
| [DeFiHackLabs](https://github.com/SunWeb3Sec/DeFiHackLabs) | Must learn | Reproduce exploits with runnable PoCs. |
| [Rekt](https://rekt.news/) | Must learn | Incident narratives and loss context. |
| [Immunefi Blog](https://immunefi.com/blog/) | Use in real audits | Vulnerability writeups and ecosystem loss reports. |
| [ChainSecurity Blog](https://www.chainsecurity.com/blog) | Use in real audits | Research and audit insights. |
| [SlowMist Hacked Archive](https://hacked.slowmist.io/) | Use in real audits | Incident database and trend tracking. |
| [BlockSec Blog](https://blocksec.com/blog) | Use in real audits | Exploit analysis and transaction traces. |
| [PeckShield Alerts](https://twitter.com/peckshield) | Watchlist | Fast incident signal; verify independently. |

## How to Study a Report

For each finding, extract:

- root cause
- impacted asset
- missing invariant or authorization check
- exploit preconditions
- why tests missed it
- fix pattern
- monitoring rule that would detect exploitation
