#!/usr/bin/env python3
"""
Version Manager for multi-CyberSecurity
统一管理和同步项目中的所有版本号

Usage:
    python scripts/version_manager.py bump patch  # 1.2.3 -> 1.2.4
    python scripts/version_manager.py bump minor  # 1.2.3 -> 1.3.0
    python scripts/version_manager.py bump major  # 1.2.3 -> 2.0.0
    python scripts/version_manager.py set 4.2.0   # 设置指定版本
    python scripts/version_manager.py check       # 检查版本一致性
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple

# 项目根目录
PROJECT_ROOT = Path(__file__).parent.parent

# 需要更新的文件列表
VERSION_FILES = [
    ("README.md", [
        (r"multi-CyberSecurity v[\d.]+", "multi-CyberSecurity v{version}"),
        (r"version-[\d.]+-", "version-{version}-"),
    ]),
    ("cli.py", [
        (r"multi-CyberSecurity v[\d.]+(?: Enhanced)?", "multi-CyberSecurity v{version} Enhanced"),
        (r"multi-CyberSecurity v[\d.]+ - AI", "multi-CyberSecurity v{version} - AI"),
    ]),
    ("framework/skills/index.md", [
        (r"Framework Version: v[\d.]+", "Framework Version: v{version}"),
    ]),
]


def get_current_version() -> str:
    """从 README.md 获取当前版本号"""
    readme_path = PROJECT_ROOT / "README.md"
    content = readme_path.read_text(encoding="utf-8")
    
    # 匹配标题中的版本号
    match = re.search(r"multi-CyberSecurity v([\d.]+)", content)
    if match:
        return match.group(1)
    
    # 匹配 badge 中的版本号
    match = re.search(r"version-([\d.]+)-", content)
    if match:
        return match.group(1)
    
    raise ValueError("Could not find current version in README.md")


def bump_version(version: str, bump_type: str) -> str:
    """递增版本号"""
    parts = version.split(".")
    
    # 确保有3个部分
    while len(parts) < 3:
        parts.append("0")
    
    major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])
    
    if bump_type == "major":
        return f"{major + 1}.0.0"
    elif bump_type == "minor":
        return f"{major}.{minor + 1}.0"
    elif bump_type == "patch":
        return f"{major}.{minor}.{patch + 1}"
    else:
        raise ValueError(f"Unknown bump type: {bump_type}")


def update_file(filepath: Path, patterns: List[Tuple[str, str]], version: str) -> bool:
    """更新单个文件中的版本号"""
    if not filepath.exists():
        print(f"Warning: {filepath} not found")
        return False
    
    content = filepath.read_text(encoding="utf-8")
    original_content = content
    
    for pattern, replacement_template in patterns:
        replacement = replacement_template.format(version=version)
        content = re.sub(pattern, replacement, content)
    
    if content != original_content:
        filepath.write_text(content, encoding="utf-8")
        print(f"Updated: {filepath}")
        return True
    else:
        print(f"No changes: {filepath}")
        return False


def update_version(new_version: str) -> None:
    """更新所有文件中的版本号"""
    print(f"Updating version to v{new_version}...")
    print("-" * 50)
    
    updated = False
    for relative_path, patterns in VERSION_FILES:
        filepath = PROJECT_ROOT / relative_path
        if update_file(filepath, patterns, new_version):
            updated = True
    
    print("-" * 50)
    if updated:
        print(f"✅ Version updated to v{new_version}")
        print("\nNext steps:")
        print(f"  1. Review the changes: git diff")
        print(f"  2. Commit: git commit -am 'chore: bump version to v{new_version}'")
        print(f"  3. Tag: git tag -a v{new_version} -m 'Release v{new_version}'")
        print(f"  4. Push: git push origin main && git push origin v{new_version}")
    else:
        print("ℹ️ No files were updated")


def check_version_consistency() -> bool:
    """检查所有文件中的版本号是否一致"""
    print("Checking version consistency...")
    print("-" * 50)
    
    versions = {}
    
    for relative_path, patterns in VERSION_FILES:
        filepath = PROJECT_ROOT / relative_path
        if not filepath.exists():
            continue
        
        content = filepath.read_text(encoding="utf-8")
        
        for pattern, _ in patterns:
            matches = re.findall(pattern, content)
            if matches:
                # 提取版本号
                version_match = re.search(r"v?([\d.]+)", matches[0])
                if version_match:
                    versions[relative_path] = version_match.group(1)
                    break
    
    # 检查一致性
    unique_versions = set(versions.values())
    
    for filepath, version in versions.items():
        print(f"  {filepath}: v{version}")
    
    print("-" * 50)
    
    if len(unique_versions) == 1:
        print(f"✅ All files are consistent at v{list(unique_versions)[0]}")
        return True
    else:
        print(f"❌ Version inconsistency detected!")
        print(f"   Found versions: {', '.join(sorted(unique_versions))}")
        return False


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "bump":
        if len(sys.argv) < 3:
            print("Error: bump type required (patch/minor/major)")
            sys.exit(1)
        
        bump_type = sys.argv[2]
        current = get_current_version()
        new_version = bump_version(current, bump_type)
        update_version(new_version)
    
    elif command == "set":
        if len(sys.argv) < 3:
            print("Error: version required (e.g., 4.2.0)")
            sys.exit(1)
        
        new_version = sys.argv[2]
        update_version(new_version)
    
    elif command == "check":
        consistent = check_version_consistency()
        sys.exit(0 if consistent else 1)
    
    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
