import streamlit as st
import os
from generator import NFTGenerator
from pathlib import Path

if 'gogo' not in st.session_state:
    print('init gogo')
    st.session_state.gogo = False

with st.sidebar:
    input_dir = st.text_input('input dir')
    is_animate = st.checkbox('animate?', )
    if is_animate:
        fps = st.number_input('fps', 1)
        n_frame = st.number_input('no. of frame', 1)

    test = st.button('test')
    st.session_state['test'] = True
    with st.form(key="generate?"):
        amount = st.number_input('amount', 1)
        output_dir = st.text_input('output dir', 'generated')
        unique = st.checkbox("unique mode")
        st.write('*unique mode will generate in order (not random)')
        submit_button = st.form_submit_button(label='go go')

if submit_button:
    print('GOGO')
    print(output_dir)
    print(amount)
    p = Path(output_dir)
    p.mkdir(parents=True, exist_ok=True)
    the_bar = st.progress(0)
    if is_animate:
        nft_generator = NFTGenerator(input_dir=input_dir, animate=is_animate, fps=fps, n_frame=n_frame, unique=unique)
        for i in range(amount):
            the_bar.progress((i + 1) / amount)
            nft_generator.generate(save_path=output_dir, file_name=i)
    else:
        nft_generator = NFTGenerator(input_dir=input_dir, unique=unique)
        for i in range(amount):
            the_bar.progress((i + 1) / amount)
            nft_generator.generate(save_path=output_dir, file_name=i)
    st.header("DONE!")
    st.subheader(f"pls check out {p.absolute()}")

if test:
    if is_animate:
        nft_generator = NFTGenerator(input_dir=input_dir, animate=is_animate, fps=fps, n_frame=n_frame, unique=unique)
        sample = nft_generator.generate()
        st.image(sample, caption=[f'frame {i + 1}' for i in range(len(sample))])
    else:
        nft_generator = NFTGenerator(input_dir=input_dir, unique=unique)
        sample = nft_generator.generate()
        st.image(sample, caption="sample")
