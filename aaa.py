import os
import subprocess
import shutil
import time
import hashlib


def sha256(filename):
    # 创建一个 SHA-256 对象
    sha256_hash = hashlib.sha256()

    # 打开文件以进行二进制读取
    with open(filename, 'rb') as f:
        # 从文件中读取数据并更新散列对象
        while True:
            data = f.read(65536)
            if not data:
                break
            sha256_hash.update(data)

    # 获取散列值的十六进制表示形式
    return sha256_hash.hexdigest()


timestamp = time.time()


def zip(source_dir: str, target_file: str):
    """
    Compresses the contents of a directory using the zip command.

    :param source_dir: The directory to compress.
    :param target_file: The name of the archive file to create.
    """
    # Create the zip command with the appropriate arguments
    cmd = ['zip', '-r', target_file, source_dir]

    # Call the command using subprocess.run()
    try:
        result = subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        raise Exception(
            f"Failed to compress directory {source_dir}. Error: {e}")

    print(f"Successfully compressed directory {source_dir} into {target_file}")


def tar(source_dir: str, target_file: str):
    cmd = ['tar', '-czf', target_file, source_dir]
    try:
        result = subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        raise Exception(
            f"Failed to compress directory {source_dir}. Error: {e}")

    print(f"Successfully compressed directory {source_dir} into {target_file}")


directory = "./yock"
if directory is None:
    raise ValueError('Missing required input parameter: directory')

version = int(timestamp)
if version is None:
    raise ValueError('Missing required input parameter: version')

temp_dir = 'temp'
os.makedirs(temp_dir)

for item in os.listdir(directory):
    item_path = os.path.join(directory, item)
    if os.path.isfile(item_path):
        shutil.copy2(item_path, temp_dir)

subprocess.run(['tar', '-czf', f'{version}.tar.gz', temp_dir])
zip("./opencmd", f"{version}.zip")
subprocess.run(['gh', 'release', 'create',
               f'v{version}', f'{version}.tar.gz', f'{version}.zip'], check=True)
