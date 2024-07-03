
# Django Imports
from django.conf import settings

# Openai Imports
from openai import OpenAI


class ChatGpt:
    """
    ChatGpt class.

    @lexique: 
        usage_name: The name of the usage in the settings.py file.
    """

    def __init__(self, usage_name=None) -> None:
        """
        ChatGpt constructor.
        """
        self.api_token = self.__load_api_token(usage_name)
        self.client = OpenAI(
            # organization=self.api_token['organization'],
            # project=self.api_token['project'],
            api_key=self.api_token['api_key']
        )

    def __load_api_token(self, usage_name):
        """
        Load the api token.
        """
        if not hasattr(settings, 'CHATGPT_CONFIG_LIST'):
            raise Exception("CHATGPT_CONFIG_LIST is not defined in the settings.py file.")
        
        if settings.CHATGPT_CONFIG_LIST.get(usage_name) is None:
            raise Exception(f"Token name {usage_name} is not defined in the settings.py file.")
        
        return settings.CHATGPT_CONFIG_LIST.get(usage_name)
    
    def create_assitant(
            self, 
            instructions=None, 
            name=None, 
            tools=[{"type": "code_interpreter"}], 
            model="gpt-4-turbo"
        ):
        """
        Create an assistant.

        @params:
            name: The name of the assistant.
            description: The description of the assistant.
        """
        my_assistant = self.client.beta.assistants.create(
            instructions=instructions,
            name=name,
            tools=[{"type": "code_interpreter"}],
            model="gpt-4-turbo",
        )
        return my_assistant

    def send_message(self, message, assistant_id):
        """
        Send a message to the assistant.
        """
        thread = self.client.beta.threads.create()
        message = self.client.beta.threads.messages.create(
            # assistant_id=assistant_id,
            thread_id=thread.id,
            role="user",
            content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
        )
        for message in thread.messages:
            print(message.role, message.content)


    def multiple_message(self, messages):
        """
        Get the response from the GPT.

        @params: 
            messages: The list of messages.
                @example: 
                    [
                        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
                    ]
        """
        # completion = self.client.ChatCompletion.create(
        #     model="gpt-4",
        #     messages=messages
        # )
        # return completion.choices[0].message

    def multiple_autocomplete(self, messages):
        """
        Autocomplete the message.

        @params:
            messages: The list of messages.
                @example:
                    [
                        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
                    ]
        """
        completion = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
        )

        return completion.choices[0].message
    
    def assistants_list(self, order="desc", limit="20"):
        """
        Get the list of assistants.
        """
        assistants = self.client.beta.assistants.list(
            order=order,
            limit=limit,
        )
        return assistants