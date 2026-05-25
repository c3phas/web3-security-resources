# Solidity/EVM Auditor

Audience: aspiring auditors, contest participants, Solidity engineers, and
security reviewers working on EVM protocols.

## Outcomes

- Review access control, accounting, oracle, upgradeability, governance, and liquidation flows.
- Use Foundry, Slither, Aderyn, Echidna, Medusa, Halmos, and debuggers effectively.
- Write minimal PoCs and invariant tests that prove impact.
- Communicate findings with root cause, exploit path, impact, and fix guidance.

If your main question is whether smart contract auditing remains a good path as
AI tools improve, read the [AI-era smart contract auditor roadmap](ai-era-smart-contract-auditor.md)
after this page. This roadmap builds the base; the AI-era roadmap explains how
to stay relevant as tool-assisted review becomes normal.

## Roadmap

| Stage | Focus | Proof of work |
| --- | --- | --- |
| Fundamentals | Solidity, EVM calls, storage, events, gas, ERC standards | Explain five common storage/call bugs and reproduce one. |
| Tooling | Foundry, Slither, Aderyn, Echidna, Halmos, Tenderly | Run a baseline tool pass and triage false positives. |
| DeFi primitives | AMMs, lending, staking, vaults, bridges, oracles | Build threat models for three protocol types. |
| Manual review | State machines, permissions, math, external calls, upgrade paths | Produce a report on a real contest or public codebase. |
| Advanced testing | Stateful fuzzing, invariants, symbolic execution, differential tests | Add invariants that catch a known exploit class. |

## Must Learn

| Resource | Why |
| --- | --- |
| [Solidity Docs](https://docs.soliditylang.org/) | Source of truth for compiler behavior and language semantics. |
| [Foundry Book](https://book.getfoundry.sh/) | Build, test, fuzz, fork, and debug modern EVM systems. |
| [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/) | Reference implementations for ERCs, access control, and upgradeable patterns. |
| [OWASP Smart Contract Top 10 2026](https://owasp.org/www-project-smart-contract-top-10/) | Shared risk taxonomy for current smart contract weaknesses. |
| [OWASP SCSVS](https://scs.owasp.org/SCSVS/) | Structured verification standard for smart contract assessments. |
| [Secureum](https://secureum.substack.com/) | Solidity security drills and interview-grade review concepts. |

## Use in Real Audits

| Tool or reference | Use |
| --- | --- |
| [Slither](https://github.com/crytic/slither) | Static analysis, inheritance graphs, printers, and quick bug triage. |
| [Aderyn](https://github.com/Cyfrin/aderyn) | Static analysis with auditor-friendly reporting. |
| [Echidna](https://github.com/crytic/echidna) | Property-based fuzzing for Solidity systems. |
| [Medusa](https://github.com/crytic/medusa) | High-performance fuzzing for complex EVM targets. |
| [Halmos](https://github.com/a16z/halmos) | Symbolic testing for Foundry tests. |
| [hevm](https://github.com/ethereum/hevm) | Symbolic execution and EVM debugging. |
| [Tenderly](https://tenderly.co/) | Transaction debugging, simulations, and fork analysis. |
| [Sourcify](https://sourcify.dev/) | Source verification and contract metadata lookup. |

## Situational / Advanced

- Formal verification with [Certora Prover](https://www.certora.com/prover) or
  [Runtime Verification](https://runtimeverification.com/).
- MEV-aware protocol analysis with oracle, liquidation, and sandwich-risk models.
- Cross-chain review for bridges, light clients, messaging, replay, and finality assumptions.
- Upgrade governance review for timelocks, proxy admin, multisig, and emergency roles.

## Finding Quality Bar

A good finding includes: affected code, preconditions, exploit path, realistic
impact, minimal PoC, severity reasoning, suggested fix, and residual risk. A
tool warning without manual validation is not a finding.
