import json
from pathlib import Path
import pytest

# 將 SubAgent 工作目錄設定為檢查目標
# Set SubAgent working directory as the target for checking
work_dir = Path(__file__).resolve().parent.parent.parent / "work" / "knn"
notebook_path = work_dir / "knn_tutorial.ipynb"

@pytest.fixture(scope="module")
def notebook_data():
    # 確保 Notebook 檔案存在且為合法 JSON
    # Ensure Notebook file exists and is valid JSON
    assert notebook_path.exists(), f"找不到檔案：{notebook_path}"
    with open(notebook_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def test_notebook_structure(notebook_data):
    # 檢查是否具備 Jupyter Notebook 基本結構
    # Check if basic Jupyter Notebook structure is present
    assert "cells" in notebook_data, "Notebook 缺少 cells 欄位"
    cells = notebook_data["cells"]
    assert len(cells) >= 6, "Notebook 的儲存格數量不足，應有完整教學步驟"

def test_key_machine_learning_steps(notebook_data):
    # 檢查是否涵蓋教學必備的機器學習步驟關鍵字
    # Check if essential machine learning tutorial steps and keywords are covered
    full_text = ""
    for cell in notebook_data["cells"]:
        source = cell.get("source", "")
        if isinstance(source, list):
            full_text += "".join(source) + "\n"
        elif isinstance(source, str):
            full_text += source + "\n"

    # 1. 資料集與模型
    # 1. Dataset and model
    assert "KNeighborsClassifier" in full_text, "未包含 KNN 分類器模型 (KNeighborsClassifier)"
    
    # 2. 訓練集與測試集拆分
    # 2. Training and test set split
    assert "train_test_split" in full_text, "未包含訓練集與測試集拆分 (train_test_split)"

    # 3. 特徵工程 (特徵縮放)
    # 3. Feature engineering (feature scaling)
    assert any(scaler in full_text for scaler in ["StandardScaler", "MinMaxScaler"]), "未包含特徵工程/特徵縮放 (StandardScaler 或 MinMaxScaler)"

    # 4. 模型評估
    # 4. Model evaluation
    assert any(metric in full_text for metric in ["accuracy_score", "score", "confusion_matrix", "classification_report"]), "未包含模型評估指標"

    # 5. K 值超參數建議與圖表
    # 5. K value hyperparameter recommendation and visualization
    assert any(k_word in full_text for k_word in ["n_neighbors", "超參數", "Hyperparameter", "最佳"]), "未包含 K 值超參數探討與建議"

    # 6. 繁體中文與註解規則 (檢查關鍵繁體中文說明)
    # 6. Traditional Chinese and comment rules
    assert any(term in full_text for term in ["訓練集", "測試集", "特徵", "準確率"]), "內容未包含足夠的繁體中文說明"

def test_code_cells_syntax(notebook_data):
    # 檢查所有程式碼儲存格的 Python 語法是否完全正確
    # Check if Python syntax in all code cells is completely valid
    import ast
    for idx, cell in enumerate(notebook_data["cells"]):
        if cell.get("cell_type") == "code":
            source = "".join(cell.get("source", []))
            try:
                ast.parse(source)
            except SyntaxError as e:
                pytest.fail(f"儲存格 (Cell {idx}) 存在 Python 語法錯誤 (SyntaxError): {e}")

