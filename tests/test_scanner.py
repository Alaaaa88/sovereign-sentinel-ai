import os
import pytest

# اختبار للتأكد من وجود المحرك الأساسي (Core Engine)
def test_core_engine_exists():
    assert os.path.exists("core-engine/scanner"), "Core engine binary not found!"

# اختبار بسيط للتأكد من أن الاختبارات تعمل
def test_placeholder():
    assert True
