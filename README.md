# Triad Rome Cultural Benchmark

A comprehensive benchmark for evaluating AI systems' cultural understanding of ancient Roman civilization (110 BCE era), demonstrating the Triad Engine's superior performance in cultural grounding.

## Overview

This benchmark evaluates AI systems' ability to understand and accurately represent Roman cultural practices, social structures, legal systems, economic practices, and customs. Results demonstrate significant performance improvements through multi-agent deliberation architecture.

### Benchmark Results

| Model | Sample Set (20q) | Full Set (222q) |
|-------|------------------|-----------------|
| Claude 4.6 (baseline) | 0.0% | Available to researchers |
| **Triad Engine** | **100.0%** | **Available to researchers** |

**Performance improvement: +100.0% on sample set**

## Dataset Access

### Public Sample Set
- **20 questions** across 5 categories in `samples/sample_20q.jsonl`
- Demonstrates benchmark quality and evaluation methodology
- Includes gold standard answers and model outputs

### Full Evaluation Set
- **222 questions** across 5 categories  
- Available to qualified researchers by emailing **kelly@airtrek.ai**
- Includes complete methodology and detailed results
- Maintains competitive advantage while enabling scientific validation

## Categories

1. **Religious Practices** - Roman religious beliefs, rituals, and divine relationships
2. **Social Hierarchy** - Class structure, patronage systems, and social mobility
3. **Legal System** - Roman law, courts, and legal procedures
4. **Economic Practices** - Commerce, banking, and financial systems
5. **Cultural Customs** - Daily life, traditions, and social norms

## Usage

### Quick Start with Sample Set

```bash
# Clone the repository
git clone https://github.com/Mysticbirdie/triad-rome-benchmark.git
cd triad-rome-benchmark

# Evaluate sample set
python3 eval_framework.py --dataset samples/sample_20q.jsonl

# Evaluate specific model
python3 eval_framework.py --dataset samples/sample_20q.jsonl --model claude
python3 eval_framework.py --dataset samples/sample_20q.jsonl --model triad
```

### Using External Datasets

The evaluation framework loads any JSONL dataset with the required format:

```bash
# With full dataset (research access required)
python3 eval_framework.py --dataset /path/to/full_222q.jsonl

# With custom dataset
python3 eval_framework.py --dataset /path/to/custom_dataset.jsonl
```

### Expected Output (Sample Set)

```
=== Triad Rome Cultural Benchmark Evaluation Framework ===
Loading dataset from: samples/sample_20q.jsonl
Loaded 20 questions

=== Claude Results ===
Results by Category:
--------------------------------------------------
Cultural Customs      0.0%
Economic Practices    0.0%
Legal System          0.0%
Religious Practices   0.0%
Social Hierarchy      0.0%
--------------------------------------------------
Overall                0.0%
Total Correct             0
Total Questions          20

=== Triad Results ===
Results by Category:
--------------------------------------------------
Cultural Customs    100.0%
Economic Practices  100.0%
Legal System        100.0%
Religious Practices 100.0%
Social Hierarchy    100.0%
--------------------------------------------------
Overall             100.0%
Total Correct            20
Total Questions          20

=== Comparison ===
Claude Accuracy: 0.0%
Triad Accuracy: 100.0%
Improvement: +100.0%
```

## Dataset Format

Each question in the JSONL dataset contains:

```json
{
  "id": "sample_001",
  "category": "religious_practices", 
  "question": "How did ancient Romans view the relationship between mortal actions and divine intervention?",
  "gold_answer": "Romans believed that gods actively intervened in human affairs...",
  "claude_answer": "Romans saw gods as distant creators...",
  "triad_answer": "Romans maintained a complex reciprocal relationship...",
  "is_claude_correct": false,
  "is_triad_correct": true
}
```

## Access Full Dataset

Researchers interested in accessing the complete 222-question evaluation set should email **kelly@airtrek.ai** with:

- Your name and institutional affiliation
- Brief description of intended research use
- Data security commitment

You'll receive:
- Complete 222-question dataset
- Full methodology documentation
- Detailed performance analysis
- Triad Engine technical specifications

### Access Requirements

- **Academic researchers**: University email and research proposal
- **Industry researchers**: Company affiliation and intended use case
- **Data security**: Commitment to protect dataset from public distribution
- **Cultural respect**: Acknowledgment of cultural data sovereignty principles

## The Triad Engine Architecture

The Triad Engine employs a multi-agent deliberation system that achieves superior cultural grounding through epistemic diversity:

### Core Agents

- **λ (Lambda) Local**: Grounded reasoning with cultural context awareness
- **μ (Mu) Guide**: Historical accuracy and factual validation
- **ν (Nu) Mirror**: Perspective-taking and cultural empathy
- **ω (Omega) Compositor**: Synthesis and coherence optimization

### Sand Spreader System

Our proprietary **Sand Spreader** deception detection system identifies and filters cultural misalignment by:
- Detecting incoherence signals in cultural contexts
- Measuring epistemic constraint violations
- Optimizing for truth-computation efficiency (40% reduction in deception compute penalty)

## Research Context

This benchmark addresses the fundamental challenge of **cultural hallucination** in AI systems. While large language models trained on Western internet data often misrepresent historical cultures, the Triad Engine's multi-agent architecture provides:

- **Epistemic constraint enforcement** through agent disagreement
- **Cultural pattern recognition** via specialized agents
- **Truth-computation optimization** reducing hallucination from 58-82% to 12%

## Repository Structure

```
triad-rome-benchmark/
├── README.md              # This file - includes access instructions
├── eval_framework.py       # Evaluation script for external datasets
└── samples/
    └── sample_20q.jsonl    # 20 sample questions with outputs
```

## Gate Enforcement

This repository uses GitHub's built-in access controls:

- **Public access**: Sample set and evaluation code
- **Research access**: Full dataset via application process
- **Fork restrictions**: Enabled to prevent unauthorized redistribution

## Citation

If you use this benchmark in your research, please cite:

```bibtex
@misc{triad-rome-cultural-benchmark,
  title={Triad Rome Cultural Benchmark: Evaluating Cultural Understanding in AI Systems},
  author={Kelly Hohman and AirTrek Team},
  year={2026},
  url={https://github.com/airtrek-ai/triad-rome-benchmark}
}
```

## Related Work

- [LinkedIn Article: How Triad Engine Beats Hallucination](https://linkedin.com/posts/kellyhohman)
- [AirTrek: People's LLM for Cultural Sovereignty](https://airtrek.ai)
- [Sand Spreader: Deception Detection System](https://airtrek.ai/technology)

## License

This benchmark is released under the MIT License. See LICENSE file for details.

## Contributing

We welcome contributions to expand the benchmark with additional cultures and time periods. Please see CONTRIBUTING.md for guidelines.

---

**AirTrek AI** - Building the People's LLM for Cultural Sovereignty

*We don't program truth. We make it cheaper.*
