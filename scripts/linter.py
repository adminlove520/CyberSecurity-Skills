import os
import re

def lint_skill_files(root_dir):
    errors = []
    required_fields = ['id', 'title', 'category', 'difficulty']
    
    for root, dirs, files in os.walk(root_dir):
        if 'skills' in dirs:
            skill_dir = os.path.join(root, 'skills')
            for f in os.listdir(skill_dir):
                if f.endswith('.md'):
                    file_path = os.path.join(skill_dir, f)
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        
                        # Check Frontmatter
                        match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
                        if not match:
                            errors.append(f"Missing Frontmatter: {file_path}")
                            continue
                        
                        frontmatter = match.group(1)
                        for field in required_fields:
                            if f"{field}:" not in frontmatter:
                                errors.append(f"Missing required field '{field}' in {file_path}")
                                
    return errors

if __name__ == "__main__":
    results = lint_skill_files(".")
    if results:
        print("Linter Errors Found:")
        for err in results:
            print(f"- {err}")
    else:
        print("All skill files passed validation.")
