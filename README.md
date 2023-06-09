# Todo List API with Langchain

## Introduction

This project presents a simple Todo List API that is developed with FastAPI and Langchain. FastAPI is a modern and fast web framework for Python, while Langchain provides an API based on OpenAI's GPT-4 model.

## Features

**Adding Todos:** Users can add new Todos to the list. Once a Todo is created, an email notification is sent in the background.

**Reading Todos:** Users can view the entire Todo list or fetch details of a specific Todo. There is also a filtering option that allows users to view completed or incomplete tasks separately.

**Updating Todos:** Each Todo in the list can be updated based on its unique ID.

**Deleting Todos:** Users can remove a Todo from the list using its unique ID.

**OpenAPI Documentation:** The API provides an endpoint for fetching the OpenAPI documentation in YAML format.

The project demonstrates a practical application of integrating a natural language model (Langchain) with a web application to handle user requests.

The App is also deployed on Deta Space. For more information, look here: https://deta.space/