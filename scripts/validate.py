#!/usr/bin/env python3
"""Validate required framework files and internal Markdown links (stdlib only)."""
import pathlib, re, sys
root = pathlib.Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
required = ['INSTALL.md','skills/interaction/SKILL.md','PROJECT_MODE.md','AGENTS.md','README.md','skills/discovery/SKILL.md','skills/implementation/SKILL.md','skills/quality/SKILL.md','skills/continuity/SKILL.md','templates/README.md','templates/AGENTS.md','templates/project/requirements.md','templates/project/decisions.md','templates/project/state.md','templates/project/tasks.md','templates/project/acceptance.md']
errors=[]
for rel in required:
    if not (root/rel).is_file(): errors.append('Missing: '+rel)
for md in root.rglob('*.md'):
    for link in re.findall(r'\]\(([^)]+)\)', md.read_text(encoding='utf-8')):
        if link.startswith(('http:', 'https:', '#', 'mailto:', '{{')): continue
        dest=(md.parent/link.split('#')[0]).resolve()
        if not dest.is_relative_to(root) or not dest.exists(): errors.append(f'Broken link: {md.relative_to(root)} -> {link}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'PASS: {len(required)} required files and local Markdown links validated')
