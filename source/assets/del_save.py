# -*- coding: utf-8 -*-
import os
import shutil

target_dir = os.path.join(os.environ['LOCALAPPDATA'], 'Sisyphe.io')

shutil.rmtree(target_dir)