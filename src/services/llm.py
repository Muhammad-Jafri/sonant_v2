import openai


class LLMService:
    def __init__(self, model_name: str = "gpt-3.5-turbo"): #TODO pass api key here
        """
        Initializes the LLMService with the specified OpenAI model.

        Parameters:
        model_name (str): The name of the OpenAI model to use. Defaults to 'gpt-3.5-turbo'.
        """
        self.model_name = model_name

    def answer_query(self, query: str) -> str:
        """
        Sends a query to the OpenAI model and returns the response.

        Parameters:
        query (str): The input query to be answered by the model.

        Returns:
        str: The model's response to the query.
        """
        try:
            response = openai.ChatCompletion.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": query}
                ]
            )
            # Extract and return the response text
            return response["choices"][0]["message"]["content"].strip()
        except Exception as e:
            return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    service = LLMService()
    response = service.answer_query("What is the capital of France?")
    print(response)