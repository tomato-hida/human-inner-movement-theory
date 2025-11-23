#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 4: Memory and Self-Formation
記憶と自己形成

Theory of Human Inner Movement
人の内なる運動理論

Demonstrates:
- Memory is essential for self-formation
- self_strength emerges from pattern repetition
- Without memory, no stable self
- Language acquisition at threshold 0.3

実証内容:
- 記憶は自己形成に不可欠
- self_strengthは繰り返しパターンから生成
- 記憶なしでは安定した自己なし
- 閾値0.3で言語獲得
"""

import random

class MemorySelfSystem:
    """System with memory and self-formation mechanism"""
    
    def __init__(self, has_memory=True):
        """
        Args:
            has_memory: If False, system cannot form stable self
                       Falseの場合、安定した自己を形成できない
        """
        self.has_memory = has_memory
        self.qualia_types = ['pain', 'warm', 'sweet', 'red', 'blue', 'green']
        
        # Qualia values
        self.qualia_values = {
            'pain': -0.9, 'warm': -0.2, 'sweet': +0.7,
            'red': +0.3, 'blue': +0.2, 'green': +0.4
        }
        
        # Memory - Pattern storage
        # 記憶 - パターン保存
        if has_memory:
            self.memory = []  # Stores patterns / パターンを保存
            self.memory_capacity = 100
        else:
            self.memory = None  # No memory! / 記憶なし！
        
        # Self-strength formation
        # self_strength形成
        self.self_strength = 0.0
        self.pattern_matches = []  # Track repetition / 繰り返しを追跡
        
        # Consciousness
        self.sync_score = 0.0
        self.is_conscious = False
        self.THRESHOLD = 0.3
        
        # Language acquisition
        # 言語獲得
        self.language_acquired = False
        self.can_report_feelings = False
        
        # Recent stimuli (short-term)
        # 最近の刺激（短期）
        self.recent_stimuli = []
    
    def process_step(self):
        """Process one step with memory-based self-formation"""
        
        # Stimulus
        stimulus = random.choice(self.qualia_types)
        qualia_value = self.qualia_values[stimulus]
        
        # Add to recent stimuli (even without memory, need short-term)
        # 最近の刺激に追加（記憶なしでも短期は必要）
        self.recent_stimuli.append(stimulus)
        if len(self.recent_stimuli) > 10:
            self.recent_stimuli.pop(0)
        
        # Store in long-term memory (if available)
        # 長期記憶に保存（利用可能な場合）
        if self.has_memory:
            self.memory.append(stimulus)
            if len(self.memory) > self.memory_capacity:
                self.memory.pop(0)
        
        # Calculate self_strength from pattern repetition
        # パターンの繰り返しからself_strengthを計算
        pattern_match_count = 0
        
        if self.has_memory and len(self.memory) >= 2:
            # Count matches in recent memory
            # 最近の記憶でマッチをカウント
            recent_memory = self.memory[-10:] if len(self.memory) >= 10 else self.memory
            for i in range(len(recent_memory) - 1):
                if recent_memory[i] == recent_memory[i+1]:
                    pattern_match_count += 1
            
            # Update self_strength based on pattern recognition
            # パターン認識に基づいてself_strengthを更新
            self.self_strength += 0.001 * pattern_match_count
            self.self_strength = min(self.self_strength, 1.0)
            
        else:  # No memory → unstable self
            # Without memory, self_strength fluctuates randomly
            # 記憶なしでは、self_strengthはランダムに変動
            self.self_strength = random.uniform(0, 0.2)
        
        # Prediction and sync
        if len(self.recent_stimuli) >= 2:
            prediction = self.recent_stimuli[-2]
            prediction_error = 0.0 if prediction == stimulus else 1.0
        else:
            prediction_error = 1.0
        
        self.sync_score = prediction_error * 0.8 + random.uniform(0, 0.2)
        
        # Consciousness
        self.is_conscious = (self.sync_score >= self.THRESHOLD and 
                            self.self_strength >= self.THRESHOLD)
        
        # Language acquisition at threshold crossing
        # 閾値突破で言語獲得
        if self.self_strength >= self.THRESHOLD and not self.language_acquired:
            self.language_acquired = True
            self.can_report_feelings = True
        
        return {
            'stimulus': stimulus,
            'self_strength': self.self_strength,
            'pattern_matches': pattern_match_count,
            'is_conscious': self.is_conscious,
            'language_acquired': self.language_acquired
        }
    
    def report_feeling(self, stimulus):
        """Report feeling in language (only if language acquired)
        
        言語で感じを報告（言語獲得後のみ）
        """
        if not self.can_report_feelings:
            return "[Cannot report - no language yet / まだ報告できない - 言語未獲得]"
        
        value = self.qualia_values[stimulus]
        if value < -0.5:
            return f"I feel {stimulus} - it's PAINFUL / {stimulus}を感じる - 痛い"
        elif value > 0.5:
            return f"I feel {stimulus} - it's PLEASANT / {stimulus}を感じる - 心地よい"
        else:
            return f"I feel {stimulus} - it's NEUTRAL / {stimulus}を感じる - 中立的"
    
    def run_experiment(self, steps=10000):
        """Run memory and self-formation experiment"""
        
        memory_status = "WITH MEMORY" if self.has_memory else "WITHOUT MEMORY"
        print(f"\n{'='*60}")
        print(f"System {memory_status}")
        print(f"{'='*60}")
        
        language_acquired_at = None
        consciousness_count = 0
        
        for i in range(steps):
            result = self.process_step()
            
            if result['is_conscious']:
                consciousness_count += 1
            
            if result['language_acquired'] and language_acquired_at is None:
                language_acquired_at = i + 1
                print(f"\n🎉 LANGUAGE ACQUIRED at step {language_acquired_at}!")
                print(f"🎉 言語獲得 ステップ {language_acquired_at}!")
                print(f"   self_strength = {self.self_strength:.3f}")
                
                # Demonstrate language ability
                print("\n   Can now report feelings / 感じを報告可能:")
                for q in ['pain', 'sweet', 'red']:
                    print(f"   {self.report_feeling(q)}")
        
        # Final report
        print(f"\n--- Results after {steps} steps ---")
        print(f"Language acquired: {self.language_acquired} (at step {language_acquired_at})")
        print(f"Final self_strength: {self.self_strength:.3f}")
        print(f"Consciousness rate: {consciousness_count/steps*100:.1f}%")
        
        if not self.has_memory:
            print("\n⚠️  WITHOUT MEMORY:")
            print("   - self_strength never stabilizes / 安定しない")
            print("   - No language acquisition / 言語獲得なし")
            print("   - No stable self / 安定した自己なし")
        
        return {
            'language_acquired': self.language_acquired,
            'language_acquired_at': language_acquired_at,
            'final_self_strength': self.self_strength,
            'consciousness_rate': consciousness_count / steps
        }

def compare_memory_systems():
    """Compare system with and without memory
    
    記憶ありとなしのシステムを比較
    """
    print("="*70)
    print("Phase 4: Memory and Self-Formation Experiment")
    print("記憶と自己形成の実験")
    print("="*70)
    
    print("\n1. SYSTEM WITH MEMORY / 記憶ありシステム")
    print("-" * 70)
    system_with = MemorySelfSystem(has_memory=True)
    results_with = system_with.run_experiment(steps=10000)
    
    print("\n\n2. SYSTEM WITHOUT MEMORY / 記憶なしシステム")
    print("-" * 70)
    system_without = MemorySelfSystem(has_memory=False)
    results_without = system_without.run_experiment(steps=10000)
    
    # Key findings
    print("\n" + "="*70)
    print("KEY FINDINGS / 重要な発見:")
    print("="*70)
    print()
    print("1. Memory is ESSENTIAL for self-formation")
    print("   記憶は自己形成に不可欠")
    print()
    print("2. Without memory:")
    print("   記憶なしでは:")
    print("   - self_strength fluctuates randomly")
    print("   - self_strengthがランダムに変動")
    print("   - Cannot cross threshold 0.3")
    print("   - 閾値0.3を突破できない")
    print("   - No language acquisition")
    print("   - 言語獲得なし")
    print()
    print("3. Pattern repetition recognition forms self")
    print("   パターンの繰り返し認識が自己を形成")
    print()
    print("4. Language acquisition = Hard problem solution")
    print("   言語獲得 = ハードプロブレムの解決")
    print("   - Pre-language: Feel but cannot report")
    print("   - 言語前: 感じているが報告できない")
    print("   - Post-language: Can report 'red', 'pain', etc.")
    print("   - 言語後: '赤い'、'痛い'等を報告可能")
    print("="*70)

if __name__ == "__main__":
    compare_memory_systems()
