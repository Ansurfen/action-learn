import datetime
import json
import time
import hashlib
import subprocess


def zip(source_dir: str, target_file: str):
    """
    Compresses the contents of a directory using the zip command.

    :param source_dir: The directory to compress.
    :param target_file: The name of the archive file to create.
    """
    # Create the zip command with the appropriate arguments
    cmd = ['zip', '-r', '-X', target_file, source_dir]

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


def sha256(filename):
    sha256_hash = hashlib.sha256()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            sha256_hash.update(data)
    return sha256_hash.hexdigest()


def is_new_day(timestamp):
    date = datetime.datetime.fromtimestamp(timestamp).date()
    today = datetime.date.today()
    return date != today


data = {}
with open('./release.json', 'r') as fp:
    data = json.load(fp)
    fp.close()

release_ver = data["_meta"]["version"]
release_ts = data["_meta"]["timestamp"]
# 1) 当前还没运行过，赋值为当前时间
# 2) 拿上一次运行的时间戳和当前时间比较，检测是否为新的一天
if release_ts == 0 or is_new_day(release_ts):
    release_ver = 1  # 新的一天版本从1开始累加，运行的结尾release_ver会累加1代表当前day的下一个版本号
    release_ts = time.time()  # 更新时间为当前的时间
# release的tag,  date部分，格式为 2023-1-1
# 他会和 ver 拼接成  2023-1-1-v1 这种形式作为最终tag
release_tag = time.strftime(
    '%Y-%m-%d', time.localtime(release_ts)) + f'-v{release_ver}'

# 压缩包处理列表
compress = [[zip, "zip"], [tar, "tar.gz"]]

# 要release的压缩包列表
candidates = []
for name, v in data.items():
    if name == "_meta":
        continue
    brfore_hash = data[name]["sha256"]
    after_hash = ""
    for idx, cmp in enumerate(compress):
        cmp[0]("./" + name, f'{name}.{cmp[1]}')
        if after_hash == "":
            after_hash = sha256(f'{name}.{cmp[1]}')
        # 通过哈希值比较确认压缩包是否要更新
        # 不同则加入候选列表，等待release
        if brfore_hash != after_hash:
            candidates.append(f'{name}.{cmp[1]}')
            # 添加到候选列表里就更新哈希，以第一个为准
            print(name, idx, after_hash)
            if idx == 0:
                data[name]["sha256"] = after_hash
                # tag 用来给客户端记录，同步版本用的
                data[name]["tag"] = release_tag
        else:
            break

subprocess.run(['gh', 'release', 'create', release_tag] +
               candidates, check=True)
# 更新_meta
release_ver += 1  # 当前day的下一个版本号
data["_meta"]["version"] = release_ver
data["_meta"]["timestamp"] = release_ts

with open('./release.json', 'w+') as fp:
    json.dump(data, fp, indent=4)
    fp.close()
