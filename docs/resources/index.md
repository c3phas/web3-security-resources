# Curated Resources

Use this section as a working index. The tiers are editorial judgments based on
practical security value, maintenance, accessibility, and reputation.

## Must Learn

| Resource | Category | Track | Note |
| --- | --- | --- | --- |
| [OWASP Smart Contract Top 10 2026](https://owasp.org/www-project-smart-contract-top-10/) | Standard | EVM, protocol | Current shared vocabulary for high-impact smart contract risks. |
| [OWASP SCSVS](https://scs.owasp.org/SCSVS/) | Standard | Auditor | Verification standard for smart contract assessments. |
| [OWASP SCSTG](https://scs.owasp.org/SCSTG/) | Testing guide | Auditor | Test guide aligned to smart contract security controls. |
| [OpenZeppelin Readiness Guide](https://www.openzeppelin.com/readiness-guide) | Audit readiness | Protocol | Practical preparation model before external review. |
| [SEAL Frameworks](https://frameworks.securityalliance.org/) | Operations | Protocol | Security program and incident readiness frameworks. |
| [Foundry Book](https://book.getfoundry.sh/) | Tooling | EVM | Core EVM development and audit test framework. |
| [Solidity Docs](https://docs.soliditylang.org/) | Language | EVM | Primary compiler and language reference. |
| [Solodit](https://solodit.cyfrin.io/) | Vulnerability intel | Auditor | Searchable public finding and contest intelligence. |
| [DeFiHackLabs](https://github.com/SunWeb3Sec/DeFiHackLabs) | Exploit study | Auditor | Reproduce historical DeFi incidents. |
| [Mastering Ethereum](https://github.com/ethereumbook/ethereumbook) | Fundamentals | Beginner | Durable blockchain and EVM background. |

## Use in Real Audits

| Resource | Category | Track | Note |
| --- | --- | --- | --- |
| [Slither](https://github.com/crytic/slither) | Static analysis | EVM | Fast bug triage, inheritance graphs, and printers. |
| [Aderyn](https://github.com/Cyfrin/aderyn) | Static analysis | EVM | Auditor-oriented static analysis and reports. |
| [Echidna](https://github.com/crytic/echidna) | Fuzzing | EVM | Property-based fuzzing. |
| [Medusa](https://github.com/crytic/medusa) | Fuzzing | EVM | High-performance stateful fuzzing. |
| [Halmos](https://github.com/a16z/halmos) | Symbolic testing | EVM | Symbolic execution for Foundry tests. |
| [Tenderly](https://tenderly.co/) | Debugging | EVM | Transaction simulation, forks, and debugging. |
| [Sourcify](https://sourcify.dev/) | Verification | EVM | Source-code verification metadata. |
| [Immunefi](https://immunefi.com/) | Bug bounty | Protocol | Bounty hosting and disclosure workflows. |
| [Sherlock](https://www.sherlock.xyz/) | Contests | Auditor | Competitive audits and coverage markets. |
| [Cantina](https://cantina.xyz/) | Contests | Auditor | Competitive audits, bounties, and private engagements. |

## Situational / Advanced

| Resource | Category | Track | Note |
| --- | --- | --- | --- |
| [Certora Prover](https://www.certora.com/prover) | Formal methods | EVM | Specification and formal verification for high-value systems. |
| [Runtime Verification](https://runtimeverification.com/) | Formal methods | Multi-chain | Semantics and verification services. |
| [0xPARC](https://learn.0xparc.org/) | ZK | ZK | Strong ZK education and research community. |
| [zkSecurity](https://www.zksecurity.xyz/) | ZK | ZK | ZK audit research and vulnerability guidance. |
| [Starknet Docs](https://docs.starknet.io/) | Chain docs | Cairo | Current Starknet platform documentation. |
| [Move Book](https://move-book.com/) | Language | Move | Practical Move language reference. |
| [Anchor Docs](https://www.anchor-lang.com/docs) | Framework | Solana | Solana program development and account constraints. |
| [Token-2022](https://spl.solana.com/token-2022) | Token standard | Solana | Extension-heavy token surface. |

## Paid / Certification

| Resource | Category | Track | Note |
| --- | --- | --- | --- |
| [Certora Prover](https://www.certora.com/prover) | Formal methods | EVM | Commercial tooling; valuable for protocols with formal specs. |
| [AuditBase](https://www.auditbase.com/) | Training/tools | EVM | Paid security learning and scanning options. |
| [Offensive Security](https://www.offsec.com/) | General security | Full-stack | Useful for web, infra, and attacker methodology. |
| [SANS SEC554](https://www.sans.org/cyber-security-courses/blockchain-smart-contract-security/) | Training | Protocol | Structured paid blockchain and smart contract security training. |

## Watchlist

| Resource | Category | Track | Note |
| --- | --- | --- | --- |
| [AIxCC](https://aicyberchallenge.com/) | AI security | AI-assisted | Watch for program-analysis lessons that transfer to audits. |
| [Wake](https://ackeeblockchain.com/wake/) | Testing | EVM | Growing Python-based Solidity testing and analysis framework. |
| [GoPlus Security](https://gopluslabs.io/) | User protection | Full-stack | Transaction and token risk APIs for wallet/app defenses. |
| [Blockaid](https://www.blockaid.io/) | User protection | Full-stack | Wallet and dapp threat detection. |
| [Hypernative](https://www.hypernative.io/) | Monitoring | Protocol | Real-time risk and exploit detection platform. |

The machine-readable catalog lives in [resources.yml](../data/resources.yml).
