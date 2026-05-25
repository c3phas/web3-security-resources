---
social_image: assets/social/ai-era-smart-contract-auditor-og-v1.png
---

# AI-era Smart Contract Auditor

Audience: people asking whether it is still worth becoming a smart contract
auditor now that AI tools can read code, explain bugs, and scaffold tests.

## Short answer

Yes, but the job is changing. Do not train to be a slower version of an AI code
summarizer. Train to be the person who can turn code, protocol intent, attacker
incentives, tests, traces, and market context into verified security judgment.

AI will compress beginner tasks: summarizing files, listing common bug classes,
drafting tests, and explaining tool warnings. It will not remove the need for
auditors who can prove exploitability, reason about protocol economics, write
strong invariants, reject plausible but false findings, and communicate risk in a
way teams can act on.

## Staged path

| Stage | Build | Proof of work |
| --- | --- | --- |
| 1. Solidity and EVM base | Solidity semantics, storage, calls, events, proxies, ERC standards, Foundry basics | Explain and test five classic bugs without using AI as the answer key. |
| 2. Exploit reproduction | Fork tests, transaction tracing, public reports, DeFiHackLabs-style writeups | Reproduce ten real exploits and document root cause, preconditions, and fix. |
| 3. Invariant thinking | Stateful fuzzing, accounting rules, access-control properties, oracle assumptions | Write invariants that catch at least three known exploit classes. |
| 4. Manual review depth | Protocol state machines, privileged roles, math, external calls, liquidations, governance | Produce two complete reports on public codebases or contests. |
| 5. AI-assisted workflow | Context packing, prompt discipline, tool triage, test scaffolding, adversarial verification | Show where AI helped, where it was wrong, and how you verified the final claim. |
| 6. Specialization | Lending, AMMs, bridges, restaking, perps, wallets, account abstraction, ZK, or Solana | Build a small public portfolio around one domain with repeatable review artifacts. |

Start with the [Solidity/EVM auditor roadmap](solidity-evm-auditor.md) if you
need the base. Use the [AI-assisted auditor workflow](ai-assisted-auditor.md)
once you can already validate the output.

## 90-day plan

| Time | Focus | Deliverable |
| --- | --- | --- |
| Days 1-15 | Solidity, EVM, Foundry, common bug classes | Five minimal vulnerable contracts with passing exploit tests. |
| Days 16-30 | Public exploit reproduction | Five fork-test reproductions with short notes and transaction links. |
| Days 31-45 | DeFi primitives and reports | Three protocol threat models covering assets, roles, invariants, and failure modes. |
| Days 46-60 | Fuzzing and invariants | One repo with stateful fuzz tests that catch an intentional bug. |
| Days 61-75 | Contest-style manual review | One full report on a public scope, including invalidated hypotheses. |
| Days 76-90 | AI workflow and portfolio polish | A public case study showing prompts, AI mistakes, verification steps, and final findings. |

The schedule is aggressive. If you have less time, keep the order and stretch
the timeline. Do not skip exploit reproduction or invariants.

## Portfolio proof

Hiring managers, contest judges, and protocol teams need evidence that you can
do real work. A useful portfolio includes:

- Exploit reproductions with runnable tests, not only blog summaries.
- Invariants with a clear explanation of the asset or accounting rule they
  protect.
- Short reports that include root cause, exploit path, preconditions, impact,
  severity reasoning, and fix guidance.
- Notes on false positives you rejected and why they were not exploitable.
- A repeatable review checklist for your chosen protocol type.
- Public writeups that make tradeoffs clear without leaking private code.

## AI workflow

Use AI as an assistant, not as an authority.

1. Ask it to summarize architecture, assets, trust boundaries, privileged roles,
   and state transitions.
2. Ask for bug hypotheses and invariants, then map each one back to concrete
   code paths.
3. Ask it to scaffold tests, but make the test realistic yourself.
4. Run static analysis, fuzzing, fork tests, and traces to validate or reject
   hypotheses.
5. Keep a log of AI mistakes: hallucinated APIs, impossible call paths, missing
   preconditions, wrong severity, or fake exploitability.
6. Report only findings that meet the normal evidence bar.

If a claim cannot survive code review, a runnable PoC, a trace, an invariant, or
a rigorous argument, it is not a finding.

## Durable moat

The durable moat is not memorizing bug lists. It is judgment under uncertainty.
Build skills that remain useful when models improve:

- Protocol and attacker mental models.
- Ability to read unfamiliar code quickly without losing state.
- Economic reasoning around liquidations, oracle manipulation, MEV, governance,
  incentives, and insolvency.
- Test design that encodes security properties, not only happy paths.
- Clear severity reasoning and remediation advice.
- Taste for evidence: knowing when a plausible issue is still unproven.
- Operational awareness across frontends, APIs, wallets, keys, monitoring, and
  incident response.

## What not to do

- Do not collect certificates instead of proving exploit reasoning.
- Do not paste private code into tools without understanding data handling.
- Do not report AI-generated claims without manual validation.
- Do not learn only named bug classes; most high-impact issues are protocol
  specific.
- Do not ignore offchain risk. DNS, frontends, wallets, APIs, bots, keys, and
  deployment pipelines can break the same users as a contract bug.
- Do not mistake benchmark scores for audit readiness.
- Do not chase every ecosystem at once. Pick one base, produce proof, then
  expand.
