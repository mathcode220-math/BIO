# Universal SAT/CNF Framework - Documentation

## ⚠️ PROPRIETARY LICENSE NOTICE

**Copyright (c) 2026 Universal SAT/CNF Framework Team. All Rights Reserved.**

This software is proprietary and confidential. Commercial use is strictly prohibited without a written license agreement.

**For licensing inquiries, contact: [INSERT YOUR CONTACT EMAIL HERE]**

---

## 📚 Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Basic Usage](#basic-usage)
4. [Technical Documentation](#technical-documentation)
5. [Examples](#examples)
6. [FAQ](#faq)

---

## Overview

The **Universal SAT/CNF Framework** is a powerful, domain-agnostic optimization system using MaxSAT (Maximum Satisfiability) and CNF (Conjunctive Normal Form) formulations to solve complex constraint satisfaction problems.

While this documentation includes demonstrations for protein folding (HP model), the framework is **completely general-purpose** and applicable to:

- **Scheduling & Logistics**: Resource allocation, task scheduling, route optimization
- **Circuit Verification**: Hardware verification, logic circuit optimization
- **Cryptanalysis**: Boolean satisfiability in cryptographic analysis
- **Planning Problems**: AI planning, automated reasoning
- **Resource Allocation**: Optimal assignment problems
- **And More**: Any problem expressible as Boolean constraints

### What is the HP Model?

The HP (Hydrophobic-Polar) model is a simplified mathematical representation of proteins where:
- **H (Hydrophobic)**: Water-repelling amino acids - tend to cluster inside
- **P (Polar)**: Water-attracting amino acids - tend to stay on the surface

### How Does MaxSAT Work?

MaxSAT (Maximum Satisfiability) is a logical optimization problem:
1. Build **Hard Constraints** that must be satisfied
2. Build **Soft Constraints** we want to maximize
3. Use a MaxSAT solver to find the optimal solution

---

## التثبيت

### المتطلبات الأساسية

```bash
Python 3.8+
pip 21.0+
```

### تثبيت المكتبات

```bash
# تثبيت جميع المتطلبات
pip install -r requirements.txt

# أو تثبيت يدوي
pip install numpy matplotlib pandas seaborn pysat
```

### اختيار محرك MaxSAT

#### خيار 1: RCMaxSAT (موصى به)
```bash
pip install rcmaxsat
```

#### خيار 2: Clingo
```bash
pip install clingo
```

---

## الاستخدام الأساسي

### مثال بسيط

```python
from src.optimizer import run_simulation, build_optimized_hp_wcnf_3d
from src.visualization import visualize_structure
from src.utils import validate_sequence

# تسلسل بروتين بسيط
sequence = "HPPHHPH"

# التحقق من الصحة
if not validate_sequence(sequence):
    print("تسلسل غير صالح!")
else:
    # تشغيل المحاكاة
    result = run_simulation(sequence, grid_dim=5, is_3d=True)
    
    print(f"النتائج:")
    print(f"- الوقت: {result['total_time']:.2f} ثانية")
    print(f"- عدد المتغيرات: {result['n_variables']}")
    print(f"- عدد القيود: {result['n_clauses']}")
```

### تصور الهيكل

```python
# إحداثيات افتراضية للعرض
coordinates = [
    (0, 0, 0), (1, 0, 0), (1, 1, 0),
    (2, 1, 0), (2, 2, 0), (3, 2, 0), (3, 3, 0)
]

visualize_structure(coordinates, sequence, 
                   title="هيكل البروتين",
                   save_path="results/structures/protein_structure.png")
```

---

## الوثائق التقنية

### دوال التحسين (optimizer.py)

#### `build_optimized_hp_wcnf_3d(sequence, dim_x, dim_y, dim_z)`

تبني نموذج WCNF لطي البروتين ثلاثي الأبعاد.

**المعاملات:**
- `sequence`: تسلسل البروتين (أحرف H و P)
- `dim_x, dim_y, dim_z`: أبعاد الشبكة
- `use_clingo`: استخدام Clingo بدلاً من RCMaxSAT

**الإرجاع:**
- `wcnf`: نموذج WCNF
- `n_aa`: عدد الأحماض الأمينية
- `n_cells`: عدد الخلايا

#### `run_simulation(seq, grid_dim=5, is_3d=True, timeout=60)`

تشغيل محاكاة كاملة.

**المعاملات:**
- `seq`: تسلسل البروتين
- `grid_dim`: بعد الشبكة (مكعب)
- `is_3d`: هل المحاكاة ثلاثية الأبعاد
- `timeout`: مهلة الوقت بالثواني

**الإرجاع:**
- قاموس يحتوي على نتائج المحاكاة

### دوال التصور (visualization.py)

#### `visualize_structure(coordinates, sequence, title, save_path)`

رسم الهيكل ثلاثي الأبعاد.

#### `plot_energy_comparison(results_list, save_path)`

مقارنة الطاقة بين تسلسلات متعددة.

#### `create_contact_map(coordinates, sequence, save_path)`

إنشاء خريطة التلامس.

### الدوال المساعدة (utils.py)

#### `validate_sequence(sequence)`

التحقق من صحة التسلسل.

#### `calculate_energy(coordinates, sequence)`

حساب طاقة التكوين.

#### `save_results_to_json(results, filename)`

حفظ النتائج إلى JSON.

---

## الأمثلة

### مثال 1: تسلسلات قصيرة

```python
sequences = ["HPPH", "HPHPHP", "HPPHHPH"]

for seq in sequences:
    result = run_simulation(seq, grid_dim=4)
    print(f"{seq}: Energy = {result.get('energy', 'N/A')}")
```

### مثال 2: تحليل متقدم

```python
from src.utils import generate_sequence_report, count_amino_acids

sequence = "HPPHHPHPHPPH"

# تقرير مفصل
report = generate_sequence_report(sequence)
print(report)

# إحصائيات
counts = count_amino_acids(sequence)
print(f"\nنسبة H: {counts['h_percentage']:.1f}%")
```

### مثال 3: حفظ النتائج

```python
from src.utils import save_results_to_json, save_results_to_csv

results = []
for seq in ["HPPH", "HPHPHP", "HPPHHPH"]:
    result = run_simulation(seq, grid_dim=5)
    results.append(result)

# حفظ JSON
save_results_to_json({'experiments': results}, 'results/all_results.json')

# حفظ CSV
save_results_to_csv(results, 'results/summary.csv')
```

---

## الأسئلة الشائعة

### س: ما هو الحد الأقصى لطول التسلسل؟

ج: يعتمد على موارد النظام. عملياً:
- حتى 10 أحماض: سريع جداً (< 1 ثانية)
- 10-20 حمض: معقول (ثوانٍ إلى دقائق)
- 20+: قد يحتاج ساعات أو أيام

### س: لماذا أستخدم MaxSAT بدلاً من خوارزميات أخرى؟

ج: MaxSAT يضمن:
- إيجاد الحل الأمثل العالمي (ليس المحلي)
- معالجة دقيقة للقيود
- قابلية التوسع مع تحسينات الكود

### س: كيف يمكنني تحسين الأداء؟

ج: نصائح:
1. استخدم أبعاد شبكة مناسبة (ليست كبيرة جداً)
2. استخدم قيوداً إضافية لتقليل فضاء البحث
3. جرب محركات MaxSAT مختلفة
4. استخدم التوازي إذا أمكن

### س: هل يدعم ثنائي الأبعاد؟

ج: نعم، لكن التركيز الحالي على 3D. يمكن تطوير نسخة 2D بسهولة.

---

## المراجع

1. Dill, K.A. et al. "Principles of protein folding."
2. MaxSAT Evaluations: https://maxsat-evaluations.github.io/
3. PySAT: https://pysathq.github.io/

---

## المساهمة

نرحب بالمساهمات! يرجى قراءة دليل المساهمة في README.md.

## الترخيص

MIT License - انظر ملف LICENSE للتفاصيل.
