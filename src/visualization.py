"""
Visualization Module for Universal SAT/CNF Framework
Contains functions for 3D structure visualization and analysis plots.

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

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns


def visualize_structure(coordinates, sequence, title="Protein Structure", save_path=None):
    """
    تصور هيكل البروتين ثلاثي الأبعاد
    
    Args:
        coordinates: قائمة الإحداثيات [(x,y,z), ...]
        sequence: تسلسل البروتين
        title: عنوان الرسم
        save_path: مسار الحفظ (اختياري)
    """
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    coords = np.array(coordinates)
    x, y, z = coords[:, 0], coords[:, 1], coords[:, 2]
    
    # تلوين الأحماض الأمينية حسب النوع
    colors = ['red' if aa == 'H' else 'blue' for aa in sequence]
    sizes = [100 if aa == 'H' else 60 for aa in sequence]
    
    # رسم النقاط
    scatter = ax.scatter(x, y, z, c=colors, s=sizes, alpha=0.8, edgecolors='black')
    
    # رسم الروابط بين الأحماض المتتالية
    for i in range(len(coordinates) - 1):
        ax.plot([x[i], x[i+1]], [y[i], y[i+1]], [z[i], z[i+1]], 
                'gray', linewidth=2, alpha=0.6)
    
    # إضافة تسميات
    for i, (xi, yi, zi) in enumerate(zip(x, y, z)):
        ax.text(xi, yi, zi, f'{i}:{sequence[i]}', fontsize=9, ha='right')
    
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title(title, fontsize=14, fontweight='bold')
    
    # تحسين العرض
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Structure saved to {save_path}")
    
    plt.show()
    
    return fig, ax


def plot_energy_comparison(results_list, save_path=None):
    """
    رسم مقارنة الطاقة بين تسلسلات مختلفة
    
    Args:
        results_list: قائمة من نتائج المحاكاة
        save_path: مسار الحفظ (اختياري)
    """
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    sequences = [r['sequence'] for r in results_list]
    lengths = [r['length'] for r in results_list]
    times = [r['total_time'] for r in results_list]
    clauses = [r['n_clauses'] for r in results_list]
    
    # الرسم 1: الوقت مقابل طول التسلسل
    axes[0, 0].plot(lengths, times, 'bo-', linewidth=2, markersize=8)
    axes[0, 0].set_xlabel('Sequence Length', fontsize=12)
    axes[0, 0].set_ylabel('Computation Time (s)', fontsize=12)
    axes[0, 0].set_title('Computation Time vs Sequence Length', fontsize=14, fontweight='bold')
    axes[0, 0].grid(True, alpha=0.3)
    
    # الرسم 2: عدد القيود مقابل طول التسلسل
    axes[0, 1].plot(lengths, clauses, 'ro-', linewidth=2, markersize=8)
    axes[0, 1].set_xlabel('Sequence Length', fontsize=12)
    axes[0, 1].set_ylabel('Number of Clauses', fontsize=12)
    axes[0, 1].set_title('Problem Complexity vs Sequence Length', fontsize=14, fontweight='bold')
    axes[0, 1].grid(True, alpha=0.3)
    
    # الرسم 3: توزيع الأزمنة
    axes[1, 0].hist(times, bins='auto', color='skyblue', edgecolor='black', alpha=0.7)
    axes[1, 0].set_xlabel('Time (s)', fontsize=12)
    axes[1, 0].set_ylabel('Frequency', fontsize=12)
    axes[1, 0].set_title('Distribution of Computation Times', fontsize=14, fontweight='bold')
    axes[1, 0].grid(True, alpha=0.3)
    
    # الرسم 4: كفاءة الخوارزمية
    efficiency = [length / time if time > 0 else 0 for length, time in zip(lengths, times)]
    axes[1, 1].bar(range(len(sequences)), efficiency, color='green', alpha=0.7)
    axes[1, 1].set_xlabel('Sequence Index', fontsize=12)
    axes[1, 1].set_ylabel('Efficiency (AA/s)', fontsize=12)
    axes[1, 1].set_title('Algorithm Efficiency', fontsize=14, fontweight='bold')
    axes[1, 1].set_xticks(range(len(sequences)))
    axes[1, 1].set_xticklabels([f'S{i+1}' for i in range(len(sequences))], rotation=45)
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Comparison plots saved to {save_path}")
    
    plt.show()
    
    return fig, axes


def plot_3d_rotation_animation(coordinates, sequence, save_path=None):
    """
    إنشاء رسوم متحركة لدوران الهيكل ثلاثي الأبعاد
    (يتطلب تثبيت ffmpeg للفيديو)
    
    Args:
        coordinates: قائمة الإحداثيات
        sequence: تسلسل البروتين
        save_path: مسار الحفظ (اختياري)
    """
    from matplotlib.animation import FuncAnimation
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    coords = np.array(coordinates)
    colors = ['red' if aa == 'H' else 'blue' for aa in sequence]
    
    def update(angle):
        ax.clear()
        ax.scatter(coords[:, 0], coords[:, 1], coords[:, 2], 
                  c=colors, s=80, alpha=0.8)
        
        # رسم الروابط
        for i in range(len(coords) - 1):
            ax.plot([coords[i, 0], coords[i+1, 0]],
                   [coords[i, 1], coords[i+1, 1]],
                   [coords[i, 2], coords[i+1, 2]],
                   'gray', linewidth=2, alpha=0.6)
        
        ax.view_init(elev=20, azim=angle)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f'Protein Structure - Rotation {angle}°')
        
        return ax
    
    anim = FuncAnimation(fig, update, frames=np.linspace(0, 360, 36),
                        interval=100, blit=False)
    
    if save_path:
        anim.save(save_path, writer='pillow', fps=10)
        print(f"Animation saved to {save_path}")
    
    plt.show()
    
    return anim


def create_contact_map(coordinates, sequence, save_path=None):
    """
    إنشاء خريطة التلامس للبروتين
    
    Args:
        coordinates: قائمة الإحداثيات
        sequence: تسلسل البروتين
        save_path: مسار الحفظ (اختياري)
    """
    n = len(sequence)
    contact_matrix = np.zeros((n, n))
    
    for i in range(n):
        for j in range(i + 1, n):
            dist = sum(abs(coordinates[i][d] - coordinates[j][d]) for d in range(3))
            if dist == 1:  # متجاوران مكانياً
                contact_matrix[i, j] = 1
                contact_matrix[j, i] = 1
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # إنشاء heatmap
    sns.heatmap(contact_matrix, annot=True, fmt='.0f', cmap='YlOrRd',
               xticklabels=[f'{i}:{s}' for i, s in enumerate(sequence)],
               yticklabels=[f'{i}:{s}' for i, s in enumerate(sequence)],
               ax=ax, cbar_kws={'label': 'Contact (1=Yes, 0=No)'})
    
    ax.set_title('Protein Contact Map', fontsize=14, fontweight='bold')
    ax.set_xlabel('Amino Acid Index', fontsize=12)
    ax.set_ylabel('Amino Acid Index', fontsize=12)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Contact map saved to {save_path}")
    
    plt.show()
    
    return fig, ax, contact_matrix
