import os
import openai

# Charger la clé API à partir des variables d'environnement
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Une erreur s'est produite : {e}"

if __name__ == "__main__":
    print("Bienvenue sur le chatbot GPT! Tapez 'quit', 'exit' ou 'bye' pour terminer la conversation.")
    while True:
        user_input = input("vous: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("chatbot: Au revoir!")
            break

        response = chat_with_gpt(user_input)
        print("chatbot:", response)

