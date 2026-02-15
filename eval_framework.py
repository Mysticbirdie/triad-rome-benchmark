#!/usr/bin/env python3
"""
Triad Rome Cultural Benchmark Evaluation Framework

Loads external JSONL datasets and computes accuracy metrics for Claude and Triad Engine
across different categories and overall performance.

Usage:
    python eval_framework.py --dataset /path/to/dataset.jsonl
    python eval_framework.py --dataset samples/sample_20q.jsonl
"""

import json
import sys
import argparse
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple, Optional

def load_dataset(file_path: str) -> List[Dict]:
    """Load the JSONL dataset from external path."""
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    data.append(json.loads(line))
    except FileNotFoundError:
        print(f"Error: Dataset file not found: {file_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSONL: {e}")
        sys.exit(1)
    
    return data

def compute_metrics(data: List[Dict], model: str) -> Tuple[Dict[str, float], float, int, int]:
    """Compute accuracy metrics by category and overall for specified model."""
    category_stats = defaultdict(lambda: {'correct': 0, 'total': 0})
    total_correct = 0
    total_questions = 0
    
    correct_field = f'is_{model}_correct'
    
    for item in data:
        category = item['category']
        is_correct = item[correct_field]
        
        category_stats[category]['total'] += 1
        category_stats[category]['correct'] += 1 if is_correct else 0
        
        total_questions += 1
        total_correct += 1 if is_correct else 0
    
    # Convert to percentages
    category_accuracies = {}
    for category, stats in category_stats.items():
        accuracy = (stats['correct'] / stats['total']) * 100
        category_accuracies[category] = accuracy
    
    overall_accuracy = (total_correct / total_questions) * 100 if total_questions > 0 else 0
    
    return category_accuracies, overall_accuracy, total_correct, total_questions

def format_category_name(category: str) -> str:
    """Format category names for display."""
    return category.replace('_', ' ').title()

def print_results(model: str, category_accuracies: Dict[str, float], overall_accuracy: float, 
                  total_correct: int, total_questions: int):
    """Print formatted results for a model."""
    print(f"\n=== {model.title()} Results ===")
    print("Results by Category:")
    print("-" * 50)
    for category in sorted(category_accuracies.keys()):
        accuracy = category_accuracies[category]
        formatted_category = format_category_name(category)
        print(f"{formatted_category:<20} {accuracy:>6.1f}%")
    
    print("-" * 50)
    print(f"{'Overall':<20} {overall_accuracy:>6.1f}%")
    print(f"{'Total Correct':<20} {total_correct:>6}")
    print(f"{'Total Questions':<20} {total_questions:>6}")

def main():
    """Main evaluation function."""
    parser = argparse.ArgumentParser(description='Triad Rome Cultural Benchmark Evaluation Framework')
    parser.add_argument('--dataset', type=str, required=True,
                       help='Path to external JSONL dataset file')
    parser.add_argument('--model', type=str, choices=['claude', 'triad', 'both'], 
                       default='both', help='Model to evaluate (default: both)')
    
    args = parser.parse_args()
    
    dataset_path = Path(args.dataset)
    if not dataset_path.exists():
        print(f"Error: Dataset file not found: {dataset_path}")
        print("Usage examples:")
        print("  python eval_framework.py --dataset samples/sample_20q.jsonl")
        print("  python eval_framework.py --dataset /path/to/full/dataset.jsonl")
        sys.exit(1)
    
    print("=== Triad Rome Cultural Benchmark Evaluation Framework ===")
    print(f"Loading dataset from: {dataset_path}")
    
    # Load dataset
    data = load_dataset(dataset_path)
    print(f"Loaded {len(data)} questions")
    
    models_to_eval = ['claude', 'triad'] if args.model == 'both' else [args.model]
    results = {}
    
    for model in models_to_eval:
        category_accuracies, overall_accuracy, total_correct, total_questions = compute_metrics(data, model)
        results[model] = {
            'category_accuracies': category_accuracies,
            'overall_accuracy': overall_accuracy,
            'total_correct': total_correct,
            'total_questions': total_questions
        }
        print_results(model, category_accuracies, overall_accuracy, total_correct, total_questions)
    
    # Comparison if both models evaluated
    if 'claude' in results and 'triad' in results:
        claude_acc = results['claude']['overall_accuracy']
        triad_acc = results['triad']['overall_accuracy']
        improvement = triad_acc - claude_acc
        
        print(f"\n=== Comparison ===")
        print(f"Claude Accuracy: {claude_acc:.1f}%")
        print(f"Triad Accuracy: {triad_acc:.1f}%")
        print(f"Improvement: +{improvement:.1f}%")

if __name__ == "__main__":
    main()
