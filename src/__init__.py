"""
Universal SAT/CNF Optimization Framework Package
A general-purpose solver for combinatorial optimization problems using MaxSAT and CNF formulations.

While this package includes demonstrations for protein folding (HP model), 
the core architecture is completely general-purpose and applicable to:
- Scheduling and logistics
- Circuit verification
- Resource allocation
- Cryptanalysis
- Planning problems
- And many other constraint satisfaction problems
"""

__version__ = "1.0.0"
__author__ = "Universal SAT/CNF Framework Team"
__license__ = "Proprietary - All Rights Reserved"
__copyright__ = "Copyright (c) 2026 Universal SAT/CNF Framework Team"

from .optimizer import build_optimized_hp_wcnf_3d, run_simulation
from .visualization import visualize_structure, plot_energy_comparison
from .utils import validate_sequence, calculate_energy

__all__ = [
    'build_optimized_hp_wcnf_3d',
    'run_simulation',
    'visualize_structure',
    'plot_energy_comparison',
    'validate_sequence',
    'calculate_energy'
]

# LICENSE WARNING
# This software is proprietary and confidential.
# Commercial use is strictly prohibited without a written license agreement.
# Contact the copyright holder for licensing inquiries.
# Unauthorized use will result in legal action.
