import gradio as gr
from app import get_response
import json
import os

with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "branding.json"))) as f:
    brand_info = json.load(f)["brand"]

with gr.Blocks(theme="default", title=brand_info["organizationName"]) as app:
    # Centered Logo
    gr.HTML(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        <img src="{brand_info['logo']['title']}" alt="{brand_info['organizationName']} Logo" style="height: 300px;">
    </div>
    """)
    
    # Centered Slogan
    gr.HTML(f"""
    <h3 style="text-align:center; margin-top:-20px;">{brand_info['slogan']}</h3>
    """)

    gr.ChatInterface(
        fn=get_response,
        chatbot=gr.Chatbot(
            height=500,
            avatar_images=(None, brand_info["chatbot"]["avatar"]),
            type="messages"
        ),
        title=brand_info["organizationName"],
        description=None,  # remove default description
        type="messages",
        examples=[
            ["What is zoo?"],
            ["Can you explain a role of a zookeeper?"],
            ["How to maintain a zoo?"],
            ["which is the biggest zoo in india?"]
        ]
    )

if __name__ == "__main__":
    app.launch()
