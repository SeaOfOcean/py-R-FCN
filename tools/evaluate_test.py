import _init_paths
from datasets.pascal_voc import pascal_voc
from datasets.factory import get_imdb

imdb = pascal_voc('test', '2007')
imdb._do_python_eval('results')
