# Contributing to Triad Rome Benchmark

Thank you for your interest in contributing to the cultural grounding benchmark for LLMs!

## How to Contribute

### Adding New Questions
- Questions must be historically accurate for Ancient Rome, 110 CE
- Focus on anachronism detection, character consistency, cultural values
- Provide clear ground truth answers
- Include category classification

### Evaluation Framework
- Follow the existing evaluation framework in `eval_framework.py`
- Ensure proper handling of edge cases
- Document any new metrics

### Data Quality
- All historical claims must be sourced
- Cultural references should be period-accurate
- Avoid modern concepts that didn't exist in 110 CE

## Development Setup

```bash
# Clone the repository
git clone https://github.com/Mysticbirdie/triad-rome-benchmark.git
cd triad-rome-benchmark

# Run evaluation
python eval_framework.py
```

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
