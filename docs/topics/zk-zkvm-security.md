---
title: ZK and zkVM Security
description: Review proof statements, guest code, public inputs, verifier contracts, witness handling, recursion, prover operations, and zkVM upgrades.
---

# ZK and zkVM Security

A valid proof only supports a defined statement under specific implementation
and verifier assumptions. Review the statement, guest code, public inputs,
verifier, prover operations, and upgrade model together.

## Review questions

- What exactly is proven, and what remains trusted input or off-chain assumption?
- Can the verifier accept proofs for the wrong program, image, chain, or public input?
- How are guest code, dependencies, prover infrastructure, and upgrades controlled?

## Review workflow

1. Separate proof statement, witness, public inputs, verifier, and application logic.
2. Review image IDs, versioning, verifier keys, recursion, and upgrade paths.
3. Test malformed, stale, cross-context, and replayed proof submissions.
4. Monitor prover availability, cost, queues, and fallback behavior.

## Common risks

| Risk | What to verify |
| --- | --- |
| Wrong statement proven | Specification, public inputs, and application-side interpretation. |
| Verifier mismatch | Image ID, verifying key, chain binding, and upgrade authorization. |
| Witness leakage | Logs, proving service, debugging artifacts, and retention. |
| Prover centralization | Queue, outage, cost, censorship, and fallback path. |

## Linked checklists

- [Pre-audit readiness](../checklists/pre-audit.md)
- [Supply chain security](../checklists/supply-chain.md)
- [Security program maturity](security-program-maturity.md)

## FAQ

**Does a valid proof mean the protocol is secure?**
No. The proof only supports one statement under the assumptions encoded in the
guest, verifier, and application logic.

**What is the common review mistake?**
Reviewers inspect verifier contracts without validating the statement, guest
code, public inputs, and operational upgrade model.

## Starting resources

- [RISC Zero docs](https://dev.risczero.com/)
- [RISC Zero security overview](https://github.com/risc0/risc0/security)
- [SP1 repository](https://github.com/succinctlabs/sp1)
