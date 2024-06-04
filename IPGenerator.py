import random
import os
from tqdm import tqdm

def generate_ip_range(start_ip, end_ip, total_ips=None, randomize=False):
    start = list(map(int, start_ip.split('.')))
    end = list(map(int, end_ip.split('.')))
    temp = start
    ip_range = []

    while temp != end:
        ip_range.append('.'.join(map(str, temp)))
        temp[3] += 1
        for i in (3, 2, 1):
            if temp[i] == 256:
                temp[i] = 0
                temp[i-1] += 1

    ip_range.append(end_ip)

    if total_ips:
        ip_range = ip_range[:total_ips]

    if randomize:
        random.shuffle(ip_range)

    return ip_range

def generate_ips(total_ips, randomize=False):
    generated_ips = set()
    with tqdm(total=total_ips, desc="Generating IPs", ncols=100) as pbar:
        while len(generated_ips) < total_ips:
            ip = '.'.join(map(str, (random.randint(0, 255) for _ in range(4))))
            if ip not in generated_ips:
                generated_ips.add(ip)
                pbar.update(1)
    return list(generated_ips)

def save_ips_to_file(filename, ip_list):
    # Create the directory if it doesn't exist
    if not os.path.exists('Result'):
        os.makedirs('Result')
    
    file_path = os.path.join('Result', filename)
    with open(file_path, 'w') as file:
        for ip in tqdm(ip_list, desc="Saving to file", ncols=100):
            file.write(ip + '\n')
