# LangChain API Demo

This folder contains a small end-to-end example of how to connect a FastAPI backend to a Streamlit frontend using LangChain and LangServe.

## What the files do

### `app.py`

This is the backend API server.

- It creates a FastAPI application.
- It loads environment variables from a `.env` file.
- It configures OpenAI and LangChain credentials.
- It exposes LangChain routes with `langserve.add_routes()`.
- It defines a simple prompt that asks the model to write a poem about a topic in two paragraphs.

Two routes are added:

- `/llm/openai` - exposes the raw `ChatOpenAI` model.
- `/llm/res/openai` - exposes the prompt plus model chain that generates the final response.

When you run this file, the API starts on `http://localhost:8800`.

### `client.py`

This is the frontend app built with Streamlit.

- It shows a small page title.
- It gives the user a text box to type a topic.
- It sends that topic to the FastAPI server using `requests.post()`.
- It displays the response returned by the model.

In simple terms, this file is the user interface, and `app.py` is the brain that talks to the language model.

## How it works

1. You start the FastAPI server from `app.py`.
2. You start the Streamlit app from `client.py`.
3. You type a topic such as `nature`, `friendship`, or `technology`.
4. The Streamlit app sends the topic to the API.
5. The API sends the topic to OpenAI through LangChain.
6. The generated poem is returned and shown on the page.

## Requirements

Make sure the required packages are installed. The exact packages should be listed in `requirement.txt`.

You also need a `.env` file with your API keys, such as:

```env
OPENAI_API_KEY=your_openai_key_here
LANGCHAIN_API_KEY=your_langchain_key_here
```

## How to run

### 1. Start the API server

Run the backend from this folder:

```bash
python app.py
```

The server should start on port `8800`.

### 2. Start the Streamlit client

In another terminal, run:

```bash
streamlit run client.py
```

### 3. Test it

Type a topic into the input box and wait for the poem response.

## Learning notes

- `FastAPI` is used to build the backend API.
- `Streamlit` is used to build the simple user interface.
- `LangChain` helps structure the prompt and model call.
- `LangServe` turns the LangChain chain into API endpoints.
- `requests` is used in the client to send data to the backend.

## 📄 Contact

Developed by [Asad Hussain](mailto:techie.asad.dev@gmail.com).  
- **GitHub**: [@snackoverflowasad](https://github.com/snackoverflowasad)  
- **LinkedIn**: [Asad Hussain](https://www.linkedin.com/in/asad-hussain-765502319/)  
- **Portfolio**: [asadhussain.in](https://www.asadhussain.in/)

