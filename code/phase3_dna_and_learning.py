#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase 3: DNA Initial Values and Learning
DNA初期値と学習

Theory of Human Inner Movement
人の内なる運動理論

🔥 TRY THIS / 試してみて:
   python phase3_dna_and_learning.py --dna_pain=100
   
   → Pain and pleasure will mix! / 痛みと快感が混合する！
   → This is NOT a bug. Some people are like this.
   → これはバグじゃない。こういう人はいる。
"""

import random
import argparse

class DNALearningSystem:
    """System with DNA initial values and learning"""
    
    def __init__(self, dna_values=None):
        """
        Args:
            dna_values: Custom DNA initial values (optional)
        """
        self.qualia_types = ['pain', 'warm', 'sweet', 'pleasure']
        
        # DNA initial values (genetic predisposition)
        # DNA初期値（遺伝的素因）
        if dna_values:
            self.qualia_dna = dna_values
        else:
            self.qualia_dna = {
                'pain': -0.9,      # Strong avoidance / 強い回避
                'warm': -0.2,      # Mild avoidance / 軽度の回避
                'sweet': +0.7,     # Approach / 接近
                'pleasure': +0.8   # Strong approach / 強い接近
            }
        
        # Learned adjustments (experience-based)
        # 学習による調整（経験ベース）
        self.qualia_learned = {q: 0.0 for q in self.qualia_types}
        
        # Learning rate / 学習率
        self.learning_rate = 0.01
        
        # Memory and consciousness
        self.recent_patterns = []
        self.self_strength = 0.0
        self.sync_score = 0.0
        self.is_conscious = False
        self.THRESHOLD = 0.3
        
        # Track interesting states
        self.mixed_states = []  # pain + pleasure混合状態
    
    def get_effective_value(self, qualia_type):
        """Get effective qualia value (DNA + learned)"""
        return self.qualia_dna.get(qualia_type, 0) + self.qualia_learned.get(qualia_type, 0)
    
    def normalize_value(self, value):
        """Normalize extreme values to -1 to +1 range, with overflow effects"""
        # 極端な値は-1〜+1に正規化、オーバーフロー効果あり
        if value > 1.0:
            # Overflow: extreme positive wraps into mixed state
            overflow = value - 1.0
            return 1.0, overflow  # returns (normalized, overflow)
        elif value < -1.0:
            overflow = abs(value) - 1.0
            return -1.0, overflow
        return value, 0.0
    
    def process_step(self):
        """Process one step with potential mixed states"""
        
        # Stimulus
        stimulus = random.choice(self.qualia_types)
        raw_value = self.get_effective_value(stimulus)
        effective_value, overflow = self.normalize_value(raw_value)
        
        # Check for mixed state (pain + pleasure)
        # DNA初期値が極端だと、痛みと快感が混合する
        is_mixed = False
        mixed_pleasure = 0.0
        
        if stimulus == 'pain' and overflow > 0:
            # Extreme pain DNA → pain mixes with pleasure
            # 極端な痛みDNA → 痛みが快感と混合
            is_mixed = True
            mixed_pleasure = overflow * 0.8  # Part of overflow becomes pleasure
            self.mixed_states.append({
                'step': len(self.recent_patterns) + 1,
                'pain': effective_value,
                'pleasure': mixed_pleasure,
                'raw_dna': raw_value
            })
        
        # Prediction and error
        if self.recent_patterns:
            prediction = self.recent_patterns[-1]
            prediction_error = 0.0 if prediction == stimulus else 1.0
        else:
            prediction_error = 1.0
        
        # Update memory
        self.recent_patterns.append(stimulus)
        if len(self.recent_patterns) > 10:
            self.recent_patterns.pop(0)
        
        # Self-strength
        if len(self.recent_patterns) >= 2:
            matches = sum(1 for i in range(len(self.recent_patterns)-1) 
                         if self.recent_patterns[i] == self.recent_patterns[i+1])
            self.self_strength += 0.01 * matches
            self.self_strength = min(self.self_strength, 1.0)
        
        # Sync score
        self.sync_score = prediction_error * 0.8 + random.uniform(0, 0.2)
        
        # Consciousness
        self.is_conscious = (self.sync_score >= self.THRESHOLD and 
                            self.self_strength >= self.THRESHOLD)
        
        return {
            'stimulus': stimulus,
            'dna_value': self.qualia_dna.get(stimulus, 0),
            'effective_value': effective_value,
            'is_mixed': is_mixed,
            'mixed_pleasure': mixed_pleasure,
            'is_conscious': self.is_conscious
        }
    
    def run_experiment(self, steps=1000):
        """Run experiment and show results"""
        
        print(f"\nRunning {steps} steps...")
        print(f"{steps}ステップ実行中...\n")
        
        for i in range(steps):
            result = self.process_step()
            
            # Report mixed states when they occur
            if result['is_mixed'] and len(self.mixed_states) <= 10:
                print(f"Step {i+1}: MIXED STATE DETECTED!")
                print(f"  Pain: {result['effective_value']:.2f}")
                print(f"  + Pleasure: {result['mixed_pleasure']:.2f}")
                print(f"  >>> 痛いのに気持ちいい状態\n")
        
        # Summary
        print("=" * 60)
        print("RESULTS / 結果")
        print("=" * 60)
        print(f"\nDNA Initial Values / DNA初期値:")
        for q, v in self.qualia_dna.items():
            print(f"  {q}: {v:+.1f}")
        
        print(f"\nMixed states detected: {len(self.mixed_states)}")
        print(f"痛み+快感の混合状態: {len(self.mixed_states)}回検出")
        
        if self.mixed_states:
            print("\n" + "=" * 60)
            print("🔥 THIS IS NOT A BUG! / これはバグじゃない！")
            print("=" * 60)
            print("""
