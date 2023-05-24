import os
import subprocess
import shutil

# 获取需要打包的目录路径
directory = os.environ.get('INPUT_DIRECTORY')
if directory is None:
    raise ValueError('Missing required input parameter: directory')

# 获取 release 版本号
version = os.environ.get('INPUT_VERSION')
if version is None:
    raise ValueError('Missing required input parameter: version')

# 创建临时目录
temp_dir = 'temp'
os.makedirs(temp_dir)

# 复制需要打包的文件到临时目录中
for item in os.listdir(directory):
    item_path = os.path.join(directory, item)
    if os.path.isfile(item_path):
        shutil.copy2(item_path, temp_dir)

# 打包临时目录
subprocess.run(['tar', '-czf', f'{version}.tar.gz', temp_dir])

# 发布 Release
subprocess.run(['gh', 'release', 'create', f'v{version}', f'{version}.tar.gz'], check=True)
