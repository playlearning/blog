# Download papers

The following steps download `papers` in a YAML file.

1. Save python script [downloader.py](https://raw.githubusercontent.com/playlearning/blog/master/.vuepress/public/yaml/papers/downloader.py)
2. Save YAML file. (eg. [rl_task.yaml](https://raw.githubusercontent.com/playlearning/blog/master/.vuepress/public/yaml/papers/rl_task.yaml))
3. Run `python downloader.py rl_task.yaml -s <some folder>` to download papers.

(Notice: Downloading will resume from break point if you interrupted before.)
