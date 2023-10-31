# HLD: Chat AI Firefox Add-ons Discovery Feature

## Overview

The HLD showcases the process of assisting Firefox users in discovering and installing browser extensions using the AI-powered Chatbot Discovery Tool. The system is divided into distinct components, each serving a specific function, ensuring users have a smooth and interactive experience while searching for browser extensions.

## High-Level Design Diagram

![High-Level Design Diagram](/static/images/HLD_Mozilla.jpg)

## Components and Their Functions:

### Firefox Users:

- The primary user interface where users interact with the system.
- Users can describe the extensions they are looking for and get extension suggestions based on their inputs.
- Users can send installation requests and receive installation confirmations.

### Extension Installer:

- Responsible for installing the suggested extensions to the user's browser.
- Sends installation confirmations to users.

### Mozilla Chatbot Discovery Tool:

- Acts as the middle-man between users and the backend AI system.
- Receives user's extension description and forwards it to the AI web service for processing.
- Retrieves extension suggestions from the AI web service and sends them to users.

### LLM Based AI Web Service:

- The AI backend responsible for processing user inputs and recommending extensions.
- Analyzes user's description of the required extension.
- Fetches matching extensions from the database repository using LLM (Language Model).
- Returns the best matching extension suggestions to the Chatbot Discovery Tool.

### Extension DB Interface:

- An interface between the Firefox extension database repository and the LLM Based AI Web Service.
- Pulls extension data used to train the LLM.

### Firefox Extension DB Repository:

- A database storing Firefox extension data.
- This data is used by LLM for processing and suggesting extensions to users.

## Data Flow:

1. Users describe their required extension to the Chatbot Discovery Tool.
2. The Chatbot Discovery Tool sends the user's description to the LLM Based AI Web Service for processing.
3. The AI Web Service interacts with the Extension DB Interface to fetch and analyze extension data.
4. The AI Web Service sends extension suggestions back to the Chatbot Discovery Tool.
5. The Chatbot Discovery Tool provides the user with the suggested extensions.
6. Users can send an installation request for a specific extension.
7. The Extension Installer handles the installation process and sends back an installation confirmation to the user.