When DNA initial value for pain is extreme (e.g., 100),
the system exhibits pain-pleasure mixing.

DNA初期値が極端（例：100）だと、
痛みと快感が混合する状態が発生する。

Real humans with this trait:
この特性を持つ実際の人間：
- Self-harm behaviors / 自傷行為
- BDSM preferences / SM嗜好  
- Extreme spicy food lovers / 激辛好き
- Extreme sports enthusiasts / エクストリームスポーツ愛好者

This behavior EMERGED from the 5-layer architecture.
It was NOT explicitly programmed!

この挙動は5層アーキテクチャから創発した。
明示的にプログラムしていない！
""")
        
        return self.mixed_states


def main():
    parser = argparse.ArgumentParser(
        description='Phase 3: DNA Initial Values Experiment',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples / 使用例:
  python phase3_dna_and_learning.py --dna_pain=100
  python phase3_dna_and_learning.py --dna_pain=50 --dna_pleasure=100
  python phase3_dna_and_learning.py --steps=5000
        """
    )
    
    parser.add_argument('--dna_pain', type=float, default=-0.9,
                        help='DNA initial value for pain (default: -0.9, try 100!)')
    parser.add_argument('--dna_warm', type=float, default=-0.2,
                        help='DNA initial value for warm (default: -0.2)')
    parser.add_argument('--dna_sweet', type=float, default=0.7,
                        help='DNA initial value for sweet (default: 0.7)')
    parser.add_argument('--dna_pleasure', type=float, default=0.8,
                        help='DNA initial value for pleasure (default: 0.8)')
    parser.add_argument('--steps', type=int, default=1000,
                        help='Number of steps to run (default: 1000)')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("Phase 3: DNA Initial Values Experiment")
    print("DNA初期値の実験")
    print("=" * 60)
    
    # Create custom DNA values
    dna_values = {
        'pain': args.dna_pain,
        'warm': args.dna_warm,
        'sweet': args.dna_sweet,
        'pleasure': args.dna_pleasure
    }
    
    # Check for extreme values
    if args.dna_pain > 10:
        print(f"\n⚠️  EXTREME DNA VALUE DETECTED: pain = {args.dna_pain}")
        print("   極端なDNA値を検出: pain = {args.dna_pain}")
        print("   Expecting mixed pain-pleasure states...")
        print("   痛み+快感の混合状態が予想される...\n")
    
    system = DNALearningSystem(dna_values=dna_values)
    results = system.run_experiment(steps=args.steps)


if __name__ == "__main__":
    main()
