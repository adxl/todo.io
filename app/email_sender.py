class EmailSender:
    @staticmethod
    def send(recipeint):
        """Send an email to a customer"""

        message = f"Email sent to {recipeint} successfully !"
        raise NotImplementedError(message)
