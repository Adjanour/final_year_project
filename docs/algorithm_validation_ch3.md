# Chapter 3 Algorithm Validation (DCA‑Trie v1/v2)

This note validates the methodology claims in `Chapters/Chapter3.tex` against papers in `papers/`.

## Sources checked

- `papers/luo2025-graph-constrained-reasoning.pdf` (GCR)
- `papers/li2024-decoding-on-graphs.pdf` (DoG)
- `papers/willard2023-efficient-guided-generation-llms.pdf` (efficient guided/constrained decoding)
- `papers/beurer-kellner2024-guiding-llms-the-right-way.pdf` (DOMINO, constrained decoding masking)
- `papers/hokamp2017-grid-beam-search.pdf` (constrained beam search foundation)

> Note: `papers/luo2024gcr.pdf` appears empty/corrupted in local storage (`pdftotext` returns “Document stream is empty”). Validation therefore uses `luo2025-graph-constrained-reasoning.pdf`, which contains the same GCR core mechanism.

## Validation by claim

### 1) Static graph-constrained baseline (GCR-style oracle)

**Claim in Chapter 3:** Baseline constrains decoding with a prebuilt KG-trie from graph structure and question entities.

**Status:** ✅ Supported.

**Evidence:** GCR describes a trie-based KG index (KG-Trie / prefix-tree style) that constrains decoding and grounds reasoning paths in KG structure.

---

### 2) Dynamic step-wise expansion (DoG-style traversal)

**Claim in Chapter 3:** A dynamic constrained oracle can expand the local graph scope during decoding based on intermediate reasoning state.

**Status:** ✅ Supported.

**Evidence:** DoG explicitly states that graph-aware constrained decoding uses a local query-centric subgraph that “progressively expands” as reasoning proceeds, while restricting valid token scope.

---

### 3) Mask-based constrained decoding mechanism

**Claim in Chapter 3:** At each step, valid-token masking enforces hard constraints in beam decoding.

**Status:** ✅ Supported.

**Evidence:** DOMINO/general constrained-decoding formulations describe update-constraint → compute mask → allow only valid next tokens; constrained beam-search literature also supports this paradigm.

---

### 4) Structural faithfulness guarantee

**Claim in Chapter 3:** Faithfulness is preserved if admitted tokens are restricted to valid graph transitions.

**Status:** ✅ Conceptually supported, with implementation caveat.

**Evidence:** GCR/DoG framing supports faithful KG-grounded generation under hard graph constraints.

**Caveat:** Guarantee depends on exact token-level implementation (mask correctness and tokenizer alignment). DOMINO-style work highlights that misaligned tokenization can weaken strict guarantees if not handled carefully.

---

### 5) Complexity statements in v1/v2 sections

**Claim in Chapter 3:**

- v1 decode-time lookup remains GCR-like (`O(d)` local branching lookup)
- v2 adds per-expansion semantic scoring overhead (`O(|N_e| * d_E)` style)

**Status:** 🟡 Plausible and methodologically consistent, but mostly project-derived rather than directly quoted from source papers.

**Interpretation:** These are acceptable if presented as analytical complexity of your implementation assumptions (data structures + encoder calls), not as direct claims from GCR/DoG text.

---

### 6) DCA-specific semantic gating (v1 static, v2 dynamic)

**Claim in Chapter 3:** Cosine-threshold semantic scoring is integrated into trie admission.

**Status:** 🟡 Novel contribution (not baseline paper claim).

**Interpretation:** This should be framed as your method extension over GCR/DoG, which is already how Chapter 3 presents it.

## Bibliography key sanity

Current keys in `references.bib` exist and are usable:

- `luo2024gcr` (arXiv-form misc entry)
- `li2024dog` (arXiv-form misc entry)
- Also available: `luo2025-graph-constrained-reasoning`, `li2024-decoding-on-graphs`

If you want camera-ready rigor, you can cite the final venue versions (`luo2025-graph-constrained-reasoning`, `li2024-decoding-on-graphs`) instead of the arXiv-style aliases.

## Recommended Chapter 3 wording tweaks (optional)

1. Where you state guarantees, add a one-line qualifier: guarantee holds under correct tokenization and mask construction.
2. Where you state complexity, tag it as “implementation-level analysis” of your DCA-trie design.
3. Keep DoG citation near dynamic expansion equations (already done) and GCR citation near static trie/oracle definitions (already done).
