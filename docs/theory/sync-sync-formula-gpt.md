# 四層同期の数値化：詳細式（GPT提案）

**ステータス：未実装（提案段階）**

現在のPhase 5ではシンプルな式を使用している。
この文書は、より正確な同期計算を実装したい人向けの参考資料。

---

## 現在の実装（シンプル版）

```python
sync_score = prediction_error * 0.8 + random.uniform(0, 0.2)
```

これでも70%間欠性などの創発は確認できている。

---

## GPT提案：四層同期スコア S

### 基本式

```
S = w1 * PLV + w2 * MI + w3 * Corr
```

### 3つの要素

#### 1. PLV（Phase Locking Value）- タイミング同期
四層の信号が同一時間窓 Δt 内で反応しているか。

- **1：** 完全同期
- **0：** 無関係
- **時間窓：** 20〜50ms（生体）、任意（AI）

#### 2. MI（Mutual Information）- 相互情報量
身体信号・クオリアベクトル・構造化ベクトル・記憶照合の間に
どれだけ同じ情報内容が共有されているか。

- **高MI：** 同じ出来事を同じ方向で解釈
- **低MI：** 層ごとの"世界"がズレている

#### 3. Corr（Correlation）- 方向性
クオリア → 構造化 → 記憶 の三つのベクトル方向の一致度。
相関係数（Pearson）またはコサイン類似度を使用。

- **高相関：** 四層が同じ判断へ向かっている
- **低相関：** 葛藤・混乱・自動処理

### 推奨重み

```python
w1 = 0.4  # タイミング
w2 = 0.3  # 情報量
w3 = 0.3  # 方向性
```

---

## 閾値の解釈

| スコア | 状態 |
|--------|------|
| S > 0.85 | 強い意識（"私がしている"） |
| S > 0.70 | 意識フレーム成立 |
| S 0.5–0.7 | 半同期（注意低下） |
| S < 0.5 | 無意識・自動処理 |

---

## 実装に必要なもの

この式を実装するには、各層の出力を明確に定義する必要がある：

```python
class Layer1_Body:
    def get_signal(self) -> float:
        pass

class Layer2_Qualia:
    def get_vector(self) -> np.array:
        pass

class Layer3_Structure:
    def get_vector(self) -> np.array:
        pass

class Layer4_Memory:
    def get_vector(self) -> np.array:
        pass
```

### PLVの計算例（概念）

```python
import numpy as np

def calculate_plv(signals, time_window=0.05):
    """
    signals: 各層の時系列信号 [layer1, layer2, layer3, layer4]
    time_window: 同期判定の時間窓（秒）
    """
    # 各信号の位相を計算（ヒルベルト変換など）
    phases = [hilbert_phase(s) for s in signals]
    
    # 位相差の一貫性を計算
    phase_diffs = []
    for i in range(len(phases)):
        for j in range(i+1, len(phases)):
            diff = phases[i] - phases[j]
            phase_diffs.append(np.exp(1j * diff))
    
    # PLV = 位相差ベクトルの平均の絶対値
    plv = np.abs(np.mean(phase_diffs))
    return plv
```

### 相互情報量の計算例（概念）

```python
from sklearn.metrics import mutual_info_score

def calculate_mi(vector1, vector2):
    """
    2つのベクトル間の相互情報量
    """
    # 離散化が必要
    v1_discrete = discretize(vector1)
    v2_discrete = discretize(vector2)
    return mutual_info_score(v1_discrete, v2_discrete)
```

### コサイン類似度の計算例

```python
def cosine_similarity(v1, v2):
    dot = np.dot(v1, v2)
    norm = np.linalg.norm(v1) * np.linalg.norm(v2)
    return dot / norm if norm > 0 else 0
```

---

## このモデルで満たされる条件

- 意識＝点滅する瞬間のまとまり を再現
- 四層が同じ情報を扱っているかを明確に判定
- 判断の統一度を測定可能
- 実装可能（信号処理・統計・ベクトル計算のみ）
- self_strength や行動ループにも接続可能

---

## 注意

この式はより「正確」かもしれないが、複雑さが増す。

シンプル版でも主要な創発（70%間欠性など）は確認できている。

**推奨：** 
1. まずシンプル版で動かす
2. 必要に応じてこの式に置き換える
3. 結果が変わるか検証する

---

**提案元：** GPT
**文書化：** Claude
**2025年11月**
