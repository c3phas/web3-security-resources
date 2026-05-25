# Tools

## EVM Development, Testing, and Debugging

| Tool | Tier | Use |
| --- | --- | --- |
| [Foundry](https://book.getfoundry.sh/) | Must learn | Compile, test, fuzz, fork, script, and debug EVM systems. |
| [Hardhat](https://hardhat.org/) | Use in real audits | Common project framework; many scopes still use it. |
| [Remix](https://remix.ethereum.org/) | Situational / advanced | Quick experiments and education. |
| [Tenderly](https://tenderly.co/) | Use in real audits | Transaction simulation and debugging. |
| [Sourcify](https://sourcify.dev/) | Use in real audits | Verified source metadata and contract lookup. |
| [Etherscan](https://etherscan.io/) | Use in real audits | Contract, transaction, and event inspection. |
| [Dune](https://dune.com/) | Situational / advanced | On-chain analytics and incident queries. |

## Static Analysis

| Tool | Tier | Use |
| --- | --- | --- |
| [Slither](https://github.com/crytic/slither) | Use in real audits | Static analysis, printers, inheritance, and call graph views. |
| [Aderyn](https://github.com/Cyfrin/aderyn) | Use in real audits | Solidity static analysis with report output. |
| [Mythril](https://github.com/ConsenSysDiligence/mythril) | Situational / advanced | Symbolic analysis for EVM bytecode. |
| [Manticore](https://github.com/trailofbits/manticore) | Situational / advanced | Symbolic execution platform. |
| [Semgrep](https://semgrep.dev/) | Use in real audits | Custom source-code rules for frontends, APIs, and Solidity patterns. |
| [Solhint](https://github.com/protofire/solhint) | Use in real audits | Solidity linting and style/security rules. |

## Fuzzing and Formal Methods

| Tool | Tier | Use |
| --- | --- | --- |
| [Echidna](https://github.com/crytic/echidna) | Use in real audits | Property-based fuzzing. |
| [Medusa](https://github.com/crytic/medusa) | Use in real audits | Stateful EVM fuzzing. |
| [Halmos](https://github.com/a16z/halmos) | Use in real audits | Symbolic testing from Foundry tests. |
| [hevm](https://github.com/ethereum/hevm) | Situational / advanced | EVM symbolic execution and testing. |
| [Certora Prover](https://www.certora.com/prover) | Paid / certification | Formal verification with executable specs. |
| [K Framework](https://kframework.org/) | Situational / advanced | Semantics framework behind several verification efforts. |

## Chain-Specific Tooling

| Tool | Tier | Use |
| --- | --- | --- |
| [Anchor](https://www.anchor-lang.com/docs) | Must learn | Solana framework and account constraints. |
| [Starknet Foundry](https://foundry-rs.github.io/starknet-foundry/) | Use in real audits | Cairo contract testing. |
| [Scarb](https://docs.swmansion.com/scarb/) | Use in real audits | Cairo package manager and build tool. |
| [Move Prover](https://aptos.dev/en/build/smart-contracts/prover) | Situational / advanced | Specification and verification for Move. |
| [Circom](https://docs.circom.io/) | Must learn | Circuit language for SNARK circuits. |
| [Noir](https://noir-lang.org/docs) | Watchlist | ZK DSL with improving developer experience. |

## Monitoring and User Protection

| Tool | Tier | Use |
| --- | --- | --- |
| [Forta](https://forta.org/) | Use in real audits | Detection bots and on-chain monitoring. |
| [OpenZeppelin Defender](https://www.openzeppelin.com/defender) | Use in real audits | Admin operations, monitoring, and automation. |
| [Hypernative](https://www.hypernative.io/) | Paid / certification | Real-time protocol monitoring and exploit detection. |
| [Blockaid](https://www.blockaid.io/) | Paid / certification | Wallet and dapp transaction protection. |
| [GoPlus](https://gopluslabs.io/) | Use in real audits | Token, address, and transaction risk APIs. |
| [Socket](https://socket.dev/) | Use in real audits | Supply-chain risk for JavaScript packages. |
| [OpenSSF Scorecard](https://github.com/ossf/scorecard) | Use in real audits | Open-source dependency health checks. |
