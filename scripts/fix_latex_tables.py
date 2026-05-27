"""Fix LaTeX longtable issues in nbconvert output."""
import sys

tex_file = sys.argv[1]

with open(tex_file, 'r', encoding='utf-8') as f:
    tex = f.read()

# Remove \real{...} which causes "no counter 'none'" error
while r'\real{' in tex:
    start = tex.index(r'\real{')
    # find matching }
    depth = 0
    i = start + 5  # after \real
    while i < len(tex):
        if tex[i] == '{':
            depth += 1
        elif tex[i] == '}':
            if depth == 0:
                tex = tex[:start] + tex[i + 1:]
                break
            depth -= 1
        i += 1
    else:
        break

with open(tex_file, 'w', encoding='utf-8') as f:
    f.write(tex)

print(f"Fixed LaTeX tables in {tex_file}")
