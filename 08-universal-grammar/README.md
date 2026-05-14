# Paper VIII: From G_2 to Universal Grammar

A math-first derivation of Natural Semantic Metalanguage (NSM)
via the Clifford algebra Cl(3,1), with the chain
G_2 -> Fano(2,2) -> Cl(3) -> (Cl(3,1), Cl(1,3), seam) -> witness
-> 21 blade primes -> 9 channel primes -> 11 operator primes
-> Universal Grammar theorem -> Combined Reading Lemma
-> Engine-UG-Witness Triad.

## Files

- `universal_grammar.tex` -- the paper source (LaTeX article).
- `universal_grammar.pdf` -- compiled paper (21 pages).
- `universal_grammar.md` -- a unified markdown version (for
  fast reading without LaTeX).
- `Makefile` -- build/clean targets.

## Building

```
make
```

This runs `pdflatex` three times (twice for cross-references, once
final). Output: `universal_grammar.pdf`.

To clean intermediate files:

```
make clean
```

## Companion code

All code referenced in the paper is in
`../../clifford_language/`. The per-layer derivation and
verification modules follow the naming convention
`derive_layerN_*.py` and `verify_layerN_*.py` for layers 0--7,
with cross-cutting work in `derive_cc1_prime_inventory.py`,
`derive_rho.py`, and `verify_cc3_greenberg.py`. The integration
probe is `verify_layer8_ug_theorem.py`.

The empirical Phase 1--4 probes are
`probe_multilingual_5family.py`,
`probe_voice_eversion.py`,
`probe_operator_compiler.py`, and
`probe_zeta_functional.py`.

## Status

Every probe referenced in the paper passes:

- Layer 0 (octonions / G_2): PASS
- Layer 1 (Fano lines = 7 NSM compositional identities): 7/7
- Layer 2 (Cl(3) spatial closure): 4/4
- Layer 3 (eversion law on 622 chains): 622/622
- Layer 4 (witness uniqueness): 6/6
- Layer 5 (21 forced blade primes, diameter-2 closure): 6/6
- Layer 6 (9 channel primes, 4 fundamental projectors): 6/6
- Layer 7 (11 operators, 189/189 closure tests): 7/7
- Layer 8 (Universal Grammar theorem integration): PASS

CC1: 29 compound primes derived.
CC2: rho_predicted = 10/21 = 0.4762, vs.
     rho_enwik9 = 0.473 (0.67% error).
CC3: 10 Greenberg word-order universals consistent with
     grade-ladder predictions.

## Section 12 capstone: the Combined Reading

Section 12 of the paper adds the Combined Reading Lemma
(Theorem 12.2) and the Engine-UG-Witness Triad (Theorem 12.3).
The capstone joins this paper's UG derivation to an independently
derived byte-stream engine -- the Acoustic Eversion Engine
(`forcing/acousticeversionLLM/`) -- and proves that the two
ontologies decompose every Cl(3,1) state into orthogonal
complement halves, mediated by the witness pair as the unique
lawful third.

Six probes verify five concrete capabilities on real language
(reuse-existing-only corpus: 50 active/passive English pairs,
20 PARALLEL_SENTENCES across 6 language families, 10,000 enwik9
windows, 150 algebraic chains):

| Capability | Probe | Pass |
| - | - | - |
| Voice swap (algebraic) | `probe_engine_voice_swap.py` | PASS |
| 8-channel semantic Fourier | `probe_engine_translation_invariance.py` | PASS |
| Witness Born rule (opt-in) | `probe_engine_witness_born_rule.py` | PASS |
| Byte+atom co-stream | `probe_engine_co_stream.py` | PASS |
| Chirality budget signature | `probe_chirality_budget.py` | PASS |
| Capstone (Combined Reading Lemma identities) | `probe_combined_reading.py` | 150/150 |

Empirical highlights:

- Engine is perspective-invariant on real English: median
  `cos(M_act, M_pas) = 1.0000` over 50 active/passive pairs.
- 8 semantic Fourier channels invariant within 0.005 across 6
  languages on 20 NSM-canonical sentences; W_witness Pearson
  +0.9016 (the most translation-stable channel).
- enwik9 epsilon-fraction = 0.4633 vs simple-NSM byte stream
  epsilon-fraction = 0.2222 -- non-overlapping 95% CIs, the
  first concrete genre signature the framework supports.
- Combined Reading Lemma identities pass exactly on 150/150
  chains (100 random + 50 real-language).

The probes reuse existing corpora only (PARALLEL_SENTENCES from
Phase 1, enwik9 from CC2, plus the hand-picked active/passive
pairs in `data_corpora.py`). All v2 invariants (V2-T-1..V2-T-33)
and the v2 hot path are preserved unchanged; the v3 amendments
are additive (see `forcing/acousticeversionLLM/spec.md` Section 14
and `spec-ug.md`).

For the full empirical results and proof outline of the Combined
Reading Lemma, see
[`docs/derivation/combined_reading.md`](../../docs/derivation/combined_reading.md).
