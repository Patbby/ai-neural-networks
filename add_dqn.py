#!/usr/bin/env python3
import re

# Read the current index.html
with open('/root/.openclaw/workspace/ai-neural-networks/index.html', 'r') as f:
    content = f.read()

# The DQN card HTML
dqn_card = '''            <!-- DQN Paper Card -->
            <div class="network-card" onclick="location.href='papers/dqn.html'">
                <span class="tag">Nature 2015</span>
                <h3>DQN · Deep Q-Networks</h3>
                <p>Human-level Control Through Deep Reinforcement Learning - Combining deep learning with RL to master Atari games from raw pixels.</p>
                <svg class="preview-svg" viewBox="0 0 300 150">
                    <defs>
                        <linearGradient id="dqn-grad" x1="0%" y1="0%" x2="100%" y2="0%">
                            <stop offset="0%" style="stop-color:#6366f1"/>
                            <stop offset="100%" style="stop-color:#ec4899"/>
                        </linearGradient>
                    </defs>
                    <!-- Game Frame -->
                    <rect x="20" y="50" width="45" height="45" fill="none" stroke="#6366f1" stroke-width="2" rx="3"/>
                    <text x="42" y="78" fill="#fff" font-size="9" text-anchor="middle">Atari</text>
                    <!-- CNN -->
                    <rect x="75" y="45" width="50" height="55" fill="rgba(99,102,241,0.3)" stroke="#6366f1" stroke-width="2" rx="3"/>
                    <text x="100" y="65" fill="#fff" font-size="9" text-anchor="middle">CNN</text>
                    <text x="100" y="80" fill="#c7d2fe" font-size="7" text-anchor="middle">Q-Network</text>
                    <!-- Q-Values -->
                    <rect x="140" y="40" width="50" height="20" fill="rgba(236,72,153,0.3)" stroke="#ec4899" stroke-width="1.5" rx="2"/>
                    <text x="165" y="53" fill="#fff" font-size="6" text-anchor="middle">Q(s,↑)</text>
                    <rect x="140" y="65" width="50" height="20" fill="rgba(236,72,153,0.5)" stroke="#ec4899" stroke-width="2" rx="2"/>
                    <text x="165" y="78" fill="#fff" font-size="6" text-anchor="middle">Q(s,↓)</text>
                    <rect x="140" y="90" width="50" height="20" fill="rgba(236,72,153,0.3)" stroke="#ec4899" stroke-width="1.5" rx="2"/>
                    <text x="165" y="103" fill="#fff" font-size="6" text-anchor="middle">Q(s,→)</text>
                    <!-- Action -->
                    <rect x="210" y="60" width="70" height="30" fill="rgba(16,185,129,0.2)" stroke="#10b981" stroke-width="2" rx="3"/>
                    <text x="245" y="80" fill="#6ee7b7" font-size="10" text-anchor="middle">Action</text>
                    <!-- Arrows -->
                    <path d="M65 72 L75 72" stroke="#6366f1" stroke-width="2"/>
                    <path d="M125 72 L140 72" stroke="#6366f1" stroke-width="2"/>
                    <path d="M190 75 L210 75" stroke="#ec4899" stroke-width="2"/>
                </svg>
            </div>

'''

# Find and insert before the "More Papers Coming" section
pattern = r'(            <!-- More Papers Coming -->)'
replacement = dqn_card + r'\1'

new_content = re.sub(pattern, replacement, content)

# Write the updated content
with open('/root/.openclaw/workspace/ai-neural-networks/index.html', 'w') as f:
    f.write(new_content)

print("DQN card added successfully!")
