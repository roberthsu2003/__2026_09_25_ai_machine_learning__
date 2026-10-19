# 任務卡：KNN 機器學習演算法初學者教學範例筆記本

## 你的需求（原話）
我要制作一個機器學習,knn演算法的範例,這個是要教學生的,所以我要有ipynb,必需要有良好的註解,能讓學生看的懂,必需要有訓練集和測試集,必需做特徵工程,必需要有評估,而且最後建議學生使用那一個超參數
我沒有資料集,圖表和顯示文字,一律使用繁體中文,不要有太多的專業語法,如果有專業語法,請下面增加白話的語法

## 我的理解：要做什麼
1. 在 `work/knn/` 目錄建立一個教學專用的 Jupyter Notebook 檔案：`knn_tutorial.ipynb`。
2. 使用 Scikit-Learn 內建經典且直觀的 Dataset(資料集)（例如：經典的鳶尾花資料集 `load_iris`），不需要額外下載外部檔案。
3. 包含完整清晰的 Machine Learning(機器學習) 步驟：
   - **載入資料與探索**：白話解說什麼是 Feature(特徵) 與 Target(目標/標籤)。
   - **拆分資料集**：切分為 Training Set(訓練集) 與 Test Set(測試集)，白話解釋為什麼不能用考試題目來複習。
   - **Feature Engineering(特徵工程)**：進行 Feature Scaling(特徵縮放，如 `StandardScaler`)，白話說明為什麼計算距離的演算法必須把特徵尺度縮放一致。
   - **Model Training(模型訓練)**：使用 `KNeighborsClassifier` 演算法，白話解釋 KNN 原理（「近朱者赤，近墨者黑」投票機制）。
   - **Model Evaluation(模型評估)**：計算 Accuracy(準確率) 並以混淆矩陣或圖表輔助說明。
   - **Hyperparameter(超參數) 尋優與建議**：測試不同的 K 值（`n_neighbors` 從 1 到 20），繪製 K 值與準確率關係折線圖，最後給學生明確的建議（例如選擇最穩定的 K 值，避免 Overfitting(過度擬合) 或 Underfitting(擬合不足)）。
4. 語言與格式規範：
   - 圖表與所有文字說明一律使用繁體中文，Matplotlib 需設定繁體中文字型支援（如微軟正黑體、PingFang HK/TC 或 sans-serif 避免中文亂碼）。
   - 避免生硬語法，若出現專有名詞或專業語法，下方皆需附上白話語法/白話生活比喻。
   - 程式碼註解依照規定：**上面用中文，下方用英文**。

## 分工
- SubAgent(子代理)：`knn-tutor`（OpenCode）
- 工作目錄：`/Users/roberthsu2003/Documents/GitHub/2026_09_25_ai_machine_learning/herdr-lab/work/knn`

## 驗收標準
- 檔案 `work/knn/knn_tutorial.ipynb` 存在且格式正確。
- Notebook 包含以下完整教學單元：
  1. 內建資料集載入與特徵說明
  2. 訓練集與測試集拆分（`train_test_split`）
  3. 特徵工程與縮放（`StandardScaler` 或 `MinMaxScaler`）
  4. KNN 模型訓練（`KNeighborsClassifier`）
  5. 模型評估指標與圖表
  6. K 值超參數分析與最終推薦建議
- 註解與文字說明符合要求（繁體中文、雙語註解、專業名詞附白話解釋）。
- 驗收指令：`uvx pytest -q checks/knn/test_knn_notebook.py`

## 派工指示（我會傳給 SubAgent 的原文）
你是 SubAgent，只負責完成下面的任務，不要執行任何 herdr 指令，也不要執行 git commit，做完回覆『完成』。

請在當前目錄建立一個給初學者學生的教學 Jupyter Notebook：`knn_tutorial.ipynb`。

教學目標是讓學生理解 KNN (K-Nearest Neighbors，K-近鄰演算法)，請依序包含以下單元（每個步驟都要有 Markdown 說明單元格與 Code 程式碼單元格）：

1. **認識資料集 Dataset**：
   - 使用 `sklearn.datasets.load_iris` 載入內建鳶尾花資料。
   - 用表格展示前 5 筆資料，用白話解釋什麼是 Feature(特徵)（花萼、花瓣長寬）與 Target(目標標籤)（花朵品種）。
2. **切分資料集 Data Splitting**：
   - 使用 `train_test_split` 將資料切分為 Training Set(訓練集) 與 Test Set(測試集)（例如 80% / 20%）。
   - 白話說明：就像平時練習題（訓練集）與期末考卷（測試集），考試不能先偷看答案。
3. **Feature Engineering(特徵工程) - 特徵縮放**：
   - 使用 `sklearn.preprocessing.StandardScaler` 做標準化縮放。
   - 白話說明：KNN 是算幾何距離的，如果身高用公分（170）、體重用公斤（65），數字大的特徵會霸道地主導距離，所以必須把它們放在同一個天平上。
4. **KNN 模型訓練與原理**：
   - 使用 `sklearn.neighbors.KNeighborsClassifier`。
   - 白話說明：「物以類聚、近朱者赤」，看看身邊最靠近的 K 個鄰居大多是什麼品種，就投票決定它是什麼品種。
5. **Model Evaluation(模型評估)**：
   - 計算測試集的 Accuracy(準確率)。
   - 繪製繁體中文混淆矩陣圖或評估說明。
6. **尋找最佳 Hyperparameter(超參數) K 值與建議**：
   - 測試 K = 1 到 20 的模型表現。
   - 使用 Matplotlib 繪製折線圖（X軸：K值、Y軸：準確率），圖表標題與軸標籤一律使用繁體中文（請設定支援繁中的字型設定）。
   - 明確總結並給學生建議：建議學生挑選哪一個 K 值（例如 K=3 或 K=5），並用白話解釋為什麼太小（K=1）容易受雜訊干擾 Overfitting(過度擬合)，太大又會失去局部特徵 Underfitting(擬合不足)。

特別注意規範：
- 如果程式碼要寫註解，請遵循：上面用中文，下方用英文。
- 專有名詞請使用：英文(中文) 形式，並附白話對照。
- 儲存為合法的 `.ipynb` 檔案。做完請回覆『完成』。
