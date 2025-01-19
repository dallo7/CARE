import streamlit as st

cntx = """ You are an AI developed to enhance democratic processes by ensuring the accuracy and validity of information. Your primary task is to fact-check and verify the authenticity of various types of content, including text, images, and links. This project aims to combat misinformation and promote informed decision-making among the public. """
const = """ - Ensure that all sources used for verification are reputable and trustworthy. - Maintain a neutral and unbiased tone in your analysis. - Clearly indicate any uncertainties or limitations in your findings. - Provide actionable recommendations for further verification if needed. """
exa = """ - **Example 1: Text Verification** - **Input:** "The Eiffel Tower is located in Berlin." - **Output:** The statement "The Eiffel Tower is located in Berlin" is false. The Eiffel Tower is located in Paris, France. [Source: Wikipedia] - **Example 2: Image Verification** - **Input:** [Image of the Eiffel Tower] - **Output:** The provided image is an authentic photograph of the Eiffel Tower in Paris, France. [Source: Reverse Image Search] - **Example 3: Link Verification** - **Input:** [URL to a website claiming the Eiffel Tower is in Berlin] - **Output:** The website claiming the Eiffel Tower is in Berlin contains false information. The Eiffel Tower is located in Paris, France. [Source: Official Eiffel Tower Website] """

op = "Optional"
req = "Required!"


def main():
    st.title("AI Prompt Generator using CARE Method")
    st.write(
        f"Craft effective prompts for AI tools using the CARE method. Fill in the fields below and get a ready-to-use prompt!\n\n The Context, Constrains and Examples have been pre-filled. What is required is Your request!" )

    context = st.text_area("C - Provide Context", "",
                           placeholder=f"**{op}** The context has been pre-filled. Please add any additional details if necessary")
    ask = st.text_area(
        "A - Make the Request",
        "",
        placeholder=f"**{req}**Define what you want done an format of the output",
        # required=True
    )
    constraints = st.text_area(
        "R - Constrain AI",
        "",
        placeholder=f"**{op}**The rules have been pre-filled. Please add any additional details if necessary"
    )
    examples = st.text_area(
        "E - Provide Examples",
        "",
        placeholder=f"**{op}**The examples have been pre-filled. Please add any additional details if necessary"
    )

    prompt = f" Context: **{cntx}**\n *{context}*\n\n Request: *{ask}*\n\n\n Constraints: **{const}**\n *{constraints}*\n\n Examples: **{exa}**\n *{examples}*"
    st.subheader("Generated Prompt")
    st.code(prompt, language="markdown")

    if st.button("Copy to Clipboard"):
        st.write("Copy the text below and use it in your AI tool.")
        st.code(prompt, language="markdown")

    st.write(
        "\nUse this prompt in tools like [Hugging Face Chat](https://huggingface.co/chat) or [ChatGPT](https://chat.openai.com/) or [Gemini](https://gemini.com/) for better outputs!")


if __name__ == "__main__":
    main()
