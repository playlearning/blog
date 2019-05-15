import os
from pathlib import Path
import requests

import argparse
from dateutil.parser import parse
from ruamel.yaml import YAML
from tqdm import tqdm


def get_name(url, title=None):
    name = url.split('/')[-1]
    if title:
        suffix = name.split('.')[-1]
        title.replace(':', ' -')
        name = '.'.join([title, suffix])
    return name


def download_list(papers, folder='.'):
    for paper in papers:
        if type(paper) is dict:
            title = paper['title']
            url = paper['link']
        elif type(paper) in [tuple, list]:
            title, url = paper
        else:
            raise NotImplementedError(
                "'{}' is not allowed.".format(type(papers)))
        download(url, folder, title=title)

def download(url, folder='.', title=None):
    folder = Path(folder).expanduser()
    folder.mkdir(parents=True, exist_ok=True)

    file_name = get_name(url, title)
    dst = folder.joinpath(file_name)
    try:
        download_from_url(url, str(dst))
    except Exception as e:
        print('Failed to download `{}`: \n{}'.format(file_name, str(e)))
        print('\t`{}`.'.format(url))


def download_yaml(path, folder='.'):
    yaml = YAML()
    info = yaml.load(Path(path))
    papers = info['papers']
    plist = []
    for paper in papers:
        link = paper['link']
        if link:
            head = []
            head.append(str(parse(str(paper['date'])).year))
            if 'abbr' in paper:
                head.append(paper['abbr'])
            title = '[{}] {}'.format(','.join(head), paper['title'])
            plist.append((title, link))
    download_list(plist, folder)


# https://gist.github.com/wy193777/0e2a4932e81afc6aa4c8f7a2984f34e2
def download_from_url(url, dst):
    """
    @param: url to download file
    @param: dst place to put the file
    """
    filename = Path(dst).name
    max_len = 30
    info = (filename[:max_len] + '..') if len(filename) > max_len else filename

    headers = requests.head(url).headers
    if "Content-Length" in headers:
        file_size = int(headers["Content-Length"])
        first_byte = os.path.getsize(dst) if os.path.exists(dst) else 0
        if first_byte >= file_size:
            return file_size

        header = {"Range": "bytes=%s-%s" % (first_byte, file_size)}
        pbar = tqdm(
            total=file_size, initial=first_byte, ncols=0,
            unit='B', unit_scale=True, desc=info)
        req = requests.get(url, headers=header, stream=True)
        with(open(dst, 'ab')) as f:
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    pbar.update(1024)
        pbar.close()
    else:
        print(info)
        req = requests.get(url, stream=True)
        with(open(dst, 'wb')) as f:
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('yaml', help='YAML file path.')
    parser.add_argument('-s', '--save', default='.', help='Saving location.')

    args = parser.parse_args()
    download_yaml(args.yaml, args.save)
