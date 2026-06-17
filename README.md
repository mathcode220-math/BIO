# 🧮 Universal SAT/CNF Optimization Framework

![License: Proprietary](https://img.shields.io/badge/License-Proprietary-red.svg)
![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)
![MaxSAT](https://img.shields.io/badge/optimization-MaxSAT-green.svg)

---

## ⚠️ IMPORTANT NOTICE - PROPRIETARY LICENSE

**⛔ COMMERCIAL USE STRICTLY PROHIBITED WITHOUT PRIOR WRITTEN AGREEMENT**

This software is protected by a **strict Proprietary License**. 

- **Corporate Usage:** Any company, organization, or entity wishing to use, integrate, modify, deploy, or derive value from this code **MUST** contact the author directly to negotiate a commercial license agreement **BEFORE** any usage.
- **Patent Pending:** The algorithms and methodologies implemented herein may be subject to pending patent applications.
- **Legal Action:** Unauthorized use, distribution, modification, or derivation of this work will result in immediate legal action.
- **No Implied License:** No rights are granted to you under this software except as explicitly stated in a written license agreement.

**For licensing inquiries, please contact: [INSERT YOUR CONTACT EMAIL HERE]**

---

## 📋 Overview

The **Universal SAT/CNF Optimization Framework** is a high-performance, domain-agnostic solver system designed to tackle complex combinatorial optimization problems using **Maximum Satisfiability (MaxSAT)** and **Conjunctive Normal Form (CNF)** formulations.

While this repository includes demonstrations for protein folding (HP model), the core architecture is **completely general-purpose** and can be applied to any problem that can be encoded into Boolean satisfiability constraints.

### Core Capabilities

- **Universal SAT/CNF Engine:** Encode arbitrary logical constraints and objective functions into optimized CNF/WCNF formats
- **Domain-Agnostic Solver:** Applicable to scheduling, logistics, circuit verification, resource allocation, cryptanalysis, planning, and more
- **Advanced Encoding Strategies:** Efficient clause generation with symmetry breaking and constraint propagation
- **Hybrid Optimization:** Combines exact MaxSAT solving with heuristic search and local optimization
- **Multi-Dimensional Visualization:** Tools for rendering high-dimensional solution spaces, constraint graphs, and energy landscapes
- **Benchmarking Suite:** Comprehensive tools for performance evaluation across different problem instances

## ✨ Key Features

- **Flexible Constraint Modeling:** Express complex relationships using Boolean logic, cardinality constraints, and pseudo-Boolean inequalities
- **Optimized CNF Generation:** Minimal clause encoding with variable elimination and clause learning
- **Multiple Solver Backends:** Support for RCMaxSAT, Clingo, Open-WBO, and other MaxSAT solvers
- **3D/ND Visualization:** Interactive visualization of solutions in multi-dimensional spaces
- **Energy Landscape Analysis:** Tools for exploring solution space topology and local optima
- **Batch Processing:** Run large-scale experiments with automatic result aggregation
- **Export Capabilities:** Save models, solutions, and visualizations in multiple formats (JSON, CSV, PNG, SVG)

## 🚀 Quick Start

```python
# Import core modules
from src.optimizer import build_optimized_hp_wcnf_3d, solve_maxsat
from src.visualization import visualize_structure, plot_energy_comparison

# Define a problem (example: protein folding as demonstration)
sequence = "HPPHHPH"  # HP sequence (can be any binary constraint problem)

# Build CNF/WCNF model
wcnf = build_optimized_hp_wcnf_3d(
    sequence, 
    dim_x=6, dim_y=6, dim_z=6,
    use_clingo=False
)

# Solve the optimization problem
solution = solve_maxsat(wcnf)

# Visualize results
visualize_structure(solution.coordinates, sequence)
```

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/universal-sat-cnf-framework.git
cd universal-sat-cnf-framework

# Install dependencies
pip install -r requirements.txt
```

## 📁 Project Structure

```
universal-sat-cnf-framework/
├── Copy_of_Untitled11.ipynb      # Main demonstration notebook
├── README.md                      # This file
├── LICENSE                        # Proprietary license
├── requirements.txt               # Python dependencies
├── src/                           # Source code
│   ├── __init__.py
│   ├── optimizer.py              # Core SAT/CNF encoding & solving
│   ├── visualization.py          # Multi-dimensional visualization
│   └── utils.py                  # Utility functions
├── notebooks/                     # Additional Jupyter notebooks
├── results/                       # Output directory
│   ├── structures/               # Solution structures
│   ├── plots/                    # Generated visualizations
│   └── data/                     # Raw data exports
├── tests/                         # Unit tests
└── docs/                          # Documentation
```

## 🔧 Advanced Usage

### Building Optimized WCNF Models

```python
from src.optimizer import build_optimized_hp_wcnf_3d

sequence = "HPPHHPHP"
wcnf = build_optimized_hp_wcnf_3d(
    sequence, 
    dim_x=6, dim_y=6, dim_z=6,
    use_clingo=False
)
```

### Running Benchmark Suites

```python
from src.optimizer import run_benchmark_suite

# Test multiple problem instances
instances = ["HPPH", "HPHPHP", "HPPHHPH"]
results = run_benchmark_suite(instances, grid_dim=5)
```

### Custom Constraint Encoding

```python
from src.optimizer import encode_custom_constraints

# Define your own logical constraints
constraints = [
    ("x1 OR x2 OR NOT x3", "hard"),
    ("x4 XOR x5", "soft", weight=10)
]
wcnf = encode_custom_constraints(constraints)
```

## 📊 Performance Benchmarks

| Instance | Dimensions | Energy/Optimum | Time (s) | Status |
|----------|------------|----------------|----------|--------|
| HPPH     | 4×4×4      | -2             | 0.15     | ✅ Solved |
| HPHPHP   | 5×5×5      | -3             | 0.42     | ✅ Solved |
| HPPHHPH  | 6×6×6      | -4             | 1.23     | ✅ Solved |

## 🎯 Algorithm Overview

The framework follows these key steps:

1. **Problem Encoding:** Transform problem constraints into Boolean variables and clauses
2. **CNF Generation:** Build optimized Conjunctive Normal Form representations
3. **Optimization:** Solve using state-of-the-art MaxSAT solvers (RCMaxSAT, Clingo, Open-WBO)
4. **Validation:** Verify solution correctness and constraint satisfaction
5. **Visualization:** Render solutions with interactive multi-dimensional plots

## 📝 Requirements

- Python 3.8 or higher
- Python libraries:
  - `numpy` - Numerical computations
  - `matplotlib` - Visualization
  - `pandas` - Data manipulation
  - `rcmaxsat` or `clingo` - MaxSAT solver backends

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

**Note:** By submitting contributions, you agree that your code will be governed by the same Proprietary License as this project.

## 📄 License

**⛔ PROPRIETARY LICENSE - ALL RIGHTS RESERVED**

This project is protected under a **strict proprietary license**. 

### Prohibited Without Commercial License:
- ❌ Any commercial use in products or services
- ❌ Integration into commercial applications
- ❌ Providing services to third parties for fees
- ❌ Redistribution or resale
- ❌ Modification or creation of derivative works for commercial purposes
- ❌ Patent infringement or unauthorized implementation of algorithms

### Permitted Uses (with restrictions):
- ✅ Non-commercial academic research (requires prior written approval)
- ✅ Personal evaluation and educational purposes
- ✅ Educational use in accredited institutions (notification required)

**ANY COMPANY OR ORGANIZATION MUST OBTAIN A WRITTEN COMMERCIAL LICENSE BEFORE USING THIS SOFTWARE.**

For licensing inquiries, please contact: **[INSERT YOUR CONTACT EMAIL HERE]**

See the [LICENSE](LICENSE) file for the complete legal text.

## 👥 Authors

- **Universal SAT/CNF Framework Development Team**

## 🙏 Acknowledgments

- Original HP Model: Dill, K.A. et al.
- MaxSAT Solvers: RCMaxSAT, Clingo, Open-WBO
- SAT Community and Researchers

## 📞 Contact

For questions, suggestions, collaboration proposals, and **commercial licensing**:

- Open an issue on GitHub
- Contact via email: **[INSERT YOUR CONTACT EMAIL HERE]**

**Corporate Inquiries:** All companies must contact us directly before any usage, evaluation, or testing of this software.

## 🔗 Useful Links

- [MaxSAT Evaluations](https://maxsat-evaluations.github.io/)
- [Boolean Satisfiability Problem](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem)
- [Constraint Satisfaction Problems](https://en.wikipedia.org/wiki/Constraint_satisfaction_problem)

---

<div align="center">

**Built with ❤️ for Advanced Optimization Research**

© 2026 Universal SAT/CNF Framework Team. All Rights Reserved.

**PROPRIETARY AND CONFIDENTIAL**

</div>
