# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

**The Unofficial Guide to Quantum Computing Careers and Learning.** 
While there are thousands of official textbooks and vendor docs (IBM, Google) explaining the physics of quantum mechanics, it is incredibly difficult to find honest, grounded information about the *reality* of working in the field. This domain captures the "unofficial" knowledge: salary bands, how much math you actually need for a SWE role, honest reviews of certifications, and the struggles of dealing with noisy quantum hardware vs. the startup hype. This is valuable for traditional computer scientists looking to pivot into the industry without getting a PhD.

---

## Document Sources

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | Reddit | Forum Thread | `documents/01_reddit_phd_job.md` |
| 2 | Hacker News | Forum Thread | `documents/02_hn_startup_reality.md` |
| 3 | Personal Blog | Blog Post | `documents/03_qiskit_cert_review.md` |
| 4 | Reddit | Forum Thread | `documents/04_qml_usefulness.md` |
| 5 | StackExchange | Q&A | `documents/05_shors_algorithm_intuitive.md` |
| 6 | GitHub | Curated List | `documents/06_awesome_quantum_rants.md` |
| 7 | YouTube | Video Transcript | `documents/07_day_in_life_qse.md` |
| 8 | Reddit | Forum Thread | `documents/08_omscs_quantum_course.md` |
| 9 | Blind | Forum Thread | `documents/09_teamblind_quantum_tc.md` |
| 10 | Discord | FAQ / Chat Archive | `documents/10_hackathon_faq.md` |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:** 512 characters

**Overlap:** 64 characters

**Why these choices fit your documents:** The source documents are mostly short, conversational forum posts and lists. A fixed-size character chunking strategy is a robust starting point. 512 characters is large enough to contain a complete thought (like a single Reddit comment or a list item) but small enough that the semantic meaning isn't diluted. The 64-character overlap helps preserve context for ideas that might be split across a chunk boundary. We skipped complex HTML cleaning because our ingestion pipeline uses clean markdown files without HTML boilerplate.

**Final chunk count:** 47 (Note: This is slightly under the 50-chunk heuristic because our source documents are highly concentrated, pre-cleaned markdown files consisting of short forum comments, rather than bloated web pages. The resulting chunks perfectly encapsulate individual thoughts.)

---

## Sample Chunks

**Chunk 1** (Source: `09_teamblind_quantum_tc.md` | Length: 371 chars)
> **Comment: ionq_insider**
> At IonQ, the culture is highly driven by the hardware team. Software engineers are sometimes treated as second-class citizens compared to the trapped-ion physicists. But if you want to work on a system that is actually scaling up right now, it's a great place to be. TC is competitive for startups, but again, liquid cash is lower than big tech.

**Chunk 2** (Source: `03_qiskit_cert_review.md` | Length: 307 chars)
> **Is it worth it?**
> If you have zero professional experience in quantum computing and want to get your resume noticed by recruiters, yes. It proves you understand the basics of quantum circuits and can write code using IBM's framework. However, it will *not* get you a job on its own. It's a stepping stone.

**Chunk 3** (Source: `09_teamblind_quantum_tc.md` | Length: 415 chars)
> **Comment: verified_ibm_q**
> I'm at IBM Quantum. The TC here is standard IBM bands, meaning it's lower than Google/Meta. Expect around $160k-$180k base for a mid-level SWE, plus a 10% bonus. The culture is very corporate, slow-moving, and academic. You will be working on a very small piece of a massive system. The interview was standard Leetcode Mediums plus system design. No quantum physics questions were asked.

**Chunk 4** (Source: `09_teamblind_quantum_tc.md` | Length: 263 chars)
> # Blind: Salary and Interview Culture at Quantum Companies (Rigetti, IonQ, IBM)
> 
> **Post by: SWE_looking_to_pivot**
> I have offers from Rigetti Computing and IBM Quantum. What is the culture and Total Compensation (TC) like? I'm coming from a standard web dev role.

**Chunk 5** (Source: `02_hn_startup_reality.md` | Length: 384 chars)
> **Comment: hardware_hacker**
> I worked at one of the big superconducting qubit companies. The real bottleneck right now isn't even the quantum chips, it's the classical control hardware. We literally ran out of physical space in the dilution refrigerator for the coaxial cables needed to control 100+ qubits. Until we solve the wiring problem, scaling to 10,000 qubits is a pipe dream.

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:** `all-MiniLM-L6-v2` via `sentence-transformers`

**Production tradeoff reflection:** For a real production system where cost is not a constraint, I would evaluate a larger, more powerful API-based model like OpenAI's `text-embedding-3-large`. The key tradeoffs would be accuracy vs. latency and cost. The larger model would likely provide more nuanced and accurate embeddings for domain-specific jargon, leading to better retrieval. However, this comes at the cost of higher per-query pricing, dependence on an external service, and increased network latency compared to the fast, free, and local `all-MiniLM-L6-v2` model.

---

## Retrieval Test Results

**Query 1:** "According to Blind reviews, what is the expected base salary range for a mid-level SWE at IBM Quantum?"
* **Top relevant chunk retrieved:** "I'm at IBM Quantum. The TC here is standard IBM bands, meaning it's lower than Google/Meta. Expect around $160k-$180k base for a mid-level SWE, plus a 10% bonus..."
* **Why it is relevant:** The user specifically asked for the base salary range for a mid-level SWE at IBM Quantum, and this chunk provides the exact salary band ($160k-$180k) from a verified IBM Quantum employee.

**Query 2:** "What version of Qiskit should I study for the IBM Qiskit Developer Certification?"
* **Top relevant chunk retrieved:** "A huge gotcha: IBM frequently updates Qiskit. Make sure you are studying the version of Qiskit that the exam is currently testing! When I took it, the exam was testing Qiskit 0.28..."
* **Why it is relevant:** The query asks which version of Qiskit to study, and the chunk directly addresses this by warning the reader that IBM updates Qiskit frequently and they must check the syllabus for the specific version being tested.

**Query 3:** "If I don't have a PhD, what specific roles should I target at a quantum company according to QubitWrangler?"
* **Top relevant chunk retrieved:** "**Comment: QubitWrangler** Not impossible at all, but you have to target the right roles... Look for 'Quantum Software Engineer' or 'Control Systems Engineer' roles, not 'Quantum Research Scientist'."

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:** "You are a helpful assistant for the 'Unofficial Guide to Quantum Computing Careers'. Your job is to answer user questions using ONLY the provided context. If the context does not contain enough information to answer the question, you must explicitly state: 'I don't have enough information on that.' Do not use your general knowledge to answer."

**How source attribution is surfaced in the response:** Sources are programmatically collected during the retrieval stage from the metadata of each chunk. Once the LLM generates the answer, the Gradio interface formats these extracted source document names into a bulleted list and displays them in a dedicated "Retrieved from" output text box, ensuring attribution is deterministic.

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

**One way your implementation diverged from the spec, and why:**

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*
