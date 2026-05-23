import os
import re
import json

def build_skill_graph(root_dir):
    graph = {
        "mitre_attack_mapping": {},
        "categories": {},
        "skills": []
    }
    
    for root, dirs, files in os.walk(root_dir):
        if 'skills' in dirs:
            skill_dir = os.path.join(root, 'skills')
            for f in os.listdir(skill_dir):
                if f.endswith('.md'):
                    file_path = os.path.join(skill_dir, f)
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        
                        # Extract metadata
                        match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
                        if match:
                            meta_str = match.group(1)
                            meta = {}
                            for line in meta_str.split('\n'):
                                if ':' in line:
                                    k, v = line.split(':', 1)
                                    meta[k.strip()] = v.strip().strip('"').strip("'")
                            
                            skill_id = meta.get('id')
                            title = meta.get('title')
                            
                            # Map MITRE ATT&CK
                            mitre = meta.get('mitre_attack', '[]')
                            # Clean up the string representation of list
                            mitre_ids = [id.strip().strip("'").strip('"') for id in mitre.strip('[]').split(',') if id.strip()]
                            
                            skill_entry = {
                                "id": skill_id,
                                "title": title,
                                "path": file_path,
                                "mitre_attack": mitre_ids
                            }
                            graph["skills"].append(skill_entry)
                            
                            for m_id in mitre_ids:
                                if m_id not in graph["mitre_attack_mapping"]:
                                    graph["mitre_attack_mapping"][m_id] = []
                                graph["mitre_attack_mapping"][m_id].append(skill_id)
                                
    return graph

if __name__ == "__main__":
    skill_graph = build_skill_graph(".")
    with open("framework/skill_graph.json", "w", encoding="utf-8") as f:
        json.dump(skill_graph, f, indent=2, ensure_ascii=False)
    print("Generated semantic skill graph at framework/skill_graph.json")
