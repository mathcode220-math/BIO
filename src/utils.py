"""
Utility Functions for Universal SAT/CNF Framework
Contains helper functions for validation, data processing, and file I/O.

While this module includes demonstrations for protein folding (HP model),
the core architecture is completely general-purpose and applicable to:
- Scheduling and logistics
- Circuit verification
- Resource allocation
- Cryptanalysis
- Planning problems
- And many other constraint satisfaction problems

Copyright (c) 2026 Universal SAT/CNF Framework Team. All Rights Reserved.
This software is proprietary and confidential.
Commercial use is strictly prohibited without a written license agreement.
"""

import os
import json
import csv
from datetime import datetime


def validate_sequence(sequence):
    """
    التحقق من صحة تسلسل البروتين
    
    Args:
        sequence: تسلسل البروتين المدخل
    
    Returns:
        bool: True إذا كان التسلسل صالحاً
    """
    if not sequence:
        return False
    
    valid_chars = set('HP')
    return all(c.upper() in valid_chars for c in sequence)


def normalize_sequence(sequence):
    """
    توحيد صيغة التسلسل (أحرف كبيرة فقط)
    
    Args:
        sequence: تسلسل البروتين
    
    Returns:
        str: التسلسل الموحد
    """
    return sequence.upper().replace(' ', '').replace('-', '')


def calculate_energy(coordinates, sequence):
    """
    حساب طاقة التكوين بناءً على تلامسات H-H
    
    Args:
        coordinates: قائمة الإحداثيات [(x,y,z), ...]
        sequence: تسلسل البروتين
    
    Returns:
        int: قيمة الطاقة (سالبة = أكثر استقراراً)
    """
    if not coordinates or len(coordinates) != len(sequence):
        return 0
    
    h_indices = [i for i, aa in enumerate(sequence) if aa == 'H']
    contacts = 0
    
    for i_idx, i in enumerate(h_indices):
        for j in h_indices[i_idx + 1:]:
            if abs(i - j) > 1:  # غير متتاليين في السلسلة
                # حساب المسافة الإقليدية
                dist = sum(abs(coordinates[i][d] - coordinates[j][d]) 
                          for d in range(min(3, len(coordinates[i]))))
                if dist == 1:  # متجاوران مكانياً
                    contacts += 1
    
    return -contacts  # الطاقة السالبة تعني استقرار أكبر


def calculate_radius_of_gyration(coordinates):
    """
    حساب نصف قطر الدوران للبروتين
    
    Args:
        coordinates: قائمة الإحداثيات
    
    Returns:
        float: نصف قطر الدوران
    """
    import numpy as np
    
    if not coordinates:
        return 0.0
    
    coords = np.array(coordinates)
    center = np.mean(coords, axis=0)
    distances = np.sqrt(np.sum((coords - center) ** 2, axis=1))
    
    return np.mean(distances)


def save_results_to_json(results, filename=None):
    """
    حفظ نتائج المحاكاة إلى ملف JSON
    
    Args:
        results: قاموس النتائج
        filename: اسم الملف (اختياري)
    
    Returns:
        str: مسار الملف المحفوظ
    """
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"results_{timestamp}.json"
    
    # إضافة معلومات الوقت
    results['timestamp'] = datetime.now().isoformat()
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print(f"Results saved to {filename}")
    return filename


def save_results_to_csv(results_list, filename=None):
    """
    حفظ قائمة من النتائج إلى ملف CSV
    
    Args:
        results_list: قائمة من قواميس النتائج
        filename: اسم الملف (اختياري)
    
    Returns:
        str: مسار الملف المحفوظ
    """
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"results_{timestamp}.csv"
    
    if not results_list:
        return filename
    
    # تحديد المفاتيح المشتركة
    keys = set()
    for result in results_list:
        keys.update(result.keys())
    keys = sorted(list(keys))
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        
        for result in results_list:
            # تحويل القيم غير القابلة للكتابة
            row = {}
            for key in keys:
                value = result.get(key, '')
                if isinstance(value, (list, dict)):
                    value = str(value)
                row[key] = value
            writer.writerow(row)
    
    print(f"Results saved to {filename}")
    return filename


def load_results_from_json(filename):
    """
    تحميل نتائج من ملف JSON
    
    Args:
        filename: مسار الملف
    
    Returns:
        dict: النتائج المحملة
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


def create_output_directory(base_dir="results"):
    """
    إنشاء مجلدات الإخراج الضرورية
    
    Args:
        base_dir: المجلد الأساسي
    
    Returns:
        dict: مسارات المجلدات المنشأة
    """
    directories = {
        'structures': os.path.join(base_dir, 'structures'),
        'plots': os.path.join(base_dir, 'plots'),
        'data': os.path.join(base_dir, 'data'),
    }
    
    for name, path in directories.items():
        os.makedirs(path, exist_ok=True)
    
    return directories


def format_sequence_for_display(sequence, max_length=50):
    """
    تنسيق التسلسل للعرض
    
    Args:
        sequence: تسلسل البروتين
        max_length: الطول الأقصى للسطر الواحد
    
    Returns:
        str: التسلسل المنسق
    """
    if len(sequence) <= max_length:
        return sequence
    
    lines = []
    for i in range(0, len(sequence), max_length):
        start = i + 1
        end = min(i + max_length, len(sequence))
        line = sequence[i:i + max_length]
        lines.append(f"{start:4d} {line} {end:4d}")
    
    return '\n'.join(lines)


def count_amino_acids(sequence):
    """
    عد أنواع الأحماض الأمينية في التسلسل
    
    Args:
        sequence: تسلسل البروتين
    
    Returns:
        dict: عدد كل نوع
    """
    counts = {'H': 0, 'P': 0}
    
    for aa in sequence.upper():
        if aa in counts:
            counts[aa] += 1
    
    counts['total'] = len(sequence)
    counts['h_percentage'] = (counts['H'] / counts['total'] * 100) if counts['total'] > 0 else 0
    
    return counts


def generate_sequence_report(sequence):
    """
    إنشاء تقرير مفصل عن التسلسل
    
    Args:
        sequence: تسلسل البروتين
    
    Returns:
        str: نص التقرير
    """
    counts = count_amino_acids(sequence)
    
    report = []
    report.append("=" * 60)
    report.append("PROTEIN SEQUENCE REPORT")
    report.append("=" * 60)
    report.append(f"\nSequence Length: {counts['total']} amino acids")
    report.append(f"Hydrophobic (H): {counts['H']} ({counts['h_percentage']:.1f}%)")
    report.append(f"Polar (P): {counts['P']} ({100 - counts['h_percentage']:.1f}%)")
    report.append("\nFormatted Sequence:")
    report.append("-" * 60)
    report.append(format_sequence_for_display(sequence))
    report.append("-" * 60)
    report.append("=" * 60)
    
    return '\n'.join(report)
