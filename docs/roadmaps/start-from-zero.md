---
title: Start From Zero
description: Start From Zero page in the Web3 Security Resources 2026 hub.
---

# Start From Zero

Audience: beginners, Web2 engineers entering Web3, students, and security
engineers who need blockchain fundamentals before auditing.

## Outcomes

By the end of this track you should be able to:

- Explain transactions, blocks, wallets, private keys, gas, contracts, and finality.
- Read simple Solidity contracts and reason about storage, calls, and permissions.
- Use Foundry to compile, test, fuzz lightly, fork mainnet, and reproduce a bug.
- Read public audit reports and identify root cause, impact, and missing controls.

## Learning Sequence

| Phase | Focus | Deliverable |
| --- | --- | --- |
| 1 | Blockchain and cryptography basics | Explain a transaction lifecycle and key-management failure modes. |
| 2 | EVM and Solidity basics | Build and test an ERC-20, vault, and simple NFT. |
| 3 | Linux, Git, and developer workflow | Reproduce a public PoC locally with a clean README. |
| 4 | Testing and debugging | Write unit, fuzz, invariant, and fork tests for a small protocol. |
| 5 | Security mindset | Convert three historical incidents into prevention checklists. |

## Must Learn

| Resource | Why |
| --- | --- |
| [Mastering Ethereum](https://github.com/ethereumbook/ethereumbook) | Strong fundamentals for accounts, transactions, gas, and EVM concepts. |
| [Cyfrin Updraft](https://updraft.cyfrin.io/) | Beginner-friendly Solidity, Foundry, and audit training. |
| [Solidity Documentation](https://docs.soliditylang.org/) | Primary language reference; use it instead of outdated blog snippets. |
| [Foundry Book](https://book.getfoundry.sh/) | The baseline toolchain for modern EVM testing and audit reproduction. |
| [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/) | Battle-tested contract patterns and implementation references. |
| [Ethernaut](https://ethernaut.openzeppelin.com/) | Guided vulnerability practice for early Solidity learners. |

## Use in Practice

| Resource | Why |
| --- | --- |
| [Solodit](https://solodit.cyfrin.io/) | Search public findings by pattern and protocol type. |
| [DeFiHackLabs](https://github.com/SunWeb3Sec/DeFiHackLabs) | Reproduce historical exploits and understand transaction-level mechanics. |
| [Secureum Bootcamp](https://secureum.substack.com/) | Security concepts, quizzes, and foundational audit vocabulary. |
| [RareSkills Solidity Articles](https://www.rareskills.io/solidity) | Clear explanations of EVM, Solidity, math, and testing details. |

## Common Traps

- Skipping general software security and assuming every issue is Solidity-only.
- Learning tools before learning what a correct protocol state should be.
- Reading old Solidity material without checking compiler-version changes.
- Treating CTF solutions as audit methodology. They are practice, not a full review process.

## Graduation Project

Pick a small open-source protocol or training repo. Write a short threat model,
run tests and static analysis, add one invariant test, and produce a two-page
audit-style report with findings, non-findings, and assumptions.
