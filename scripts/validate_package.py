#!/usr/bin/env python3
"""Check basic skill metadata and relative Markdown links; no external dependencies."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote

root = Path(__file__).resolve().parent.parent
expected = ('delivery-first', 'ai-development-workflow', 'multi-agent-dev-sop')
errors = []
for name in expected:
    file = root / 'skills' / name / 'SKILL.md'
    if not file.is_file():
        errors.append(f'missing {file.relative_to(root)}')
        continue
    content = file.read_text(encoding='utf-8')
    match = re.match(r'\A---\s*\n(.*?)\n---\s*\n', content, re.S)
    if not match or not re.search(r'^name:\s*' + re.escape(name) + r'\s*$', match.group(1), re.M) or not re.search(r'^description:\s*\S', match.group(1), re.M):
        errors.append(f'invalid metadata: {file.relative_to(root)}')
for file in root.rglob('*.md'):
    text = file.read_text(encoding='utf-8')
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if target.startswith(('http:', 'https:', '#', 'mailto:')):
            continue
        path = unquote(target.split('#', 1)[0])
        if path and not (file.parent / path).exists():
            errors.append(f'broken link in {file.relative_to(root)}: {target}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('OK: three skill metadata blocks and local Markdown links')
