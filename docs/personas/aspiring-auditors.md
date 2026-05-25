---
title: For Aspiring Auditors
description: A 30/60/90-day path for learning smart contract auditing through exploit reproduction, invariants, public reports, and chain-specific testing.
---

# For Aspiring Auditors

Build skill by pairing exploit history, ecosystem-specific testing, audit
reports, and repeatable review artifacts. The goal is not to collect tools. The
goal is to reason from code and state to exploitability, impact, and remediation.

## 30 / 60 / 90-day path

| Window | What to do | Evidence to keep |
| --- | --- | --- |
| 30 days | Read three public audit reports, reproduce two historical bugs, and set up Foundry plus one non-EVM test stack. | Notes, fork tests, traces, failing tests, fixed tests. |
| 60 days | Build a review notebook with assets, actors, invariants, trust assumptions, privileged roles, and known unknowns. | Threat model, invariant list, issue template, severity rubric. |
| 90 days | Review a small open-source protocol or toy scope and publish a responsible non-sensitive write-up. | Report excerpt, PoC tests, remediation notes, reviewer feedback. |

## Must-read pages

- [AI-era smart contract auditor](../roadmaps/ai-era-smart-contract-auditor.md)
- [Analysis methods](../resources/analysis-methods.md)
- [Reports and vulnerability intelligence](../resources/reports-and-vuln-intel.md)
- [Solana testing and audit tooling](../topics/solana-testing-audit-tooling.md)

## Checklists to use first

- [Pre-audit readiness](../checklists/pre-audit.md)
- [Account abstraction readiness](../checklists/account-abstraction.md)
- [Solana program readiness](../checklists/solana-program.md)

## First 10 resources

1. [OWASP SCSVS](https://scs.owasp.org/SCSVS/)
2. [OWASP SCSTG](https://scs.owasp.org/SCSTG/)
3. [Solodit](https://solodit.cyfrin.io/)
4. [DeFiHackLabs](https://github.com/SunWeb3Sec/DeFiHackLabs)
5. [OpenZeppelin EIP-4337 audit](https://www.openzeppelin.com/news/eth-foundation-account-abstraction-audit)
6. [Solana Program Security course](https://solana.com/developers/courses/program-security)
7. [Mollusk](https://solana.com/docs/programs/testing/mollusk)
8. [Anchor LiteSVM](https://www.anchor-lang.com/docs/testing/litesvm)
9. [Tenderly docs](https://docs.tenderly.co/)
10. [BlockSec Phalcon simulator](https://docs.blocksec.com/phalcon/phalcon-explorer/simulator)

## Common failure

New auditors often jump from tool output to severity without proving the exploit
path. Treat every tool result and AI suggestion as a hypothesis until a test,
trace, invariant violation, or source-level argument proves it.
