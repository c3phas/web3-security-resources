# Analysis Methods

Good security work layers methods. No scanner, fuzzer, formal spec, AI model, or
manual review is enough alone. Use each method for what it is good at, then tie
the evidence back to protocol invariants and realistic impact.

## Static Analysis

Static analysis is the fastest way to build code understanding, catch common
patterns, and generate review leads. Treat findings as hypotheses until a human
confirms exploitability.

| Resource | Tier | Best use |
| --- | --- | --- |
| [Slither](https://github.com/crytic/slither) | Use in real audits | Solidity static analysis, inheritance graphs, printers, and custom detectors. |
| [Aderyn](https://github.com/Cyfrin/aderyn) | Use in real audits | Auditor-friendly reports and Solidity issue triage. |
| [Semgrep](https://semgrep.dev/) | Use in real audits | Custom rules for Solidity, TypeScript, APIs, CI, and offchain code. |
| [Solhint](https://github.com/protofire/solhint) | Use in real audits | Solidity linting and lightweight policy checks. |
| [Mythril](https://github.com/ConsenSysDiligence/mythril) | Situational / advanced | Bytecode-level symbolic analysis and bug hunting. |
| [Wake](https://github.com/Ackee-Blockchain/wake) | Watchlist | Python-based Solidity testing and analysis framework. |

## Dynamic Analysis and Debugging

Dynamic analysis shows what actually happens under realistic state, forked
chains, malicious inputs, and transaction traces.

| Resource | Tier | Best use |
| --- | --- | --- |
| [Foundry Fork Testing](https://book.getfoundry.sh/forge/fork-testing) | Must learn | Reproduce mainnet incidents and validate exploit paths against live state. |
| [Tenderly](https://tenderly.co/) | Use in real audits | Transaction simulation, forks, trace debugging, and alerting. |
| [Etherscan](https://etherscan.io/) | Use in real audits | Contract, tx, event, proxy, and verification inspection. |
| [Dune](https://dune.com/) | Situational / advanced | On-chain data analysis, incident queries, and dashboards. |
| [DeFiHackLabs](https://github.com/SunWeb3Sec/DeFiHackLabs) | Must learn | Historical exploit reproduction with runnable tests. |

## Fuzzing and Invariants

Fuzzing is strongest when the team can state what must always be true: conserved
assets, bounded debt, correct accounting, role restrictions, and safe state
transitions.

| Resource | Tier | Best use |
| --- | --- | --- |
| [Foundry Invariant Testing](https://book.getfoundry.sh/forge/invariant-testing) | Must learn | Fast invariant tests inside the normal EVM workflow. |
| [Echidna](https://github.com/crytic/echidna) | Use in real audits | Property-based Solidity fuzzing. |
| [Medusa](https://github.com/crytic/medusa) | Use in real audits | High-performance stateful EVM fuzzing. |
| [ItyFuzz](https://github.com/fuzzland/ityfuzz) | Situational / advanced | Snapshot-based smart contract fuzzing and exploit generation research. |
| [Wake](https://github.com/Ackee-Blockchain/wake) | Watchlist | Python-driven tests, fuzzing, and Solidity analysis. |

## Symbolic Execution and Formal Verification

Use symbolic and formal methods when assets are high value, invariants are
precise, and implementation risk justifies the extra modeling effort.

| Resource | Tier | Best use |
| --- | --- | --- |
| [Halmos](https://github.com/a16z/halmos) | Use in real audits | Symbolic execution over Foundry tests. |
| [hevm](https://github.com/ethereum/hevm) | Situational / advanced | EVM symbolic execution and low-level debugging. |
| [Certora Prover](https://www.certora.com/prover) | Paid / certification | Specification-driven verification for critical protocols. |
| [Kontrol](https://kontrol.runtimeverification.com/) | Situational / advanced | Foundry-integrated formal verification using K semantics. |
| [K Framework](https://kframework.org/) | Situational / advanced | Semantics framework used for rigorous execution models. |
| [Move Prover](https://aptos.dev/en/build/smart-contracts/prover) | Situational / advanced | Specification and verification for Move modules. |

## AI-Assisted Analysis

AI can speed up code reading, invariant discovery, test scaffolding, and report
drafting. It must not be trusted as the source of truth. Always verify with code,
tests, traces, and manual reasoning.

| Resource | Tier | Best use |
| --- | --- | --- |
| [Pashov AI Web3 Security](https://github.com/pashov/ai-web3-security) | Must learn | Curated list of AI Web3 security tools and skills. |
| [Pashov Skills](https://github.com/pashov/skills) | Use in real audits | Solidity auditor and x-ray skills for AI-assisted review. |
| [Octane Security](https://www.octane.security/) | Paid / certification | Commercial AI-assisted review tool to evaluate carefully. |
| [Nethermind AuditAgent](https://auditagent.nethermind.io/) | Watchlist | Nethermind-backed AI audit agent; verify outputs manually. |
| [TestMachine EVMbench](https://testmachine.ai/evmbench/) | Watchlist | Benchmark context for AI EVM security performance. |
| [Paradigm EVMbench](https://www.paradigm.xyz/2026/02/evmbench) | Watchlist | Research framing for EVM exploit-generation benchmarks. |
| [OpenAI EVMbench](https://openai.com/index/introducing-evmbench/) | Watchlist | Benchmark framing for evaluating EVM exploit reasoning. |
| [Re-Evaluating EVMBench](https://arxiv.org/abs/2603.10795) | Watchlist | Cautionary paper for interpreting EVMbench-style results. |

## Pentesting and Offchain Review

Most production incidents are not purely contract bugs. Dapps also have auth,
APIs, admin panels, DNS, CI/CD, secrets, support tooling, and wallet UX.

| Resource | Tier | Best use |
| --- | --- | --- |
| [Burp Suite](https://portswigger.net/burp) | Must learn | Web/API testing, authz checks, and request tampering. |
| [OWASP ZAP](https://www.zaproxy.org/) | Use in real audits | Open-source web app scanning and proxy testing. |
| [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/) | Must learn | Structured web testing methodology. |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Must learn | Application security control baseline. |
| [Socket](https://socket.dev/) | Use in real audits | JavaScript package and install-time risk visibility. |
| [VANTAGE by DigiBastion](https://vantage.digibastion.com/) | Watchlist | External domain, DNS, frontend, phishing, and Web3 trust-risk monitoring. |
