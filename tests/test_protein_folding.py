"""
Test Module for Universal SAT/CNF Framework
Unit tests for optimizer, visualization, and utility functions.

Copyright (c) 2026 Universal SAT/CNF Framework Team. All Rights Reserved.
This software is proprietary and confidential.
Commercial use is strictly prohibited without a written license agreement.
"""

import unittest
import os
import sys

# إضافة مسار src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from optimizer import validate_sequence, calculate_energy, build_optimized_hp_wcnf_3d
from utils import count_amino_acids, normalize_sequence, format_sequence_for_display


class TestOptimizer(unittest.TestCase):
    """اختبارات دوال التحسين"""
    
    def test_validate_sequence_valid(self):
        """التحقق من تسلسلات صالحة"""
        self.assertTrue(validate_sequence("HPPH"))
        self.assertTrue(validate_sequence("HPHPHP"))
        self.assertTrue(validate_sequence("HHHH"))
        self.assertTrue(validate_sequence("PPPP"))
    
    def test_validate_sequence_invalid(self):
        """التحقق من تسلسلات غير صالحة"""
        self.assertFalse(validate_sequence("ABC"))
        self.assertFalse(validate_sequence("HPPX"))
        self.assertFalse(validate_sequence(""))
        self.assertFalse(validate_sequence("123"))
    
    def test_calculate_energy(self):
        """اختبار حساب الطاقة"""
        # حالة بسيطة: لا تلامسات
        coords = [(0, 0, 0), (1, 0, 0), (2, 0, 0)]
        sequence = "HPH"
        energy = calculate_energy(coords, sequence)
        self.assertEqual(energy, 0)  # H غير متجاورين
        
        # حالة مع تلامس H-H
        coords = [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0)]
        sequence = "HPPH"
        energy = calculate_energy(coords, sequence)
        # H في (0,0,0) و (1,0,0) - المسافة = 1
        self.assertEqual(energy, -1)


class TestUtils(unittest.TestCase):
    """اختبارات الدوال المساعدة"""
    
    def test_count_amino_acids(self):
        """اختبار عد الأحماض الأمينية"""
        sequence = "HPPHHP"
        counts = count_amino_acids(sequence)
        
        self.assertEqual(counts['H'], 3)
        self.assertEqual(counts['P'], 3)
        self.assertEqual(counts['total'], 6)
        self.assertAlmostEqual(counts['h_percentage'], 50.0)
    
    def test_normalize_sequence(self):
        """اختبار توحيد التسلسل"""
        self.assertEqual(normalize_sequence("hpph"), "HPPH")
        self.assertEqual(normalize_sequence("H-P-P-H"), "HPPH")
        self.assertEqual(normalize_sequence("h p p h"), "HPPH")
    
    def test_format_sequence_for_display(self):
        """اختبار تنسيق العرض"""
        sequence = "HPPH" * 15  # 60 حرف
        formatted = format_sequence_for_display(sequence, max_length=20)
        
        lines = formatted.split('\n')
        self.assertEqual(len(lines), 3)  # 60 / 20 = 3 أسطر
        
        # التحقق من أن كل سطر يحتوي على 20 حرف
        for line in lines[:-1]:  # جميع الأسطر ما عدا الأخير
            parts = line.split()
            if len(parts) >= 2:
                self.assertEqual(len(parts[1]), 20)


class TestIntegration(unittest.TestCase):
    """اختبارات التكامل"""
    
    def test_full_pipeline(self):
        """اختبار خط الأنابيب الكامل"""
        sequence = "HPPH"
        
        # التحقق من الصحة
        self.assertTrue(validate_sequence(sequence))
        
        # العد
        counts = count_amino_acids(sequence)
        self.assertEqual(counts['total'], 4)
        
        # التوحيد
        normalized = normalize_sequence("h-p-p-h")
        self.assertEqual(normalized, "HPPH")


def run_tests():
    """تشغيل جميع الاختبارات"""
    # إنشاء مجموعة الاختبارات
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # إضافة الاختبارات
    suite.addTests(loader.loadTestsFromTestCase(TestOptimizer))
    suite.addTests(loader.loadTestsFromTestCase(TestUtils))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # تشغيل الاختبارات
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
