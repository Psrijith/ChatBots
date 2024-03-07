 
### FREE API ### 
Gemini API: Quickstart with Python 

bookmark_border
Run in Google Colab
View source on GitHub
This quickstart demonstrates how to use the Python SDK for the Gemini API, which gives you access to Google's Gemini large language models. In this quickstart, you will learn how to:

Set up your development environment and API access to use Gemini.
Generate text responses from text inputs.
Generate text responses from multimodal inputs (text and images).
Use Gemini for multi-turn conversations (chat).
Use embeddings for large language models.
Prerequisites
You can run this quickstart in Google Colab, which runs this notebook directly in the browser and does not require additional environment configuration.

Alternatively, to complete this quickstart locally, ensure that your development environment meets the following requirements:

Python 3.9+
An installation of jupyter to run the notebook.
Setup
Install the Python SDK
The Python SDK for the Gemini API, is contained in the google-generativeai package. Install the dependency using pip:


pip install -q -U google-generativeai
Import packages
Import the necessary packages.


import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Used to securely store your API key
from google.colab import userdata
Setup your API key
Before you can use the Gemini API, you must first obtain an API key. If you don't already have one, create a key with one click in Google AI Studio.

Get an API key

In Colab, add the key to the secrets manager under the "🔑" in the left panel. Give it the name GOOGLE_API_KEY.

Once you have the API key, pass it to the SDK. You can do this in two ways:

Put the key in the GOOGLE_API_KEY environment variable (the SDK will automatically pick it up from there).
Pass the key to genai.configure(api_key=...)

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)
List models
Now you're ready to call the Gemini API. Use list_models to see the available Gemini models:

gemini-pro: optimized for text-only prompts.
gemini-pro-vision: optimized for text-and-images prompts.

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)
Note: For detailed information about the available models, including their capabilities and rate limits, see Gemini models. There are options for requesting rate limit increases. The rate limit for Gemini-Pro models is 60 requests per minute (RPM).
The genai package also supports the PaLM family of models, but only the Gemini models support the generic, multimodal capabilities of the generateContent method.

Generate text from text inputs
For text-only prompts, use the gemini-pro model:


model = genai.GenerativeModel('gemini-pro')
The generate_content method can handle a wide variety of use cases, including multi-turn chat and multimodal input, depending on what the underlying model supports. The available models only support text and images as input, and text as output.

In the simplest case, you can pass a prompt string to the GenerativeModel.generate_content method:


%%time
response = model.generate_content("What is the meaning of life?")

CPU times: user 110 ms, sys: 12.3 ms, total: 123 ms
Wall time: 8.25 s
In simple cases, the response.text accessor is all you need. To display formatted Markdown text, use the to_markdown function:


to_markdown(response.text)
