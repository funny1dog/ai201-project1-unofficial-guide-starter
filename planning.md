# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

**The Unofficial Guide to Quantum Computing Careers and Learning.** 
While there are thousands of official textbooks and vendor docs (IBM, Google) explaining the physics of quantum mechanics, it is incredibly difficult to find honest, grounded information about the *reality* of working in the field. This domain captures the "unofficial" knowledge: salary bands, how much math you actually need for a SWE role, honest reviews of certifications, and the struggles of dealing with noisy quantum hardware vs. the startup hype. This is valuable for traditional computer scientists looking to pivot into the industry without getting a PhD.

---

## Documents

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | r/QuantumComputing | Thread on getting a QC job without a PhD | `reddit.com/r/QuantumComputing/` -> `documents/01_reddit_phd_job.md` |
| 2 | Hacker News | Thread about the realities of Quantum Startups | `news.ycombinator.com/` -> `documents/02_hn_startup_reality.md` |
| 3 | Personal Blog | Honest review of the IBM Qiskit Developer Cert | `medium.com/tag/qiskit` -> `documents/03_qiskit_cert_review.md` |
| 4 | r/learnmachinelearning | Discussion on the usefulness of QML | `reddit.com/r/learnmachinelearning/` -> `documents/04_qml_usefulness.md` |
| 5 | Physics StackExchange | Intuitive explanation of Shor's Algorithm for SWEs | `physics.stackexchange.com/` -> `documents/05_shors_algorithm_intuitive.md` |
| 6 | Awesome List Gist | Opinionated commentary on QC frameworks/books | `github.com/topics/quantum-computing` -> `documents/06_awesome_quantum_rants.md` |
| 7 | YouTube Transcript | A day in the life of a Quantum Software Engineer | `youtube.com/` -> `documents/07_day_in_life_qse.md` |
| 8 | r/OMSCS | Reviews on GT's CS 8803 (Intro to QC) course | `reddit.com/r/OMSCS/` -> `documents/08_omscs_quantum_course.md` |
| 9 | Blind (Teamblind) | Salary and interview culture at Rigetti/IonQ/IBM | `teamblind.com/company/Rigetti` -> `documents/09_teamblind_quantum_tc.md` |
| 10 | Discord Archive | Unofficial FAQ for a Quantum Hackathon | Local Discord Export -> `documents/10_hackathon_faq.md` |

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:**

**Overlap:**

**Reasoning:**

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:**

**Top-k:**

**Production tradeoff reflection:**

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1.

2.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**
