
# Django imports
from django.test import TestCase

# GpmChatGpt imports
from chatgpt.libs import ChatGpt

class TestClassChatGpt(TestCase):
    """
    Test class for the ChatGpt class.

    @usage: python3 manage.py test chatgpt.tests.TestClassChatGpt
    """

    def setUp(self):
        """
        Setup the test.
        """
        self.chatgpt = ChatGpt(usage_name='buzz-matchmacking')
        self.assertIsNotNone(self.chatgpt)

    def test_chatgpt_constructor(self):

        """
        Test the ChatGpt constructor.
        """
        # gptresponse = chatgpt.multiple_message(messages=[
        #     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        #     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        # ])
        # print (gptresponse)

    # def test_chatgpt_create_assistant(self):
    #     """
    #     Test the create_assitant method.
    #     """
    #     assistant = self.chatgpt.create_assitant(
    #         instructions="You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
    #         name="Math Tutor",
    #     )
    #     self.chatgpt.send_message(
    #         message="What is the square root of 16?",
    #         assistant_id=assistant.id,
    #     )

    def test_send_message(self):
        """
        Test the send_message method.
        """
        response = self.chatgpt.send_message(
            message="What is the square root of 16?",
        )
        # self.assertIsNotNone(response)