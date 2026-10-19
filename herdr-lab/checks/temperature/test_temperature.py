import sys
from pathlib import Path
import pytest

# 將 SubAgent 工作目錄加入 Python 搜尋路徑
# Add the SubAgent working directory to Python search path
work_dir = Path(__file__).resolve().parent.parent.parent / "work" / "temperature"
sys.path.insert(0, str(work_dir))

from temperature import celsius_to_fahrenheit, fahrenheit_to_celsius

# --- 攝氏轉華氏測試 ---
# --- Celsius to Fahrenheit tests ---

def test_celsius_to_fahrenheit_freezing():
    # 測試攝氏 0 度轉換為華氏 32 度
    # Test 0 Celsius converts to 32 Fahrenheit
    assert celsius_to_fahrenheit(0) == 32.0

def test_celsius_to_fahrenheit_boiling():
    # 測試攝氏 100 度轉換為華氏 212 度
    # Test 100 Celsius converts to 212 Fahrenheit
    assert celsius_to_fahrenheit(100) == 212.0

def test_celsius_to_fahrenheit_negative():
    # 測試攝氏 -40 度轉換為華氏 -40 度
    # Test -40 Celsius converts to -40 Fahrenheit
    assert celsius_to_fahrenheit(-40) == -40.0

def test_celsius_to_fahrenheit_body_temp():
    # 測試攝氏 37 度轉換為華氏 98.6 度
    # Test 37 Celsius converts to 98.6 Fahrenheit
    assert pytest.approx(celsius_to_fahrenheit(37), 0.1) == 98.6

# --- 華氏轉攝氏測試 ---
# --- Fahrenheit to Celsius tests ---

def test_fahrenheit_to_celsius_freezing():
    # 測試華氏 32 度轉換為攝氏 0 度
    # Test 32 Fahrenheit converts to 0 Celsius
    assert fahrenheit_to_celsius(32) == 0.0

def test_fahrenheit_to_celsius_boiling():
    # 測試華氏 212 度轉換為攝氏 100 度
    # Test 212 Fahrenheit converts to 100 Celsius
    assert fahrenheit_to_celsius(212) == 100.0

def test_fahrenheit_to_celsius_negative():
    # 測試華氏 -40 度轉換為攝氏 -40 度
    # Test -40 Fahrenheit converts to -40 Celsius
    assert fahrenheit_to_celsius(-40) == -40.0

def test_fahrenheit_to_celsius_body_temp():
    # 測試華氏 98.6 度轉換為攝氏 37 度
    # Test 98.6 Fahrenheit converts to 37 Celsius
    assert pytest.approx(fahrenheit_to_celsius(98.6), 0.1) == 37.0
