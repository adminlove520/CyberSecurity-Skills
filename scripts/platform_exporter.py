import os
import json
import re

def parse_simple_yaml(yaml_str):
    data = {}
    for line in yaml_str.split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            data[key.strip()] = val.strip().strip('"').strip("'")
    return data

def parse_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if match:
        frontmatter = parse_simple_yaml(match.group(1))
        body = match.group(2)
        return frontmatter, body
    return None, content

def generate_openclaw_manifests(skill_library_path, output_path):
    # Create OpenClaw specific files
    soul_content = "# Security Expert Soul\n\nYou are a professional Cyber Security Specialist and Pen-tester..."
    agents_content = "# Security Capabilities\n\n"
    identity_content = "# Security Agent Identity\n\nThis agent is equipped with a comprehensive Cyber Security Skill library."

    for root, dirs, files in os.walk(skill_library_path):
        if 'skills' in dirs:
            skill_dir = os.path.join(root, 'skills')
            for f in os.listdir(skill_dir):
                if f.endswith('.md'):
                    meta, body = parse_md_file(os.path.join(skill_dir, f))
                    if meta:
                        agents_content += f"## {meta.get('title')}\n"
                        agents_content += f"**Category**: {meta.get('category')}\n"
                        agents_content += f"**Tools**: {meta.get('tools')}\n\n"

    os.makedirs(output_path, exist_ok=True)
    with open(os.path.join(output_path, 'SOUL.md'), 'w', encoding='utf-8') as f:
        f.write(soul_content)
    with open(os.path.join(output_path, 'AGENTS.md'), 'w', encoding='utf-8') as f:
        f.write(agents_content)
    with open(os.path.join(output_path, 'IDENTITY.md'), 'w', encoding='utf-8') as f:
        f.write(identity_content)

def generate_trae_rules(skill_library_path, output_file):
    rules = "# multi-CyberSecurity Rules for Trae\n\n"
    rules += "When performing security tasks, refer to the following skill library:\n\n"
    
    for root, dirs, files in os.walk(skill_library_path):
        if 'skills' in dirs:
            skill_dir = os.path.join(root, 'skills')
            for f in os.listdir(skill_dir):
                if f.endswith('.md'):
                    meta, _ = parse_md_file(os.path.join(skill_dir, f))
                    if meta:
                        rules += f"- **{meta.get('title')}**: Path: `{os.path.relpath(os.path.join(skill_dir, f), skill_library_path)}`\n"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(rules)

if __name__ == "__main__":
    project_root = "."
    generate_openclaw_manifests(project_root, "templates/openclaw")
    generate_trae_rules(project_root, ".traerules")
    print("Exported platform-specific manifests.")
