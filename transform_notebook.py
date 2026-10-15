import json

def transform_notebook(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    translations = {
        "儲存格 1：設定視覺化中文字型（繁體中文顯示）": "Cell 1: Set up visualization font (Traditional Chinese display)",
        "匯入 glob 模組：用於批次搜尋字型檔路徑": "Import glob module: for batch searching font file paths",
        "匯入 os 模組：處理檔案路徑拼接": "Import os module: for handling file path concatenation",
        "匯入 mplfonts 套件：提供中文字型檔與快速設定工具": "Import mplfonts package: provides Chinese fonts and quick setup tools",
        "從 Matplotlib 匯入字型管理器：用於手動註冊字型": "Import font manager from Matplotlib: used for manual font registration",
        "匯入 Matplotlib 繪圖模組：建立圖表的基礎工具": "Import Matplotlib plotting module: basic tool for creating charts",
        "匯入 Seaborn 套件：進階統計繪圖（基於 Matplotlib）": "Import Seaborn package: advanced statistical plotting (based on Matplotlib)",
        "從 mplfonts 匯入快速套用字型函式": "Import quick font application function from mplfonts",
        "迴圈註冊 mplfonts 內附的所有 .otf / .ttf 字型檔": "Loop to register all .otf / .ttf font files included in mplfonts",
        "將找到的字型逐一加入 Matplotlib 字型管理器": "Add found fonts one by one to Matplotlib font manager",
        "套用 Noto Sans CJK SC 字型（支援繁體中文顯示）": "Apply Noto Sans CJK SC font (supports Traditional Chinese display)",
        "設定負號正常顯示，避免中文模式下變成方塊": "Set negative signs to display normally to avoid squares in Chinese mode",
        "印出成功訊息，確認字型已載入": "Print success message to confirm font is loaded",
        "儲存格 2：匯入套件並讀取房產資料集": "Cell 2: Import packages and read the real estate dataset",
        "匯入 Pandas：處理表格資料（DataFrame）的核心套件": "Import Pandas: core package for handling tabular data (DataFrame)",
        "匯入 NumPy：數值運算基礎套件（後續特徵工程用）": "Import NumPy: basic package for numerical computation (used for feature engineering)",
        "匯入 Matplotlib：底層繪圖套件": "Import Matplotlib: low-level plotting package",
        "匯入 Seaborn：高階統計視覺化套件": "Import Seaborn: high-level statistical visualization package",
        "1. 讀取繁體中文來源資料集（CSV 檔，需與 ipynb 同目錄）": "1. Read the Traditional Chinese source dataset (CSV file, must be in the same directory as ipynb)",
        "印出標題提示": "Print title prompt",
        "顯示前 5 筆資料，快速檢查欄位與內容": "Display the first 5 rows to quickly check columns and content",
        "儲存格 3：區分特徵矩陣 X 與標籤向量 y": "Cell 3: Distinguish Feature Matrix X and Label Vector y",
        "觀念：特徵 Feature 是模型的輸入，標籤 Label 是模型要預測的答案": "Concept: Features are the model's inputs, Labels are the answers the model predicts",
        "2. 選取 4 個欄位作為特徵矩陣 X（2D DataFrame：樣本數 x 特徵數）": "2. Select 4 columns as the feature matrix X (2D DataFrame: samples x features)",
        "選取房屋總價作為標籤向量 y（1D Series：只有一欄目標值）": "Select house total price as the label vector y (1D Series: single target column)",
        "印出 X 的形狀，確認樣本數與特徵數": "Print shape of X to confirm the number of samples and features",
        "印出 y 的形狀，確認樣本數（應與 X 列數一致）": "Print shape of y to confirm the number of samples (should match X rows)",
        "印出分隔標題，準備查看各特徵型態": "Print separator title to prepare for viewing each feature's data type",
        "查看每個特徵的資料型態：數值型 vs 類別型影響後續編碼方式": "View data types of each feature: Numerical vs Categorical affects subsequent encoding",
        "儲存格 4：視覺化特徵與標籤的關係（散佈圖）": "Cell 4: Visualize the relationship between features and labels (Scatter plot)",
        "3. 繪製特徵與標籤的關係圖：用圖形理解資料趨勢": "3. Plot relationship between features and labels: understand data trends via graphics",
        "新建圖形，設定寬 8 吋、高 5 吋": "Create a new figure, setting width to 8 inches and height to 5 inches",
        "繪製散佈圖：X=建築坪數，Y=房屋總價，並以行政區域上色區分": "Plot scatter plot: X=Building Area, Y=House Total Price, colored by administrative district",
        "設定圖表標題": "Set chart title",
        "設定 X 軸標籤（含單位：坪）": "Set X-axis label (includes unit: Ping)",
        "設定 Y 軸標籤（含單位：萬元）": "Set Y-axis label (includes unit: 10k)",
        "設定顯示虛線格線，提升數值判讀性": "Set dashed grid lines to improve readability",
        "自動調整版面，避免標籤被裁切": "Automatically adjust layout to prevent label clipping",
        "顯示圖表": "Display chart",
        "觀念總結：特徵矩陣 X 是模型觀察的世界，標籤 y 則是模型要預測的解答！": "Concept Summary: Feature Matrix X is the world the model observes, Label Vector y is the answer the model predicts!"
    }

    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            new_source = []
            original_source = cell['source']
            
            i = 0
            while i < len(original_source):
                line = original_source[i]
                # Determine if it's a comment line
                stripped = line.strip()
                if stripped.startswith("#") and len(stripped) > 1 and stripped != "#" and stripped != "# ":
                    # It's a comment
                    indent = line[:line.find("#")]
                    content = stripped[1:].strip()
                    
                    eng_content = translations.get(content)
                    if eng_content:
                        new_line = f"{indent}# {content}\n# {eng_content}\n"
                        new_source.append(new_line)
                        i += 1
                        # Check if we should add a blank line after this comment block
                        if i < len(original_source):
                            next_line = original_source[i]
                            if not next_line.strip().startswith("#"):
                                new_source.append("\n")
                        continue
                
                new_source.append(line)
                i += 1
            
            cell['source'] = new_source

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

if __name__ == "__main__":
    transform_notebook('/Users/roberthsu2003/Documents/GitHub/2026_09_25_ai_machine_learning/10_13/feature.ipynb')
