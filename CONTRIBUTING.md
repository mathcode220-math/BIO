# Contributing to Universal SAT/CNF Framework

## ⚠️ IMPORTANT LICENSING NOTICE

**Before contributing, please read this carefully:**

This project is protected by a **PROPRIETARY LICENSE**. By submitting contributions, you agree to the following terms:

1. **All contributions become the exclusive property** of the Universal SAT/CNF Framework Team.
2. **Contributors retain no rights** to use their contributions for commercial purposes.
3. **Companies and organizations** must obtain explicit written permission before contributing.
4. **Individual contributors** must confirm they are not bound by any conflicting agreements.

---

## How to Contribute

We welcome contributions from the research community! However, due to the proprietary nature of this project, all contributions must follow strict guidelines.

### Types of Contributions We Accept

- **Bug reports** (via GitHub Issues)
- **Bug fixes** (via Pull Requests)
- **Documentation improvements**
- **Test cases** for edge scenarios
- **Performance optimizations** (with benchmark evidence)
- **New constraint encodings** for novel problem domains

### Steps to Contribute

1. **Contact Us First**: Before starting any work, email us at `your-email@example.com` to discuss your proposed contribution.

2. **Sign Contributor Agreement**: All contributors must sign our Individual Contributor License Agreement (ICLA).

3. **Fork the Repository**: Create a personal fork for development.

4. **Create a Branch**: Use descriptive branch names (e.g., `fix/sat-encoding-bug`, `feature/new-constraint-type`).

5. **Make Your Changes**: Follow the coding standards below.

6. **Write Tests**: All new features must include comprehensive tests.

7. **Submit Pull Request**: Provide a detailed description of your changes.

8. **Code Review**: Maintainers will review your contribution.

---

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git

### Installation

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/universal-sat-cnf-framework.git
cd universal-sat-cnf-framework

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e ".[dev]"

# Copy configuration files
cp config.yaml config.local.yaml
cp .env.example .env
```

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test file
pytest tests/test_optimizer.py
```

---

## Coding Standards

### Code Style

- Follow **PEP 8** style guidelines
- Use **Black** for automatic formatting: `black src/ tests/`
- Maximum line length: **88 characters**
- Use **type hints** for all function signatures

### Documentation

- All public functions must have **docstrings**
- Use **Google-style** docstring format
- Include **examples** in docstrings when applicable
- Update **README.md** for user-facing changes

Example:
```python
def solve_maxsat(clauses: List[List[int]], weights: Optional[List[float]] = None) -> Solution:
    """
    Solve a MaxSAT problem using the RC2 algorithm.
    
    Args:
        clauses: List of CNF clauses, where each clause is a list of literals
        weights: Optional list of weights for each clause (default: all equal)
    
    Returns:
        Solution object containing the optimal assignment and cost
    
    Example:
        >>> clauses = [[1, 2], [-1, 3], [2, -3]]
        >>> solution = solve_maxsat(clauses)
        >>> print(solution.cost)
        0
    """
    pass
```

### Commit Messages

Follow the **Conventional Commits** specification:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring without behavior change
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

Example:
```
feat(optimizer): add hierarchical decomposition strategy

Implement a new hierarchical decomposition approach for large-scale
SAT problems. This strategy divides the problem into sub-problems
and solves them incrementally.

Closes #42
```

---

## Testing Requirements

### Test Coverage

- **Minimum 80% code coverage** for new features
- All critical paths must be tested
- Edge cases must be documented and tested

### Test Structure

```python
import pytest
from src.optimizer import solve_maxsat

class TestMaxSATSolver:
    """Test suite for MaxSAT solver functionality."""
    
    def test_simple_sat(self):
        """Test basic satisfiable formula."""
        clauses = [[1, 2], [-1, 3]]
        solution = solve_maxsat(clauses)
        assert solution.satisfiable
        assert solution.cost == 0
    
    def test_unsatisfiable(self):
        """Test unsatisfiable formula."""
        clauses = [[1], [-1]]
        solution = solve_maxsat(clauses)
        assert not solution.satisfiable
    
    @pytest.mark.parametrize("size", [10, 100, 1000])
    def test_performance(self, size):
        """Test performance with varying problem sizes."""
        clauses = generate_random_clauses(size)
        solution = solve_maxsat(clauses)
        assert solution.solve_time < 10.0  # seconds
```

---

## Pull Request Process

1. **Update Documentation**: Ensure README.md and inline docs reflect your changes.

2. **Add Changelog Entry**: Add an entry to `CHANGELOG.md` under the "Unreleased" section.

3. **Pass CI/CD**: All automated tests must pass before merging.

4. **Code Review**: At least one maintainer must approve your PR.

5. **Squash Commits**: Squash related commits before merging.

---

## Security Guidelines

- **Never commit sensitive information** (API keys, passwords, etc.)
- **Validate all inputs** to prevent injection attacks
- **Use secure random number generators** for cryptographic applications
- **Report security vulnerabilities** privately to `your-email@example.com`

---

## Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity, nationality, race, religion, or sexual orientation.

### Expected Behavior

- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insulting comments
- Publishing others' private information
- Other unethical or unprofessional conduct

---

## Legal Considerations

### Intellectual Property

- All contributions are subject to the project's **proprietary license**
- Contributors grant the project team **exclusive rights** to their contributions
- Contributors must ensure their work does not infringe on third-party rights

### Patent Rights

- Contributors grant the project team a **non-exclusive patent license** for any patents covering their contributions
- The project team reserves the right to file patents on contributed technologies

---

## Questions?

If you have any questions about contributing, please contact us at:

📧 **Email**: your-email@example.com

We look forward to your contributions!

---

**Last Updated**: June 2024  
**Version**: 1.0.0
