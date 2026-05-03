from pathlib import Path
import re
text = Path('index.html').read_text(encoding='utf-8')
classes = re.findall(r'class="([^"]+)"|class=\'([^\']+)\'', text)
all_classes = []
for a, b in classes:
    s = a or b
    all_classes.extend(s.split())
uniq = sorted(set(all_classes))
print(len(uniq))
for c in uniq[:200]:
    print(c)
