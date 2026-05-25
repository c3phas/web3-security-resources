---
title: Solana Program Readiness Checklist
description: Evidence-based readiness gates for Solana account validation, PDAs, CPI safety, account lifecycle, Anchor constraints, and fast local tests.
---

# Solana Program Readiness

| Gate | Evidence | Owner | Pass condition | Common failure |
| --- | --- | --- | --- | --- |
| Accounts are validated | Signer, owner, PDA seed, bump, type, mutability, executable, and token-account checks. | Solana engineer | Every instruction rejects substituted or unauthorized accounts. | Anchor constraints cover common paths but custom account logic is under-tested. |
| PDA and CPI assumptions are tested | Canonical bump tests, signer seeds, CPI target validation, and cross-program failure cases. | Solana engineer | Program-derived authority cannot be reused or redirected unexpectedly. | Tests prove the expected PDA but not malicious alternatives. |
| State transitions resist reinitialization | Initialization, close, reopen, rent, zero-copy, and duplicate mutable account tests. | Solana engineer | Attackers cannot reset, alias, or close state into unsafe transitions. | Lifecycle tests stop after first successful initialization. |
| Fast local tests run in CI | Mollusk, LiteSVM, or validator-backed tests for security-critical instructions. | Engineering lead | Security tests run consistently before merge. | Local tests are too slow and become optional. |

## References

- [Solana Program Security course](https://solana.com/developers/courses/program-security)
- [Mollusk](https://solana.com/docs/programs/testing/mollusk)
- [Anchor LiteSVM](https://www.anchor-lang.com/docs/testing/litesvm)
- [Surfpool](https://docs.surfpool.run/)
