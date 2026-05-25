---
title: ZK Security
description: ZK Security page in the Web3 Security Resources 2026 hub.
---

# ZK Security

Audience: circuit engineers, auditors, protocol security engineers, and
researchers reviewing SNARK/STARK systems and verifier integrations.

## Outcomes

- Understand constraints, witnesses, public inputs, trusted setup, soundness, completeness, and zero knowledge.
- Review common circuit bugs: unconstrained signals, missing range checks, aliasing, field overflows, and incorrect public inputs.
- Assess verifier integration, proof lifecycle, key management, recursion, and upgrade risk.

## Roadmap

| Stage | Focus | Proof of work |
| --- | --- | --- |
| Foundations | Finite fields, commitments, constraints, arithmetization | Explain how a false witness can pass when constraints are missing. |
| Circuits | Circom, Noir, Halo2, R1CS/PLONKish models | Write and break a small circuit. |
| Verification | Verifier contracts, public inputs, proof keys | Review a verifier integration checklist. |
| Protocol integration | Bridges, rollups, identity, privacy, app-specific proofs | Threat model data availability and finality assumptions. |
| Advanced | Recursion, trusted setup, proving performance, side channels | Document assumptions that cannot be checked in code alone. |

## Must Learn

| Resource | Why |
| --- | --- |
| [0xPARC Learning Group](https://learn.0xparc.org/) | Strong ZK learning material and practice tracks. |
| [zkSecurity Blog](https://www.zksecurity.xyz/blog/) | Practical ZK vulnerability research and audit insights. |
| [RareSkills ZK Book](https://www.rareskills.io/zk-book) | Accessible introduction to zero-knowledge proof systems. |
| [Circom Docs](https://docs.circom.io/) | Primary reference for Circom circuit development. |
| [Noir Docs](https://noir-lang.org/docs) | Modern ZK DSL and tooling reference. |
| [Halo2 Book](https://zcash.github.io/halo2/) | Halo2 proof-system reference. |

## Use in Real Audits

- Check that every private witness value that matters is constrained.
- Confirm range checks for values that leave the field or map to application integers.
- Verify public inputs cannot be reordered, omitted, replayed, or mis-bound.
- Review trusted setup, proving key, verification key, and ceremony assumptions.
- Treat verifier contracts as normal smart contracts with access, upgrade, and integration risks.
