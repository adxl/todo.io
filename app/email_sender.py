class EmailSender:
    @staticmethod
    def send(recipeint):
        message = f"Email sent to {recipeint} successfully !"
        raise NotImplementedError(message)
