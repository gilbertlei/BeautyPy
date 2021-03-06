#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.image as mpimg

def emboss(input_path, output_path):

    '''
    This function embosses the original image and saves the embossed image to path.

    Parameters
    ---------------------------------------
    input_path -> the file path for the original image we want to compress
    output_path ->  the file path to save the compressed image

    Return
    ---------------------------------------
    NA
    '''
    
    input_img = mpimg.imread(input_path)

    return
