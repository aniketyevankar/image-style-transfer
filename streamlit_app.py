import streamlit as st
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import PIL.Image
import io
import os

def load_image(image, max_dim=512):
    image = image.convert('RGB')
    original_size = np.array(image.size)
    scale = max_dim / max(original_size)
    new_size = tuple((original_size * scale).astype(int))
    image = image.resize(new_size, PIL.Image.LANCZOS)
    image = np.array(image) / 255.0
    image = image.astype(np.float32)
    return image[np.newaxis, ...]

def save_image(image, output_path):
    image = tf.squeeze(image)
    image = tf.clip_by_value(image, 0.0, 1.0)
    image = (image * 255).numpy().astype(np.uint8)
    image = PIL.Image.fromarray(image)
    image.save(output_path)

def show_image(image, title=None):
    image = tf.squeeze(image)
    image = image.numpy()
    return PIL.Image.fromarray((image * 255).astype(np.uint8))

# Load the pre-trained model from TensorFlow Hub
model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

style_images = {
    "Van Gogh - Starry Night": "van_gogh_starry_night.jpg",
    "Van Gogh - Almond Blossoms": "van_gogh_almond_blossoms.jpg",
    "Van Gogh - Irises": "van_gogh_irises.jpg",
    "Van Gogh - Wheat Field with Cypresses": "Wheat_Field_with_Cypresses.jpg",
    "Van Gogh - Wheatfield with Crows.jpg": "Wheatfield_with_Crows.jpg"
}

# Streamlit app
st.title("Style Transfer App")
st.write("Upload an image and choose a style to see it transformed!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Select style
style_choice = st.radio("Choose a style", list(style_images.keys()))

if uploaded_file is not None:
    content_image = PIL.Image.open(uploaded_file)
    content_image = load_image(content_image)

    if style_choice:
        style_image_path = style_images[style_choice]
        style_image = PIL.Image.open(style_image_path)
        style_image = load_image(style_image)

        # Apply style transfer
        stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]

        # Display the stylized image
        st.image(show_image(stylized_image), caption='Stylized Image', use_column_width=True)

        # Provide an option to download the image
        img_byte_arr = io.BytesIO()
        show_image(stylized_image).save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        st.download_button(label='Download Image', data=img_byte_arr, file_name='stylized_image.png', mime='image/png')
