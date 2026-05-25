---
title: Solana Testing and Audit Tooling
description: Review Solana account validation, PDA handling, CPI safety, Anchor constraints, Mollusk, LiteSVM, Surfpool, and CI testing.
---

# Solana Testing and Audit Tooling

Solana security depends heavily on explicit account validation, PDA derivation,
CPI behavior, and account lifecycle edge cases. Fast local tests help keep these
checks mandatory instead of optional.

## Review questions

- Can an attacker substitute a signer, owner, PDA, token account, or executable account?
- Do tests cover reinitialization, closing, duplicate mutable accounts, and CPI target validation?
- Can CI run security-critical cases quickly enough to stay required?

## Review workflow

1. Start with signer, owner, PDA, account type, executable, mutability, and token-account checks.
2. Add lifecycle tests for initialize, update, close, reopen, and duplicate accounts.
3. Use Mollusk or LiteSVM for fast instruction-level coverage.
4. Use Surfpool or validator-backed tests where realistic network behavior matters.

## Common risks

| Risk | What to verify |
| --- | --- |
| Missing signer checks | Required signers and delegated authorities. |
| Owner confusion | Account owner, token owner, mint, and program ownership. |
| PDA reuse | Canonical bump, seed domain separation, and lifecycle. |
| Unsafe CPI | Target program, signer seeds, account forwarding, return assumptions. |

## Linked checklists

- [Solana program readiness](../checklists/solana-program.md)
- [Pre-audit readiness](../checklists/pre-audit.md)
- [Incident war room](../checklists/incident-war-room.md)

## FAQ

**Which tool should a team start with?**
Use fast local tools for instruction-level checks, then add validator-like
workflows for integration behavior.

**What makes Solana audits different?**
The account model makes substitution, lifecycle, and CPI validation central to
the review.

## Starting resources

- [Solana Program Security course](https://solana.com/developers/courses/program-security)
- [Mollusk docs](https://solana.com/docs/programs/testing/mollusk)
- [Anchor LiteSVM docs](https://www.anchor-lang.com/docs/testing/litesvm)
- [Surfpool docs](https://docs.surfpool.run/)
