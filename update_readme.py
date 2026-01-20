import re
import requests
import os
import time
from datetime import datetime

# GitHub API Token (optional but recommended for rate limits)
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'User-Agent': 'Mozilla/5.0 (compatible; AutoUpdateScript/1.0)'
} if GITHUB_TOKEN else {
    'User-Agent': 'Mozilla/5.0 (compatible; AutoUpdateScript/1.0)'
}

def get_last_update_time(repo_url):
    """
    获取 GitHub 仓库的最后更新时间 (pushed_at)
    """
    # 提取 owner 和 repo
    match = re.search(r'github\.com/([^/]+)/([^/]+)', repo_url)
    if not match:
        return None
    
    owner, repo = match.groups()
    if repo.endswith('.git'):
        repo = repo[:-4]
    
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    print(f"Requesting: {api_url}")
    
    try:
        response = requests.get(api_url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            data = response.json()
            pushed_at = data.get('pushed_at')
            if pushed_at:
                # 格式化时间为 YYYY-MM-DD
                dt = datetime.strptime(pushed_at, "%Y-%m-%dT%H:%M:%SZ")
                return dt.strftime("%Y-%m-%d")
        elif response.status_code == 403:
            print(f"Rate limit exceeded or forbidden for {repo_url}")
        elif response.status_code == 404:
            print(f"Repo not found: {repo_url}")
    except Exception as e:
        print(f"Error fetching {repo_url}: {e}")
    
    return None

def update_readme(file_path):
    """
    读取并更新 README.md 文件
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    # 用于识别表格列的索引
    url_col_index = -1
    last_update_col_index = -1
    in_table = False
    header_processed = False
    

    # 正则表达式匹配 Markdown 表格行
    table_row_pattern = re.compile(r'^\s*\|.*\|\s*$')
    
    current_table_rows = [] # 存储当前表格的数据行 (parts)
    current_table_header = None # 存储表头行
    current_table_separator = None # 存储分隔行
    
    for i, line in enumerate(lines):
        stripped_line = line.strip()
        
        # 检查是否是表格行
        if table_row_pattern.match(stripped_line):
            parts = [p.strip() for p in stripped_line.split('|')]
            if len(parts) >= 2 and parts[0] == '': parts.pop(0)
            if len(parts) >= 1 and parts[-1] == '': parts.pop(-1)
            
            # 1. 处理表头
            if not in_table:
                in_table = True
                # 检查是否存在“项目地址”列
                try:
                    url_col_index = -1
                    for idx, col in enumerate(parts):
                        if '项目地址' in col or 'Address' in col or 'URL' in col:
                            url_col_index = idx
                            break
                    
                    if url_col_index != -1:
                        last_update_col_index = -1
                        for idx, col in enumerate(parts):
                            if '最近更新' in col or 'Last Updated' in col:
                                last_update_col_index = idx
                                break
                        
                        if last_update_col_index == -1:
                            parts.append('最近更新')
                            last_update_col_index = len(parts) - 1
                            
                        current_table_header = parts
                        header_processed = True
                        continue # 表头暂不写入，等表格处理完
                except ValueError:
                    pass
            
            # 2. 处理分隔行
            if '---' in stripped_line:
                if header_processed and current_table_header:
                     # 确保分隔行长度与表头一致
                    while len(parts) < len(current_table_header):
                         parts.append('---')
                    current_table_separator = parts
                elif not header_processed:
                    # 如果不是我们要处理的表头（没找到项目地址列），直接写入之前的缓存（如果有）和当前行
                    new_lines.append(line) 
                continue

            # 3. 处理数据行
            if url_col_index != -1 and header_processed:
                # 提取并更新数据
                if len(parts) > url_col_index:
                    cell_content = parts[url_col_index]
                    url_match = re.search(r'https://github\.com/[a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+', cell_content)
                    
                    if url_match:
                        repo_url = url_match.group(0)
                        # print(f"Checking {repo_url}...") 
                        # 暂时注释掉打印以减少干扰，或者保留
                        
                        update_time = get_last_update_time(repo_url)
                        
                        if update_time:
                            if last_update_col_index >= len(parts):
                                parts.append(update_time)
                            else:
                                parts[last_update_col_index] = update_time
                            
                            if not GITHUB_TOKEN:
                                time.sleep(1)
                        else:
                             if last_update_col_index >= len(parts):
                                parts.append('-')
                    else:
                        if last_update_col_index >= len(parts):
                            parts.append('-')
                else:
                    # 数据行格式不对，补齐
                     while len(parts) <= last_update_col_index:
                        parts.append('-')
                
                current_table_rows.append(parts)
            else:
                # 不是我们要处理的表格的数据行，直接写入
                new_lines.append(line)
            
        else:
            # 表格结束（遇到空行或非表格行）
            if in_table and header_processed and current_table_header:
                # 1. 写入表头
                new_lines.append('| ' + ' | '.join(current_table_header) + ' |\n')
                # 2. 写入分隔行
                if current_table_separator:
                     new_lines.append('| ' + ' | '.join(current_table_separator) + ' |\n')
                
                # 3. 排序数据行
                # last_update_col_index 是日期列索引
                # 日期格式为 YYYY-MM-DD，可以直接字符串排序
                # 倒序排列：最新的在前面
                # 注意处理 '-' 或空值，放在最后
                def sort_key(row):
                    if last_update_col_index < len(row):
                        val = row[last_update_col_index]
                        if re.match(r'\d{4}-\d{2}-\d{2}', val):
                            return val
                    return '0000-00-00' # 无效日期排在最后
                
                current_table_rows.sort(key=sort_key, reverse=True)
                
                # 4. 写入数据行
                for row in current_table_rows:
                    new_lines.append('| ' + ' | '.join(row) + ' |\n')
            
            # 重置表格状态
            in_table = False
            header_processed = False
            url_col_index = -1
            last_update_col_index = -1
            current_table_rows = []
            current_table_header = None
            current_table_separator = None
            
            new_lines.append(line)

    # 文件末尾如果还在表格中（虽然不太可能，通常最后会有换行，但以防万一）
    if in_table and header_processed and current_table_header:
         new_lines.append('| ' + ' | '.join(current_table_header) + ' |\n')
         if current_table_separator:
             new_lines.append('| ' + ' | '.join(current_table_separator) + ' |\n')
         
         def sort_key(row):
            if last_update_col_index < len(row):
                val = row[last_update_col_index]
                if re.match(r'\d{4}-\d{2}-\d{2}', val):
                    return val
            return '0000-00-00'
         current_table_rows.sort(key=sort_key, reverse=True)
         for row in current_table_rows:
            new_lines.append('| ' + ' | '.join(row) + ' |\n')

    # 写入文件

    # 写入文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("README.md updated successfully.")

if __name__ == "__main__":
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    update_readme(readme_path)
