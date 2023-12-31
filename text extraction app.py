# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 14:16:14 2023

@author: Lenovo
"""

import paddleocr
import streamlit as st
import numpy as np
ocr = paddleocr.OCR()
def main():
    st.title("Store Bill Text Extraction")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])

    if uploaded_file is not None:
        # Read image from the uploaded file
        image = paddleocr.get_image(uploaded_file)

        # Perform OCR on the image
        result = ocr.ocr(image, use_gpu=False)

        # Display extracted text
        for line in result:
            st.write(line[1])

if __name__ == "__main__":
    main()
