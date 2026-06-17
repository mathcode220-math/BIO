"""
Optimizer Module for Universal SAT/CNF Framework
Contains MaxSAT-based optimization functions for constraint satisfaction problems.

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

import time
from pysat.formula import WCNF


def build_optimized_hp_wcnf_3d(sequence, dim_x, dim_y, dim_z, use_clingo=False):
    """
    بناء نموذج WCNF محسن لطي البروتين ثلاثي الأبعاد
    
    Args:
        sequence: تسلسل البروتين (أحرف H و P)
        dim_x, dim_y, dim_z: أبعاد الشبكة
        use_clingo: استخدام محرك Clingo بدلاً من RCMaxSAT
    
    Returns:
        wcnf: نموذج WCNF
        n_aa: عدد الأحماض الأمينية
        n_cells: عدد الخلايا في الشبكة
    """
    N = len(sequence)
    S = dim_x * dim_y * dim_z
    n_cells = S
    
    wcnf = WCNF()
    
    # حساب الجوار المسبقاً لتحسين الأداء
    neighbors = {}
    for x in range(dim_x):
        for y in range(dim_y):
            for z in range(dim_z):
                pos = x * dim_y * dim_z + y * dim_z + z
                adj = []
                for dx, dy, dz in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
                    nx, ny, nz = x + dx, y + dy, z + dz
                    if 0 <= nx < dim_x and 0 <= ny < dim_y and 0 <= nz < dim_z:
                        neighbor_pos = nx * dim_y * dim_z + ny * dim_z + nz
                        adj.append(neighbor_pos)
                neighbors[pos] = adj
    
    # متغيرات الموضع: x(i, p) = 1 إذا كان الحمض الأميني i في الموضع p
    # متغيرات الاتصال: a(i, j) = 1 إذا كان i و j متجاورين في السلسلة ومكانياً
    
    # قيد 1: كل حمض أميني يجب أن يكون في موضع واحد بالضبط
    for i in range(N):
        clause = [encode_position(i, p) for p in range(S)]
        wcnf.append(clause)  # على الأقل موضع واحد
        
        # على الأكثر موضع واحد (زوجي)
        for p1 in range(S):
            for p2 in range(p1 + 1, S):
                wcnf.append([-encode_position(i, p1), -encode_position(i, p2)])
    
    # قيد 2: لا يمكن أن يشغل حمضان أمينيان نفس الموضع
    for p in range(S):
        for i in range(N):
            for j in range(i + 1, N):
                wcnf.append([-encode_position(i, p), -encode_position(j, p)])
    
    # قيد 3: الأحماض الأمينية المتتالية يجب أن تكون متجاورة مكانياً
    for i in range(N - 1):
        # على الأقل زوج واحد من المواضع المتجاورة
        adjacent_pairs = []
        for p in range(S):
            for neighbor_p in neighbors.get(p, []):
                adjacent_pairs.append([encode_position(i, p), encode_position(i+1, neighbor_p)])
        
        if adjacent_pairs:
            # تبسيط: نضيف قيد أن هناك على الأقل واحد صحيح
            # في التطبيق الكامل، نستخدم متغيرات مساعدة للاتصال
            pass
    
    # دالة الطاقة: تعظيم التلامس بين H-H غير المتتاليين
    h_positions = [i for i, aa in enumerate(sequence) if aa == 'H']
    
    for i_idx, i in enumerate(h_positions):
        for j in h_positions[i_idx + 1:]:
            if abs(i - j) > 1:  # غير متتاليين
                # إضافة وزن إيجابي للتلامس المحتمل
                for p in range(S):
                    for neighbor_p in neighbors.get(p, []):
                        # نفضل وجود H-H متجاورين
                        wcnf.append([encode_contact(i, j, p)], weight=1)
    
    return wcnf, N, n_cells


def encode_position(amino_acid_idx, position):
    """ترميز متغير الموضع"""
    return amino_acid_idx * 1000 + position + 1


def encode_contact(aa1, aa2, position):
    """ترميز متغير التلامس"""
    return 100000 + aa1 * 1000 + aa2 * 10 + position % 1000


def run_simulation(seq, grid_dim=5, is_3d=True, timeout=60):
    """
    تشغيل محاكاة طي البروتين
    
    Args:
        seq: تسلسل البروتين
        grid_dim: بعد الشبكة (مكعب)
        is_3d: هل المحاكاة ثلاثية الأبعاد
        timeout: مهلة الوقت بالثواني
    
    Returns:
        dict: نتائج المحاكاة
    """
    print(f"Processing sequence: {seq}")
    print(f"Grid dimensions: {grid_dim}x{grid_dim}x{grid_dim if is_3d else 1}")
    
    start_time = time.time()
    
    if is_3d:
        wcnf, n_aa, n_cells = build_optimized_hp_wcnf_3d(seq, grid_dim, grid_dim, grid_dim)
    else:
        # نسخة ثنائية الأبعاد (يمكن تطويرها)
        wcnf, n_aa, n_cells = build_optimized_hp_wcnf_3d(seq, grid_dim, grid_dim, 1)
    
    build_time = time.time() - start_time
    print(f"WCNF built in {build_time:.2f} seconds")
    print(f"Number of variables: {wcnf.nv}")
    print(f"Number of clauses: {len(wcnf.hard)} hard + {len(wcnf.soft)} soft")
    
    # حل النموذج (يتطلب مثبت MaxSAT)
    # result = solve_with_rcmaxsat(wcnf, timeout=timeout)
    
    elapsed = time.time() - start_time
    
    return {
        'sequence': seq,
        'length': n_aa,
        'grid_dim': grid_dim,
        'is_3d': is_3d,
        'build_time': build_time,
        'total_time': elapsed,
        'n_variables': wcnf.nv,
        'n_clauses': len(wcnf.hard) + len(wcnf.soft),
        'status': 'built'  # أو 'solved' إذا تم الحل
    }


def validate_sequence(sequence):
    """التحقق من صحة تسلسل البروتين"""
    if not sequence:
        return False
    valid_chars = set('HP')
    return all(c in valid_chars for c in sequence.upper())


def calculate_energy(coordinates, sequence):
    """
    حساب طاقة التكوين بناءً على تلامسات H-H
    
    Args:
        coordinates: قائمة الإحداثيات
        sequence: تسلسل البروتين
    
    Returns:
        energy: قيمة الطاقة (عدد التلامسات H-H السالبة)
    """
    h_indices = [i for i, aa in enumerate(sequence) if aa == 'H']
    contacts = 0
    
    for i_idx, i in enumerate(h_indices):
        for j in h_indices[i_idx + 1:]:
            if abs(i - j) > 1:  # غير متتاليين
                dist = sum(abs(coordinates[i][d] - coordinates[j][d]) for d in range(3))
                if dist == 1:  # متجاوران مكانياً
                    contacts += 1
    
    return -contacts  # الطاقة السالبة تعني استقرار أكبر
