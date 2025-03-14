import streamlit as st
from dotenv import load_dotenv
import os
import openai
from diffusers import StableDiffusionPipeline
import torch

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_images_using_openai(text):
    response = openai.Image.create(prompt=text, n=1, size="512x512")
    image_url = response['data'][0]['url']
    return image_url


def generate_images_using_huggingface_diffusers(text):
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    prompt = text
    image = pipe(prompt).images[0]
    return image


choice = st.sidebar.selectbox("Select your choice", ["Home", "DALL-E", "HuggingFace Diffusers"])
if choice == "Home":
    st.title("AI Image generation app")
    with st.expander("About the app"):
        st.write("This is a simple image generation app that uses AI to generates images from text prompt.")

elif choice == "DALL-E":
    st.subheader("Image generation using open AI'S DALLE")
    input_prompt = st.text_input("Enter your text prompt")
    if input_prompt is not None:
        if st.button("Generate image"):
            image_url = generate_images_using_openai(input_prompt)
            st.image(image_url,caption = "Generated by DALL-E")
elif choice == "Huggingface Diffusers":
    st.subheader("Image generation using Huggingface Diffusers")
    input_prompt = st.text_input("Enter your text prompt")
    if input_prompt is not None:
        if st.button("Generate image"):
            image_output = generate_images_using_huggingface_diffusers(input_prompt)
            st.info("Generating image")
            st.success("Image generated successfully")
            st.image(image_output,caption = "Generated by HuggingFace Diffusers")



