"""
Gradio UI for the Customer Support Chatbot.
"""

import gradio as gr
from src.config import APP_TITLE, APP_DESCRIPTION, get_logger
from src.prompts import WELCOME_MESSAGE

logger = get_logger(__name__)

# Custom CSS
custom_css = """
.gradio-container {
    max-width: 800px !important;
    margin: auto !important;
}
.chat-header {
    text-align: center;
    padding: 20px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 10px;
    margin-bottom: 20px;
}
"""

def create_chat_interface(chat_handler):
    """
    Create the Gradio chat interface.
    """

    with gr.Blocks(title=APP_TITLE) as demo:

        # Header
        gr.HTML(f"""
            <div class="chat-header">
                <h1>🖥️ {APP_TITLE}</h1>
                <p>{APP_DESCRIPTION}</p>
            </div>
        """)

        # ✅ Chatbot (Gradio 4.x messages format)
        chatbot = gr.Chatbot(
            value=[{"role": "assistant", "content": WELCOME_MESSAGE}],
            height=500,
            show_label=False
        )

        # Input row
        with gr.Row():
            msg = gr.Textbox(
                placeholder="Type your message here...",
                show_label=False,
                scale=9,
                container=False,
            )
            submit_btn = gr.Button("Send", variant="primary", scale=1)

        # Clear chat
        clear_btn = gr.Button("🗑️ Clear Chat", size="sm")

        # Examples
        gr.Examples(
            examples=[
                "What products do you have?",
                "Show me all monitors",
                "Search for wireless printer",
                "I want to place an order",
            ],
            inputs=msg,
            label="Try these examples:",
        )

        # ===================== ACTIONS =====================

        async def respond(message: str, history: list):
            if not message or not message.strip():
                return "", history

            logger.info(f"ui_message_received: {message[:50]}")

            # Append user message
            history = history + [{"role": "user", "content": message}]

            try:
                # Call backend handler
                response = await chat_handler(message, history)

                history = history + [
                    {"role": "assistant", "content": response}
                ]

                logger.info(f"ui_response_sent: {len(response)} chars")

            except Exception as e:
                logger.error(f"ui_error: {str(e)}")
                history = history + [
                    {
                        "role": "assistant",
                        "content": "⚠️ Sorry, something went wrong. Please try again."
                    }
                ]

            return "", history

        def clear_chat():
            logger.info("ui_chat_cleared")
            return [{"role": "assistant", "content": WELCOME_MESSAGE}]

        # ===================== EVENTS =====================

        msg.submit(respond, [msg, chatbot], [msg, chatbot])
        submit_btn.click(respond, [msg, chatbot], [msg, chatbot])
        clear_btn.click(clear_chat, None, chatbot)

    return demo


def launch_ui(demo, share=False):
    """
    Launch the Gradio interface.
    """
    logger.info(f"ui_launching (share={share})")

    demo.queue()   # ✅ REQUIRED for async
    demo.launch(css=custom_css, share=share)

