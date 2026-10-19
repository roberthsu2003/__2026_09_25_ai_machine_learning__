# 任務卡：溫度轉換程式（攝氏與華氏雙向轉換）

## 你的需求（原話）
找一個小模型幫我寫溫度轉換的程式，攝氏轉華氏，寫完你檢查。我還要一個,華氐轉攝氐的功能，直接開opencode,不要指定模型。

## 我的理解：要做什麼
1. 在 `work/temperature/` 目錄建立一個名為 `temperature.py` 的 Python 程式檔案。
2. 檔案內需包含兩個 Function(函式)：
   - `celsius_to_fahrenheit(celsius)`：輸入攝氏溫度，計算並回傳華氏溫度。
   - `fahrenheit_to_celsius(fahrenheit)`：輸入華氏溫度，計算並回傳攝氏溫度。
3. 程式碼中的註解需符合規則：上方中文、下方英文。

## 分工
- SubAgent(子代理)：`temp-coder`（OpenCode，使用預設 Model(模型)，不額外指定模型）
- 工作目錄：`/Users/roberthsu2003/Documents/GitHub/2026_09_25_ai_machine_learning/herdr-lab/work/temperature`

## 驗收標準
- 檔案 `work/temperature/temperature.py` 存在。
- 檔案中定義了 `celsius_to_fahrenheit` 與 `fahrenheit_to_celsius` 兩個函式。
- 攝氏轉華氏測試通過（0°C -> 32°F、100°C -> 212°F、-40°C -> -40°F、37°C -> 98.6°F）。
- 華氏轉攝氏測試通過（32°F -> 0°C、212°F -> 100°C、-40°F -> -40°C、98.6°F -> 37°C）。
- 驗收指令：`uvx pytest -q checks/temperature/test_temperature.py`

## 派工指示（我會傳給 SubAgent 的原文）
你是 SubAgent，只負責完成下面的任務，不要執行任何 herdr 指令，也不要執行 git commit，做完回覆『完成』。

請在當前目錄建立一個名為 `temperature.py` 的檔案，實作溫度轉換功能：
1. 建立名為 `celsius_to_fahrenheit(celsius)` 的函式：
   - 輸入攝氏溫度，回傳計算後的華氏溫度數值。
   - 公式：華氏 = 攝氏 * 9 / 5 + 32
2. 建立名為 `fahrenheit_to_celsius(fahrenheit)` 的函式：
   - 輸入華氏溫度，回傳計算後的攝氏溫度數值。
   - 公式：攝氏 = (華氏 - 32) * 5 / 9
3. 如果程式碼要寫註解，請遵循格式：上面用中文，下方用英文。
4. 保持程式碼簡潔清晰。做完請回覆『完成』。
