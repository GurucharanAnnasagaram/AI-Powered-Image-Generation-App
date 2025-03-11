Project Overview
📌 Objective:
To build a Streamlit-based AI Image Generator that enables users to convert text prompts into images using DALL·E and Stable Diffusion.

📌 Key Features:
✅ Dual AI Model Selection – Users can choose between DALL·E (OpenAI) and Stable Diffusion (Hugging Face Diffusers).
✅ Text-to-Image Generation – Converts user-provided text prompts into AI-generated images.
✅ User-Friendly UI – Built with Streamlit, offering a simple and intuitive interface.
✅ CUDA Acceleration – Uses GPU for faster image generation with Stable Diffusion.
✅ Expandable Design – Can integrate new AI models in the future.

Technology Stack
Streamlit – For interactive UI.
OpenAI API (DALL·E) – Generates images from text prompts.
Hugging Face Diffusers (Stable Diffusion) – AI-powered image synthesis.
Torch (PyTorch) – For efficient GPU-based processing.
dotenv – Securely loads API keys.
How It Works
🔹 User selects AI model – Chooses between DALL·E or Stable Diffusion.
🔹 Enter a text prompt – Users provide a description of the image they want to generate.
🔹 AI Model processes the input –

DALL·E calls OpenAI’s API to generate an image.
Stable Diffusion runs a deep learning pipeline on GPU to create an image.
🔹 Generated Image is displayed – The app presents the AI-created image with a caption.
Use Cases
✅ Art & Design Inspiration – AI-generated images for creative projects.
✅ Marketing & Advertising – Quick visual content generation for campaigns.
✅ AI Research & Development – Experiment with text-to-image AI models.
✅ Content Creation – Create unique visuals for blogs, social media, or videos.
