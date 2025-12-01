from PIL import Image
import streamlit as st

st.header("Image Editing")
image = Image.open("range_rover.jpg")
st.image(image, caption="Range Rover")

# Rotate image
st.title("Rotate Image")
angle = st.selectbox("Select rotation angle", [0,45, 90, 180, 270, 360])
if angle != 0:
    rotated_image = image.rotate(-angle, expand=True)  # Negative for clockwise
    st.image(rotated_image, caption=f"Rotated {angle}°")
else:
    st.info("Select an angle to rotate the image.")


# Apply flip on image
st.title("Flipping the Image")
flip_option = st.selectbox(
    "Select flip mode",
    ["None", "Left to Right", "Top to Bottom", "Transpose"]
)
if flip_option == "Left to Right":
    flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    st.image(flipped_image, caption="Flipped Left to Right")
elif flip_option == "Top to Bottom":
    flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    st.image(flipped_image, caption="Flipped Top to Bottom")
elif flip_option == "Transpose":
    flipped_image = image.transpose(Image.TRANSPOSE)
    st.image(flipped_image, caption="Transposed (Diagonal Flip)")
else:
    st.info("Select a flip mode to see the result.")

st.title("Resize the Image")
st.write(f"Original size: {image.size[0]} x {image.size[1]} (width x height)")
# Resize controls using input boxes
st.subheader("Resize Image Using Width and Height")
# Input boxes for dimensions
width = st.number_input("Enter new width (px):", min_value=1, value=image.size[0])
height = st.number_input("Enter new height (px):", min_value=1, value=image.size[1])
# Resize and display
if st.button("Resize Image"):
    resized_image = image.resize((int(width), int(height)))
    st.image(resized_image, caption=f"Resized to {width} x {height}")


from PIL import Image, ImageFilter
# Apply Filters to Range Rover Image
st.title("Apply Filters to Image")
st.subheader("Select a Filter to Apply")
filter_option = st.selectbox(
    "Choose a filter",
    [
        "None",
        "BLUR",
        "CONTOUR",
        "DETAIL",
        "EDGE_ENHANCE",
        "EDGE_ENHANCE_MORE",
        "EMBOSS",
        "SHARPEN",
        "SMOOTH",
        "SMOOTH_MORE"
    ]
)
# Apply selected filter
filtered_image = image
if filter_option != "None":
    filter_map = {
        "BLUR": ImageFilter.BLUR,
        "CONTOUR": ImageFilter.CONTOUR,
        "DETAIL": ImageFilter.DETAIL,
        "EDGE_ENHANCE": ImageFilter.EDGE_ENHANCE,
        "EDGE_ENHANCE_MORE": ImageFilter.EDGE_ENHANCE_MORE,
        "EMBOSS": ImageFilter.EMBOSS,
        "SHARPEN": ImageFilter.SHARPEN,
        "SMOOTH": ImageFilter.SMOOTH,
        "SMOOTH_MORE": ImageFilter.SMOOTH_MORE
    }
    filtered_image = image.filter(filter_map[filter_option])
    st.image(filtered_image, caption=f"{filter_option} Filter Applied", use_container_width=True)
else:
    st.info("Select a filter to apply to the image.")

from PIL import Image, ImageEnhance
st.title("Enhance Image")
# Sliders for enhancements
color_factor = st.slider("Color", min_value=0.0, max_value=3.0, value=1.0, step=0.1)
contrast_factor = st.slider("Contrast", min_value=0.0, max_value=3.0, value=1.0, step=0.1)
brightness_factor = st.slider("Brightness", min_value=0.0, max_value=3.0, value=1.0, step=0.1)
sharpness_factor = st.slider("Sharpness", min_value=0.0, max_value=3.0, value=1.0, step=0.1)
# Apply enhancements
enhanced_image = ImageEnhance.Color(image).enhance(color_factor)
enhanced_image = ImageEnhance.Contrast(enhanced_image).enhance(contrast_factor)
enhanced_image = ImageEnhance.Brightness(enhanced_image).enhance(brightness_factor)
enhanced_image = ImageEnhance.Sharpness(enhanced_image).enhance(sharpness_factor)
# Display enhanced image
st.image(enhanced_image, caption="Enhanced Image", use_container_width=True)


# Black and white image
st.title("Black and white Image")
st.image(image.convert("1"))